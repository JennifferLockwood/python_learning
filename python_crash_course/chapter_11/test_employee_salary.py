import unittest
from employee_salary import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class Employee. TIY 11-3 'Employee'."""

    def setUp(self):
        """
        Create a employee and a set of information for use in all test methods.
        """
        first_name = 'elm'
        last_name = 'pine'
        salary = 100000
        self.new_employee = Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        """Do salaries increase a default raise?"""
        self.new_employee.give_raise()

        self.assertEqual(self.new_employee.salary, 105000)

    def test_given_custom_raise(self):
        """Do salaries increase a custom raise?"""
        self.new_employee.give_raise(2000)

        self.assertEqual(self.new_employee.salary, 102000)

if __name__ == "__main__":
    unittest.main()
