from controllers.DatabaseController import DatabaseController
from controllers.model_controllers.EntityController import EntityController
from controllers.service_controllers.TwitterController import TwitterController


def main():
    DatabaseController.create_tables()
    artist = EntityController.create_entity("Snoop Dogg", "musician")
    artist = EntityController.update_entity_twitter(artist, 3004231, "SnoopDogg")
    TwitterController.get_entity_profile_info(artist)


if __name__ == "__main__":
    main()
