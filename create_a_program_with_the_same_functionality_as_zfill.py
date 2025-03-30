# Create a program with the same functionality as zfill

# Ask user for input
print('This program will mimic the function of zfill withput using it')
user_input = input('Enter a number: ')

# Add zeros to the beginning 
zero_fill = user_input.rjust(10, "0")
print(zero_fill)