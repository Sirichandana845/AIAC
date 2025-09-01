class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

    def is_passing(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"
student1 = student("Alice", 101, 85)
student2 = student("Bob", 102, 72)
student3 = student("Charlie", 103, 58)
students = [student1, student2, student3]
for student in students:
    student.display_info()
    print(f"Grade: {student.is_passing()}")