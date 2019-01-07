import os, sys, Character, GameState, Quest, time, Npc, Terminal, Inventory
# Author: Comicals
# Auto ToT 1.0
# 8/18/2018


# Set it True or False if you like to have equip boxes open automatically
OpenBox = True

# Set True or False for ToT quest of the level to be done
Lv20 = True
Lv30 = True
Lv40 = True
Lv50 = True
Lv60 = True
#############################################

if GameState.IsInGame():
    print("Running")
    if Lv20 and Quest.GetQuestState(61586) !=2 and Character.GetLevel()>= 20:
        Terminal.SetCheckBox("bot/puffram", False)
        Npc.ClearSelection()
        Npc.RegisterSelection("Cash Shop")
        Npc.RegisterSelection("Beauty Salon")
        Npc.RegisterSelection("Receive")
        Quest.StartQuest(61586, 9201253)
        time.sleep(10)
    elif OpenBox and Quest.GetQuestState(61586) == 2:
        if Inventory.FindItemByID(2430445).valid:
            Inventory.UseItem(2430445)      
      
    if Lv30 and Quest.GetQuestState(61587) !=2 and Character.GetLevel()>= 30:
        Terminal.SetCheckBox("bot/puffram", True)
        time.sleep(10)
    elif OpenBox and Quest.GetQuestState(61587) ==2 :
        if Inventory.FindItemByID(2430447).valid:
            Inventory.UseItem(2430447)
          
    if Lv40 and Quest.GetQuestState(61588) !=2 and Character.GetLevel()>= 40:
        Terminal.SetCheckBox("bot/puffram", False)
        Npc.ClearSelection()
        Npc.RegisterSelection("Safety Charm")
        Npc.RegisterSelection("Respawn Token")
        Npc.RegisterSelection("You get")
        Quest.StartQuest(61588, 9201253)
        time.sleep(10)
    elif OpenBox and Quest.GetQuestState(61588) == 2:
        if Inventory.FindItemByID(2430449).valid:
            Inventory.UseItem(2430449)  
      
    if Lv50 and Quest.GetQuestState(61589) !=2 and Character.GetLevel() >= 50:
        Terminal.SetCheckBox("bot/puffram", False)
        Npc.ClearSelection()
        Npc.RegisterSelection("Familiar")
        Npc.RegisterSelection("Teleport Rock")
        Npc.RegisterSelection("You get")
        Quest.StartQuest(61589, 9201253)
        time.sleep(10)
    elif OpenBox and Quest.GetQuestState(61589) ==2:
        if Inventory.FindItemByID(2430450).valid:
            Inventory.UseItem(2430450)
      
    if Lv60 and Quest.GetQuestState(61590) !=2 and Character.GetLevel() >= 60:
        Terminal.SetCheckBox("bot/puffram", False)
        Npc.ClearSelection()
        Npc.RegisterSelection("Potential")
        Npc.RegisterSelection("Bonus Potential")
        Npc.RegisterSelection("Cube")
        Npc.RegisterSelection("Soul Weapon")
        Npc.RegisterSelection("gift")
        Quest.StartQuest(61590, 9201253)
        time.sleep(10)
    elif OpenBox and Quest.GetQuestState(61590) ==2:
        if Inventory.FindItemByID(2430451).valid:
            Inventory.UseItem(2430451)