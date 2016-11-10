from models.Artist import Artist


class TwitterController:

    def __init__(self):
        snoop = Artist("SnoopDogg")
        self.get_artist_tweet(snoop)

    def get_artist_tweet(artist):