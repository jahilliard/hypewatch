from models.Entity.Entity import Entity
from datetime import datetime


class EntityController:
    @staticmethod
    def create_entity(name, type):
        entity = Entity()
        entity.name = name
        entity.type = type
        entity.start_tracking = datetime.utcnow()
        entity.active = True
        entity.save()
        return entity

    @staticmethod
    def update_entity_twitter(entity, twitter_uid, twitter_uhandle):
        entity.twitter_uid = twitter_uid
        entity.twitter_uhandle = twitter_uhandle
        entity.update()
        return entity


