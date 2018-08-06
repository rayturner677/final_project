import disk
import core
from datetime import datetime


def main():

    sign_in = input('         Employee(1) or Costumer(2):').strip().lower()
    name = input("What's you name?").strip()
    print('To exit enter done.')
    print("Deposit will be refunded with return.")

    inventory = disk.read_file()

    for item in inventory.values():
        print('{}, Price: ${}, Stock: {}, replacement: ${}'.format(
            item['name'],
            item['price'],
            item['stock'],
            item['replacement'],
        ))

    while True:
        if sign_in == '1':
            rent_or_return = input(
                'Would you like to rent or return today ' + name +
                '?', ).strip().lower()

            if rent_or_return == 'rent':
                user_choice = input('What would you like to rent?')
                if core.in_stock(inventory, user_choice):
                    user_days = input(
                        'How long would you like to rent our merchandise?')

                inventory[user_choice]['stock'] -= 1
                print(inventory[user_choice])
                print('taxed :', core.price_with_tax(inventory, user_choice))
                cost_indays = inventory[user_choice]['price'] * user_days.isdigit(
                )
                print('cost with days rented:', cost_indays)
                taxed = core.price_with_tax(inventory, user_choice)
                replacement = core.find_replacement(inventory, user_choice)
                cost_indays = inventory[user_choice]['price'] * int(user_days)
                total = round(taxed + cost_indays + replacement, 2)
                print(total)
                disk.write_file(inventory, user_choice, user_days)

            elif rent_or_return == 'return':
                return_choice = input('What item are you returning today?')
                core.add_to_stock(inventory, return_choice)
                print(inventory[return_choice])

            elif rent_or_return == 'done':
                break
            elif user_days == '':
                break
            else:
                print('Not in stock')
        if sign_in == '2':
            print('camaro, 4-wheeler, jet ski')
            user_choice = input('What would you like to rent today ' + name +
                                '?').strip().lower()
            if core.in_stock(inventory, user_choice):
                user_days = input(
                    'How long would you like to rent our merchandise?')
                inventory[user_choice]['stock'] -= 1
                taxed = core.price_with_tax(inventory, user_choice)
                cost_indays = inventory[user_choice]['price'] * user_days.isdigit(
                )
                print('taxed:', core.price_with_tax(inventory, user_choice))
                print('cost with days rented:', cost_indays)
                taxed = core.price_with_tax(inventory, user_choice)
                cost_indays = inventory[user_choice]['price'] * int(user_days)
                replacement = core.find_replacement(inventory, user_choice)
                total = round(taxed + cost_indays + replacement, 2)
                print('total:', total)
                disk.write_file(inventory, user_choice, user_days)
            elif user_choice == 'done':
                break
            else:
                print('Not in stock')


if __name__ == '__main__':
    main()
