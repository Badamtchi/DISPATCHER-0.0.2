from sqlalchemy.orm import Session
from . import models


class MessageRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_query_all(self, filters):
        return self.db.query(models.Messages).filter(*(getattr(models.Messages, attr) == value for attr, value in filters.items())).all()
    
    def get_query_one(self, filters):
        return self.db.query(models.Messages).filter(*(getattr(models.Messages, attr) == value for attr, value in filters.items())).first()

    def inbox(self, user):
        return self.get_query_all(filters={'receiver': user})
    
    def inbox_unseen(self, user):
        return self.get_query_all(filters={'receiver': user, 'seen': False})
    
    def outbox(self, user):
        return self.get_query_all(filters={'sender': user})

    def msg_by_id(self, id):
        return self.get_query_one(filters={'id': id})
    

    def send(self, msg):
        self.db.add(msg)
        self.db.commit()
        self.db.refresh(msg)
        return msg
    
    def edit(self, msg):
        self.db.commit()
        return msg.first()

