### Strings ###

string1 = "my string"
string2 = "my other string"

print(len(string1))
print(len(string2))

print(string1 + " " + string2)

my_new_line_string = "This is a string\nwith a new line"
print(my_new_line_string)

my_tab_string = "This is a string\twith a tab"
print(my_tab_string)

my_scape_string = "This is a string with a \\ backslash"
print(my_scape_string)

# formatted strings

name, surname, age = "John" , "Doe" , 35

print("My name is {} {} and im {}".format(name, surname, age))
print("My name is %s %s and im %d"%(name, surname, age))

# print("my name is " + name + " " + surname + " and my age is " + age) # this will raise an error because age is not a string
print("my name is " + name + " " + surname + " and my age is " + str(age))
print(f"My name is {name} {surname} and im {age}") # f string

# Character unpacking

language = "Python"
a, b, c, d, e, f = language
print(a)
print(d)

# Division

language_slice = language[1:3] # this will return characters from index 1 to 2
print(language_slice)

language_slice = language[1:] # this will return from index 1 to the end
print(language_slice)

language_slice = language[-2] # this will return the last character
print(language_slice)

language_slice = language[0:6:2] # this will return characters from index 0 to 5 with a step of 2
print(language_slice)

# Reverse a string

reversed_language = language[::-1] # this will reverse the string
print(reversed_language)

# functions

print(language.capitalize()) # capitalize the first letter
print(language.upper()) # convert to uppercase
print(language.count("t")) # count the number of occurrences of a character
print(language.isnumeric()) # check if the string is numeric
print("1234".isnumeric()) # check if the string is numeric
print(language.lower()) # convert to lowercase
print(language.upper().isupper())