# Create  a program with the same functionality as rindex

# Ask user for input
print('This program will mimic the function of rindex without using it')
user_input = input('Say something: ')
word_find = input('What do you want to find?: ')

# Find the last apperance of the word
if word_find in user_input:
    last_occurence = user_input.rfind(word_find)
    print(f'The word you were looking for last appeared at {last_occurence}')

else: 
    print('It seems like the word you are looking for is not here')