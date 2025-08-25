# Nested dictionary representing student information
students = {
    1: {
        'first_name': 'xxxx',
        'last_name': 'Sirichandana',
        'branch': 'CSE',
        'sgpa': 9.2345677
    },
    2: {
        'first_name': 'xxxx',
        'last_name': 'Hasini',
        'branch': 'ECE',
        'sgpa': 9.9244558
    },
    3: {
        'first_name': 'xxxx',
        'last_name': 'Nivedha',
        'branch': 'CSE',
        'sgpa': 9.5344678
    }
}

def extract_student_info(student):
    full_name = f"{student['first_name']} {student['last_name']}"
    branch = student['branch']
    sgpa = student['sgpa']
    return full_name, branch, sgpa

# Extract and print information for each student
for sid, info in students.items():
    full_name, branch, sgpa = extract_student_info(info)
    print(f"FULL NAME: {full_name}")
    print(f"BRANCH: {branch}")
    print(f"SGPA: {sgpa}\n")