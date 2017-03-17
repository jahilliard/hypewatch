from src.src.controllers.service_controllers.SoundcloudController import SoundcloudController
from src.src.controllers.service_controllers.SpotifyController import SpotifyController
from src.src.models.Entity.Entity import Entity

from src.src.controllers.service_controllers.TwitterController import TwitterController


def load_soundcloud():
    entities = Entity.get_all_entities()
    for entity in entities:
        SoundcloudController.get_entity_profile_info(entity=entity)
    print("soundcloud")


def load_spotify():
    entities = Entity.get_all_entities()
    for entity in entities:
        SpotifyController.get_entity_profile_info(entity=entity)
    print("spotify")


def load_twitter():
    entities = Entity.get_all_entities()
    for entity in entities:
        TwitterController.get_entity_profile_info(entity=entity)
    print("twitter")