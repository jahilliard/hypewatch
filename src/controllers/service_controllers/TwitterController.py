from src.models.Twitter.TwitterProfile import TwitterProfile


class TwitterController:
    @staticmethod
    def get_entity_profile_info(entity):
        twitter_profile = TwitterProfile()
        twitter_profile.owner = entity
        twitter_profile.get_profile()
        return True
