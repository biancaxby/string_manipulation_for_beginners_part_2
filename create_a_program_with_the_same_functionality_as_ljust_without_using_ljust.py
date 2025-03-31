# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter.
#  Create a program that do the same functionality without using ljust() function.

# Ask user for input
print('This program will mimic the ljust function without using it')
sentence = input('Say whatever you want: ')

# Format the string to add spaces to the end of the string
left_align = "{:<20}".format(sentence)

print(left_align)