from student_record.student_records import StudentRecord
import unittest

class TestStudentRecord(unittest.TestCase):
    def setUp(self):
        self.files = StudentRecord('grades.csv')

