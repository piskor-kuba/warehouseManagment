from fastapi import APIRouter, Depends, HTTPException
from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from models import schemas
from authorization.auth import get_current_active_user

router = APIRouter(prefix="/client", tags=["client"])

@router.get("/", response_model = list[schemas.Clients])
def read_clients(skip: int = 0, limit: int = 100, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    clients = CRUD.getClients(db, skip, limit)
    if clients is None:
        raise HTTPException(status_code=404, detail="clients not found")
    return clients

@router.get("/{client_id}", response_model= schemas.Clients, status_code=200)
def read_client_by_id(client_id: int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.getClientById(db = db, client_id = client_id)


@router.post("/", response_model= schemas.ClientCreate, status_code=201)
def create_client(name: schemas.ClientCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    client = read_clients(db = db)
    if name in client:
        raise HTTPException(status_code=400, detail="Client existed")
    return CRUD.createClient(db = db, client = name)\

@router.post("/new_transition", response_model= schemas.ClientProductCreate, status_code=201)
def new_transition(new: schemas.ClientProductCreate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    client = CRUD.getClientById(db,new.id_client)
    if client is None:
        raise HTTPException(status_code= 400, detail="Client not existed")
    return CRUD.createClientProduct(db = db, client_product = new)

@router.patch("/{client_id}", response_model= schemas.ClientUpdate, status_code=200)
def update_client(client_id: int, client: schemas.ClientUpdate, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    return CRUD.updateClient(db = db, client = client, client_id = client_id)


@router.delete("/{client_id}", status_code=204)
def delete_product(client_id : int, current_user: schemas.LoginData = Depends(get_current_active_user) ,db: Session = Depends(getDB)):
    client = CRUD.getClientById(db,client_id)
    if client is None:
        raise HTTPException(status_code=404, detail=" Client not found")
    return CRUD.delClient(db = db, client = client)
