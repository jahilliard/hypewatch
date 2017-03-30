from src.src.models.Twitter.TwitterProfile import TwitterProfile


class TwitterController:
    @staticmethod
    def get_entity_profile_info(entity):
        twitter_profile = TwitterProfile()
        twitter_profile.owner = entity
        twitter_profile.get_profile()
        return True

    @staticmethod
    def get_delta(entity_id):
        query_data = TwitterProfile.delta_count(entity_id)
        data_dict = {"owner_id": entity_id, "tracked": [], "count_delta": [], "followers_count": []}
        for row in query_data:
            data_dict["followers_count"].append(row.followers_count)
            data_dict["count_delta"].append(row.count_delta)
            data_dict["tracked"].append(row.tracked)
        return data_dict
