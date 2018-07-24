import disk
import core


def main():
    filename = './inventory.txt'
    # with open('inventory.txt', 'w') as file:
    #     file.write(text)

    # with open('history.txt', 'w') as file:
    #     file.write(text)

    name = input("What's you name?")
    user_choice = input('What would you like to rent today ' + name + '?')
    receipt = []
    while True:
        if choice in 'inventory.txt':
            return user_choice
            receipt.append(user_choice)


if __name__ == '__main__':
    main()
