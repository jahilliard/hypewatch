from src.src.models.Soundcloud.SoundcloudProfile import SoundcloudProfile


class SoundcloudController:
    @staticmethod
    def get_entity_profile_info(entity):
        soundcloud_prof = SoundcloudProfile()
        soundcloud_prof.owner = entity
        soundcloud_prof.get_profile()
        return True

    @staticmethod
    def pull_graph_data(request):
        pass

    @staticmethod
    def get_delta(entity_id):
        query_data = SoundcloudProfile.delta_count(entity_id)
        data_dict = {"owner_id": entity_id, "tracked": [], "count_delta": [], "followers_count": []}
        for row in query_data:
            data_dict["followers_count"].append(row.followers_count)
            data_dict["count_delta"].append(row.count_delta)
            data_dict["tracked"].append(row.tracked)
        return data_dict
