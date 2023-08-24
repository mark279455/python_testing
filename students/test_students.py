import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class Test_student(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.student = Student("Joe", "Bloggs")


    def tearDown(self):
        pass

    def test_full_name(self):
        self.assertEqual(self.student.full_name, "Joe Bloggs")

    def test_alert_santa(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        self.assertEqual(self.student.email, "joebloggs@email.com")

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.assertEqual(self.student.apply_extension(21), old_end_date+ timedelta(days=21))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

if __name__ == '__main__':
    unittest.main()
