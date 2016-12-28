def print_invite(guests, date='today'):
    print('Iinvited', len(guests), 'guests at', date)
    for guest in guests:
        print('Dear ' + guest + ', we sincerely invite you to dinner at ' + date + '.')

# My guest list
guests = ['Grandmother', 'Uncle Lee', 'Mother', 'Father']
date = 'New Year\'s Day'

print_invite(guests, date)

canceled_guest = guests[0]
print('\nI am sorry to know that ' + canceled_guest + ' can\'t attend the dinner at New Year\'s Day. \n')

i = guests.index(canceled_guest)
guests[i] = 'Sister'

print_invite(guests, date)


