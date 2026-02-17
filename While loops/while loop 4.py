#---------------Get Loot--------------#
locked = True
lockpick = ''


while locked is True:
    lockpick = input('Chest is locked. Enter "Y" to pick lock: ')
    
    if lockpick.lower() == 'y':
        locked = False
    else:
        print('Chest is locked.')

print('Chest unlocked. Enjoy loot.')