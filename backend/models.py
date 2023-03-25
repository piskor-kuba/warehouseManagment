from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
import passlib.hash as hash

class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    category_product = relationship("Product", back_populates="product_category")

class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key = True, index = True)
    id_category = Column(Integer, ForeignKey("Category.id"))
    name = Column(String)
    describe = Column(String)

    product_category = relationship("Category", back_populates="category_product")
    product_amount = relationship("ProductAmount", uselist=False, back_populates="amount_product")
    product_clientProduct = relationship("ClientProduct", back_populates="clientProduct_product")

class ProductAmount(Base):
    __tablename__ = "Product_Amount"
    id = Column(Integer, primary_key=True, index=True)
    id_product = Column(Integer, ForeignKey("Product.id"))
    amount = Column(Integer)

    amount_product = relationship("Product", uselist=False, back_populates="product_amount")

class Persons(Base):
    __tablename__ = "Persons"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    surname = Column(String)
    phone = Column(Integer)
    address = Column(String)

    persons_client = relationship("Clients", uselist=False, back_populates="client_persons")

class Clients(Base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True, index=True)
    id_persons = Column(Integer, ForeignKey("Persons.id"))
    amount = Column(Integer)

    client_clientProduct = relationship("ClientProduct", back_populates="clientProduct_client")
    client_persons = relationship("Persons", uselist=False, back_populates="persons_client")

class ClientProduct(Base):
    __tablename__ = "Client_Product"
    id = Column(Integer, primary_key=True, index=True)
    id_client = Column(Integer, ForeignKey("Clients.id"))
    id_product = Column(Integer, ForeignKey("Product.id"))

    clientProduct_product = relationship("Product", back_populates="product_clientProduct")
    clientProduct_client = relationship("Clients", back_populates="client_clientProduct")

class Workplace(Base):
    __tablename__ = "Workplace"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    workplace_employee = relationship("Employees", uselist=False, back_populates="employee_workplace")

class Role(Base):
    __tablename__ = "Role"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    role_employee = relationship("Employees", uselist=False, back_populates="employee_role")

class Employees(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True, index=True)
    id_persons = Column(Integer, ForeignKey("Persons.id"))
    id_workplace = Column(Integer, ForeignKey("Workplace.id"))
    id_role = Column(Integer, ForeignKey("Role.id"))

    employee_workplace = relationship("Workplace", uselist=False, back_populates="workplace_employee")
    employee_role = relationship("Role", uselist=False, back_populates="role_employee")
    employee_loginData = relationship("LoginData", uselist=False, back_populates="loginData_employee")

class LoginData(Base):
    __tablename__ = "Login_data"
    id = Column(Integer, primary_key=True, index=True)
    id_employee = Column(Integer, ForeignKey("Employees.id"))
    login = Column(String)
    password = Column(String)

    loginData_employee = relationship("Employees", uselist=False, back_populates="employee_loginData")

    def verify_password(self, password:str):
        return hash.bcrypt.verify(password, self.password)