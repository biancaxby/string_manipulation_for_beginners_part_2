# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# Ask user for input
print('This program will mimic the function of a capitalize function without using it')
statement = input('Say whatever you want: ')

# Locate the first letter of the string and convert it to uppercase
capitalize = statement[:1].upper()
# Convert the rest of the string to lowercase
characters = statement[1:].lower()

# Concatinate the two variables together
joined_variables = capitalize + characters

print(joined_variables)