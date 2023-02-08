from sqlalchemy.orm import Session
from . import models


class MessageRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_query_all(self, filters):
        return self.db.query(models.Messages).filter(*(getattr(models.Messages, attr) == value for attr, value in filters.items()))
    
    def get_query_one(self, filters):
        return self.db.query(models.Messages).filter(*(getattr(models.Messages, attr) == value for attr, value in filters.items()))

    def inbox(self, user):
        return self.get_query_all(filters={'receiver': user}).all()
    
    def inbox_unseen(self, user):
        return self.get_query_all(filters={'receiver': user, 'seen': False}).all()
    
    def outbox(self, user):
        return self.get_query_all(filters={'sender': user}).all()

    def msg_by_id(self, id):
        return self.get_query_one(filters={'id': id}).first()
    
    def send(self, msg):
        self.db.add(msg)
        self.db.commit()
        self.db.refresh(msg)
        return msg
    
    def edit(self, id, msg):
        msg_query = self.get_query_one(filters={'id': id})
        msg_query.update(msg.dict(), synchronize_session=False)
        self.db.commit()
        return msg_query.first()

    def delete(self, id, user):
        msg_query = self.get_query_one(filters={'id': id, 'sender': user})
        msg_query.delete(synchronize_session=False)
        self.db.commit()
        return {"messages": "completed"}


