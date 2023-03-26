from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from database import getDB
from models import LoginData as Model
from schemas import LoginData
from sqlalchemy.orm import Session
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserValidation(LoginData):
    pass
    class Config:
        orm_mode = True

__SECRET_KEY = "e06d1c3cff8a63fa08adc863b66d18c62ad06cd8eab65f51b41ab603c047dfaf"
__ALGORITHM = "HS256"
__PWD_CONTEXT = CryptContext(schemes = ["bcrypt"], deprecated= "auto")
__OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl = "token")

def __get_password_hash(password):
    return __PWD_CONTEXT.hash(password)

def __verify_password(plain_password, hashed_password):
    return __PWD_CONTEXT.verify(plain_password, hashed_password)

def __get_user(username: str, db: Session):
    user = db.query(Model).filter(Model.login == username).first()
    if user is None:
        raise HTTPException(status_code = 404, detail = "User not found")
    return user

async def __get_current_user(token: str = Depends(__OAUTH2_SCHEME), db: Session = Depends(getDB)):
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
def create_user(db: Session, user: LoginData):
    db_user = db.query(Model).filter(Model.login == user.login).first()
    if db_user:
        raise HTTPException(status_code = 400, detail="Email already in use")
    hashed_password = __get_password_hash(user.password)
    db_user = Model(login = user.login, password = hashed_password, id_employee = user.id_employee)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = __get_user(db = db, username = username)
    if user is None or __verify_password(password, user.password) is None:
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update( { "exp": expire } )
    encoded_jwt = jwt.encode(to_encode, __SECRET_KEY, algorithm = __ALGORITHM)
    return encoded_jwt

async def get_current_active_user(current_user: LoginData = Depends(__get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code = 400, detail = "Inactive user")
    return current_user

def getAccessTokenExpireMinutes():
    return ACCESS_TOKEN_EXPIRE_MINUTES