# set can store muitiplt items same as the list, but does not allow duplicate values

hours_in_day = 24


def day_of_units(num_of_days):
    if num_of_days > 0:
        return "This is a valid number."
    elif num_of_days < 0:
        return "This is negative, no conversion for you."
    else:
        return "❌ Days should be positive values only!"


while True:
    user_input = input("Please! Enter number of days: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    print(user_input.split(","))
    print(set(user_input.split(",")))

    print(type(user_input.split(",")))
    print(type(set(user_input.split(","))))
    
    try:
        for num_of_days in set(user_input.split(",")):

            num_of_days = int(num_of_days)

            result = day_of_units(num_of_days)

            print(result)

            if num_of_days > 0:
                hours = num_of_days * hours_in_day
                print(
                    f"Based on {num_of_days} days, "
                    f"this process may take {hours} hours to complete."
                )

    except ValueError:
        print("❌ Please enter valid numbers only!")
