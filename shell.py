import disk
import core
from datetime import datetime


def print_inventory(inventory):
    for item in inventory.values():
        print('{}, Price: ${}, Stock: {}, replacement: ${}'.format(
            item['name'],
            item['price'],
            item['stock'],
            item['replacement'],
        ))

def sign_in():
    while True:
        answer = input('         Employee(1) or Costumer(2):').strip().lower()
        if answer in ['1', '2']:
            return answer
        else:
            print('invalid response')

def get_name():
    while True:
    answer = input("What's you name?").strip()
    if answer.isalpha():
        return answer   
    else:
        print('invalid response')


# prints out instructions for this program
def instructions():
    print('\nTo exit enter done.')
    print('\n' "Deposit will be refunded with return.")


def rent_or_return():
    while True:
        answer = input('Would you like to rent or return today ' + name +
                    '?', ).strip().lower()
        if answer in ['rent', 'return']:
            return answer
        else:
            print("Invalid response.")


def get_userchoice():
    while True:
    answer =  input('What would you like to rent?')
    if answer in inventory.keys:
        return answer
    else:
        print('invalid response')


def user_days():
    while True:
    answer = input('How long would you like to rent our merchandise?')
    if answer.isdigit():
        return answer
    else:
        print('invalid response')

def return_choice():
    while True:
    answer = input('How long would you like to rent our merchandise?')
    if answer.isdigit():
        return answer
    else:
        print('invalid response')

def main():
    inventory = disk.read_file()
    print_inventory(inventory)
    

    while True:
        if sign_in() == '1':
            rent_or_return()
            if rent_or_return() == 'rent':
                user_choice()
                if core.in_stock(inventory, user_choice):
                    user_days()
                inventory[user_choice]['stock'] -= 1
                print(inventory[user_choice])
                print('taxed :', core.price_with_tax(inventory, user_choice))
                cost_indays = int(inventory[user_choice]['price'] * user_days)
                print('cost with days rented:', cost_indays)
                taxed = core.price_with_tax(inventory, user_choice)
                replacement = core.find_replacement(inventory, user_choice)
                cost_indays = inventory[user_choice]['price'] * int(user_days)
                total = round(taxed + cost_indays + replacement, 2)
                print(total)
                disk.write_file(inventory, user_choice, user_days)

            elif rent_or_return() == 'return':
                return_choice()
                core.add_to_stock(inventory, return_choice)
                print(inventory[return_choice])

            elif rent_or_return() == 'done':
                break
            elif user_days() == '':
                break
            else:
                print('Not in stock')
        if sign_in == '2':
            print(inventory.keys())
            user_choice()
                                 '?').strip().lower()
            if core.in_stock(inventory, user_choice):
                user_days()
                inventory[user_choice]['stock'] -= 1
                print(inventory[user_choice])
                taxed = core.price_with_tax(inventory, user_choice)
                cost_indays = int(inventory[user_choice]['price'] * user_days)
                print('taxed:', core.price_with_tax(inventory, user_choice))
                print('cost with days rented:', cost_indays)
                taxed = core.price_with_tax(inventory, user_choice)
                cost_indays = inventory[user_choice]['price'] * int(user_days)
                replacement = core.find_replacement(inventory, user_choice)
                total = round(taxed + cost_indays + replacement, 2)
                print('total:', total)
                disk.write_file(inventory, user_choice, user_days)
            elif user_choice() == 'done':
                break
            else:
                print('Not in stock')


if __name__ == '__main__':
    main()
