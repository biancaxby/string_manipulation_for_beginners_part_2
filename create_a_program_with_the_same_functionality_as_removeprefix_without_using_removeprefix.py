#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# Ask user for input
print('This program will mimic the funtion removeprefix( w/o using it)')
user_input = input('Give me a word or something: ')
# Ask them what to remove
prefix = input('What do you want to remove?: ')
# Replace the values that they want to remove
if user_input:
    replaced = user_input.replace(prefix, "")

print(replaced)