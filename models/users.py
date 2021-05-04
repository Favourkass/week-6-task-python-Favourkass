import psycopg2
import time



class Users:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(host = 'localhost', dbname = 'books_users_db' , user = 'postgres', password = '12345')
            self.cursor = self.conn.cursor() 
            # self.cursor.execute('CREATE DATABASE books_users_db')
        
            self.conn.autocommit = True
        except(Exception) as error:
            print("Error while connecting to Postgresql", error)
       

        
       
        
    # def create_connection(self):
    #     self.cursor.execute('CREATE DATABASE books_users_db')
    #     self.conn = psycopg2.connect(host = 'localhost', dbname ='books_users_db' , user = 'postgres', password = '12345')
    #     self.cursor = self.conn.cursor() 
        
       
    #     self.conn.autocommit = True
        


    
    def create_table(self):
        with open('sql_files/schema.sql', 'r') as schema_file:
            schema_values = schema_file.read()
            self.cursor.execute(schema_values)
            self.conn.commit()
            self.conn.close()


    def populate_table(self):
       
        with open('sql_files/seeder.sql', 'r') as seeder_file:
            seeder_values = seeder_file.read()
            self.cursor.execute(seeder_values)
            self.conn.commit()
            

    def create_user(self, username, firstname, lastname ):
        self.cursor.execute('INSERT INTO users(username, firstname, lastname)'
                            'VALUES(%s,%s, %s)',
                            (username,firstname,lastname))
        self.conn.commit()

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def get_user(self, id):
        self.cursor.execute(f"SELECT * FROM users WHERE id = {id}")
        return self.cursor.fetchall()

    def update_record_of_user(self, username, firstname, lastname, id):
        self.cursor.execute(f'UPDATE users SET username = %s, firstname = %s, lastname = %s, updated_at = now() WHERE id = {id}', (username,firstname,lastname))
        self.conn.commit()
    def destroy(self, id):
        self.cursor.execute(f'DELETE FROM users WHERE id = {id}')

    

    



values = Users()

print(values.get_all_users())
