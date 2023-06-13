from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/product", tags=["product"])

@router.get("/", response_model = list[schemas.Product])
def read_product(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    product = CRUD.getProduct(db, skip, limit)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product\

@router.get("/{product_id}", response_model= schemas.Product, status_code=200)
def read_product_by_id(product_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.getProductById(db = db, product_id = product_id)

@router.get("/amount", response_model = list[schemas.ProductAmount])
def read_amount(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    product_amount = CRUD.getProductAmount(db, skip, limit)
    if product_amount is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_amount

@router.post("/", response_model= schemas.ProductCreate, status_code=201)
def create_product(product: schemas.ProductCreate, current_user: schemas.LoginData = Depends(get_current_active_user), db: Session = Depends(getDB)):
    category = CRUD.getCategoryById(category_id= product.id_category, db = db)
    if category is None :
        raise HTTPException(status_code=404, detail="Category not Found")
    #CRUD.createProduct(db = db, product = product)
    return CRUD.createProduct(db = db, product = product) #CRUD.createProductAmount(db = db, product = pro, amount = product.amount)

@router.patch("/{product_id}", response_model= schemas.ProductUpdate, status_code=200)
def update_product(product_id: int, product: schemas.ProductUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.updateProduct(db = db, product = product, product_id = product_id)

@router.patch("/{product_id}", response_model= schemas.ProductAmountUpdate, status_code=200)
def update_product_amount(product_amount_id: int, product_amount: schemas.ProductAmountUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.updateProductAmount(db = db, product_amount = product_amount, product_amount_id = product_amount_id)

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    product = CRUD.getProductById(db,product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    CRUD.delProductAmount(db = db, product_id = product_id)
    return CRUD.delProduct(db = db, product = product)