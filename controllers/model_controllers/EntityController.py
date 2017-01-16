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

