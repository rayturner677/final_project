def make_inv(data):
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


def updated_inv(inventory):

    for item in inventory:
        item


def in_stock(inventory, item_name):
    if item_name in inventory and inventory[item_name]['stock'] > 0:
        return True
    else:
        return False


def rent_item(inventory, item_name):
    inventory[item_name]['stock'] -= 1
    print(inventory[item_name])


def item_cost(inventory, item_name, days):
    return inventory[item_name]['price'] * days


def get_tax(cost):
    return cost * 0.07


def get_deposit(inventory, item_name):
    return inventory[item_name]['replacement'] * .10


def return_item(inventory, return_choice):
    inventory[return_choice]['stock'] += 1
    print('deposit refunded')
    return
