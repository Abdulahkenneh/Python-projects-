import random
import sys

"""Theme: Dangerous adventure 

Basic storyline: The player is drop in a huge building to hunt for treasure.  They must navigate through the mansion, collecting items that will help them get rich. However, there is a dangerous ghost haunting the mansion, and if the player encounters it before collecting all the items, they lose the game."""



class Initial_obj():
    #intialize the objext
    def __init__(self,dir,account):
    

        self.dir = dir
        self.account = account
        
    def get_direction(self):
            dir = input("""
please enter one direction of the room you want to collect treslasure:Nouth, East,South
or West > """).lower()

            account = self.account
            item = Items(dir,account)
            item.check_condition(dir)
        
    def key_room(self,item):
            self.select_items(item)             
    def dinning_room(self,item):
            self.select_items(item)
    def basement(self,item):
            self.select_items(item)
    def map_room(self,item):
            self.select_items(item)
            
    def select_items(self,item):
         print(f"\nYou are in the {item} room")
         res = input(f"Do you want to pick {item}? yes or no \n").lower()
         if res == "yes":
          self.account +=(1*10)
          print(f"\nGreat Job Your account ballance is now: {self.account} USD")
          self.get_direction()
         elif res =="no":
          self.account -=10
          print(f"Ohh!! Your account ballance is now: {self.account} USD")
          
          print("would you like to move to another room")
          quit_game()
          
          
                                            
                                                    
class Items(Initial_obj):
                                      def check_condition(self,dir):
                                          
                                          items= ["key","matchbox","candle","map"]
                                          
                                          random.shuffle(items)
                                          gost_direction = items[-1]
                                          if dir == "nouth":
                                              item = items[0]
                                              self.key_room(item)
                                          elif dir == "south":
                                              item = items[1]
                                              self.dinning_room(item)
                                          elif dir == "west":
                                              item = items[2]
                                              self.basement(item)
                                          elif dir == "east":
                                              item = items[3]
                                              self.map_room(item)
                                          elif dir == gost_direction:
                                              print("There is a Gost there do you want to see it ? yes or no")
                                              ans = input("> ").lower()
                                              if ans == "yes":
                                                  print("You fail !")
                                                  print("Gost has won ")
                               
                                              elif ans =="no":                     print("Great job! \n you have avoided the Gost ")
                                              self.get_direction()
                                          else:
                                              print("Direction invalid! ")
                                              self.get_direction()
  
          
                  
def main():
                                   account = 0
                                   while account < 5:
                                       init = Initial_obj(dir,account)
                                       init.get_direction()
                                       account +=1
                                       def quit_game():
                                           res = input("> ").lower()
                                           while True:
                                               if res =="yes":
                                                   init.get_direction()
                                               if res =="no":
                                                   break
                                                   
    
main()             
                   
                               
   


                                                                                                                                                               
             


            









           
                           

