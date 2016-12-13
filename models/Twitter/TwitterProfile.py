from models.BaseModel import BaseModel
from services.social_services.TwitterService import TwitterService
from peewee import *
from models.Entity.Entity import Entity


class TwitterProfile(BaseModel):
    twitter_serv = TwitterService()
    tracked = DateTimeField()
    owner = ForeignKeyField(Entity, related_name='twitter_profiles')
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
    created_at = DateTimeField()
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
        return TwitterProfile.twitter_serv.get_twitter_profile(self.owner)

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass