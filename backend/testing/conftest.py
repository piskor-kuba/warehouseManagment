from typing import Any
from typing import Generator
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from database import models
from dependencies import getDB
from routers import users,product,person,employee,category,client,workplace,role

def get_user(email: str, db: Session):
    user = db.query(models.LoginData).filter(models.LoginData.login == email).first()
    return user

def user_authentication_headers(client: TestClient, email: str, password: str, otp: str):
    data = {"username": email, "password": password, "client_secret": otp}
    headers = { 'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded',}
    res = client.post("/users/token", data=data, headers=headers)
    response = res.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers

def authentication_token(client: TestClient, email: str, db: Session):
    password = "qwerty"
    user = get_user(email=email, db=db)
    if not user:
        print("Something is no yes")
        return None
    return user_authentication_headers(client=client, email=email, password=password, otp = "000000")

def start_application():
    app = FastAPI()
    app.include_router(users.router)
    app.include_router(category.router)
    app.include_router(product.router)
    app.include_router(person.router)
    app.include_router(employee.router)
    app.include_router(role.router)
    return app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def app() -> Generator[FastAPI, Any, None]:
    models.Base.metadata.create_all(engine)
    app = start_application()
    yield app


@pytest.fixture(scope="module")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="module")
def client(app: FastAPI, db_session: SessionTesting) -> Generator[TestClient, Any, None]:
    def getTestDB():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[getDB] = getTestDB
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def user_token(client: TestClient, db_session: Session):
    return authentication_token(client=client, email="test@test.pl", db=db_session)