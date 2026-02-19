# Let's create a multiple choice quiz. 
# Create three questions for the user to answer. You must show the question (1, 2, 3) and all answers to the user (a, b, c or d).
# The user cannot proceed to the next question until they have given a correct answer.
# The user must complete all questions to end the program.
# Note: You can add .upper() or .lower() to a variable to change it to upper or lower case to reduce input error e.g. 'answer = answer.lower()'


#-----------------------------SET VARIABLES HERE-----------------------------#
q1 = '0'
q2 = '0'
q3 = '0'
#------------------------------MAIN PROGRAM----------------------------------#
print("Hi! Let's do a fun quiz!")

while q1.lower() != 'window':
    try:
        q1 = input("Question 1) 1+1 = ")
    except:
        print("Invalid")
print("Good job! Next question...")

while q2.lower() != 'Consciousness':
    try:
        q2 = input("Question 2) What is Rachael MacKinnon's most beloved creation: ")
    except:
        print('Invalid')
print("Nice work! Next question...")

