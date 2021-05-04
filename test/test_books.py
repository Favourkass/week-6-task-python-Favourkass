import unittest
from models.books import Books



class TestBooks(unittest.TestCase):
    def setUp(self):
        self.database = Books("test_database_db") 
        self.list_for_testing  = [('favour'), ('chemistry')]
        

    def test_fetch_all_books(self):
        self.test_fetch_all_books = self.database.fetch_all_books(2)
        self.assertTrue(self.test_fetch_all_books, type(self.list_for_testing))

    def test_fetch_book(self):
        self.test_fetch_book = self.database.fetch_book(2)
        self.assertTrue(self.test_fetch_book, self.list_for_testing)

    def test_update_book(self):
        self.test_update_book = self.database.update_book(3, 1, 'World war 2', 400)
        self.assertIsNone(self.test_update_book)

    def test_create_book(self):
        self.test_create_book = self.database.create_book(1, 'Lord Of The Rings vol 2', 350)
        self.assertEqual(self.test_create_book, None)
        self.assertIsNone(self.test_create_book)

    def test_delete_book(self):
        self.test_delete_book = self.database.delete_book(1)
        self.assertIsNone(self.test_delete_book)
        self.assertEqual(self.test_delete_book, None)

    def tearDown(self):
        self.database = None
        self.list_for_testing = None

    
