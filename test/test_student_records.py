from student_record.student_records import StudentRecord
import unittest

class TestStudentRecord(unittest.TestCase):
    def setUp(self):
        self.database = StudentRecord('test_database.db')
        self.files = StudentRecord('grades.csv')
        self.list_for_test = ['hello']

    def test_create_table(self): 
        self.test_create_table = self.database.create_table()
        self.assertIsNone(self.test_create_table)
        
    def test_open_csv_file(self):
        self.test_open_csv_file = self.database.open_csv_file('grades.csv')
        self.assertIsNotNone(self.test_open_csv_file)

    def test_read_all(self):
        self.test_read_all = self.database.read_all()
        self.assertEqual(self.test_read_all, type(self.list_for_test))

    # def test_add_student(self):
    #     self.test_add_student = self.database.add_student('nnabue', 'favour', '124-61-7788', 78, 90, 77, 84, 90, 'A')
    #     self.assertIsNone(self.test_add_student)

    # def test_update_record(self):
    #     self.test_update_record = self.database.update_record(65,77,87,90,64, 'B', '345-67-8901')
    #     self.assertIsNone(self.test_read_all)
    #     sel.assertEqual(self.test_read_all, None)   
    # 
    def test_delete_record(self):
        self.test_delete_record =   self.database.delete_record('632-79-9939')  
        self.assertIsNone(self.test_delete_record)

    def test_above_50(self):
        self.test_above_50 =self.database.scored_above_50()
        self.assertEqual(self.test_above_50, type(self.list_for_test))

    def test_below_50(self):
        self.test_below_50 = self.database.scored_below_50()
        self.assertEqual(self.test_below_50, type(self.list_for_test))
        

    def test_test1_above_45(self):
        self.test_test1_above_45 = self.database.scored_above_45_in_test1()
        self.assertEqual(self.test_test1_above_45, type(self.list_for_test))

# if __name__ == '__main__':
#     unittest.main()

