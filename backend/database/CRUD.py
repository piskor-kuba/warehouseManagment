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

def delCategory(db: Session, category: schemas.CategoryDelete):
    db.delete(category)
    db.commit()

def updateCategory(db: Session, category: schemas.CategoryUpdate, category_id:int):
    db_category = getCategoryById(db,category_id)
    if db_category is None:
        return None
    for key,value in vars(category).items():
        setattr(db_category,key,value) if value else None

    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

##################################################__PRODUCT__##################################################
def createProduct(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(id_category = product.id_category, name = product.name, describe = product.describe)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def getProductById(db: Session, product_id:int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def getProduct(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def updateProduct(db: Session, product: schemas.ProductUpdate, product_id:int):
    db_product = getProductById(db,product_id)
    if db_product is None:
        return None
    for key,value in vars(product).items():
        setattr(db_product,key,value) if value else None

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delProduct(db: Session, product: schemas.ProductDelete):
    db.delete(product)
    db.commit()
    return product


##################################################__PRODUCT-AMOUNT__##################################################
def getProductAmount(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductAmount).offset(skip).limit(limit).all()

def createProductAmount(db: Session, product: schemas.ProductCreate):
    db_product_amount = models.ProductAmount(id_product=product.id, amount=product.amount)
    db.add(db_product_amount)
    db.commit()
    db.refresh(db_product_amount)
    return db_product_amount

def updateProductAmount(db: Session, product_amount: schemas.ProductAmountUpdate, product_amount_id:int):
    db_product_amount = db.query(models.ProductAmount).filter(models.ProductAmount.id == product_amount_id).first()
    if db_product_amount is None:
        return None
    for key,value in vars(product_amount).items():
        setattr(db_product_amount,key,value) if value else None

    db.add(db_product_amount)
    db.commit()
    db.refresh(db_product_amount)
    return db_product_amount

def delProductAmount(db: Session, product_id:int):
    db_product_amount = db.query(models.ProductAmount).filter(models.ProductAmount.id_product == product_id).first()
    db.delete(db_product_amount)
    db.commit()

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

def updatePerson(db: Session, person: schemas.PersonsUpdate, person_id:int):
    db_person = getPersonById(db,person_id)
    if db_person is None:
        return None
    for key,value in vars(person).items():
        setattr(db_person,key,value) if value else None

    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def delPerson(db: Session, person: schemas.PersonsDelete):
    db.delete(person)
    db.commit()


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

def updateClient(db: Session, client: schemas.ClientUpdate, client_id:int):
    db_client = getClientById(db,client_id)
    if db_client is None:
        return None
    for key,value in vars(client).items():
        setattr(db_client,key,value) if value else None

    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def delClient(db: Session, client: schemas.ClientDelete):
    db.delete(client)
    db.commit()


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

def getWorkplaceById(db: Session, workplace_id:int):
    return db.query(models.Workplace).filter(models.Workplace.id == workplace_id).first()

def createWorkplace(db: Session, workplace: schemas.WorkplaceCreate):
    db_workplace = models.Workplace(name = workplace.name)
    db.add(db_workplace)
    db.commit()
    db.refresh(db_workplace)
    return db_workplace

def updateWorkplace(db: Session, workplace: schemas.WorkplaceUpdate, workplace_id:int):
    db_workplace = db.query(models.Workplace).filter(models.Workplace.id == workplace_id).first()
    if db_workplace is None:
        return None
    for key,value in vars(workplace).items():
        setattr(db_workplace,key,value) if value else None

    db.add(db_workplace)
    db.commit()
    db.refresh(db_workplace)
    return db_workplace

def delWorkplace(db: Session, workplace: schemas.WorkplaceDelete):
    db.delete(workplace)
    db.commit()

##################################################__ROLE__##################################################
def getRole(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()

def getRoleById(db: Session, role_id:int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()

def createRole(db: Session, role: schemas.RoleCreate):
    db_role = models.Role(name = role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def updateRole(db: Session, role: schemas.RoleUpdate, role_id:int):
    db_role = getRoleById(db,role_id)
    if db_role is None:
        return None
    for key,value in vars(role).items():
        setattr(db_role,key,value) if value else None

    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def delRole(db: Session, role: schemas.RoleDelete):
    db.delete(role)
    db.commit()

##################################################__EMPLOYEES__##################################################
def getEmployees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employees).offset(skip).limit(limit).all()

def getEmployeeById(db: Session, employee_id:int):
    return db.query(models.Employees).filter(models.Employees.id == employee_id).first()

def createEmployee(db: Session, employee: schemas.EmployeesCreate):
    db_employee = models.Employees(id_person = employee.id_person, id_workplace = employee.id_workplace, id_role = employee.id_role)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def updateEmployee(db: Session, employee: schemas.EmployeesUpdate, employee_id:int):
    db_employee = getEmployeeById(db,employee_id)
    if db_employee is None:
        return None
    for key,value in vars(employee).items():
        setattr(db_employee,key,value) if value else None

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delEmployee(db: Session, employee: schemas.EmployeesDelete):
    db.delete(employee)
    db.commit()