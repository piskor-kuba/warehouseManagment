from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import pyotp

__SECRET_KEY = "SuperSecretKeyThatEveryoneCanSee" #Musi być kodowane w Base32 czyli litery od A do Z i cyfry od 2 do 7


def totp_generate(login: str, db: Session = Depends(getDB)):
    totp = pyotp.TOTP(__SECRET_KEY)
    if CRUD.getOtpByLogin(login = login, db = db) is not None:
        CRUD.delOtp(db = db, login = login)

    CRUD.createOtpRecord(db = db,otp = totp.now(),login = login)

    return totp

def totp_verify(login: str, otp_code:str, db: Session = Depends(getDB)):
    otp = CRUD.getOtpByLogin(db = db, login=login)
    if otp is None or not otp_code == otp.otp_code:
        raise HTTPException(status_code=400, detail="Incorrect code")
    return True

def release_otp(login: str, db: Session = Depends(getDB)):
    CRUD.delOtp(db=db, login=login)
