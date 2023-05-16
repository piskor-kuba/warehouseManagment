from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class CategoryBase(BaseModel):
    name: str

class ProductBase(BaseModel):
    id_category: int
    name: str
    describe: Optional[str] = None

class ProductAmountBase(BaseModel):
    id_product: int
    amount: int

class PersonsBase(BaseModel):
    name: str
    surname: str
    phone: str
    address:str

class ClientsBase(BaseModel):
    id_persons: int
    amount: int

class ClientProductBase(BaseModel):
    id_client:int
    id_product:int

class WorkplaceBase(BaseModel):
    name: str

class RoleBase(BaseModel):
    name: str

class EmployeesBase(BaseModel):
    id_person:int
    id_workplace:int
    id_role:int

class LoginDataBase(BaseModel):
    login: str
    password: str
    disabled: bool

class OtpBase(BaseModel):
    login: str
    otp_code: str