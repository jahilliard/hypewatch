import unittest
from controllers.DatabaseController import DatabaseController
from controllers.model_controllers.EntityController import EntityController
from controllers.service_controllers.TwitterController import TwitterController
from controllers.service_controllers.SoundcloudController import SoundcloudController
from controllers.service_controllers.SpotifyController import SpotifyController
from models.Entity.Entity import Entity
from models.Twitter.TwitterProfile import TwitterProfile
from models.Soundcloud.SoundcloudProfile import SoundcloudProfile
from models.Spotify.SpotifyProfile import SpotifyProfile


class EntityTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        DatabaseController.create_tables()
        entity = Entity()
        EntityController.create_entity_db(entity, "Illenium", "musician")

    @classmethod
    def tearDownClass(cls):
        DatabaseController.drop_tables()

    def test_entity_to_db(self):
        self.assertTrue(Entity.read("Illenium", "musician"))
        self.assertEqual(Entity.read("Illenium", "musician").name, "Illenium")

    def test_read_entity(self):
        entity = Entity.read("Illenium", "musician")
        self.assertEqual(entity.name, "Illenium")
        self.assertEqual(entity.type, "musician")

    def test_update_twitter_credentials(self):
        entity = Entity.read("Illenium", "musician")
        self.assertTrue(EntityController.update_entity_twitter_credentials_db(entity, 2187489492, "ILLENIUMMUSIC"))
        self.assertEqual(entity.twitter_uhandle, "ILLENIUMMUSIC")
        self.assertEqual(entity.twitter_uid, 2187489492)

    def test_update_soundclound_credentials(self):
        entity = Entity.read("Illenium", "musician")
        self.assertTrue(EntityController.update_entity_soundcloud_credentials_db(entity, 27111815, "illeniumofficial"))
        self.assertEqual(entity.soundcloud_uname, "illeniumofficial")
        self.assertEqual(entity.soundcloud_uid, 27111815)


class TwitterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        DatabaseController.create_tables()
        entity = Entity()
        EntityController.create_entity_db(entity, "Illenium", "musician")
        EntityController.update_entity_twitter_credentials_db(entity, 2187489492, "ILLENIUMMUSIC")

    @classmethod
    def tearDownClass(cls):
        DatabaseController.drop_tables()

    def test_get_and_store_twitter_profile_to_db(self):
        entity = Entity.read("Illenium", "musician")
        self.assertTrue(TwitterController.get_entity_profile_info(entity))
        self.assertEqual(entity.id, TwitterProfile.select().where(TwitterProfile.owner_id == entity.id).get().id)


class SoundcloudTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        DatabaseController.create_tables()
        entity = Entity()
        EntityController.create_entity_db(entity, "Illenium", "musician")
        EntityController.update_entity_soundcloud_credentials_db(entity, 27111815, "illeniumofficial")

    @classmethod
    def tearDownClass(cls):
        DatabaseController.drop_tables()

    def test_get_and_store_soundcloud_profile_to_db(self):
        entity = Entity.read("Illenium", "musician")
        self.assertTrue(SoundcloudController.get_entity_profile_info(entity))
        self.assertEqual(entity.id, SoundcloudProfile.select().where(SoundcloudProfile.owner_id == entity.id).get().id)


class SpotfiyTest(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        DatabaseController.drop_tables()

    @classmethod
    def setUpClass(cls):
        DatabaseController.create_tables()
        entity = Entity()
        EntityController.create_entity_db(entity, "Illenium", "musician")
        EntityController.update_entity_spotify_credentials_db(entity, "45eNHdiiabvmbp4erw26rg")

    def test_get_and_store_spotify_profile_to_db(self):
        entity = Entity.read("Illenium", "musician")
        self.assertTrue(SpotifyController.get_entity_profile_info(entity))
        self.assertEqual(entity.id, SpotifyProfile.select().where(SpotifyProfile.owner_id == entity.id).get().id)


if __name__ == '__main__':
    unittest.main()