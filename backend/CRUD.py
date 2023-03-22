from sqlalchemy.orm import Session
import models
import schemas

def createCategory(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name = category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def getCategory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def createProduct(db: Session, product: schemas.ProductCreate, categoryId:int):
    db_product = models.Category(id_category = categoryId, name = product.name, describe = product.describe)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def getProduct(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


