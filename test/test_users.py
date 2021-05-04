from models.users import Users
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.database = ('test_database_db')
        self.list_for_test = 