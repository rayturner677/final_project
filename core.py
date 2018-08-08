def in_stock(inventory, item_name):
    if item_name in inventory and inventory[item_name]['stock'] > 0:
        return True
    else:
        return False


def price_with_tax(inventory, item_name):
    price = inventory[item_name]['price'] * 1.07
    return round(price, 2)


def add_to_stock(inventory, return_choice):
    inventory[return_choice]['stock'] += 1
    return


def find_replacement(inventory, item_name):
    return int(inventory[item_name]['replacement']) * .10
