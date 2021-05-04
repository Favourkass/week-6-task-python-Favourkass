import psycopg2


class Books:
    def __init__(self):
        self.conn = psycopg2.connect(host = 'localhost', dbname ='books_users_db' , user = 'postgres', password = '12345')
        self.cursor = self.conn.cursor() 
        self.conn.autocommit = True


    def fetch_all_books(self, user_id):
        self.cursor.execute(f'SELECT name FROM books where user_id = {int(user_id)}')
        return self.cursor.fetchall()

    def fetch_book(self, id):
        self.cursor.execute(f'SELECT name from books where id = {id}')
        return self.cursor.fetchall()

    def create_book(self, user_id, name, pages):
        self.cursor.execute('INSERT INTO books(user_id, name, pages) VALUES(%s,%s, %s)',
                            (user_id,name,pages))
        self.conn.commit()

    def update_book(self, id, user_id, name, pages):
        self.cursor.execute(f'UPDATE books SET user_id = %s, name = %s, pages = %s, updated_at = now() WHERE id = {id}',
                            (user_id, name, pages))
        self.conn.commit()

    def delete_book(self, id):
        self.cursor.execute(f'DELETE FROM books WHERE id = {id}')
        self.conn.commit()

values = Books()
print(values.fetch_book(2))