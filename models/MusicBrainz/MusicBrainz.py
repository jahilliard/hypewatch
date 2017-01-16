from datetime import datetime
from services.metadata_services.MusicBrainzService import MusicBrainzService


class MusicBrainz:

    @staticmethod
    def get_artist_albums(entity):
        if entity.musicbrainz_uid:
            pass
        else:
            return False