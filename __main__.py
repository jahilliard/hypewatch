from controllers.DatabaseController import DatabaseController
from models.Entity.Entity import Entity
from controllers.model_controllers.EntityController import EntityController
from controllers.service_controllers.TwitterController import TwitterController
from controllers.service_controllers.SoundcloudController import SoundcloudController
from models.Twitter.TwitterProfile import TwitterProfile
from services.streaming_services.SoundcloudService import SoundcloudService
from services.streaming_services.SpotifyService import SpotifyService


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

if __name__ == "__main__":
    main()
