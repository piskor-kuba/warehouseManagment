from datetime import timedelta
from typing import Annotated
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

import CRUD
import models
import schemas
from database import getDB, engine
from auth import Token, create_user, authenticate_user, create_access_token, get_current_active_user, getAccessTokenExpireMinutes

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "test"}


@app.get("/category/", response_model = list[schemas.Category])
def read_category(skip: int = 0, limit: int = 100, db: Session = Depends(getDB)):
    category = CRUD.getCategory(db,skip,limit)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.get("/user/", response_model = list[schemas.LoginData])
def read_user(skip: int = 0, limit: int = 100, db: Session = Depends(getDB)):
    category = CRUD.get_user(db,skip,limit)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@app.post("/category/", response_model= schemas.CategoryCreate, status_code=201)
def create_category(name:schemas.CategoryCreate, db: Session = Depends(getDB)):
    category = read_category(db = db)
    if name in category:
        raise HTTPException(status_code=400, detail="Category existed")
    return CRUD.createCategory(db = db, category=name)

@app.get("/product/", response_model = list[schemas.Product])
def read_product(skip: int = 0, limit: int = 100, db: Session = Depends(getDB)):
    product = CRUD.getProduct(db,skip,limit)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/", response_model= schemas.ProductCreate, status_code=201)
def create_product(product:schemas.ProductCreate,db: Session = Depends(getDB)):
    category = CRUD.getCategoryById(category_id= product.id_category, db = db)
    if category is None :
        raise HTTPException(status_code=404, detail="Category not Found")
    return CRUD.createProduct(db = db, product = product)

@app.patch("/product/{product_id}", response_model= schemas.ProductUpdate, status_code=200)
def update_product(product_id: int, product:schemas.ProductUpdate, db: Session = Depends(getDB)):
    return CRUD.updateProduct(db = db, product = product, product_id = product_id)


@app.post("/token", response_model = Token)
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

@app.post("/api/users/", response_model = Token)
def create_user(user: schemas.LoginData, db: Session = Depends(getDB)):
    created_user = create_user(db, user)
    token_data = {"sub": jsonable_encoder(created_user)}
    access_token = create_access_token(token_data)
    return Token(access_token = access_token, token_type = "bearer")

@app.get("/users/me/", response_model = schemas.LoginData)
async def read_users_me(current_user: schemas.LoginData = Depends(get_current_active_user)):
    return current_user
