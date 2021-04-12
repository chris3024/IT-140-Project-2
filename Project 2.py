# Christopher Sharp

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# setting starting room
starting_room = 'Great Hall'

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
