def extract_student_info(student_dict):
    """
    Extracts and returns FULL NAME, BRANCH, and SGPA from a nested student dictionary.
    """
    full_name = student_dict.get('FULL NAME', 'N/A')
    branch = student_dict.get('BRANCH', 'N/A')
    sgpa = student_dict.get('SGPA', 'N/A')
    return full_name, branch, sgpa
# Example nested dictionary of students
students = {
    1: {
        'FULL NAME': 'xxxx Sirichandana',
        'BRANCH': 'CSE',
        'SGPA': 9.2345677
    },
    2: {
        'FULL NAME': 'xxxx Hasini',
        'BRANCH': 'ECE',
        'SGPA': 9.9244558
    },
    3: {
        'FULL NAME': 'xxxx Nivedha',
        'BRANCH': 'CSE',
        'SGPA': 9.5344678
    }
}
# Extract and print information for each student
for student_id, info in students.items():
    full_name, branch, sgpa = extract_student_info(info)
    print(f"FULL NAME: {full_name}")
    print(f"BRANCH: {branch}")
    print(f"SGPA: {sgpa}")
    print()  # Blank line between students
