# SCHOOL MANAGEMENT SYSTEM

print("-----------------------------SCHOOL MANAGEMENT SYSTEM------------------------")


def student():
    while True:
        full_name = input("Enter your full name here: ")
        email = input("Enter your email: ")
        phone = int(input("Enter your phone number: "))
        course = input("What course are you registering for? ")
        username = input("Enter your username here: ")
        password = input("Enter your password: ")

        print(f"Welcome to Aptech {full_name}")

        print("\nConfirm your details before proceeding")
        print(f"Your full name is {full_name}")
        print(f"Your email is {email}")
        try:
            print(f"Your phone number is {phone}")
        except ValueError:
            print("Enter your number in integer")

        print(f"Course Selected is {course}")

        conf = input("Is th above info correct? type Y or N: ")

        if conf.lower() == "y":
            print("\nKindly Log in to your account")

            user = input("Enter your username: ")
            pass1 = input("Enter your password: ")

            if user == username and pass1 == password:
                print("Loging Successful")


            else:
                print("Invalid Username or Password")
                break

        else:
            print("Kindly Re-register")
            break


student()
