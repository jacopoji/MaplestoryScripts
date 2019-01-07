import Character
import Field
import GameState
import Inventory
import Npc
import Terminal
import time

Terminal.SetRushByLevel(False)

while True:
    time.sleep(1)

    if GameState.IsInGame() == False:
        continue

    if Terminal.IsRushing():
        continue

    currentMap = Field.GetID()
    item = Inventory.FindItemByID(4001017)

    if currentMap == 211042300:
        Character.Teleport(-732, -220)
        
        if item.valid:
            Npc.ClearSelection()
            Npc.RegisterSelection("Normal Zakum")
            Character.EnterPortal()
        else:
            Npc.ClearSelection()
            Npc.RegisterSelection("Receive an offering for Zakum.")
            Npc.RegisterSelection("Normal/Chaos Zakum")
            Character.TalkToNpc(2030008)
    elif currentMap == 211042400:
        if item.valid:
            Npc.ClearSelection()
            Npc.RegisterSelection("Request entry to the Zakum expedition. (Party members will all move at the same time.)")
            Character.TalkToNpc(2030013)
        else:
            Character.Teleport(-1606, -332)
            Character.EnterPortal()
    else:
        break
