from src.src.models.Entity.Entity import Entity
from src.src.models.User.User import User
from src.src.models.BaseModel import BaseModel
from peewee import *


class UserEntity(BaseModel):
    entity = ForeignKeyField(Entity, related_name='entity')
    user_with_permission = ForeignKeyField(User, related_name='user_with_permission')

    @staticmethod
    def create_userentity_table():
        BaseModel.__metaclass__.database.connect()
        BaseModel.__metaclass__.database.create_table(UserEntity, safe=True)
        BaseModel.__metaclass__.database.close()

    @staticmethod
    def drop_userentity_table():
        UserEntity.drop_table()


