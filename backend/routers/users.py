from datetime import timedelta
from fastapi import Depends,APIRouter,HTTPException,status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from models import schemas
from authorization.auth import get_current_active_user, create_access_token, Token, Otp,authenticate_user, getAccessTokenExpireMinutes, create_user, send_otp_code, get_user
from dependencies import getDB
from sqlalchemy.orm import Session
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def read_users(current_user: str = Depends(get_current_active_user)):
    return current_user

@router.post("/create", status_code=201)
def create_user_account(user: schemas.CreateUser, db: Session = Depends(getDB)):
    created_user = create_user(db = db, user = user)
    return created_user

@router.post("/token", response_model = Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(getDB)):
    user = authenticate_user(db = db, username = form_data.username, password = form_data.password, otp_code=form_data.client_secret)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password",
            headers = {"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes = getAccessTokenExpireMinutes())
    access_token = create_access_token(data = {"sub": user.login}, expires_delta=access_token_expires)
    token = Token( access_token = access_token, token_type =  "bearer")
    return token

@router.post("/OTP_code", status_code=200)
def OTP_code(data: Otp, db: Session = Depends(getDB)):
    code = send_otp_code(db, data.username, data.password)
    if code is False:
        raise HTTPException(status_code=404, detail="Incorrect username or password")

