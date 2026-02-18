fridge = "no"
while fridge.lower() != "yes":
    try:
        fridge = input('BEEP!\nIS THE FRIDGE CLOSED YET? ')
    except:
        print('BEEEEP!\nINVALID, INVALID')
print("Fridge is closed, peace returns at last")

#\n makes the words after be on a different line