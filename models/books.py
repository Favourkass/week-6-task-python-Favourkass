import psycopg2


class Books:
    def __init__(self):
        self.conn = psycopg2.connect(host = 'localhost', dbname ='books_users_db' , user = 'postgres', password = '12345')
        self.cursor = self.conn.cursor() 
        self.conn.autocommit = True


    def fetch_all_books(self, user_id):
        self.cursor.execute(f'SELECT name FROM books where user_id = {int(user_id)}')
        return self.cursor.fetchall()
        self.conn.close()
        self.cursor.close()

  

values = Books()
print(values.fetch_all_books('2'))