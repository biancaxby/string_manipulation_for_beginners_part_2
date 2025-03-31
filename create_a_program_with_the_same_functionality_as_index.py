# Create a program with the same functionality as index

# Ask user for input
print('This program will mimic the function of index without using it')
user_input = input('Say something: ')
find_word = input('What do you want to find?: ')

# Locate the first appearance of the word
if find_word in user_input:
    word_finder = user_input.find(find_word)
    print(f'The word you are looking for is in {word_finder}')

else:
    print('The word you are looking for is not here')