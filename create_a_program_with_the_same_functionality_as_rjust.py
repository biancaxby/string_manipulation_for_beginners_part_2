# Create a program with the same functionality as rjust 

# Ask user for input
print('This program will mimic the funtion of rjust without using it')
user_input = input('Say something: ')

# Format the string to add spaces on the beginning of the string
formatted_string = "{:>20}".format(user_input)

print(formatted_string)