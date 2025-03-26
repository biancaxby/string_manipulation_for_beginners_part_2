# Create a program that ask the user to input a complete statement. Print the number of words in the input.

# ask user for input
print('Enter something that you want to say!')
statement = input()
# split the sentences so that they can be read as sepearate index oer word instead of characters
split_sentence = statement.split()

print(len(split_sentence))