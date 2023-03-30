from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/category", tags=["category"])

@router.get("/", response_model = list[schemas.Category])
def read_category(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    category = CRUD.getCategory(db, skip, limit)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/", response_model= schemas.CategoryCreate, status_code=201)
def create_category(name: schemas.CategoryCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    category = read_category(db = db)
    if name in category:
        raise HTTPException(status_code=400, detail="Category existed")
    return CRUD.createCategory(db = db, category=name)

@router.patch("/{category_id}", response_model= schemas.CategoryUpdate, status_code=200)
def update_category(category_id: int, category: schemas.CategoryUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.updateCategory(db = db, category = category, category_id = category_id)

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    category = CRUD.getCategoryById(db,category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return CRUD.delCategory(db = db, category = category)