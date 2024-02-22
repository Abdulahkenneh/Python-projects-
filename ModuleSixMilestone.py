import time
import sys
# Oumar Kenneh

inventories = {}
list =[]

rooms = {
    'Great Hall': {'East': 'Foyer',"North":"Living Room"},
    "Foyer":{"West":"Great Hall"},
    "Living Room":{"West":"Altic","East":"Bed Room","North":"Dinning Room","South":"Great Hall"},
   "Altic":{"East":"Living Room"},
   "Bed Room":{"North":"Library","West":"Living Room"},
   "Library":{"South":"Bed Room"},
   "Dinning Room":{"West":"Basement","East":"Ghost Room","south":"Living Room"},
   "Basement":{"East":"Dinning Room"},
   "Ghost Room":{"West":"Dinning Room"}   
}





def move_to_room(current_room, direction):
    """Attempts to move to a room in the specified direction from the current room."""
      
    
    
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
        
        
    else:
        print("You can't go that way.")
        return current_room

   



def main():
    items = {
    'Great Hall': "ghost",
    "Foyer":"key",
    "Living Room":"candlestick",
   "Altic":"Matchbox",
   "Bed Room":"Nife",
   "Library":"golden book",
   "Dinning Room":"flashlight",
   "Basement":"Diamond",
   "Ghost Room":""   
}
    current_room = 'Great Hall'  
   # Starting room


    while True:
        print('\nYou are in the', current_room)
        
      
        print('\nEnter your best move if it is correct without the interferance of the ghost room,we will add an item to your inventories that is belonging to that room.')
        print('Make a move (North, South, East, West) or "exit" to end the game: \n')
        command = input("> ").capitalize()
        print(current_room)
        
       # if current_room =="Ghost Room":
           # break  
        if command == 'Exit':
                print("Are you sure you want exist the game ?")
        
                if input("\n>").lower().startswith("yes"):
                    print('Exiting the game. Thanks for playing!')
                    exit()
                else:
                    main()
        elif command in ['North', 'South', 'East', 'West']:
                current_room = move_to_room(current_room, command)
                if current_room =="Ghost Room":
                    print("I am sorry you lost try again !!!")
                    break
                if items[current_room] not in list and items[current_room] !="":
                     list.append(items[current_room])
                     print("Invenrories: ",list)
                     if len(list) == 7:
                         print("\nCongratulation you won the game")
                         res = input("Do you still want to play? ").lower()
                         if res=="yes":
                             move_to_room(current_room, command)
                         elif res =="no":
                             exit()
                         else:
                             print("Sorry I dont understand that ")
                         
                elif items[current_room] =="ghost":
                    print("Im sorry you have lost the game !!") 
                    break           
                else:
                    print(list)
           
        else:
             print('Invalid command. Please try again.')
             add_inventories(current_room,items)        
    


if __name__ == "__main__":
    main()




    