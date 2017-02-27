from datetime import datetime

from peewee import *

from src.models.BaseModel import BaseModel


class Entity(BaseModel):
    name = CharField()
    type = CharField()
    start_tracking = DateTimeField()
    stop_tracking = DateTimeField(null=True)
    twitter_uhandle = CharField(null=True)
    twitter_uid = DoubleField(null=True)
    soundcloud_uname = CharField(null=True)
    soundcloud_uid = DoubleField(null=True)
    instagram_uname = CharField(null=True)
    instagram_uid = DoubleField(null=True)
    spotify_uid = CharField(null=True)
    musicbrainz_uid = CharField(null=True)
    active = BooleanField()

    @staticmethod
    def create_entity_table():
        BaseModel.__metaclass__.database.connect()
        BaseModel.__metaclass__.database.create_table(Entity, safe=True)
        BaseModel.__metaclass__.database.close()

    @staticmethod
    def drop_entity_table():
        Entity.drop_table()

    @staticmethod
    def read(name, type):
        entity = Entity.select().where(Entity.name == name and Entity.type == type).get()
        if entity:
            return entity

    def create_entity_db(self, name, type):
        self.name = name
        self.type = type
        self.start_tracking = datetime.utcnow()
        self.active = True
        self.save()
        return self

    def update_entity_twitter_credentials_db(self, twitter_uid, twitter_uhandle):
        self.twitter_uid = twitter_uid
        self.twitter_uhandle = twitter_uhandle
        self.save()
        return True

    def update_entity_instagram_credentials_db(self, instagram_uid, instagram_uhandle):
        self.instagram_uid = instagram_uid
        self.instagram_uhandle = instagram_uhandle
        self.save()
        return True

    def update_entity_soundcloud_credentials_db(self, soundcloud_uid, soundcloud_uname):
        self.soundcloud_uid = soundcloud_uid
        self.soundcloud_uname = soundcloud_uname
        self.save()
        return True

    def update_entity_spotify_credentials_db(self, spotify_uid):
        self.spotify_uid = spotify_uid
        self.save()
        return True

    def update_entity_musicbrainz_credentials_db(self, musicbrainz_uid):
        self.musicbrainz_uid = musicbrainz_uid
        self.save()
        return True
