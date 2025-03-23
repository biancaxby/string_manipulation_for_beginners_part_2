# Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# ask user for input
print('Enter your fullname with a LOT of spaces in the beginning and this program will remove the spaces.')
name = input('Enter your name here: ')

# remove the spaces on the beginning of the name
print(name.lstrip())