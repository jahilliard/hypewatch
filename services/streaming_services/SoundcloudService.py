import soundcloud
from config.config import Config
from managers.RequestManager import RequestManager


class SoundcloudService:
    client = soundcloud.Client(
        client_id=Config.soundcloud_api_key,
        client_secret=Config.soundcloud_api_secret
    )

    @staticmethod
    def get_profile(entity):
        if entity.souncloud_uname:
            soundcloud_prof_info = SoundcloudService.client.get('/users/' + entity.souncloud_uname)
            return soundcloud_prof_info
