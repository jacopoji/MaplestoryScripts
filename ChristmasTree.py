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
        time.sleep(1)
        continue
    time.sleep(1)
    quest = Quest.GetQuestState(15982)
    if quest != 1:
	time.sleep(1)
        Quest.StartQuest(15982, 9001147)
	time.sleep(2)
    elif quest == 1:
        if Quest.CheckCompleteDemand(15982, 9001147) == 0:
            Quest.CompleteQuest(15982, 9001147)
	    time.sleep(2)
    else:
	time.sleep(1)
        break
