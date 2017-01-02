
filename = 'python_notes.txt'


def print_file_by_read(filename):
    try:
        with open(filename) as file_obj:
            print("\nprint_file_by_read:")
            content = file_obj.read()
            print(content)
    except FileExistsError:
        print('File not exist.')

def print_file_by_object(filename):
    try:
        with open(filename) as file_obj:
            print("\nprint_file_by_object:")
            for line in file_obj:
                print(line.rstrip())
    except FileExistsError:
        print('File not exist.')

def print_file_by_readlines(filename):
    try:
        with open(filename) as file_obj:
            lines = file_obj.readlines()
            print("\nprint_file_by_readlines:")
        for line in lines:
                print(line.rstrip())
    except FileExistsError:
        print('File not exist.')



print_file_by_read(filename)

print_file_by_object(filename)

print_file_by_readlines(filename)