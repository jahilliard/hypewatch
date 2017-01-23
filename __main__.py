# from controllers.DatabaseController import DatabaseController
from src.controllers.DatabaseController import DatabaseController
from src.models.Entity.Entity import Entity
from config.Config import Config


def main():
    # DatabaseController.create_tables()
    # entity = Entity()
    # EntityController.create_entity_db(entity, "Illenium", "musician")
    # EntityController.update_entity_soundcloud_credentials_db(entity, 27111815, "illeniumofficial")
    # EntityController.update_entity_twitter_credentials_db(entity, 2187489492, "ILLENIUMMUSIC")
    # entity = Entity.read("Illenium", "musician")
    # print(entity.id)
    # TwitterController.get_entity_profile_info(entity)
    # print(TwitterProfile.select().where(TwitterProfile.owner_id == entity.id).get().id)
    # pass
    # SpotifyService()
    # MusicBrainzService.get_tracks_by_artist("91a81925-92f9-4fc9-b897-93cf01226282")
    print("Test Run")
    print(Config.TEST_ENV)

if __name__ == "__main__":
    main()
