import peewee as pw
import pymysql
from config.config import Config


class Mysql:
    db = pymysql.connect(host=Config.db_host, port=Config.db_port, user=Config.db_user,
                         passwd=Config.db_passwd, db=Config.db_name)
    db = pw.MySQLDatabase(db)

    def __init__(self):
        return