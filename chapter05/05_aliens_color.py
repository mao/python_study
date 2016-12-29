import random

alien_colors = ['green', 'red', 'yellow', 'black', 'white']

def get_alien_points( choice ):
    if alien_colors[choice] == 'green':
        print('Congratulate, you got 5 points!')
        return 5
    else:
        print('Sorry, you missed this chance.')
        return 0

scores = 0

for i in range(0, 1000):
    choice = random.randint(0, 4)
    scores += get_alien_points(choice)

print('Congratulate, your scores are:', scores)