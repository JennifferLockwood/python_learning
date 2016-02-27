class Employee:
    """
    Take in a first name, a last name, and an annual salary.
    'TIY 11-3. Employee.'
    """

    def __init__(self, first_name, last_name, salary):
        """Store an employee full name and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """
        Adds $5000 to the salary by default but also
        accepts a different raise amount.
        """
        self.salary += amount
