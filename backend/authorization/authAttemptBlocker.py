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
        user = db.query(AttemptBlocker).filter(AttemptBlocker.login == username).first()
        if user is not None:
            db.delete(user)
            db.commit()

    def block_user_if_needed(self, username, db):
        if self.is_blocked(username, db):
            raise HTTPException(status_code=429, detail="Too Many Requests")

