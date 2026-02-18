# Define a function to combine the first name and last name into a full name
def getName(first, last):
    # Concatenate the first and last names with a space in between
    full_name = f'{first} {last}'
    # Return the full name
    return full_name

# Prompt the user to enter their first name and store it in choice_1
choice_1 = input('Enter your first name: ')
# Prompt the user to enter their surname and store it in choice_2
choice_2 = input('Enter your surname: ')

# Call the getName function with the user's inputs and store the result in final
final = getName(choice_1, choice_2)
# Print the full name
print(final)
