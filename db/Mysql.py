import peewee as pw
from config.Config import Config


class Mysql:
    db = pw.MySQLDatabase(Config.db_name, host=Config.db_host, port=Config.db_port, user=Config.db_user,
                          passwd=Config.db_passwd) if not Config.TEST_ENV else pw.MySQLDatabase(Config.test_db_name,
                          host=Config.test_db_host, port=Config.test_db_port, user=Config.test_db_user,
                          passwd=Config.test_db_passwd)