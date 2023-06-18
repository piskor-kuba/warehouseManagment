from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/category", tags=["category"])

@router.get("/", response_model = list[schemas.Category])
def read_category(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a list of categories.

    Args:
        skip (int): The number of categories to skip (used for pagination).
        limit (int): The maximum number of categories to return (used for pagination).
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        List[schemas.Category]: The list of categories.

    Raises:
        HTTPException(404): If no categories are found.
    """
    category = CRUD.getCategory(db, skip, limit)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.get("/{category_id}", response_model= schemas.Category, status_code=200)
def read_category_by_id(category_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a category by its ID.

    Args:
        category_id (int): The ID of the category to retrieve.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.Category: The retrieved category.

    Raises:
        HTTPException(404): If the category is not found.
    """
    category = CRUD.getCategoryById(db=db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model= schemas.CategoryCreate, status_code=201)
def create_category(name: schemas.CategoryCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Create a new category.

    Args:
        name (schemas.CategoryCreate): The category data to be created.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.CategoryCreate: The created category.

    Raises:
        HTTPException(400): If the category already exists.
    """
    category = CRUD.createCategory(db = db, category=name)
    if category is None:
        raise HTTPException(status_code=400, detail="Category existed")
    return category

@router.patch("/{category_id}", response_model= schemas.CategoryUpdate, status_code=200)
def update_category(category_id:int, category: schemas.CategoryUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update a category by ID.

    Args:
        category_id (int): The ID of the category to be updated.
        category (schemas.CategoryUpdate): The updated category data.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.CategoryUpdate: The updated category.

    Raises:
        HTTPException(400): If the category with the specified ID does not exist.
    """
    cat = CRUD.getCategoryById(db=db, category_id=category_id)
    if cat is None:
        raise HTTPException(status_code=400, detail="Category not existed")
    return CRUD.updateCategory(db = db, category = category, category_id = category_id)

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Delete a category by ID.

    Args:
        category_id (int): The ID of the category to be deleted.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the category with the specified ID does not exist.
    """
    category = CRUD.getCategoryById(db,category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return CRUD.delCategory(db = db, category = category)