#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Ask user for input
sentence = input('Enter a sentence: ')

# Check if the input is all in capital letters
# Print 'True' if the input is all in capital letters
if sentence == sentence.upper():
    print('True')

else:
    print('False')