# Create a program that ask the user to input a complete statement. Print the number of words in the input.

print('Enter something that you want to say!')
statement = input()
split_sentence = statement.split()

print(len(split_sentence))
