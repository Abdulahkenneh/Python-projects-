import time
import sys
# Oumar Kenneh


rooms = {
    'Great Hall': {'East': 'Foyer',"North":"Living Room"},
    "Foyer":{"West":"Great Hall"},
    "Living Room":{"West":"Altic","East":"Bed Room","North":"Dinning Room"},
   "Altic":{"East":"Living Room"},
   "Bed Room":{"North":"Library","West":"Living Room"},
   "Library":{"South":"Bed Room"},
   "Dinning Room":{"West":"Basement","East":"Ghost Room"},
   "Basement":{"East":"Dinning Room"},
   "Ghost Room":{"West":"Dinning Room"}   
}


def move_to_room(current_room, direction):
    """Attempts to move to a room in the specified direction from the current room."""
    
    
    inventories = []
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("You can't go that way.")
        return current_room

def main():
    current_room = 'Great Hall'  
   # Starting room


    while True:
        print('\nYou are in the', current_room)
        command = input('\nEnter your move (North, South, East, West) or "exit" to end the game: \n').capitalize()
        print()

        if command == 'Exit':
            print("Are you sure you want exist the game ?")
            if input("\n>").lower().startswith("yes"):
                print('Exiting the game. Thanks for playing!')
                exit()
            else:
                main()
        elif command in ['North', 'South', 'East', 'West']:
            current_room = move_to_room(current_room, command)
        else:
            print('Invalid command. Please try again.')


if __name__ == "__main__":
    main()
    