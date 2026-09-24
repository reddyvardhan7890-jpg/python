#LIST  → ordered collection
#SET   → unique values, no guaranteed order
#SORTED → gives you a sorted result



my_set = {"jan", "feb", "mar", "apr", "may", "jun", "jul"}
my_list=[1,23,34,55,23]
print(my_list)
print(my_set)

for element in my_set:
    print(element)

my_set.add("August")
print(my_set)

my_set.remove("August")
print(my_set)

my_list.remove(23)
print(my_list)

# ==========================================
# PYTHON BUILT-IN FUNCTIONS
# ==========================================


# 1. print()
# print() is used to display/output something on the screen.

print("Hello Python")
print(100)
print(10 + 20)


# ------------------------------------------
# 2. type()
# type() tells us what data type a value is.

print(type(10))          # int
print(type("Hello"))     # str
print(type(10.5))        # float
print(type(True))        # bool


# ------------------------------------------
# 3. input()
# input() is used to get information from the user.
# IMPORTANT: input() always returns a STRING.

name = input("Enter your name: ")
print(name)

# Even if you enter 25, input() treats it as "25"
age = input("Enter your age: ")
print(type(age))         # str


# ------------------------------------------
# 4. int()
# int() converts a value into an integer.
# This is useful when working with numbers from input().

age = int(input("Enter your age: "))

print(age)
print(type(age))         # int


# Example:
number = int("100")

print(number)
print(type(number))


# ------------------------------------------
# 5. set()
# set() creates a SET.
# A set stores unique values and removes duplicates.

numbers = [1, 2, 2, 3, 3, 4]

my_set = set(numbers)

print(my_set)

# Output:
# {1, 2, 3, 4}


# ==========================================
# EXTRA PRACTICE
# ==========================================

# Using input() + int() + type() + print()

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

result = number1 + number2

print("Result:", result)
print("Data type of result:", type(result))


# ==========================================
# SET PRACTICE
# ==========================================

my_list = [10, 20, 20, 30, 30, 40]

print("Original list:", my_list)

my_set = set(my_list)

print("After converting to set:", my_set)
print("Data type:", type(my_set))


# ==========================================
# QUICK REMINDER
# ==========================================

# print()  -> displays something
# type()   -> tells the data type
# input()  -> gets input from the user
# int()    -> converts to integer
# set()    -> creates a set / removes duplicates


my_dictionary  = {"jan:" "900", "hours:" "30mins"}
print(my_dictionary["hours"])