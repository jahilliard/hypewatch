from src.models.Entity.Entity import Entity


class EntityController:
    '''TODO: write handlers for other info into the DB (ie Twitter)'''
    @staticmethod
    def create_new_entity(request):
        data = request.json
        if "entity" in data:
            entity_data = data["entity"]
            if "name" and "type" in entity_data:
                name = entity_data["name"]
                type = entity_data["type"]
                entity = Entity()
                entity.create_entity_db(name, type)
            else:
                return {"error": "Name and Type not defined"}
        else:
            return {"error": "Base Entity not Defined"}

    @staticmethod
    def update_entity_twitter_credentials_db(entity, twitter_uid, twitter_uhandle):
        entity.update_entity_twitter_credentials_db(twitter_uid, twitter_uhandle)
        return True

    @staticmethod
    def update_entity_instagram_credentials_db(entity, instagram_uid, instagram_uhandle):
        entity.update_entity_instagram_credentials_db(instagram_uid, instagram_uhandle)
        return True

    @staticmethod
    def update_entity_soundcloud_credentials_db(entity, soundcloud_uid, soundcloud_uhandle):
        entity.update_entity_soundcloud_credentials_db(soundcloud_uid, soundcloud_uhandle)
        return True

    @staticmethod
    def update_entity_spotify_credentials_db(entity, spotify_uid):
        entity.update_entity_spotify_credentials_db(spotify_uid)
        return True

    @staticmethod
    def update_entity_musicbrainz_credentials_db(entity, musicbrainz_uid):
        entity.update_entity_musicbrainz_credentials_db(musicbrainz_uid)
        return True

    @staticmethod
    def get_entity(name, type):
        return Entity.read(name, type)

