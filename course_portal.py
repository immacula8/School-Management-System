from course import Course

class Teacher:
    def __init__(self, name: str):
        self.name = name
        self.courses = []


class Student:
    def __init__(self, name: str):
        self.name = name
        self.courses = []


def create_course() -> Course:
    code = input("Enter course code (e.g. CSC101): ").strip().upper()
    title = input("Enter course title: ").strip()
    return Course(code, title)


def create_teacher() -> Teacher:
    name = input("Enter teacher name: ").strip()
    return Teacher(name)


def create_student() -> Student:
    name = input("Enter student name: ").strip()
    return Student(name)


def course_menu(course: Course):
    """Menu that manipulates a single course object."""

    while True:
        print("\n─── Course Menu ───")
        print(course)
        print("1. Assign teacher")
        print("2. Add student")
        print("3. List students")
        print("0. Return to main menu")
        choice = input("Select option: ").strip()

        if choice == "1":
            teacher = create_teacher()
            course.assign_teacher(teacher)
            print(f"Teacher {teacher.name} assigned.")

        elif choice == "2":
            student = create_student()
            course.add_student(student)
            print(f"Student {student.name} added.")

        elif choice == "3":
            if not course.students:
                print("No students enrolled yet.")
            else:
                print("Enrolled students:")
                for idx, s in enumerate(course.students, 1):
                    print(f"  {idx}. {s.name}")

        elif choice == "0":
            break
        else:
            print("Invalid option. Try again.")


def start_course_portal():
    courses = []

    while True:
        print("\n=== Course Management Portal ===")
        print("1. Create new course")
        print("2. Select existing course")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            course = create_course()
            courses.append(course)
            print(f"Course {course.course_code} created.")

        elif choice == "2":
            if not courses:
                print("No courses yet – create one first.")
                continue
            for idx, c in enumerate(courses, 1):
                print(f"  {idx}. {c.course_code} – {c.title}")
            try:
                sel = int(input("Select course number: "))
                course = courses[sel - 1]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue
            course_menu(course)

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice – try again.")

if __name__ == "__main__":
    start_course_portal()
