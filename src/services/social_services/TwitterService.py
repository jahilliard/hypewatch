import base64
from config.Config import Config
from src.managers.RequestManager import RequestManager


class TwitterService:
    base_url = "https://api.twitter.com"

    # TODO: URL encode the consumer key and the consumer secret according RFC 1738.
    def __init__(self):
        bearer_token_cred = Config.twitter_api_key + ":" + Config.twitter_api_secret
        bearer_token_cred = base64.b64encode(bearer_token_cred.encode("utf-8"))
        self.s = RequestManager.init_session()
        self.s.headers.update({"Authorization": "Basic " + bearer_token_cred.decode("utf-8")})
        self.access_token = RequestManager.post(self.s, self.base_url + "/oauth2/token/?grant_type=client_credentials")
        if "access_token" in self.access_token:
            self.s.headers.update({"Authorization": "Bearer " + self.access_token["access_token"]})

    def get_twitter_profile(self, entity):
        get_url = self.base_url + "/1.1/users/show.json?user_id=" + str(int(entity.twitter_uid))
        twitter_account_res = RequestManager.get(self.s, get_url)
        return twitter_account_res

    def get_most_recent_tweets(self, entity, count=5):
        get_url = self.base_url + "/1.1/statuses/user_timeline.json?user_id=" + str(entity.twitter_uid) + \
                  "&count=" + str(count)
        twitter_account_res = RequestManager.get(self.s, get_url)
        return twitter_account_res
