from student import Student

def register_user():
    print("\n--- Register User ---")
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    email = input("Email: ").strip()
    date_of_birth = input("Date of Birth: ").strip()
    phone_number = input("Phone (12 digits): ").strip()
    password = input("Create a strong password: ").strip()

    if "@" not in email or "." not in email:
        print("Invalid Email.")
        return

    if not phone_number.isdigit() or len(phone_number) != 12:
        print("Phone number must be 12 digits.")
        return

    if email in Student.users_db:
        print("Email already registered.")
        return  # ⬅️ Critical line

    new_user = Student(first_name, last_name, email, date_of_birth, phone_number, password)
    Student.users_db[email] = new_user
    print("Registered successfully!")
