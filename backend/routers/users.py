from datetime import timedelta
from fastapi import Depends,APIRouter,HTTPException,status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from models import schemas
from authorization.auth import get_current_active_user, create_access_token, Token, authenticate_user, getAccessTokenExpireMinutes, create_user
from dependencies import getDB
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def read_users(current_user: schemas.LoginData = Depends(get_current_active_user)):
    return current_user

@router.post("/create")
def create_user_account(user: schemas.LoginData, db: Session = Depends(getDB)):
    created_user = create_user(db = db, user = user)
    token_data = {"sub": jsonable_encoder(created_user)}
    access_token = create_access_token(token_data)
    return Token(access_token = access_token, token_type = "bearer")

@router.post("/token", response_model = Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(getDB)):
    user = authenticate_user(db = db, username = form_data.username, password = form_data.password)
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