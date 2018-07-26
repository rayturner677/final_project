import core
import disk
from datetime import datetime


def in_stock(inventory, stock):
    for item_name in inventory:
        if inventory[item_name]['stock'] != 0:
            return
    else:
        False


def add_to_stock(inventory, stock):
    new_inv += 1
    return new_inv


def main():
    read = disk.open_file
    inventory = {
        'camaro': {
            'name': 'camaro',
            'price': 180 * 1.07,
            'stock': 4,
            'replacement': 150
        },
        '4-wheeler': {
            'name': '4-wheeler',
            'price': 29 * 1.07,
            'stock': 15,
            'replacement': 150,
        },
        'skeet jet': {
            'name': 'skeet jet',
            'price': 43 * 1.07,
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
        if inventory['camaro']['stock'] == 0:
            break
        if inventory['4-wheeler']['stock'] == 0:
            break
        if inventory['skeet jet']['stock'] == 0:
            break
        while True:
            user_choice = input('What would you like to rent today ' + name +
                                '?').strip().lower()
            if user_choice == 'camaro':
                receipt.append(inventory['camaro'])
                inventory['camaro']['stock'] -= 1
                print(inventory['camaro'])
                break
            elif user_choice == '4-wheeler':
                receipt.append(inventory['4-wheeler'])
                inventory['4-wheeler']['stock'] -= 1
                print(inventory['4-wheeler'])
                break
            elif user_choice == 'skeet jet':
                receipt.append(inventory['skeet jet'])
                print(inventory['skeet jet'])
                inventory['skeet jet']['stock'] -= 1
                break
            elif user_choice == 'done':
                break
            else:
                print('invalid request')
                return

    while True:
        print('alive')
        break

    print(receipt)

    # def history(payment,  amount):
    #     time = datetime.now()
    #     text = '/n{}, {}, {}' .format(time , item, amount)

    # with open('history.txt', 'w') as file:
    #         file.write(text)


if __name__ == '__main__':
    main()
