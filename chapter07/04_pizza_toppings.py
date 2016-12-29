active = True
toppings = []

while active:
    topping = input('Please tell us what toppings you\'d like? Enter ok to quit ')
    if topping.lower() == 'ok':
        active = False
    else:
        print('We will add', topping.lower(), 'into it.')
        toppings.append(topping)

statement = "We will add "
index = 0
for topping in toppings:
    if index == 0:
        index += 1
    else:
        statement += ', '
    statement += topping

statement += ' into your pizza. Thank you!'

print('\n' + statement)