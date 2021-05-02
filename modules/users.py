import psycopg2
import time

current_time = time.ctime()


class Users:
    create_conn = psycopg2.connect(host = 'localhost', database = 'books', user = 'postgres', password = '12345')

    cursor = create_conn.cursor()


    @staticmethod
    def insert_into_users_table(username, first_name, last_name, created_at):
        Users.cursor.execute("INSERT INTO users" "(username, firstname, lastname, created_at)" "VALUES(%s,%s,%s,%s)", (username,first_name, last_name, created_at))

        Users.create_conn.commit()
        Users.cursor.close()
        Users.create_conn.close()


new= Users()
new.insert_into_users_table('kassidy', 'Favour', 'Nnabue', current_time)