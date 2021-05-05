from models.users import Users
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.database = Users('test_database_db')
        self.list_for_test = [('HELLO'), ('HI')]

    def test_create_table(self):
        self.test_create_table = self.database.create_table()
        self.assertIsNotNone(self.test_create_table)

    def test_populate_table(self):
        self.test_populate_table = self.database.populate_table()
        self.assertIsNotNone(self.test_populate_table)

    def test_create_user(self):
        self.test_create_user = self.database.create_user('Uchenna', 'Uche', 'Ogbonna')
        self.assertIsNone(self.test_create_user)
        self.assertEqual(self.test_create_user, None)

    def test_update_user(self):
        self.test_update_user = self.database.update_record_of_user('Kate', 'Katherine', 'Ugoji', 2)
        self.assertIsNone(self.test_update_user)
        self.assertEqual(self.test_update_user, None)

    def test_get_all_users(self):
        self.test_get_all_users = self.database.get_all_users()
        self.assertTrue(self.test_get_all_users, type(self.list_for_test))
        

    def test_get_user(self):
        self.test_get_user = self.database.get_user(2)
        self.assertTrue(self.test_get_user, self.list_for_test)
        self.assertIsInstance(self.test_get_user, list)

    # def test_destroy(self):
    #     self.test_destroy = self.database.destroy(1)
    #     self.assertIsNone(self.test_destroy)
    #     self.assertEqual(self.test_destroy, None)

    def tearDown(self):
        self.database = None
        self.list_for_testing = None
