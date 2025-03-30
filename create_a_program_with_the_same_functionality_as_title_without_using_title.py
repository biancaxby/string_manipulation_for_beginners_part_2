#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# Ask user for input
statement = input("Enter whatever you want to say: ")

# Separate the sentences 
strip_statement = statement.split()
# Locate the first letter per word in the list 
capital = [word[0].upper() + word[1:].lower() if len(word) > 0 else "" for word in strip_statement]


print(" ".join(capital))