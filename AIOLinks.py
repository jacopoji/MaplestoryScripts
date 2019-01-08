'''
Links skills
TODO:
Kanna           DONE
Luminous        DONE
Demon Avenger   
Demon Slayer    
Mercedes        
Hayato          
Xenon           
Phantom         
Illium          
Cadena          
Ark             
Evan            
'''

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
import Character,Context,DataType,Field,Inventory,Key,Npc,Packet,Quest,Terminal,time,GameState,sys,os,Party,json,math,Login,datetime

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

def teleport_enter(x,y):
    Character.Teleport(x,y)
    time.sleep(1)
    Character.EnterPortal()
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
            StartQuest(23210, 2151000)
        elif Quest.CheckCompleteDemand(23210, 2151000) != 0:
            #need to fight the cat
            if field_id != 931050100:
                if field_id != 310020100:
                    Terminal.Rush(310020100)
                else:
                    teleport_enter(515,-14)
            else:
                Terminal.SetCheckBox("Kami Vac",True)
                toggleAttack(True)
        elif Quest.CheckCompleteDemand(23210, 2153006) == 0:
            print("Done fighting")
            Quest.CompleteQuest(23210, 2153006)
    elif Quest.GetQuestState(23211) !=2:
        if Quest.GetQuestState(23210) == 0:
            StartQuest(23211, 2153006)
        elif Quest.CheckCompleteDemand(23211, 2153006) == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection("Move ")
            Quest.CompleteQuest(23211, 2153006)
    elif Quest.GetQuestState(23212) !=2:
        print("third quest")
        if Quest.GetQuestState(23212) == 0:
            StartQuest(23212, 2151009)
        elif Quest.GetQuestState(23212) == 1:
            if field_id == 931050100:
                teleport_enter(111,-14)
            elif field_id != 310010000:
                Terminal.Rush(310010000)
            else:
                Quest.CompleteQuest(23212, 2151009)
                toggle_rush_by_level(True)
                Terminal.SetCheckBox("Kami Vac",True)
            
############################################
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
    ''' 
    if charLvl in range(115,125):
        return (leopard_portal,mossy_tree_forest)
    elif charLvl in range(125,135):
        return (leopard_portal,secret_pirate)
    elif charLvl in range(135,145):
        return (leopard_portal,other_world)
    elif charLvl in range(145,155):
        return (leopard_portal,forbidden_time)
    elif charLvl in range(155,160):
        return (leopard_portal,clandestine_ruins)
    '''
    return (leopard_portal,mossy_tree_forest)
def rushToMP():
    #fieldid = Field.GetID()
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
    #fieldid = Field.GetID()
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
            #	accountData['equips'].append(item.sn)
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
    with open('{}.txt'.format(Terminal.GetLineEdit("LoginID")),'w') as charInfo:
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
        Terminal.SetCheckBox(settings, False)

def toggleAttack(on):
    attack_key = 0x44
    pgup_key = 0x21
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
    elif job == 3101:
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31011000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
    elif job == 3120:
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31201000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
    elif job == 3121:
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31211000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", on)
    elif job == 3112:
        Terminal.SetLineEdit("SISkillID","31121010")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 6500:
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
    elif job == 6510 or job == 6511:
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
    elif job == 6512:
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
    elif job == 3512:
        mech_att(on)
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection",False)
    elif job == 2512:
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
    elif job == 4112:
        Terminal.SetLineEdit("SISkillID","41121011")
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
    elif job == 11212: #beast tamer
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
    elif job == 15212:
        Terminal.SetLineEdit("SISkillID","152121041")
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
    elif job == 1212:
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
    elif job == 572:
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
    elif job == 15512: #ark
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
    elif job == 6412: #Cadena
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
        if on:
            if not Terminal.GetCheckBox("Auto Attack"):
                print("Toggle Skill Injection "+str(on))
                Terminal.SetCheckBox("Auto Attack", on)
        else:
            if Terminal.GetCheckBox("Auto Attack"):
                print("Toggle Skill Injection "+str(on))
                Terminal.SetCheckBox("Auto Attack", on)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
    '''
    elif job == 3612: #xenon
        Terminal.SetLineEdit("SISkillID","36121000")
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
    '''

safety_setting()

if GameState.IsInGame():
    toggleAttack(True)

############################Job Advancements###############################
if job == 4200 and level < 13:
    print("Completing Kanna First job")
    kannaFirst()

if job == 4200 and level >= 30:
    print("Completing Kanna Second job")
    second_job_quest = Quest.GetQuestState(57458)
    if second_job_quest == 0:
        Quest.StartQuest(57458, 000000)

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
elif job == 3101 and level >= 30:
    print("Completing Demon Avenger first job")
    toggle_rush_by_level(False)
    DAFirst()


###### lvl 50 hyper rock #######
if Quest.GetQuestState(61589) !=2 and Character.GetLevel() >= 50:
    print("Getting hyper rock")
    Npc.ClearSelection()
    Npc.RegisterSelection("Familiar")
    Npc.RegisterSelection("Teleport Rock")
    Npc.RegisterSelection("You get")
    Quest.StartQuest(61589, 9201253)
    time.sleep(3)
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

if Character.GetLevel() >= 13 and GameState.IsInGame():
    # Jr. Boogie
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
if level >= 60 and star_force and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and Character.GetMeso()>= 5000000 and not SCLib.GetVar("cube_lock"):
    if level >= 140:
        for equips in equip_slot_list:
            item = Inventory.GetItem(1,equips)
            if item.valid and item.currentStar != star_force_level:
                #print("Starforcing item {}".format(item.id))
                starItem(equips, item.currentStar, item.maxStar, star_force_level, item.id)
        for accessories in accessory_slot_list:
            item = Inventory.GetItem(1,accessories)
            if item.valid and item.id in accessory_list and item.currentStar != star_force_level:
                #print("Starforcing item {}".format(item.id))
                starItem(accessories, item.currentStar, item.maxStar, star_force_level, item.id)
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

if KillZakumDaily and level >= 110 and not SCLib.GetVar("DoingMP") and not accountData["cubing_done"] and accountData['phase_one']:
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

#####Black gate	

#print(SCLib.GetVar("cube_lock"))
if DoBlackGate and not SCLib.GetVar("cube_lock") and SCLib.GetVar("checked_equip") and Character.GetHP() > 0 and level >= 145 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("GettingEarring") and not SCLib.GetVar("GettingLep"):
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