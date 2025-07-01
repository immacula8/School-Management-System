from register import register_user
from login import login_user

def main():
    while True:
        action = input("\nDo you want to (register / login / quit)? ").strip().lower()

        if action == "register":
            register_user()

        elif action == "login":
            user = login_user()
            if user:
                user.display_profile()

        elif action == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose register, login, or quit.")

if __name__ == "__main__":
    main()
