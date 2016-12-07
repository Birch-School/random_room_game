import random
#imports the methods into this namespace, less typing
from player import *

def r1(player):
    print ('You are sitting in a large dim room')
    
def r2(player):
    pass

def r4(player):
    print("...Must have been a painting, then")

###########################  Setup game here ###########

#************************** Load the rooms **************
room =[]       
roomslist=[]
##############  convert to a list of lists ######################
for line in open("rooms.csv"):
    line = line.strip('\n')         # lose the newline characters
    room = line.split(",")          # single room list
    roomslist.append(room)          # list ofall the room lists
# print (roomslist) 
###############  make into a dictionary ######################
#************ this version just uses the list, *****************
'''     all lines between triple quotes are comments!!
keys = []
number_of_rooms = (len(roomslist))
for i in range(number_of_rooms):
    keys.append(i)
rooms = dict(zip(keys, roomslist))
#print (rooms)
'''
############### ############Start a player ######################
player = Player('Arlin', 1)
room = player.change_room()     
#  change_room()  call to local function

############################ Game Loop #########################
while True:
    print (player.info())
    room = player.change_room()
    rm_name, rm_describe, rm_item = roomslist[room][0], roomslist[room][1],\
    roomslist[room][2]
    print ('{}, You are in {}, {}'.format(player.name, rm_name,rm_describe))  
    print ('There is a {} here - you take it.'.format(rm_item))
    player.things.append("{}".format(rm_item))
    print('Your inventory is now:')
    print(player.inventory())
    input("Pause...")
