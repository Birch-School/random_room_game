#imports the methods into this namespace, less typing
from player import *

def switchboard(player,room):
    print ('You are in room {}'.format(room))
    if room == 1:
        print ('This is not your day')
    elif room == 2:
        pass
    if 'chalk' in player.things:
        print ('Consider this Python question carefully, O seeker of Truth')
        answer = input ('What is "2" * 2?')
        if answer == '22':      # input returns a string, not a number!
            print ("You have answered correctly, Oh wise one and the powers have added a life")
            player.lifes = player.lifes = + 1
        else:
            print ("The number you seek is 22, not 4!  The magic is the quotes around the first number")
            player.lifes =  player.lifes = - 1
    print (player.lifes)
        


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
#room = player.change_room()     

############################ Game Loop #########################
while True:
    print (player.info())
    room = player.change_room()
    switchboard(player, room)
    rm_name, rm_describe, rm_item = roomslist[room][0], roomslist[room][1],\
    roomslist[room][2]
    print ('{}, You are in {}, {}'.format(player.name, rm_name,rm_describe))  
    print ('There is a {} here - you take it.'.format(rm_item))
    player.things.append("{}".format(rm_item))
    print('Your inventory is now:')
    print(player.inventory())
    input("pause")
