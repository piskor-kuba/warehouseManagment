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
    """Send an email with a verification code to the specified email address.

    This function composes and sends an email containing a verification code to the specified email address. It uses the SMTP protocol to send the email via a Gmail server.

    Args:
        email (str): The recipient's email address.
        otp (OTP): An instance of the OTP class used to generate the verification code.

    Raises:
        HTTPException: If there is an error in sending the email.

    Returns:
        None
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
    """Generate a TOTP (Time-Based One-Time Password) for a user and send it via email.

    This function generates a TOTP for the specified login and sends it via email. It performs the following steps:
    - Creates an instance of the pyotp.TOTP class using the secret key (__SECRET_KEY).
    - If there is an existing OTP (One-Time Password) record for the login in the database, it deletes it.
    - Creates a new OTP record in the database with the current OTP value and the specified login.
    - Calls the __send_email function to send the OTP via email to the specified login.
    - Returns the TOTP instance.

    Args:
        login (str): The login for which the TOTP needs to be generated.
        db (Session): The database session obtained from the getDB function.

    Returns:
        pyotp.TOTP: The TOTP instance generated for the user.
        """
    totp = pyotp.TOTP(__SECRET_KEY)
    if CRUD.getOtpByLogin(login = login, db = db) is not None:
        CRUD.delOtp(db = db, login = login)
    CRUD.createOtpRecord(db = db,otp = totp.now(),login = login)
    __send_email(login,totp)
    return totp

def totp_verify(login: str, otp_code:str, db: Session = Depends(getDB)):
    """Verify a TOTP (Time-Based One-Time Password) code for a user.

    This function verifies the TOTP code entered by the user against the OTP code stored in the database for the specified login. It performs the following steps:
    - Retrieves the OTP record from the database based on the login.
    - If the OTP record is not found or the OTP code does not match the entered code, it returns False.
    - If the OTP code matches the entered code, it returns True.

    Args:
        login (str): The login for which the TOTP code needs to be verified.
        otp_code (str): The TOTP code entered by the user.
        db (Session): The database session obtained from the getDB function.

    Returns:
        bool: True if the TOTP code is valid, False otherwise.
        """
    otp = CRUD.getOtpByLogin(db = db, login=login)
    if otp is None or not otp_code == otp.otp_code:
        return False
    return True

def release_otp(login: str, db: Session = Depends(getDB)):
    """Release the OTP (One-Time Password) record for a user.

    This function deletes the OTP record from the database for the specified login.

    Args:
        login (str): The login for which the OTP record needs to be released.
        db (Session): The database session obtained from the getDB function.

    Returns:
        None
    """
    CRUD.delOtp(db=db, login=login)
