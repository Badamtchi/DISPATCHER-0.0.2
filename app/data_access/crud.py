from sqlalchemy.orm import Session
from . import models


class MessageRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_query(self, filters):
        return self.db.query(models.Messages).filter(*(getattr(models.Messages, attr) == value for attr, value in filters.items())).all()

    def inbox(self, user):
        return self.get_query(filters={'receiver': user})
    
    def inbox_unseen(self, user):
        return self.get_query(filters={'receiver': user, 'seen': False})
    
    def outbox(self, user):
        return self.get_query(filters={'sender': user})
