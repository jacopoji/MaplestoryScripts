'''
Links skills
TODO:
Kanna           DONE
Luminous        DONE
Demon Avenger   DONE
Demon Slayer    DONE
Mercedes        DONE
Hayato          DONE
Xenon           
Phantom         
Illium          DONE(untested)
Cadena          DONE(untested)
Ark             DONE(untested)
Evan            
'''
curbrockhideout = [600050000,600050010,600050020]
#do Monster park how many times?
do_MP = True
do_MP_count = 2
buy_tickets = 1

#Starforce items or not
star_force = True
star_force_level = 10
safeguard = True
whitelist = []

#Zakum
DoZakumDaily=True


DoBlackGate = True

#Key to restart pers. variables
HotKey = 0x7A

#headers that might need to be updated every game update
#headers updated for v199
store_header = 0x00F5
block_header = 0x0695
buy_ticket_header = 0x0539
recv = 0x06CB
SF_header = 0x0138
StarForceRecv = 0x014D
collide_header = 0x0104
potential_header = 0x013E
potential_recv = 0x0271
BlockBuyHeader = 0x067C
BuyItemHeader = 0x00F4

#equip slot numbers
helmet_slot = -1
top_slot = -5
shoe_slot = -7
glove_slot = -8
cape_slot = -9
weapon_slot = -11
eye_slot = -3
face_slot = -2
earring_slot = -4
ring1_slot = -12
ring2_slot = -13
ring3_slot = -15
ring4_slot = -16
necklace_slot = -17
emblem_slot = -61

#accessories
aquatic_letter_eye = 1022231
condensed_power_crystal = 1012478
half_earrings = 1032022
rose_earrings = 1032017
horntail_ring = 1113149
horntail_earrings = 1032241
horntail_necklace = 1122000
chaos_horntail_necklace = 1122076
kanna_ring = 1113155
greed_pendant = 1122219
blackgate_mask = 1012535
blackgate_necklace = 1122312
blackgate_ring = 1113185

#lists
equip_slot_list = [helmet_slot,top_slot,shoe_slot,glove_slot,cape_slot,weapon_slot]
accessory_list = [aquatic_letter_eye,condensed_power_crystal,half_earrings,horntail_ring,horntail_necklace,chaos_horntail_necklace,kanna_ring,greed_pendant,blackgate_mask,blackgate_necklace,blackgate_ring]
accessory_slot_list = [eye_slot,face_slot,earring_slot,ring1_slot,ring2_slot,ring3_slot,ring4_slot,necklace_slot]
ring_list = [kanna_ring,blackgate_ring,horntail_ring]
face_list = [condensed_power_crystal,blackgate_mask]
eye_list = [aquatic_letter_eye]
earring_list = [half_earrings,rose_earrings,horntail_earrings]
necklace_list = [greed_pendant,blackgate_necklace,chaos_horntail_necklace,horntail_necklace]
blackgate_eqp = [1004549, 1012535, 1052952, 1082658, 1102840, 1113185, 1122312, 1132289, 1152191]

MP_Coin = 4310020
import Character,Field,Inventory,Key,Npc,Packet,Quest,Terminal,time,GameState,sys,os,Party,json,Login,datetime

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "/SunCat")

try:
    import SunCat, SCLib, SCHotkey
except:
    print("Couldn't find SunCat module")

SCLib.StartVars()
###persist variables
if SCLib.GetVar("MPDone") is None:
    SCLib.PersistVar("MPDone", False)
if SCLib.GetVar("DoingMP") is None:
    SCLib.PersistVar("DoingMP",False)
if SCLib.GetVar("retry_count") is None:
    SCLib.PersistVar("retry_count",0)
if SCLib.GetVar("KillZakumDaily") is None:
    SCLib.PersistVar("KillZakumDaily", DoZakumDaily)
if SCLib.GetVar("HasSpawned") is None:
    SCLib.PersistVar("HasSpawned", False)
if SCLib.GetVar("NowLockedVar") is None:
    SCLib.PersistVar("NowLockedVar", False)
if SCLib.GetVar("DoingZakum") is None:
    SCLib.PersistVar("DoingZakum",False)
if SCLib.GetVar("zakum_retry_count") is None:
    SCLib.PersistVar("zakum_retry_count",0)
if SCLib.GetVar("DoingBG") is None:
    SCLib.PersistVar("DoingBG",False)
HasSpawned = SCLib.GetVar("HasSpawned")
NowLockedVar = SCLib.GetVar("NowLockedVar")
KillZakumDaily = SCLib.GetVar("KillZakumDaily")
job = Character.GetJob()
level = Character.GetLevel()
field_id = Field.GetID()
pos = Character.GetPos()

#DEFINE MP DUNGEON OPTIONS
mapSleep = 2.0 #Delay in between entering and exiting map
shortSleep = 0.2 #Increase if lagging
mossy_tree_forest = "Mossy Tree Forest (Lv.115-124)"
sky_forest = "Sky Forest Training Center (Lv.120-129)"
secret_pirate = "Secret Pirate Hideout (Lv.125-134)"
other_world = "Otherworld Battleground (Lv.135-144)"
dangerous_forest = "Dangerously Isolated Forest (Lv.140-149)"
forbidden_time = "Forbidden Time (Lv.145-154)"
clandestine_ruins = "Clandestine Ruins (Lv.150-159)"
leopard_portal = (493,92)
tiger_portal = (661,92)

#map ids
CheifsResidence = 211000001
TheDoorToZakum = 211042300
EntranceToZakumAlter = 211042400
ZakumsAltar = [280030100,280030101,280030102,280030103,280030104]
TheCaveOfTrials3Zakum = 211042200
blackgate_maps = [610050000,610051300, 610051400, 610051500, 610051600, 610051700, 610051800, 610051900, 610052000, 610050100, 610050200, 610050600, 610050700, 610050800, 610051200, 610050300, 610050400, 610050500, 610050900, 610051000, 610051100]
henesys = 100000000

###Jobs, Jobs[0] = 1st job, Jobs[1] = 2nd job etc###
KannaJobs = [4200, 4210, 4211, 4212]
LuminousJobs = [2700, 2710, 2711, 2712]
ArkJobs = [15500, 15510, 15511, 15512]
BlasterJobs = [3700, 3710, 3711, 3712]
DemonAvengerJobs = [3101, 3120, 3121, 3122]
DemonSlayerJobs = [3100, 3110, 3111, 3112]
AranJobs = [2100, 2110, 2111, 2112]
MercedesJobs = [2300, 2310, 2311, 2312]
HayatoJobs = [4100, 4110, 4111, 4112]
BattleMageJobs = [3200, 3210, 3211, 3212]
WildHunterJobs = [3300, 3310, 3311, 3312]
KaiserJobs = [6100, 6110, 6111, 6112]
MihileJobs = [5100, 5110, 5111, 5112]
AngelicBusterJobs = [6500, 6510, 6511, 6512]
XenonJobs = [3600, 3610, 3611, 3612]
PhantomJobs = [2400, 2410, 2411, 2412]
EvanJobs = [2200, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218]
IlliumJobs = [15200,15210,15211,15212]
CadenaJobs = [6400,6410,6411,6412]

NpcTylusWarriorInstructor = 2020008
NpcRobeiraMagicianInstructor = 2020009
NpcReneBowmanInstructor = 2020010
NpcArecThiefInstructor = 2020011
NpcPedroPirateInstructor = 2020013
EncryptedSlateOfTheSquad = 2083000

#mob ids
NormalZakum = 8800002
NormalZakumv1 = 8800000
NormalZakumv2 = 8800001    
blackgate_boss = [9480235, 9480236, 9480237, 9480238, 9480239]

padding = 20
map1 = 101050010
map2 = 910150100
try:
    SCHotkey.StartHotkeys(100)
except:
    SCHotkey.StopHotkeys()
def KillPersistVarThred():
    print("Restarting SCLib variables")
    SCLib.StopVars()
    time.sleep(1)

SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F11

def toggle_rush_by_level(indicator):
    Terminal.SetCheckBox("Rush By Level",indicator)
    Terminal.SetRushByLevel(indicator)

def toggle_kami(indicator):
    Terminal.SetCheckBox("Kami Vac",indicator)

def toggle_HTR(indicator):
    Terminal.SetCheckBox("map/maprusher/hypertelerock",indicator)

def acceptQuest(quest, startnpc, startmap, currentmap):
    toggle_kami(False)
    if currentmap != startmap:
        Terminal.Rush(startmap)
    questnpc = Field.FindNpc(startnpc)
    if questnpc.valid:
        if pos.x != questnpc.x:
            time.sleep(0.5)
            Character.Teleport(questnpc.x, questnpc.y)
        else:
            Quest.StartQuest(quest, startnpc)
def completeQuest(quest, endnpc, endmap, grindmap, currentmap):
    toggle_kami(False)
    if Quest.CheckCompleteDemand(quest, endnpc) ==0:
        if currentmap != endmap:
            Terminal.Rush(endmap)
            time.sleep(2)
        questnpc = Field.FindNpc(endnpc)
        if questnpc.valid:
            if pos.x != questnpc.x:
                time.sleep(0.5)
                Character.Teleport(questnpc.x, questnpc.y)
            else:
                Quest.CompleteQuest(quest, endnpc)
    else:
        toggle_kami(True)
        if currentmap != grindmap:
            Terminal.Rush(grindmap)
def mapID(id):
    if type(id) is int:
        return Field.GetID() == id
    else:
        return Field.GetID() in id

def rush(mapid):
    if not Terminal.IsRushing():
        print("Rushing to map ID: {0}".format(mapid))
        Terminal.Rush(mapid)
        time.sleep(2)
    else:
        time.sleep(1)

def toHex(val, nbits):
    return ((val + (1 << nbits)) % (1 << nbits))


def teleport_enter(x,y):
    time.sleep(1)
    Character.Teleport(x,y)
    time.sleep(1)
    Character.EnterPortal()
    time.sleep(1)

def EnterPortal(name):
    portal = Field.FindPortal(name)
    pos = Character.GetPos()
    if pos.x != portal.x:
        toggle_kami(False)
        Character.Teleport(portal.x, portal.y-20)
        time.sleep(1)
    else:
        Character.EnterPortal()
        toggle_kami(True)

def gotoGreatSpirit():
    while Field.GetID() != map2:
        if (Field.GetID() != map1) and (Field.GetID() != map2):
            Terminal.Rush(map1)
            time.sleep(1)
        if Field.GetID() == map1:
            Character.TalkToNpc(1033211)
            time.sleep(1)

def StartQuest(quest, npc, map):
   if Terminal.IsRushing():
       time.sleep(1)
   elif mapID != map:
       time.sleep(3)
       Terminal.Rush(map)
   else:
       location = Field.FindNpc(npc) #change
       if location.valid:
           if abs(Character.GetPos().x - location.x) > 400:
               toggle_kami(False)
               Character.Teleport(location.x, location.y)
       time.sleep(1)
       Quest.StartQuest(quest, npc)
       time.sleep(1)
       toggle_kami(True)

def CompleteQuest(quest, npc, map):
   if Terminal.IsRushing():
       time.sleep(1)
   elif mapID != map:
       time.sleep(3)
       Terminal.Rush(map)
   else:
       location = Field.FindNpc(npc)
       if location.valid:
           if abs(Character.GetPos().x - location.x) > 400:
               toggle_kami(False)
               Character.Teleport(location.x, location.y)
       time.sleep(1)
       Quest.CompleteQuest(quest, npc)
       time.sleep(1)
       toggle_kami(True)

def KillMobAndLoot(map):
   if Terminal.IsRushing():
       time.sleep(1)
   elif mapID != map:
       Terminal.Rush(map)
       time.sleep(3)
   else:
       Terminal.SetCheckBox("Kami Loot", True)
       Terminal.SetCheckBox("Auto Loot", True)

#########Job specific advancements##########
def kannaFirst():
    if field_id == 807040000:
        if Terminal.IsRushing():
            print("Stopping terminal rush")
            Terminal.StopRush()
        print("Doing First Job")
        Terminal.SetCheckBox("Kami Vac",False)
        toggle_rush_by_level(False)
        quest_state = Quest.GetQuestState(57400)
        quest_state1 = Quest.GetQuestState(57401)
        quest_state2 = Quest.GetQuestState(57402)
        print("Doing quests")
        if quest_state != 2:
            print("Quest 0")
            if quest_state == 0:
                Quest.StartQuest(57400, 000000)
        elif quest_state1 != 2:
            print("Quest 1")
            if quest_state1 == 0:
                Quest.StartQuest(57401, 9130082)
            elif quest_state1 == 1:
                Quest.CompleteQuest(57401, 9130082)
        elif quest_state2 != 2:
            print("Quest 3")
            if quest_state2 == 0:
                Quest.StartQuest(57402, 000000)
            elif quest_state2 ==1:
                portal = Field.FindPortal("east00")
                if portal.valid:
                    print("Found portal at x={} y={}".format(portal.x,portal.y))
                    Character.Teleport(portal.x, portal.y-10)
                    time.sleep(1)
                    Character.EnterPortal()
    elif field_id == 807040100:
        quest = Quest.GetQuestState(57402)
        if quest == 1:
            Quest.CompleteQuest(57402, 9130083)
            print("Returning control to rush by level")
            toggle_rush_by_level(True)
            toggle_kami(True)
    else:
        time.sleep(1)
        fan = Inventory.FindItemByID(1552000)
        time.sleep(1)
        if fan.valid:
            print("Equipping fan")
            Inventory.SendChangeSlotPositionRequest(1, fan.pos, -11, -1)
            time.sleep(1)
        print("Setting up first job settings")
        Key.Set(0x44, 1, 42001000)
        time.sleep(1)

def LumiFirst():
    Quest.StartQuest(25560, 0)

def LumiSecond():
    Quest.StartQuest(25510, 1032209)

def LumiThird():
    Quest.StartQuest(25511, 1032209)

def LumiFourth():
    Quest.StartQuest(25512, 0)

def DAFirst():
    Terminal.SetCheckBox("Kami Vac",False)
    toggleAttack(False)
    if Quest.GetQuestState(23210) !=2:
        if Quest.GetQuestState(23210) == 0:
            Quest.StartQuest(23210, 2151000)
        elif Quest.CheckCompleteDemand(23210, 2153006) != 0:
            #need to fight the cat
            print("Entering cat fighting map")
            if field_id != 931050100:
                if field_id != 310020100:
                    Terminal.Rush(310020100)
                else:
                    teleport_enter(515,-14)
            else:
                Terminal.SetCheckBox("Kami Vac",True)
                toggleAttack(True)
        else:
            print("Done fighting")
            Quest.CompleteQuest(23210, 2153006)
    elif Quest.GetQuestState(23211) !=2:
        print("Second quest")
        if Quest.GetQuestState(23211) == 0:
            Quest.StartQuest(23211, 2153006)
        elif Quest.CheckCompleteDemand(23211, 2153006) == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection("Move ")
            Quest.CompleteQuest(23211, 2153006)
    elif Quest.GetQuestState(23212) !=2:
        print("third quest")
        if Quest.GetQuestState(23212) == 0:
            print("Start third quest")
            Quest.StartQuest(23212, 2151009)
        elif Quest.GetQuestState(23212) == 1:
            if field_id == 931050110:
                teleport_enter(111,-14)
                print("Rush out of instanced map")
            elif field_id != 310010000:
                Terminal.Rush(310010000)
                print("Rush to hide")
            else:
                Quest.CompleteQuest(23212, 2151009)
                toggle_rush_by_level(True)
                Terminal.SetCheckBox("Kami Vac",True)

def DASecond():
    Terminal.SetCheckBox("Kami Vac",False)
    toggleAttack(False)
    if Quest.GetQuestState(23213) !=2:
        if Quest.GetQuestState(23213) == 0:
            Quest.StartQuest(23213, 2151009)
        elif Quest.GetQuestState(23213) == 1:
            if field_id != 931050110:
                if field_id != 310020100:
                    Terminal.Rush(310020100)
                else:
                    teleport_enter(515,-14)
            else:
                Quest.CompleteQuest(23213, 2153006)
    elif Quest.GetQuestState(23218) != 2:
        if Quest.GetQuestState(23218) == 0:
            Quest.StartQuest(23218, 2153006)
        elif Quest.GetQuestState(23218) == 1:
            if Field.FindMob(9001037).valid:
                Terminal.StopRush()
                toggleAttack(True)
                toggle_kami(True)
            elif field_id == 931050120:
                toggle_kami(False)
                teleport_enter(109,-14)
            else:
                Quest.CompleteQuest(23218, 2153006)
        
def MercedesFirst():
    Quest.StartQuest(29952, 1033210)

def MercedesSecond():
    map1 = 101050010
    toggle_rush_by_level(False)
    #get an complete the first quest
    quest1 = Quest.GetQuestState(24010)
    #get an complete the second quest
    quest2 = Quest.GetQuestState(24011)
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(24010, 0)
            time.sleep(2)
        elif quest1 == 1:
            if Field.GetID() != map2:
                gotoGreatSpirit()
            else:
                Quest.CompleteQuest(24010, 1033210)
    elif quest2 != 2:
        if quest2 == 0:
            if Field.GetID() != map2:
                gotoGreatSpirit()
            else:
                Quest.StartQuest(24011, 1033210)
                time.sleep(1)
        elif quest2 == 1:
            if Field.GetID() != map2:
                gotoGreatSpirit()
            else:
                Quest.CompleteQuest(24011, 1033210)
def HayatoFirst():
    if field_id == 807040000:
        if Terminal.IsRushing():
            print("Stopping terminal rush")
            Terminal.StopRush()
        print("Doing First Job")
        Terminal.SetCheckBox("Kami Vac",False)
        toggle_rush_by_level(False)
        quest_state = Quest.GetQuestState(57102)
        quest_state1 = Quest.GetQuestState(57103)
        quest_state2 = Quest.GetQuestState(57104)
        print("Doing quests")
        if quest_state != 2:
            print("Quest 0")
            if quest_state == 0:
                Quest.StartQuest(57102, 000000)
            elif quest_state == 1:
                Quest.CompleteQuest(57102, 9130031)
        elif quest_state1 != 2:
            print("Quest 1")
            if quest_state1 == 0:
                Quest.StartQuest(57103, 9130031)
            elif quest_state1 == 1:
                Quest.CompleteQuest(57103, 9130031)
        elif quest_state2 != 2:
            print("Quest 3")
            if quest_state2 == 0:
                Quest.StartQuest(57104, 9130031)
            elif quest_state2 ==1:
                portal = Field.FindPortal("east00")
                if portal.valid:
                    print("Found portal at x={} y={}".format(portal.x,portal.y))
                    Character.Teleport(portal.x, portal.y-10)
                    time.sleep(1)
                    Character.EnterPortal()
    elif field_id == 807040100:
        quest = Quest.GetQuestState(57104)
        if quest == 1:
            Quest.CompleteQuest(57104, 9130024)
            print("Returning control to rush by level")
            toggle_rush_by_level(True)
            toggle_kami(True)
    else:
        toggle_rush_by_level(True)
        toggle_kami(True)

def IlliumZero():
    pet = Inventory.FindItemByID(2434265)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)

    while Terminal.IsRushing():
        time.sleep(1)

    if level == 1 and field_id == 940202009:
        toggle_kami(False)
        Character.Teleport(-3319, 79)
        time.sleep(2)
     
        time.sleep(1)
        Character.EnterPortal()
        time.sleep(4)

    if level == 1 and field_id == 940202011:
        Character.Teleport(-3400, 79)
        Character.Teleport(-3000, 5000)
     
    if field_id == 940202013 or field_id == 940202014 or field_id == 940202015:
        mob = Field.FindMob(2400418)
        if mob.valid:
            Character.Teleport(mob.x, 20000)
            Character.BasicAttack()
        else:
            time.sleep(1)
            Character.Teleport(832,813)
            time.sleep(1)
            Character.EnterPortal()
            toggle_kami(True)
         
    # some questing begins here
    preparations = Quest.GetQuestState(34800)
    collecting = Quest.GetQuestState(34801)
    if preparations != 2:
        if preparations == 0:
            Quest.StartQuest(34800, 3001330)
            time.sleep(1)

        elif Quest.CheckCompleteDemand(34800, 3001330) != 0:
            Inventory.SendChangeSlotPositionRequest(1, 1, -11, -1)
            time.sleep(1)
            Inventory.UseItem(2000046)
            time.sleep(1)
        else:
            Quest.CompleteQuest(34800, 3001330)

 
    if collecting != 2:
        if collecting == 0:
            Quest.StartQuest(34801, 3001330)
            time.sleep(1)
        elif Quest.CheckCompleteDemand(34801, 3001330) != 0:
            if field_id == 940202012:
                toggle_kami(False)
                Character.Teleport(13,813)
                time.sleep(1)
                Character.EnterPortal()
                time.sleep(1)
            if field_id == 940202015:
                mob = Field.FindMob(2400418)
                if mob.valid:
                    Character.Teleport(mob.x, 10000)
                    Character.BasicAttack()
                else:
                    Character.Teleport(832,813)
                    time.sleep(1)
                    Character.EnterPortal()
                    time.sleep(1)
            if field_id in range(940203000, 940203010) :
                mob = Field.FindMob(2400413)
                item = Field.FindItem(4036162)
                if item.valid:
                    if item.y in range(pos.y - 50, pos.y + 50):
                        Character.Teleport(item.x, 20000)
                        Character.LootItem()
                    elif item.y < 600:
                        Character.Teleport(-146, 20000)
                        time.sleep(2)
                        Character.Jump()
                        Character.MoveY(584, 3000)
                        time.sleep(1)
                    else:
                        Character.JumpDown()
                elif mob.valid:
                    if mob.y in range(pos.y - 50, pos.y + 50):
                        Character.Teleport(mob.x, 10000)
                        Character.BasicAttack()
                    elif mob.y < 600:
                        Character.Teleport(-146, 20000)
                        time.sleep(2)
                        Character.Jump()
                        Character.MoveY(584, 1000)
                        time.sleep(1)
                    else:
                        Character.JumpDown()
 
        else:
            Quest.CompleteQuest(34801, 3001330)
            Character.Teleport(803, 50000)
            Character.EnterPortal()
            toggle_kami(True)

def IlliumFirst():
    grossular = Quest.GetQuestState(34802)
    combat = Quest.GetQuestState(34803)
    social = Quest.GetQuestState(34804)
    crystalGate = Quest.GetQuestState(34805)
    specialActivity = Quest.GetQuestState(34806)
    dean = Quest.GetQuestState(34807)
    divine1 = Quest.GetQuestState(34808)
    cries = Quest.GetQuestState(34809)
    gate2 = Quest.GetQuestState(34811)
    aftergate = Quest.GetQuestState(34812)
    verdantFlora = Quest.GetQuestState(34813)
    festival2 = Quest.GetQuestState(34814)
    festival3 = Quest.GetQuestState(34815)
    festival4 = Quest.GetQuestState(34816)
    jobadv = Quest.GetQuestState(34817)
    escape = Quest.GetQuestState(34718)
    if Terminal.IsRushing() and (field_id == 402000521 or field_id == 402000524):
        Character.EnterPortal()
        Key.Press(0x26) #up key
    if field_id == 402000526 and specialActivity != 2:
        Quest.StartQuest(34806, 0)
 
    if grossular != 2:
        if grossular == 0:
            rush(402000526)
            Quest.StartQuest(34802, 3001332)
         
        elif Quest.CheckCompleteDemand(34802, 3001332) != 0:
            if field_id != 402000511:
                rush(402000511)
            time.sleep(1)
         
        else:
            rush(402000526)
            Quest.CompleteQuest(34802, 3001332)
 
    elif combat != 2:
        if combat == 0:
            if field_id != 402000527:
                rush(402000527)
            print("Pressing Control Key")
            Key.Press(0x11)
            time.sleep(3)
            Key.Press(0x11)
            Quest.StartQuest(34803, 3001333)
         
        elif Quest.CheckCompleteDemand(34803, 3001333) != 0:
            rush(402000531)
            if pos.x not in range(440,470):
                toggle_kami(False)
                Character.Teleport(461, 20000)
     
        else:
            rush(402000527)
            Quest.CompleteQuest(34803, 3001333)
         
    elif social != 2:
        if social == 0:
            rush(402000530)
            Quest.StartQuest(34804, 3001360)
     
        elif Quest.CheckCompleteDemand(34804, 3001360) != 0:
            Character.TalkToNpc(3001314)
            time.sleep(3)
            Character.TalkToNpc(3001315)
            time.sleep(3)
            Character.TalkToNpc(3001316)
            time.sleep(3)
            Character.TalkToNpc(3001317)
            time.sleep(3)
            Character.TalkToNpc(3001318)
         
        else:
            Quest.CompleteQuest(34804, 3001360)
 
    elif crystalGate != 2:
        if crystalGate == 0:
            rush(402000530)
            Quest.StartQuest(34805, 3001334)
            time.sleep(2)
         
        elif Quest.CheckCompleteDemand(34805, 3001334) != 0:
            if field_id != 402000517:
                rush(402000517)
         
            else:
                time.sleep(1)
                # remove these lines if you're using mob vac
                Character.Teleport(1500, 50000)
             
        else:
            rush(402000530)
            while Terminal.IsRushing():
                time.sleep(1)
            Quest.CompleteQuest(34805, 3001334)
            rush(402000528)
 
    elif specialActivity != 2:
        if specialActivity == 0:
            Quest.StartQuest(34806, 0)
     
        else:
            rush(402000528)
            Quest.CompleteQuest(34806, 3001331)
         
    elif dean != 2:
        if dean == 0:
            rush(402000532)
            Quest.StartQuest(34807, 3001337)
            time.sleep(1)
         
        elif Quest.CheckCompleteDemand(34807, 3001337) != 0:
            rush(402000534)
            Character.Teleport(500, 10000)
         
        else:
            rush(402000532)
            Quest.CompleteQuest(34807, 3001337)
                 
    elif divine1 != 2:
        if divine1 == 0:
            rush(402000526)
            Quest.StartQuest(34808, 3001335)
         
        elif Quest.CheckCompleteDemand(34808, 3001335) != 0:
            rush(402000514)
            print("Long Sleep")
            time.sleep(30)
            Quest.StartQuest(34809, 0)
            while True:
                if GameState.IsInGame():
                    toggle_kami(True)
                    rush(402000513)
                    cries = Quest.GetQuestState(34809)
                    after = Quest.GetQuestState(34810)
                    if cries != 2:
                        if Quest.CheckCompleteDemand(34809, 3001338) != 0:
                            rush(402000513)
                            while Terminal.IsRushing():
                                time.sleep(1)
                        else:
                            Quest.CompleteQuest(34809, 3001338)
                    elif after != 2:
                        if after == 0:
                            time.sleep(1)
                            Npc.ClearSelection()
                            time.sleep(1)
                            Npc.RegisterSelection("Choice 1")
                            time.sleep(1)
                            Quest.StartQuest(34810, 3001338)
                    else:
                        break
                else:
                    break
             
        else:
            rush(402000526)
            toggle_kami(False)
            Quest.CompleteQuest(34808, 3001335)
            rush(402000530)
 
    elif gate2 != 2:
        if gate2 == 0:
            rush(402000530)
         
        elif Quest.CheckCompleteDemand(34811, 3001334) != 0:
            toggle_kami(False)
            Character.Teleport(0, 10000)
            rush(402000535)
         
        else:
            rush(402000530)
            Quest.CompleteQuest(34811, 3001334)
         
    elif aftergate != 2:
        if aftergate == 0:
            rush(402000530)
            Quest.StartQuest(34812, 0)
            time.sleep(5)
     
        elif Quest.CheckCompleteDemand(34812, 3001336) != 0:
            rush(402000501)
         
        else:
            Quest.CompleteQuest(34812, 3001336)
         
    elif verdantFlora != 2:
        if verdantFlora == 0:
            rush(402000501)
            print("Might get stuck here")
            #E6 00 06 01 00 00 00 00
            Npc.ClearSelection()
            time.sleep(2)
            Npc.RegisterSelection("Of course!")
            time.sleep(1)
            Quest.StartQuest(34813, 3001336)
            time.sleep(1)
            Npc.ClearSelection()
            time.sleep(2)
            Npc.RegisterSelection("Of ")
            time.sleep(2)
         
        elif Quest.CheckCompleteDemand(34813, 3001336) != 0:
            rush(402000502)
            Character.Teleport(1309, 10000)
         
        else:
            rush(402000501)
            while Terminal.IsRushing():
                time.sleep(1)
            Quest.CompleteQuest(34813, 3001336)
            time.sleep(5)
            rush(402000529)
         
    elif festival2 != 2:
        if festival2 == 0:
            rush(402000529)
            Quest.StartQuest(34814, 3001339)
            toggle_kami(False)
            time.sleep(3)
         
        elif Quest.CheckCompleteDemand(34814, 3001339) != 0:
            rush(402000507)
            time.sleep(1)
         
        else:
            rush(402000529)
            Quest.CompleteQuest(34814, 3001339)
            time.sleep(1)
         
    elif festival3 != 2:
        if festival3 == 0:
            rush(402000529)
            Quest.StartQuest(34815, 3001339)
            time.sleep(3)
     
        elif Quest.CheckCompleteDemand(34815, 3001339) != 0:
            rush(402000509)
            time.sleep(1)
         
        else:
            rush(402000529)
            Quest.CompleteQuest(34815, 3001339)
            time.sleep(1)
         
    elif festival4 != 2:
        if festival4 == 0:
            rush(402000529)
            Quest.StartQuest(34816, 3001339)
            time.sleep(2)
         
        elif Quest.CheckCompleteDemand(34816, 3001339) != 0:
            rush(402000504)
            time.sleep(1)
         
        else:
            rush(402000529)
            Quest.CompleteQuest(34816, 3001339)
            time.sleep(1)
                 
    elif jobadv != 2:
        if jobadv == 0:
            rush(402000529)
            Quest.StartQuest(34817, 3001339)
            time.sleep(2)
     
        elif Quest.CheckCompleteDemand(34817, 3001339) != 0:
            if field_id == 402000529:
                rush(402000504)
             
            elif field_id in range(940202100, 940202199):
                mob = Field.FindMob(2400420)
                if mob.valid:
                    time.sleep(20)
                    Character.Teleport(-500, 20000)
                    time.sleep(1)
                else:
                    Character.Teleport(1, -683)
                    time.sleep(2)
                    Character.EnterPortal()
                    Character.EnterPortal()
                    time.sleep(3)
         
            elif field_id in range(940202200, 940202299):
                Character.JumpDown()
                time.sleep(2)
                Character.JumpDown()
                time.sleep(10)
                Character.JumpDown()
                mob = Field.FindMob(2400420)
                mob2 = Field.FindMob(2400421)
                if mob.valid or mob2.valid:
                    time.sleep(1)
                else:
                    Character.Teleport(-583, -31)
                    time.sleep(2)
                    Character.EnterPortal()
                    Character.EnterPortal()
            elif field_id in range(940202300, 940202399):
                Character.Teleport(35, 10000)
                Character.JumpDown()
                time.sleep(1)
                mob = Field.FindMob(2400421)
                if mob.valid:
                    time.sleep(1)
                else:
                    Character.Teleport(1,-638)
                    time.sleep(1)
                    Character.EnterPortal()
            elif field_id in range(940202400, 940202499):
                Character.Teleport(-1, -638)
                time.sleep(1)
                Character.EnterPortal()
        else:
            time.sleep(1)
    elif escape != 2:
        rush(940202032)
        Character.Teleport(915, 10000)
        Quest.CompleteQuest(34718, 3001344)
        time.sleep(10)

def IlliumSecond():
    escape = Quest.GetQuestState(34818)
    lookback = Quest.GetQuestState(34820)
    if escape != 2:
        rush(940202032)
        toggle_kami(False)
        Character.Teleport(332, 10000)
        Quest.CompleteQuest(34818, 3001344)
        time.sleep(10)
     
    elif field_id == 940202032 and escape == 2:
        Quest.StartQuest(34860, 0)
        Character.Teleport(332, 10000)
        Character.EnterPortal()

    elif field_id in range(940202500, 940202599):
        Character.Teleport(25, 10000)
        Character.EnterPortal()

    elif field_id in range(940202600, 940202699): 
        Character.Teleport(25, 10000)
        Character.EnterPortal()
         
    elif field_id in range(940202700, 940202799):
        Character.Teleport(25, 10000)
        Character.EnterPortal()
     
    elif field_id == 940202036:
        Character.Teleport(0, 200)
 
    elif field_id == 940202037:
        time.sleep(4)
        Character.Teleport(803,813)
        time.sleep(1)
        Character.EnterPortal()
     
    elif lookback != 2:
        if lookback == 0:
            rush(940202040)
            Quest.StartQuest(34820, 3001343)
         
        elif Quest.CheckCompleteDemand(34820, 3000002) == 0:
            rush(400000000)
            Quest.CompleteQuest(34820, 3000002)
            print("Completed all Illium Quests and now returning control to rush by level")
            time.sleep(1)
            toggle_rush_by_level(True)
            
def CadenaFirst():
    quest1 = Quest.GetQuestState(34600)
    quest2 = Quest.GetQuestState(34601)
    quest3 = Quest.GetQuestState(34602)
    quest4 = Quest.GetQuestState(34603)
    quest5 = Quest.GetQuestState(34656)
    quest6 = Quest.GetQuestState(34604)
    quest7 = Quest.GetQuestState(34605)
    quest8 = Quest.GetQuestState(34606)
    quest9 = Quest.GetQuestState(34607)
    quest10 = Quest.GetQuestState(34608)
    quest11 = Quest.GetQuestState(34609)
    quest12 = Quest.GetQuestState(34610)
    quest13 = Quest.GetQuestState(34611)
    quest14 = Quest.GetQuestState(34612)
    quest15 = Quest.GetQuestState(34613)
    quest16 = Quest.GetQuestState(34614)
    quest17 = Quest.GetQuestState(34615)
    quest18 = Quest.GetQuestState(34616)
    quest19 = Quest.GetQuestState(34617)
    quest20 = Quest.GetQuestState(34618)
    quest21 = Quest.GetQuestState(34619)
    quest22 = Quest.GetQuestState(34620)
    quest23 = Quest.GetQuestState(34621)
    quest24 = Quest.GetQuestState(34622)
    quest25 = Quest.GetQuestState(34623)
    quest26 = Quest.GetQuestState(34624)
    quest27 = Quest.GetQuestState(34625)
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(34600, 0)
            time.sleep(10)
        elif field_id == 940200500:
            EnterPortal("west00")
        elif field_id == 940200501:
            EnterPortal("up00")
    if quest2 != 2:
        if quest2 == 0:
            if field_id == 940200502:
                Quest.StartQuest(34601, 3001221)
            elif field_id == 940200600 or 940200601:
                Key.Press(0x11)
                time.sleep(1)
        elif quest2 == 1:
            Quest.CompleteQuest(34601, 3001221)
    elif quest3 != 2:
        if field_id == 402000002:
            if quest3 == 0:
                Quest.StartQuest(34602, 3001202)
                time.sleep(10)
            elif quest3 == 1:
                Npc.ClearSelection()
                Npc.RegisterSelection("remain")
                Npc.RegisterSelection("Never")
                Quest.CompleteQuest(34602, 3001202)
                time.sleep(8)
        else:
            Terminal.Rush(402000002)
    elif quest4 != 2:
        if field_id == 402000002:
            if quest4 == 0:
                Quest.StartQuest(34603, 3001202)
            elif quest4 == 1:
                if Quest.CheckCompleteDemand(34603, 3001202) == 0:
                    Quest.CompleteQuest(34603, 3001202)
                else:
                    Inventory.UseItem(2437264)
        else:
            Terminal.Rush(402000002)
    elif quest5 != 2:
        if field_id != 402000001:
            Terminal.Rush(402000001)
        else:
            if quest5 == 0:
                Quest.StartQuest(34656, 3001200)
    elif quest6 != 2:
        if field_id != 402000001:
            Terminal.Rush(402000001)
        else:
            if quest6 == 0:
                Quest.StartQuest(34604, 3001200)
            elif quest6 == 1:
                pos = Character.GetPos()
                if pos.x != -308:
                    toggle_kami(False)
                    Character.Teleport(-308, 304)
                else:
                    Quest.CompleteQuest(34604, 3001210)
                    toggle_kami(True)
    elif quest7 != 2:
        if quest7 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34605, 3001210)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(34605, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34605, 3001210)
            else:
                if field_id != 402000110:
                    Terminal.Rush(402000110)
    elif quest8 != 2:
        if quest8 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34606, 3001210)
        elif quest8 == 1:
            if Quest.CheckCompleteDemand(34606, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34606, 3001210)
            else:
                if field_id != 402000111:
                    Terminal.Rush(402000111)
    elif quest9 != 2:
        if quest9 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34607, 3001210)
        elif quest9 == 1:
            if Quest.CheckCompleteDemand(34607, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34607, 3001210)
            elif field_id != 402000112:
                Terminal.Rush(402000112)
    elif quest10 != 2:
        if quest10 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                pos = Character.GetPos()
                if pos.x != -308:
                    toggle_kami(False)
                    Character.Teleport(-308, 304)
                else:
                    Quest.StartQuest(34608, 3001210)
                    toggle_kami(True)
        if quest10 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.CompleteQuest(34608, 3001203)
    elif quest11 != 2:
        if quest11 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34609, 3001210)
        elif quest11 == 1:
            if Quest.CheckCompleteDemand(34609, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34609, 3001210)
            else:
                if field_id != 402000220:
                    Terminal.Rush(402000220)
    elif quest12 != 2:
        if quest12 == 0:
            if field_id != 402000200:
                Terminal.Rush(402000200)
            else:
                Quest.StartQuest(34610, 3001218)
        elif quest12 == 1:
            Quest.CompleteQuest(34610, 3001218)
            Terminal.Sleep(3)
    elif quest13 != 2:
        if quest13 == 0:
            if field_id == 940200700:
                time.sleep(8)
                EnterPortal("next00")
                time.sleep(3)
            elif field_id == 940200800:
                time.sleep(8)
                EnterPortal("next00")
                time.sleep(3)
            elif field_id == 940200900:
                time.sleep(8)
                EnterPortal("next00")
                time.sleep(3)
            else:
                pos = Character.GetPos()
                if pos.x != -506:
                    toggle_kami(False)
                    Character.Teleport(-506, 45)
                    time.sleep(2)
                else:
                    Quest.StartQuest(34611, 3001218)
                    toggle_kami(True)
        elif quest13 == 1:
            if field_id == 940200900:
                EnterPortal("next00")
                time.sleep(5)
            if field_id == 402000210:
                Quest.CompleteQuest(34611, 3001214)
    elif quest14 != 2:
        if quest14 == 0:
            Quest.StartQuest(34612, 3001214)
        elif quest14 == 1:
            Quest.CompleteQuest(34612, 3001214)
            time.sleep(2)
    elif quest15 != 2:
        if quest15 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                time.sleep(3)
                Quest.StartQuest(34613, 0)
        elif quest15 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.CompleteQuest(34613, 3001210)
                time.sleep(2)
    elif quest16 != 2:
        if quest16 == 0:
            Quest.StartQuest(34614, 0)
        elif quest16 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                pos = Character.GetPos()
                if pos.x != -98:
                    toggle_kami(False)
                    Character.Teleport(-98, 304)
                else:
                    Quest.CompleteQuest(34614, 3001226)
                    toggle_kami(True)
    elif quest17 != 2:
        if quest17 == 0:
            Quest.StartQuest(34615, 0)
            time.sleep(3)
        elif quest17 == 1:
            # Talk to Gusto
            Terminal.Rush(402000200)
            while Terminal.IsRushing():
                time.sleep(5)
            Character.TalkToNpc(3001218)
            time.sleep(3)

            # Talk to Corbo
            Terminal.Rush(402000100)
            while Terminal.IsRushing():
                time.sleep(5)
            Character.TalkToNpc(3001219)
            time.sleep(3)

            # Talk to Antuin
            Terminal.Rush(402000000)
            while Terminal.IsRushing():
                time.sleep(5)
            pos = Character.GetPos()
            if pos.x != -1639:
                toggle_kami(False)
                Character.Teleport(-1639, 35-20)
                time.sleep(3)
            Character.TalkToNpc(3001212)
            time.sleep(8)
            toggle_kami(True)
    elif quest18 != 2:
        if quest18 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34616, 0)
        elif quest18 == 1:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.CompleteQuest(34616, 3001204)
    elif quest19 != 2:
        if quest19 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34617, 3001204)
        elif quest19 == 1:
            if Quest.CheckCompleteDemand(34617, 3001204) == 0:
                if field_id != 402000000:
                    Terminal.Rush(402000000)
                else:
                    pos = Character.GetPos()
                    if pos.x != -1639:
                        toggle_kami(False)
                        Character.Teleport(-1639, 35 - 20)
                    else:
                        Quest.CompleteQuest(34617, 3001204)
                        toggle_kami(True)
            else:
                if field_id != 402000120:
                    Terminal.Rush(402000120)
    elif quest20 != 2:
        if quest20 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34618, 3001204)
        elif quest20 == 1:
            if Quest.CheckCompleteDemand(34618, 3001204) == 0:
                if field_id != 402000000:
                    Terminal.Rush(402000000)
                else:
                    pos = Character.GetPos()
                    if pos.x != -1639:
                        toggle_kami(False)
                        Character.Teleport(-1639, 35 - 20)
                    else:
                        Quest.CompleteQuest(34618, 3001204)
                        toggle_kami(True)
            else:
                if field_id != 402000121:
                    Terminal.Rush(402000121)
    elif quest21 != 2:
        if quest21 == 0:
            while Field.GetID() == 940200507:
                Key.Press(0x20)
                Key.Up(0x20)
                time.sleep(0.1)
            else:
                pos = Character.GetPos()
                if pos.x != -1701:
                    toggle_kami(False)
                    Character.Teleport(-1701, 27 - 20)
                    time.sleep(3)
                Quest.StartQuest(34619, 3001204)
                toggle_kami(True)
    elif quest22 != 2:
        if quest22 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34620, 3001212)
        elif quest22 == 1:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.CompleteQuest(34620, 3001212)
    elif quest23 != 2:
        if quest23 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34621, 0)
        elif quest23 == 1:
            if Quest.CheckCompleteDemand(34621, 3001228) == 0:
                if field_id != 402000000:
                    Terminal.Rush(402000000)
                else:
                    Quest.CompleteQuest(34621, 3001228)
            else:
                if field_id != 402000122:
                    Terminal.Rush(402000122)
    elif quest24 != 2:
        if quest24 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34622, 0)
        elif quest24 == 1:
            if field_id != 402000301:
                Terminal.Rush(402000301)
            else:
                Quest.CompleteQuest(34622, 3001220)
    elif quest25 != 2:
        if quest25 == 0:
            if field_id == 940201000:
                time.sleep(1)
            elif field_id != 402000301:
                Terminal.Rush(402000301)
            else:
                Quest.StartQuest(34623, 3001223)
        elif quest25 == 1:
            if field_id == 402000301:
                Quest.CompleteQuest(34623, 3001211)
    elif quest26 != 2:
        if quest26 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34624, 3001200)
        elif quest26 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.CompleteQuest(34624, 3001200)
    elif quest27 != 2:
        if quest27 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34625, 3001200)
        elif quest27 == 1:
            if field_id != 402000400:
                Terminal.Rush(402000400)
            else:
                Quest.CompleteQuest(34625, 3001205)
                
    if job == 6400 and level >= 30:
        Quest.StartQuest(34657, 3001250)
        toggle_kami(True)
        toggle_rush_by_level(True)

def ArkFirst():
    quest1 = Quest.GetQuestState(34915)
    quest2 = Quest.GetQuestState(34916)
    quest3 = Quest.GetQuestState(34917)
    quest4 = Quest.GetQuestState(34918)
    quest5 = Quest.GetQuestState(34919)
    quest6 = Quest.GetQuestState(34920)
    quest7 = Quest.GetQuestState(34921)
    quest8 = Quest.GetQuestState(34922)
    quest9 = Quest.GetQuestState(34923)
    quest10 = Quest.GetQuestState(34924)
    quest11 = Quest.GetQuestState(34925)
    quest12 = Quest.GetQuestState(34926)
    quest13 = Quest.GetQuestState(34927)
    quest14 = Quest.GetQuestState(34928)
    quest15 = Quest.GetQuestState(34929)
    quest16 = Quest.GetQuestState(34930)
    quest17 = Quest.GetQuestState(34931)
    quest18 = Quest.GetQuestState(34932)
    quest19 = Quest.GetQuestState(34933)
    quest20 = Quest.GetQuestState(34934)
    quest21 = Quest.GetQuestState(34935)
    quest22 = Quest.GetQuestState(34936)
    quest23 = Quest.GetQuestState(34937)
    quest24 = Quest.GetQuestState(34938)
    quest25 = Quest.GetQuestState(34902)
    if quest1 != 2:
        print("1")
        if quest1 == 0:
            StartQuest(34915, 3001406, 402000615)
        if field_id == 940205000:
            toggle_kami(True)
    elif quest2 != 2:   
        print("2")
        if quest2 == 0:
            toggle_kami(False)
            StartQuest(34916, 3001400, 402000600)
        elif quest2 == 1:
            toggle_kami(False)
            CompleteQuest(34916, 3001400, 402000600)
    elif quest3 != 2:
        print("3")
        if quest3 == 0:
            toggle_kami(False)
            StartQuest(34917, 3001400, 402000600)
        elif quest3 == 1:
            if Quest.CheckCompleteDemand(34917, 3001400):
                KillMobAndLoot(402000610)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34917, 3001400, 402000600)
    elif quest4 != 2:
        print("4")
        if quest4 == 0:
            toggle_kami(False)
            StartQuest(34918, 3001400, 402000600)
        elif quest4 == 1:
            toggle_kami(False)
            CompleteQuest(34918, 3001401, 402000600)
    elif quest5 != 2:
        print("5")
        if quest5 == 0:
            toggle_kami(False)
            StartQuest(34919, 3001401, 402000600)
        elif quest5 == 1:
            if Quest.CheckCompleteDemand(34919, 3001401):
                KillMobAndLoot(402000611)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34919, 3001401, 402000600)
    elif quest6 != 2:
        print("6")
        if quest6 == 0:
            toggle_kami(False)
            StartQuest(34920, 3001401, 402000600)
        elif quest6 == 1:
            CompleteQuest(34920, 3001402, 402000600)
    elif quest7 != 2:
        print("7")
        if quest7 == 0:
            toggle_kami(False)
            StartQuest(34921, 3001402, 402000600)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(34921, 3001402):
                KillMobAndLoot(402000612)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34921, 3001402, 402000600)
    elif quest8 != 2:
        print("8")
        if quest8 == 0:
            toggle_kami(False)
            StartQuest(34922, 3001402, 402000600)
        elif quest8 == 1:
            toggle_kami(False)
            CompleteQuest(34922, 3001403, 402000600)
    elif quest9 != 2:
        print("9")
        if quest9 == 0:
            toggle_kami(False)
            StartQuest(34923, 3001404, 402000613)
        elif quest9 == 1:
            if Quest.CheckCompleteDemand(34923, 3001404):
                KillMobAndLoot(402000613)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34923, 3001404, 402000613)
    elif quest10 != 2:
        print("10")
        if quest10 == 0:
            toggle_kami(False)
            StartQuest(34924, 3001400, 402000600)
        elif quest10 == 1:
            toggle_kami(False)
            CompleteQuest(34924, 3001405, 402000614)
    elif quest11 != 2:
        print("11")
        if quest11 == 0:
            toggle_kami(False)
            StartQuest(34925, 3001405, 402000614)
        elif quest11 == 1:
            toggle_kami(False)
            CompleteQuest(34925, 3001400, 402000600)
    elif quest12 != 2:
        print("12")
        if quest12 == 0:
            toggle_kami(False)
            StartQuest(34926, 3001402, 402000600)
        elif quest12 == 1:
            if Quest.CheckCompleteDemand(34926, 3001402):
                KillMobAndLoot(402000616)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34926, 3001402, 402000600)
    elif quest13 != 2:
        print("13")
        if quest13 == 0:
            toggle_kami(False)
            StartQuest(34927, 3001401, 402000600)
        elif quest13 == 1:
            if Quest.CheckCompleteDemand(34927, 3001401):
                KillMobAndLoot(402000617)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34927, 3001401, 402000600)
    elif quest14 != 2:
        print("14")
        if quest14 == 0:
            toggle_kami(False)
            StartQuest(34928, 3001400, 402000600)
        elif quest14 == 1:
            toggle_kami(False)
            CompleteQuest(34928, 3001407, 402000615)
    elif quest15 != 2:
        print("15")
        if quest15 == 0:
            toggle_kami(False)
            StartQuest(34929, 3001400, 402000600)       
        elif quest15 == 1:
            toggle_kami(False)
            CompleteQuest(34929, 3001408, 402000620)
    elif quest16 != 2:
        print("16")
        if quest16 == 0:
            toggle_kami(False)
            StartQuest(34930, 3001409, 402000621)
        elif quest16 == 1:
            if Quest.CheckCompleteDemand(34930, 3001409):
                KillMobAndLoot(402000621)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34930, 3001409, 402000621)
    elif quest17 != 2:
        print("17")
        if quest17 == 0:
            toggle_kami(False)
            StartQuest(34931, 3001410, 402000622)
        elif quest17 == 1:
            if Quest.CheckCompleteDemand(34931, 3001410):
                KillMobAndLoot(402000622)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34931, 3001410, 402000622)
    elif quest18 != 2:
        print("18")
        if quest18 == 0:
            toggle_kami(False)
            StartQuest(34932, 3001411, 402000630)
        elif quest18 == 1:
            toggle_kami(False)
            CompleteQuest(34932, 3001412, 402000631)
    elif quest19 != 2:
        print("19")
        if quest19 == 0:
            toggle_kami(False)
            StartQuest(34933, 3001412, 402000631)
        elif quest19 == 1:
            if Quest.CheckCompleteDemand(34933, 3001412):
                KillMobAndLoot(402000631)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34933, 3001412, 402000631)
    elif quest20 != 2:
        print("20")
        if quest20 == 0:
            toggle_kami(False)
            StartQuest(34934, 3001413, 402000633)
        elif quest20 == 1:
            if Quest.CheckCompleteDemand(34934, 3001413):
                KillMobAndLoot(402000633)
                time.sleep(5)
            else:
                toggle_kami(False)
                CompleteQuest(34934, 3001413, 402000633)
    elif quest21 != 2:
        print("21")
        if quest21 == 0:
            toggle_kami(False)
            StartQuest(34935, 3001414, 402000635)
        elif quest21 == 1:
            toggle_kami(False)
            CompleteQuest(34935, 3001416, 402000648)
    elif quest22 != 2:
        print("22")
        if quest22 == 0:
            toggle_kami(False)
            StartQuest(34936, 3001415, 402000648)
            time.sleep(2)
            while Field.GetID() == 402090006:
                Key.Press(0x20)
                Key.Press(0x88)
                print("press")
    elif quest23 != 2:
        print("23")
        if quest23 == 0:
            toggle_kami(False)
            StartQuest(34937, 3001417, 402000644)
        elif quest23 == 1:
            toggle_kami(False)
            CompleteQuest(34937, 3001417, 402000644)
    elif quest24 != 2:
        print("24")
        if quest24 == 0:
            if Field.GetID() == 402000644:
                toggle_kami(False)
                StartQuest(34938, 3001423, 402000644)
            elif Field.GetID() == 940205100:
                toggle_kami(True)
                time.sleep(3)
                EnterPortal("next00")
            elif Field.GetID() == 940205200:
                toggle_kami(True)
                time.sleep(3)
                EnterPortal("next00")
            elif Field.GetID() == 940205300:
                toggle_kami(True)
                time.sleep(3)
                EnterPortal("next00")
    elif quest25 != 2:
        print("25")
        if quest25 == 0:
            toggle_kami(False)
            StartQuest(34902, 0, 402000640)

def ArkSecond():
    quest1 = Quest.GetQuestState(34939)
    quest2 = Quest.GetQuestState(34940)
    if quest1 != 2:
        if quest1 == 0:
            toggle_kami(False)
            StartQuest(34939, 0, 402000640)
        elif quest1 == 1:
            toggle_kami(False)
            CompleteQuest(34939, 0, 402000640)
    elif quest2 != 2:
        if quest2 == 0:
            if Field.GetID() == 402000640:
                toggle_kami(False)
                StartQuest(34940, 0, 402000640)
        elif Field.GetID() == 940205400:
            toggle_kami(True)
            time.sleep(3)
            TakePortal("next00")
        elif Field.GetID() == 940205500:
            toggle_kami(True)
            time.sleep(3)
            TakePortal("next00")
        elif Field.GetID() == 940205600:
            toggle_kami(True)
            time.sleep(3)
            TakePortal("next00")
        elif Field.GetID() == 940205900:
            toggle_kami(True)
            time.sleep(3)
    elif level >= 60:
        jobQuest = Quest.GetQuestState(34903)
        print("Completing Ark Third Job Adv")
        if jobQuest != 2:
            if jobQuest == 0:
                Quest.StartQuest(34903, 0)
                time.sleep(5)
            elif jobQuest == 1:
                Quest.CompleteQuest(34903, 0)
                time.sleep(5)

def ArkFourth():
    jobQuest = Quest.GetQuestState(34904)
    if jobQuest != 2:
        if jobQuest == 0:
            Quest.StartQuest(34904, 0)
            time.sleep(5)
        elif jobQuest == 1:
            Quest.CompleteQuest(34904, 0)
            time.sleep(5)
################################################################
def id2str(jobid):
    if jobid in LuminousJobs:
        return "Luminous"
    elif jobid in DemonAvengerJobs:
        return "Demon Avenger"
    elif jobid in DemonSlayerJobs:
        return "Demon Slayer"
    elif jobid in MercedesJobs:
        return "Mercedes"
    elif jobid in HayatoJobs:
        return "Hayato"
    elif jobid in XenonJobs:
        return "Xenon"
    elif jobid in PhantomJobs:
        return "Phantom"
    elif jobid in ArkJobs:
        return "Ark"
    elif jobid in EvanJobs:
        return "Evan"
    elif jobid in IlliumJobs:
        return "Illium"
    elif jobid in CadenaJobs:
        return "Cadena"
    else:
        return "Unknown Job"



def starItem(pos, currStar, itemMaxStar, userMaxStar, itemid):
   with open('starforceCosts.txt', 'a+') as sfCosts:
       #print('{0} {1}'.format("Position: ".ljust(padding), str(pos)))
       sfCosts.write('{0} {1}\n'.format("Position: ".ljust(padding), str(pos)))
       slotStartingMeso = Character.GetMeso()
       slotStartingStar = currStar
     
       if itemid in whitelist:
           return
       while currStar < userMaxStar and currStar < itemMaxStar and Inventory.GetItem(1, pos).valid:     
           if GameState.IsInGame():
               print("#-----------------------Star-----------------------#")
               print('{0} {1}'.format("Starring From: ".ljust(padding), str(currStar)))
               print('{0} {1}'.format("User Max stars: ".ljust(padding), str(userMaxStar)))
               print('{0} {1}'.format("Item max stars: ".ljust(padding), str(itemMaxStar)))
               print('{0} {1}'.format("Item ID: ".ljust(padding), str(itemid)))
             
               sfCosts.write("\t#-----------------------Star-----------------------#\n")
               sfCosts.write('\t{0} {1}\n'.format("Starring From: ".ljust(padding), str(currStar)))
               sfCosts.write('\t{0} {1}\n'.format("User Max stars: ".ljust(padding), str(userMaxStar)))
               sfCosts.write('\t{0} {1}\n'.format("Item max stars: ".ljust(padding), str(itemMaxStar)))
               sfCosts.write('\t{0} {1}\n'.format("Item ID: ".ljust(padding), str(itemid)))
             
               beforeMeso = Character.GetMeso()
             
               # star the item
               oPacket = Packet.COutPacket(SF_header)
               oPacket.Encode1(0x01)
               oPacket.EncodeBuffer("** ** ** **")
               oPacket.Encode2(toHex(pos, 16))
               oPacket.Encode1(0x00)
               oPacket.Encode4(0x00000001)
               oPacket.Encode4(0xFFFFFFFF)
               if safeguard and currStar in range(12, 17):
                   oPacket.Encode2(0x0101)
                   print("SAFEGUARDING")
                   sfCosts.write('\tSAFEGUARDING\n')
               else:
                   oPacket.Encode2(0x0100)
               Packet.SendPacket(oPacket)
           
               # wait for recv
               iPacket = Packet.WaitForRecv(StarForceRecv, 10000)
           
               if iPacket.GetRemaining() < 140:
                   print("Recv length too short (was: " + str(iPacket.GetRemaining()) + ")")
                   sfCosts.write("\tRecv length too short (was: " + str(iPacket.GetRemaining()) + ")\n")
                   break
                 
               afterMeso = Character.GetMeso()
               iCosted = beforeMeso - afterMeso
               print('{0} {1:,}'.format("Meso Cost of Star: ".ljust(padding), iCosted))
               print('{0} {1}'.format("iPacket remaining: ".ljust(padding), iPacket.GetRemaining()))
             
               sfCosts.write('\t{0} {1:,}\n'.format("Meso Cost of Star: ".ljust(padding), iCosted))
               sfCosts.write('\t{0} {1}\n'.format("iPacket remaining: ".ljust(padding), iPacket.GetRemaining()))

               # remove this line if you want faster stars
               # note: this is used as a delay (for safety, etc), so remove at your own risk
               Packet.WaitForRecv(StarForceRecv, 1000)
             
             
               # update current star counter
               currStar = Inventory.GetItem(1, pos).currentStar

               # get max star again in case item blew up
               # item blown up means itemMaxStar = 0
               itemMaxStar = Inventory.GetItem(1, pos).maxStar
             
       slotEndingMeso = Character.GetMeso()
       slotEndingStar = currStar
       slotTotalCost = slotStartingMeso - slotEndingMeso
       if (slotStartingMeso - slotEndingMeso) != 0:
           print('{0} {1:,} meso from star {2} to {3}\n'.format("Total Cost: ".ljust(padding), slotTotalCost, str(slotStartingStar), str(slotEndingStar)))
           sfCosts.write('{0} {1:,} meso from star {2} to {3}\n\n'.format("Total Cost: ".ljust(padding), slotTotalCost, str(slotStartingStar), str(slotEndingStar)))
       
################# MONSTER PARK
################# MONSTER PARK
################# MONSTER PARK
#57.19% -> 91.23%
def dungeonSelector():
    #charLvl = Character.GetLevel()
    if level in range(115,125):
        return (leopard_portal,mossy_tree_forest)
    elif level in range(125,135):
        return (leopard_portal,secret_pirate)
    elif level in range(135,145):
        return (leopard_portal,other_world)
    elif level in range(145,155):
        return (leopard_portal,forbidden_time)
    elif level in range(155,160):
        return (leopard_portal,clandestine_ruins)
    #return (leopard_portal,mossy_tree_forest)
def rushToMP():
    #field_id = Field.GetID()
    rushToMPFlag = True
    while rushToMPFlag:
        field_id_check = Field.GetID()
        if field_id_check == 100000000:
            Character.Teleport(3133,334)
            Character.TalkToNpc(9071003)
            time.sleep(1)
        else:
            Terminal.Rush(100000000)
            time.sleep(1)
        if field_id_check == 951000000:
            print("Complete rushToMP")
            rushToMPFlag = False

def enterDungeon():
    #field_id = Field.GetID()
    enterDungeonFlag = True
    try_count = 0
    while enterDungeonFlag and try_count < 6:
        try_count += 1
        field_id_check = Field.GetID()
        token = dungeonSelector()
        print("Entering dungeon {}".format(token[1]))
        pos = Character.GetPos()
        if pos.x not in range(token[0][0]-5,token[0][0]+5):
            Character.Teleport(token[0][0],token[0][1])
        time.sleep(1)
        Npc.ClearSelection()
        Character.EnterPortal()
        Npc.RegisterSelection(token[1])
        time.sleep(1)
        if field_id_check != 951000000:
            print("Complete enterDungeon")
            enterDungeonFlag = False
#2
def mapsMP():
    return Field.GetID() >= 952000000 and Field.GetID() <= 954070599

def rush_out_MP():
    rush_out_flag = True
    while rush_out_flag:
        rush_out_field = Field.GetID()
        if rush_out_field == 951000000:
            Character.TalkToNpc(9071003)
        if rush_out_field != 951000000 and not mapsMP():
            rush_out_flag = False
        time.sleep(1)

#Zakum
def ResetNowLockedFunction():
    if NowLockedVar:
        print("Resetting NowLockedVar back to False")
        SCLib.UpdateVar("NowLockedVar", False)
def NowLockedFunction():
    if not NowLockedVar:
        print("Boss Attempt started, Now locked for this boss")
        SCLib.UpdateVar("NowLockedVar", True)
def DidSpawn():
    if not HasSpawned:
        print("Updating HasSpawned to True")
        SCLib.UpdateVar("HasSpawned", True)
def ResetSpawn():
    if HasSpawned:
        print("Resetting HasSpawned back to False")
        SCLib.UpdateVar("HasSpawned", False)
def GetToTheDoorToZakum():
    print("Going to Zakum")
    if field_id != CheifsResidence:
        Terminal.Rush(CheifsResidence)
    else:
        #Ark, Angelic Buster, Cannoneer, Jett, Mechanic, Shade, Thunder Breaker
        Pirates = [15500, 15510, 15511, 15512, 6500, 6510, 6511, 6512, 530, 531, 532, 508, 570, 571, 572, 3500, 3510, 3511, 3512, 2500, 2510, 2511, 2512, 1500, 1510, 1511, 1512]
        #Wild Hunter, Wind Archer, Mercedes
        Bowman = [3300, 3310, 3311, 3312, 1300, 1310, 1311, 1312, 2300, 2310, 2311, 2312]
        #Phantom, Xenon, Dual Blade
        Thief = [2400, 2410, 2411, 2412, 3600, 3610, 3611, 3612, 400, 430, 431, 432, 433, 434]
        #Kanna, Battle Mage, Beast Tamer, Blaze Wizard, Evan, Luminous
        Magician = [4200, 4210, 4211, 4212, 3200, 3210, 3211, 3212, 11000, 11200, 11210, 11211, 11212, 1200, 1210, 1211, 1212, 2200, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2700, 2710, 2711, 2712, ]
        #Aran, Blaster, Demon Avenger, Demon Slayer, Hayato, Kaiser, Mihile, Zero, Dawn Warrior
        Warrior = [3700, 3710, 3711, 3712, 2100, 2110, 2111, 2112, 3101, 3120, 1321, 3122, 3100, 3110, 3111, 3112, 4100, 4110, 4111, 4112, 6100, 6110, 6111, 6112, 5100, 5110, 5111, 5112, 10100, 10110, 10111, 10112, 1100, 1110, 1111, 1112]
        if job in Bowman:
            TalkNPC = NpcReneBowmanInstructor
        elif job in Thief:
            TalkNPC = NpcArecThiefInstructor
        elif job in Magician:
            TalkNPC = NpcRobeiraMagicianInstructor
        elif job in Warrior:
            TalkNPC = NpcTylusWarriorInstructor
        elif job in Pirates:
            TalkNPC = NpcPedroPirateInstructor
        zakjob = [6995, 6996, 6997, 6998, 6999]
        for i in zakjob:
            ZakumCheck = Quest.GetQuestState(i)
            if ZakumCheck == 2:
                ZakumQuest = True
                break
            else:
                ZakumQuest = False
        if ZakumQuest:
            Npc.ClearSelection()
            Npc.RegisterSelection("I want to challenge Zakum.")
            time.sleep(1)
            Character.TalkToNpc(TalkNPC)
            time.sleep(1)
        else:
            Npc.ClearSelection()
            Npc.RegisterSelection("I want to try the Zakum quest.")
            time.sleep(1)
            Character.TalkToNpc(TalkNPC)
            time.sleep(1)

def startupCheck(accountId):
    split_id = accountId.split("@")[0]
    if os.path.exists('info/{}.json'.format(split_id)):
        #print("Loading")
        with open('info/{}.json'.format(split_id)) as f:
            return json.load(f)
    else:
        print("Creating")
        with open('info/{}.json'.format(split_id), "w+") as db_file:
            db_file.write(json.dumps({}))
            return {}

def handleReady(data):
    if 'link_start' not in data:
        data['link_start'] = 0
    if 'link_end' not in data:
        data['link_end'] = 11
    if 'storing_meso' not in data:
        data['storing_meso'] = False
    if 'cur_pos' not in data:
        data['cur_pos'] = Terminal.GetLineEdit("LoginChar")
    if 'changing_mule' not in data:
        data['changing_mule'] = False
    if 'date' not in data:
        data['date'] = str(datetime.datetime.utcnow().date())
    if 'daily_done' not in data:
        data['daily_done'] = False
    if 'phase_one' not in data:
        data['phase_one'] = False
    if 'done_char' not in data:
        data['done_char'] = []
    if 'training_done' not in data:
        data['training_done'] = False
def writeJson(data,accountId):
    split_id = accountId.split("@")[0]
    with open('info/{}.json'.format(split_id), 'w') as outfile:
        parsed = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(parsed)
        outfile.close()

accountId = Terminal.GetLineEdit("LoginID")
accountData = startupCheck(accountId)
handleReady(accountData)
writeJson(accountData,accountId)

current_date = str(datetime.datetime.utcnow().date())
if current_date != accountData['date']:
    accountData['date'] = current_date
    accountData['daily_done'] = False
    writeJson(accountData,accountId)

#7

def reveal_potential(itemPos):
    if Character.GetMeso() > 500000:
        oPacket = Packet.COutPacket(potential_header)
        oPacket.EncodeBuffer("** ** ** 00 7F 00")
        oPacket.Encode2(itemPos)
        Packet.SendPacket(oPacket)
        rPacket = Packet.WaitForRecv(potential_recv,5000)
        print(rPacket)

def reveal_all_potential():
    print("revealing potentials")
    item_list = Inventory.GetItems(1)
    for item in item_list:
        if item.grade > 0 and item.option1 == 0 and GameState.IsInGame():
            #if item.sn not in accountData['equips']:
            #    accountData['equips'].append(item.sn)
            reveal_potential(item.pos)
            time.sleep(0.5)

def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))

######Black gate
def BossCheck():
    print("Waiting for boss to spawn...")
    time.sleep(10)
    for mob in blackgate_boss:
        print("Checking for boss: " + str(mob) + "...")
        while Field.FindMob(mob).valid and GameState.IsInGame():
            print("Boss found: " + str(mob) + ", killing boss...")
            time.sleep(6)
    for item in blackgate_eqp:
        print("Checking for item: " + str(item) + "...")
        while Field.FindItem(item).valid and GameState.IsInGame():
            Terminal.SetCheckBox("Kami Vac",False)
            print("item found with id:" + str(item) + ", waiting until item looted")
            time.sleep(9)
    for mob in blackgate_boss:
        print("Checking for boss: " + str(mob) + "...")
        while Field.FindMob(mob).valid and GameState.IsInGame():
            print("Boss found: " + str(mob) + ", killing boss...")
            time.sleep(6)
    for item in blackgate_eqp:
        print("Checking for item: " + str(item) + "...")
        while Field.FindItem(item).valid and GameState.IsInGame():
            Terminal.SetCheckBox("Kami Vac",False)
            print("item found with id:" + str(item) + ", waiting until item looted")
            time.sleep(9)
    for mob in blackgate_boss:    
        print("Checking for boss: " + str(mob) + "...")
        while Field.FindMob(mob).valid and GameState.IsInGame():
            print("Boss found: " + str(mob) + ", killing boss...")
            time.sleep(6)
    for item in blackgate_eqp:
        print("Checking for item: " + str(item) + "...")
        while Field.FindItem(item).valid and GameState.IsInGame():
            Terminal.SetCheckBox("Kami Vac",False)
            print("item found with id:" + str(item) + ", waiting until item looted")
            time.sleep(9)
    print("no boss found or boss killed")
    time.sleep(2)


def EnterPortal(name):
    time.sleep(0.5)
    portal = Field.FindPortal(name)
    pos = Character.GetPos()
    if pos.x != portal.x:
        print("Portal " + str(name) + " found, teleporting...")
        Character.Teleport(portal.x, portal.y-20)
        time.sleep(0.5)
        print("Teleported to portal: " + str(name)+"...")
    print("Trying to enter portal...")
    while GameState.IsInGame() and Character.GetPos().x == portal.x:
        if Field.GetID() == 610050000:
            break
        Character.EnterPortal()
        time.sleep(0.5)

if job == -1 and not accountData['changing_mule']:
    #print("Not logged in yet")
    Terminal.SetLineEdit("LoginChar",accountData["cur_pos"])
    time.sleep(2)

if accountData['changing_mule'] and GameState.GetLoginStep() == 2:
    Terminal.SetCheckBox("Auto Login",False)
    Terminal.SetLineEdit("LoginChar",str(int(accountData["cur_pos"]) + 1))
    chars = Login.GetChars()
    for char in chars:
        if char.level >= 140:
            accountData["done_char"].append(str(char.id))
    Terminal.SetCheckBox("Auto Login",True)
    accountData["changing_mule"] = False
    accountData["cur_pos"] = str(int(accountData["cur_pos"]) + 1)
    writeJson(accountData,accountId)

if accountData['training_done'] and GameState.GetLoginStep() == 2:
    Terminal.SetCheckBox("Auto Login",False)
    chars = Login.GetChars()
    with open('info/{}.txt'.format(Terminal.GetLineEdit("LoginID")),'w') as charInfo:
        for char in chars:
            charInfo.write("{} {}\n".format(id2str(char.id),char.level))
        charInfo.close()
    Terminal.ChangeStatus("#################Training Done##############")

if len(accountData["done_char"]) == 12 and GameState.IsInGame():
    accountData['training_done'] = True
    Terminal.ChangeStatus("#################Training Done##############")
    writeJson(accountData,accountId)
    Terminal.Logout()


def safety_setting():
    #Turn off dangerous settings
    dangerous_settings = ["Auto Aggro","MonkeySpiritsNDcheck","General FMA","Full Map Attack","Mob Vac","Grenade Kami","Mob Falldown","Vellum Freeze","main/boss_freeze","Full God Mode","Guard God Mode"]
    for settings in dangerous_settings:
        if settings == "General FMA":
            if job not in IlliumJobs:
                Terminal.SetCheckBox(settings, False)
        else:
            Terminal.SetCheckBox(settings, False)

def toggleAttack(on):
    attack_key = 0x44
    pgup_key = 0x21
    if Character.IsOwnFamiliar(9960098):
        Terminal.SetSlider("sliderMP", 90)
    else:
        Terminal.SetSlider("sliderMP", 10)
    if job == 3712:
        Terminal.SetLineEdit("SISkillID","37121003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 4200: #kanna first job
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key, 1, 42001000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4210: #kanna 2nd
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",on)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetSpinBox("SkillInjection", 100)
        Terminal.SetLineEdit("SISkillID","42001006")
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4211 or job ==4212: #kanna 3rd + 4th
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",on)
        Terminal.SetCheckBox("Summon Kishin",True)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Key.Set(0x47,1,42111003)
    elif job == 2700: #lumi first job
        # 20040217 Dark Mode Buff
        # 20040216 Light Mode
        # 20040220 20040219 Equi Mode
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,27001201)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job in LuminousJobs and field_id in curbrockhideout:
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,27001201)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 2710: #lumi second job
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        if Character.HasBuff(2,20040217): #use dark magic
            Key.Set(attack_key,1,27001201)
        else:
            Key.Set(attack_key,1,27101100)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 2711: #lumi third job
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        if Character.HasBuff(2,20040216): #Light Mode
            Key.Set(attack_key,1,27101100)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            Key.Set(attack_key,1,27111303)
        else:                              #Dark Mode
            Key.Set(attack_key,1,27111202)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 2712: #lumi fourth job
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        if Character.HasBuff(2,20040216): #Light Mode
            Key.Set(attack_key,1,27121100)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            Key.Set(attack_key,1,27111303)
        else:                              #Dark Mode
            Key.Set(attack_key,1,27121202)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 3101: #DA first job
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31011000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job in DemonAvengerJobs and field_id in curbrockhideout:
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31011000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 3120: #DA 2nd
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31201000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 3121 or job == 3122: #DA third job and fourth job
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31211000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 3100 or job == 3110 or job == 3111: #DS first - third job
        #Key.Set(attack_key,1,31000004)31001008
        Terminal.SetLineEdit("SISkillID","31001008")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 3112: #DS fourth job
        Terminal.SetLineEdit("SISkillID","31121010")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 2300: #Mercedes 1st 
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,23001000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job in MercedesJobs and field_id in curbrockhideout:
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,23001000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job ==2310: #Mercedes 2nd
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,23101000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job ==2311 or job == 2312: #Mercedes 3rd + 4th
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,23111000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4100: #Hayato 1st 41001004
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","41001004")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job in HayatoJobs and field_id in curbrockhideout:
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","41001004")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 4110: #Hayato 2nd 41101000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","41101000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 4111: #Hayato 3rd 41111011
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","41111011")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 4112: #Hayato 4th 41121011
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","41121011")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 3600:#Xenon 1st 36001000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","36001000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job in XenonJobs and field_id in curbrockhideout:
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","36001000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 3610:#Xenon 2nd 36101000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","36101000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 3611:#Xenon 3rd 36111000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","36111000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 3612:#Xenon 4th 36121000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","36121000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 2400: #Phantom 1st 24001000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","24001000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job in PhantomJobs and field_id in curbrockhideout:
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","24001000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 2410: #Phantom 2nd 24101000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","24101000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 2411: #Phantom 3rd 24111000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","24111000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 2412: #Phantom 4th 24121000
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","24121000")
        Terminal.SetCheckBox("Skill Injection", on)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 15000: #Illium Pre 1st
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 15200 or job == 15210 or job == 15211 or job == 15212: #Illium 1st+2nd+3rd+4th
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",True)
        Terminal.SetCheckBox("General FMA",True)
    elif job == 6400 or job == 6410 or job == 6411: #Cadena 1st + 2nd + 3rd 64001006 or 64001001
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","64001006")
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetRadioButton("SIRadioCadena",True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", on)
    elif job == 6412: # Cadena 4th job 64121016 May want to change this 
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","64121016")
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetRadioButton("SIRadioCadena",True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", on)
    elif job == 15500 or job == 15510 or job == 15511: #Ark 1st + 2nd + 3rd 155001100
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID", "155001100")
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",700)
        Terminal.SetRadioButton("SIRadioMelee",True)
    elif job == 15512: #Ark 4th 155121007 @50
        Terminal.SetLineEdit("SISkillID", "155121007")
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",50)
        Terminal.SetRadioButton("SIRadioMelee",True)
    elif job == 6500: #AB 1st
        Terminal.SetLineEdit("SISkillID","65001100")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMagic",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 6510 or job == 6511: #AB 2nd + 3rd
        Terminal.SetLineEdit("SISkillID","65101100")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMagic",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 6512: #AB 4th
        Terminal.SetLineEdit("SISkillID","65121100")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMagic",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 3512: #mechanic 4th
        #mech_att(on)
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection",False)
    elif job == 2512: #Shade 4th
        Terminal.SetLineEdit("SISkillID","25120003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 11212: #beast tamer 4th
        Terminal.SetLineEdit("SISkillID","112000002")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",200)
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        count = 0
        if on:
            while count < 50 and Field.GetMobCount()>0:
                Key.Down(0x44)
                time.sleep(0.1)
                Key.Up(0x44)
                time.sleep(0.1)
                Key.Press(0x44)
                count += 1
    elif job == 1212: #BW 4th
        Terminal.SetLineEdit("SISkillID","12121055")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 572: #Jett 4th
        Terminal.SetLineEdit("SISkillID","5710020")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 132 or job == 2412: #DK or phantom
        Terminal.SetLineEdit("SISkillID","1311011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 15512: #ark 4th change this to safer method
        Terminal.SetLineEdit("SISkillID","155121007")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",30)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 6412: #Cadena 4th
        Terminal.SetLineEdit("SISkillID","64121011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetRadioButton("bot/si_cadena",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)

    elif job not in KannaJobs:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)

safety_setting()

if GameState.IsInGame():
    toggleAttack(True)
    #print("Toggling attack")

############################Job Advancements###############################
if job == 4200 and level < 13:
    print("Completing Kanna First job")
    kannaFirst()

if job == 4200 and level >= 30:
    print("Completing Kanna Second job")
    second_job_quest = Quest.GetQuestState(57458)
    if second_job_quest == 0:
        Quest.StartQuest(57458, 000000)
    toggle_rush_by_level(True)
    toggle_kami(True)

if job == 2700 and level == 10:
    print("Completing Lumi first job")
    LumiFirst()
    toggle_rush_by_level(True)
    toggle_kami(True)
elif job == 2700 and level == 30:
    print("Completing Lumi second job")
    LumiSecond()
    toggle_rush_by_level(True)
    toggle_kami(True)
elif job ==2710 and level == 60:
    print("Completing Lumi third job")
    LumiThird()
    toggle_rush_by_level(True)
    toggle_kami(True)
    if Quest.GetQuestState(25675) !=2 and Character.GetLevel() >= 60:
        print("Getting Silver Emblem")
        Quest.StartQuest(25675, 1032209)
elif job == 2711 and level ==100:
    print("Completing Lumi fourth job")
    LumiFourth()
    toggle_rush_by_level(True)
    toggle_kami(True)
    if Quest.GetQuestState(25676) !=2 and Character.GetLevel() >= 100:
        print("Getting Gold Emblem")
        Quest.StartQuest(25676, 1032209)
elif (job == 3101 or job ==3100) and level >= 30:
    #print("Completing Demon Avenger first job")
    toggle_rush_by_level(False)
    DAFirst()
elif (job == 3120 or job == 3110) and level >= 60:
    #print("Completing Demon Avenger second job")
    toggle_rush_by_level(False)
    DASecond()
elif (job == 3121 or job == 3111) and field_id == 931050110 and level == 60:
    teleport_enter(111,-14)
    toggle_rush_by_level(True)
    toggle_kami(True)
elif job == 2300 and level <= 13:
    quest = Quest.GetQuestState(29952)
    if quest == 0:
        MercedesFirst()
elif job == 2300 and level >= 30:
    toggle_kami(False)
    MercedesSecond()
elif job == 2310 and field_id == 910150100:
    teleport_enter(9,-250)
    toggle_rush_by_level(True)
    toggle_kami(True)
elif job == 4100 and level <13:
    HayatoFirst()
elif job == 4100 and level >=30:
    print("Completing Hayato Second job")
    second_job_quest = Quest.GetQuestState(57162)
    if second_job_quest == 0:
        Quest.StartQuest(57162, 000000)
    toggle_rush_by_level(True)
    toggle_kami(True)
elif job == 15000:
    print("Completing Illium Pre-First job")
    IlliumZero()
elif job == 15200:
    print("Completing Illium First Job")
    IlliumFirst()
elif job == 15210:
    print("Completing Illium Second Job")
    IlliumSecond()
elif job == 6400:
    print("Completing Cadena First Job and Second Job")
    CadenaFirst()
elif job == 15001:
    if field_id == 402000615:
        Quest.StartQuest(34901, 0)
    print("Starting Ark job")
elif job == 15500:
    print("Completing Ark First Job")
    ArkFirst()
elif job == 15510:
    print("Completing Ark Second Job")
    ArkSecond()
elif job == 15511 and level >= 100:
    print("Completing Ark Fourth Job")
    ArkFourth()
###### lvl 50 hyper rock #######
if Quest.GetQuestState(61589) !=2 and Character.GetLevel() >= 50:
    #print("Getting hyper rock")
    #Npc.ClearSelection()
    #Npc.RegisterSelection("Familiar")
    #Npc.RegisterSelection("Teleport Rock")
    #Npc.RegisterSelection("You get")
    #Quest.StartQuest(61589, 9201253)
    #time.sleep(3)
    Terminal.SetCheckBox("bot/htr",True)
    time.sleep(3)
    Terminal.SetCheckBox("bot/htr",False)
elif Quest.GetQuestState(61589) ==2:
    if Inventory.FindItemByID(2430450).valid:
        print("Using equip box lvl50")
        Inventory.UseItem(2430450)

###### lvl 60 tot ########
if Quest.GetQuestState(61590) !=2 and Character.GetLevel() >= 60:
    print("Getting tot badge")
    Npc.ClearSelection()
    Npc.RegisterSelection("Potential")
    Npc.RegisterSelection("Bonus Potential")
    Npc.RegisterSelection("Cube")
    Npc.RegisterSelection("Soul Weapon")
    Npc.RegisterSelection("gift")
    Quest.StartQuest(61590, 9201253)
    time.sleep(3)
elif Quest.GetQuestState(61590) ==2:
    if Inventory.FindItemByID(2430451).valid:
        print("Using equip box lvl60")
        Inventory.UseItem(2430451)

def getBoogie():
    if Character.IsOwnFamiliar(9960098) == False:
        # sleep 1 second every loop
        time.sleep(1)
        toggle_rush_by_level(False)
        item = Inventory.FindItemByID(2870098)
        drop = Field.FindItem(2870098)
        pos = Character.GetPos()
        if drop.valid:
            Terminal.SetCheckBox("Kami Vac",False)
            toggleAttack(False)
            Terminal.SetCheckBox("Auto Loot",True)
            if pos.x == drop.x and pos.y == drop.y:
                print("Teleported to item location, waiting item to be picked up")
                time.sleep(3)
            else:
                Character.Teleport(drop.x,drop.y)
                print("Teleporting to item location, waiting item to be picked up")
                time.sleep(3)
        if item.valid:
            # use familiar
            Inventory.UseFamiliarCard(2870098)
            toggle_rush_by_level(True)
            time.sleep(1)
            Terminal.SetCheckBox("Kami Vac",True)
            toggleAttack(True)
            if not Terminal.GetCheckBox("Familiar 0"):
                Terminal.SetComboBox("Familiar0",1)
                Terminal.SetCheckBox("Familiar 0",True)
                Terminal.SetCheckBox("Auto Loot",False)
        else:
            if Field.GetID() == 102010000:
                # Perion Southern Ridge
                # let bot kill mobs and pickup?
                toggleAttack(True)
                time.sleep(3)
            elif Terminal.IsRushing():
                time.sleep(3)
            else:
                # rush to the map
                Terminal.Rush(102010000)

if Character.GetLevel() >= 13 and GameState.IsInGame():
    # Jr. Boogie
    if job in IlliumJobs:
        lookback = Quest.GetQuestState(34820)
        if lookback == 2:
            getBoogie()
    elif job in CadenaJobs:
        if job != 6400:
            getBoogie()
    elif job in ArkJobs:
        if job == 15511:
            getBoogie()
    else:
        getBoogie()
    

if Character.GetLevel() >= 83 and GameState.IsInGame():
    # Big Spider
    if Character.IsOwnFamiliar(9960295) == False:
        print("Getting Big Spider")
        toggle_rush_by_level(False)
        # sleep 1 second every loop
        time.sleep(1)
        item = Inventory.FindItemByID(2870295)
        drop = Field.FindItem(2870295)
        pos = Character.GetPos()
        if drop.valid:
            Terminal.SetCheckBox("Kami Vac",False)
            toggleAttack(False)
            Terminal.SetCheckBox("Auto Loot",True)
            if pos.x == drop.x and pos.y == drop.y:
                print("Teleported to item location, waiting item to be picked up")
                time.sleep(3)
            else:
                Character.Teleport(drop.x,drop.y)
                print("Teleporting to item location, waiting item to be picked up")
                time.sleep(3)
        if item.valid:
            # use familiar
            print("Found big spider familiar")
            Inventory.UseFamiliarCard(2870295)
            toggle_rush_by_level(True)
            time.sleep(1)
            Terminal.SetCheckBox("Kami Vac",True)
            toggleAttack(True)
            if not Terminal.GetCheckBox("Familiar 0"):
                Terminal.SetComboBox("Familiar0",2)
                Terminal.SetCheckBox("Familiar 0",True)
                Terminal.SetCheckBox("Auto Loot",False)
        else:
            if Field.GetID() == 310050600:
                # let bot kill mobs and pickup?
                print("Farming for big spider")
                time.sleep(5)
            else:
                # rush to the map
                print("Rushing to Big Spider map")
                if not Terminal.GetCheckBox("map/maprusher/hypertelerock"):
                    Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
                Terminal.Rush(310050600)

#auto star force pensalir gear and accessories
if level >= 60 and star_force and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and Character.GetMeso()>= 5000000:
    #if level >= 140:
    #    for equips in equip_slot_list:
    #        item = Inventory.GetItem(1,equips)
    #        if item.valid and item.currentStar != star_force_level:
    #            #print("Starforcing item {}".format(item.id))
    #            starItem(equips, item.currentStar, item.maxStar, star_force_level, item.id)
    #    for accessories in accessory_slot_list:
    #        item = Inventory.GetItem(1,accessories)
    #        if item.valid and item.id in accessory_list and item.currentStar != star_force_level:
    #            #print("Starforcing item {}".format(item.id))
    #            starItem(accessories, item.currentStar, item.maxStar, star_force_level, item.id)
    for x in range(-100, 0):
        item = Inventory.GetItem(1, x)
        if item.valid and item.currentStar != star_force_level and item.currentStar != item.maxStar:
            starItem(x, item.currentStar, item.maxStar, star_force_level, item.id)

#ZAKUM DAILY
if KillZakumDaily == False and (field_id == TheDoorToZakum or field_id == EntranceToZakumAlter) and not SCLib.GetVar("DoingMP"):
    if field_id == TheDoorToZakum:
        if pos.x != -3003:
            Character.Teleport(-3003, -220)
            time.sleep(0.5)
            Character.EnterPortal()
            SCLib.UpdateVar("DoingZakum",False)
            toggle_rush_by_level(True)
            Terminal.SetCheckBox("Kami Vac",True)
            Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
    elif (field_id == TheDoorToZakum or field_id == EntranceToZakumAlter or field_id == TheCaveOfTrials3Zakum):
        if pos.x != -1599:
            Character.Teleport(-1599, -331)
            time.sleep(0.5)
            Character.EnterPortal()

if KillZakumDaily and level >= 110 and not SCLib.GetVar("DoingMP") and accountData['phase_one']:
    print("Doing Zakum")
    Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
    if Terminal.GetCheckBox("Kami Vac"):
        Terminal.SetCheckBox("Kami Vac",False)
    Terminal.SetComboBox("Familiar0",2)
    toggle_rush_by_level(False)
    Terminal.SetCheckBox('filter_equip',False)
    SCLib.UpdateVar("DoingZakum",True)
    pos = Character.GetPos()
    if field_id not in ZakumsAltar:
        if field_id != EntranceToZakumAlter:
            if field_id != TheDoorToZakum:
                GetToTheDoorToZakum()
            else:
                if pos.x != -720:
                    NewY = pos.y -5
                    Character.Teleport(-720, NewY)
                elif Inventory.GetItemCount(4001017) < 1:
                    Npc.ClearSelection()
                    Npc.RegisterSelection("Receive an offering for Zakum.")
                    time.sleep(1)
                    Npc.RegisterSelection("Normal/Chaos Zakum")
                    Character.TalkToNpc(2030008)
                    time.sleep(1)
                else:
                    print("Entering Portal to EntranceToZakumAlter")
                    Npc.ClearSelection()
                    Npc.RegisterSelection("Normal Zakum")
                    time.sleep(1)
                    Character.EnterPortal()
                    time.sleep(1)
        else:
            if not NowLockedVar:
                if SCLib.GetVar("zakum_retry_count") >= 7:
                    SCLib.UpdateVar("KillZakumDaily",False)
                    ResetNowLockedFunction()
                else:
                    Party.CreateParty()
                    print("Talking to Adobis to enter ZakumsAltar")
                    Character.TalkToNpc(2030013)
                    SCLib.UpdateVar("zakum_retry_count",SCLib.GetVar("zakum_retry_count")+1)
                    time.sleep(1)

            else:
                print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                SCLib.UpdateVar("KillZakumDaily", False)
                ResetNowLockedFunction()
    else:
        print("In zakum altar")
        NowLockedFunction()
        boss2 = Field.FindMob(NormalZakumv2)
        boss1 = Field.FindMob(NormalZakumv1)
        boss = Field.FindMob(NormalZakum)
        if boss.valid or boss1.valid or boss2.valid:
            print("Boss valid")
            DidSpawn()
            if pos.x != -353:
                Character.Teleport(-353, 84)
            else:
                print("Fighting Zakum StandBy")
        else:
            if HasSpawned:
                print("Zakum is dead, waiting 10 sec before continue")
                time.sleep(5)
                face_drop = Field.FindItem(condensed_power_crystal)
                if face_drop.valid:
                    print("Found condensed power crystal")
                    Character.Teleport(face_drop.x,face_drop.y)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(3)
                eye_drop = Field.FindItem(aquatic_letter_eye)
                if eye_drop.valid:
                    print("Found aquatic letter eye")
                    Character.Teleport(eye_drop.x,eye_drop.y)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(3)
                face_check = Field.FindItem(condensed_power_crystal)
                eye_check = Field.FindItem(aquatic_letter_eye)
                time.sleep(5)
                if not face_check.valid and not eye_check.valid:
                    print("Did not find accessory, leaving.")
                    Terminal.SetComboBox("Familiar0",1)
                    Character.TalkToNpc(2030010)
                    time.sleep(1)
                    SCLib.UpdateVar("KillZakumDaily", False)
                    if accountData['cur_pos'] == '11':
                        accountData['daily_done'] = True
                        writeJson(accountData,accountId)
                    ResetSpawn()
                    ResetNowLockedFunction()
                    if field_id == TheDoorToZakum:
                        if pos.x != -3003:
                            Character.Teleport(-3003, -220)
                            time.sleep(1)
                            Character.EnterPortal()
                            SCLib.UpdateVar("DoingZakum",False)
            else:
                print("Finding item in inventory to drop")
                stone = Inventory.FindItemByID(4001017)
                if stone.valid:
                    if pos.x != -25:
                        Character.Teleport(-25, 84)
                    else:
                        print("Dropping stone to spawn Zakum")
                        Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)

if level >= 110 and not accountData['phase_one']:
    if accountData['cur_pos'] == "11": #finished training all link to level 110
        print("Phase one end")
        accountData['phase_one'] = True
        accountData['cur_pos'] = '-1'
        accountData['changing_mule'] = True
        writeJson(accountData,accountId)
        Terminal.Logout()
    else:
        print("Current character done, moving to next one")
        accountData['changing_mule'] = True
        writeJson(accountData,accountId)
        Terminal.Logout()

if accountData['daily_done'] and not SCLib.GetVar("DoingZakum"):
    if accountData['cur_pos'] == "11": #finished doing zakum for every undone links
        print("Daily done")
        accountData['cur_pos'] = '-1'
        accountData['changing_mule'] = True
        writeJson(accountData,accountId)
        Terminal.Logout()
    else:
        print("Current character done Zakum, moving to next one")
        accountData['changing_mule'] = True
        writeJson(accountData,accountId)
        Terminal.Logout()

if level >= 140 and not SCLib.GetVar("DoingZakum"):
    print("Current character done, moving to next one")
    accountData['changing_mule'] = True
    writeJson(accountData,accountId)
    Terminal.Logout()
#####Black gate    

#print(SCLib.GetVar("cube_lock"))
if DoBlackGate and Character.GetHP() > 0 and level >= 145 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    toggle_rush_by_level(False)
    map = Field.GetID()
    channel = GameState.GetChannel()
    print("Blackgate farming")
    SCLib.UpdateVar("DoingBG",True)
    if Terminal.GetCheckBox('filter_equip'):
        Terminal.SetCheckBox('filter_equip',False)
    if not Terminal.GetCheckBox('Kami Loot'):
        Terminal.SetCheckBox('Kami Loot',True)
    if not Terminal.GetCheckBox('Auto Loot'):
        Terminal.SetCheckBox('Auto Loot',True)
    Terminal.SetCheckBox("Kami Vac",True)
    toggleAttack(True)
    Terminal.SetSpinBox("FilterMeso",0)
    if Inventory.GetEmptySlotCount(1) == 0:
        if not Terminal.IsRushing():
            Terminal.Rush(henesys)
    #for item in winter_coupons:
    #    if Character.HasBuff(1, item) == False:
    #        Inventory.UseItem(item)
    #        time.sleep(1)
    if farmed_enough_accessories():
        print("farmed enough accessories")
        SCLib.UpdateVar("DoingBG",False)
    if Terminal.IsRushing():
        print("Rushing... Please wait...")
        #if map == 610050000:
        #    Terminal.StopRush()
        time.sleep(2)
    # IF FOR SOME REASON U END UP IN HENE
    elif map not in blackgate_maps:
        print("Rushing to blackgate")
        Terminal.Rush(610050000)
    # IF AT BDF MAIN MAP
    elif map == 610050000:
        time.sleep(5)
        if channel == 30:
            channel = 1
        else:
            channel += 1
        Terminal.ChangeChannel(channel)
        while Terminal.IsRushing():
            time.sleep(3)
        print("Current channel" + str(GameState.GetChannel()))
        print("Rushing to starting map")
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610050100)
        else:
            print("Still has ring")

    elif map == 610050100:
        print("Arrived in " + str(map) + "...")
        BossCheck()
        # EnterPortal("south00")
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610051500)
        else:
            print("Still has ring")

    elif map == 610051500:
        print("Arrived in " + str(map) + "...")
        BossCheck()
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610050000)
        else:
            print("Still has ring")
        # BACK TO STARTING POINT
curbrock1 = Quest.GetQuestState(5499)
curbrock2 = Quest.GetQuestState(5500)
curbrock3 = Quest.GetQuestState(5501)
sabitrama = 1061005

curbrockescaperoute1 = 600050030
curbrockescaperoute2 = 600050040
curbrockescaperoute3 = 600050050
escaperoutes = [curbrockescaperoute1,curbrockescaperoute2,curbrockescaperoute3]
if GameState.IsInGame() and not Terminal.IsRushing() and level >= 27 and level <= 29 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    pos = Character.GetPos()
    if curbrock1 !=2:
        if curbrock1 ==0:
            toggle_rush_by_level(False)
            Quest.StartQuest(5499, sabitrama)
        elif curbrock1 ==1:
            if Quest.CheckCompleteDemand(5499, sabitrama) ==0:
                if pos.x != -425 and field_id == curbrockhideout:
                    toggle_kami(False)
                    teleport_enter(-425,-195)
                    toggle_kami(True)
                elif pos.x != -549 and field_id == curbrockescaperoute2:
                    toggle_kami(False)
                    teleport_enter(-549,-195)
                    toggle_kami(True)
                    toggle_rush_by_level(True)
                else:
                    Quest.CompleteQuest(5499,sabitrama)
            else:
                toggle_kami(True)
                toggleAttack(True)
if GameState.IsInGame() and not Terminal.IsRushing() and level >= 30 and level < 60 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    pos = Character.GetPos()
    if curbrock2 !=2:
        if curbrock2 ==0:
            toggle_rush_by_level(False)
            Quest.StartQuest(5500, sabitrama)
        elif curbrock2 ==1:
            if Quest.CheckCompleteDemand(5500, sabitrama) ==0:
                if pos.x != -425 and field_id == curbrockhideout:
                    toggle_kami(False)
                    teleport_enter(-425,-195)
                    toggle_kami(True)
                elif pos.x != -549 and field_id == curbrockescaperoute2:
                    toggle_kami(False)
                    teleport_enter(-549,-195)
                    toggle_kami(True)
                    toggle_rush_by_level(True)
                else:
                    Quest.CompleteQuest(5500,sabitrama)
            else:
                toggle_kami(True)
                toggleAttack(True)
if GameState.IsInGame() and not Terminal.IsRushing() and level >= 60 and level < 100 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    pos = Character.GetPos()
    if curbrock3 !=2:
        if curbrock3 ==0:
            toggle_rush_by_level(False)
            Quest.StartQuest(5501, sabitrama)
        elif curbrock3 ==1:
            if Quest.CheckCompleteDemand(5501, sabitrama) ==0:
                if pos.x != -425 and field_id == curbrockhideout:
                    toggle_kami(False)
                    teleport_enter(-425,-195)
                    toggle_kami(True)
                elif pos.x != -549 and field_id == curbrockescaperoute3:
                    toggle_kami(False)
                    teleport_enter(-549,-195)
                    toggle_kami(True)
                    toggle_rush_by_level(True)
                else:
                    Quest.CompleteQuest(5501,sabitrama)
            else:
                toggle_kami(True)
                toggleAttack(True)

if pos.x != -549 and field_id in escaperoutes:
    pos = Character.GetPos()
    toggle_kami(False)
    teleport_enter(-549,-195)
    toggle_kami(True)
    toggle_rush_by_level(True)
    toggleAttack(True)

quest26 = Quest.GetQuestState(2976)
if GameState.IsInGame() and not Terminal.IsRushing() and Character.GetLevel() >= 35 and quest26 !=2 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    time.sleep(1)
    pos = Character.GetPos()
    
    #field_id to Field Name
    BeachGrassDunes1 = (120040100)
    BeachGrassDunes2 = (120040200)
    BeachGrassDunes3 = (120040300)
    GoldBeachResort = (120040000)
    GoldBeachSeaSide1 = (120041000)
    GoldBeachSeaSide2 = (120041100)
    GoldBeachSeaSide3 = (120041200)
    ShallowSea1 = (120041300)
    ShallowSea2 = (120041400)
    ShallowSea3 = (120041500)
    SoftWaveBeach1 = (120041600)
    GentleWaves2 = (120041700)
    HardWaveBeach = (120041800)
    ShadyBeach = (120041900)

    #NPCID to Npc Name
    PilotIrvin = (1082101)
    SwansonBGD2 = (1082201)
    LittleRichieResort = (1082002)
    SwansonResort = (1082000)
    RalphioGBSS2 = (1082202)
    TofuBGSS2 = (1082203)
    SwansonGBSS2 = (1082204)
    RalphioGBSS3 = (1082205)
    SwansonSS1 = (1082206)
    InnerTubeCaddy = (1082005)
    LittleRichieSS2 = (1082207)
    LittleRichieSS3 = (1082208)
    SwansonSS3 = (1082209)
    TofuHWB = (1082210)
    
    #QuestID to Quest Name
    FlyingBlind = (2951)
    AMissionOfGratImportance = (2952)
    FunWithTheSon = (2953)
    GoldenFruit = (2954)
    HouseKeeping = (2955)
    DangerOnTheCoast = (2956)
    LittleTroubleMaker = (2957)
    StatusReport = (2958)
    TheDayTheLightsWentOut = (2959)
    ShineALight = (2960)
    LocalsAndYokels = (2961)
    SubMarineDreams = (2962) 
    PrivateBeach = (2963)
    PutARingOnIt = (2964)
    TheHuntForBlackNovemner = (2965)
    BlackWave = (2966)
    FloatingAway = (2967)
    FreshFlavours = (2968)
    ShrimpySitiuation = (2969)
    TheSadTaleOfLilWilly = (2970)
    FerryFrustrations = (2971)
    TheOriginalSlimeStar = (2972)
    GoingTribal = (2973)
    ChefsSpecial = (2974)
    TerrorFromTheDeep = (2975)
    GoldBeachGoldenOppertunity = (2950)
    
    
    
    #Gets Queststate on Quests
    quest1 = Quest.GetQuestState(FlyingBlind)
    quest2 = Quest.GetQuestState(AMissionOfGratImportance)
    quest3 = Quest.GetQuestState(FunWithTheSon)
    quest4 = Quest.GetQuestState(GoldenFruit)
    quest5 = Quest.GetQuestState(HouseKeeping)
    quest6 = Quest.GetQuestState(DangerOnTheCoast)
    quest7 = Quest.GetQuestState(LittleTroubleMaker)
    quest8 = Quest.GetQuestState(StatusReport)
    quest9 = Quest.GetQuestState(TheDayTheLightsWentOut)
    quest10 = Quest.GetQuestState(ShineALight)
    quest11 = Quest.GetQuestState(LocalsAndYokels)
    quest12 = Quest.GetQuestState(SubMarineDreams)
    quest13 = Quest.GetQuestState(PrivateBeach)
    quest14 = Quest.GetQuestState(PutARingOnIt)
    quest15 = Quest.GetQuestState(TheHuntForBlackNovemner)
    quest16 = Quest.GetQuestState(BlackWave)
    quest17 = Quest.GetQuestState(FloatingAway)
    quest18 = Quest.GetQuestState(FreshFlavours)
    quest19 = Quest.GetQuestState(ShrimpySitiuation)
    quest20 = Quest.GetQuestState(TheSadTaleOfLilWilly)
    quest21 = Quest.GetQuestState(FerryFrustrations)
    quest22 = Quest.GetQuestState(TheOriginalSlimeStar)
    quest23 = Quest.GetQuestState(GoingTribal)
    quest24 = Quest.GetQuestState(ChefsSpecial)
    quest25 = Quest.GetQuestState(TerrorFromTheDeep)
    quest26 = Quest.GetQuestState(2976)
    quest27 = Quest.GetQuestState (GoldBeachGoldenOppertunity)
    
    #Complete quest27 (GoldBeachGoldenOppertunity)
    if quest27 !=2:
        toggle_rush_by_level(False)
        if quest27 ==0:
            toggle_kami(False)
            Quest.StartQuest(GoldBeachGoldenOppertunity, 1082100)
            toggle_kami(True)
    #Complete quest1 (Flying blind)
    elif quest1 !=2:
        if quest1 ==0:
            toggle_kami(False)
            if field_id != BeachGrassDunes3:
                Terminal.Rush(BeachGrassDunes3)
            if pos.x != -822:
                Character.Teleport(-822, -85)
            else:
                Quest.StartQuest(FlyingBlind, PilotIrvin)
        elif quest1 ==1:
            if Quest.CheckCompleteDemand(FlyingBlind, PilotIrvin) ==0:
                toggle_kami(False)
                if field_id != BeachGrassDunes3:
                    Terminal.Rush(BeachGrassDunes3)
                if pos.x != -822:
                    Character.Teleport(-822, -85)
                else:
                    Quest.CompleteQuest(FlyingBlind, PilotIrvin)
            else:
                toggle_kami(True)
                if field_id != BeachGrassDunes3:
                    Terminal.Rush(BeachGrassDunes3)
    #Complete quest2 (A Mission of great importance)
    elif quest2 !=2:
        if quest2 ==0:
            toggle_kami(False)
            if field_id != BeachGrassDunes2:
                Terminal.Rush(BeachGrassDunes2)
            if pos.x != -769:
                Character.Teleport(-769, -85)
            else:
                Quest.StartQuest(AMissionOfGratImportance, SwansonBGD2)
        elif quest2 ==1:
            if Quest.CheckCompleteDemand(AMissionOfGratImportance, LittleRichieResort)==0:
                toggle_kami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -331:
                    Character.Teleport(-331, 116)
                else:
                    Quest.CompleteQuest(AMissionOfGratImportance, LittleRichieResort)
            else:
                toggle_kami(True)
                if field_id != BeachGrassDunes2:
                    Terminal.Rush(BeachGrassDunes2)
    #Complete quest3 (Fun With the son)
    elif quest3 !=2:
        if quest3 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(FunWithTheSon, LittleRichieResort)
        elif quest3 ==1:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(FunWithTheSon, SwansonResort)
    #Complete quest4 (GoldenFruit)
    elif quest4 !=2:
        if quest4 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(GoldenFruit, SwansonResort)
        elif quest4 ==1:
            if Quest.CheckCompleteDemand(GoldenFruit, SwansonResort)==0:
                toggle_kami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -7:
                    Character.Teleport(-7, 116)
                else:
                    Quest.CompleteQuest(GoldenFruit, SwansonResort)
            else:
                toggle_kami(True)
                if field_id != BeachGrassDunes1:
                    Terminal.Rush(BeachGrassDunes1)
    #Complete quest5 (HouseKeeping)
    elif quest5 !=2:
        if quest5 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(HouseKeeping, SwansonResort)
        elif quest5 ==1:
            if Quest.CheckCompleteDemand(HouseKeeping, SwansonResort)==0:
                toggle_kami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -7:
                    Character.Teleport(-7, 116)
                else:
                    Quest.CompleteQuest(HouseKeeping, SwansonResort)
            else:
                toggle_kami(True)
                if field_id != GoldBeachSeaSide1:
                    Terminal.Rush(GoldBeachSeaSide1)
    #Complete quest6 (danger on the coast)
    elif quest6 !=2:
        if quest6 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(DangerOnTheCoast, SwansonResort)
        elif quest6 ==1:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(DangerOnTheCoast, SwansonResort)
    #Complete quest7 (LittleTroubleMaker)
    elif quest7 !=2:
        if quest7 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(LittleTroubleMaker, LittleRichieResort)
        elif quest7 ==1:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(LittleTroubleMaker, SwansonResort)
    #Complete quest8 (StatusReport)
    elif quest8 !=2:
        if quest8 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(StatusReport, SwansonResort)
        elif quest8 ==1:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.CompleteQuest(StatusReport, LittleRichieResort)
    #complete quest9 (TheDayTheLightsWentOut)
    elif quest9 !=2:
        if quest9 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(TheDayTheLightsWentOut, SwansonResort)
        elif quest9 ==1:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -727:
                Character.Teleport(-727, -85)
            else:
                Quest.CompleteQuest(TheDayTheLightsWentOut, RalphioGBSS2)
    #Complete quest10 (ShineALight)
    elif quest10 !=2:
        if quest10 ==0:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -727:
                Character.Teleport(-727, -85)
            else:
                Quest.StartQuest(ShineALight, RalphioGBSS2)
        elif quest10 ==1:
            if Quest.CheckCompleteDemand(ShineALight, RalphioGBSS2)==0:
                toggle_kami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != -727:
                    Character.Teleport(-727, -85)
                else:
                    Quest.CompleteQuest(ShineALight, RalphioGBSS2)
            else:
                toggle_kami(True)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
    #Complete quest11 (LocalsAndYokels)
    elif quest11 !=2:
        if quest11 ==0:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -549:
                Character.Teleport(-549, -85)
            else:
                Quest.StartQuest(LocalsAndYokels, TofuBGSS2)
        elif quest11 ==1:
            if Quest.CheckCompleteDemand(LocalsAndYokels, TofuBGSS2)==0:
                toggle_kami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != -549:
                    Character.Teleport(-549, -85)
                else:
                    Quest.CompleteQuest(LocalsAndYokels, TofuBGSS2)
            else:
                toggle_kami(True)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
    #Complete quest12 (SubMarineDreams)
    elif quest12 !=2:
        if quest12 ==0:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -549:
                Character.Teleport(-549, -85)
            else:
                Quest.StartQuest(SubMarineDreams, TofuBGSS2)
                time.sleep(5)
        elif quest12 ==1:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -549:
                Character.Teleport(-549, -85)
            else:
                Quest.CompleteQuest(SubMarineDreams, TofuBGSS2)
    #Complete quest13 (PrivateBeach)
    elif quest13 !=2:
        if quest13 ==0:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -408:
                Character.Teleport(-408, -25)
            else:
                Quest.StartQuest(PrivateBeach, SwansonGBSS2)
        elif quest13 ==1:
            if Quest.CheckCompleteDemand(PrivateBeach, SwansonGBSS2)==0:
                toggle_kami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != -408:
                    Character.Teleport(-408, -25)
                else:
                    Quest.CompleteQuest(PrivateBeach, SwansonGBSS2)
            else:
                toggle_kami(True)
                if field_id != GoldBeachSeaSide3:
                    Terminal.Rush(GoldBeachSeaSide3)
    #Complete quest14 (PutARingOnIt)
    elif quest14 !=2:
        if quest14 ==0:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide3:
                Terminal.Rush(GoldBeachSeaSide3)
            if pos.x != 825:
                Character.Teleport(825, -205)
            else:
                Quest.StartQuest(PutARingOnIt, RalphioGBSS3)
        elif quest14 ==1:
            if Quest.CheckCompleteDemand(PutARingOnIt, RalphioGBSS3)==0:
                toggle_kami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != 825:
                    Character.Teleport(825, -205)
                else:
                    Quest.CompleteQuest(PutARingOnIt, RalphioGBSS3)
            else:
                toggle_kami(True)
                if field_id != GoldBeachSeaSide3:
                    Terminal.Rush(GoldBeachSeaSide3)
    #Complete quest15 (TheHuntForBlackNovemner)
    elif quest15 !=2:
        if quest15 ==0:
            toggle_kami(False)
            if field_id != GoldBeachSeaSide3:
                Terminal.Rush(GoldBeachSeaSide3)
            if pos.x != 825:
                Character.Teleport(825, -205)
            else:
                Quest.StartQuest(TheHuntForBlackNovemner, RalphioGBSS3)
        elif quest15 ==1:
            toggle_kami(False)
            if field_id != ShallowSea1:
                Terminal.Rush(ShallowSea1)
            if pos.x != -168:
                Character.Teleport(-168, -325)
            else:
                Quest.CompleteQuest(TheHuntForBlackNovemner, SwansonSS1)
    #Complete quest16 (BlackWave)
    elif quest16 !=2:
        if quest16 ==0:
            toggle_kami(False)
            if field_id != ShallowSea1:
                Terminal.Rush(ShallowSea1)
            if pos.x != -168:
                Character.Teleport(-168, -325)
            else:
                Quest.StartQuest(BlackWave, SwansonSS1)
        elif quest16 ==1:
            if Quest.CheckCompleteDemand(BlackWave, SwansonResort)==0:
                toggle_kami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -7:
                    Character.Teleport(-7, 116)
                else:
                    Quest.CompleteQuest(BlackWave, SwansonResort)
            else:
                toggle_kami(True)
                if field_id != ShallowSea1:
                    Terminal.Rush(ShallowSea1)
    #Complete quest17 (FloatingAway)
    elif quest17 !=2:
        if quest17 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(FloatingAway, SwansonResort)
        elif quest17 ==1:
            if Quest.CheckCompleteDemand(FloatingAway, InnerTubeCaddy)==0:
                toggle_kami(False)
                if field_id != ShallowSea2:
                    Terminal.Rush(ShallowSea2)
                elif pos.x != -627:
                    Character.Teleport(-627, 116)
                else:
                    Quest.CompleteQuest(FloatingAway, InnerTubeCaddy)
            else:
                toggle_kami(True)
                if field_id != ShallowSea2 and Inventory.FindItemByID(4000759).count < 30:
                    Terminal.Rush(ShallowSea2)
                elif Inventory.FindItemByID(4000759).count >= 30:
                    Terminal.Rush(ShallowSea1)
    #Complete quest18 (FreshFlavours)
    elif quest18 !=2:
        if quest18 ==0:
            toggle_kami(False)
            if field_id != ShallowSea2:
                Terminal.Rush(ShallowSea2)
            if pos.x != -352:
                Character.Teleport(-352, -145)
            else:
                Quest.StartQuest(FreshFlavours, LittleRichieSS2)
        elif quest18 ==1:
            if Quest.CheckCompleteDemand(FreshFlavours, LittleRichieSS3)==0:
                toggle_kami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -1131:
                    Character.Teleport(-1131, -325)
                else:
                    Quest.CompleteQuest(FreshFlavours, LittleRichieSS3)
            else:
                toggle_kami(True)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
    #COmplete quest 19 (ShrimpySitiuation)
    elif quest19 !=2:
        if quest19 ==0:
            toggle_kami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -1131:
                Character.Teleport(-1131, -325)
            else:
                Quest.StartQuest(ShrimpySitiuation, LittleRichieSS3)
        elif quest19 ==1:
            if Quest.CheckCompleteDemand(ShrimpySitiuation, LittleRichieSS3)==0:
                toggle_kami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -1131:
                    Character.Teleport(-1131, -325)
                else:
                    Quest.CompleteQuest(ShrimpySitiuation, LittleRichieSS3)
            else:
                toggle_kami(True)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
    #COmplete quest20 (TheSadTaleOfLilWilly)
    elif quest20 !=2:
        if quest20 ==0:
            toggle_kami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -637:
                Character.Teleport(-637, 116)
            else:
                Quest.StartQuest(TheSadTaleOfLilWilly, SwansonSS3)
        elif quest20 ==1:
            if Quest.CheckCompleteDemand(TheSadTaleOfLilWilly, SwansonSS3)==0:
                toggle_kami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -637:
                    Character.Teleport(-637, 116)
                else:
                    Quest.CompleteQuest(TheSadTaleOfLilWilly, SwansonSS3)
            else:
                toggle_kami(True)
                if field_id != SoftWaveBeach1:
                    Terminal.Rush(SoftWaveBeach1)
    #Complete quest21 (FerryFrustrations)
    elif quest21 !=2:
        if quest21 ==0:
            toggle_kami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -637:
                Character.Teleport(-637, 116)
            else:
                Quest.StartQuest(FerryFrustrations, SwansonSS3)
        elif quest21 ==1:
            if Quest.CheckCompleteDemand(FerryFrustrations, SwansonSS3)==0:
                toggle_kami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -637:
                    Character.Teleport(-637, 116)
                else:
                    Quest.CompleteQuest(FerryFrustrations, SwansonSS3)
            else:
                toggle_kami(True)
                Terminal.Rush(GentleWaves2)
                time.sleep(30)
                Terminal.Rush(HardWaveBeach)
                time.sleep(30)
    #Complete quest22 (TheOriginalSlimeStar)
    elif quest22 !=2:
        if quest22 ==0:
            toggle_kami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -637:
                Character.Teleport(-637, 116)
            else:
                Quest.StartQuest(TheOriginalSlimeStar, SwansonSS3)
        elif quest22 ==1:
            toggle_kami(False)
            if field_id != HardWaveBeach:
                Terminal.Rush(HardWaveBeach)
            if pos.x != -211:
                Character.Teleport(-211, -145)
            else:
                Quest.CompleteQuest(TheOriginalSlimeStar, TofuHWB)
    #Complete quest23 (GoingTribal)
    elif quest23 !=2:
        if quest23 ==0:
            toggle_kami(False)
            if field_id != HardWaveBeach:
                Terminal.Rush(HardWaveBeach)
            if pos.x != -211:
                Character.Teleport(-211, -145)
            else:
                Quest.StartQuest(GoingTribal, TofuHWB)
        elif quest23 ==1:
            if Quest.CheckCompleteDemand(GoingTribal, TofuHWB)==0:
                toggle_kami(False)
                if field_id != HardWaveBeach:
                    Terminal.Rush(HardWaveBeach)
                if pos.x != -211:
                    Character.Teleport(-211, -145)
                else:
                    Quest.CompleteQuest(GoingTribal, TofuHWB)
            else:
                toggle_kami(True)
                if field_id != HardWaveBeach:
                    Terminal.Rush(HardWaveBeach)
    #Complete quest24 (ChefsSpecial)
    elif quest24 !=2:
        if quest24 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(ChefsSpecial, SwansonResort)
        elif quest24 ==1:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(ChefsSpecial, SwansonResort)
    #Complete quest 25 (TerrorFromTheDeep)
    elif quest25 !=2:
        print("quest 25")
        if Party.IsInParty():
            Party.LeaveParty()
        if quest25 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(TerrorFromTheDeep, LittleRichieResort)
        elif quest25 ==1:
            if Quest.CheckCompleteDemand(TerrorFromTheDeep, LittleRichieResort)==0:
                time.sleep(2)
                toggle_kami(False)
                if field_id in range(ShadyBeach,ShadyBeach+20):
                    Character.Teleport(381, 125)
                    time.sleep(1)
                    Character.EnterPortal()
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -331:
                    Character.Teleport(-331, 116)
                else:
                    Quest.CompleteQuest(TerrorFromTheDeep, LittleRichieResort)
            else:
                if field_id not in range(ShadyBeach,ShadyBeach+20):
                    Terminal.Rush(HardWaveBeach)
                    toggle_kami(False)
                    if pos.x != 797:
                        Character.Teleport(797, -385)
                    else:
                        toggleAttack(False)
                        time.sleep(2)
                        Character.EnterPortal()
                        toggleAttack(True)
                else:
                    toggle_kami(True)
    #Complete quest 26 for beachbum medal
    elif quest26 !=2:
        print("quest 26")
        if quest26 ==0:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(2976, LittleRichieResort)
        elif quest25 ==1:
            toggle_kami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.CompleteQuest(2976, LittleRichieResort)
                time.sleep(2)
                Inventory.SendChangeSlotPositionRequest(1,Inventory.FindItemByID(1032254).pos,earring_slot,-1)
                time.sleep(2)
                toggle_rush_by_level(True)
                toggle_kami(True)
    #All quest for Gold Beach Complete!
elif quest26 == 2 and Inventory.FindItemByID(1032254).valid:
    print("Equiping earring and enabling rush by level")
    time.sleep(2)
    Inventory.SendChangeSlotPositionRequest(1,Inventory.FindItemByID(1032254).pos,earring_slot,-1)
    time.sleep(2)
    toggle_rush_by_level(True)
    toggle_kami(True)
elif quest26 == 2 and field_id == GoldBeachResort:
    toggle_rush_by_level(True)
    toggle_kami(True)
    print("Just in case stuck in gold beach, return control to rush by level")
quest17 = Quest.GetQuestState(2054)
if GameState.IsInGame() and not Terminal.IsRushing() and level >= 65 and level < 90 and quest17!=2:
    #print("Doing")
    toggle_rush_by_level(False)
    time.sleep(1)
    pos = Character.GetPos()
    #NPC ID TO NPC NAME

    Ilji = (1061019)
    Gwin = (1061013)
    Ronnie = (1061004)
    TheNote = (1063014)
    MuYoung = (1061014)
    TristansSpirit = (1061015)
    InsignificantBeing = (1061012)
    John = (20000)
    ChunJi = (1061020)
    Chrisharama =(1061000)
    #MAPID TO MAPNAME

    SleepyWood = (105000000)
    SilentSwamp = (105010000)
    HumidSwamp = (105010100)
    SunlessArea = (105020000)
    CaveCliff = (105020100)
    ColdWind = (105020200)
    ChillyCave = (105020300)
    CaveExit = (105020400)
    AnotherDoor = (105030000)
    TempleEntrance = (105030100)
    CollapsedTemple = (105030200)
    EndlessHallway = (105030300)
    GloomyTemple = (105030400)
    ForbiddenAltar = (105030500)
    BottomoftheTemple = (105100100)
    HerosMemory = (910520000)

    #QUESTID TO QUEST NAME
    DrakeAttack1 = (2581)
    DrakeAttack2 = (2582)
    DrakeAttack3 = (2583)
    DrakeAttack4 = (2584)
    DrakeAttack5 = (2585)
    InjuredAdventurer = (2265)
    InjuredAdventurer2 = (2266)
    InjuredAdventurer3 = (2267)
    InjuredAdventurer4 = (2268)
    RonniesMarble = (2586)
    MysteriousNote = (2237)
    MysteriousNote2 = (2238)
    ASpellThatSealsUpACriticalDanger = (2096)
    ASpellThatSealsUpACriticalDanger2 = (2097)
    ForestOfTenacity1 = (2052)
    ForestOfTenacity2 = (2053)
    ForestOfTenacity3 = (2054)
    HerosGladius = (2047)
    HerosGladiusChis = (2048)

    quest1 = Quest.GetQuestState(DrakeAttack1)
    quest2 = Quest.GetQuestState(DrakeAttack2)
    quest3 = Quest.GetQuestState(DrakeAttack3)
    quest4 = Quest.GetQuestState(DrakeAttack4)
    quest5 = Quest.GetQuestState(DrakeAttack5)
    quest6 = Quest.GetQuestState(InjuredAdventurer)
    quest7 = Quest.GetQuestState(InjuredAdventurer2)
    quest8 = Quest.GetQuestState(InjuredAdventurer3)
    quest9 = Quest.GetQuestState(InjuredAdventurer4)
    quest10 = Quest.GetQuestState(RonniesMarble)
    quest11 = Quest.GetQuestState(MysteriousNote)
    quest12 = Quest.GetQuestState(MysteriousNote2)
    quest13 = Quest.GetQuestState(ASpellThatSealsUpACriticalDanger)
    quest14 = Quest.GetQuestState(ASpellThatSealsUpACriticalDanger2)
    quest15 = Quest.GetQuestState(ForestOfTenacity1)
    quest16 = Quest.GetQuestState(ForestOfTenacity2)
    quest17 = Quest.GetQuestState(ForestOfTenacity3)
    
    #Complete quest1 (DrakeAttack1)
    if quest1 != 2:
        if quest1 ==0:
            acceptQuest(DrakeAttack1, Ilji, SleepyWood, field_id)
        elif quest1 ==1:
            completeQuest(DrakeAttack1, Ilji, SleepyWood, HumidSwamp, field_id)
        elif quest1 ==1:
            Terminal.Rush(SleepyWood)
    #complete quest2 (DrakeAttack2)
    elif quest2 != 2:
        if quest2 ==0:
            acceptQuest(DrakeAttack2, Ilji, SleepyWood, field_id)
        elif quest2 ==1:
            completeQuest(DrakeAttack2, Ilji, SleepyWood, SunlessArea, field_id)
    #complete quest3 (DrakeAttack3)
    elif quest3 != 2:
        if quest3 ==0:
            acceptQuest(DrakeAttack3, Ilji, SleepyWood, field_id)
        elif quest3 ==1:
            completeQuest(DrakeAttack3, Ilji, SleepyWood, CaveCliff, field_id)
    #complete quest4 (DrakeAttack4)
    elif quest4 != 2:
        if quest4 ==0:
            acceptQuest(DrakeAttack4, Ilji, SleepyWood, field_id)
        elif quest4 ==1:
            completeQuest(DrakeAttack4, Ilji, SleepyWood, ChillyCave, field_id)
    #complete quest5 (DrakeAttack5)
    elif quest5 != 2:
        if quest5 ==0:
            acceptQuest(DrakeAttack5, Ilji, SleepyWood, field_id)
        elif quest5 ==1:
            completeQuest(DrakeAttack5, Ilji, SleepyWood, CaveExit, field_id)
    #complete quest6 (InjuredAdventurer)
    elif quest6 != 2:
        if quest6 ==0:
            acceptQuest(InjuredAdventurer, Ilji, SleepyWood, field_id)
        elif quest6 ==1:
            completeQuest(InjuredAdventurer, Gwin, AnotherDoor, SleepyWood, field_id)
    #complete quest7 (InjuredAdventurer2)
    elif quest7 != 2:
        toggle_HTR(False)
        if quest7 ==0:
            acceptQuest(InjuredAdventurer2, Gwin, AnotherDoor, field_id)
        elif quest7 ==1:
            completeQuest(InjuredAdventurer2, Gwin, AnotherDoor, TempleEntrance, field_id)
    #complete quest8 (InjuredAdventurer3)
    elif quest8 != 2:
        toggle_HTR(False)
        if quest8 ==0:
            acceptQuest(InjuredAdventurer3, Gwin, AnotherDoor, field_id)
        elif quest8 ==1:
            completeQuest(InjuredAdventurer3, Gwin, AnotherDoor, CollapsedTemple, field_id)
    #complete quest9 (InjuredAdventurer4)
    elif quest9 != 2:
        toggle_HTR(True)
        if quest9 ==0:
            acceptQuest(InjuredAdventurer4, Gwin, AnotherDoor, field_id)
        elif quest9 ==1:
            if pos.x != -542:
                Character.Teleport(-525, 1028)
                time.sleep(1)
                Character.EnterPortal()
                time.sleep(1)
                completeQuest(InjuredAdventurer4, Ilji, SleepyWood, SleepyWood, field_id)
    #complete quyest10 (RonniesMarble)
    elif quest10 != 2:
        if quest10 ==0:
            acceptQuest(RonniesMarble, Ronnie, SilentSwamp, field_id)
        elif quest10 ==1:
            completeQuest(RonniesMarble, Ronnie, SilentSwamp, SunlessArea, field_id)
    #complete quest11 (MysteriousNote)
    elif quest11 != 2:
        toggle_HTR(False)
        if quest11 ==0:
            acceptQuest(MysteriousNote, TheNote, SunlessArea, field_id)
        elif quest11 ==1:
            completeQuest(MysteriousNote, MuYoung, BottomoftheTemple, BottomoftheTemple, field_id)
    #complete quest12 (Mysteriousnote2)
    elif quest12 != 2:
        if quest12 ==0:
            toggle_kami(False)
            acceptQuest(MysteriousNote2, MuYoung, BottomoftheTemple, field_id)
        elif quest12 ==1:
            Character.TalkToNpc(TristansSpirit)
            toggle_kami(True)
            completeQuest(MysteriousNote2, TristansSpirit, HerosMemory, HerosMemory, field_id)
    #complete quest13 (ASpellThatSealsUpACriticalDanger)
    elif quest13 !=2:
        toggle_HTR(False)
        if field_id == HerosMemory:
            if pos.x != -343:
                toggle_kami(False)
                Character.Teleport(-343, 190)
            else:
                Character.EnterPortal()
        elif quest13 ==0:
            acceptQuest(ASpellThatSealsUpACriticalDanger, InsignificantBeing, AnotherDoor, field_id)
        elif quest13 ==1:
            completeQuest(ASpellThatSealsUpACriticalDanger, InsignificantBeing, AnotherDoor, ChillyCave, field_id)
    #complete quest14 (ASpellThatSealsUpACriticalDanger2)
    elif quest14 !=2: 
        toggle_HTR(False)
        if quest14 ==0:
            acceptQuest(ASpellThatSealsUpACriticalDanger2, InsignificantBeing, AnotherDoor, field_id)
        elif quest14 ==1:
            if Quest.CheckCompleteDemand(ASpellThatSealsUpACriticalDanger2, InsignificantBeing) ==0:
                completeQuest(ASpellThatSealsUpACriticalDanger2, InsignificantBeing, AnotherDoor, AnotherDoor, field_id)
            else:
                toggle_kami(True)
                if Inventory.GetItemCount(4031213) < 10:
                    if field_id != TempleEntrance:
                        Terminal.Rush(TempleEntrance)
                elif Inventory.GetItemCount(4031214) < 10:
                    if field_id != CollapsedTemple:
                        Terminal.Rush(CollapsedTemple)
                elif Inventory.GetItemCount(4031215) < 10:
                    if field_id != ForbiddenAltar:
                        Terminal.Rush(ForbiddenAltar)
    #complete quest15 (ForestOfTenacity1)
    elif quest15 !=2:
        #print("here")
        if field_id == AnotherDoor:
            if pos.x != -523:
                Character.Teleport(-523, 1028)
                time.sleep(1)
            Character.EnterPortal()
            time.sleep(1)
        if quest15 ==0:
            #print("trying to accept quest")
            if field_id == BottomoftheTemple or field_id == 105100000:
                toggle_HTR(False)
                rush(AnotherDoor)
                time.sleep(2)
            toggle_HTR(True)
            acceptQuest(ForestOfTenacity1, John, SleepyWood, field_id)
        elif quest15 ==1:
            if Quest.CheckCompleteDemand(ForestOfTenacity1, John)==0:
                completeQuest(ForestOfTenacity1, John, SleepyWood,SleepyWood, field_id)
            else:
                if field_id != 910530001:
                    if field_id != 910530000:
                        if field_id != SleepyWood:
                            Terminal.Rush(SleepyWood)
                        if pos.x != 1038:
                            Character.Teleport(1038, 255)
                            time.sleep(3)
                            Character.TalkToNpc(1061006)
                            time.sleep(2)
                    elif field_id == 910530000:
                        if pos.x != -75:
                            Character.Teleport(-75, -2685)
                        else:
                            Character.EnterPortal()
                if field_id == 910530001:
                    if pos.x != 762:
                        Character.Teleport(762, -2325)
                    else:
                        Character.TalkToNpc(1063000)
    #complete quest16 (ForestOfTenacity2)
    elif quest16 != 2:
        if quest16 ==0:
            acceptQuest(ForestOfTenacity2, John, SleepyWood, field_id)
        if quest16 ==1:
            if Quest.CheckCompleteDemand(ForestOfTenacity2, John) ==0:
                completeQuest(ForestOfTenacity2, John, SleepyWood,SleepyWood, field_id)
            else:
                if field_id != 910530101:
                    if field_id != 910530100:
                        if field_id != SleepyWood:
                            Terminal.Rush(SleepyWood)
                        if pos.x != 887:
                            Character.Teleport(887, 255)
                        else:
                            Character.TalkToNpc(1061006)
                    if field_id == 910530100:
                        if pos.x != 1259:
                            Character.Teleport(1259, -2565)
                            time.sleep(1)
                        else:
                            Character.EnterPortal()
                if field_id == 910530101:
                    if pos.x != -434:
                        Character.Teleport(-434, -1935)
                        time.sleep(1)
                    else:
                        Character.TalkToNpc(1063001)
    #complete quest17 (ForestOfTenacity3)
    elif quest17 != 2:
        if quest17 ==0:
            acceptQuest(ForestOfTenacity3, John, SleepyWood, field_id)
        elif quest17 ==1:
            if Quest.CheckCompleteDemand(ForestOfTenacity3, John)==0:
                completeQuest(ForestOfTenacity3, John, SleepyWood, SleepyWood, field_id)
                if quest17 == 2:
                    toggle_HTR(True)
                    toggle_rush_by_level(True)
                    toggle_kami(True)
            else:
                if field_id != 910530202:
                    if field_id != 910530201:
                        if field_id != 910530200:
                            if field_id != SleepyWood:
                                Terminal.Rush(SleepyWood)
                            if pos.x != 887:
                                Character.Teleport(887, 255)
                                time.sleep(2)
                            else:
                                Character.TalkToNpc(1061006)
                                time.sleep(2)
                        if field_id == 910530200:
                            if pos.x != 1523:
                                Character.Teleport(1523, -1905)
                                time.sleep(1)
                            else:
                                Character.EnterPortal()
                                time.sleep(1)
                    if field_id == 910530201:
                        if pos.x != 255:
                            Character.Teleport(255, -1545)
                            time.sleep(1)
                        else:
                            Character.EnterPortal()
                            time.sleep(1)
                if field_id == 910530202:
                    if pos.x != 1009:
                        Character.Teleport(1009, -3345)
                        time.sleep(1)
                    else:
                        Character.TalkToNpc(1063002)
                        time.sleep(1)