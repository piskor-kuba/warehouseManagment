import tableModel

class Category(tableModel.CategoryBase):
    id:int

    class Config:
        orm_mode = True

class CategoryCreate(tableModel.CategoryBase):
    pass

class Product(tableModel.ProductBase):
    id:int

    class Config:
        orm_mode = True

class ProductCreate(tableModel.ProductBase):
    pass

class ProductAmount(tableModel.ProductAmountBase):
    id:int
    id_product:int

    class Config:
        orm_mode = True

class Persons(tableModel.PersonsBase):
    id:int

    class Config:
        orm_mode = True

class Clients(tableModel.ClientsBase):
    id:int

    class Config:
        orm_mode = True

class ClientProduct(tableModel.ClientProductBase):
    id:int
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
    id:int
    class Config:
        orm_mode = True