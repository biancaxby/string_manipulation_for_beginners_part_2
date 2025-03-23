#Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# ask user for input
print('Enter your full name and this program shall convert it into a Snake case format!')
name = input('Enter name here: ')

# convert characters to lowercase
lower_case = name.lower()

# replace the spaces to underscores
snake_case = lower_case.replace(" ", "_")

print(snake_case)