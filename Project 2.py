"""
object_adventure.py

A text adventure with objects you can pick up and put down.
"""


# update 9/1
# create functions to develop code
#testing branches

def show_instructions():
    print('\nGiant Troll Text Adventure')
    print('Explore the castle and collect all 6 items\n'
          'before meeting the Giant Troll or meet your demise')
    print()


# data setup
rooms = {'Grand Foyer': {'name': 'Grand Foyer', 'east': 'Great Hall', 'item': []},
         'Great Hall': {'name': 'Great Hall', 'east': 'Classroom', 'south': 'Common Room', 'North': 'Library',
                        'west': 'Grand Foyer', 'item': ['pie']},
         'Common Room': {'name': 'Common Room', 'west': 'temple', 'south': 'bedroom',
                         'item': ['chains', 'thumbscrews']},
         'bedroom': {'name': 'a bedroom', 'north': 'torture', 'west': 'empty', 'contents': ['sheets', 'bed'],
                     'text': 'This is clearly a bedroom, but no one has slept\nhere in a long time.'}}
directions = ['north', 'south', 'east', 'west']
current_room = rooms['Grand Foyer']
inventory = []
show_instructions()
# game loop
while True:
    # display current location
    print()
    print('You are in {}.'.format(current_room['name']))
    print(inventory)
    # display movable objects
    if current_room['item']:
        print('In the room are: {}'.format(current_room['item']))
    print('-' * 30)
    # get user input
    command = input('\nWhat direction do you go?\n').strip().lower()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break
    # gather objects
    elif command.lower().split()[0] == 'get':
        item = command.lower().split()[1]
        if item in current_room['item']:
            current_room['item'].remove(item)
            inventory.append(item)
        else:
            print("I don't see that here.")
    # bad command
    else:
        print("I don't understand that command.")
