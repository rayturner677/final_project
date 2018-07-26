import core
import disk
from datetime import datetime


def in_stock(inventory, item_name):
    if item_name in inventory and inventory[item_name]['stock'] > 0:
        return True
    else:
        False


def price_with_tax(inventory, item_name):
    price = inventory[item_name]['price'] * 1.07
    return round(price, 2)


def add_to_stock(inventory, item_name):
    inventory[item_name]['stock'] += 1
    return


def main():
    read = disk.open_file
    inventory = {
        'camaro': {
            'name': 'camaro',
            'price': 180,
            'stock': 4,
            'replacement': 150
        },
        '4-wheeler': {
            'name': '4-wheeler',
            'price': 29,
            'stock': 15,
            'replacement': 150,
        },
        'skeet jet': {
            'name': 'skeet jet',
            'price': 43,
            'stock': 8,
            'replacement': 37
        }
    }

    # with open('history.txt', 'w') as file:
    #     file.write(text)

    name = input("What's you name?").strip()
    print('camaro, 4-wheeler, skeet jet')
    receipt = []
    while True:
        user_choice = input('What would you like to rent today ' + name +
                            '?').strip().lower()
        if in_stock(inventory, user_choice):
            receipt.append(inventory[user_choice]['price'])
            receipt append(inventory[user_choice]['replacement'])
            inventory[user_choice]['stock'] -= 1
            print(inventory[user_choice])
            print('cost:', price_with_tax(inventory, user_choice))
        elif user_choice == 'done':
            break
        else:
            print('Not in stock')

    print('total:' receipt)

    # def history(payment,  amount):
    #     time = datetime.now()
    #     text = '/n{}, {}, {}' .format(time , item, amount)

    # with open('history.txt', 'w') as file:
    #         file.write(text)


if __name__ == '__main__':
    main()
