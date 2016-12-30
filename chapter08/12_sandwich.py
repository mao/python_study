def make_sandwich(*toppings):
    ordered_sandwich = 'You order a sandwich with topping: '

    l = len(toppings)
    for topping in toppings:
        ordered_sandwich += topping
        l -= 1
        if l > 0:
            ordered_sandwich += ', '

    ordered_sandwich += '.'
    print(ordered_sandwich)


make_sandwich('green peppers', 'onions', 'sausage', 'pepperoni')
make_sandwich('bacon', 'onions', 'sausage', 'pepperoni', 'hot dog')
make_sandwich('bacon')
make_sandwich('bacon', 'onions', 'sausage', 'ice cream', 'hot dog')