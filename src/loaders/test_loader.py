from src.models.Entity.Entity import Entity
from src.controllers.service_controllers.SoundcloudController import SoundcloudController
from src.controllers.service_controllers.SpotifyController import SpotifyController
from src.controllers.service_controllers.TwitterController import TwitterController


def load_items():
    entities = Entity.get_all_entities()
    for entity in entities:
        SoundcloudController.get_entity_profile_info(entity=entity)
        SpotifyController.get_entity_profile_info(entity=entity)
        TwitterController.get_entity_profile_info(entity=entity)

if __name__ == "__main__":
    load_items()