import Character
import Packet
import Terminal
import Field
import time
import GameState
import Inventory
import Npc
import Key
import Quest



def mano():
    mob = Field.FindMob(9300815)
    if mob.valid:
        Terminal.SetCheckBox("Kami Vac", True)
        Terminal.SetCheckBox("Auto Attack", True)
        Character.BasicAttack()
    if not mob.valid:
        Terminal.SetCheckBox("Kami Vac", False)
        Terminal.SetCheckBox("Auto Attack", False)
        Character.Teleport(68, 150)
        Character.EnterPortal()

if Field.GetID() == 4000011:
    Character.Teleport(1106 ,545)
    time.sleep(3)
    Character.EnterPortal()
if Field.GetID() == 4000012:
    Npc.ClearSelection()
    Npc.RegisterSelection("I don't need you, Mai! (Skip tutorial and teleport straight to town.)")
    Character.TalkToNpc(10301)
    time.sleep(5)
    
if Character.GetLevel() == 2:
    if Field.GetID() == 4000020:
        Character.Teleport(1614 ,154)
        time.sleep(5)
        Character.TalkToNpc(10304)
        time.sleep(3)
        Character.TalkToNpc(10304)
if Character.GetLevel() == 3:
    if Field.GetID() == 4000020:
        Character.Teleport(2197, 274)
        Character.EnterPortal()
if Field.GetID() == 4000021:
    Character.Teleport(683, 215)
    time.sleep(3)
    Character.EnterPortal()
if Field.GetID() == 4000026:
    Character.Teleport(765, 215)
    time.sleep(3)
    Character.EnterPortal()
if Character.GetLevel() ==3:
    if Field.GetID() == 4000030:
       Character.Teleport(2506, 287)
       time.sleep(3)
       Character.EnterPortal()      
if Field.GetID() == 4000031:
    if Character.GetLevel() ==3:
        Character.Teleport(1962, 407)
        time.sleep(5)
        Quest.CompleteQuest(32211, 10305)
if Character.GetLevel() ==4:
    Quest.StartQuest(32212, 10305)
    time.sleep(5)
    Quest.CompleteQuest(32212, 10306)
if Character.GetLevel() ==5:
    Quest.StartQuest(32213, 10306)
    if Quest.GetQuestState(32213) == 1:
        if Field.GetID() == 4000031:
            Character.Teleport(34 ,527)
            time.sleep(3)
            Character.EnterPortal()
    if Field.GetID() == 4000030:
        if not Inventory.FindItemByID(4033914).valid:
            Character.Teleport(1895 ,407)
            time.sleep(5)
            Character.BasicAttack()
            item = Field.FindItem(4033914)
            if item.valid:
                Character.Teleport(item.x, item.y)
                Terminal.SetCheckBox("Auto Loot", True)
        if Inventory.FindItemByID(4033914).valid:
            if Field.GetID() == 4000030:
                Terminal.SetCheckBox("Auto Loot", False)
                Character.Teleport(2506, 287)
                time.sleep(3)
                Character.EnterPortal()      
    
if Character.GetLevel() == 6:
    if Field.GetID() == 4000030:
        Character.EnterPortal()
    if Field.GetID() == 4000031:
        Character.Teleport(1835, 407)
        time.sleep(5)
        Quest.StartQuest(32214, 10305)
        if Quest.GetQuestState(32214) ==1:
            Character.EnterPortal()
    mano()
if Character.GetLevel() == 7:
    Character.TalkToNpc(10307)
    time.sleep(5)
    Quest.StartQuest(32216, 10306)
    time.sleep(5)
if Character.GetLevel() == 10:
    if Field.GetID() == 120000101:
        Quest.StartQuest(1405, 1090000)
    if Field.GetID() == 100000101:
        Quest.StartQuest(1403, 1012100)
    if Field.GetID() == 102000003:
        Quest.StartQuest(1401, 1022000)
    if Field.GetID() == 103000003:
        Quest.StartQuest(1404, 1052001)
    if Field.GetID() == 101000003:
        Quest.StartQuest(1402, 1032001)
