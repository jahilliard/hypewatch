from datetime import datetime

from src.src.models.BaseModel import BaseModel
from peewee import *
from src.src.services.streaming_services.SoundcloudService import SoundcloudService

from src.src.models.Entity.Entity import Entity


class SoundcloudProfile(BaseModel):
    tracked = DateTimeField()
    owner = ForeignKeyField(Entity, related_name='soundcloud_profile_metrics')
    description = TextField(null=True)
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
        if self.owner.soundcloud_uid:
            soundcloud_info = SoundcloudService.get_profile(self.owner)
            self.tracked = datetime.utcnow()
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
        else:
            return False
    
    def pull_last_week_data(self):
        pass


    @staticmethod
    def create_soundcloudprof_table():
        BaseModel.__metaclass__.database.connect()
        BaseModel.__metaclass__.database.create_table(SoundcloudProfile, safe=True)
        BaseModel.__metaclass__.database.close()

    @staticmethod
    def drop_soundcloudprof_table():
        SoundcloudProfile.drop_table()

    @staticmethod
    def delta_count(entity_id):
        query_results = SoundcloudProfile.raw("select t1.owner_id as owner_id, t2.followers_count as followers_count, "
                                              "t2.followers_count - t1.followers_count as count_delta FROM "
                                              "soundcloudprofile as t1 join soundcloudprofile as t2 ON "
                                              "DATE(t1.tracked) = DATE(t2.tracked) - INTERVAL 1 DAY "
                                              "and t1.owner_id = t2.owner_id Where DATE(t2.tracked) >= NOW() - "
                                              "INTERVAL 1 WEEK AND t1.owner_id = %s ORDER BY t2.tracked DESC",
                                              entity_id)
        return query_results
