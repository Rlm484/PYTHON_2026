# Initialize variables to store the first name and surname
first_name = ''
surname = ''

# Define a function to get the user's first name and surname
def getName():
    # Use the global keyword to modify the global variables
    global first_name, surname  
    
    # Prompt the user to enter their first name and store it in the first_name variable
    first_name = input('Enter first name: ')
    # Prompt the user to enter their surname and store it in the surname variable
    surname = input('Enter surname: ')

# Define a function to print the user's full name
def fullName():
    # Use the global keyword to access the global variables
    global first_name, surname  

    # Print the full name by combining the first name and surname
    print(f'{first_name} {surname}')

# Call the getName function to get the user's first name and surname
getName()
# Call the fullName function to print the user's full name
fullName()
