from student import Student

def login_user():
    print("\n--- Login ---")
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    user = Student.users_db.get(email)
    if user and user.password == password:
        print(f"Welcome back, {user.first_name}!")
        return user
    else:
        print("Invalid email or password.")
        return None
