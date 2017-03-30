import json
from datetime import datetime

from src.src.models.BaseModel import BaseModel
from src.src.models.Entity.Entity import Entity
from peewee import *

from src.src.services.social_services.TwitterService import TwitterService


class TwitterProfile(BaseModel):
    twitter_serv = TwitterService()
    tracked = DateTimeField()
    owner = ForeignKeyField(Entity, related_name='twitter_profile_metrics')
    lang = CharField(8)
    profile_location = CharField(null=True)
    profile_image_url_https = CharField(null=True)
    profile_use_background_image = BooleanField()
    contributors_enabled = BooleanField()
    default_profile_image = BooleanField()
    profile_text_color = CharField()
    profile_banner_url = CharField()
    has_extended_profile = BooleanField()
    profile_background_color = CharField(null=True)
    time_zone = CharField(null=True)
    translator_type = CharField(null=True)
    description = CharField(null=True)
    url = CharField(null=True)
    default_profile = BooleanField()
    follow_request_sent = CharField(null=True)
    status = TextField()
    profile_background_image_url_https = CharField(null=True)
    verified = BooleanField()
    profile_image_url = CharField(null=True)
    created_at = CharField()
    profile_background_tile = BooleanField()
    favourites_count = IntegerField()
    profile_sidebar_fill_color = CharField(null=True)
    statuses_count = IntegerField()
    followers_count = IntegerField()
    notifications = CharField(null=True)
    location = CharField(null=True)
    is_translator = BooleanField()
    protected = BooleanField()
    listed_count = IntegerField()
    geo_enabled = CharField(null=True)
    following = CharField(null=True)
    friends_count = IntegerField()
    is_translation_enabled = BooleanField()
    profile_background_image_url = CharField(null=True)
    utc_offset = CharField(null=True)
    profile_sidebar_border_color = CharField(null=True)

    def get_profile(self):
        self.tracked = datetime.utcnow()
        twitter_profile_info = TwitterProfile.twitter_serv.get_twitter_profile(self.owner)
        if "protected" in twitter_profile_info:
            self.protected = twitter_profile_info["protected"]
        if "profile_background_image_url_https" in twitter_profile_info:
            self.profile_background_image_url_https = twitter_profile_info["profile_background_image_url_https"]
        if "listed_count" in twitter_profile_info:
            self.listed_count = twitter_profile_info["listed_count"]
        if "created_at" in twitter_profile_info:
            self.created_at = twitter_profile_info["created_at"]
        if "lang" in twitter_profile_info:
            self.lang = twitter_profile_info["lang"]
        if "followers_count" in twitter_profile_info:
            self.followers_count = twitter_profile_info["followers_count"]
        if "is_translator" in twitter_profile_info:
            self.is_translator = twitter_profile_info["is_translator"]
        if "time_zone" in twitter_profile_info:
            self.time_zone = twitter_profile_info["time_zone"]
        if "description" in twitter_profile_info:
            self.description = twitter_profile_info["description"]
        if "profile_text_color" in twitter_profile_info:
            self.profile_text_color = twitter_profile_info["profile_text_color"]
        if "profile_sidebar_fill_color" in twitter_profile_info:
            self.profile_sidebar_fill_color = twitter_profile_info["profile_sidebar_fill_color"]
        if "verified" in twitter_profile_info:
            self.verified = twitter_profile_info["verified"]
        if "follow_request_sent" in twitter_profile_info:
            self.follow_request_sent = twitter_profile_info["follow_request_sent"]
        if "geo_enabled" in twitter_profile_info:
            self.geo_enabled = twitter_profile_info["geo_enabled"]
        if "status" in twitter_profile_info:
            self.status = json.dumps(twitter_profile_info["status"])
        if "profile_image_url" in twitter_profile_info:
            self.profile_image_url = twitter_profile_info["profile_image_url"]
        if "profile_background_color" in twitter_profile_info:
            self.profile_background_color = twitter_profile_info["profile_background_color"]
        if "translator_type" in twitter_profile_info:
            self.translator_type = twitter_profile_info["translator_type"]
        if "contributors_enabled" in twitter_profile_info:
            self.contributors_enabled = twitter_profile_info["contributors_enabled"]
        if "following" in twitter_profile_info:
            self.following = twitter_profile_info["following"]
        if "profile_location" in twitter_profile_info:
            self.profile_location = twitter_profile_info["profile_location"]
        if "statuses_count" in twitter_profile_info:
            self.statuses_count = twitter_profile_info["statuses_count"]
        if "profile_use_background_image" in twitter_profile_info:
            self.profile_use_background_image = twitter_profile_info["profile_use_background_image"]
        if "favourites_count" in twitter_profile_info:
            self.favourites_count = twitter_profile_info["favourites_count"]
        if "profile_background_tile" in twitter_profile_info:
            self.profile_background_tile = twitter_profile_info["profile_background_tile"]
        if "is_translation_enabled" in twitter_profile_info:
            self.is_translation_enabled = twitter_profile_info["is_translation_enabled"]
        if "profile_banner_url" in twitter_profile_info:
            self.profile_banner_url = twitter_profile_info["profile_banner_url"]
        if "profile_image_url_https" in twitter_profile_info:
            self.profile_image_url_https = twitter_profile_info["profile_image_url_https"]
        if "notifications" in twitter_profile_info:
            self.notifications = twitter_profile_info["notifications"]
        if "url" in twitter_profile_info:
            self.url = twitter_profile_info["url"]
        if "friends_count" in twitter_profile_info:
            self.friends_count = twitter_profile_info["friends_count"]
        if "utc_offset" in twitter_profile_info:
            self.utc_offset = twitter_profile_info["utc_offset"]
        if "has_extended_profile" in twitter_profile_info:
            self.has_extended_profile = twitter_profile_info["has_extended_profile"]
        if "default_profile_image" in twitter_profile_info:
            self.default_profile_image = twitter_profile_info["default_profile_image"]
        if "profile_background_image_url" in twitter_profile_info:
            self.profile_background_image_url = twitter_profile_info["profile_background_image_url"]
        if "default_profile" in twitter_profile_info:
            self.default_profile = twitter_profile_info["default_profile"]
        if "profile_sidebar_border_color" in twitter_profile_info:
            self.profile_sidebar_border_color = twitter_profile_info["profile_sidebar_border_color"]
        if "location" in twitter_profile_info:
            self.location = twitter_profile_info["location"]
        self.save()
        return True

    @staticmethod
    def create_twitterprof_table():
        BaseModel.__metaclass__.database.connect()
        BaseModel.__metaclass__.database.create_table(TwitterProfile, safe=True)
        BaseModel.__metaclass__.database.close()

    @staticmethod
    def drop_twitterprof_table():
        TwitterProfile.drop_table()

    def read(self):
        TwitterProfile.read()

    @staticmethod
    def delta_count(entity_id):
        query_results = TwitterProfile.raw("select t1.owner_id as owner_id, t2.followers_count as followers_count, "
                                           "t2.tracked as tracked, "
                                              "t2.followers_count - t1.followers_count as count_delta FROM "
                                              "twitterprofile as t1 join twitterprofile as t2 ON "
                                              "DATE(t1.tracked) = DATE(t2.tracked) - INTERVAL 1 DAY "
                                              "and t1.owner_id = t2.owner_id Where DATE(t2.tracked) >= NOW() - "
                                              "INTERVAL 1 WEEK AND t1.owner_id = %s ORDER BY t2.tracked DESC",
                                           entity_id)
        return query_results
