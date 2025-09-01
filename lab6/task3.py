def age_group(age):
    if age < 60:
        if age < 20:
            if age < 13:
                return "Child"
            else:
                return "Teenager"
        else:
            return "Adult"
    else:
        return "Senior"

age = [25, 56, 98, 100, 2, 18]
for a in age:
    print(f"The age group for {a} is: {age_group(a)}")

def age_groups(ages):
    groups = []
    for a in ages:
        if a < 13:
            groups.append("Child")
        elif a < 20:
            groups.append("Teenager")
        elif a < 60:
            groups.append("Adult")
        else:
            groups.append("Senior")
    return groups

ages = [25, 56, 98, 100, 2, 18]
print(age_groups(ages))