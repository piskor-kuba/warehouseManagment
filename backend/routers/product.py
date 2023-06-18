from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/product", tags=["product"])

@router.get("/", response_model = list[dict])
def read_product(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a list of products.

    Args:
        skip (int): Number of products to skip.
        limit (int): Maximum number of products to retrieve.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If no products are found.

    Returns:
        List[schemas.Product]: A list of products.
    """
    product = CRUD.getProduct(db, skip, limit)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/{product_id}", response_model= dict, status_code=200)
def read_product_by_id(product_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a product by ID.

    Args:
        product_id (int): The ID of the product.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the product with the specified ID is not found.

    Returns:
        schemas.Product: The product with the specified ID.
    """
    product = CRUD.getProductById(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="product not found")
    return product

@router.get("/amount/{product_id}", response_model = schemas.ProductAmount, status_code=200)
def read_amount(product_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve the amount of a product by ID.

    Args:
        product_id (int): The ID of the product.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(200): If there is a lack of this product.

    Returns:
        schemas.ProductAmount: The amount of the product with the specified ID.
    """
    product_amount = CRUD.getProductAmountById(db=db, product_id=product_id)
    if product_amount is None:
        raise HTTPException(status_code=200, detail="lack of this product")
    return product_amount

@router.post("/", response_model= schemas.ProductCreate, status_code=201)
def create_product(product: schemas.ProductCreate, current_user: schemas.LoginData = Depends(get_current_active_user), db: Session = Depends(getDB)):
    """
    Create a new product.

    Args:
        product (schemas.ProductCreate): The data of the product to be created.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the category for the product is not found.

    Returns:
        schemas.ProductCreate: The created product.
    """
    category = CRUD.getCategoryById(category_id= product.id_category, db = db)
    if category is None :
        raise HTTPException(status_code=404, detail="Category not Found")
    pro = CRUD.createProduct(db = db, product = product)
    CRUD.createProductAmount(db = db, product = pro, amount = product.amount)
    return product

@router.patch("/{product_id}", response_model= schemas.ProductUpdate, status_code=200)
def update_product(product_id: int, product: schemas.ProductUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update a product.

    Args:
        product_id (int): The ID of the product to be updated.
        product (schemas.ProductUpdate): The updated data of the product.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the product is not found.

    Returns:
        schemas.ProductUpdate: The updated product.
    """
    pro = CRUD.getProductById(db=db, product_id=product_id)
    if pro is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return CRUD.updateProduct(db = db, product = product, product_id = product_id)

@router.patch("/amount/", response_model= schemas.ProductAmountUpdate, status_code=200)
def update_product_amount(product_amount: schemas.ProductAmountUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update the amount of a product.

    Args:
        product_amount (schemas.ProductAmountUpdate): The updated amount of the product.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the product is not found.

    Returns:
        schemas.ProductAmountUpdate: The updated product amount.
    """
    pro = CRUD.getProductAmountById(db=db, product_id=product_amount.id_product)
    if pro is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return CRUD.updateProductAmount(db = db, product_amount = product_amount, product_amount_id = pro.id)

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Delete a product.

    Args:
        product_id (int): The ID of the product to be deleted.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the product is not found.

    Returns:
        None
    """
    product = CRUD.getProductById(db,product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    CRUD.delProductAmount(db = db, product_id = product_id)
    return CRUD.delProduct(db = db, product = product)