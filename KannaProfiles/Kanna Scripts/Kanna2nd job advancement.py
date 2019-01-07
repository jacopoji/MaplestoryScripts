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
import sys

while True:
    time.sleep(1)
    jobid = Character.GetJob()
    level = Character.GetLevel()
    if jobid == -1 or level == -1:
        #not in game
        continue
    if jobid == 4210:
        break
    elif jobid != 4200 or level < 30:
        break
    quest = Quest.GetQuestState(57458)
    if quest == 0:
        Quest.StartQuest(57458, 000000)
    
    
