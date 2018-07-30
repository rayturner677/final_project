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


def find_replacement(inventory, item_name):
    inventory[item_name]['replacement'] * 1.10


def get_total(inventory, item_name, items):
    receipt = []
    total = 0
    for item in items:
        receipt.append(item)
    for item in items:
        total += inventory[item_name]['price']
    return receipt


def main():
    inventory = {
        'camaro': {
            'name': 'camaro',
            'price': 180,
            'stock': 4,
            'replacement': 40000
        },
        '4-wheeler': {
            'name': '4-wheeler',
            'price': 29,
            'stock': 15,
            'replacement': 6000,
        },
        'jet ski': {
            'name': 'jet ski',
            'price': 43,
            'stock': 8,
            'replacement': 5000
        }
    }
    sign_in = input('         Employee(1) or Costumer(2):').strip().lower()
    name = input("What's you name?").strip()
    with open('inventory.txt', 'r') as file:
        data = file.readlines()
        print(data)

    while True:
        if sign_in == '1':
            user_choice = input(
                'What would you like to rent today ' + name +
                '?', ).strip().lower()
            user_days = input(
                'How long would you like to rent our merchandise?')
            if in_stock(inventory, user_choice):
                inventory[user_choice]['stock'] -= 1
                print(inventory[user_choice])
                print('taxed :', price_with_tax(inventory, user_choice))
                cs = inventory[user_choice]['price'] * user_days.isdigit()
                print(cs)
            elif user_choice == 'done':
                break
            else:
                print('Not in stock')
        print('camaro, 4-wheeler, jet ski')
        if sign_in == '2':
            user_choice = input('What would you like to rent today ' + name +
                                '?').strip().lower()
            user_days = input(
                'How long would you like to rent our merchandise?')
            if in_stock(inventory, user_choice):
                inventory[user_choice]['stock'] -= 1
                print(inventory[user_choice])
                print('cost:', price_with_tax(inventory, user_choice))
                cs = inventory[user_days]['price'] * user_days.isdigit()
                print(cs)

            elif user_choice == 'done':
                break
            else:
                print('Not in stock')
    receipt = get_total(inventory, item_name, items)
    print(receipt)


# def history(payment,  amount):
#     time = datetime.now()
#     text = '/n{}, {}, {}' .format(time , item, amount)

# with open('history.txt', 'w') as file:
#         file.write(text)

if __name__ == '__main__':
    main()
