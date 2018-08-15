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


def get_name():
    answer = input("What's you name?").strip()
    return answer


def sign_in():
    while True:
        answer = input('         Employee(1) or Costumer(2):').strip().lower()
        if answer in ['1', '2']:
            return answer
        else:
            print('invalid response')


def rent_or_return(name):
    print('Would you like to [rent] or [return] today ' + name + '?')
    while True:
        answer = input('>>> ').lower().replace('[', '').replace(']',
                                                                '').strip()
        if answer in ['rent', 'return']:
            return answer
        else:
            print("Invalid response.")


def get_rental_item(inventory, name):
    print('What would you like to rent?')
    print(' '.join(inventory.keys()))
    while True:
        answer = input('>>> ')
        if answer in inventory.keys():
            if core.in_stock(inventory, answer):
                return answer
            else:
                print('oops that item is not in stock... please pick another')
        else:
            print('invalid response')


def user_days():
    while True:
        answer = input('How long would you like to rent our merchandise?')
        if answer.isdigit():
            return int(answer)
        else:
            print('invalid response')


def print_receipt(name, item, days, cost, tax, deposit, total):
    print('''
    Customer Name: {}
    Renting a {} for {} days.
    \tCost: ${:.2f}
    \tTax: ${:.2f}
    \tDeposit: ${:.2f}
    TOTAL: ${:.2f}
    ''')


def rental_shell(inventory, name):
    rental_item = get_rental_item(inventory, name)
    days = user_days()
    core.rent_item(inventory, rental_item)
    cost = core.item_cost(inventory, rental_item, days)
    tax = core.get_tax(cost)
    deposit = core.get_deposit(inventory, rental_item)
    total = cost + tax + deposit
    print_receipt(name, rental_item, days, cost, tax, deposit, total)
    disk.write_history_file(inventory, rental_item, user_days, total, deposit)


# prints out instructions for this program
# def instructions():
#     print('\nTo exit enter done.')
#     print('\n' "Deposit will be refunded with return.")

# def return_choice():
#     while True:
#     answer = input('How long would you like to rent our merchandise?')
#     if answer.isdigit():
#         return answer
#     else:
#         print('invalid response')


def main():
    inventory = disk.read_file()
    name = get_name()
    print_inventory(inventory)
    decision = sign_in()

    while True:
        if decision == '1':
            # employee stuff
            # womp womp need to add more here later
            print('still working on this...')
        if decision == '2':
            decision = rent_or_return(name)
            if decision == 'rent':
                rental_shell(inventory, name)

            # elif rent_or_return() == 'return':
            #     return_choice()
            #     core.add_to_stock(inventory, return_choice)
            #     print(inventory[return_choice])

            # elif rent_or_return() == 'done':
            #     break
            # elif user_days() == '':
            #     break
            # else:
            #     print('Not in stock')
            # print(inventory.keys())
            # user_choice()
            #                      '?').strip().lower()
            # if core.in_stock(inventory, user_choice):
            #     user_days()
            #     inventory[user_choice]['stock'] -= 1
            #     print(inventory[user_choice])
            #     taxed = core.price_with_tax(inventory, user_choice)
            #     cost_indays = int(inventory[user_choice]['price'] * user_days)
            #     print('taxed:', core.price_with_tax(inventory, user_choice))
            #     print('cost with days rented:', cost_indays)
            #     taxed = core.price_with_tax(inventory, user_choice)
            #     cost_indays = inventory[user_choice]['price'] * int(user_days)
            #     replacement = core.find_replacement(inventory, user_choice)
            #     total = round(taxed + cost_indays + replacement, 2)
            #     print('total:', total)
            #     disk.write_file(inventory, user_choice, user_days)
            elif user_choice() == 'done':
                break
            else:
                print('Not in stock')


if __name__ == '__main__':
    main()
