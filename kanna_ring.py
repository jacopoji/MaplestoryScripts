import Terminal, Quest, Character, Npc,GameState,time,Field,GameState,Inventory,Packet,sys,os
if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCLib, SCHotkey
except:
	print("Couldn't find SunCat module")

#######################
#######################
######### W I P #######
#######################
#######################

quest1 = Quest.GetQuestState(58901)
quest2 = Quest.GetQuestState(58902)
quest3 = Quest.GetQuestState(58903)
quest4 = Quest.GetQuestState(58907)
quest5 = Quest.GetQuestState(58908)
quest6 = Quest.GetQuestState(58909)
quest7 = Quest.GetQuestState(58910)
quest8 = Quest.GetQuestState(58911)
quest9 = Quest.GetQuestState(58913)
quest10 = Quest.GetQuestState(58941)
quest11 = Quest.GetQuestState(58942)
quest12 = Quest.GetQuestState(58943)
quest13 = Quest.GetQuestState(58944)
quest14 = Quest.GetQuestState(58945)
quest15 = Quest.GetQuestState(58946)
quest16 = Quest.GetQuestState(58947)
quest17 = Quest.GetQuestState(58963)
quest18 = Quest.GetQuestState(58964)
quest19 = Quest.GetQuestState(58965)
quest20 = Quest.GetQuestState(58950)
quest21 = Quest.GetQuestState(58966)
quest22 = Quest.GetQuestState(58967)
quest23 = Quest.GetQuestState(58968)

herb_header = 0x03E3
#Key to restart pers. variables
HotKey = 0x7A

def TP_EnterPortal(x,y):
    Character.Teleport(x,y)
    time.sleep(1)
    Character.EnterPortal()

SCLib.StartVars()
if SCLib.GetVar("HuntDone") is None:
    SCLib.PersistVar("HuntDone", False)

SCHotkey.StartHotkeys(100)
def KillPersistVarThred():
	SCLib.StopVars()
	time.sleep(1)

SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F11
#SunCat.StopTP()
print("Starting kanna ring script")
Terminal.SetCheckBox("Kami Loot",False)
Terminal.SetCheckBox("Auto Loot",False)

if GameState.IsInGame():
    if quest1 != 2:
        if quest1 == 0:
            print("Starting first quest")
            Quest.StartQuest(58901, 9130102)
        elif quest1 == 1:
            print("Doing first quest")
            if Quest.CheckCompleteDemand(58901,9130102) == 0:
                if Field.GetID() == 807000000:
                    TP_EnterPortal(-1688,32)
                elif Field.GetID() == 811000001:
                    Quest.CompleteQuest(58901, 9130102)
                else:
                    Terminal.Rush(807000000)
    if quest2 != 2:
        if quest2 == 0:
            print("Starting second quest")
            #if Field.GetID() == 811000001:
            Quest.StartQuest(58902, 9130102)
        elif quest2 == 1:
            print("Doing second quest")
            if Quest.CheckCompleteDemand(58902,9130102) == 0:
                SunCat.StopTP()
                Character.Teleport(633,-268)
                Quest.CompleteQuest(58902, 9130102)
            else:
                quest_done_flag = False
                if quest2 == 1:
                    drop = Field.FindItem(4034126)
                    if drop.valid:
                        SunCat.KamiTP(drop.x,drop.y)
                        Character.LootItem()
    if quest3 != 2:
        if quest3 == 0:
            SunCat.StopTP()
            print("Starting third quest")
            Quest.StartQuest(58903, 9130102)
        elif quest3 ==  1:
            print("Doing third quest")
            if Quest.CheckCompleteDemand(58903, 9130102) == 0:
                print("Testing")
                #if Field.GetID() == 811000004:
                #    Character.Teleport(801,-28)
                #    time.sleep(1)
                #    Character.EnterPortal()
                #elif Field.GetID() == 811000001:
                #    Quest.CompleteQuest(58903, 9130102)
            else:
                if Field.GetID() == 811000001:
                    SunCat.StopTP()
                    TP_EnterPortal(-843,-688)
                elif Field.GetID() == 811000004:
                    reactor = Field.FindReactor(8650012)
                    if reactor.valid and SCLib.GetVar("HuntDone"):
                        print("found reactor")
                        pos = Character.GetPos()
                        if pos.x not in range(reactor.x-5,reactor.x+5):
                            print("Teleporting to herb")
                            Character.Teleport(reactor.x,reactor.y-30)
                        elif pos.y not in range(reactor.y-5,reactor.y+5):
                            print("Teleporting to herb")
                            Character.Teleport(reactor.x,reactor.y-30)
                        else:
                            quest_item = Inventory.FindItemByID(4009286)
                            if quest_item.valid:
                                print("Throwing the quest items to reactor")
                                Inventory.SendChangeSlotPositionRequest(4, quest_item.pos, 0, 1)
                                time.sleep(2)
                            else:
                                print("Done throwing the quest items")
                                #packet to interact with the herb 03E3 [5995E50B]
                                #
                                time.sleep(10)
                                oPacket = Packet.COutPacket(herb_header)
                                oPacket.EncodeBuffer("[5995E50B]") #03E3 [C7323C0B] channel7 #03E3 [4835CA0B] channel2 03E3 [F2A6DC0B] #03E3 [FC0E430B]
                                print("Sending out packet to interact with herb") 
                                #Packet.SendPacket(oPacket) #E3 03 86 AB 34 00
                                time.sleep(2)
                                herb_drop = Field.FindItem(4034128)
                                if herb_drop.valid:
                                    print("Picking up herb")
                                    Character.Teleport(herb_drop.x,herb_drop.y)
                                    Character.LootItem()
                    while not SCLib.GetVar("HuntDone"):
                        drop = Field.FindItem(4009286)
                        if drop.valid:
                            SunCat.KamiTP(drop.x,drop.y)
                            Character.LootItem()
                        if Inventory.GetItemCount(4009286) >= 40:
                            SCLib.UpdateVar("HuntDone",True)
                            SunCat.StopTP()
                            print("Farmed enough items, finding reactor")
else:
    print("Not in game")
    time.sleep(1)

#channel 1 E3 03 5E 2A 41 00
#channel 2 E3 03 1C 95 48 00
#channel 3 E3 03 53 F8 04 00
#channel 4 E3 03 6A F8 04 00
#channel 5 E3 03 DA F7 04 00
#channel 6 E3 03 9F F2 16 00
#channel 7 E3 03 B2 9C 08 00
#channel 8 E3 03 31 F8 04 00
#channel 9 E3 03 D3 5F 30 00
#channel10 E3 03 51 F8 04 00
#channel11 E3 03 5E F8 04 00
#channel12 E3 03 01 F8 04 00
#channel13 
#channel14 E3 03 61 F8 04 00
#channel15 E3 03 87 88 09 00
#channel16 E3 03 86 AB 34 00 E3 03 50 1A 46 00
#channel17 E3 03 D3 F8 04 00 E3 03 6C E9 36 00
#channel18 E3 03 C4 93 24 00 E3 03 67 92 32 00
#channel19 E3 03 2F F8 04 00
#channel20 E3 03 A8 F8 04 00


#StartQuest(58901, 9130102) Regards ...
#rush to momijigaoka 807000000 then to 811000001 portal x = -1688 y = 32
#CompleteQuest(58901, 9130102)
#StartQuest(58902, 9130102)
#farm for 30 "100 Spells for the Serious Soldier" 4034126
#CompleteQuest(58902, 9130102)
#StartQuest(58903, 9130102)
#rush to 811000001 portal x = -843 y = -688 enter portal
#hidden field 811000004 farm for 30 "Contaminated Goblin Detritus" 4009286
#find reactor 8650012
#Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)
#MAYBE click NPC key or have to find packet
#make sure id 4034128 is in inventory
#rush back from portal 801 -28
#CompleteQuest(58903, 9130102)
#StartQuest(58907, 9130102)
#rush to momijigaoka through portal  810  -28
#teleport to 40 32
#CompleteQuest(58907, 9130008)
#enter heizen temple through portal x = -1688 y = 32
#StartQuest(58908, 9130103)
#StartQuest(58909, 9130104)
#StartQuest(58910, 9130103)
#StartQuest(58911, 9130103)
#CompleteQuest(58911, 9130103)
#StartQuest(58913, 9130103)
#find use item "Special Metamorph Potion" 2432732
#register "Kanna"
#in map 811000099 tp x = -141 y = -142 enter portal
#StartQuest(58941, 9130107)
#reactor 03E3 [7B1F2A0C]         0096 68D1671A D770D751 150D3AB9 FC87002F 27A4E792 00000000 00000000 96B65DE9
#find item "Lost Sack" 4034177 in field and loot
#CompleteQuest(58941, 9130107)
#StartQuest(58942, 9130107)
#enter portal in map 811000014   -124  -238
#hunt for "Princess No's Orders" 4034158 use "attack"
#rush back to 811000014 in map 811000098 from portal -611 122
#CompleteQuest(58942, 9130107)
#StartQuest(58943, 9130107)
#enter portal in map 811000014   -124  -238
#hunt for red jar 4034159 yellow jar 4034161 and blue jar 4034160
#rush back to 811000014 in map 811000098 from portal -611 122
#CompleteQuest(58943, 9130107)
#StartQuest(58944, 9130107)
#enter portal in map 811000014 947 62
#hunt 100 spearman
#rush back in map 811000015  -667  62 portal
#CompleteQuest(58944, 9130107)
#StartQuest(58945, 9130107)
#enter portal in map 811000014 947 62
#enter portal in map 811000015 947 62
#hunt 150 swordsman
#enter portal in map 811000016 -488 62
#enter portal in map 811000015 -667 62
#CompleteQuest(58945, 9130107)
#StartQuest(58946, 9130107)
#enter portal in map 811000014 947 62
#enter portal in map 811000015 947 62
#enter portal in map 811000016 933 62
#hunt 150 horsemen
#enter portal in map 811000017 -667 62
#enter portal in map 811000016 -488 62
#enter portal in map 811000015 -667 62
#CompleteQuest(58946, 9130107)
#StartQuest(58947, 9130107)
#enter portal in map 811000014 947 62
#enter portal in map 811000015 947 62
#enter portal in map 811000016 933 62
#enter portal in map 811000017 1035 62
#teleport to 399 62
#CompleteQuest(58947, 9130108)

#StartQuest(58963, 9130108)
#teleport to 6 62
#drop 4034136 "Wrapped Jars"
#StartQuest(58964, 0)
#in map 811000019 enter portal 180 -73
#kill miromu
#CompleteQuest(58964, 0)
#StartQuest(58965, 0)

#in map 811000020 enter portal -579 146
#StartQuest(58950, 0)
#in map 811000019 enter portal 1293 62
#StartQuest(58966, 0)
#in map 811000021 enter portal 973 62
#kill pink whale
#CompleteQuest(58966, 0)
#in map 811000025 enter portal -16 -70
#kill
#in map 811000026 enter portal 794 -55
#kill
#in map 811000027 enter portal 574 187
#in map 811000029 teleport to 205 -205
#StartQuest(58967, 9130116)
#StartQuest(58968, 0)
#in map 811000029 enter portal -616 -205
#in map 811000027 enter portal -603 187
#in map 811000026 enter portal -607 187
#in map 811000025 enter portal 1106 62
#in map 811000028 enter portal -59 -221
#in map 811000033 kill
#CompleteQuest(58968, 0)