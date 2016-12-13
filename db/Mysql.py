import peewee as pw
from config.config import Config


class Mysql:
    db = pw.MySQLDatabase(Config.db_name, host=Config.db_host, port=Config.db_port, user=Config.db_user,
                          passwd=Config.db_passwd)
