from datetime import date, timedelta
import requests
import calendar


class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=self.days_to_add())
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def course_schedule(self):
        response = requests.get(
            f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "There was an error requesting the course_schedule data"

    @property
    def start_date(self):
        return self._start_date

    @staticmethod
    def is_leap_year(year):
        return calendar.isleap(year)

    def days_to_add(self):
        addon = 365
        day_of_year = int(self.start_date.strftime('%j'))
        if day_of_year > 59:
            if Student.is_leap_year(self.start_date.year) or Student.is_leap_year(self.start_date.year+1):
                addon = 366
        return addon


def main():
    student = Student("Fred", "Smith")
    student.days_to_add()


main()
