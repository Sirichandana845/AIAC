class Student:
    """
    Represents a student with name, age, and marks in three subjects.
    """

    def __init__(self, name, age, marks):
        """
        Initializes a Student instance.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            marks (list of int): Marks in three subjects.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        """
        Prints the student's details in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}")

    def total(self):
        """
        Returns the total marks obtained by the student.

        Returns:
            int: Sum of marks.
        """
        return sum(self.marks)
