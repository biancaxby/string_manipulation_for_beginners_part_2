#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Assign variables first
statement = input('Say whatever you want: ')
locate = input('What do you want to find?: ')

# Use find or index to locate the ending symbol or word
if statement[-len(locate)] == locate:
    print(f"Found it! It's in the end of the statement!")

else:
    print(f'{locate} is not in the end')
