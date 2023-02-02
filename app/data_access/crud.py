from sqlalchemy.orm import Session
from . import models

class MessageRepository:
    def __init__(self, db:Session):
        self.db = db
    
    def get_all_messages(self):
        return self.db.query(models.Messages).all()

    def get_msgs(self, user):
        return self.db.query(models.Messages).filter(models.Messages.receiver == user).all()