from datetime import datetime
from fastapi import HTTPException
from database.models import AttemptBlocker
class AuthAttemptBlocker:
    def __init__(self):
        pass
    def register_failed_attempt(self, username, db):
        user = db.query(AttemptBlocker).filter(AttemptBlocker.login == username).first()
        if user is None:
            block = AttemptBlocker(login = username, attempts = 1, time = datetime.now())
            db.add(block)
            db.commit()
            db.refresh(block)
            return
        if user.attempts < 6:
            block = AttemptBlocker(login=username, attempts=user.attempts+1, time=datetime.utcnow())
            db.delete(user)
            db.add(block)
            db.commit()
            db.refresh(block)
        else:
            return "User temporarily blocked"

    def is_blocked(self, username,db):
        """Check if a user is blocked based on their login attempts.

        This function checks if the specified username is blocked in the database based on their login attempts. It considers the following conditions:
        - If the user does not exist in the AttemptBlocker table, they are not blocked.
        - If the user has less than 6 login attempts, they are not blocked.
        - If the current date is later than the date of the last login attempt recorded for the user, the attempts are reset and the user is not blocked.
        - If the time difference between the current time and the time of the last login attempt is less than 5 minutes and the current hour is greater than or equal to the recorded hour, the user is blocked.
        - If the time difference between the current time and the time of the last login attempt is greater than 5 minutes, the attempts are reset and the user is not blocked.
        - Otherwise, the user is considered blocked.

        Args:
            username (str): The username of the user to be checked.
            db (Database): An instance of the database connection.

        Returns:
            bool: True if the user is blocked, False otherwise.
        """
        user = db.query(AttemptBlocker).filter(AttemptBlocker.login == username).first()
        if user is not None:
            if user.attempts < 6:
                return False
            if datetime.now().day > user.time.day or datetime.now().month > user.time.month or datetime.now().year > user.time.year:
                self.reset_attempts(username,db)
                return False
            if datetime.now().minute - user.time.minute < 5:
                if datetime.now().hour < user.time.hour:
                    return True
            if datetime.now().minute - user.time.minute > 5:
                self.reset_attempts(username, db)
                return False
            else:
                return True
        return False

    def reset_attempts(self, username,db):
        """This function removes the entry of the user from the AttemptBlocker table in the database, effectively resetting the login attempts for that user.

        Args:
            username (str): The username of the user whose login attempts need to be reset.
            db (Database): An instance of the database connection.

        Returns:
            None
        """
        user = db.query(AttemptBlocker).filter(AttemptBlocker.login == username).first()
        if user is not None:
            db.delete(user)
            db.commit()

    def block_user_if_needed(self, username, db):
        """This function checks if the specified username is blocked in the database. If the user is blocked, it raises an HTTPException with status code 429 (Too Many Requests).

        Args:
            username (str): The username of the user to be checked.
            db (Database): An instance of the database connection.

        Raises:
            HTTPException: If the user is blocked.

        Returns:
            None
        """
        if self.is_blocked(username, db):
            raise HTTPException(status_code=429, detail="Too Many Requests")

