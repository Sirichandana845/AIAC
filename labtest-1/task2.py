class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            return 'A+'
        elif 75 <= self.marks < 90:
            return 'A'
        elif 60 <= self.marks < 75:
            return 'B'
        elif 50 <= self.marks < 60:
            return 'C'
        else:
            return 'F'

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")

def display_sorted_students(students, sort_key='marks'):
    if sort_key == 'marks':
        sorted_students = sorted(students, key=lambda s: s.marks, reverse=True)
    elif sort_key == 'name':
        sorted_students = sorted(students, key=lambda s: s.name)
    elif sort_key == 'roll_no':
        sorted_students = sorted(students, key=lambda s: s.roll_no)
    else:
        sorted_students = students

    for student in sorted_students:
        student.display_details()
        print('-' * 20)

if __name__ == "__main__":
    n = int(input("Enter number of students: "))
    students = []
    for _ in range(n):
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = float(input("Enter marks: "))
        students.append(Student(name, roll_no, marks))

    print("\nStudents sorted by marks:")
    display_sorted_students(students, sort_key='marks')
