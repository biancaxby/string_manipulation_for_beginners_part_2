#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# Assign values to the variables
sentence = "Witness the might of the seas!"

# Add spaces on the left to make the value on the center
center_substitute = sentence.rjust(65)

# Print the output
print(center_substitute)