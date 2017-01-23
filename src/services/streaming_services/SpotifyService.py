import base64
from config.Config import Config
from src.managers.RequestManager import RequestManager


class SpotifyService:
    base_url = "https://api.spotify.com"
    auth_base_url = "https://accounts.spotify.com"

    # TODO: URL encode the consumer key and the consumer secret according RFC 1738.
    def __init__(self):
        bearer_token_cred = Config.spotify_api_key + ":" + Config.spotify_api_secret
        bearer_token_cred = base64.b64encode(bearer_token_cred.encode("utf-8"))
        self.s = RequestManager.init_session()
        auth_url = self.auth_base_url + "/api/token"
        self.s.headers.update({"Authorization": "Basic " + bearer_token_cred.decode("utf-8")})
        self.access_token = RequestManager.post(self.s, auth_url, data={"grant_type": "client_credentials"})
        if "access_token" in self.access_token:
            self.s.headers.update({"Authorization": "Bearer " + self.access_token["access_token"]})

    def get_profile(self, entity):
        if entity.spotify_uid:
            get_url = self.base_url + "/v1/artists/" + entity.spotify_uid
            spotify_account_res = RequestManager.get(self.s, get_url)
            return spotify_account_res
        else:
            return False

