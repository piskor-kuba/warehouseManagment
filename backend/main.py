from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import CRUD
import models
import schemas
from database import getDB, engine
import auth

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


@app.post("/api/users/")
async def create_user(user: schemas.AccountCreate, db: Session = Depends(getDB)):
    db_user = await auth.get_user_by_login(db, user.login)
    if db_user:
        raise HTTPException(status_code = 400, detail = "Email already in use")
    user = await auth.create_user(db, user)
    return await auth.create_token(user)


@app.post("/api/token/")
async def generate_token( form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(getDB)):
    user = await auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code = 401, detail = "Invalid Credentials")
    return await auth.create_token(user)

@app.get("/api/users/myprofile/", response_model = schemas.LoginData)
async def get_user(user: schemas.LoginData = Depends(auth.get_current_user)):
    return user