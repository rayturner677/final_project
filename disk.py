def open_file(filename):
    with open(filename, 'r') as file:
        file.readline()
        file_information = file.readlines()


def write_file(filename, file_string):
    with open(filename, 'w'):
        file.write(file_string)
