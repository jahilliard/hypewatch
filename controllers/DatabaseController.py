from models.Entity.Entity import Entity


class DatabaseController:
    @staticmethod
    def create_tables():
        Entity.create_entity_table()

    @staticmethod
    def drop_tables():
        Entity.drop_entity_table()