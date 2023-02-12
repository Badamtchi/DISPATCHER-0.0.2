from sqlalchemy.orm import Session
from . import models


class GeneralRepository:
    def __init__(self, db:Session):
        self.db = db
    
    def get_query_msg(self, filters):
        return self.db.query(models.Messages).filter_by(**filters)
    
    def get_query_usr(self, filters):
        return self.db.query(models.Users).filter_by(**filters)
    
    # filter and filter_by:
    # def get_query_msg(self, filters):
    #     return self.db.query(models.Messages).filter(*(getattr(models.Messages, attr) == value for attr, value in filters.items()))


class MessageRepository(GeneralRepository):
    def inbox(self, user):
        return self.get_query_msg(filters={'receiver': user}).all()
    
    def inbox_unseen(self, user):
        return self.get_query_msg(filters={'receiver': user, 'seen': False}).all()
    
    def outbox(self, user):
        return self.get_query_msg(filters={'sender': user}).all()

    def msg_by_id_receiver(self, id, user):
        return self.get_query_msg(filters={'id': id, 'receiver': user}).first()
    
    def msg_by_id_sender(self, id, user):
        return self.get_query_msg(filters={'id': id, 'sender': user}).first()
    
    def send(self, msg):
        self.db.add(msg)
        self.db.commit()
        self.db.refresh(msg)
        return msg
    
    def edit(self, id, msg, user):
        msg_query = self.get_query(filters={'id': id, 'sender': user})
        msg_query.update(msg.dict(), synchronize_session=False)
        self.db.commit()
        return msg_query.first()

    def delete(self, id, user):
        msg_query = self.get_query(filters={'id': id, 'sender': user})
        msg_query.delete(synchronize_session=False)
        self.db.commit()
        return {"messages": "completed"}


class UserRepository(GeneralRepository):
    def usr_by_phone(self, phone):
        return self.get_query_usr(filters={'phone': phone}).first()
        
    def create(self, usr):
        self.db.add(usr)
        self.db.commit()
        self.db.refresh(usr)
        return usr
    