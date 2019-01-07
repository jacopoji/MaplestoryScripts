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

while True:
    time.sleep(1)
    quest = Quest.GetQuestState(55611)
    if quest != 1:
        Quest.StartQuest(55611, 9201256)
    elif quest == 1:
        if Quest.CheckCompleteDemand(55611, 9201256) == 0:
            Quest.CompleteQuest(55611, 9201256)
    else:
        break