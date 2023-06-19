from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from dependencies import getDB
from database.models import LoginData as Model
from models.schemas import LoginData, CreateUser
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .F2A import totp_generate, totp_verify, release_otp
import re
from .authAttemptBlocker import AuthAttemptBlocker
from configuration.config import Authorization
"""
auth.py
==========================
The module contains functions and variables needed to perform user authentication 
"""

class Token(BaseModel):
    access_token: str
    token_type: str

class Otp(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    username: str | None = None

config = Authorization()

__SECRET_KEY = config.key
__ALGORITHM = config.algorithm
__PWD_CONTEXT = CryptContext(schemes = ["bcrypt"], deprecated= "auto")

__OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl = "users/token")
__AUTH_ATTEMPT_BLOCKER = AuthAttemptBlocker()

def __get_password_hash(password):
    """
    Generates a hashed password using the password hashing context.

    Args:
        password (str): Plain-text password.

    Returns:
        str: Hashed password.

    """
    return __PWD_CONTEXT.hash(password)

def __verify_password(plain_password, hashed_password):
    """
    Verifies if the plain password matches the hashed password.

    Args:
        plain_password (str): Plain-text password.
        hashed_password (str): Hashed password.

    Returns:
        bool: True if the passwords match, False otherwise.

    """
    return __PWD_CONTEXT.verify(plain_password, hashed_password)

def __verify_email(email):
    """
    Verifies if the email address is valid.

    Args:
        email (str): Email address to verify.

    Returns:
        bool: True if the email is valid, False otherwise.

    """
    regex = re.compile(rf'{config.emailRegex}')
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def __get_user(username: str, db: Session):
    """
    Retrieves a user from the database based on the username.

    Args:
        username (str): Username of the user to retrieve.
        db (Session): Database session.

    Returns:
        Model: User model object if found, None otherwise.

    """
    user = db.query(Model).filter(Model.login == username).first()
    if user is None:
        return
    return user

async def __get_current_user(token: str = Depends(__OAUTH2_SCHEME), db: Session = Depends(getDB)):
    """
    Retrieves the current user based on the provided token.

    Args:
        token (str): Authentication token.
        db (Session): Database session.

    Returns:
        User: Current user if authenticated.

    Raises:
        HTTPException: If the token is invalid or the user is not found.

    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,__SECRET_KEY, algorithms=[__ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username = username)
    except JWTError:
        raise credentials_exception
    user = __get_user(db = db, username = token_data.username)

    if user is None:
        raise credentials_exception
    return user

#public
ACCESS_TOKEN_EXPIRE_MINUTES = 30
def create_user(db: Session, user: CreateUser):
    """
    Creates a new user.

    Args:
        db (Session): Database session.
        user (CreateUser): User data to be created.

    Returns:
        str: Success message if the user is created.

    Raises:
        HTTPException: If the email is already in use or has incorrect syntax.

    """
    db_user = db.query(Model).filter(Model.login == user.login).first()
    if db_user:
        raise HTTPException(status_code = 400, detail="Email already in use")
    if not __verify_email(user.login):
        raise HTTPException(status_code=400, detail="Incorrect syntax of email address")
    hashed_password = __get_password_hash(user.password)
    db_user = Model(login = user.login, password = hashed_password, id_employee = user.id_employee)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "New user created"

def authenticate_user(db: Session, username: str, password: str, otp_code:str):
    """
    Authenticates a user based on username, password, and OTP code.

    Args:
        db (Session): Database session.
        username (str): Username.
        password (str): Password.
        otp_code (str): OTP code.

    Returns:
        user: Authenticated user.

    Raises:
        HTTPException: If the data provided is invalid.

    """
    __AUTH_ATTEMPT_BLOCKER.block_user_if_needed(username=username, db=db)
    user = __get_user(db = db, username = username)
    if user is None or __verify_password(password, user.password) is False or totp_verify(db=db, login=username, otp_code = otp_code) is False:
        if user is not None:
            __AUTH_ATTEMPT_BLOCKER.register_failed_attempt(username= username,db = db)
        raise HTTPException(status_code=400, detail="Invalid data")
    release_otp(db=db, login=username)
    __AUTH_ATTEMPT_BLOCKER.reset_attempts(username= username,db = db)
    return user

def send_otp_code(db: Session, username: str, password: str):
    """
    Sends an OTP code to the user for authentication.

    Args:
        db (Session): Database session.
        username (str): Username.
        password (str): Password.

    Returns:
        bool: True if the OTP code is sent successfully.

    Raises:
        HTTPException: If the login or password is invalid.

    """
    __AUTH_ATTEMPT_BLOCKER.block_user_if_needed(username=username, db=db)
    user = __get_user(db=db, username=username)
    if user is None or __verify_password(password, user.password) is False:
        if user is not None:
            __AUTH_ATTEMPT_BLOCKER.register_failed_attempt(username= username,db = db)
        raise HTTPException(status_code=400, detail="invalid login or password")
    totp_generate(db=db, login=username)
    __AUTH_ATTEMPT_BLOCKER.reset_attempts(username = username, db = db)
    return True

def get_user(db: Session, username: str, password: str):
    """
    Retrieves the user from the database based on the provided username and password.

    Args:
        db (Session): Database session.
        username (str): Username.
        password (str): Password.

    Returns:
        Union[bool, Model]: User model if the username and password are valid, False otherwise.

    """
    user = __get_user(db=db, username=username)
    if user is None or __verify_password(password, user.password) is False:
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates an access token with the provided data.

    Args:
        data (dict): Data to be encoded in the access token.
        expires_delta (timedelta | None): Expiration time for the access token. If None, a default expiration time of 15 minutes is used.

    Returns:
        str: Encoded access token.

    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update( { "exp": expire } )
    encoded_jwt = jwt.encode(to_encode, __SECRET_KEY, algorithm = __ALGORITHM)
    return encoded_jwt

async def get_current_active_user(current_user: LoginData = Depends(__get_current_user)):
    """
    Returns the login of the current active user.

    Args:
        current_user (LoginData): Current authenticated user.

    Raises:
        HTTPException: If the user is inactive.

    Returns:
        str: Login of the current active user.

    """
    if current_user.disabled:
        raise HTTPException(status_code = 400, detail = "Inactive user")
    return current_user.login

def getAccessTokenExpireMinutes():
    """
    Returns the expiration time of the access token in minutes.

    Returns:
        int: Expiration time of the access token in minutes.

    """
    return ACCESS_TOKEN_EXPIRE_MINUTES


