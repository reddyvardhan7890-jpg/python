#try - lets you "test" a block of code for errors
# Expect - catches the error and lets you handle it
#looping - to execute logic multiple times
#python has 2 loop commands
#conditions - evaluate to true or false
#are used most commonly in "if statements" and " loop"
#while loop
hours_in_day = 24

def day_of_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * hours_in_day} hours"
    elif num_of_days == 0:
        return "❌ Zero is not valid! Please enter more than 0 days."
    elif num_of_days < 0:
        return "This is negative, no conversion for you."
    else:
        return "❌ Days should be positive values only!"

while True:
        user_input = input("Please! Enter number of days: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        try:                                        # ← TRY this block
            user_input_number = int(user_input)
            if user_input_number >0:# if "abc" → jumps to except
                result = day_of_units(user_input_number)
                print(result)
                print(f"Hey user! Based on the {user_input} days given, this process may take {user_input_number * hours_in_day} hours to complete.")
            else:
                result = day_of_units(user_input_number)
                print(result)

        except ValueError:                          # ← CATCHES the crash
            print("❌ Please enter a valid number only!")

