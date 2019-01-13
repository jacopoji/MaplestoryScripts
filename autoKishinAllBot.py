import os, sys, Terminal, time, GameState, Field, Character, Context, Key
#KannaForEveryBot.py
#Author: Comicals
#10/22/18 v1.2

#--- Filter BOT---
# 0 every bot
# 1 bots only in whitelist
# 2 bots except in blacklist
idFilter        = 1
idWhiteList     = [53,102,103]
idBlackList     = []


#--- Filter MAP --- 
# 0 Follow bots in any map
# 1 Follow bots only in whitelisted maps
# 2 Follow bots except in blacklisted maps
# 3 Follow bots only in current map
goldenBeachMaps = [120040100,120040100,120040300,120041000,120041100,120041200,120041300,120041400,120041500,120041600,120041700,120041800]
mapFilter       = 1
mapWhiteList    = [100020400,101030500,120040100,120040100,120040300,120041000,120041100,120041200,120041300,120041400,120041500,120041600,120041700,120041800,103030000,102030000,105010301,211040200,260020500,261020300,240010700,224000100,251010100,103041115,221030400,221030620,271030540,273020000,240010600,260020700]
mapBlackList    = []

# Maximum time spent on each bot. 
# Set True  if you like to have your kanna stay for given time period in the map
# Set False if you like to move to next bot right after finishing kishin.
timeout         = 15
wait            = False


#########################
# Dont Touch below
#########################
visited     = []
kishinPump  = 5

def Kishin(pump=3):
    safe = True
    for player in Field.GetCharacters():
        if not Terminal.IsLocalUser(player.id):
            safe = False
    if safe:
        for i in range(pump):
            Character.UseSkill(42111003)
            time.sleep(1)
       
       
def WaitForFollow(user, startTime):
    timer = 0
    time.sleep(3)
    while (Field.GetID() != user.mapid or GameState.GetChannel() != user.channel) \
        and time.time() - startTime < timeout:
        time.sleep(1)
        timer+=1
    if Terminal.IsRushing():
        #print(Field.GetID(), user.mapid, GameState.GetChannel(), user.channel)
        if Field.GetID() != user.mapid or GameState.GetChannel() != user.channel:
            print("Failed in chasing {0} at {1} Ch{2}".format(user.charname, user.mapid, user.channel), flush=True)
        Terminal.StopRush()
   
   
def CheckIdFilter(user):
    if idFilter == 0:
        return True
    elif idFilter == 1 and user.clientid in idWhiteList:
        return True
    elif idFilter == 2 and user.clientid not in idBlackList:
        return True
    else:
        return False
   
   
def CheckMapFilter(user):
    if mapFilter == 0:
        return True
    elif mapFilter == 1 and user.mapid in mapWhiteList:
        return True
    elif mapFilter == 2 and user.mapid not in mapBlackList:
        return True
    elif mapFilter == 3 and user.mapid == Field.GetID():
        return True
    else:
        return False

def CheckKanna(user):
    if avoidKanna and user.jobid in [4211, 4212]:
        return False
    else:
        return True
       
if GameState.IsInGame() and Character.GetJob() in [4211, 4212]:
    for user in Terminal.GetLocalUsers():
        user = Terminal.GetLocalUser(user.clientid) # dynamic update
        if CheckIdFilter(user) and CheckMapFilter(user) and user.channel > 0:
            location = (user.mapid, user.channel)
            startTime = time.time()
            if location not in visited:
                visited.append(location)
                print("Kishin for {0} at {1} Ch{2}".format(user.charname, user.mapid, user.channel), flush=True)
                Terminal.SetFollowID(user.clientid)
                WaitForFollow(user, startTime)
                Kishin(kishinPump)
                while time.time() - startTime < timeout and wait:
                    time.sleep(1)