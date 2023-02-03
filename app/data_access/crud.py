from sqlalchemy.orm import Session
from . import models

class MessageRepository:
    def __init__(self, db:Session):
        self.db = db
    
    def get_all_messages(self):
        return self.db.query(models.Messages).all()

    def get_all_msgs(self, user):
        return self.db.query(models.Messages).filter(models.Messages.receiver == user).all()
    
    def get_messages(self, **filters):
        return self.db.query(models.Messages).filter(getattr(models.Messages, attr) == value for attr, value in filters.items()).all()
    
    def inbox(self, user):
        return self.get_messages(filters={"receiver": user})
