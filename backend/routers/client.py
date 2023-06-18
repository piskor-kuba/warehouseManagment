from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/client", tags=["client"])

@router.get("/", response_model = list[dict])
def read_clients(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a list of clients.

    Args:
        skip (int): The number of clients to skip (for pagination).
        limit (int): The maximum number of clients to retrieve (for pagination).
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        List[dict]: A list of clients.

    Raises:
        HTTPException(404): If no clients are found.
    """
    clients = CRUD.getClients(db, skip, limit)
    if clients is None:
        raise HTTPException(status_code=404, detail="clients not found")
    return clients

@router.get("/{client_id}", response_model= dict, status_code=200)
def read_client_by_id(client_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Retrieve a client by ID.

    Args:
        client_id (int): The ID of the client.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        dict: The client information.

    Raises:
        HTTPException(404): If the client is not found.
    """
    client = CRUD.getClientById(db = db, client_id = client_id)
    if client_id < 1 or client is None:
        raise HTTPException(status_code=404, detail="clients not found")
    return client


@router.post("/", response_model= schemas.ClientCreate, status_code=201)
def create_client(name: schemas.ClientCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Create a new client.

    Args:
        client (schemas.ClientCreate): The client data to be created.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.ClientCreate: The created client.

    Raises:
        HTTPException(400): If the client already exists.
    """
    client = CRUD.createClient(db = db, client = name)
    if client is None:
        raise HTTPException(status_code=400, detail="Client existed")
    return CRUD.createClient(db = db, client = name)

@router.post("/new_transition", response_model= schemas.ClientProductCreate, status_code=201)
def new_transition(new: schemas.ClientProductCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Create a new client product transition.

    Args:
        new_transition (schemas.ClientProductCreate): The client product transition data to be created.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.ClientProductCreate: The created client product transition.

    Raises:
        HTTPException(400): If the client does not exist.
    """
    client = CRUD.getClientById(db,new.id_client)
    if client is None:
        raise HTTPException(status_code= 400, detail="Client not existed")
    return CRUD.createClientProduct(db = db, client_product = new)

@router.patch("/{client_id}", response_model= schemas.ClientUpdate, status_code=200)
def update_client(client_id: int, client: schemas.ClientUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Update a client by its ID.

    Args:
        client_id (int): The ID of the client to be updated.
        updated_client (schemas.ClientUpdate): The updated client data.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Returns:
        schemas.ClientUpdate: The updated client.

    Raises:
        HTTPException(400): If the client does not exist.
    """
    cli= CRUD.getClientById(db = db, client_id = client_id)
    if cli is None:
        raise HTTPException(status_code=400, detail="Client not existed")
    return CRUD.updateClient(db = db, client = client, client_id = client_id)


@router.delete("/{client_id}", status_code=204)
def delete_client(client_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    """
    Delete a client by its ID.

    Args:
        client_id (int): The ID of the client to be deleted.
        current_user (schemas.LoginData): The currently authenticated user obtained through the get_current_active_user dependency.
        db (Session): The database session obtained from the getDB dependency.

    Raises:
        HTTPException(404): If the client is not found.
    """
    client = CRUD.getClientById(db,client_id)
    if client is None:
        raise HTTPException(status_code=404, detail=" Client not found")
    return CRUD.delClient(db = db, client = client)
