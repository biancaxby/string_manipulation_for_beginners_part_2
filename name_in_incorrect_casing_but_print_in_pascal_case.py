# Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# ask user for input
print('Enter your fulllname and this program will convert it into a Pascal case!')
name = input('Enter your name here: ')

# convert the first letter of the name
capitalized_name = name.title()

# remove spaces in between the name
pascal_case = capitalized_name.replace(" ", "")

print(pascal_case)