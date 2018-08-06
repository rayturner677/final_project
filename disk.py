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


def write_file(inventory, user_choice, user_days):
    taxed = core.price_with_tax(inventory, user_choice)
    cost_indays = inventory[user_choice]['price'] * int(user_days)
    replacement = core.find_replacement(inventory, user_choice)
    total = round(taxed + cost_indays + replacement, 2)
    time = datetime.now()

    text = '\n{}, {}, {}'.format(time, inventory[user_choice]['name'], total)

    with open('history.txt', 'a') as file:
        data = file.write(text)
