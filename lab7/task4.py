class Applicant:
    def __init__(self, name, education, experience, gender, age):
        self.name = name
        self.education = education  # e.g., "PhD", "Masters", "Bachelors", "High School"
        self.experience = experience  # years of experience (int)
        self.gender = gender  # e.g., "Male", "Female", "Other"
        self.age = age  # int

    def score(self):
        score = 0

        # Education scoring
        education_weights = {
            "PhD": 30,
            "Masters": 25,
            "Bachelors": 20,
            "High School": 10,
            "Other": 5
        }
        score += education_weights.get(self.education, 0)

        # Experience scoring
        if self.experience >= 10:
            score += 30
        elif self.experience >= 5:
            score += 20
        elif self.experience >= 2:
            score += 10
        else:
            score += 5

        # Age scoring (prefer working age, but not biased against older/younger)
        if 22 <= self.age <= 35:
            score += 20
        elif 36 <= self.age <= 50:
            score += 15
        elif 18 <= self.age < 22:
            score += 10
        elif 51 <= self.age <= 65:
            score += 10
        else:
            score += 0  # Out of typical working age

        # Gender scoring (should be neutral, but let's show how bias could be introduced)
        # UNFAIR/BIAS EXAMPLE (do NOT use in real systems):
        # if self.gender == "Male":
        #     score += 5
        # elif self.gender == "Female":
        #     score += 5
        # else:
        #     score += 5
        # Instead, we do NOT add any points for gender to avoid bias.

        return score

    def __str__(self):
        return (f"{self.name}: Education={self.education}, Experience={self.experience} years, "
                f"Gender={self.gender}, Age={self.age}, Score={self.score()}")

def analyze_scoring_logic():
    print("Scoring Logic Analysis:")
    print("- Education: Higher degrees get more points. This may disadvantage those with less access to education.")
    print("- Experience: More years get more points, but early-career applicants get some points too.")
    print("- Age: Favors typical working ages, but does not penalize older/younger applicants harshly.")
    print("- Gender: No points are added for gender, avoiding gender bias.")
    print("Potential Biases:")
    print("- Education and experience may correlate with socioeconomic status, potentially introducing indirect bias.")
    print("- Age bands are broad to avoid age discrimination, but edge cases may still be disadvantaged.")
    print("- Gender is not considered in scoring to avoid bias.")

def main():
    applicants = [
        Applicant("Alice", "Masters", 6, "Female", 30),
        Applicant("Bob", "Bachelors", 12, "Male", 45),
        Applicant("Charlie", "PhD", 3, "Other", 28),
        Applicant("Diana", "High School", 8, "Female", 38),
        Applicant("Eve", "Bachelors", 1, "Female", 21),
        Applicant("Frank", "Masters", 15, "Male", 55),
        Applicant("Grace", "Other", 0, "Other", 19)
    ]

    print("Applicant Scores:")
    for applicant in applicants:
        print(applicant)

    print("\n")
    analyze_scoring_logic()

if __name__ == "__main__":
    main()
