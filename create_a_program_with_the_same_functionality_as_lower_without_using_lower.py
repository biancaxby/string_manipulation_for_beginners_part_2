# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Ask user for input
statement = input('Enter whatever you want to say: ')

# Convert the input made by user to lowercase
lowercase = statement.casefold()

# Print output
print(lowercase)