from peewee import *
from db.Mysql import Mysql


class BaseModel(Model):
    class Meta:
        database = Mysql.db
