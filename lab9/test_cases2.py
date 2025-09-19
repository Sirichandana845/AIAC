def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid input"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test cases including boundaries and invalid inputs
test_scores = [
    100,    # Upper boundary for A
    90,     # Lower boundary for A
    89,     # Upper boundary for B
    80,     # Lower boundary for B
    79,     # Upper boundary for C
    70,     # Lower boundary for C
    69,     # Upper boundary for D
    60,     # Lower boundary for D
    59,     # Upper boundary for F
    0,      # Lower boundary for F
    -5,     # Invalid: negative
    105,    # Invalid: above 100
    "eighty", # Invalid: string
    None,   # Invalid: NoneType
    75.5    # Valid: float in C range
]

for score in test_scores:
    print(f"assign_grade({repr(score)}) => {assign_grade(score)}")