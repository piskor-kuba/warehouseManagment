from sqlalchemy.orm import Session
from models import schemas
from database import models


##################################################__CATEGORY__##################################################
def createCategory(db: Session, category: schemas.CategoryCreate):
    existed = db.query(models.Category).filter(models.Category.name == category.name).first()
    if existed is not None:
        return None
    db_category = models.Category(name = category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def getCategory(db: Session, skip: int = 0, limit: int = 100):
    """Get a list of categories from the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        skip (int): The number of categories to skip (used for pagination). Defaults to 0.
        limit (int): The maximum number of categories to retrieve (used for pagination). Defaults to 100.

    Returns:
        List[models.Category]: A list of category objects.
        """
    return db.query(models.Category).offset(skip).limit(limit).all()

def getCategoryById(db: Session, category_id:int):
    """Get a category from the database by its ID.

    Args:
        db (Session): The database session obtained from the getDB function.
        category_id (int): The ID of the category to retrieve.

    Returns:
        models.Category: The category object with the specified ID.
    """
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def delCategory(db: Session, category: schemas.CategoryDelete):
    """Delete a category from the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        category (schemas.CategoryDelete): The category object to be deleted.

    Returns:
        None
    """
    db.delete(category)
    db.commit()

def updateCategory(db: Session, category: schemas.CategoryUpdate, category_id:int):
    """Update a category in the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        category (schemas.CategoryUpdate): The updated category information.
        category_id (int): The ID of the category to be updated.

    Returns:
        models.Category: The updated category object.
    """
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
    """Create a new product in the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        product (schemas.ProductCreate): The product information used to create the new product.

    Returns:
        models.Product: The newly created product object.
    """
    db_product = models.Product(id_category = product.id_category, name = product.name, describe = product.describe)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def getProductById(db: Session, product_id:int):

    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    category = getCategoryById(db = db, category_id=product.id_category)
    response = {
        "category":category.name,
        "product_name":product.name,
        "describe":product.describe,
        "product_id":product.id
    }
    return response

def getProduct(db: Session, skip: int = 0, limit: int = 100):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    response = [
        {"category":getCategoryById(db = db, category_id=item.id_category).name,
         "product_name": item.name,
         "describe": item.describe,
         "product_id": item.id
         } for item in products
    ]

    return response

def updateProduct(db: Session, product: schemas.ProductUpdate, product_id:int):
    """Update a product in the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        product (schemas.ProductUpdate): The updated product information.
        product_id (int): The ID of the product to be updated.

    Returns:
        models.Product: The updated product object.
    """
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
    """Delete a product from the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        product (schemas.ProductDelete): The product object to be deleted.

    Returns:
        schemas.ProductDelete: The deleted product object.
        """
    db.delete(product)
    db.commit()
    return product


##################################################__PRODUCT-AMOUNT__##################################################
def getProductAmount(db: Session, skip: int = 0, limit: int = 100):
    """Get a list of product amounts from the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        skip (int): The number of product amounts to skip (used for pagination). Defaults to 0.
        limit (int): The maximum number of product amounts to retrieve (used for pagination). Defaults to 100.

    Returns:
        List[models.ProductAmount]: A list of product amount objects.
    """
    return db.query(models.ProductAmount).offset(skip).limit(limit).all()

def getProductAmountById(db: Session, product_amount_id:int):
    return db.query(models.ProductAmount).filter(models.ProductAmount.id == product_amount_id).first()

def createProductAmount(db: Session, product, amount):
    db_product_amount = models.ProductAmount(id_product=product.id, amount=amount)
    db.add(db_product_amount)
    db.commit()
    db.refresh(db_product_amount)
    return db_product_amount

def updateProductAmount(db: Session, product_amount: schemas.ProductAmountUpdate, product_amount_id:int):
    """Update a product amount in the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        product_amount (schemas.ProductAmountUpdate): The updated product amount information.
        product_amount_id (int): The ID of the product amount to be updated.

    Returns:
        models.ProductAmount: The updated product amount object.
    """
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
    """Delete a product amount from the database.

    Args:
        db (Session): The database session obtained from the getDB function.
        product_id (int): The ID of the product amount to be deleted.
    """
    db_product_amount = db.query(models.ProductAmount).filter(models.ProductAmount.id_product == product_id).first()
    db.delete(db_product_amount)
    db.commit()

##################################################__PERSONS__##################################################
def getPersons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Persons).offset(skip).limit(limit).all()

def getPersonById(db: Session, person_id:int):
    return db.query(models.Persons).filter(models.Persons.id == person_id).first()

def createPerson(db: Session, person: schemas.PersonsCreate):
    existed = db.query(models.Persons).\
        filter(models.Persons.name == person.name,\
               models.Persons.surname == person.surname,\
               models.Persons.phone == person.phone,\
               models.Persons.address == person.address\
               ).first()
    if existed is not None:
        return None
    db_person = models.Persons(name = person.name, surname = person.surname, phone = person.phone, address = person.address)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

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
    clients = db.query(models.Clients).offset(skip).limit(limit).all()
    response = [
        {
            "Name": ' '.join([getPersonById(db=db, person_id=item.id_persons).name,
                              getPersonById(db=db, person_id=item.id_persons).surname]),
            "Amount":item.amount,
            "Clinet_id":item.id
        } for item in clients
    ]

    return response

def getClientById(db: Session, client_id:int):
    client = db.query(models.Clients).filter(models.Clients.id == client_id).first()
    response = {
        "Name": ' '.join([getPersonById(db=db, person_id=client.id_persons).name,
                          getPersonById(db=db, person_id=client.id_persons).surname]),
        "Amount": client.amount,
        "Clinet_id": client.id
    }

    return response
def createClient(db: Session, client: schemas.ClientCreate):
    existed = db.query(models.Clients). \
        filter(models.Clients.id_persons == client.id_persons, \
               models.Clients.amount == client.amount \
               ).first()
    if existed is not None:
        return None
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
    existed = db.query(models.Workplace).filter(models.Workplace.name == workplace.name).first()
    if existed is not None:
        return None
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
    existed = db.query(models.Role).filter(models.Role.name == role.name).first()
    if existed is not None:
        return None
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
    employees = db.query(models.Employees).offset(skip).limit(limit).all()
    response = [
        {
        "Name": ' '.join([getPersonById(db=db, person_id= item.id_persons).name, getPersonById(db=db, person_id= item.id_persons).surname]),
        "Workplace": getWorkplaceById(db=db, workplace_id=item.id_workplace).name,
        "Role": getRoleById(db=db, role_id=item.id_role).name,
        "Employee_id":item.id
        } for item in employees
    ]
    return response
def getEmployeeById(db: Session, employee_id:int):
    employee = db.query(models.Employees).filter(models.Employees.id == employee_id).first()
    response = {
        "Name": ' '.join([getPersonById(db=db, person_id=employee.id_persons).name,
                          getPersonById(db=db, person_id=employee.id_persons).surname]),
        "Workplace": getWorkplaceById(db=db, workplace_id=employee.id_workplace).name,
        "Role": getRoleById(db=db, role_id=employee.id_role).name,
        "Employee_id": employee.id
    }
    return response

def createEmployee(db: Session, employee: schemas.EmployeesCreate):
    existed = db.query(models.Employees). \
        filter(models.Employees.id_persons == employee.id_persons, \
               models.Employees.id_workplace == employee.id_workplace, \
               models.Employees.id_role == employee.id_role \
               ).first()
    if existed is not None:
        return None
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

##################################################__OTP__##################################################
def getOtpByLogin(db: Session, login:str):
    return db.query(models.Otp).filter(models.Otp.login == login).first()

def createOtpRecord(db: Session, otp:str, login:str):
    db_otp = models.Otp(login = login, otp_code = otp)
    db.add(db_otp)
    db.commit()
    db.refresh(db_otp)
    return db_otp

def delOtp(db: Session, login: str):
    db_otp = getOtpByLogin(db,login)
    db.delete(db_otp)
    db.commit()
