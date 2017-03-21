from src.src.models.Twitter.TwitterProfile import TwitterProfile


class TwitterController:
    @staticmethod
    def get_entity_profile_info(entity):
        twitter_profile = TwitterProfile()
        twitter_profile.owner = entity
        twitter_profile.get_profile()
        return True

    @staticmethod
    def get_delta(entity):
        return TwitterProfile.delta_count(entity.id)