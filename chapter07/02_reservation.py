seattings = input('How many people in dinner?\n')

if int(seattings) > 8:
    print('There is no table available now, do you mind confirm later?')
else:
    print('There is an available table, do you like to reserve it now?')