# Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# ask user for input
print('Enter your name in an incorrect casing format and this program will reverse the casing!')
name = input('Enter your name here: ')
# convert the lowercase to uppercase and vice versa
print(name.swapcase())
