import json


class Grades:
    def __init__(self):
        """ Initializes grades dictionary from storage """
        self.load_grade_from_file()

    def add_grade(self, student_id, course, score):
        """ To add a grade based on student ID """
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")

        if student_id not in self.grades:
            self.grades[student_id] = {}

        self.grades[student_id][course] = {
                "score": score,
                "score_grade": self.get_score_grade(score)
        }
        self.save_grade_to_file()

    def get_score_grade(self, score):
        """ To grade and get score """
        match score:
            case s if s >= 70:
                return "A"
            case s if s >= 60:
                return "B"
            case s if s >= 50:
                return "C"
            case s if s >= 45:
                return "D"
            case _:
                return "F"

    def get_student_grade(self, student_id):
        """ To get all students courses and grades """
        return self.grades.get(student_id, {})


    def delete_student_grade(self, student_id, course):
        """ To delete student grade """
        try:
            del self.grades[student_id][course]
            if not self.grades[student_id]: # delete student if has no more courses
                del self.grades[student_id]
            self.save_grade_to_file()
        except KeyError:
            raise KeyError("Grade not found")

    def update_grade(self, student_id, course, new_score):
        """ To update student grade """
        self.add_grade(student_id, course, new_score)

    def save_grade_to_file(self, filename="grades.json"):
        """ To save to storage """
        with open(filename, "w") as file:
            json.dump(self.grades, file, indent=4)
            print("Grade saved to memory")

    def load_grade_from_file(self, filename="grades.json"):
        """ To loade from memory or storage """
        try:
            with open(filename, "r") as file:
                self.grades = json.load(file)
                print("Grade gotten from memeory")
        except (FileNotFoundError, json.JSONDecodeError):
            self.grades = {}
