# Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# ask user for input
number = input('Enter a number 0-1000: ')

# set the digits to a 6 number format and fill the ramaining numbers with zeros
num_with_zeros = number.zfill(6)

print(num_with_zeros)