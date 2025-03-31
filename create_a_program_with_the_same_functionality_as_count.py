# Create a program with the same functionality as count

# Initialize variables
word_counter = 0

# Ask user for input
print('This program shall mimic the function of count')
user_input = input('Say something: ')
count = input('What do you want to count?: ')

# Separate the words 
split_words = user_input.split()
for word in split_words:
    if word == count :
        word_counter += 1  

   

print((word_counter))