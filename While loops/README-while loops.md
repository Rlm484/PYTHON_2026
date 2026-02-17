# While Loops
## How are they different to For loops?
While loops allow us to repeat code *while a certain condition is true*, rather than For loops which run *for a set number of times*. 

For instance, most games will run *while a character's health is more than 0*, or *while game_over is NOT true*. 

## How do we use them?
It's really quite simple and almost reads like written above. For instance, here's the structure for a game running whilst the character has health:


    character_health = 3

    while character_health > 0:
        runGame()

    print('Game Over!')

The above code will run as long as the character health does not fall down to zero. Once the character's health falls to zero or below, the program lets the user know that the game is over.

We can also check to see if something runs until it is not true, using similar operators to our IF statements. 

### Operators:
- Is equal to (==)
- Is NOT equal to (!=)
- More than (>)
- Less than (<)
- More than or equal to (>=)
- Less than or equal to (<=)

### Example of NOT equal to:

    game_over = False
    
    while game_over != True:
        
        runGame()

    print('Game Over!')
    
The above code runs UNTIL the game_over is equal to true. 

