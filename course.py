class Course:

    def __init__(self, course_code: str, title: str, teacher=None):
        """Create a new course.

        Args:
            course_code: Unique identifier like "CSC101".
            title: Human‑readable course title.
            teacher: A Teacher object (or None until one is assigned).
        """
        self.course_code = course_code
        self.title = title
        self.teacher = teacher 
        self.students = []

    def __str__(self):
        teacher_name = self.teacher.name if self.teacher else "TBD"
        return f"{self.course_code} – {self.title} (Teacher: {teacher_name})"

    def assign_teacher(self, teacher):
        """Attach a Teacher object to this course."""
        self.teacher = teacher

    def add_student(self, student):
        """Add a Student object to this course
            and avoiding duplicates."""
        if student not in self.students:
            self.students.append(student)

            if hasattr(student, "courses"):
                student.courses.append(self)
        else:
            print(f"{student.name} is already registered in {self.course_code}.")
