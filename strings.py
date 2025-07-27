# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print("Hello")
print('Hello')

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

# Modify Strings
# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = " Hello, World! "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(","))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Format String
# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.
price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# A placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 59} dollars"
print(txt)

# String Count Method
# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# The count() method returns the number of times a specified value appears in the string.
# string.count(value, start, end)
# Parameter Values
# value	Required. A String. The string to value to search for
# start	Optional. An Integer. The position to start the search. Default is 0
# end	Optional. An Integer. The position to end the search. Default is the end of the string
# Search from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

# Stirng encode() Method
# UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)

# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
# string.encode(encoding=encoding, errors=errors)

# encoding	Optional. A String specifying the encoding to use. Default is UTF-8
# errors	Optional. A String specifying the error method. Legal values are:
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded
# ignore'	- ignores the characters that cannot be encoded
# namereplace'	- replaces the character with a text explaining the character
# strict'	- Default, raises an error on failure
# replace'	- replaces the character with a questionmark
# xmlcharrefreplace'	- replaces the character with an xml character

txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# String endswith() Method:
# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# The endswith() method returns True if the string ends with the specified value, otherwise False.
# string.endswith(value, start, end)
# value	Required. The value to check if the string ends with. This value parameter can also be a tuple, then the method returns true if the string ends with any of the tuple values.
# start	Optional. An Integer specifying at which position to start the search
# end	Optional. An Integer specifying at which position to end the search

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# Check if the string ends with either the phrase "world." or "castle.":
txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

# String expandtabs() Method:
# Set the tab size to 2 whitespaces:
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

# The expandtabs() method sets the tab size to the specified number of whitespaces.
# string.expandtabs(tabsize)
# absize	Optional. A number specifying the tabsize. Default tabsize is 8
txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

# Stirng find() Method:
# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
# string.find(value, start, end)
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:
txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))


# String format_map() Method:
# Insert the name and age from a dictionary into the placeholders.
myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))

# The format_map() method formats the specified values of a dictionary and insert them inside the string's placeholders.
# The format_map() method returns the formatted string.

# string.format_map(dictionary)
# dictionary	Required. A dictionary. The values in the dictionary can be formatted and used in the string.

# String isalnum() Method:
# Check if all the characters in the text are alphanumeric:

txt = "Company12"
x = txt.isalnum()
print(x)

# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# Example of characters that are not alphanumeric: (space)!#%&? etc.

# string.isalnum()

txt = "Company 12"
x = txt.isalnum()
print(x)

# Stirng isalpha() Method
# Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x)

# The isalpha() method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.

# string.isalpha()
txt = "Company10"
x = txt.isalpha()
print(x)

String isascii() Method:
# Check if all the characters in the text are ascii characters:
txt = "Company123"
x = txt.isascii()
print(x)

# The isascii() method returns True if all the characters are ascii characters  (a-z).
# string.isascii()

# String isdecimal() Method:
# Check if all the characters in a string are decimals (0-9)
txt = "1234"
x = txt.isdecimal()
print(x)

# The isdecimal() method returns True if all the characters are decimals (0-9).
# This method can also be used on unicode objects.

# string.isdecimal()

# String isdigit() Method:
