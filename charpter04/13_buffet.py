foods = ('noodle', 'pizza', 'hamburger', 'chips', 'steak')


def print_buffet(foods):
    print('\nThe buffet provide:')
    for food in foods:
        print(food.title())

print_buffet(foods)

#  It would go wrong!
# foods[1] = 'Pasta'

foods = ('noodle', 'sandwich', 'hot dog', 'chips', 'steak')
print_buffet(foods)