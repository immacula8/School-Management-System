# School Management System - Teacher Module
# Manage Teachers 
# Add Teacher with their ID, name, Date-employed, Job-role/Subject, Job description, Email, phone, Address and Ratings 
# Search for a teacher using his/her ID
# View all teachers 
# Update a teacher's record with ID
# Delete a teacher's record by ID


class Teacher:
    valid_keys = ['teacher_name', 'date_employed', 'subject', 'job_description', 'email', 'phone_number', 'address', 'rating']

    def __init__(self, teacher_id, teacher_name, date_employed, subject, job_description, email, phone_number, address, rating):
        self.teacher_id = teacher_id
        self.subject = subject
        self.teacher_name = teacher_name
        self.date_employed = date_employed
        self.job_description = job_description
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.rating = rating

        def to_dict(self):
            return {
                "teacher_id": self.teacher_id,
                "name": self.teacher_name,
                "date_employed": self.date_employed,
                "subject": self.subject,
                "job_description": self.job_description,
                "email": self.email,
                "phone": self.phone_number,
                "address": self.address,
                "rating": self.rating
            }
    def update_info(self, **kwargs):
        """Update teacher's information with provided keyword arguments."""
        for key, value in kwargs.items():
            if key in self.__class__.valid_keys and hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return f"{self.teacher_name}, teaches {self.subject}. Job Description: {self.job_description}, Email: {self.email}, Rating: {self.rating}"