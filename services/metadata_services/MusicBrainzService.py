import musicbrainzngs as mb


class MusicBrainzService:
    mb.set_useragent("HypeWatch.io", "0.01", "http://hypewatch.io")

    @staticmethod
    def get_tracks_by_artist(artist_id):
        artist_info = mb.get_artist_by_id(artist_id,
                                          includes=["release-groups"],
                                          release_type=["album", "ep", "single"])
        if "release-group-list" in artist_info:
            return artist_info["release-group-list"]
        else:
            return []
