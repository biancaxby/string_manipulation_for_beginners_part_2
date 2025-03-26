# Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

# ask user for input 
print('Enter your fullname with the incorrect casing and this program will convert it into proper casing!')
fullname = input('Enter name here: ')

# use title function to convert the improper casing to a proper one
print(fullname.title())