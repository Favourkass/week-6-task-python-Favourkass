import sqlite3
import csv

'''class StudentRecord creates a class for records of students and it does the following:
creates the database and connects to it
creates table for student records
open the csv file and writes them all into the created table
reads all record from the database
adds new record to the database
updates and deletes records from the database
gets a students that scored above 50 as final from db
gets a students that scored below 50 as final from db
gets a students that scored abve 50 as test1 from db 
'''

class StudentRecord:
    def __init__(self, dbname):

        try:
            self.connection = sqlite3.connect(dbname)
            self.cursor = self.connection.cursor()
        except(Exception) as error:
            print("invalid database to connect to", error)

    def create_table(self):
        self.cursor.execute('''CREATE TABLE if not exists student_table(first_name text, last_name text, ssn text, test1 int, test2 int, test3 int,
        test4 int, final int, grade text)''')

    def open_csv_file(self):

        with open('grades.csv', 'r') as open_csv:
            reader = csv.reader(open_csv)
            self.cursor.executemany('INSERT INTO student_table VALUES(?,?,?,?,?,?,?,?,?)', reader)
            self.connection.commit()
            self.connection.close()
            return reader # for testing purposes

    def read_all(self):
        get_all_grades = self.cursor.execute('''SELECT * FROM student_table''').fetchall()
        # return get_all_grades
        for row in get_all_grades:
            print(f'\n First Name: {row[0]} \n Last Name: {row[1]} \n Tests: {row[3:7]} \n Grade: {row[8]}')
        self.connection.close()
        return type(get_all_grades)
        

    def add_student(self, first_name, last_name, ssn, test1, test2, test3, test4, final, grade):
        try:
            self.cursor.execute('''INSERT INTO student_table(first_name, last_name, ssn, test1, test2, test3, test4, final, grade)
                                VALUES(?,?,?,?,?,?,?,?,?)''',(first_name, last_name, ssn, test1, test2, test3, test4, final, grade))
            self.connection.commit()

        except(Exception) as error:
            print("invalid parameters entered", error)


    def update_record(self,test1, test2, test3, test4, final, grade, ssn):
        self.cursor.execute('''UPDATE student_table SET test1 = ?, test2 = ?, test3 =?, test4 = ?, final = ?, grade = ? 
        WHERE(ssn = ?)''', (test1, test2, test3, test4, final, grade, ssn))
        self.connection.commit()
        self.connection.close()

    def delete_record(self, ssn):
        self.cursor.execute('DELETE FROM student_table WHERE ssn=?', (ssn,))
        self.connection.commit()
        self.connection.close()

    def scored_above_50(self):
        scored_above_50 = self.cursor.execute('SELECT * FROM student_table WHERE final >= 50').fetchall()
        for row in scored_above_50[1:]:
            print(f'\n First Name: {row[0]} \n Last Name: {row[1]} \n Tests: {row[3:8]} \n Grade: {row[8]}')
        self.connection.close()
        return type(scored_above_50)
    def scored_below_50(self):
        scored_below_50 = self.cursor.execute( 'SELECT * FROM student_table WHERE final <= 50').fetchall()
        for row in scored_below_50:
            print(f'\n First Name: {row[0]} \n Last Name: {row[1]} \n Tests: {row[3:8]} \n Grade: {row[8]}')
        self.connection.close()
        return type(scored_below_50)


    def scored_above_45_in_test1(self):
        scored_abov_45 = self.cursor.execute('SELECT * FROM student_table WHERE test1 >= 45').fetchall()
        for row in scored_abov_45[1:]:
            print(f'\n First Name: {row[0]} \n Last Name: {row[1]} \n Tests: {row[3:8]} \n Grade: {row[8]}')
        self.connection.close()
        return type(scored_abov_45)



# print(value.read_all())
# print(value.update_record( '60', '78', '86','64', '80', 'A', '345-67-8901'))
# print(value.add_student('Long', 'nicholas', '145-53-1634', '40', '50','60', '65','67', 'A' ))


