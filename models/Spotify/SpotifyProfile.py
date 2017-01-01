from models.BaseModel import BaseModel
from services.streaming_services.SpotifyService import SpotifyService
from peewee import *
from models.Entity.Entity import Entity
from datetime import datetime


class SpotifyProfile(BaseModel):
    spotify_serv = SpotifyService()
    tracked = DateTimeField()
    owner = ForeignKeyField(Entity, related_name='spotify_profile_metrics')
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