from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import pyotp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__SECRET_KEY = "SuperSecretKeyThatEveryoneCanSee" #Musi być kodowane w Base32 czyli litery od A do Z i cyfry od 2 do 7
__PASSWORD = "bgqdvoiwwfuwqjzf"
__FROM = "wykrota.swajda@gmail.com"

def __send_email(email,otp):
    emailBody = """<html><body><p>Twój kod weryfikacyjny to: <b>{code}</b></p></body></html>""".format(code=otp.now())
    message = MIMEMultipart('alternative',None,[MIMEText(emailBody,'html')])
    message['Subject'] = "Kod weryfikacyjny"
    message['From'] = __FROM
    message['To'] = email
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(__FROM,__PASSWORD)
        server.sendmail(__FROM,email,message.as_string())
        server.quit()
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=400, detail="Error in sending email")

def totp_generate(login: str, db: Session = Depends(getDB)):
    totp = pyotp.TOTP(__SECRET_KEY)
    if CRUD.getOtpByLogin(login = login, db = db) is not None:
        CRUD.delOtp(db = db, login = login)
    CRUD.createOtpRecord(db = db,otp = totp.now(),login = login)
    __send_email(login,totp)
    return totp

def totp_verify(login: str, otp_code:str, db: Session = Depends(getDB)):
    otp = CRUD.getOtpByLogin(db = db, login=login)
    if otp is None or not otp_code == otp.otp_code:
        raise HTTPException(status_code=400, detail="Incorrect code")
    return True

def release_otp(login: str, db: Session = Depends(getDB)):
    CRUD.delOtp(db=db, login=login)
