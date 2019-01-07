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
    job = Character.GetJob()
    if job==4211 or  job == 4212:
        if Character.GetSP() == 0:
            Key.Set(0x47,1,42111003)
            time.sleep(1)
            break
        else:
            time.sleep(1)
            continue
