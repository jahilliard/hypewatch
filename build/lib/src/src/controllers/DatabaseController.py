from src.src.models.Entity.Entity import Entity
from src.src.models.User.User import User
from src.src.models.Spotify.SpotifyProfile import SpotifyProfile
from src.src.models.Twitter.TwitterProfile import TwitterProfile
from src.src.models.Soundcloud.SoundcloudProfile import SoundcloudProfile
from src.src.models.UserEntity.UserEntity import UserEntity
from datetime import datetime


class DatabaseController:
    @staticmethod
    def create_tables():
        User.create_user_table()
        Entity.create_entity_table()
        UserEntity.create_userentity_table()
        TwitterProfile.create_twitterprof_table()
        SoundcloudProfile.create_soundcloudprof_table()
        SpotifyProfile.create_spotifyprof_table()

    @staticmethod
    def drop_tables():
        SpotifyProfile.drop_spotifyprof_table()
        TwitterProfile.drop_twitterprof_table()
        SoundcloudProfile.drop_table()
        UserEntity.drop_userentity_table()
        Entity.drop_entity_table()
        User.drop_user_table()

    @staticmethod
    def load_sample_data():
        jhilliard = User(email="justin.a.hilliard@gmail.com", password="TEST_PASSWORD",
                         joined_platform=datetime.utcnow(),
                         active=True, is_superuser=True)
        jhilliard.save()
        gryffin = Entity(name='Gryffin', type='musician', twitter_uhandle='gryffinofficial', twitter_uid='1885133492',
                         soundcloud_uname='gryffinofficial', soundcloud_uid='58879381',
                         spotify_uid='2ZRQcIgzPCVaT9XKhXZIzh',
                         active=True)
        gryffin.save()
        UserEntity(entity=gryffin, user_with_permission=jhilliard)
        bipolar = Entity(name='Bipolar Sunshine', type='musician', twitter_uhandle='bipolarsunshine',
                         twitter_uid=452945111,
                         soundcloud_uname='bipolarsunshine', soundcloud_uid=11144557,
                         spotify_uid='0CjWKoS55T7DOt0HJuwF1H',
                         active=True)
        bipolar.save()
        UserEntity(entity=bipolar, user_with_permission=jhilliard)
        billie = Entity(name='Billie Eilish', type='musician', twitter_uhandle='billieeilish', twitter_uid=2150327072,
                        soundcloud_uname='billieeilish', soundcloud_uid=87105617, spotify_uid='6qqNVTkY8uBg9cP3Jd7DAH',
                        active=True)
        billie.save()
        UserEntity(entity=billie, user_with_permission=jhilliard)
        jacob = Entity(name='Jacob Banks', type='musician', twitter_uhandle='MrJacobBanks', twitter_uid=74636548,
                       soundcloud_uname='mrjacobbanks', soundcloud_uid=2731954, spotify_uid='0AepkoQhYvkjEzzwIcGxdV',
                       active=True)
        jacob.save()
        UserEntity(entity=jacob, user_with_permission=jhilliard)
        jerry = Entity(name='Jerry Folk', type='musician', twitter_uhandle='JerryFolk', twitter_uid=2588327533,
                       soundcloud_uname='jerryfolkmusic', soundcloud_uid=10731939, spotify_uid='356FCJoyYWyzONni54Dgrv',
                       active=True)
        jerry.save()
        UserEntity(entity=jerry, user_with_permission=jhilliard)
        kolaj = Entity(name='KOLAJ', type='musician', twitter_uhandle='kolajband', twitter_uid=3241834266,
                       soundcloud_uname='kolajband', soundcloud_uid=67043508, spotify_uid='0hhL0iOf9ebHlwxWQyeH2w',
                       active=True)
        kolaj.save()
        UserEntity(entity=kolaj, user_with_permission=jhilliard)
        callie = Entity(name='Callie Reiff', type='musician', twitter_uhandle='CallieReiff', twitter_uid='241797576',
                        soundcloud_uname='calliereiff', soundcloud_uid=102443393, spotify_uid='0XRFU9DhKXOo9vM4wKClyy',
                        active=True)
        callie.save()
        UserEntity(entity=callie, user_with_permission=jhilliard)
