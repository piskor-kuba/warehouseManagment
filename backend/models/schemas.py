from . import tableModel
from typing import Optional


class Category(tableModel.CategoryBase):
    id:int

    class Config:
        orm_mode = True

class CategoryCreate(tableModel.CategoryBase):
    pass
    class Config:
        orm_mode = True

class Product(tableModel.ProductBase):
    id:int
    class Config:
        orm_mode = True

class ProductCreate(tableModel.ProductBase):
    pass
    class Config:
        orm_mode = True

class ProductUpdate(tableModel.ProductBase):
    id_category: Optional[int] = None
    name: Optional[str] = None
    describe: Optional[str] = None
    class Config:
        orm_mode = True

class ProductAmount(tableModel.ProductAmountBase):
    id:int
    class Config:
        orm_mode = True

class ProductAmountCreate(tableModel.ProductAmountBase):
    pass
    class Config:
        orm_mode = True

class Persons(tableModel.PersonsBase):
    id:int
    class Config:
        orm_mode = True

class PersonsCreate(tableModel.PersonsBase):
    pass
    class Config:
        orm_mode = True

class Clients(tableModel.ClientsBase):
    id:int
    class Config:
        orm_mode = True

class ClientCreate(tableModel.ClientsBase):
    pass
    class Config:
        orm_mode = True

class ClientProduct(tableModel.ClientProductBase):
    id:int
    class Config:
        orm_mode = True

class ClientProductCreate(tableModel.ClientProductBase):
    pass
    class Config:
        orm_mode = True

class Workplace(tableModel.WorkplaceBase):
    id:int
    class Config:
        orm_mode = True

class Role(tableModel.RoleBase):
    id:int

    class Config:
        orm_mode = True

class Employees(tableModel.EmployeesBase):
    id:int
    class Config:
        orm_mode = True

class LoginData(tableModel.LoginDataBase):
    id_employee: int
    class Config:
        orm_mode = True

