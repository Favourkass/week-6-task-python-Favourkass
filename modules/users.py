import psycopg2
import time



class Users:
    def __init__(self):
        self.conn = psycopg2.connect(host = 'localhost', dbname = None, user = 'postgres', password = '12345') 
        self.cursor = self.conn.cursor() 
        self.conn.autocommit = True
        self.cursor.execute('DROP DATABASE IF EXISTS books_users_db')
        self.cursor.execute('CREATE DATABASE books_users_db')
       

        
    # def create_database(self):
       
        
        



    def create_connection(self):
        self.conn = psycopg2.connect(host = 'localhost', dbname ='books_users_db' , user = 'postgres', password = '12345')

        self.cursor = self.conn.cursor()
        self.conn.autocommit = True
    
    def create_table(self):
        self.create_connection()
        with open('sql_files/schema.sql', 'r') as schema_file:
            schema_values = schema_file.read()
            self.cursor.execute(schema_values)
            self.conn.commit()


    def populate_table(self):
        self.create_connection()
        with open('sql_files/seeder.sql', 'r') as seeder_file:
            seeder_values = seeder_file.read()
            self.cursor.execute(seeder_values)
            self.conn.commit()




values = Users()
values.create_table()
values.populate_table()
