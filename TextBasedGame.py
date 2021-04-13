# Christopher Sharp

def show_instructions():
    print("\nWelcome to Moreside Castle!\n"
          "Collect 6 items to win the game, or meet your demise at the hands of the Giant Troll.\n"
          "Move commands: go South, go North, go East, go West\n"
          "Add to Inventory: get 'item name'")
    print("-----------------------------------")


def player_status(inventory, current_room, rooms):
    print('\nInventory:', inventory)
    print('You are in', current_room)
    if 'item' in rooms[current_room]:
        print('You see a', rooms[current_room]['item'])
    print("-----------------------------------")


def main():
    inventory = []

    rooms = {
        'Grand Foyer': {'East': 'Great Hall'},
        'Great Hall': {'South': 'Common Room', 'North': 'Library', 'East': 'Classroom',
                       'West': 'Grand Foyer', 'item': 'Pie'},
        'Common Room': {'North': 'Great Hall', 'East': 'Dormitory', 'item': 'Scarf'},
        'Dormitory': {'West': 'Common Room', 'item': 'Wand'},
        'Library': {'South': 'Great Hall', 'East': 'Observatory', 'item': 'Book'},
        'Observatory': {'West': 'Library', 'item': 'Cloak'},
        'Classroom': {'North': 'Dungeon', 'West': 'Great Hall', 'item': 'Potion'},
        'Dungeon': {'South': 'Classroom', 'item': 'Giant Troll'}
    }

    current_room = 'Grand Foyer'

    show_instructions()

    while True:

        player_status(inventory, current_room, rooms)

        # getting user command
        command = input('Enter Command\n')

        # game movements
        if command.split()[0] == 'go':
            command = command.split()[1].capitalize()
            if command in rooms[current_room]:
                current_room = rooms[current_room][command]

                if current_room == 'Dungeon':
                    print('You are now battling the Giant Troll')
                    if len(inventory) >= 6:
                        print('Congrats! You defeated the Giant Troll')
                    else:
                        print('NOM..NOM..You were eaten by the troll')
                    break

            else:
                print('Invalid Move. There is no room to the {}'.format(command))

        elif command.split()[0] == 'get':
            command = command.split()[1].capitalize()
            if command in rooms[current_room]['item']:
                if len(command) == len(rooms[current_room]['item']):
                    inventory.append(command)
                    del rooms[current_room]['item']
                else:
                    print('Invalid input')
            else:
                print('I don\'t see that here')

        else:
            print('Invalid Command')


main()
