from database.database import SessionLocal
from sqlalchemy.orm import Session

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

