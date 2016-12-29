sandwich_orders = ['tuna sandwich', 'eggs sandwich', 'bacon sandwich', 'ham sandwich']
finished_orders = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print('I made your', sandwich + '.')
    finished_orders.append(sandwich)

print('\nI have made', finished_orders)