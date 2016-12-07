''' A simple start to a text maze game with a single path thru the maze
Players have to choose the correct direction to get out of a room.

This also is an introduction to making objects in Python.
'''
import random

class Player:
    
    def __init__ (self, name, room):
        self.things = ['marshmallow']   #list of objects
        self.commands =['eat', 'hit']
        self.visited=[]
        self.lifes = 2
        self.name = name
        self.room = room
        self.action = {'hit':'You hit the cat with a marshmallow',\
         'eat':'You eat the marshmallow'}
        
    def info(self):
        print ('Hi {}.  Your room {}. You have {} lifes left \n' \
        .format(self.name, self.room, self.lifes))
        print ('You have been to these rooms.'+ str(self.visited))
        print ('*'* 60)
        
    def change_room(self):
         self.room = random.randint(0,2)  # random maze
         self.visited.append(self.room)   # where have I already been
         print (self.visited)
         if 1 in self.visited:
             print ('Been there, done that')
             #self.change_room()
         else:
            print ('You must be new here')
         #self.room += 1      #code for a sequential maze
         return (self.room)

    def take(self, thing):
        pass
        
    def inventory(self):
        print (self.things)
        
    def win(self):
        print ('Congratulations, You have completed the maze')
        #play again?

    def lose(self):
        self.lifes = self.lifes -1
        if self.lifes == 0:
            print ('Sorry Jack, Your dead!')

    def mallow(self, action):
        action = str.lower(action)
        print (self.action[action] + '\n\n')
            
