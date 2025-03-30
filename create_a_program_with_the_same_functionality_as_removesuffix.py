# Create a program that has the same funtionality as removesuffix

# Ask user for input
print('This program will mimic the function of removesuffix without using it')
user_input = input('Say something: ')
remove_this = input('What do you want to remove?: ')

# Remove the what the user wants to remove
if user_input.endswith(remove_this):
    removed_suffix = user_input.replace(remove_this, "")
    print(removed_suffix)

else:
    print('Error')