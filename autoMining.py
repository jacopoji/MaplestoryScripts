#Auto-miner/harvester
#V1.2
# By iNeedMahBlitz
# 6/6/2018

import Character
import GameState
import DataType
import Field
import Key
import time
import Terminal

silvervein = 200000
magentavein = 200001
bluevein = 200002
brownvein = 200003
emeraldvein = 200004
goldvein = 200005
aquamarinevein = 200006
redvein = 200007
blackvein = 200008
purplevein = 200009
#-----#
silverherb = 100000
magentaherb = 100001
blueherb = 100002
brownherb = 100003
emeraldherb = 100004
goldherb = 100005
aquamarineherb = 100006
redherb = 100007
blackherb = 100008
purpleherb = 100009

#Brown Vein = 200003
#Y Key = 0x59
#Intermediate Harvesting Farm Map = 910001012

mineID = 200003 # Can change this to the reactor ID of the vein you want to mine
npcKey = 0x20 
miningMap = 910001012 #Map ID for the brown veins

def telePortToLoc(x,y):
   print("Start Function. Going to Teleport")
   time.sleep(1)
   Character.Teleport(x,y)
   print("Teleported to ("+str(x)+","+str(y)+")")
   time.sleep(2)
   print("Done Teleport Function")


def keyPress(key):
   time.sleep(0.25)
   Key.Press(key)

def cmpT(t1, t2):
  return sorted(t1) == sorted(t2)

def checkAgain(portalToCheck):
   portal=Field.FindReactor(mineID)
   print("Old Portal Co-ordinates: "+str(portalToCheck.x)+","+str(portalToCheck.y))
   print("New Portal Co-ordinates: "+str(portal.x)+","+str(portal.y))
   if portal.valid:
       if(cmpT((portal.x,portal.y),(portalToCheck.x,portalToCheck.y))):
           print("Logging out.")
           Terminal.Logout()
       else:
           print("x/y not the same; continuing...")



def findMine():
   print("Finding mine.")
   time.sleep(2)
   portal = Field.FindReactor(mineID)
   print("Mine Found")
   if portal.valid:
       print("Mine Valid")
       telePortToLoc(portal.x-50, portal.y)
       time.sleep(3.5)
       print("Hitting NPC Key")
       Key.Press(npcKey)
       print("Done hitting NPC Key, should have finished mining that shit.")
       time.sleep(4.5)
       checkAgain(portal)

if GameState.IsInGame():
   field_id = Field.GetID()
   if(field_id == miningMap):
       findMine()
   else:
       print("Not in the right map.")
       time.sleep(10)
else:
    print("Character is either offline or hasn't logged in yet.")
    time.sleep(10)