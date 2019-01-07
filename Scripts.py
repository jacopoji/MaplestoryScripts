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
    job = Character.GetJob()
    level = Character.GetLevel()
    if job == -1 or level == -1:
        continue
    field_id = Field.GetID()
    if Terminal.IsRushing():
        continue
        
    if field_id == 540000000:
        Terminal.Rush(541020610)
    elif field_id == 541020610:
        portal = Field.FindPortal("MD00")
        if portal.valid:
            Character.Teleport(portal.x, portal.y)
            time.sleep(3)
            Character.EnterPortal()
            time.sleep(0.1)
            Character.EnterPortal() #incase 1st doesn't register
