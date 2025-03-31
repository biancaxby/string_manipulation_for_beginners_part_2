# Create a program with the same funtionality as upper

# Ask user for input
print('This program will mimic the function of upper without using it')
user_input = input('say something: ')

# Convert all of the characters to lowercase then use swapcase
lower_case = user_input.lower()

print(lower_case.swapcase())
