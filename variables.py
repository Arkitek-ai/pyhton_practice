# Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print (x)
print(y)
print(z)

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

# Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a


# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Ilegal
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Variable names with more than one word can be difficult to read.
# Camel Case:
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case:
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)