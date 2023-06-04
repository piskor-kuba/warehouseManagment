from pydantic import BaseModel, StrictStr, StrictInt
from typing import Optional

class CategoryBase(BaseModel):
    name: StrictStr

class ProductBase(BaseModel):
    id_category: StrictInt
    name: StrictStr
    describe: Optional[StrictStr] = None

class ProductAmountBase(BaseModel):
    id_product: StrictInt
    amount: StrictInt

class PersonsBase(BaseModel):
    name: StrictStr
    surname: StrictStr
    phone: StrictStr
    address:StrictStr

class ClientsBase(BaseModel):
    id_persons: StrictInt
    amount: StrictInt

class ClientProductBase(BaseModel):
    id_client:StrictInt
    id_product:StrictInt

class WorkplaceBase(BaseModel):
    name: StrictStr

class RoleBase(BaseModel):
    name: StrictStr

class EmployeesBase(BaseModel):
    id_person:StrictInt
    id_workplace:StrictInt
    id_role:StrictInt

class LoginDataBase(BaseModel):
    login: StrictStr
    password: StrictStr
    disabled: bool

class CreateUser(BaseModel):
    login: StrictStr
    password: StrictStr

class OtpBase(BaseModel):
    login: StrictStr
    otp_code: StrictStr