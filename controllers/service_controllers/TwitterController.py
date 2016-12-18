from models.Twitter.TwitterProfile import TwitterProfile
import json
from datetime import datetime


class TwitterController:
    @staticmethod
    def get_entity_profile_info(entity):
        twitter_profile = TwitterProfile()
        twitter_profile.owner = entity
        twitter_profile_info = twitter_profile.get_profile()
        twitter_profile.tracked = datetime.utcnow()
        if "protected" in twitter_profile_info:
            twitter_profile.protected = twitter_profile_info["protected"]
        if "profile_background_image_url_https" in twitter_profile_info:
            twitter_profile.profile_background_image_url_https = twitter_profile_info[
                "profile_background_image_url_https"]
        if "listed_count" in twitter_profile_info:
            twitter_profile.listed_count = twitter_profile_info["listed_count"]
        if "created_at" in twitter_profile_info:
            twitter_profile.created_at = twitter_profile_info["created_at"]
        if "lang" in twitter_profile_info:
            twitter_profile.lang = twitter_profile_info["lang"]
        if "followers_count" in twitter_profile_info:
            twitter_profile.followers_count = twitter_profile_info["followers_count"]
        if "is_translator" in twitter_profile_info:
            twitter_profile.is_translator = twitter_profile_info["is_translator"]
        if "time_zone" in twitter_profile_info:
            twitter_profile.time_zone = twitter_profile_info["time_zone"]
        if "description" in twitter_profile_info:
            twitter_profile.description = twitter_profile_info["description"]
        if "profile_text_color" in twitter_profile_info:
            twitter_profile.profile_text_color = twitter_profile_info["profile_text_color"]
        if "profile_sidebar_fill_color" in twitter_profile_info:
            twitter_profile.profile_sidebar_fill_color = twitter_profile_info["profile_sidebar_fill_color"]
        if "verified" in twitter_profile_info:
            twitter_profile.verified = twitter_profile_info["verified"]
        if "follow_request_sent" in twitter_profile_info:
            twitter_profile.follow_request_sent = twitter_profile_info["follow_request_sent"]
        if "geo_enabled" in twitter_profile_info:
            twitter_profile.geo_enabled = twitter_profile_info["geo_enabled"]
        if "status" in twitter_profile_info:
            twitter_profile.status = json.dumps(twitter_profile_info["status"])
        if "profile_image_url" in twitter_profile_info:
            twitter_profile.profile_image_url = twitter_profile_info["profile_image_url"]
        if "profile_background_color" in twitter_profile_info:
            twitter_profile.profile_background_color = twitter_profile_info["profile_background_color"]
        if "translator_type" in twitter_profile_info:
            twitter_profile.translator_type = twitter_profile_info["translator_type"]
        if "contributors_enabled" in twitter_profile_info:
            twitter_profile.contributors_enabled = twitter_profile_info["contributors_enabled"]
        if "following" in twitter_profile_info:
            twitter_profile.following = twitter_profile_info["following"]
        if "profile_location" in twitter_profile_info:
            twitter_profile.profile_location = twitter_profile_info["profile_location"]
        if "statuses_count" in twitter_profile_info:
            twitter_profile.statuses_count = twitter_profile_info["statuses_count"]
        if "profile_use_background_image" in twitter_profile_info:
            twitter_profile.profile_use_background_image = twitter_profile_info["profile_use_background_image"]
        if "favourites_count" in twitter_profile_info:
            twitter_profile.favourites_count = twitter_profile_info["favourites_count"]
        if "profile_background_tile" in twitter_profile_info:
            twitter_profile.profile_background_tile = twitter_profile_info["profile_background_tile"]
        if "is_translation_enabled" in twitter_profile_info:
            twitter_profile.is_translation_enabled = twitter_profile_info["is_translation_enabled"]
        if "profile_banner_url" in twitter_profile_info:
            twitter_profile.profile_banner_url = twitter_profile_info["profile_banner_url"]
        if "profile_image_url_https" in twitter_profile_info:
            twitter_profile.profile_image_url_https = twitter_profile_info["profile_image_url_https"]
        if "notifications" in twitter_profile_info:
            twitter_profile.notifications = twitter_profile_info["notifications"]
        if "url" in twitter_profile_info:
            twitter_profile.url = twitter_profile_info["url"]
        if "friends_count" in twitter_profile_info:
            twitter_profile.friends_count = twitter_profile_info["friends_count"]
        if "utc_offset" in twitter_profile_info:
            twitter_profile.utc_offset = twitter_profile_info["utc_offset"]
        if "has_extended_profile" in twitter_profile_info:
            twitter_profile.has_extended_profile = twitter_profile_info["has_extended_profile"]
        if "default_profile_image" in twitter_profile_info:
            twitter_profile.default_profile_image = twitter_profile_info["default_profile_image"]
        if "profile_background_image_url" in twitter_profile_info:
            twitter_profile.profile_background_image_url = twitter_profile_info["profile_background_image_url"]
        if "default_profile" in twitter_profile_info:
            twitter_profile.default_profile = twitter_profile_info["default_profile"]
        if "profile_sidebar_border_color" in twitter_profile_info:
            twitter_profile.profile_sidebar_border_color = twitter_profile_info["profile_sidebar_border_color"]
        if "location" in twitter_profile_info:
            twitter_profile.location = twitter_profile_info["location"]
        twitter_profile.save()
        return twitter_profile
