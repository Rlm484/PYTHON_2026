# Week 6 - Modules 8 and 9
Let's go a bit deeper into functions before completing the activities...

## Structure
The structure of our code is now going to change, as we want to set **global variables**, then setup **functions**, then run our **functions** at the bottom.

    #--------------------Name of Program---------------------#
        Name your program

    #-----------------Setup Global Variables-----------------#
        Setup variables that are required for whole program to run.

    #--------------------Setup Functions---------------------#
        Setup functions that you will use in your program.

    #--------------------Run functions-----------------------#
        Mostly just run your functions here - most code should now be in a function, so this should not be too long!

## What is a Global Variable?
We cannot just use all variables in our functions if they are declared outside of the function. Now there are two ways we can go about this. In Grok Learning you have learned to take variables as parameters, then return values and restore them in variables. 

However, there is also another way. To change outside variables inside the function, we can redeclare them inside the function as **global variables**.

### Why not just use return?
Now, return is usually the **cleaner** solution if you do not need to use the variable in other functions. However, if you want to user the variable **in many functions**, it is best if we use a **global variable**. 

### Declaring Global Variables
Declaring them is easy! Let's look at the following program of changing a username:

    #-----------------Username Change System-----------------#

    #-----------------Setup Global Variables-----------------#
    username = 'jake_p'

    #--------------------Setup Functions---------------------#
    def username_change():
        global username

        username = input('Enter new username: ')
        print(f'Your new username is {username}')

    #---------------------Run functions----------------------#
    username_change()

### Return Statement
Now the above could have just as easily been done using a return statement and parameters and it would likely be cleaner:
    #-----------------Username Change System-----------------#

    #---------------------Setup Variables--------------------#

    #--------------------Setup Functions---------------------#
    def username_change():
        username = input('Enter new username: ')
        return username

    #---------------------Run functions----------------------#
    print(username_change())

Now please note that the above is only more appropriate **because we do not need to use just ONE variable throughout several functions.**

### Example of Where to use Globals
The above example was better solved with a return statement, but sometimes a global variable makes more sense. 

For instance, if I am creating a game, and need to track the player's position, health, attack and other properties through multiple different functions (e.g. movement, enemy attack, boss fight, traps), a global variable would make more sense. This is because the player only has **one of each of these attributes**, but this **one value** may change due to **multiple different game functions**. 
