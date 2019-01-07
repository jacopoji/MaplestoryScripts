import Character,Context,DataType,Field,Inventory,Key,Npc,Packet,Quest,Terminal,time,GameState,sys,os,Party, json,math,Login

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "/SunCat")

try:
	import SunCat, SCLib, SCHotkey
except:
	print("Couldn't find SunCat module")

def startQuest(quest, npc):
    print("Starting quest {0} from npc {1}".format(quest, npc))
    Quest.StartQuest(quest, npc)
    time.sleep(1)

def completeQuest(quest, npc):
    print("Completing quest {0} from npc {1}".format(quest, npc))
    Quest.StartQuest(quest, npc)
    time.sleep(1)

def needQuest(id):  # quest hasn't been accepted
    return Quest.GetQuestState(id) == 0

def hasQuest(id):  # quest is active
    return Quest.GetQuestState(id) == 1

def doQuest(id):  # quest isn't complete/turned in
    return Quest.GetQuestState(id) != 2

def doneQuest(id,npc):
    return Quest.CheckCompleteDemand(id, npc) == 0

def rush(mapid):
    Terminal.Rush(mapid)

def kami(switch):
    Terminal.SetCheckBox("Kami Vac",switch)
q1 = 34249
q2 = 34250
q3 = 34251
q4 = 34252
q5 = 34253
q6 = 34254
q7 = 34255
q8 = 34256
q9 = 34257
q10 = 34258
q11 = 34259
q12 = 34260
q13 = 34261
q14 = 34262
q15 = 34263
npc1 = 3003422
npc2 = 3003420
npc3 = 3003421
npc4 = 3003423
npc5 = 3003424
npc6 = 3003425
npc7 = 3003426
npc8 = 3003427
npc9 = 3003428
npc10= 3003429
npc11= 3003430
#StartQuest(34249, 3003422)
#in map 450005400 , talk to StartQuest(34249, 3003422)
#time sleep(5) until map 450006000
#go to map 450006010 StartQuest(34250, 3003420 teleport to 371 -687 for kanna  CompleteQuest(34250, 3003420)
#StartQuest(34251, 3003420) then go to map 450006030 CompleteQuest(34251, 3003421)
#StartQuest(34252, 3003421) teleport to 220 -417 for kanna CompleteQuest(34252, 3003421)
#time.sleep(10) until map 450006040 go to map 450006130 then go to map 450006110 teleport to -2059 -473 StartQuest(34253, 3003423) tp to -465 -656 for kanna
#teleport to -2059 -473 CompleteQuest(34253, 3003424) time.sleep(7) StartQuest(34254, 3003425)
#in map 450006130 teleport to 1956 -449 CompleteQuest(34254, 3003426)
#in map 450006130 StartQuest(34255, 3003426) go to map 450006140
#for kanna tp -963 24 check complete go back 450006130 CompleteQuest(34255, 3003426)
#StartQuest(34256, 3003427) go to map 450006150 for kanna tp -188 -298 done go back to 450006130
#CompleteQuest(34256, 3003427) StartQuest(34257, 3003427) tp to -344 24 CompleteQuest(34257, 3003425) sleep(10)
#in map 450006240 StartQuest(34258, 3003428)
#in map 450006240 CompleteQuest(34258, 3003429) StartQuest(34259, 3003429) go to map 450006210 tp 418 25 for kanna
#find item 2437666 in inventory use it until quest complete
#go back to 450006240 CompleteQuest(34259, 3003429) StartQuest(34260, 3003428) time.sleep(10)
#in map 450006240 StartQuest(34261, 3003429) go to 450006220 for kanna tp 485 25
#go back to 450006240 CompleteQuest(34261, 3003429) sleep(15) StartQuest(34262, 3003428) time.sleep(10)
#in map 450006300 StartQuest(34263, 3003430) for kanna tp 1482 297 go back -233 30 CompleteQuest(34263, 3003430) sleep(10)
currmap = Field.GetID()
job = Character.GetJob()
pos = Character.GetPos()
if GameState.IsInGame():
    if doQuest(q1):
        if needQuest(q1):
            startQuest(q1,npc1)
        time.sleep(1)
    elif doQuest(q2):
        if needQuest(q2):
            if currmap == 450006000:
                Terminal.Rush(450006010)
            elif currmap == 450006010:
                time.sleep(5)
                startQuest(q2,npc2)
            else:
                time.sleep(3)
        elif hasQuest(q2):
            if doneQuest(q2,npc2):
                completeQuest(q2,npc2)
            elif job == 4212 and pos.x != 371:
                Character.Teleport(371,-687)
                time.sleep(3)
            else:
                time.sleep(3)
    elif doQuest(q3):
        if needQuest(q3):
            if currmap == 450006010:
                startQuest(q3,npc2)
            else:
                Terminal.Rush(450006010)
                time.sleep(2)
        elif hasQuest(q3):
            if currmap != 450006030:
                Terminal.Rush(450006030)
            elif doneQuest(q3,npc3):
                completeQuest(q3,npc3)
            else:
                time.sleep(3)
    elif doQuest(q4):
        if needQuest(q4):
            if currmap != 450006030:
                Terminal.Rush(450006030)
            elif currmap == 450006030:
                startQuest(q4,npc3)
            else:
                time.sleep(3)
        elif hasQuest(q4):
            if doneQuest(q4,npc3):
                completeQuest(q4,npc3)
                time.sleep(10)
            elif job == 4212 and pos.x != 220:
                Character.Teleport(220,-417)
                time.sleep(3)
            else:
                time.sleep(3)
    elif doQuest(q5):
        if needQuest(q5):
            if currmap == 450006040:
                rush(450006130)
                time.sleep(3)
            elif currmap == 450006130:
                rush(450006110)
                time.sleep(3)
            elif currmap == 450006110:
                kami(False)
                Character.Teleport(-2059,-473)
                time.sleep(1)
                startQuest(q5,npc4)
                kami(True)
        elif hasQuest(q5):
            if doneQuest(q5,npc5):
                if pos.x != -2059:
                    kami(False)
                    Character.Teleport(-2059,-473)
                    time.sleep(1)
                else:
                    completeQuest(q5,npc5)
                    time.sleep(7)
                    kami(True)
            elif job == 4212 and pos.x != -465:
                Character.Teleport(-465,-656)
                time.sleep(3)
            else:
                time.sleep(3)
    elif doQuest(q6):
        if needQuest(q6):
            if currmap == 450006130:
                startQuest(q6,npc6)
            else:
                rush(450006130)
                time.sleep(1)
        elif hasQuest(q6):
            if doneQuest(q6,npc7):
                if currmap == 450006130:
                    if pos.x != 1956:
                        kami(False)
                        Character.Teleport(1956,-449)
                        time.sleep(1)
                    else:
                        completeQuest(q6,npc7)
                        time.sleep(1)
                        kami(True)
                else:
                    rush(450006130)
    elif doQuest(q7):
        if needQuest(q7):
            if currmap != 450006130:
                rush(450006130)
                time.sleep(1)
            else:
                startQuest(q7,npc7)
        elif hasQuest(q7):
            if doneQuest(q7,npc7):
                if currmap != 450006130:
                    rush(450006130)
                    time.sleep(1)
                else:
                    completeQuest(q7,npc7)
                    time.sleep(1)
            elif currmap != 450006140:
                rush(450006140)
                time.sleep(1)
            elif currmap == 450006140:
                if job == 4212 and pos.x != -963:
                    Character.Teleport(-963,24)
                    time.sleep(1)
                else:
                    kami(True)
                    print("Wait for quest to be done")
                    time.sleep(1)
    elif doQuest(q8):
        if needQuest(q8):
            if currmap != 450006130:
                rush(450006130)
                time.sleep(1)
            else:
                startQuest(q8,npc8)
        elif hasQuest(q8):
            if doneQuest(q8,npc8):
                if currmap != 450006130:
                    rush(450006130)
                    time.sleep(1)
                else:
                    completeQuest(q7,npc7)
                    time.sleep(1)
            elif currmap != 450006150:
                rush(450006150)
                time.sleep(1)
            elif currmap == 450006150:
                if job == 4212 and pos.x != -188:
                    Character.Teleport(-188,-298)
                    time.sleep(1)
                else:
                    print("Wait for quest to be done")
                    time.sleep(1)
    