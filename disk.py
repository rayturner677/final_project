from datetime import datetime
import core


def read_file():
    with open('inventory.txt', 'r') as file:
        data = file.readlines()
    inventory = {}
    for item_info in data:
        item = item_info.split(',')
        item_name = item[0].strip()
        price = int(item[1].strip())
        stock = int(item[2].strip())
        replacement = int(item[3].strip())
        inventory[item_name] = {
            'name': item_name,
            'price': price,
            'stock': stock,
            'replacement': replacement
        }
    return inventory


def write_history_file(inventory, rental_item, user_days, cost, deposit):
    time = datetime.now()
    text = '\n{}, {}, {}, {}'.format(time, rental_item, cost, deposit)
    with open('history.txt', 'a') as file:
        data = file.write(text)
