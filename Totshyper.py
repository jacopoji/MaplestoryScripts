import Character
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

hyperquest = Quest.GetQuestState(61589)

if GameState.IsInGame:
    if hyperquest != 2:
        time.sleep(1)
        Quest.StartQuest(61589, 9201253)
        time.sleep(1)
        Npc.ClearSelection()
        print('1')
        time.sleep(1)
        Npc.RegisterSelection('Familiar')
        time.sleep(1)
        print('2')
        Npc.ClearSelection()
        time.sleep(1)
        Npc.RegisterSelection('Teleport Rock')
        time.sleep(1)
        Npc.ClearSelection()
        time.sleep(1)
        Npc.RegisterSelection("You get a gift for listening!")
        

