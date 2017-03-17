import soundcloud
from config.Config import Config


class SoundcloudService:
    client = soundcloud.Client(
        client_id=Config.soundcloud_api_key,
        client_secret=Config.soundcloud_api_secret
    )

    @staticmethod
    def get_profile(entity):
        if entity.soundcloud_uid:
            soundcloud_prof_info = SoundcloudService.client.get('/users/%d' % int(entity.soundcloud_uid))
            return soundcloud_prof_info
        else:
            return False


    @staticmethod
    def resolve_url(user_url):
        soundcloud_prof_info = SoundcloudService.client.get('/resolve', url=user_url)
        return soundcloud_prof_info
