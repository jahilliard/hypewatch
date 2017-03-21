from src.src.models.Spotify.SpotifyProfile import SpotifyProfile


class SpotifyController:
    @staticmethod
    def get_entity_profile_info(entity):
        prof = SpotifyProfile()
        prof.owner = entity
        prof.get_profile()
        return True

    @staticmethod
    def get_delta(entity):
        return SpotifyProfile.delta_count(entity.id)
