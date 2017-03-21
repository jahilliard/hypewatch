from src.src.models.Entity import Entity
from src.src.platform.Error import Error
from src.src.models.UserEntity.UserEntity import UserEntity
from src.src.models.Twitter.TwitterProfile import TwitterProfile
from src.src.models.Soundcloud.SoundcloudProfile import SoundcloudProfile
from src.src.models.Entity.Entity import Entity
from datetime import datetime, timedelta


class EntityController:
    # TODO: write handlers for other info into the DB (ie Twitter)
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
                if "twitter" in entity_data:
                    twitter_entity_data = entity_data["twitter"]
                    twitter_uid = twitter_entity_data["twitter_uid"]
                    twitter_uhandle = twitter_entity_data["twitter_uhandle"]
                    entity.update_entity_twitter_credentials_db(twitter_uid, twitter_uhandle)
                if "soundcloud" in entity_data:
                    soundcloud_entity_data = entity_data["soundcloud"]
                    soundcloud_uid = soundcloud_entity_data["soundcloud_uid"]
                    soundcloud_uname = soundcloud_entity_data["soundcloud_uname"]
                    entity.update_entity_soundcloud_credentials_db(soundcloud_uid, soundcloud_uname)
                if "spotify" in entity_data:
                    spotify_entity_data = entity_data["spotify"]
                    spotify_uid = spotify_entity_data["spotify_uid"]
                    entity.update_entity_spotify_credentials_db(spotify_uid)
                return entity
            else:
                error = Error("Name and Type not defined")
                return error
        else:
            error = Error("Base Entity not Defined")
            return error

    @staticmethod
    def update_entity(request):
        data = request.json
        if "entity" in data:
            entity_data = data["entity"]
            if "name" and "type" in entity_data:
                name = entity_data["name"]
                type = entity_data["type"]
                entity = Entity.get_entity(name, type)
                return entity
            else:
                error = Error("Name and Type not defined")
                return error

    @staticmethod
    def get_entity_7day_twitter_data(entity):
        oldest_date = datetime.utcnow() - timedelta(days=7)
        twitter_info = TwitterProfile.select().where(
            TwitterProfile.owner == entity, TwitterProfile.tracked > oldest_date)\
            .order_by(TwitterProfile.tracked.asc())
        return twitter_info

    @staticmethod
    def get_entity_7day_soundcloud_data(entity):
        oldest_date = datetime.utcnow() - timedelta(days=7)
        soundcloud_info = SoundcloudProfile.select().where(
            SoundcloudProfile.owner == entity, SoundcloudProfile.tracked > oldest_date)\
            .order_by(SoundcloudProfile.tracked.asc())
        return soundcloud_info

    @staticmethod
    def get_approved_entities(current_user):
        entities = Entity.select().join(UserEntity).where(UserEntity.user_with_permission == current_user.id)
        return entities

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

