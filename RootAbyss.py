import Field, Character, Terminal, time, Quest, GameState, Inventory, Party, Packet,sys,os,Key,json, Login,Npc

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")

start_char_number = 0
return_char = 7
usingkami		=		True
usingHyperTeleportRock= True
HotKey = 0x78

CrimsonQueenNormal	=	True
PierreNormal	=		True
VonBonNormal	=		True
VellumNormal	=		True
###CrimsonQueen###
CrimsonQueenNormalBuffer = ["[150E0000]", "[180E0000]", "[130E0000]", "[170E0000]", "[1B0E0000]", "[240E0000]", "[280E0000]"]
#150E0000 180E0000 130E0000 170E0000 1B0E0000 240E0000 280E0000
CrimsonQueenNormalRebootBuffer = ["[FA0D0000]", "[0C0E0000]", "[0F0E0000]", "[070E0000]", "[FC0D0000]","[F60D0000]","[000E0000]","[040E0000]","[1C0E0000]","[200E0000]","[140E0000]"]
#FA0D0000 0C0E0000 0F0E0000 070E0000 FC0D0000

CrimsonQueenChaosBuffer = ["[2B110000]", "[45110000]"]
#2B110000 1F110000 45110000
CrimsonQueenChaosRebootBuffer = ["[FA0D0000]", "[1F110000]", "[30110000]"]
#FA0D0000 1F110000 30110000

###Von Bon###
VonBonNormalBuffer = ["[8E0C0000]", "[8C0C0000]", "[990C0000]", "[9D0C0000]"]
#8E0C0000 8C0C0000 990C0000 9D0C0000
VonBonNormalRebootBuffer =  ["[830C0000]", "[850C0000]", "[880C0000]", "[800C0000]", "[750C0000]","[6F0C0000]","[820C0000]","[8F0C0000]","[950C0000]","[A20C0000]","[AF0C0000]","[8D0C0000]","[9A0C0000]"]
#830C0000 850C0000 880C0000 800C0000 750C0000

VonBonChaosBuffer = ["[250F0000]", "[2F0F0000]"]
#250F0000 2F0F0000
VonbonChaosRebootBuffer = ["[730C0000]", "[090F0000]", "[120F0000]"]
#730C0000 090F0000 120F0000

###Vellum###
VellumNormalBuffer = ["[650E0000]", "[630E0000]", "[670E0000]", "[740E0000]"]
#650E0000 630E0000 670E0000 740E0000
VellumNormalRebootBuffer = ["[5A0E0000]", "[5C0E0000]", "[5F0E0000]", "[570E0000]", "[4C0E0000]","[460E0000]","[500E0000]","[540E0000]","[670E0000]","[700E0000]","[6C0E0000]","[780E0000]","[640E0000]",'[680E0000]']
#5A0E0000 5C0E0000 5F0E0000 570E0000 4C0E0000

VellumChaosBuffer = ["[DD110000]", "[FE110000]"]
#DD110000 FE110000
VellumChaosRebootBuffer = ["[4A0E0000]", "[DC110000]", "[E1110000]"]
#4A0E0000 DC110000 E1110000

###Packet Headers###
InteractHeader = 0x03F0
EnterBossHeader = 0x00EC
BlockBuyHeader = 0x0635
BuyItemHeader = 0x00EF
mech_header = 0x0147

key_quest = 30027
key_quest_npc = 1064031
eye_slot = -3
face_slot = -2
aquatic_letter_eye = 1022231
condensed_power_crystal = 1012478

queen_reactor = 1058018
vonbon_reactor = 1058016
vellum_reactor = 1058020
def doZakum():
    return Inventory.GetItem(1, -3).id == aquatic_letter_eye and Inventory.GetItem(1,-2).id == condensed_power_crystal

DoZakumDaily= not doZakum()

SCLib.PersistVar("HasSpawned", False)
SCLib.PersistVar("NowLockedVar", False)
charm_fma = Terminal.GetCheckBox("charm_fma")
MonkeySpiritsNDcheck = Terminal.GetCheckBox("MonkeySpiritsNDcheck")
Summon_Kishin = Terminal.GetCheckBox("Summon Kishin")
SCLib.PersistVar("MonkeySpiritsNDcheck", MonkeySpiritsNDcheck)
SCLib.PersistVar("charm_fma", charm_fma)
SCLib.PersistVar("Summon_Kishin", Summon_Kishin)
if SCLib.GetVar("KillCrimsonQueen") is None:
    SCLib.PersistVar("KillCrimsonQueen", True)
if SCLib.GetVar("KillPierre") is None:
    SCLib.PersistVar("KillPierre", True)
if SCLib.GetVar("KillVonBon") is None:
    SCLib.PersistVar("KillVonBon", True)
if SCLib.GetVar("KillVellum") is None:
    SCLib.PersistVar("KillVellum", True)
if SCLib.GetVar("DoneAll") is None:
    SCLib.PersistVar("DoneAll", False)
if SCLib.GetVar("TimeOut") is None:
    SCLib.PersistVar("TimeOut",0)
if SCLib.GetVar("RetryCount") is None:
    SCLib.PersistVar("RetryCount",0)
if SCLib.GetVar("KillZakumDaily") is None:
	SCLib.PersistVar("KillZakumDaily", DoZakumDaily)
if SCLib.GetVar("zakum_retry_count") is None:
	SCLib.PersistVar("zakum_retry_count",0)
if SCLib.GetVar("enter_cs") is None:
    if int(Terminal.GetLineEdit("LoginChar")) % 2 == 0:
    	SCLib.PersistVar("enter_cs",True)
    else:
        SCLib.PersistVar("enter_cs",False)
SCLib.StartVars(100)
HasSpawned = SCLib.GetVar("HasSpawned")
NowLockedVar = SCLib.GetVar("NowLockedVar")

enter_cs = SCLib.GetVar("enter_cs")
KillCrimsonQueen = SCLib.GetVar("KillCrimsonQueen")
KillPierre = SCLib.GetVar("KillPierre")
KillVonBon = SCLib.GetVar("KillVonBon")
KillVellum = SCLib.GetVar("KillVellum")
KillZakumDaily = SCLib.GetVar("KillZakumDaily")
def KillPersistVarThred():
    print("Stopping vars")
    SCLib.StopVars()
    time.sleep(1)
SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F9
NormalVonBon = 8910100
NormalPierre = 8900100
NormalPierrev2 = 8900102
NormalPierrev3 = 8900101
NormalVellum = 8930100
NormalCrimsonQueen3 = 8920100
NormalCrimsonQueen2 = 8920101
NormalCrimsonQueen1 = 8920103
NormalCrimsonQueen = 8920102
CurrentChannel = GameState.GetChannel()
pos = Character.GetPos()
fieldID = Field.GetID()
job = Character.GetJob()
level = Character.GetLevel()
KannaJobs = [4200, 4210, 4211, 4212]
mech_jobs = [3510,3511,3512]
aquatic_letter_eye = 1022231
condensed_power_crystal = 1012478
queen_portal = 1064014
pierre_portal = 1064012
vonbon_portal = 1064013
vellum_portal = 1064015

#map ids
CheifsResidence = 211000001
TheDoorToZakum = 211042300
EntranceToZakumAlter = 211042400
ZakumsAltar = [280030100,280030101,280030102,280030103,280030104]
TheCaveOfTrials3Zakum = 211042200

#npc ids
NpcRobeiraMagicianInstructor = 2020009
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


def GetToTheDoorToZakum():
		toggleKami(False)
		toggleHyperTeleportRock(True)
		print("Going to Zakum")
		if fieldID != CheifsResidence:
			Terminal.Rush(CheifsResidence)
		else:
			#Ark, Angelic Buster, Cannoneer, Jett, Mechanic, Shade, Thunder Breaker
			Pirates = [15500, 15510, 15511, 15512, 6500, 6510, 6511, 6512, 530, 531, 532, 508, 570, 571, 572, 3500, 3510, 3511, 3512, 2500, 2510, 2511, 2512, 1500, 1510, 1511, 1512]
			#Wild Hunter, Wind Archer, Mercedes
			Bowman = [3300, 3310, 3311, 3312, 1300, 1310, 1311, 1312, 2300, 2310, 2311, 2312]
			#Phantom, Xenon, Dual Blade
			Thief = [2400, 2410, 2411, 2412, 3600, 3610, 3611, 3612, 400, 430, 431, 432, 433, 434,6410,6411,6412,1412]
			#Kanna, Battle Mage, Beast Tamer, Blaze Wizard, Evan, Luminous
			Magician = [15212,4200, 4210, 4211, 4212, 3200, 3210, 3211, 3212, 11000, 11200, 11210, 11211, 11212, 1200, 1210, 1211, 1212, 2200, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2700, 2710, 2711, 2712, ]
			#Aran, Blaster, Demon Avenger, Demon Slayer, Hayato, Kaiser, Mihile, Zero, Dawn Warrior
			Warrior = [3700, 3710, 3711, 3712, 2100, 2110, 2111, 2112, 3101, 3120, 1321, 3122, 3100, 3110, 3111, 3112, 4100, 4110, 4111, 4112, 6100, 6110, 6111, 6112, 5100, 5110, 5111, 5112, 10100, 10110, 10111, 10112, 1100, 1110, 1111, 1112,132]
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
				toggleHyperTeleportRock(False)

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
def writeJson(data,accountId):
    split_id = accountId.split("@")[0]
    with open('info/{}.json'.format(split_id), 'w') as outfile:
        parsed = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(parsed)
        outfile.close()
def handleReady(data):
    if 'mule_number' not in data:
        data['mule_number'] = start_char_number
    if 'orig_char' not in data:
        data['orig_char'] = Terminal.GetLineEdit("LoginChar")
    elif str(data['orig_char']) != str(return_char):
        data['orig_char'] = str(return_char)

def InteractCrimsonQueenNormal():
    print("Sending Intreact Packet")
    for x in CrimsonQueenNormalBuffer:
        Interact = Packet.COutPacket(InteractHeader)
        Interact.EncodeBuffer(x)
        Packet.SendPacket(Interact)
    for x in CrimsonQueenNormalRebootBuffer:
        InteractReboot = Packet.COutPacket(InteractHeader)
        InteractReboot.EncodeBuffer(x)
        Packet.SendPacket(InteractReboot)
def InteractVonBonNormal():
    print("Sending Interact Packet")
    for x in VonBonNormalRebootBuffer:
        InteractReboot = Packet.COutPacket(InteractHeader)
        InteractReboot.EncodeBuffer(x)
        Packet.SendPacket(InteractReboot)
def InteractVellumNormal():
    print("Sending Interact Packet")
    for x in VellumNormalBuffer:
        Interact = Packet.COutPacket(InteractHeader)
        Interact.EncodeBuffer(x)
        Packet.SendPacket(Interact)
    for x in VellumNormalRebootBuffer:
        InteractReboot = Packet.COutPacket(InteractHeader)
        InteractReboot.EncodeBuffer(x)
        Packet.SendPacket(InteractReboot)
def EnterNormalBossPacket():
    print("Sending EnterNormal Packet")
    time.sleep(1)
    Enter = Packet.COutPacket(EnterBossHeader)
    Enter.EncodeBuffer("[0601] 00000000")
    Packet.SendPacket(Enter)

def enter_boss(boss_portal_id):
    time.sleep(1)
    Npc.ClearSelection()
    time.sleep(0.5)
    Npc.RegisterSelection("Use")
    time.sleep(0.5)
    Character.TalkToNpc(boss_portal_id)

def CheckCompleteStepAndDeliver(questid, questnpc):
    if Quest.CheckCompleteDemand(questid, questnpc) ==0:
        print("Delivering quest {0} at questnpc {1}".format(questid, questnpc))
        Quest.CompleteQuest(questid, questnpc)
        time.sleep(0.5)

def BuyGnarledWoodenKey():
    q12 = 30013
    if Quest.GetQuestState(q12) == 2:
        Quest.StartQuest(key_quest,key_quest_npc)
        time.sleep(3)
        if Inventory.GetItemCount(4033611) < 1:
            if Character.GetMeso() > 100000:
                Character.TalkToNpc(1064004)
                time.sleep(0.5)
                print("Buying key via packet")
                Packet.BlockRecvHeader(BlockBuyHeader)
                time.sleep(0.5)
                BuyKey = Packet.COutPacket(BuyItemHeader)
                BuyKey.EncodeBuffer("00 0000 003D8C4B 0001 00000000 000186A0")
                Packet.SendPacket(BuyKey)
                time.sleep(0.5)
                CloseShop = Packet.COutPacket(BuyItemHeader)
                CloseShop.EncodeBuffer("[03]")
                Packet.SendPacket(CloseShop)
                time.sleep(0.5)
                Packet.UnBlockRecvHeader(BlockBuyHeader)
            else:
                print("Not enough mesos")
                time.sleep(3)
    else:
        if Character.GetMeso() > 100000:
            Character.TalkToNpc(1064004)
            time.sleep(0.5)
            print("Buying key via packet")
            Packet.BlockRecvHeader(BlockBuyHeader)
            time.sleep(0.5)
            BuyKey = Packet.COutPacket(BuyItemHeader)
            BuyKey.EncodeBuffer("00 0000 003D8C4B 0001 00000000 000186A0")
            Packet.SendPacket(BuyKey)
            time.sleep(0.5)
            CloseShop = Packet.COutPacket(BuyItemHeader)
            CloseShop.EncodeBuffer("[03]")
            Packet.SendPacket(CloseShop)
            time.sleep(0.5)
            Packet.UnBlockRecvHeader(BlockBuyHeader)
        else:
            print("Not enough mesos")
            time.sleep(3)
def CloseShopWindowPacket():
    Packet.BlockRecvHeader(BlockBuyHeader)
    time.sleep(0.5)
    CloseShop = Packet.COutPacket(BuyItemHeader)
    CloseShop.EncodeBuffer("[03]")
    Packet.SendPacket(CloseShop)
    time.sleep(0.5)
    Packet.UnBlockRecvHeader(BlockBuyHeader)


def mapID(id):
    if Field.GetID() == id:
        print("Current map ID: {0}".format(Field.GetID()))
    else:
        print("We are not on map ID: {0}".format(id))
    return Field.GetID() == id

def rush(mapid):
    if not Terminal.IsRushing():
        print("Rushing to map ID: {0}".format(mapid))
        Terminal.Rush(mapid)
        time.sleep(2)
    else:
        print("We are currently rushing. Standby...")
        time.sleep(1)

def mech_att(on):
    count = 0
    if not Terminal.IsRushing() and job in mech_jobs and Field.GetMobCount()>0 and on:
        while count < 30 and Field.GetMobCount()>0:
            time.sleep(0.2)
            oPacket = Packet.COutPacket(mech_header)
            oPacket.Encode4(int(time.monotonic()*1000))
            oPacket.Encode4(0x0217994A)#skill ID
            oPacket.Encode1(0x01)#skill level
            oPacket.EncodeBuffer("00")
            oPacket.Encode4(0x00000000)
            oPacket.Encode1(0x0F)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode2(0x0000)
            oPacket.Encode1(0x00)
            Packet.SendPacket(oPacket)
            count += 1
def ab_att():
    count = 0
    if not Terminal.IsRushing() and job in mech_jobs and Field.GetMobCount()>0 and on:
        while count < 30 and Field.GetMobCount()>0:
            time.sleep(0.2)
            oPacket = Packet.COutPacket(0x0147)
            oPacket.Encode4(int(time.monotonic()*1000))
            oPacket.Encode4(0x03E1843C)#skill ID
            oPacket.Encode1(0x14)#skill level
            oPacket.EncodeBuffer("00")
            oPacket.Encode4(0x00000000)
            oPacket.Encode2(0xFE34)
            oPacket.Encode2(0x0039)
            oPacket.Encode1(0x02)
            oPacket.Encode4(0x00000000)
            oPacket.Encode4(0x00000000)
            oPacket.Encode2(0x021C)
            oPacket.Encode1(0x00)
            Packet.SendPacket(oPacket)
            count += 1

def tele(x, y):
    print("Teleporting to {0}, {1}".format(x, y))
    Character.Teleport(x, y)
    time.sleep(1)

def goThru(x, y):
    Terminal.SetCheckBox("Auto Attack", False)
    Character.Teleport(x, y)
    time.sleep(0.5)
    Character.EnterPortal()
    time.sleep(0.15)

def startQuest(quest, npc):
    print("Starting quest {0} from npc {1}".format(quest, npc))
    Quest.StartQuest(quest, npc)
    time.sleep(1)

def completeQuest(quest, npc):
    print("Completing quest {0} from npc {1}".format(quest, npc))
    Quest.StartQuest(quest, npc)
    time.sleep(1)

def needQuest(id):  # quest hasn't been accepted
    return Quest.GetQuestState(id) == 0

def hasQuest(id):  # quest is active
    return Quest.GetQuestState(id) == 1

def doQuest(id):  # quest isn't complete/turned in
    return Quest.GetQuestState(id) != 2

def toggleKami(on):
    if usingkami:
        if on:
            if not Terminal.GetCheckBox("Kami Vac"):
                print("Toggle Kami Vac "+str(on))
                Terminal.SetCheckBox("Kami Vac", on)
        else:
            if Terminal.GetCheckBox("Kami Vac"):
                print("Toggle Kami Vac "+str(on))
                Terminal.SetCheckBox("Kami Vac", on)
    else:
        if Terminal.GetCheckBox("Kami Vac") == True:
            print("Toggle Kami Vac False")
            Terminal.SetCheckBox("Kami Vac", False)

def toggleHyperTeleportRock(on):
    if usingHyperTeleportRock:
        if on:
            if not Terminal.GetCheckBox("map/maprusher/hypertelerock"):
                print("Toggle Hyper Teleport Rock "+str(on))
                Terminal.SetCheckBox("map/maprusher/hypertelerock", on)
        else:
            if Terminal.GetCheckBox("map/maprusher/hypertelerock"):
                print("Toggle Hyper Teleport Rock "+str(on))
                Terminal.SetCheckBox("map/maprusher/hypertelerock", on)
    else:
        if Terminal.GetCheckBox("map/maprusher/hypertelerock") == True:
            print("Toggle Hyper Teleport Rock False")
            Terminal.SetCheckBox("map/maprusher/hypertelerock", False)
def toggleFaceLeft(on):
    if on:
        if not Terminal.GetCheckBox("flacc"):
            print("Toggle FaceLeft "+str(on))
            Terminal.SetCheckBox("flacc", on)
    else:
        if Terminal.GetCheckBox("flacc"):
            print("Toggle FaceLeft "+str(on))
            Terminal.SetCheckBox("flacc", on)
def toggleSI(on):
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
    elif job == 6512:
        Terminal.SetLineEdit("SISkillID","65121008")
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
    if job not in KannaJobs:
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
def toggleGodMode(on):
    if on:
        if not Terminal.GetCheckBox("Full God Mode"):
            print("Toggle FullGodMode "+str(on))
            Terminal.SetCheckBox("Full God Mode", on)
    else:
        if Terminal.GetCheckBox("Full God Mode"):
            print("Toggle FullGodMode "+str(on))
            Terminal.SetCheckBox("Full God Mode", on)
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
        print("Boss Has Spawned Good luck!")
        SCLib.UpdateVar("HasSpawned", True)
def ResetSpawn():
    if HasSpawned:
        print("Resetting HasSpawned back to False")
        SCLib.UpdateVar("HasSpawned", False)
def toggleNoBossMapEffect(on):
    if on:
        if not Terminal.GetCheckBox("No Boss Map Effect"):
            print("Toggle No Boss Map Effect "+str(on))
            Terminal.SetCheckBox("No Boss Map Effect", on)
    else:
        if Terminal.GetCheckBox("No Boss Map Effect"):
            print("Toggle No Boss Map Effect "+str(on))
            Terminal.SetCheckBox("No Boss Map Effect", on)


def TimeOutCount():
    SCLib.UpdateVar("TimeOut",SCLib.GetVar("TimeOut") + 1)
def TimeOutReset():
    SCLib.UpdateVar("TimeOut",0)
def TimedOut():
    return SCLib.GetVar("TimeOut") >= 10
def RetryCountAdd():
    SCLib.UpdateVar("RetryCount",SCLib.GetVar("RetryCount")+1)
def RetryCountReset():
    SCLib.UpdateVar("RetryCount",0)
def RetryCountReached():
    return SCLib.GetVar("RetryCount") >= 3

def GotoRootAbyss():
    toggleKami(False)
    if not Terminal.IsRushing():
        if fieldID != ColossalRoot:
            Terminal.Rush(ColossalRoot)
            time.sleep(3)
        else:
            toggleHyperTeleportRock(False)
    
def togglebossfreeze(on):
    if on:
        if not Terminal.GetCheckBox("main/boss_freeze"):
            print("Toggle Boss Freeze "+str(on))
            Terminal.SetCheckBox("main/boss_freeze", on)
    else:
        if Terminal.GetCheckBox("main/boss_freeze"):
            print("Toggle Boss Freeze "+str(on))
            Terminal.SetCheckBox("main/boss_freeze", on)
def KannaSkills(on):
    if job in KannaJobs:
        Terminal.SetCheckBox("Auto Attack",False)
        if SCLib.GetVar("Summon_Kishin"):
            Terminal.SetCheckBox("Summon Kishin", on)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
        Terminal.SetCheckBox("charm_fma", on)
        Terminal.SetCheckBox("Grenade Kami",False)
        Terminal.SetSpinBox("MonkeySpiritsNDdelay",0)
def vonbon():
    print("Doing Von Bon")
    toggleKami(False)
    if CurrentChannel != 20:
        print("Change to Channel 20")
        Terminal.ChangeChannel(20)
    else:
        if fieldID not in TerporalCrevasseNormal:
            if fieldID not in EastGardenNormal:
                if fieldID != ColossalRoot:
                    GotoRootAbyss()
                else:
                    if Inventory.GetItemCount(4033611) < 1:
                        print("Missing Gnarled Wooden Key, Buying one before continue")
                        BuyGnarledWoodenKey()
                    else:
                        Party.CreateParty()
                        enter_boss(vonbon_portal)
            else:
                if not NowLockedVar:
                    mob = Field.FindMob(7120110)
                    if mob.valid:
                        toggleKami(True)
                        toggleSI(True)
                        KannaSkills(True)
                        togglebossfreeze(False)
                        print("Killing Blazing Imps")
                    else:
                        toggleSI(False)
                        toggleKami(False)
                        KannaSkills(False)
                        if pos.x != 3352:
                            Character.Teleport(3352, 155)
                        else:
                            Character.EnterPortal()
                else:
                    print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                    SCLib.UpdateVar("KillVonBon", False)
                    ResetNowLockedFunction()
        else:
            NowLockedFunction()
            boss = Field.FindMob(NormalVonBon)
            if boss.valid:
                toggleSI(True)
                toggleKami(True)
                KannaSkills(True)
                toggleNoBossMapEffect(True)
                togglebossfreeze(True)
                DidSpawn()
                print("Killing boss Standby")
            else:
                if HasSpawned:
                    toggleKami(False)
                    print("VonBon is dead, Waiting 5 sec before continue")
                    Terminal.SetCheckBox("Kami Loot",True)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(5)
                    Terminal.SetCheckBox("Kami Loot",False)
                    Terminal.SetCheckBox("Auto Loot",False)
                    if pos.x != -1090:
                        Character.Teleport(-1090, 453)
                    else:
                        time.sleep(1)
                        Character.EnterPortal()
                        time.sleep(0.5)
                        Character.EnterPortal()
                        time.sleep(1)
                        SCLib.UpdateVar("KillVonBon", False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                        TimeOutReset()
                else:
                    find = Field.FindReactor(vonbon_reactor)
                    if TimedOut() and not find.valid:
                        if pos.x != -1090:
                            Character.Teleport(-1090, 453)
                        else:
                            time.sleep(1)
                            Character.EnterPortal()
                            time.sleep(0.5)
                            Character.EnterPortal()
                        ResetSpawn()
                        ResetNowLockedFunction()
                        TimeOutReset()
                    else:
                        InteractVonBonNormal()
                        toggleSI(False)
                        KannaSkills(False)
def pierre():
    toggleKami(False)
    if CurrentChannel != 20:
        print("Change to Channel 20")
        Terminal.ChangeChannel(20)
    else:
        if fieldID not in AfternoonTeaTableNormal:
            if fieldID not in WestGardenNormal:
                if fieldID != ColossalRoot:
                    GotoRootAbyss()
                else:
                    if Inventory.GetItemCount(4033611) < 1:
                        print("Missing Gnarled Wooden Key, Buying one before continue")
                        BuyGnarledWoodenKey()
                    else:
                        Party.CreateParty()
                        enter_boss(pierre_portal)
            else:
                if not NowLockedVar:
                    mob = Field.FindMob(7120110)
                    if mob.valid:
                        toggleKami(True)
                        toggleSI(True)
                        KannaSkills(True)
                        togglebossfreeze(False)
                        print("Still some more Blazing imp to kill")
                    else:
                        print("Imps are dead")
                        toggleSI(False)
                        KannaSkills(False)
                        toggleKami(False)
                        if pos.x != 2407:
                            print("Moving into position to enter portal")
                            Character.Teleport(2407, 100)
                        else:
                            print("Entering portal")
                            Character.EnterPortal()
                else:
                    print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                    SCLib.UpdateVar("KillPierre", False)
                    ResetNowLockedFunction()
        else:
            NowLockedFunction()
            boss1 = Field.FindMob(NormalPierre)
            boss2 = Field.FindMob(NormalPierrev2)
            boss3 = Field.FindMob(NormalPierrev3)
            if boss1.valid or boss2.valid or boss3.valid:
                toggleSI(True)
                toggleKami(True)
                KannaSkills(True)
                toggleNoBossMapEffect(True)
                togglebossfreeze(True)
                print("Killing Pierre, standby")
            else:
                print("chest?")
                toggleKami(False)
                chest = Field.FindMob(8900103)
                newX = chest.x -50
                TimeOutCount()
                if chest.valid:
                    print("Attacking Chest to get loot")
                    DidSpawn()
                    if pos.x != newX:
                        Character.Teleport(newX, 550)
                    else:
                        toggleSI(False)
                        Character.BasicAttack()
                        Terminal.SetCheckBox("Kami Loot",True)
                        Terminal.SetCheckBox("Auto Loot",True)
                        time.sleep(7)
                        Terminal.SetCheckBox("Kami Loot",False)
                        Terminal.SetCheckBox("Auto Loot",False)
                else:
                    if HasSpawned or TimedOut():
                        print("PierreNormal and chest has been killed waiting 5 sec before continue")
                        Terminal.SetCheckBox("Kami Loot",True)
                        Terminal.SetCheckBox("Auto Loot",True)
                        time.sleep(5)
                        Terminal.SetCheckBox("Kami Loot",False)
                        Terminal.SetCheckBox("Auto Loot",False)
                        if pos.x != -382:
                            print("Moving into position to enter portal")
                            Character.Teleport(-382, 550)
                        else:
                            print("Entering portal")
                            time.sleep(1)
                            Character.EnterPortal()
                            time.sleep(0.5)
                            Character.EnterPortal()
                            time.sleep(0.5)
                            Character.EnterPortal()
                            time.sleep(0.5)
                            Character.EnterPortal()
                            time.sleep(2)
                            SCLib.UpdateVar("KillPierre", False)
                            ResetSpawn()
                            ResetNowLockedFunction()
                            TimeOutReset()
                    else:
                        KannaSkills(False)
                        toggleSI(False)

def crimsonqueen():
    toggleKami(False)
    if CurrentChannel != 20:
        print("Change to Channel 20")
        Terminal.ChangeChannel(20)
    else:
        if fieldID not in QueensCastleNormal:
            if fieldID not in SouthGardenNormal:
                if fieldID != ColossalRoot:
                    GotoRootAbyss()
                else:
                    if Inventory.GetItemCount(4033611) < 1:
                        print("Missing Gnarled Wooden Key, Buying one before continue")
                        BuyGnarledWoodenKey()
                    else:
                        Party.CreateParty()
                        enter_boss(queen_portal)
            else:
                if not NowLockedVar:
                    mob = Field.FindMob(7120110)
                    if mob.valid:
                        toggleKami(True)
                        KannaSkills(True)
                        toggleSI(True)
                        togglebossfreeze(False)
                        print("Need to kill some more Blazing Imps to enter next room")
                    else:
                        toggleSI(False)
                        toggleKami(False)
                        KannaSkills(False)
                        print("Imps are dead")
                        if pos.x != 1835:
                            print("Moving into position to enter portal")
                            Character.Teleport(1835, 259)
                        else:
                            print("Entering Portal")
                            Character.EnterPortal()
                else:
                    print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                    SCLib.UpdateVar("KillCrimsonQueen", False)
                    ResetNowLockedFunction()
        else:
            NowLockedFunction()
            boss = Field.FindMob(NormalCrimsonQueen)
            boss1 = Field.FindMob(NormalCrimsonQueen1)
            boss2 = Field.FindMob(NormalCrimsonQueen2)
            boss3 = Field.FindMob(NormalCrimsonQueen3)
            if boss.valid or boss1.valid or boss2.valid or boss3.valid:
                toggleSI(True)
                KannaSkills(True)
                toggleNoBossMapEffect(True)
                togglebossfreeze(True)
                toggleKami(True)
                print("Fighting boss standby")
            else:	
                chest = Field.FindMob(8920106)
                newX = chest.x -30
                TimeOutCount()
                if chest.valid:
                    DidSpawn()
                    print("Attacking chest to get the loot")
                    if pos.x != newX:
                        Character.Teleport(newX, 130)
                    else:
                        toggleSI(False)
                        Character.BasicAttack()
                        Terminal.SetCheckBox("Kami Loot",True)
                        Terminal.SetCheckBox("Auto Loot",True)
                        time.sleep(5)
                        Terminal.SetCheckBox("Kami Loot",False)
                        Terminal.SetCheckBox("Auto Loot",False)
                else:
                    if HasSpawned or TimedOut():
                        print("CrimsonQueen and Chest Has been killed waiting 5 sec before continue")
                        toggleKami(False)
                        Terminal.SetCheckBox("Kami Loot",True)
                        Terminal.SetCheckBox("Auto Loot",True)
                        time.sleep(5)
                        Terminal.SetCheckBox("Kami Loot",False)
                        Terminal.SetCheckBox("Auto Loot",False)
                        if pos.x != -849:
                            Character.Teleport(-849, 132)
                        else:
                            time.sleep(1)
                            Character.EnterPortal()
                            time.sleep(0.5)
                            Character.EnterPortal()
                            time.sleep(0.5)
                            Character.EnterPortal()
                            time.sleep(1)
                            
                            SCLib.UpdateVar("KillCrimsonQueen", False)
                            ResetSpawn()
                            ResetNowLockedFunction()
                            TimeOutReset()
                    else:
                        find = Field.FindReactor(queen_reactor)
                        if TimedOut() and not find.valid:
                            if pos.x != -849:
                                Character.Teleport(-849, 132)
                            else:
                                time.sleep(1)
                                Character.EnterPortal()
                                time.sleep(0.5)
                                Character.EnterPortal()
                            ResetSpawn()
                            ResetNowLockedFunction()
                            TimeOutReset()
                        else:
                            InteractCrimsonQueenNormal()
                            toggleSI(False)
                            KannaSkills(False)

def vellum():
    boss = Field.FindMob(NormalVellum)
    if not boss.valid:
        toggleKami(False)
    if CurrentChannel != 20:
        print("Change to Channel 20")
        Terminal.ChangeChannel(20)
    else:
        if fieldID not in AbyssalCaveNormal:
            if fieldID not in NorthGardenNormal:
                if fieldID != ColossalRoot:
                    GotoRootAbyss()
                else:
                    if Inventory.GetItemCount(4033611) < 1:
                        print("Missing Gnarled Wooden Key, Buying one before continue")
                        BuyGnarledWoodenKey()
                    else:
                        Party.CreateParty()
                        enter_boss(vellum_portal)
            else:
                if not NowLockedVar:
                    mob = Field.FindMob(7120111)
                    if mob.valid:
                        toggleKami(True)
                        toggleSI(True)
                        KannaSkills(True)
                        togglebossfreeze(False)
                        print("Need to kill som more Pointy imps to enter next map")
                    else:
                        toggleKami(False)
                        toggleSI(False)
                        KannaSkills(False)
                        print("Moving on")
                        if pos.x != 2290:
                            Character.Teleport(2290, 179)
                        else:
                            print("Entering Vellum Normal map")
                            Key.Press(0x26)
                else:
                    print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                    SCLib.UpdateVar("KillVellum", False)
                    ResetNowLockedFunction()
        else:
            NowLockedFunction()
            boss = Field.FindMob(NormalVellum)
            if boss.valid:
                toggleSI(True)
                KannaSkills(True)
                DidSpawn()
                if pos.x != -410:
                    Character.Teleport(-410,434)
                toggleNoBossMapEffect(True)
                togglebossfreeze(True)
                print("Killin Vallum Standby")
            else:
                if HasSpawned:
                    toggleKami(False)
                    print("Vallum is dead, waiting 5 sec before continue")
                    Terminal.SetCheckBox("Kami Loot",True)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(5)
                    Terminal.SetCheckBox("Kami Loot",False)
                    Terminal.SetCheckBox("Auto Loot",False)
                    if pos.x != -1758:
                        Character.Teleport(-1758, 440)
                    else:
                        time.sleep(1)
                        Character.EnterPortal()
                        time.sleep(0.5)
                        Character.EnterPortal()
                        time.sleep(1)
                        SCLib.UpdateVar("KillVellum", False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                        time.sleep(1)
                        accountData['mule_number'] = accountData['mule_number']+1
                        writeJson(accountData,accountId)
                else:
                    find = Field.FindReactor(vellum_reactor)
                    if TimedOut() and not find.valid:
                        if pos.x != -1758:
                            Character.Teleport(-1758, 440)
                        else:
                            time.sleep(1)
                            Character.EnterPortal()
                            time.sleep(0.5)
                            Character.EnterPortal()
                        ResetSpawn()
                        ResetNowLockedFunction()
                        TimeOutReset()
                    else:
                        InteractVellumNormal()
                        toggleSI(False)
                        KannaSkills(False)
#root00
# quest id's
q0 = 30000
q1 = q0 + 2
q2 = q1 + 1
q3 = q2 + 1
q4 = q3 + 1
q5 = q4 + 1
q6 = q5 + 1
q7 = q6 + 1
q8 = q7 + 1
q9 = 30010
q10= 30011
q11= 30012
q12= 30013
#print(q8)

# npc id's
nNeinheart = 1101002
nGirl = 1064001
nGirl2 = 1064002

# map id's
mRoot = 105200000

Terminal.SetCheckBox("Rush By Level", False)
accountId = Terminal.GetLineEdit("LoginID")
accountData = startupCheck(accountId)
handleReady(accountData)
writeJson(accountData,accountId)
if GameState.IsInGame() or GameState.IsInCashShop() and not SCLib.GetVar("DoneAll"):
    ColossalRoot = 105200000
    SouthGardenNormal = [105200300,105200301,105200302,105200303,105200304,105200305,105200306,105200307,105200308,105200309]
    QueensCastleNormal = [105200310,105200311,105200312,105200313,105200314,105200315,105200316,105200317,105200318,105200319]
    WestGardenNormal = [105200200,105200201,105200202,105200203,105200204,105200205,105200206,105200207,105200208,105200209]
    AfternoonTeaTableNormal = [105200210,105200211,105200212,105200213,105200214,105200215,105200216,105200217,105200218,105200219]
    EastGardenNormal = [105200100,105200101,105200102,105200103,105200104,105200105,105200106,105200107,105200108,105200109]
    TerporalCrevasseNormal = [105200110,105200111,105200112,105200113,105200114,105200115,105200116,105200117,105200118,105200119]
    NorthGardenNormal = [105200400,105200401,105200402,105200403,105200404,105200405,105200406,105200407,105200408,105200409]
    AbyssalCaveNormal = [105200410,105200411,105200412,105200413,105200414,105200415,105200416,105200417,105200418,105200419]
    if doQuest(63785):
        if needQuest(63785):
            startQuest(63785,9400428)
            time.sleep(1)
        elif hasQuest(63785):
            if Quest.CheckCompleteDemand(63785, 9400428) ==0:
                completeQuest(63785,9400428)
    if doQuest(63786):
        if needQuest(63786):
            startQuest(63786,9400428)
            time.sleep(1)
        elif hasQuest(63786):
            if Quest.CheckCompleteDemand(63786, 9400428) ==0:
                completeQuest(63786,9400428)
    if doQuest(63787):
        if needQuest(63787):
            startQuest(63787,9400428)
            time.sleep(1)
        elif hasQuest(63787):
            if Quest.CheckCompleteDemand(63787, 9400428) ==0:
                completeQuest(63787,9400428)
    if level > 240 or level < 160:
        print("Do not need to do RA daily for this character")
        accountData['mule_number'] = int(Terminal.GetLineEdit("LoginChar")) + 1
        writeJson(accountData,accountId)
        time.sleep(5)
        Terminal.Logout()
        time.sleep(2)
    elif doQuest(q6) and not GameState.IsInCashShop():
        mRoot = 910700200
        if doQuest(q0):
            if needQuest(q0):
                startQuest(q0, nNeinheart)
            elif hasQuest(q0):
                goThru(763, -975)

        elif doQuest(q1):
            if needQuest(q1):
                if mapID(mRoot):
                    startQuest(q1, nGirl)
                else:
                    rush(105010000)
                    port = Field.FindPortal("root00")
                    if port.valid:
                        goThru(port.x, port.y)
            elif hasQuest(q1):
                goThru(-1013, 215)
                completeQuest(q1, nGirl)

        elif doQuest(q2):
            if needQuest(q2):
                startQuest(q2, nGirl)
            elif hasQuest(q2):
                if Quest.CheckCompleteDemand(q2, nGirl) ==0:
                    completeQuest(q2, nGirl)
                else:
                    goThru(-1013, 215)
                

        elif doQuest(q3):
            if needQuest(q3):
                startQuest(q3, nGirl)
            elif hasQuest(q3):
                scroll = Inventory.FindItemByID(2431151)
                if scroll.valid:
                    Inventory.UseItem(2431151)
                completeQuest(q3, nGirl)

        elif doQuest(q4):
            if needQuest(q4):
                startQuest(q4, nGirl)
            elif hasQuest(q4):
                completeQuest(q4, nGirl)

        elif doQuest(q5):
            if needQuest(q5):
                startQuest(q5, nGirl)
            elif hasQuest(q5):
                completeQuest(q5, nGirl)

        elif doQuest(q6):
            if needQuest(q6):
                startQuest(q6, nGirl)
            elif hasQuest(q6):
                if mapID(130000000):
                    completeQuest(q6, nNeinheart)
                else:
                    rush(130000000)
                    tele(227, -9)
    elif needQuest(q7) and not GameState.IsInCashShop():
        startQuest(q7,nNeinheart)
    elif doQuest(q8) and not GameState.IsInCashShop():
        print("q8")
        if needQuest(q8):
            if fieldID != mRoot:
                    rush(mRoot)
                    time.sleep(1)
            else:
                startQuest(q8, nGirl2)
        elif hasQuest(q8):
            if Quest.CheckCompleteDemand(q8, nGirl2) ==0 and fieldID == mRoot:
                if fieldID != mRoot:
                    rush(mRoot)
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    Quest.CompleteQuest(q8, nGirl2)
            else:
                vonbon()
    elif doQuest(q9) and not GameState.IsInCashShop():
        print("q9")
        if needQuest(q9):
            startQuest(q9, nGirl2)
        elif hasQuest(q9):
            if Quest.CheckCompleteDemand(q9, nGirl2) ==0 and fieldID == mRoot:
                if fieldID != mRoot:
                    rush(mRoot)
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    Quest.CompleteQuest(q9, nGirl2)
            else:
                print("pierre")
                pierre()
    elif doQuest(q10) and not GameState.IsInCashShop():
        print("q10")
        if needQuest(q10):
            startQuest(q10, nGirl2)
        elif hasQuest(q10):
            if Quest.CheckCompleteDemand(q10, nGirl2) ==0 and fieldID == mRoot:
                if fieldID != mRoot:
                    rush(mRoot)
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    Quest.CompleteQuest(q10, nGirl2)
            else:
                crimsonqueen()
    elif doQuest(q11) and not GameState.IsInCashShop():
        print("q11")
        if needQuest(q11):
            startQuest(q11, nGirl2)
        elif hasQuest(q11):
            if Quest.CheckCompleteDemand(q11, nGirl2) ==0 and fieldID == mRoot:
                if fieldID != mRoot:
                    rush(mRoot)
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    Quest.CompleteQuest(q11, nGirl2)
                    time.sleep(1)
            else:
                vellum()
    elif doQuest(q12) and not GameState.IsInCashShop():
        print("q12")
        if needQuest(q12):
            startQuest(q12, nGirl2)
    
    elif enter_cs:
        print("11",enter_cs)
        if GameState.IsInGame() and not GameState.IsInCashShop():
            print("Going to cash shop to claim reward points")
            time.sleep(1)
            Terminal.EnterCashShop()
            time.sleep(1)
        elif GameState.IsInCashShop():
            print("Leaving cash shop to resume bossing")
            time.sleep(1)
            Terminal.LeaveCashShop()
            time.sleep(1)
            SCLib.UpdateVar("enter_cs",False)
    #StartQuest(63780, 9400428)
    elif doQuest(63780):
        if needQuest(63780):
            startQuest(63780, 9400428)

###CrimsonQueen Normal###
    elif KillCrimsonQueen:
        print("Doing Crimson Queen")
        #toggleKami(False)
        if CrimsonQueenNormal:
            #print("Normal")
            if RetryCountReached():
                SCLib.UpdateVar("KillCrimsonQueen", False)
                ResetNowLockedFunction()
                RetryCountReset()
            if CurrentChannel != 20:
                print("Change to Channel 20")
                Terminal.ChangeChannel(20)
            else:
                if fieldID not in QueensCastleNormal:
                    if fieldID not in SouthGardenNormal:
                        if fieldID != ColossalRoot:
                            GotoRootAbyss()
                        else:
                            if Inventory.GetItemCount(4033611) < 1:
                                print("Missing Gnarled Wooden Key, Buying one before continue")
                                BuyGnarledWoodenKey()
                            else:
                                Party.CreateParty()
                                enter_boss(queen_portal)
                                RetryCountAdd()
                    else:
                        if not NowLockedVar:
                            mob = Field.FindMob(7120110)
                            if mob.valid:
                                toggleKami(True)
                                KannaSkills(True)
                                toggleSI(True)
                                togglebossfreeze(False)
                                print("Need to kill some more Blazing Imps to enter next room")
                            else:
                                toggleSI(False)
                                toggleKami(False)
                                KannaSkills(False)
                                print("Imps are dead")
                                if pos.x != 1835:
                                    print("Moving into position to enter portal")
                                    Character.Teleport(1835, 259)
                                else:
                                    print("Entering Portal")
                                    Character.EnterPortal()
                        else:
                            print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                            SCLib.UpdateVar("KillCrimsonQueen", False)
                            ResetNowLockedFunction()
                else:
                    NowLockedFunction()
                    boss = Field.FindMob(NormalCrimsonQueen)
                    boss1 = Field.FindMob(NormalCrimsonQueen1)
                    boss2 = Field.FindMob(NormalCrimsonQueen2)
                    boss3 = Field.FindMob(NormalCrimsonQueen3)
                    if boss.valid or boss1.valid or boss2.valid or boss3.valid:
                        toggleSI(True)
                        KannaSkills(True)
                        toggleNoBossMapEffect(True)
                        togglebossfreeze(True)
                        toggleKami(True)
                        print("Fighting boss standby")
                    else:
                        toggleSI(False)
                        toggleKami(False)
                        chest = Field.FindMob(8920106)
                        newX = chest.x -30
                        TimeOutCount()
                        if chest.valid:
                            DidSpawn()
                            print("Attacking chest to get the loot")
                            toggleSI(False)
                            Character.BasicAttack()
                            Terminal.SetCheckBox("Kami Loot",True)
                            Terminal.SetCheckBox("Auto Loot",True)
                            time.sleep(5)
                            Terminal.SetCheckBox("Kami Loot",False)
                            Terminal.SetCheckBox("Auto Loot",False)
                        else:
                            if HasSpawned or TimedOut():
                                print("CrimsonQueen and Chest Has been killed waiting 5 sec before continue")
                                toggleKami(False)
                                Terminal.SetCheckBox("Kami Loot",True)
                                Terminal.SetCheckBox("Auto Loot",True)
                                time.sleep(5)
                                Terminal.SetCheckBox("Kami Loot",False)
                                Terminal.SetCheckBox("Auto Loot",False)
                                if pos.x != -849:
                                    Character.Teleport(-849, 132)
                                    time.sleep(1)
                                else:
                                    Character.EnterPortal()
                                    time.sleep(0.5)
                                    Character.EnterPortal()
                                    time.sleep(1)
                                    SCLib.UpdateVar("KillCrimsonQueen", False)
                                    ResetSpawn()
                                    ResetNowLockedFunction()
                                    TimeOutReset()
                                    RetryCountReset()
                            else:
                                find_q = Field.FindReactor(queen_reactor)
                                if TimedOut() and not find_q.valid:
                                    if pos.x != -849:
                                        Character.Teleport(-849, 132)
                                    else:
                                        time.sleep(1)
                                        Character.EnterPortal()
                                        time.sleep(0.5)
                                        Character.EnterPortal()
                                    ResetSpawn()
                                    ResetNowLockedFunction()
                                    TimeOutReset()
                                else:
                                    InteractCrimsonQueenNormal()
                                    toggleSI(False)
                                    KannaSkills(False)
    ###Pierre Normal###
    elif KillPierre:
        print("Doing Pierre")
        #toggleKami(False)
        if PierreNormal:
            #print("Normal")
            if RetryCountReached():
                SCLib.UpdateVar("KillPierre", False)
                ResetNowLockedFunction()
                RetryCountReset()
            if CurrentChannel != 20:
                print("Change to Channel 20")
                Terminal.ChangeChannel(20)
            else:
                if fieldID not in AfternoonTeaTableNormal:
                    if fieldID not in WestGardenNormal:
                        if fieldID != ColossalRoot:
                            GotoRootAbyss()
                        else:
                            if Inventory.GetItemCount(4033611) < 1:
                                print("Missing Gnarled Wooden Key, Buying one before continue")
                                BuyGnarledWoodenKey()
                            else:
                                Party.CreateParty()
                                enter_boss(pierre_portal)
                                RetryCountAdd()
                    else:
                        if not NowLockedVar:
                            mob = Field.FindMob(7120110)
                            if mob.valid:
                                toggleKami(True)
                                toggleSI(True)
                                KannaSkills(True)
                                togglebossfreeze(False)
                                print("Still some more Blazing imp to kill")
                            else:
                                print("Imps are dead")
                                toggleSI(False)
                                KannaSkills(False)
                                toggleKami(False)
                                if pos.x != 2407:
                                    print("Moving into position to enter portal")
                                    Character.Teleport(2407, 100)
                                else:
                                    print("Entering portal")
                                    Character.EnterPortal()
                        else:
                            print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                            SCLib.UpdateVar("KillPierre", False)
                            ResetNowLockedFunction()
                else:
                    NowLockedFunction()
                    boss1 = Field.FindMob(NormalPierre)
                    boss2 = Field.FindMob(NormalPierrev2)
                    boss3 = Field.FindMob(NormalPierrev3)
                    if boss1.valid or boss2.valid or boss3.valid:
                        toggleSI(True)
                        toggleKami(True)
                        KannaSkills(True)
                        toggleNoBossMapEffect(True)
                        togglebossfreeze(True)
                        print("Killing Pierre, standby")
                    else:
                        toggleKami(False)
                        toggleSI(False)
                        chest = Field.FindMob(8900103)
                        newX = chest.x -50
                        TimeOutCount()
                        if chest.valid:
                            print("Attacking Chest to get loot")
                            DidSpawn()
                            toggleSI(False)
                            time.sleep(1)
                            Character.BasicAttack()
                            Terminal.SetCheckBox("Kami Loot",True)
                            Terminal.SetCheckBox("Auto Loot",True)
                            time.sleep(5)
                            Terminal.SetCheckBox("Kami Loot",False)
                            Terminal.SetCheckBox("Auto Loot",False)
                        else:
                            if HasSpawned or TimedOut():
                                print("PierreNormal and chest has been killed waiting 5 sec before continue")
                                Terminal.SetCheckBox("Kami Loot",True)
                                Terminal.SetCheckBox("Auto Loot",True)
                                time.sleep(5)
                                Terminal.SetCheckBox("Kami Loot",False)
                                Terminal.SetCheckBox("Auto Loot",False)
                                if pos.x != -382:
                                    print("Moving into position to enter portal")
                                    Character.Teleport(-382, 550)
                                    time.sleep(1)
                                else:
                                    print("Entering portal")
                                    Character.EnterPortal()
                                    time.sleep(0.5)
                                    Character.EnterPortal()
                                    time.sleep(2)
                                    SCLib.UpdateVar("KillPierre", False)
                                    ResetSpawn()
                                    ResetNowLockedFunction()
                                    TimeOutReset()
                                    RetryCountReset()
                            else:
                                KannaSkills(False)
                                toggleSI(False)
    ###VonBon Normal###
    elif KillVonBon:
        print("Doing Von Bon")
        #toggleKami(False)
        
        if VonBonNormal:
            #print("Normal")
            if RetryCountReached():
                SCLib.UpdateVar("KillVonBon", False)
                ResetNowLockedFunction()
                RetryCountReset()
            if CurrentChannel != 20:
                print("Change to Channel 20")
                Terminal.ChangeChannel(20)
            else:
                if fieldID not in TerporalCrevasseNormal:
                    if fieldID not in EastGardenNormal:
                        if fieldID != ColossalRoot:
                            GotoRootAbyss()
                        else:
                            if Inventory.GetItemCount(4033611) < 1:
                                print("Missing Gnarled Wooden Key, Buying one before continue")
                                BuyGnarledWoodenKey()
                            else:
                                Party.CreateParty()
                                enter_boss(vonbon_portal)
                                RetryCountAdd()
                    else:
                        if not NowLockedVar:
                            mob = Field.FindMob(7120110)
                            if mob.valid:
                                toggleKami(True)
                                toggleSI(True)
                                KannaSkills(True)
                                togglebossfreeze(False)
                                print("Killing Blazing Imps")
                            else:
                                toggleSI(False)
                                toggleKami(False)
                                KannaSkills(False)
                                if pos.x != 3352:
                                    Character.Teleport(3352, 155)
                                else:
                                    Character.EnterPortal()
                        else:
                            print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                            SCLib.UpdateVar("KillVonBon", False)
                            ResetNowLockedFunction()
                else:
                    NowLockedFunction()
                    boss = Field.FindMob(NormalVonBon)
                    if boss.valid:
                        toggleSI(True)
                        KannaSkills(True)
                        toggleKami(True)
                        toggleNoBossMapEffect(True)
                        togglebossfreeze(True)
                        DidSpawn()
                        print("Killing boss Standby")
                    else:
                        if HasSpawned:
                            toggleKami(False)
                            print("VonBon is dead, Waiting 5 sec before continue")
                            Terminal.SetCheckBox("Kami Loot",True)
                            Terminal.SetCheckBox("Auto Loot",True)
                            time.sleep(5)
                            Terminal.SetCheckBox("Kami Loot",False)
                            Terminal.SetCheckBox("Auto Loot",False)
                            if pos.x != -1090:
                                Character.Teleport(-1090, 453)
                                time.sleep(1)
                            else:
                                Character.EnterPortal()
                                time.sleep(0.5)
                                Character.EnterPortal()
                                time.sleep(1)
                                SCLib.UpdateVar("KillVonBon", False)
                                ResetSpawn()
                                ResetNowLockedFunction()
                                RetryCountReset()
                        else:
                            find = Field.FindReactor(vonbon_reactor)
                            if TimedOut() and not find.valid:
                                if pos.x != -1090:
                                    Character.Teleport(-1090, 453)
                                else:
                                    time.sleep(1)
                                    Character.EnterPortal()
                                    time.sleep(0.5)
                                    Character.EnterPortal()
                                ResetSpawn()
                                ResetNowLockedFunction()
                                TimeOutReset()
                            else:
                                InteractVonBonNormal()
                                toggleSI(False)
                                KannaSkills(False)
    ###Vellum Normal###
    elif KillVellum:
        print("Doing Vellum")
        boss = Field.FindMob(NormalVellum)
        if not boss.valid:
            toggleKami(False)
        if VellumNormal:
            #print("Normal")
            if RetryCountReached():
                SCLib.UpdateVar("KillVellum", False)
                ResetNowLockedFunction()
                RetryCountReset()
            if CurrentChannel != 20:
                print("Change to Channel 20")
                Terminal.ChangeChannel(20)
            else:
                if fieldID not in AbyssalCaveNormal:
                    if fieldID not in NorthGardenNormal:
                        if fieldID != ColossalRoot:
                            GotoRootAbyss()
                        else:
                            if Inventory.GetItemCount(4033611) < 1:
                                print("Missing Gnarled Wooden Key, Buying one before continue")
                                BuyGnarledWoodenKey()
                            else:
                                Party.CreateParty()
                                enter_boss(vellum_portal)
                                RetryCountAdd()
                    else:
                        if not NowLockedVar:
                            mob = Field.FindMob(7120111)
                            if mob.valid:
                                toggleKami(True)
                                toggleSI(True)
                                KannaSkills(True)
                                togglebossfreeze(False)
                                print("Need to kill som more Pointy imps to enter next map")
                            else:
                                toggleKami(False)
                                toggleSI(False)
                                KannaSkills(False)
                                print("Moving on")
                                if pos.x != 2290:
                                    Character.Teleport(2290, 179)
                                else:
                                    print("Entering Vellum Normal map")
                                    Key.Press(0x26)
                        else:
                            print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                            SCLib.UpdateVar("KillVellum", False)
                            ResetNowLockedFunction()
                else:
                    NowLockedFunction()
                    boss = Field.FindMob(NormalVellum)
                    if boss.valid:
                        toggleSI(True)
                        KannaSkills(True)
                        DidSpawn() #-410 434
                        if pos.x != boss.x-120:
                            Character.Teleport(boss.x-120,434)
                        toggleNoBossMapEffect(True)
                        togglebossfreeze(True)
                        print("Killin Vallum Standby")
                    else:
                        if HasSpawned:
                            toggleKami(False)
                            print("Vallum is dead, waiting 5 sec before continue")
                            Terminal.SetCheckBox("Kami Loot",True)
                            Terminal.SetCheckBox("Auto Loot",True)
                            time.sleep(5)
                            Terminal.SetCheckBox("Kami Loot",False)
                            Terminal.SetCheckBox("Auto Loot",False)
                            if pos.x != -1758:
                                Character.Teleport(-1758, 440)
                                time.sleep(1)
                            else:
                                Character.EnterPortal()
                                time.sleep(0.5)
                                Character.EnterPortal()
                                time.sleep(1)
                                ResetSpawn()
                                ResetNowLockedFunction()
                                RetryCountReset()
                                if job in KannaJobs:
                                    Terminal.SetCheckBox("Grenade Kami",True)
                                    Terminal.SetSpinBox("MonkeySpiritsNDdelay",40)
                                time.sleep(1)
                                if fieldID not in AbyssalCaveNormal:
                                    SCLib.UpdateVar("KillVellum", False)
                                print("Done all RA bosses, moving to zakum")
                        else:
                            find = Field.FindReactor(vellum_reactor)
                            if TimedOut() and not find.valid:
                                if pos.x != -1758:
                                    Character.Teleport(-1758, 440)
                                else:
                                    time.sleep(1)
                                    Character.EnterPortal()
                                    time.sleep(0.5)
                                    Character.EnterPortal()
                                ResetSpawn()
                                ResetNowLockedFunction()
                                TimeOutReset()
                            else:
                                InteractVellumNormal()
                                toggleSI(False)
                                KannaSkills(False)
    elif KillZakumDaily == False and (fieldID == TheDoorToZakum or fieldID == EntranceToZakumAlter):
        toggleKami(False)
        toggleHyperTeleportRock(False)
        KannaSkills(False)
        if fieldID == TheDoorToZakum:
            if pos.x != -3003:
                Character.Teleport(-3003, -220)
                time.sleep(0.5)
                Character.EnterPortal()
                time.sleep(1)
                if fieldID != TheDoorToZakum:
                    SCLib.UpdateVar("KillZakumDaily",False)
        elif (fieldID == TheDoorToZakum or fieldID == EntranceToZakumAlter or fieldID == TheCaveOfTrials3Zakum):
            print("Moving to a location where MapRusher works")
            if pos.x != -1599:
                Terminal.SetCheckBox("Auto Equip",False)
                Character.Teleport(-1599, -331)
                time.sleep(0.5)
                Character.EnterPortal()
                
                

    elif KillZakumDaily:
        toggleKami(False)
        toggleSI(False)
        KannaSkills(False)
        print("Doing Zakum")
        Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
        Terminal.SetCheckBox('filter_equip',False)
        pos = Character.GetPos()
        if fieldID not in ZakumsAltar:
            if fieldID != EntranceToZakumAlter:
                if fieldID != TheDoorToZakum:
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
                    toggleSI(False)
                    KannaSkills(False)
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
                toggleSI(True)
                KannaSkills(True)
                if pos.x != -313:
                    Character.Teleport(-313, 84)
                else:
                    print("Fighting Zakum StandBy")
            else:
                if HasSpawned:
                    print("Zakum is dead, waiting 10 sec before continue")
                    toggleKami(False)
                    KannaSkills(False)
                    Terminal.SetCheckBox("Kami Loot",True)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(5)
                    toggleSI(False)
                    face_check = Field.FindItem(condensed_power_crystal)
                    eye_check = Field.FindItem(aquatic_letter_eye)
                    if not face_check.valid and not eye_check.valid:
                        Terminal.SetCheckBox("Kami Loot",False)
                        Terminal.SetCheckBox("Auto Loot",False)
                        print("Did not find accessory, leaving.")
                        Character.TalkToNpc(2030010)
                        time.sleep(1)
                        SCLib.UpdateVar("KillZakumDaily", False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                        if fieldID == TheDoorToZakum:
                            if pos.x != -3003:
                                Character.Teleport(-3003, -220)
                                time.sleep(1)
                                Character.EnterPortal()
                else:
                    print("Finding item in inventory to drop")
                    stone = Inventory.FindItemByID(4001017)
                    if stone.valid:
                        if pos.x != -25:
                            Character.Teleport(-25, 84)
                        else:
                            print("Dropping stone to spawn Zakum")
                            Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)
        #StartQuest(63785, 9400428)
    elif not KillVellum and not KillCrimsonQueen and not KillPierre and not KillVonBon and not KillZakumDaily:
        if fieldID != mRoot:
            GotoRootAbyss()
            time.sleep(3)
        else:
            print("Delivering Daily boss quests for reward points")
            #q1 = Quest.GetQuestState(26430) #ZakumNormal
            #q2 = Quest.GetQuestState(26525) #VonBonNormal
            #q3 = Quest.GetQuestState(26526) #PierreNormal
            #q4 = Quest.GetQuestState(26527) #CrimsonQueenNormal
            #q5 = Quest.GetQuestState(26528) #VellumNormal
            #q8 = Quest.GetQuestState(5870)
            CheckCompleteStepAndDeliver(26430, 9030200) #ZakumNormal
            CheckCompleteStepAndDeliver(26525, 9030200) #VonBonNormal
            CheckCompleteStepAndDeliver(26526, 9030200) #PierreNormal
            CheckCompleteStepAndDeliver(26527, 9030200) #CrimsonQueenNormal
            CheckCompleteStepAndDeliver(26528, 9030200) #VellumNormal
            CheckCompleteStepAndDeliver(5870, 9030200)
            time.sleep(1)
            accountData['mule_number'] = accountData['mule_number']+1
            writeJson(accountData,accountId)
            time.sleep(1)
            Terminal.Logout()

elif GameState.GetLoginStep() == 2:
    Terminal.SetCheckBox("Auto Login",False)
    time.sleep(1.5)
    try:
        target_char = Login.GetChar(accountData['mule_number'])
    except:
        target_char = None
    if target_char is None:
        print("Reached end of character list")
        SCLib.UpdateVar("DoneAll",True)
        Terminal.SetLineEdit("LoginChar", str(accountData['orig_char']))
        Terminal.SetCheckBox("Auto Login",True)
        time.sleep(5)
        accountData['mule_number'] = start_char_number
        writeJson(accountData,accountId)
        time.sleep(3)
    else:
        Terminal.SetLineEdit("LoginChar", str(accountData['mule_number']))
        Terminal.SetCheckBox("Auto Login",True)
        SCLib.StopVars()
        time.sleep(5)