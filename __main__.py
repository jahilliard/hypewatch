from controllers.DatabaseController import DatabaseController
from controllers.model_controllers.EntityController import EntityController
from controllers.service_controllers.TwitterController import TwitterController


def main():
    # DatabaseController.drop_tables()
    # DatabaseController.create_tables()
    artist = EntityController.create_entity("Illenium", "musician")
    EntityController.update_entity_twitter(artist, 2187489492,"ILLENIUMMUSIC")
    # TwitterController.get_entity_profile_info(artist)


if __name__ == "__main__":
    main()
