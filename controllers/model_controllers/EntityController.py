from models.Entity.Entity import Entity


class EntityController:
    @staticmethod
    def create_entity_db(entity, name, type):
        entity.create_entity_db(name, type)
        return True

    @staticmethod
    def update_entity_twitter_credentials_db(entity, twitter_uid, twitter_uhandle):
        entity.update_entity_twitter_credentials_db(twitter_uid, twitter_uhandle)
        return True

    @staticmethod
    def get_entity(name, type):
        return Entity.read(name, type)

