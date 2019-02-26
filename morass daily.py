#Morass
#Author: Comicals
#12/26/18

import Field
import Character
import Quest
import Npc
import Terminal
import GameState
import time

town       = 450006130
research   = 450006240

questmaps    = {}
returnmaps   = {}

q1  = 34276
q2  = 34277
q3  = 34278
q4  = 34279
q5  = 34280
q6  = 34281
q7  = 34282
q8  = 34283
q9  = 34284
q10 = 34285
q11 = 34286
q12 = 34287
q13 = 34288
q14 = 34289
q15 = 34290
q16 = 34291
q17 = 34292
q18 = 34293
q19 = 34294
q20 = 34295
q21 = 34296
for q in range(q1,q21):
    questmaps[q] = 0

 
#questmaps = {q1:450006120, q2:450006150, q3:450006210, q4:450006020, q5: , q6:, q7:, q8: ,}


def CheckBox(set, value):
    if Terminal.GetCheckBox(set) != value:
        Terminal.SetCheckBox(set, value)
    
def ToPortal(portal, enter=True, safe=False):
    map=Field.GetID()
    if safe:
        for char in Field.GetCharacters():
            if not Terminal.IsLocalUser(char.id):
                return False
            
    portal = Field.FindPortal(portal)
    if portal.valid:
        AAFlag      = False
        kamiFlag    = False
        if Terminal.GetCheckBox("Auto Attack"):
            AAFlag = True
            CheckBox("Auto Attack", False)
        if Terminal.GetCheckBox("Kami Vac"):
            kamiFlag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
        
        if not (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5) \
        or not (Character.GetPos().y < portal.y+10 and Character.GetPos().y > portal.y-10):
            Character.Teleport(portal.x, portal.y-20)
            time.sleep(1)
        
        attempt = 0
        while enter and Field.GetID() == map and attempt<3:
            if (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5):
                attempt+=1
                Character.EnterPortal()
                time.sleep(2)
        
        if AAFlag:
            CheckBox("Auto Attack", True)
        if kamiFlag:
            CheckBox("Kami Vac", True)
        
        
def Rush(mapid):
    if not Field.GetID() == mapid:
        Terminal.Rush(mapid)
        time.sleep(2)
    while Terminal.IsRushing():
        time.sleep(1)
        continue
        
def DoQuest(id):
    if Quest.GetQuestState(id) != 2:
        return True
    else:
        return False

def NeedQuest(id):
    if Quest.GetQuestState(id) == 0:
        return True
    else:
        return False

def HasQuest(id):
    if Quest.GetQuestState(id) == 1:
        return True
    else:
        return False

def DoneQuest(id):
    if Quest.GetQuestState(id) == 2:
        return True
    else:
        return False
    
def InProgress(id, npc):
    if Quest.CheckCompleteDemand(id, npc) != 0:
        return True
    else:
        return False

def AutoQuest(qid, questmap, endmap, npc, townpos="mid"):
    if HasQuest(qid):
        if InProgress(qid, npc):
            questmaps[qid]  = questmap
            returnmaps[qid] = endmap
        else:
            questmaps[qid]  = 0
            returnmaps[qid] = endmap
            if Field.GetID()==endmap:
                if Field.GetID() == 450006130:
                    if townpos == "mid":
                        ToMid()
                    else:
                        ToPortal("east00", False)
                Quest.CompleteQuest(qid, npc)
                time.sleep(1)
    else:
        returnmaps[qid] = 0

def AutoQuestQ10():
    if HasQuest(q10):
        if InProgress(q10, 3003432):
            if Field.GetID() != 940204309:
                for map in [450006410, 450006420, 450006430]:
                    if Field.GetID()!=map:
                        Rush(map)
                        time.sleep(1)
                    if Field.GetID()==map:
                        ToPortal("dq00")
                        time.sleep(2)
                        ToPortal("dq01")
                        time.sleep(2)
                
                    if Field.GetID() == 940204309:
                        break
            else:
                time.sleep(1)
            
            return True
        else:
            if Field.GetID()==940204309:
                Npc.ClearSelection()
                Npc.RegisterSelection("To Trueffet Square")
                ToPortal("pt_out")
                time.sleep(2)
            else:
                returnmaps[q10] = town
                if Field.GetID()==town:
                    ToMid()
                    Quest.CompleteQuest(34285, 3003432)
            
            return False

def AutoQuestQ19():
    if HasQuest(q19):
        if InProgress(q19, 3003432):
            if Field.GetID() not in [940204430, 940204450, 940204470]:
                for map in [450006410, 450006420, 450006430]:
                    if Field.GetID()!=map:
                        Rush(map)
                    if Field.GetID()==map:
                        ToPortal("dq00")
                        time.sleep(2)
                        ToPortal("dq01")
                        time.sleep(2)
                
                    if Field.GetID() == 940204430:
                        break
            elif len(Field.GetMobs())==0:
                ToPortal("pt00")
                ToPortal("pt01")
            
            return True
        else:
            returnmaps[q19] = town
            if Field.GetID() == town:
                ToMid()
                Quest.CompleteQuest(q19, 3003432)
            
            return False


def AutoQuestQ20():
    if HasQuest(q20):
        if InProgress(q20, 3003469):
            if Field.GetID() not in [940204490, 940204510, 940204530]:
                for map in [450006300, 450006310, 450006320]:
                    if Field.GetID()!=map:
                        Rush(map)
                    if Field.GetID()==map:
                        ToPortal("dq00")
                        time.sleep(2)
                
                    if Field.GetID() == 940204490:
                        break
            elif len(Field.GetMobs())==0:
                ToPortal("pt00")
            
            return True
        else:
            returnmaps[q20] = research
            if Field.GetID() == research:
                Quest.CompleteQuest(q20, 3003469)
            
            return False

def AutoQuestQ21():
    if HasQuest(q21):
        if InProgress(q21, 3003469):
            if DoQuest(34246) and Field.GetID() not in [450006240, 940204550, 940204570]:
                Rush(450006240)
                Quest.StartQuest(34246, 3003469)
            elif Field.GetID() == 940204550:
                time.sleep(1)
            elif Field.GetID() == 940204570:
                Character.TalkToNpc(3003474)
            
            return True
        else:
            returnmaps[q21] = research
            if Field.GetID() == research:
                Quest.CompleteQuest(34296, 3003469)
            
            return False

        
def ToMid():
    sp = Field.FindPortal("sp").x
    down00 = Field.FindPortal("down00").x
    pos = Character.GetPos().x
 
    if not ((pos < sp+5 and pos > sp-5) or (pos < down00+5 and pos > down00-5)):
        ToPortal("down00", False)


def SortQuest():
    # Nameless Cat 200
    AutoQuest(q1, 450006120, 450006130, 3003410, "east")

    # strong gansters 200
    AutoQuest(q2, 450006150, 450006130, 3003427, "east")

    # Blue Shadow 200
    AutoQuest(q3, 450006210, 450006130, 3003465)

    #  Xenoroid Echo Type B 200
    AutoQuest(q4, 450006020, 450006130, 3003465)

    # red shadows 200
    AutoQuest(q5, 450006230, 450006240, 3003469)

    # Big experimental gone wrong
    AutoQuest(q6, 450006320, 450006240, 3003469)

    # Thralled Guard 200
    AutoQuest(q7, 450006410, 450006240, 3003469)

    # Thralled Wizard 200
    AutoQuest(q8, 450006420, 450006240, 3003469)

    # Memory Silvers 100 / Any mob in morass
    AutoQuest(q9, 450006210, 450006130, 3003432)

    # Glittering powder 50, Nameless Cat
    AutoQuest(q11, 450006110, 450006130, 3003410, "east")

    # anti magic shell 30 / Any mob in morass
    AutoQuest(q12, 450006110, 450006130, 3003467)

    # Stolon fruit 50 / powerful gangster
    AutoQuest(q13, 450006140, 450006130, 3003426, "east")

    # shadow core 50 / shadows
    AutoQuest(q14, 450006220, 450006130, 3003466)

    #
    AutoQuest(q15, 450006020, 450006130, 3003468, "east")

    # Experiment Remnants 50 / Experiment Gone wrong
    AutoQuest(q16, 450006300, 450006240, 3003469)

    # Borken Shaft 50 / Warhammer knight
    AutoQuest(q17, 450006420, 450006240, 3003469)

    # Broken Bow 50 / Thralled archer
    AutoQuest(q18, 450006430, 450006240, 3003469)
 

if GameState.IsInGame():
    if DoQuest(34275):
        if NeedQuest(34275):
            Rush(town)
            ToMid()
            Npc.ClearSelection()
            Npc.RegisterSelection("Those")
            time.sleep(1)
            Quest.StartQuest(34275, 3003432)
            time.sleep(2)

        elif HasQuest(34275):
            if InProgress(34275, 3003432):
                inQuest = False
                SortQuest()
                # optimize pathing
                for mapid in sorted(questmaps.values()):
                    if mapid != 0 :
                        print(mapid)
                        inQuest = True
                        Rush(mapid)
                        break

                if not inQuest:
                    inQuest = AutoQuestQ10()
                if not inQuest:
                    inQuest = AutoQuestQ19()
                if not inQuest:
                    inQuest = AutoQuestQ20()
                if not inQuest:
                    inQuest = AutoQuestQ21()

                if not inQuest:
                    for map in sorted(returnmaps.values(), reverse=True):
                        if map == research:
                            Rush(research)
                            break
                        elif map == town:
                            Rush(town)
                            break

                    #Turn in quests
                    SortQuest()
                    AutoQuestQ10()
                    AutoQuestQ19()
                    AutoQuestQ20()
                    AutoQuestQ21()


            else:
                Rush(450006130)
                ToMid()
                Quest.CompleteQuest(34275, 3003432)