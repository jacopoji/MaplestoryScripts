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
import Packet
import GameState

while True:
    job = Character.GetJob()
    level = Character.GetLevel()

    #----------------Safe check-----------------------
    if GameState.IsInGame()==False:
        time.sleep(1)
        continue

    if level == -1:
        time.sleep(1)
        continue

    if level <= 33:
        time.sleep(1)
        continue

    if job == -1:
        time.sleep(1)
        continue

    if Terminal.IsRushing():
        continue
    #----------------Assignments-----------------------
    one = 15982
    NPC = 9001147
    quest1 = Quest.GetQuestState(one)
    #---------------------------------------------------
    if quest1 != 2:
        if quest1 == 0:
            time.sleep(2)
            Quest.StartQuest(one,NPC)
            time.sleep(2)
            if quest1 == 0:
                Quest.CompleteQuest(one,NPC)
            else:
                continue
        elif quest1 == 1:
            Quest.CompleteQuest(one,NPC)
            time.sleep(1)
        else:
            continue
    else:
        break
    #end of code
