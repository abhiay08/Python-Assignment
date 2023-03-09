'''Create a console app that allows users to log in and make diary entry. To keep things simple, app only
allows user to add an entry or read an earlier entry (skip the edit/delete feature)
Create an authentication system:
Create a sign up system. On starting the app, it should ask user of they want to log in or sign up (By pressing 1 or 2) If a user decides to sign up , ask for a username and password and save them in a file called passwords.txt
For example: Passwords.txt : UserA: password123 UserB: 321drowssap ...
 Also, while making the entry, make sure the username doesn’t already exist, otherwise show an error saying: “The username already exists”
 Along with this the system should also create a folder with the same username where the user’s diary entries will be saved.
For login flow: If user chooses to login, ask username and password and verify whether username exists in the file: Username doesn’t exists: show error “No user found” Password doesn’t match: show error “Incorrect
Password”
If both are correct, show user options to 1) read their entries 2) make an entry to the diary for today
View an entry: The list will be shown which has file names for all their previous entries (saved with file name as the date on which it was saved)
Make and entry: The user should be able to make a diary entry. User can press three “Enter”s in a row to stop making the entry Once the user is done with entry and presses the exit character/combination, save the entry in
the folder you created for that user at sign up time, in a file name same as the current date (whatever format of date suites you)
For all the flows, whenever a menu is shown to the user, don’t forget to add a ‘back’ option to the menu if applicable'''
import os
import datetime


def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def create_entry(username):
    filename = username + "/" + get_date() + ".txt"
    print("Enter your diary entry (press enter three times to exit): ")
    entry = ""
    while True:
        line = input()
        if line == "":
            entry += "\n"
        else:
            entry += line + "\n"
        if entry.count("\n") >= 3:
            break
    with open(filename, "w") as f:
        f.write(entry)
    print("Entry saved successfully.")


def read_entry(username):
    entries = []
    for filename in os.listdir(username):
        if filename.endswith(".txt"):
            entries.append(filename)
    if not entries:
        print("No entries found.")
    else:
        print("Select an entry to read:")
        for i, entry in enumerate(entries):
            print(f"{i + 1}. {entry}")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice < 1 or choice > len(entries):
             raise ValueError
        except ValueError:
         print("Invalid choice.")
        else:
             filename = username + "/" + entries[choice - 1]
             with open(filename, "r") as f:
                     entry = f.read()
             print(entry)


def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as f:
            data = f.readlines()
            for line in data:
                if username in line:
                    print("The username already exists.")
                    return
    with open("passwords.txt", "a") as f:
        f.write(f"{username}:{password}\n")
    os.makedirs(username, exist_ok=True)
    print("Sign up successful.")


def log_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "r") as f:
            data = f.readlines()
            for line in data:
                if line.startswith(username + ":"):
                    if line.strip().split(":")[1] == password:
                        print(f"Welcome {username}!")
                        while True:
                            print("1. Read entry")
                            print("2. Create entry")
                            print("3. Log out")
                            choice = input("Enter your choice: ")
                            if choice == "1":
                                read_entry(username)
                            elif choice == "2":
                                create_entry(username)
                            elif choice == "3":
                                print("Logged out.")
                                return
                            else:
                                print("Invalid choice.")
                        break
            else:
                print("Incorrect password.")
    else:
        print("No users found.")


def main():
    while True:
        print("1. Log in")
        print("2. Sign up")
        choice = input("Enter your choice: ")
        if choice == "1":
            log_in()
        elif choice == "2":
            sign_up()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
