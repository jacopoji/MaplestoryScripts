import Character
import Context
import DataType
import Field
import Inventory
import Key
import Npc
import Quest
import Terminal
import time
import GameState


Terminal.SetRushByLevel(False)
flowermap1 = [450005100, 450005110, 450005120, 450005121, 450005130, 450005131]

def rush(id):
    if fieldid != id:
        Terminal.Rush(id)
    else:
        time.sleep(1)
    
def spacemash():
    for _ in range(0, 40):
        Key.Press(0x20)
        Key.Press(0x88)
    
def altgame():
    for _ in range(0, 10):
        Key.Press(0x12)
        time.sleep(1)
        Key.Press(0x88)
        time.sleep(1)
    
def enterbramble():
    if fieldid != 940200216:
        rush(450005220)
        time.sleep(1)
        Character.Teleport(-850, 75)
        time.sleep(1)
        Key.Press(0x26)
    
def leavebramble():
    if fieldid == 940200216:
        Character.Teleport(-455, 75)
        time.sleep(1)
        Key.Press(0x26)

def collectrocks(mapid, rockid):
    rush(mapid)
    time.sleep(2)
    rock = Field.FindNpc(rockid)
    time.sleep(2)
    xcoo = rock.x
    ycoo = rock.y
    Character.Teleport(xcoo, ycoo)
    time.sleep(2)    
    Character.TalkToNpc(rockid)
    time.sleep(7)
    spacemash()
    time.sleep(2)

def talkquest(qstate, qid, start, end, npc, endpc):
    if qstate == 0:
        if start == 940200216:
            enterbramble()
        else:
            rush(start)
        time.sleep(3)
        Quest.StartQuest(qid, npc)
        time.sleep(1)
        qcheck(qid, endpc, end)
    
def farmquest(qstate, qid, start, end, npc, endpc, fmap):
    if qstate == 0:
        if start == 940200216:
            enterbramble()
        else:
            rush(start)
        time.sleep(1)
        Quest.StartQuest(qid, npc)
        time.sleep(1)
    if qcheck(qid, endpc, end) == -1:
        if start == 940200216:
            leavebramble()
        time.sleep(1)
        rush(fmap)
        time.sleep(3)
    
def qcheck(qid, npc, map):
    if Quest.CheckCompleteDemand(qid, npc) == 0:
        if map == 940200216:
            enterbramble()
        else:
            rush(map)
        Quest.CompleteQuest(qid, npc)
        return 0
    else:
        return -1

jobid = Character.GetJob()
level = Character.GetLevel()

if GameState.IsInGame() and (jobid != -1 or level != -1):
    time.sleep(1)
    if Terminal.IsRushing():
        time.sleep(1)
    print("hi")
    fieldid = Field.GetID()
    quest1 = Quest.GetQuestState(34450)
    quest2 = Quest.GetQuestState(34451)
    quest3 = Quest.GetQuestState(34452)
    quest4 = Quest.GetQuestState(34453)
    quest5 = Quest.GetQuestState(34454)
    quest6 = Quest.GetQuestState(34455)
    quest7 = Quest.GetQuestState(34456)
    quest8 = Quest.GetQuestState(34459)
    quest9 = Quest.GetQuestState(34460)
    quest10 = Quest.GetQuestState(34461)
    quest11 = Quest.GetQuestState(34462)
    quest12 = Quest.GetQuestState(34463)
    quest13 = Quest.GetQuestState(34464)
    quest14 = Quest.GetQuestState(34465)
    quest15 = Quest.GetQuestState(34466)
    quest16 = Quest.GetQuestState(34467)
    quest17 = Quest.GetQuestState(34468)
    quest18 = Quest.GetQuestState(34469)
    quest19 = Quest.GetQuestState(34470)
    quest20 = Quest.GetQuestState(34471)
    quest21 = Quest.GetQuestState(34472)
    quest22 = Quest.GetQuestState(34473)
    quest23 = Quest.GetQuestState(34474)
    quest24 = Quest.GetQuestState(34475)
    quest25 = Quest.GetQuestState(34476)
    quest26 = Quest.GetQuestState(34477)
    quest27 = Quest.GetQuestState(34478)
    quest28 = Quest.GetQuestState(34479)
 
    arcsymbol = Inventory.FindItemByID(1712004)
    if arcsymbol.valid:
        Inventory.SendChangeSlotPositionRequest(1, arcsymbol.pos, -1603, -1)

    if quest1 != 2:
        talkquest(quest1, 34450, 450003010, 450003010, 0, 3003300)

    elif quest2 != 2:
        talkquest(quest2, 34451, 450005015, 450005015, 3003301, 3003301)
        time.sleep(1)
        Key.Press(0x26)

    elif quest3 != 2:
        talkquest(quest3, 34452, 450005015, 450005015, 3003301, 3003301)
        
    elif quest4 != 2:
        talkquest(quest4, 34453, 450005015, 450005015, 3003301, 3003301)

    elif quest5 != 2:
        talkquest(quest5, 34454, 450005015, 450005100, 3003302, 3003304)

    elif quest6 != 2:
        if quest6 == 0:
            rush(450005100)
            Quest.StartQuest(34455, 3003303)
        if quest6 == 1:
            if Quest.CheckCompleteDemand(34455, 3003303) == 0:
                rush(450005100)
                Quest.CompleteQuest(34455, 3003303)
            else:
                while Inventory.GetItemCount(4036096) != 10:
                    rush(450005110)
                    time.sleep(1)
                while Inventory.GetItemCount(4036097) != 10:
                    rush(450005120)
                    time.sleep(1)
                while Inventory.GetItemCount(4036098) != 10:
                    rush(450005130)
                    time.sleep(1)
 
    elif quest7 != 2:
        if quest7 == 0:
            rush(450005100)
            Quest.StartQuest(34456, 3003303)
        if quest7 == 1:
            if qcheck(34456, 3003303, 450005100) == -1:
                while Inventory.GetItemCount(4036101) != 100:
                    rush(450005110)
                    time.sleep(5)
                while Inventory.GetItemCount(4036102) != 100:
                    rush(450005120)
                    time.sleep(5)
                while Inventory.GetItemCount(4036103) != 100:
                    rush(450005130)
                    time.sleep(5)
 
    elif quest8 != 2:
        if quest8 == 0:
            rush(450005100)
            Quest.StartQuest(34459, 3003304)
        if quest8 == 1:
            if qcheck(34459, 3003303, 450005100) == -1:
                for map in flowermap1:
                    rush(map)
                    time.sleep(2)
                    flower = Field.FindNpc(3003337)
                    xcoo = flower.x
                    ycoo = flower.y
                    Character.Teleport(xcoo, ycoo)
                    Character.TalkToNpc(3003337)
                    time.sleep(5)
                    if Quest.CheckCompleteDemand(34459, 3003303) == 0:
                        break
                    
    elif quest9 !=2:
        print("nine")
        if quest9 == 0:
            rush(450005100)
            Quest.StartQuest(34460, 3003303)
            time.sleep(5)
            Character.Teleport(-437, 139)
            time.sleep(5)
            spacemash()
            time.sleep(5)
            Character.Teleport(890, -200)
            time.sleep(2)
            spacemash()

    elif quest10 !=2:
        talkquest(quest10, 34461, 450005000, 450005200, 3003306, 3003307)
        time.sleep(1)
        Key.Press(0x20)
        time.sleep(1)
        talkquest(quest10, 34461, 450005000, 450005200, 3003306, 3003307)
        
    elif quest11 != 2:
        talkquest(quest11, 34462, 450005200, 450005200, 3003307, 3003308)
    
    elif quest12 != 2:
        talkquest(quest12, 34463, 450005200, 450005220, 3003307, 3003311)
    
    elif quest13 != 2:
        if quest13 == 0:
            rush(450005220)
            time.sleep(2)
            Quest.StartQuest(34464, 3003311)
            time.sleep(5)
            Character.Teleport(500, 50)
            time.sleep(10)
            Character.Teleport(-1340,70)
            if not Field.FindMob(86440141).valid:
                Key.Press(0x26)
                Key.Press(0x88)
            time.sleep(10)
            Character.Teleport(375, 50)
            time.sleep(10)
            Character.Teleport(-1380,-285)
            time.sleep(10)
            Key.Press(0x26)
            Key.Press(0x88)
            time.sleep(10)
            Character.Teleport(-350, 70)
            time.sleep(10)
            Character.Teleport(-1370, -50)
            time.sleep(10)
            Key.Press(0x26)
            Key.Press(0x88)
            
    elif quest14 != 2:
        talkquest(quest14, 34465, 450005200, 450005200, 3003309, 3003338)
    
    elif quest15 != 2:
        talkquest(quest15, 34466, 450005200, 450005220, 3003338, 3003329)
    
    elif quest16 != 2:
        farmquest(quest16, 34467, 940200216, 940200216, 3003325, 3003325, 450005230)
    
    elif quest17 !=2:
        farmquest(quest17, 34468, 940200216, 940200216, 3003325, 3003325, 450005240)
    
    elif quest18 != 2:
        talkquest(quest18, 34469, 940200216, 940200216, 3003327, 3003328)
    
    elif quest19 != 2:
        talkquest(quest19, 34470, 940200216, 940200216, 0, 3003328)
    
    elif quest20 != 2:
        talkquest(quest20, 34471, 940200216, 450005300, 3003325, 3003312)
    
    elif quest21 != 2:
        if quest21 == 0:
            rush(450005300)
            time.sleep(2)
            Character.Teleport(540, 510)
            Quest.StartQuest(34472, 3003336)
            time.sleep(5)
        if quest21 == 1:
            Quest.CompleteQuest(34472, 3003313)
        
    elif quest22 != 2:
        if quest22 == 0:
            rush(450005400)
            time.sleep(2)
            Quest.StartQuest(34473, 3003314)
            time.sleep(5)
        if qcheck(34473, 3003314, 450005400) == -1:
            time.sleep(10)
            spacemash()
    
    elif quest23 != 2:
        if quest23 == 0:
            rush(450005400)
            time.sleep(2)
            Quest.StartQuest(34474, 3003314)
            time.sleep(10)
            collectrocks(450005410, 3003316)
            time.sleep(2)
            collectrocks(450005411, 3003317)
            time.sleep(2)
            collectrocks(450005412, 3003318)
            time.sleep(2)
            collectrocks(450005431, 3003333)
            time.sleep(2)
            collectrocks(450005432, 3003334)
            time.sleep(2)
            collectrocks(450005432, 3003335)
            #collectrocks(450005430, 3003319)
        if qcheck(34474, 3003314, 450005400) == -1:
            rush(450005410)
            time.sleep(60)
            rush(450005420)
            while qcheck(34474, 3003314, 450005400) == -1:
                time.sleep(1)
 
    elif quest24 != 2:
        if quest24 == 0:
            rush(450005400)
            time.sleep(2)
            Quest.StartQuest(34475, 3003314)
        if qcheck(34475, 3003313, 450005400):
            altgame()
            spacemash()
        
    elif quest25 != 2:
        if quest25 == 0:
            rush(450005400)
            time.sleep(2)
            Quest.StartQuest(34476, 3003314)
            time.sleep(5)
            Character.Teleport(-845, -327)
            time.sleep(10)
            Character.Teleport(-2290, 140)
            if not Field.FindMob(8644016).valid:
                Key.Press(0x26)
                Key.Press(0x88)
            time.sleep(10)
            Character.Teleport(-800, -295)
            time.sleep(10)
            Character.Teleport(-2060,-145)
            if not Field.FindMob(8644017).valid:
                Key.Press(0x26)
                Key.Press(0x88)
            time.sleep(10)
            Character.Teleport(-900, -395)
            time.sleep(10)
            Character.Teleport(-2070, -117)
            if not Field.FindMob(8644018).valid:
                Key.Press(0x26)
                Key.Press(0x88)
            
    elif quest26 != 2:
        if quest26 == 0:
            rush(450005000)
            time.sleep(2)
            Quest.StartQuest(34477, 3003306)
            time.sleep(10)
        if quest26 == 1:
            time.sleep(1)
        
    elif quest27 != 2:
        talkquest(quest27, 34478, 450005000, 450005000, 3003324, 3003320)
        time.sleep(3)
        spacemash()
    
    else:
        time.sleep(1)