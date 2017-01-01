from peewee import *
from db.Mysql import Mysql


class DB:
    database = Mysql.db


class BaseModel(Model):
    __metaclass__ = DB

    class Meta:
        database = Mysql.db