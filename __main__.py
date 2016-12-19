from controllers.DatabaseController import DatabaseController
from controllers.model_controllers.EntityController import EntityController
from controllers.service_controllers.TwitterController import TwitterController
from services.streaming_services.SoundcloudService import SoundcloudService


def main():
    # DatabaseController.drop_tables()
    # DatabaseController.create_tables()
    # entity = Entity()
    # artist = EntityController.create_entity("Illenium", "musician")
    # artist = EntityController.create_entity("Illenium", "musician")
    # EntityController.update_entity_twitter(artist, 2187489492,"ILLENIUMMUSIC")
    # EntityController.update_entity_twitter(artist, 2187489492,"ILLENIUMMUSIC")
    TwitterController.update_entity_profile_info(artist)
    SoundcloudService.test_call()


if __name__ == "__main__":
    main()
