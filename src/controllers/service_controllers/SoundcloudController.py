from src.models.Soundcloud.SoundcloudProfile import SoundcloudProfile


class SoundcloudController:
    @staticmethod
    def get_entity_profile_info(entity):
        soundcloud_prof = SoundcloudProfile()
        soundcloud_prof.owner = entity
        soundcloud_prof.get_profile()
        return True

