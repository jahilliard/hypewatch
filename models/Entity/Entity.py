from models.BaseModel import BaseModel
from peewee import *
from db.Mysql import Mysql


class Entity(BaseModel):
    name = CharField()
    type = CharField()
    start_tracking = DateTimeField()
    stop_tracking = DateTimeField(null=True)
    twitter_uhandle = CharField(null=True)
    twitter_uid = IntegerField(null=True)
    active = BooleanField()

    @staticmethod
    def create_entity_table():
        Mysql.db.connect()
        Mysql.db.create_tables([Entity], True)
        Mysql.db.close()

    @staticmethod
    def drop_entity_table():
        Entity.drop_table()

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
