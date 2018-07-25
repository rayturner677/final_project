import core
from datetime import datetime


def main():
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

    with open('inventory.txt', 'r') as file:
        file.readlines()
        line = file.readlines
    file = 'inventory.txt'
    # with open('history.txt', 'w') as file:
    #     file.write(text)

    name = input("What's you name?")
    print('camaro, 4-wheeler, skeet jet')
    user_choice = input('What would you like to rent today ' + name + '?')
    receipt = []
    while True:
        if user_choice == 'camaro':
            receipt.append(inventory['camaro'])
            inventory['camaro']['stock'] -= 1
            print(inventory['camaro'])
            break
        if user_choice == '4-wheeler':
            receipt.append(inventory['4-wheeler'])
            inventory['4-wheeler']['stock'] -= 1
            print(inventory['4-wheeler'])
            break
        if user_choice == 'skeet jet':
            receipt.append(inventory['skeet jet'])
            print(inventory['skeet jet'])
            inventory['camaro']['stock'] -= 1
            break
        else:
            print('invalid request')
            break

    print(receipt)

    # def history(payment,  amount):
    #     time = datetime.now()
    #     text = '/n{}, {}, {}' .format(time , payment, amount)

    # with open('history.txt', 'w') as file:
    #         file.write(text)


if __name__ == '__main__':
    main()
