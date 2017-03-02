from src.models.Entity.Entity import Entity
from src.models.User.User import User
from src.models.Spotify.SpotifyProfile import SpotifyProfile
from src.models.Twitter.TwitterProfile import TwitterProfile
from src.models.Soundcloud.SoundcloudProfile import SoundcloudProfile


class DatabaseController:
    @staticmethod
    def create_tables():
        User.create_user_table()
        Entity.create_entity_table()
        TwitterProfile.create_twitterprof_table()
        SoundcloudProfile.create_soundcloudprof_table()
        SpotifyProfile.create_spotifyprof_table()

    @staticmethod
    def drop_tables():
        SpotifyProfile.drop_spotifyprof_table()
        TwitterProfile.drop_twitterprof_table()
        SoundcloudProfile.drop_table()
        Entity.drop_entity_table()
        User.drop_user_table()
