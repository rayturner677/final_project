def in_stock(inventory, item_name):
    if item_name in inventory and inventory[item_name]['stock'] > 0:
        return True
    else:
        return False


def rent_item(inventory, item_name):
    inventory[item_name]['stock'] -= 1


def item_cost(inventory, item_name, days):
    return inventory[item_name]['price'] * days


def get_tax(cost):
    return cost * 0.07


def get_deposit(inventory, item_name):
    return inventory[item_name]['replacement'] * .10


# def price_with_tax(inventory, item_name):
#     price = inventory[item_name]['price'] * 1.07
#     return round(price, 2)


def add_to_stock(inventory, return_choice):
    inventory[return_choice]['stock'] += 1
    return
