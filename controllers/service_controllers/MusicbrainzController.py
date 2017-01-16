from models.MusicBrainz.MusicBrainz import MusicBrainz


class MusicBrainzController:
    @staticmethod
    def get_entity_profile_info(entity):
        musicbrainz_prof = MusicBrainzProfile()
        musicbrainz_prof.owner = entity
        musicbrainz_prof.get_profile()
        return True

