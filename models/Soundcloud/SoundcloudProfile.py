from models.BaseModel import BaseModel
from services.streaming_services.SoundcloudService import SoundcloudService
from peewee import *
from models.Entity.Entity import Entity
from db.Mysql import Mysql



class SoundcloudProfile(BaseModel):
    tracked = DateTimeField()
    owner = ForeignKeyField(Entity, related_name='soundcloud_profile_metrics')
    description = CharField(null=True)
    username = CharField(null=True)
    avatar_url = CharField(null=True)
    country = CharField(null=True)
    full_name = CharField(null=True)
    city = CharField(null=True)
    website = CharField(null=True)
    track_count = IntegerField()
    playlist_count = IntegerField()
    followers_count = DoubleField()
    followings_count = DoubleField()

    def get_profile(self):
        soundcloud_info = SoundcloudService.get_profile(self.owner)
        self.description = soundcloud_info.description
        self.username = soundcloud_info.username
        self.avatar_url = soundcloud_info.avatar_url
        self.country = soundcloud_info.country
        self.full_name = soundcloud_info.full_name
        self.city = soundcloud_info.city
        self.website = soundcloud_info.website
        self.track_count = soundcloud_info.track_count
        self.playlist_count = soundcloud_info.playlist_count
        self.followers_count = soundcloud_info.followers_count
        self.followings_count = soundcloud_info.followings_count
        self.save()
        return True


    @staticmethod
    def create_soundcloudprof_table():
        Mysql.db.connect()
        Mysql.db.create_tables([SoundcloudProfile], True)
        Mysql.db.close()

    @staticmethod
    def drop_soundcloudprof_table():
        SoundcloudProfile.drop_table()

    def read(self):
        pass
