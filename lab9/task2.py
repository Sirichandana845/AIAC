def assign_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score'

# Example usage:
print(assign_grade(85)) # Output: B
print(assign_grade(45)) # Output: F
print(assign_grade(105)) # Output: Invalid score