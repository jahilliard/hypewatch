from datetime import datetime
from flask_login import UserMixin
from peewee import *

from src.models.BaseModel import BaseModel


class User(BaseModel, UserMixin):
    email = CharField()
    password = CharField()
    joined_platform = DateTimeField()
    active = BooleanField()
    is_superuser = BooleanField()

    @staticmethod
    def create_user_table():
        BaseModel.__metaclass__.database.connect()
        BaseModel.__metaclass__.database.create_table(User, safe=True)
        BaseModel.__metaclass__.database.close()

    @staticmethod
    def drop_user_table():
        User.drop_table()

    @staticmethod
    def get_by_email(email):
        entity = User.select().where(User.email == email)
        if entity.exists():
            return entity.get()
        else:
            return None

    @staticmethod
    def auth_user(email, password):
        entity = User.select().where(User.email == email and User.password == password).get()
        if entity:
            return entity

    def create_user_db(self, email, password):
        self.email = email
        self.password = password
        self.start_tracking = datetime.utcnow()
        self.active = True
        self.save()
        return self