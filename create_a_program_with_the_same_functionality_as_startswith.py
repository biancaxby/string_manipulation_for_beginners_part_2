# Create a program with the same functionality as startswith

# Ask user for input
user_input = input('Say something: ')
start = input('Your statement starts wiht?: ')

# Check if the second input is in the first input
if user_input[len(start)] == start:
    print(f'It indeed starts with {start}')

else:
    print(f'Hmmm... It doesnt appear that the string starts with {start}')