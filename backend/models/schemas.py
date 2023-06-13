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

class CategoryUpdate(tableModel.CategoryBase):
    name: Optional[str] = None
    class Config:
        orm_mode = True

class CategoryDelete(tableModel.CategoryBase):
    pass
    class Config:
        orm_mode = True

class Product(tableModel.ProductBase):
    id:int
    class Config:
        orm_mode = True

class ProductCreate(tableModel.ProductBase):
    amount:int
    class Config:
        orm_mode = True

class ProductDelete(tableModel.ProductBase):
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
class ProductAmountDelete(tableModel.ProductAmountBase):
    pass
    class Config:
        orm_mode = True

class ProductAmountUpdate(tableModel.ProductAmountBase):
    amount: Optional[int] = None
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
class PersonsDelete(tableModel.PersonsBase):
    pass
    class Config:
        orm_mode = True

class PersonsUpdate(tableModel.PersonsBase):
    name: Optional[str] = None
    surname: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
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

class ClientDelete(tableModel.ClientsBase):
    pass
    class Config:
        orm_mode = True
class ClientUpdate(tableModel.ClientsBase):
    amount: Optional[str] = None
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

class ClientProductDelete(tableModel.ClientProductBase):
    pass
    class Config:
        orm_mode = True

class ClientProductUpdate(tableModel.ClientProductBase):
    id_product: Optional[int] = None
    id_client: Optional[int] = None
    class Config:
        orm_mode = True

class Workplace(tableModel.WorkplaceBase):
    id:int
    class Config:
        orm_mode = True

class WorkplaceCreate(tableModel.WorkplaceBase):
    pass
    class Config:
        orm_mode = True

class WorkplaceDelete(tableModel.WorkplaceBase):
    pass
    class Config:
        orm_mode = True

class WorkplaceUpdate(tableModel.WorkplaceBase):
    name: Optional[str] = None
    class Config:
        orm_mode = True

class Role(tableModel.RoleBase):
    id:int

    class Config:
        orm_mode = True

class RoleCreate(tableModel.RoleBase):
    pass
    class Config:
        orm_mode = True

class RoleUpdate(tableModel.RoleBase):
    name: Optional[str] = None
    class Config:
        orm_mode = True

class RoleDelete(tableModel.RoleBase):
    pass
    class Config:
        orm_mode = True

class Employees(tableModel.EmployeesBase):
    id:int
    class Config:
        orm_mode = True

class EmployeesCreate(tableModel.EmployeesBase):
    pass
    class Config:
        orm_mode = True

class EmployeesUpdate(tableModel.EmployeesBase):
    id_person: Optional[int] = None
    id_workplace: Optional[int] = None
    id_role: Optional[int] = None
    class Config:
        orm_mode = True

class EmployeesDelete(tableModel.EmployeesBase):
    pass
    class Config:
        orm_mode = True

class LoginData(tableModel.LoginDataBase):
    id_employee: int
    class Config:
        orm_mode = True

class CreateUser(tableModel.CreateUser):
    id_employee: int
    class Config:
        orm_mode = True

class Otp(tableModel.OtpBase):
    id:int
    class Config:
        orm_mode = True

class OtpCreate(tableModel.OtpBase):
    pass
    class Config:
        orm_mode = True

class OtpDelete(tableModel.OtpBase):
    pass
    class Config:
        orm_mode = True
