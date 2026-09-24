print("Hllo world")  # String (str)
print(9.3)           # Floating-point number (float)
print(4)             # Integer (int)
print()
print("Arithmetic operators")
#Arithmetic operators are user with numeric values for mathematical operations.
#operators are used to perform operations
print(23 * 24 * 60)
print()
print("string concatenation")
#string concatenation - adding strings together and f means format
#method -1
print("20 days are " + str(20) + " minutes")
#method-2
print(f"20 days are {50} minutes")
print(f"20 days are {23 * 24 * 60} minutes")
print(f"20 days are {23 * 24 * 60 *60} seconds")

print()
print("variables")
#variables  are containers storing values
# Naming convention is convention (generally agreed scheme) for naming things
# - use lowercase with words separated by underscores
to_seconds = 23 * 24 * 60 *60
to_minutes = 23 * 24 * 60
print(f"20 days are {to_minutes} minutes")
print(f"20 days are {to_seconds} seconds")
print(f"20 days are {40 * to_minutes} minutes")
print(f"20 days are {40 * to_seconds} seconds")

print()
print("variables pratices")

to_seconds = 23 * 24 * 60 *60
to_minutes = 23 * 24 * 80
to_hours = 24
day_minute = 60
day = 24
name_of_units = "seconds"
name_of_minutes = "minutes"
name_of_hours = "hours"
print(f"20 days are {to_minutes} {name_of_units}")
print(f"20 days are {to_seconds} {name_of_units}")
print(f"20 days are {40 * to_minutes} {name_of_minutes}")
print(f"20 days are {40 * to_seconds} {name_of_hours}")

print()
print("functions")
#functions are basic blocks of codes and to avoid repeating the same logic
#A function is defined using the def keyword.
# Block of code which only runs when it is called
# calling a function = to excute the function
def day_of_units():
    print(f"20 days are {to_minutes} {name_of_units}")
    print("I am good")

day_of_units()
print()
print("functions parameteres")
#functions parameters
#parameters - information can be passed into functions as paramenters
#parameters are also called arguments
hours_in_day = 24
minutes_in_day = 24 * 60
seconds_in_day = 24 * 60 * 60

def day_of_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * hours_in_day} hours")
    print(f"{num_of_days} days are {num_of_days * minutes_in_day} minutes")
    print(f"{num_of_days} days are {num_of_days * seconds_in_day} seconds")
    print("I am good")

day_of_units(9)
#custom messages
print()
print("custom message")
def day_of_units(num_of_days, custom_messages):
    print(f"{custom_messages} {num_of_days} days are {num_of_days * hours_in_day} hours")
    print(custom_messages)
day_of_units(9, "Awesome")
print()
print("scope")
#Scope - A variable is only available from inside the region it is created
# - Global scope = variables available fro within any scope
# - Local scope = variables created inside function can only be used inside that function

def scope_check():
    of_day = 24
    my_var = "this is a variable"
    print(hours_in_day)
    print(of_day)
    print(my_var)

scope_check()
print()
print("Funtions with return values")
#function with return values
#Return values -- A function can return data as a result
hours_in_day = 24
minutes_in_day = 24 * 60
seconds_in_day = 24 * 60 * 60

def day_of_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * hours_in_day} hours"

my_var = day_of_units(9)
print(my_var)
print()
print("user accepting values")
#Built-in-function are provided by pythong language itself
#Accepting user input
input("The Number") #input() always return a string
#Expression that combines values and operators and always evaluates down to a single value
#user_input save the values
#casting converting one datatype to another datatype
hours_in_day = 24
def day_of_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * hours_in_day} hours"

user_input = input("Please ! Enter number of days: ")
user_input_number = int(user_input)

hours_in_day = day_of_units(user_input_number)
print(f"Hey user! Based on the {user_input} days given, this process may take {user_input_number * 24} hours to complete.")