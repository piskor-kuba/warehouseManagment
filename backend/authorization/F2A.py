from database import CRUD
from dependencies import getDB
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import pyotp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configuration.config import F2a

config = F2a()

__SECRET_KEY = config.key
__PASSWORD = config.password
__FROM = config.email

def __send_email(email,otp):
    """
    Function responsible for sending email messages.

    Args:
        email (str): Email address of the recipient.
        otp (object): Object containing the one-time password.

    Raises:
        HTTPException: Error occurred while sending the email.

    """
    emailBody = config.emailBody.format(code=otp.now())
    message = MIMEMultipart('alternative',None,[MIMEText(emailBody,'html')])
    message['Subject'] = config.emailSubject
    message['From'] = __FROM
    message['To'] = email
    try:
        server = smtplib.SMTP(config.smtpServer)
        server.ehlo()
        server.starttls()
        server.login(__FROM,__PASSWORD)
        server.sendmail(__FROM,email,message.as_string())
        server.quit()
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=400, detail="Error in sending email")

def totp_generate(login: str, db: Session = Depends(getDB)):
    """
    Generates a Time-based One-Time Password (TOTP) and sends it via email.

    Args:
        login (str): User login.
        db (Session, optional): Database session. Defaults to Depends(getDB).

    Returns:
        pyotp.TOTP: TOTP object.

    """
    totp = pyotp.TOTP(__SECRET_KEY)
    if CRUD.getOtpByLogin(login = login, db = db) is not None:
        CRUD.delOtp(db = db, login = login)
    CRUD.createOtpRecord(db = db,otp = totp.now(),login = login)
    __send_email(login,totp)
    return totp

def totp_verify(login: str, otp_code:str, db: Session = Depends(getDB)):
    """
    Verifies the provided OTP code for a given user login.

    Args:
        login (str): User login.
        otp_code (str): OTP code to verify.
        db (Session, optional): Database session. Defaults to Depends(getDB).

    Returns:
        bool: True if the OTP code is valid, False otherwise.

    """
    otp = CRUD.getOtpByLogin(db = db, login=login)
    if otp is None or not otp_code == otp.otp_code:
        return False
    return True

def release_otp(login: str, db: Session = Depends(getDB)):
    """
    Releases the OTP for a given user login by deleting it from the database.

    Args:
        login (str): User login.
        db (Session, optional): Database session. Defaults to Depends(getDB).

    """
    CRUD.delOtp(db=db, login=login)
