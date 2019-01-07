import Character
import Context
import DataType
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time

Terminal.SetRushByLevel(False)

while True:
    time.sleep(1)
    field_id = Field.GetID()
    jobid = Character.GetJob()
    level = Character.GetLevel()
    if jobid == -1 or level == -1:
        #not in game
        continue
    if jobid != 1211 or level < 100:
        break
    if Terminal.IsRushing():
        time.sleep(1)
        continue
    quest1 = Quest.GetQuestState(20890)
    quest2 = Quest.GetQuestState(20891)
    quest3 = Quest.GetQuestState(20892)
    quest4 = Quest.GetQuestState(20893)
    quest5 = Quest.GetQuestState(20894)
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(20890, 1101002)
        elif quest1 == 1:
            if field_id == 913031003:
                Quest.CompleteQuest(20890, 1104300)
    elif quest2 != 2:
        if quest2 == 0:
            time.sleep(1)
            Quest.StartQuest(20891, 1104300)
        elif quest2 == 1:
            if field_id == 913031003:
                Quest.CompleteQuest(20891, 1102112)
    elif quest3 != 2:
        if field_id == 130000000:
            if quest3 == 0:
                Quest.StartQuest(20892, 1101002)
            elif quest3 == 1:
                Quest.CompleteQuest(20892, 1101000)
        else:
            Terminal.Rush(130000000)
    elif quest4 != 2: #913031002
        if quest4 == 0:
            time.sleep(1)
            Quest.StartQuest(20893, 1101000)
        elif quest4 == 1:
            if field_id == 913031002:
                time.sleep(1) #let bot kill cygnus boss
            elif field_id == 130000000:
                Quest.CompleteQuest(20893, 1101000)
            else:
                time.sleep(1)
    elif quest5 != 2:
        if quest5 == 0:
            if field_id == 130000000:
                Quest.StartQuest(20894, 1101000)
        elif quest5 == 1:
            Quest.CompleteQuest(20894,1101000)
            time.sleep(1)

        
                
            
    
