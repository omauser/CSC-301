def check_number():
    try:
        user_input = int(input("Enter a number: "))
        if user_input == 0:
            print("The entered number is zero.")
        elif user_input % 2 == 0:
            print("The entered number is even.")
        else:
            print("The entered number is odd.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


check_number()
