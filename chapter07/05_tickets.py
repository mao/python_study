active = True

while active:
    input_arg = input_arg('How old are you?\t')
    if input_arg == 'quit':
        active = False
        continue
    age = int(input_arg)
    if age < 3:
        print('Your ticket is free.')
    elif age < 12:
        print('Your ticket costs $10.')
    elif age:
        print('Your ticket costs $15.')