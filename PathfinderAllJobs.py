#HowToPathfind.
#ImportAll
import os, sys, Quest, Inventory, Packet, Login, random, Character, GameState, Field, Terminal, time, Key, Npc, Party, Context

def startQuest(quest, npc):
        print("Starting quest {0} from npc {1}".format(quest, npc))
        Quest.StartQuest(quest, npc)
        time.sleep(1)

def Job1():

    def to_portal(pname, enter=True):
        map = Field.GetID()
        portal = Field.FindPortal(pname)
        if portal.valid:
            if not ((portal.x-10 < Character.GetPos().x < portal.x+10)\
                    and (portal.y-10 < Character.GetPos().y < portal.y+15)):
                Character.Teleport(portal.x, portal.y-20)
                time.sleep(1)

            attempt = 0
            while enter and Field.GetID() == map and attempt < 3:
                attempt += 1
                Character.EnterPortal()
                time.sleep(1)

    def startQuest(quest, npc):
        print("Starting quest {0} from npc {1}".format(quest, npc))
        Quest.StartQuest(quest, npc)
        time.sleep(1)

    def completeQuest(quest, npc):
        print("Completing quest {0} from npc {1}".format(quest, npc))
        Quest.StartQuest(quest, npc)
        time.sleep(1)

    def questDone(quest, npc):
        return Quest.CheckCompleteDemand(quest, npc) == 0

    def needQuest(id):  # quest hasn't been accepted
        return Quest.GetQuestState(id) == 0

    def hasQuest(id):  # quest is active
        return Quest.GetQuestState(id) == 1

    def doQuest(id):  # quest isn't complete/turned in
        return Quest.GetQuestState(id) != 2

    def doneQuest(id):  # quest isn't complete/turned in
        return Quest.GetQuestState(id) == 2

    map = Field.GetID()
    
    if Character.GetJob() != 301 and Character.GetLevel() <= 29:
        if map == 910090301:
            Terminal.SetCheckBox("RushByLevel", False)
            Terminal.SetCheckBox("Auto Pet", True)
            Inventory.UseItem(2434265)
            to_portal("east00")
        elif doQuest(35900):
            if needQuest(35900):
                time.sleep(1)
                startQuest(35900, 0)
                time.sleep(1)
            elif hasQuest(35900):
                time.sleep(1)
                completeQuest(35900, 1013305)
                time.sleep(1)
        elif doneQuest(35900) and doQuest(35901):
            if needQuest(35901):
                time.sleep(1)
                startQuest(35901, 1013305)
                time.sleep(1)
            elif hasQuest(35901):
                time.sleep(5)
                completeQuest(35901, 1013305)
                time.sleep(5)
        elif doneQuest(35901) and doQuest(35902):
            if needQuest(35902):
                time.sleep(1)
                startQuest(35902, 1013305)
                time.sleep(1)
            if hasQuest(35902):
                if not questDone(35902, 1013305):
                    if map == 910090302:
                        to_portal("east00")
                    if map == 910090303:
                        Terminal.SetCheckBox("Legit Vac", False)
                        Terminal.SetCheckBox("Mob Falldown", True)
                        Terminal.SetCheckBox("Auto Aggro", False)
                        Terminal.SetCheckBox("Melee No Delay", False)
                        Terminal.SetCheckBox("Skill Inection", False)
                        Terminal.SetCheckBox("General FMA", False)
                        Terminal.SetCheckBox("Auto Attack", True)
                        Terminal.SetPushButton("Item Filter", False)
                if questDone(35902, 1013305):
                    Terminal.SetCheckBox("Auto Aggro", False)
                    Terminal.SetCheckBox("Melee No Delay", False)
                    Terminal.SetCheckBox("Auto Attack", False)
                    if map == 910090303:
                        to_portal("west00")
                    if map == 910090302:
                        Npc.ClearSelection()
                        Npc.RegisterSelection("Fire")
                        completeQuest(35902, 1013305)
        elif doneQuest(35902) and not doneQuest(35903):
            if needQuest(35903):
                time.sleep(1)
                startQuest(35903, 9010000)
    else: 
        if map == 910090305 and Character.GetLevel() <= 15:
            Terminal.SetCheckBox("RushByLevel", True)
            to_portal("out00")

def Job2():

    if Character.GetJob() == 301 and Character.GetLevel() >= 30:
        startQuest(35939, 0)
        startQuest(35934, 9010000)

def Job3():

    if Character.GetJob() == 330 and Character.GetLevel() >= 60:
        startQuest(35931, 0)
        startQuest(35935, 9010000)

def Job4():

    if Character.GetJob() == 331 and Character.GetLevel() >= 100:
        startQuest(35932, 0)
        startQuest(35936, 9010000)

if GameState.IsInGame():
    Job1()
    Job2()
    Job3()
    Job4()




            


