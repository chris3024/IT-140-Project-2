# Christopher Sharp


# The dictionary links a room to other rooms.
rooms = {
    'Grand Foyer': {'East': 'Great Hall'},
    'Great Hall': {'South': 'Common Room', 'North': 'Library', 'East': 'Classroom',
                   'West': 'Grand Foyer', 'item': 'Pie'},
    'Common Room': {'North': 'Great Hall', 'East': 'Dormitory', 'item': 'Scarf'},
    'Dormitory': {'West': 'Common Room', 'item': 'Wand'},
    'Library': {'South': 'Great Hall', 'East': 'Observatory', 'item': 'Book'},
    'Observatory': {'West': 'Library', 'item': 'Invisibility Cloak'},
    'Classroom': {'North': 'Dungeon', 'West': 'Great Hall', 'item': 'Potion'},
    'Dungeon': {'South': 'Classroom', 'item': 'Giant Troll'}
}

# setting starting room
starting_room = 'Grand Foyer'

# setting current room
current_room = starting_room

print('\nEnter Command: go North, go South, go East, go West, or exit')
# game loop
while True:

    # Printing current room
    print('\nYou are in {}.'.format(current_room))
    print('-' * 30)

    # getting user command
    command = input('What direction do you go?\n')

    # setting exit path
    if command == 'exit':
        current_room = 'exit'
        print('Thanks for playing')
        break

    # game movements
    if command.split()[0] == 'go':
        command = command.split()[1].capitalize()
        if command in rooms[current_room]:
            current_room = rooms[current_room][command]

        else:
            print('Invalid Move. There is no room to the {}'.format(command))

    else:
        print('Invalid Command')
