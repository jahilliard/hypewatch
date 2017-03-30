from datetime import datetime

from src.src.models.BaseModel import BaseModel
from peewee import *
from src.src.services.streaming_services.SpotifyService import SpotifyService

from src.src.models.Entity.Entity import Entity


class SpotifyProfile(BaseModel):
    spotify_serv = SpotifyService()
    tracked = DateTimeField()
    owner = ForeignKeyField(Entity, related_name='spotify_profile_metrics')
    # TODO: followers to Double
    followers = TextField(null=True)
    #TODO: Handle genres table
    genres = CharField(null=True)
    popularity = IntegerField(null=True)

    def get_profile(self):
        if self.owner.spotify_uid:
            spotify_profile_info = SpotifyProfile.spotify_serv.get_profile(self.owner)
            self.tracked = datetime.utcnow()
            if "followers" in spotify_profile_info:
                if "total" in spotify_profile_info["followers"]:
                    self.followers = spotify_profile_info["followers"]["total"]
            # TODO: Handle genres
            # self.genres = spotify_profile_info.genres
            if "popularity" in spotify_profile_info:
                self.popularity = spotify_profile_info["popularity"]
            self.save()
            return True
        else:
            return False


    @staticmethod
    def create_spotifyprof_table():
        BaseModel.__metaclass__.database.connect()
        BaseModel.__metaclass__.database.create_table(SpotifyProfile, safe=True)
        BaseModel.__metaclass__.database.close()

    @staticmethod
    def drop_spotifyprof_table():
        SpotifyProfile.drop_table()

    @staticmethod
    def delta_count(entity_id):
        query_results = SpotifyProfile.raw("select t1.owner_id as owner_id, t2.followers as followers, "
                                              "t2.followers - t1.followers as count_delta, "
                                              "t2.tracked as tracked FROM "
                                              "spotifyprofile as t1 join spotifyprofile as t2 ON "
                                              "DATE(t1.tracked) = DATE(t2.tracked) - INTERVAL 1 DAY "
                                              "and t1.owner_id = t2.owner_id Where DATE(t2.tracked) >= NOW() - "
                                              "INTERVAL 1 WEEK AND t1.owner_id = %s ORDER BY t2.tracked DESC",
                                           entity_id)
        return query_results