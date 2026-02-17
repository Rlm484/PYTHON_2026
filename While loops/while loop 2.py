#---------------Correct Age Game--------------#
guess = 0
age = 21

while guess != age:
    try:
        guess = int(input("Guess Mr Scott's age: "))
    except:
        print("Come on mate, not hard to enter a number.")

print('Correct!')