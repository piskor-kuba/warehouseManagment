from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/category/", response_model = list[schemas.Category])
def read_category(skip: int = 0, limit: int = 100, db: Session = Depends(getDB)):
    category = CRUD.getCategory(db, skip, limit)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/category/", response_model= schemas.CategoryCreate, status_code=201)
def create_category(name: schemas.CategoryCreate, db: Session = Depends(getDB)):
    category = read_category(db = db)
    if name in category:
        raise HTTPException(status_code=400, detail="Category existed")
    return CRUD.createCategory(db = db, category=name)

@router.get("/product/", response_model = list[schemas.Product])
def read_product(skip: int = 0, limit: int = 100, db: Session = Depends(getDB)):
    product = CRUD.getProduct(db, skip, limit)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/product/", response_model= schemas.ProductCreate, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(getDB)):
    category = CRUD.getCategoryById(category_id= product.id_category, db = db)
    if category is None :
        raise HTTPException(status_code=404, detail="Category not Found")
    return CRUD.createProduct(db = db, product = product)

@router.patch("/product/{product_id}", response_model= schemas.ProductUpdate, status_code=200)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(getDB)):
    return CRUD.updateProduct(db = db, product = product, product_id = product_id)