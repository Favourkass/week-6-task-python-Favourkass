from models.books import Books
from models.users import Users
from student_record.student_records import StudentRecord



values = Users('test_database_db')

print(values.get_user(2))

# value = StudentRecord("Database.db")
# print(value.read_all())
