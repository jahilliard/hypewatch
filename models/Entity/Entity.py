from models.BaseModel import BaseModel
from peewee import *
from db.Mysql import Mysql
from datetime import datetime


class Entity(BaseModel):
    name = CharField()
    type = CharField()
    start_tracking = DateTimeField()
    stop_tracking = DateTimeField(null=True)
    twitter_uhandle = CharField(null=True)
    twitter_uid = DoubleField(null=True)
    soundcloud_uname = CharField(null=True)
    soundcloud_uid = DoubleField(null=True)
    active = BooleanField()

    @staticmethod
    def create_entity_table():
        Mysql.db.connect()
        Mysql.db.create_tables([Entity], True)
        Mysql.db.close()

    def create_entity_db(self, name, type):
        self.name = name
        self.type = type
        self.start_tracking = datetime.utcnow()
        self.active = True
        self.save()
        return self

    def update_entity_twitter_credentials_db(self, twitter_uid, twitter_uhandle):
        self.twitter_uid = twitter_uid
        self.twitter_uhandle = twitter_uhandle
        self.save()
        return True

    @staticmethod
    def drop_entity_table():
        Entity.drop_table()

    @staticmethod
    def read(name, type):
        entity = Entity.select().where(Entity.name == name and Entity.type == type).get()
        if entity:
            return entity
