#imports the methods into this namespace, less typing
from player import *

def r1(player):
    print ('You are sitting in a large dim room')
    
def r2(player):
    pass

def r8(player):
    print ('Whoah ...')

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
############### ############Start a player ######################
player = Player('Arlin', 1)
# room = player.change_room()     

############################ Game Loop #########################
while True:
    print (player.info())
    room = player.change_room()
    rm_name, rm_describe, rm_item = roomslist[room][0], roomslist[room][1],\
    roomslist[room][2]
    print ('{}, You are in {}, {}'.format(player.name, rm_name,rm_describe))  
    print ('There is a {} here'.format(rm_item))
    input("pause")
