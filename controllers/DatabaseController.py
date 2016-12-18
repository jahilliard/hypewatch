from models.Entity.Entity import Entity
from models.Twitter.TwitterProfile import TwitterProfile


class DatabaseController:
    @staticmethod
    def create_tables():
        Entity.create_entity_table()
        TwitterProfile.create_twitterprof_table()

    @staticmethod
    def drop_tables():
        TwitterProfile.drop_twitterprof_table()
        Entity.drop_entity_table()