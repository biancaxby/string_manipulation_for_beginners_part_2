#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.



def swapcase(user_input):
# Check if the character is in uppercase then convert it to lowercase and vice versa
    characters = ""
    for char in user_input:
        if char.isupper():
            characters += char.lower()
        else:
            characters += char.upper()
    return characters 

# Ask user for input
print('''This program will mimic the behavior of the swapcase funtion.
      And it will do so without using swapcase''')
user_input = input('Say whatever you want: ')

print(swapcase(user_input))