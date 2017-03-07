from src.models.User.User import User
from src.models.Entity.Entity import Entity
from datetime import datetime


def main():
    User(email="justin.a.hilliard@gmail.com", password="TEST_PASSWORD", joined_platform=datetime.utcnow(),
                active=True, is_superuser=True).save()
    Entity(name='Gryffin', type='musician', twitter_uhandle='gryffinofficial', twitter_uid='1885133492',
           soundcloud_uname='gryffinofficial', soundcloud_uid='58879381', spotify_uid='2ZRQcIgzPCVaT9XKhXZIzh',
           active=True).save()
    Entity(name='Bipolar Sunshine', type='musician', twitter_uhandle='bipolarsunshine', twitter_uid=452945111,
           soundcloud_uname='bipolarsunshine', soundcloud_uid=11144557, spotify_uid='0CjWKoS55T7DOt0HJuwF1H',
           active=True).save()
    Entity(name='Billie Eilish', type='musician', twitter_uhandle='billieeilish', twitter_uid=2150327072,
           soundcloud_uname='billieeilish', soundcloud_uid=87105617, spotify_uid='6qqNVTkY8uBg9cP3Jd7DAH',
           active=True).save()
    Entity(name='Jacob Banks', type='musician', twitter_uhandle='MrJacobBanks', twitter_uid=74636548,
           soundcloud_uname='mrjacobbanks', soundcloud_uid=2731954, spotify_uid='0AepkoQhYvkjEzzwIcGxdV',
           active=True).save()
    Entity(name='Jerry Folk', type='musician', twitter_uhandle='JerryFolk', twitter_uid=2588327533,
           soundcloud_uname='jerryfolkmusic', soundcloud_uid=10731939, spotify_uid='356FCJoyYWyzONni54Dgrv',
           active=True).save()
    Entity(name='KOLAJ', type='musician', twitter_uhandle='kolajband', twitter_uid=3241834266,
           soundcloud_uname='kolajband', soundcloud_uid=67043508, spotify_uid='0hhL0iOf9ebHlwxWQyeH2w',
           active=True).save()
    Entity(name='Callie Reiff', type='musician', twitter_uhandle='CallieReiff', twitter_uid='241797576',
           soundcloud_uname='calliereiff', soundcloud_uid=102443393, spotify_uid='0XRFU9DhKXOo9vM4wKClyy',
           active=True).save()


if __name__ == "__main__":
    main()
