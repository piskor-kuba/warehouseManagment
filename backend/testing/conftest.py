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
from routers import users,person,employee,category,client,workplace,role, product

def get_user(email: str, db: Session):
    """
    Retrieve a user by email.

    Args:
        email (str): Email of the user.
        db (Session): Database session.

    Returns:
        Optional[models.LoginData]: User model if found, None otherwise.

    """
    user = db.query(models.LoginData).filter(models.LoginData.login == email).first()
    return user

def user_authentication_headers(client: TestClient, email: str, password: str, otp: str):
    """
    Generate authentication headers for a user.

    Args:
        client (TestClient): FastAPI TestClient instance.
        email (str): User email.
        password (str): User password.
        otp (str): One-time password.

    Returns:
        dict: Authentication headers.

    """
    data = {"username": email, "password": password, "client_secret": otp}
    headers = { 'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded',}
    res = client.post("/users/token", data=data, headers=headers)
    response = res.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers

def authentication_token(client: TestClient, email: str, password: str, db: Session):
    """
    Perform user authentication and retrieve authentication headers.

    Args:
        client (TestClient): FastAPI TestClient instance.
        email (str): User email.
        password (str): User password.
        db (Session): Database session.

    Returns:
        dict | None: Authentication headers or None if authentication fails.

    """
    user = get_user(email=email, db=db)
    if not user:
        print("Something is no yes")
        return None
    return user_authentication_headers(client=client, email=email, password=password, otp = "000000")

def start_application():
    """
    Start the FastAPI application and include the necessary routers.

    Returns:
        FastAPI: Initialized FastAPI application.

    """
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

@pytest.fixture
def app() -> Generator[FastAPI, Any, None]:
    """
    Fixture for creating the FastAPI application for testing.

    Yields:
        FastAPI: Initialized FastAPI application.

    """
    models.Base.metadata.create_all(engine)
    app = start_application()
    yield app


@pytest.fixture
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    """
    Fixture for creating a database session for testing.

    Args:
        app (FastAPI): FastAPI application.

    Yields:
        SessionTesting: Database session.

    """
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(app: FastAPI, db_session: SessionTesting) -> Generator[TestClient, Any, None]:
    """
    Fixture for creating a test client for API testing.

    Args:
        app (FastAPI): FastAPI application.
        db_session (SessionTesting): Database session.

    Yields:
        TestClient: Test client.

    """
    def getTestDB():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[getDB] = getTestDB
    with TestClient(app) as client:
        yield client
@pytest.fixture
def database( db_session: SessionTesting) -> Generator[Session, Any, None]:
    """
    Fixture for providing a database session.

    Args:
        db_session (SessionTesting): Database session.

    Yields:
        Session: Database session.

    """
    yield db_session

@pytest.fixture
def user_token(client: TestClient, db_session: Session):
    """
    Fixture for retrieving the user authentication token.

    Args:
        client (TestClient): Test client.
        db_session (Session): Database session.

    Returns:
        Dict[str, str]: User authentication token.

    """
    return authentication_token(client=client, email="test@test.pl", password="qwerty", db=db_session)