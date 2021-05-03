import sqlite3
import csv



class StudentRecord:
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE if not exists student_table(first_name text, last_name text, ssn text, test1 int, test2 int, test3 int,
        test4 int, final int, grade text)''')

    def open_csv_file(self):
        with open('grades.csv', 'r') as open_csv:
            reader = csv.reader(open_csv)
            self.cursor.executemany('INSERT INTO student_table VALUES(?,?,?,?,?,?,?,?,?)', reader)
            self.connection.commit()
            self.connection.close()

    def read_all(self):
        get_all_grades = self.cursor.execute('''SELECT * FROM student_table''').fetchall()
        for row in get_all_grades:
            print(f'\n First Name: {row[0]} \n Last Name: {row[1]} \n Tests: {row[3:7]} \n Grade: {row[8]}')



    def add_student(self, first_name, last_name, ssn, test1, test2, test3, test4, final, grade):
        self.cursor.execute('''INSERT INTO student_table(first_name, last_name, ssn, test1, test2, test3, test4, final, grade)
                            VALUES(?,?,?,?,?,?,?,?,?)''',(first_name, last_name, ssn, test1, test2, test3, test4, final, grade))
        self.connection.commit()

    def update_record(self,test1, test2, test3, test4, final, grade, ssn):
        self.cursor.execute('''UPDATE student_table SET test1 = ?, test2 = ?, test3 =?, test4 = ?, final = ?, grade = ? 
        WHERE(ssn = ?)''', (test1, test2, test3, test4, final, grade, ssn))
        self.connection.commit()

    def delete_record(self, ssn):
        self.cursor.execute('''DELETE FROM student_table WHERE ssn = ?''', (ssn))
        self.connection.commit()

    def scored_above_50(self):
        scored_above_50 = self.cursor.execute('''SELECT * FROM student_table WHERE final >= 50''').fetchall()
        for row in scored_above_50[1:]:
            print(f'\n First Name: {row[0]} \n Last Name: {row[1]} \n Tests: {row[3:8]} \n Grade: {row[8]}')

    def scored_below_50(self):
        scored_below_50 = self.cursor.execute(''' SELECT * FROM student_table WHERE final <= 50''').fetchall()
        for row in scored_below_50:
            print(f'\n First Name: {row[0]} \n Last Name: {row[1]} \n Tests: {row[3:8]} \n Grade: {row[8]}')



value = StudentRecord()
print(value.delete_record(145-53-1634))
# print(value.update_record( '60', '78', '86','64', '80', 'A', '345-67-8901'))
# print(value.add_student('Long', 'nicholas', '145-53-1634', '40', '50','60', '65','67', 'A' ))


