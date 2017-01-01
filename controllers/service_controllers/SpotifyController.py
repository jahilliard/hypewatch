from models.Spotify.SpotifyProfile import SpotifyProfile


class SpotifyController:
    @staticmethod
    def get_entity_profile_info(entity):
        prof = SpotifyProfile()
        prof.owner = entity
        prof.get_profile()
        return True

