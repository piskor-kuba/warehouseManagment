from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from jwt import encode, decode
from sqlalchemy.orm import Session
import passlib.hash as hash
from schemas import AccountCreate, Account
from models import LoginData
from database import getDB

__TOKEN = OAuth2PasswordBearer(tokenUrl = "/api/token")
__SECRET = "secret"

async def get_user_by_login(db: Session, login: str):
    return db.query(LoginData).filter(LoginData.login == login).first()

async def create_user(db: Session, user: AccountCreate):
    user_obj = LoginData(login = user.login, password = hash.bcrypt.hash(user.password))
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

async def authenticate_user(db: Session, login: str, password: str):
    user = await get_user_by_login(db = db, login = login)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user

async def create_token(user: LoginData):
    user_obj = Account.from_orm(user)
    token = encode(user_obj.dict(), __SECRET)
    return dict(access_token = token, token_type = "bearer")


async def get_current_user(db: Session = Depends(getDB),token: str = Depends(__TOKEN)):
    try:
        payload = decode(token, __SECRET, algorithms = ["HS256"])
        user = db.query(LoginData).get(payload["id"])
        print(user)
    except:
        raise HTTPException(status_code = 401, detail = "Invalid Email or Password")

    return Account.from_orm(user)