from sqlalchemy.orm import Session
from models import schemas
from database import models


##################################################__CATEGORY__##################################################
def createCategory(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name = category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def getCategory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def getCategoryById(db: Session, category_id:int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

##################################################__PRODUCT__##################################################
def createProduct(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(id_category = product.id_category, name = product.name, describe = product.describe)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def getProduct(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def updateProduct(db: Session, product: schemas.ProductUpdate, product_id:int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        return None
    for key,value in vars(product).items():
        setattr(db_product,key,value) if value else None

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product



##################################################__PRODUCT-AMOUNT__##################################################
def getProductAmount(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductAmount).offset(skip).limit(limit).all()

def createProductAmount(db: Session, product: schemas.ProductAmountCreate):
    db_product_amount = models.Product(id_product=product.id_product, name=product.amount)
    db.add(db_product_amount)
    db.commit()
    db.refresh(db_product_amount)
    return db_product_amount

##################################################__PERSONS__##################################################
def getPersons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Persons).offset(skip).limit(limit).all()

def getPersonById(db: Session, person_id:int):
    return db.query(models.Persons).filter(models.Persons.id == person_id).first()

def createPerson(db: Session, person: schemas.PersonsCreate):
    db_person = models.Persons(name = person.name, surname = person.surname, phone = person.phone, address = person.address)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)

##################################################__CLIENTS__##################################################
def getClients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Clients).offset(skip).limit(limit).all()

def getClientById(db: Session, client_id:int):
    return db.query(models.Clients).filter(models.Clients.id == client_id).first()
def createClient(db: Session, client: schemas.ClientCreate):
    db_client = models.Clients(id_persons = client.id_persons, amount = client.amount)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

##################################################__CLIENT-PRODUCT__##################################################
def getClientProduct(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ClientProduct).offset(skip).limit(limit).all()

def createClientProduct(db: Session, client_product: schemas.ClientProductCreate):
    db_client_product = models.ClientProduct(id_client = client_product.id_client, id_product = client_product.id_product)
    db.add(db_client_product)
    db.commit()
    db.refresh(db_client_product)
    return db_client_product

##################################################__WORKPLACE__##################################################
def getWorkplace(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Workplace).offset(skip).limit(limit).all()

##################################################__ROLE__##################################################
def getRole(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()

##################################################__EMPLOYEES__##################################################
def getEmployees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employees).offset(skip).limit(limit).all()
