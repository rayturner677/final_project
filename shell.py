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
    return int(inventory[item_name]['replacement']) * .10


def get_total(inventory, item_name, items):
    receipt = []
    total = 0
    for item in items:
        receipt.append(item)
    for item in items:
        total += inventory[item_name]['price']
    return receipt
    print(receipt)


def main():

    sign_in = input('         Employee(1) or Costumer(2):').strip().lower()
    name = input("What's you name?").strip()
    print('To exit enter done.')

    print("Deposit will be refunded with return.")
    with open('inventory.txt', 'r') as file:
        data = file.readlines()
        print(data)
    inventory = {}
    for item_info in data:
        item = item_info.split(',')
        item_name = item[0].strip()
        price = int(item[1].strip())
        stock = int(item[2].strip())
        replacement = item[3].strip()
        inventory[item_name] = {
            'name': item_name,
            'price': price,
            'stock': stock,
            'replacement': replacement
        }
    while True:
        if sign_in == '1':
            user_choice = input(
                'What would you like to rent today ' + name +
                '?', ).strip().lower()
            if in_stock(inventory, user_choice):
                user_days = input(
                    'How long would you like to rent our merchandise?')
                inventory[user_choice]['stock'] -= 1
                print(inventory[user_choice])
                print('taxed :', price_with_tax(inventory, user_choice))
                cost_indays = inventory[user_choice]['price'] * user_days.isdigit(
                )
                print('cost with days rented:', cost_indays)
                time = datetime.now()
                taxed = price_with_tax(inventory, user_choice)
                replacement = find_replacement(inventory, user_choice)
                cost_indays = inventory[user_choice]['price'] * int(user_days)
                total = round(taxed + cost_indays + replacement, 2)
                text = '\n{}, {}, {}'.format(
                    time, inventory[user_choice]['name'], total)
                with open('history.txt', 'a') as file:
                    data = file.write(text)
            elif user_choice == 'done':
                break
            elif user_days == '':
                break
            else:
                print('Not in stock')
        if sign_in == '2':
            print('camaro, 4-wheeler, jet ski')
            user_choice = input('What would you like to rent today ' + name +
                                '?').strip().lower()
            if in_stock(inventory, user_choice):
                user_days = input(
                    'How long would you like to rent our merchandise?')
                inventory[user_choice]['stock'] -= 1
                taxed = price_with_tax(inventory, user_choice)
                cost_indays = inventory[user_choice]['price'] * user_days.isdigit(
                )
                print('taxed:', price_with_tax(inventory, user_choice))
                print('cost with days rented:', cost_indays)
                time = datetime.now()
                text = '/n{}, {}, {}'.format(
                    time, inventory[user_choice]['name'], total)
                with open('history.txt', 'a') as file:
                    data = file.write(text)
            elif user_choice == 'done':
                break
            else:
                print('Not in stock')
        taxed = price_with_tax(inventory, user_choice)
        cost_indays = inventory[user_choice]['price'] * int(user_days)
        replacement = find_replacement(inventory, user_choice)
        total = taxed + cost_indays + replacement
        print('total:', total)


if __name__ == '__main__':
    main()
