import psycopg2
import time



class Users:
    def __init__(self, dbname):
        self.dbname = dbname
        
        self.conn = psycopg2.connect(host = 'localhost', dbname = dbname , user = 'postgres', password = '12345')
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        # self.cursor.execute(f"DROP DATABASE IF EXISTS {self.dbname}")
        # self.cursor.execute(f"CREATE DATABASE {self.dbname}")
       

        
       
        
    def create_connection(self):
        self.conn = psycopg2.connect(host = 'localhost', dbname = self.dbname , user = 'postgres', password = '12345')
        self.cursor = self.conn.cursor() 
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()
        


    
    def create_table(self):
        self.create_connection()
        with open('sql_files/schema.sql', 'r') as schema_file:
            schema_values = schema_file.read()
            self.cursor.execute(schema_values)
            self.conn.commit()
            self.conn.close()
            return schema_values # returning values to use in testing


    def populate_table(self):
        self.create_connection()
        with open('sql_files/seeder.sql', 'r') as seeder_file:
            seeder_values = seeder_file.read()
            self.cursor.execute(seeder_values)
            self.conn.commit()
            return seeder_values 
            

    def create_user(self, username, firstname, lastname ):
        self.create_connection()
        self.cursor.execute('INSERT INTO users(username, firstname, lastname)'
                            'VALUES(%s,%s, %s)',
                            (username,firstname,lastname))
        self.conn.commit()

    def get_all_users(self):
        self.create_connection()
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def get_user(self, id):
        self.create_connection()
        self.cursor.execute(f"SELECT * FROM users WHERE id = {id}")
        return self.cursor.fetchall()

    def update_record_of_user(self, username, firstname, lastname, id):
        self.create_connection()
        self.cursor.execute(f'UPDATE users SET username = %s, firstname = %s, lastname = %s, updated_at = now() WHERE id = {id}', (username,firstname,lastname))
        self.conn.commit()

    def destroy(self, id):
        self.create_connection()
        self.cursor.execute(f'DELETE FROM users WHERE id = {id}')

    

    




