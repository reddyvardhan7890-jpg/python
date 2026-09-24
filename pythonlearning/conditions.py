#conditionals - expressions that evaluate to either true or false
#== equals: A == B
# Not Equals: a ! = b
# less than: a < b
# less than or equal to: a <=b
# greater than: a > b
# Greater than or equal to: a > = b
#  Rule: If your function returns something, always catch it in a variable and print that variable
#  — never write a separate print that recalculates everything.
hours_in_day = 24
def day_of_units(num_of_days):
    print(num_of_days > 0)  # Boolean Data type True or False
    if num_of_days > 0:
        return f"Hey user! Based on the {user_input} days given, this process may take {user_input_number * 24} hours to complete."
    elif num_of_days == 0:
        return "Zero is not valid! Please enter more than 0 days."
    else:
        return "Given Days are negative values, days are always should be positive. "

user_input = input("Please ! Enter number of days: ")

if user_input.isdigit():
    user_input_number = int(user_input)
    hours_in_day = day_of_units(user_input_number)
# Return value of inner function is the input value for the outer function
    print(hours_in_day)
else:
    print("Please be smart! stop entering the values like dumb person")

#type() isn't really for "conditions" on its own —
# it's used to check what kind of data something is (a number, text, list, etc.).
# It becomes useful inside a condition when you want to make a decision based on the data type.

def describe(value):
    try:
        result = int(value)
        print(f"{result} is a whole number")
    except ValueError:
        try:
            result = float(value)
            print(f"{result} is a float")
        except ValueError:
            print(f"'{value}' is text")
describe(input("Enter a value: "))

