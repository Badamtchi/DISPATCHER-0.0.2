from sqlalchemy.orm import Session
from . import models


class MessageRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_query(self, filters):
        if type(filters) == tuple:
            query = None
        elif type(filters) == dict:
            query = self.db.query(models.Messages).filter((getattr(models.Messages, attr) == value for attr, value in filters.items()))
        return query

    def inbox(self, user):
        return self.get_query(filters={'receiver': user}).all()



#getattr(models.Messages, attr) == value for attr, value in filters.items()