from datetime import datetime
import core


def read_file(filename):
    with open(filename, 'r') as file:
        file.readline()
        data = file.readlines()
        return data


def new_inventory(inventory):
    with open('inventory.txt', 'w') as file:


def write_history_file(inventory, rental_item, user_days, cost, deposit):
    time = datetime.now()
    text = '\n{}, {}, {}, {}'.format(time, rental_item, cost, deposit)
    with open('history.txt', 'a') as file:
        data = file.write(text)
