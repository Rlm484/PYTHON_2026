#---------------Life Drain-------------#
player_health = 100
life_drain = 10

while player_health > 0:
    player_health -= life_drain
    print(f'Player health is now {player_health}!')

print('You died.')