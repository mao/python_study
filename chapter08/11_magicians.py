def show_magicians(magicians):
    for magician in magicians:
        print(magician)

#
def make_great(magicians):
    great_magicians = []

    while magicians:
        great_magician = 'the Great ' + magicians.pop().lower().title()
        great_magicians.append(great_magician)

    while great_magicians:
        magicians.append(great_magicians.pop())

magicians = ['Jack', 'Tony', 'Abraham', 'John', 'gray']

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)