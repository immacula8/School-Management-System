class Student:
    users_db = {}  # shared memory store

    def __init__(self, first_name, last_name, email, date_of_birth, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.password = password

    def display_profile(self):
        print("\n--- Profile ---")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Phone: {self.phone_number}")