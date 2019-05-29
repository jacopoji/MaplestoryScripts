import Field, Character, Terminal, time, Quest, GameState, Inventory, Party, Packet,sys,os,Key,json, Login,Npc

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")

start_char_number = 24
return_char = 24
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
VonBonNormalRebootBuffer =  ["[00000C45]","[830C0000]", "[850C0000]", "[880C0000]", "[800C0000]", "[750C0000]","[6F0C0000]","[820C0000]","[8F0C0000]","[950C0000]","[A20C0000]","[AF0C0000]","[8D0C0000]","[9A0C0000]"]
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
sys.path.append('C:/Users/Jacopo/Desktop/Scripts')
import headers
from JobConstants import *
###Packet Headers###
InteractHeader = 0x0419 
BlockBuyHeader = headers.buy_block_header
BuyItemHeader = headers.buy_header

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

def ToggleMobDisarm(flag):
    Terminal.SetCheckBox("Mob Disarm",flag)

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

def AttackAuto(skillid,on):
    attack_key = 0x44
    Key.Set(attack_key,1,skillid)
    Terminal.SetCheckBox("Skill Injection", False)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack", on)
    Terminal.SetComboBox("AttackKey",33)
    Terminal.SetSpinBox("autoattack_spin",100)

def AttackSI(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)
    Terminal.SetRadioButton(siOption,True)

def AttackSIND(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetRadioButton(siOption,True)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)

def SemiNDAA(siSkill,dummySkill,delay,on):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection",False)
    Terminal.SetCheckBox("Melee No Delay",True)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    #count = 0
    while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        for x in range(8):
            Character.UseSkill(siSkill)
            time.sleep(0.015)
        Character.UseSkill(dummySkill)
        time.sleep(delay)
        if Terminal.IsRushing():
            break

def AttackSemiND(siSkill,dummySkill,delay,on):
    try:
        SCLib.ThreadedFunction(SemiNDAA(siSkill,dummySkill,delay,on))
    except:
        x = 1

def SetSIND(siSkill,delay,on):
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetLineEdit("SISkillID",siSkill)
    Terminal.SetCheckBox("Skill Injection",on)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetSpinBox("SkillInjection",delay)

def AttackSemiNDOnce(siSkill,dummySkill,delay,on):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    if Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetLineEdit("SISkillID",str(siSkill))
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",15)
        time.sleep(0.24)
        Terminal.SetCheckBox("Skill Injection",False)
        time.sleep(0.02)
        Character.UseSkill(dummySkill)
        time.sleep(delay)

def SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    Terminal.SetCheckBox("Speedy Gonzales",True)
    #count = 0
    if siSkill != 32120055:
        delay = 30*math.ceil(delay*1000 * (10+attackSpeed)/480)/1000
    #print("The delay for skill {} is {}, starting si".format(siSkill,delay))
    if siSkill in [5311000,5301000]:
        sleepTime = 0.161
    elif siSkill not in [25101000,25121000]:
        sleepTime = 0.231
    else:
        sleepTime = 0.101
    while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetLineEdit("SISkillID",str(siSkill))
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",17)
        time.sleep(sleepTime)
        #Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetLineEdit("SISkillID",str(dummySkill))
        time.sleep(0.043)
        Terminal.SetCheckBox("Skill Injection",False)
        time.sleep(delay+0.05)
        #if Terminal.IsRushing():
        #    break
        #if count >= 30:
        #    break
        if siSkill == 27111303 and not(Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219)):
            break
        #count += 1
    #print("Si ended due to break options")
    Terminal.SetProperty("IssueThread",True)
def AttackSemiNDMagic(siSkill,dummySkill,delay,on,attackSpeed = 4):
    try:
        if Terminal.GetProperty("IssueThread",True):
            SCLib.ThreadedFunction(SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed))
            Terminal.SetProperty("IssueThread",False)
    except:
        pass
        

def ToggleAttack(on):
    attack_key = 0x44
    pgup_key = 0x21
    if Character.IsOwnFamiliar(9960098) and level > 15 and job not in KinesisJobs:
        Terminal.SetSlider("sliderMP", 90) #use boogie to regen mana
        Terminal.SetComboBox("MPKey",4)
    else:
        Terminal.SetSlider("sliderMP", 20) #use potion to regen mana
        Terminal.SetComboBox("MPKey",6)

    if not SCLib.GetVar("DoingZakum") or not getSpider: #Ocassionaly use big spider (in zakum)
        Terminal.SetComboBox("Familiar0",1)

    #print(SCLib.GetVar("DoingJobAdv"))
    if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum"):
        if Terminal.GetCheckBox("Legit Vac") and Terminal.GetCheckBox("Kami Vac") and field_id not in mobFalldownBlacklist:# and not Terminal.GetCheckBox("Melee No Delay"):
            Terminal.SetCheckBox("Mob Falldown",on)
        else:
            if Terminal.GetCheckBox("Mob Falldown"):
                Terminal.SetCheckBox("Mob Falldown",False)
    else:
        Terminal.SetCheckBox("Mob Falldown",False)
    if Terminal.GetLineEdit("SISkillID") in SpeedyGonzalesList and Terminal.GetCheckBox("Skill Injection") and Terminal.GetCheckBox("Melee No Delay"):
        #print("In list")
        if not Terminal.GetCheckBox("Speedy Gonzales"):
            Terminal.SetCheckBox("Speedy Gonzales",True)
        if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("GettingBoogie") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"):
            if not Terminal.GetCheckBox("filter_etc"):
                Terminal.SetCheckBox("filter_etc",True)
            if not Terminal.GetCheckBox("filter_use"):
                Terminal.SetCheckBox("filter_use",True)
        else:
            if Terminal.GetCheckBox("filter_etc"):
                Terminal.SetCheckBox("filter_etc",False)
            if Terminal.GetCheckBox("filter_use"):
                Terminal.SetCheckBox("filter_use",False)
        #Terminal.SetSpinBox("FilterMeso",0)
        if level < 140:
            ToggleLoot(False)
    elif Terminal.GetLineEdit("SISkillID") in SpeedyGonzalesList:
        Terminal.SetCheckBox("Speedy Gonzales",True)
    elif job == BuccaneerJobs[1]:
        if not Terminal.GetCheckBox("Speedy Gonzales"):
            Terminal.SetCheckBox("Speedy Gonzales",True) 
    else:
        #if Terminal.GetCheckBox("Speedy Gonzales"):
        #    Terminal.SetCheckBox("Speedy Gonzales",False)
        if Terminal.GetCheckBox("filter_etc"):
            Terminal.SetCheckBox("filter_etc",False)
        if Terminal.GetCheckBox("filter_use"):
            Terminal.SetCheckBox("filter_use",False)
        if level < 140:
            Terminal.SetSpinBox("FilterMeso",0)
            
    #elif job == NightWalkerJobs[2] or job == NightWalkerJobs[3]:
    #    if not Terminal.GetCheckBox("Speedy Gonzales"):
    #        Terminal.SetCheckBox("Speedy Gonzales",True)
    if level > 60 and level < 120 and not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"):
        Terminal.SetCheckBox("Kami Loot",False)
        Terminal.SetCheckBox("Auto Loot",True)
    if job == 4200: #kanna first job
        AttackSI(42001006,on)
    elif job in KannaJobs and field_id in curbrockhideout:
        AttackSI(42001006,on)
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
    elif job == 4211:#kanna 3rd
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",on)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 4212: #kanna 4th 
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetSpinBox("charm_delay",100)
            Terminal.SetCheckBox("charm_fma",on)
            Terminal.SetCheckBox("Summon Kishin",False)
            Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
            Terminal.SetSpinBox("autoattack_spin",7500)
            Terminal.SetComboBox("AttackKey",36)
            Terminal.SetCheckBox("Skill Injection",False) #42111011
            #AttackSemiNDMagic(42111000,42001006,0.70,on)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 2700: #lumi first job
        # 20040217 Dark Mode Buff
        # 20040216 Light Mode
        # 20040220 20040219 Equi Mode
        AttackSemiNDMagic(27001201,27001201,0.98,on)
    elif job in LuminousJobs and field_id in curbrockhideout:
        AttackAuto(27001201,on)
    elif job == 2710: #lumi second job
        if Character.HasBuff(2,20040217): #use dark magic
            #AttackAuto(27001201,on)
            AttackSI(27101202,on,200)
        else:
            #AttackSemiNDMagic(27101100,27101100,0.5,on)
            AttackAuto(27101100,on)
    elif job == 2711: #lumi third job
        if Character.HasBuff(2,20040216): #Light Mode
            AttackAuto(27101100,on)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            AttackSemiNDMagic(27111303,27111303,1.77,on)
        else:                              #Dark Mode
            #AttackAuto(27111202,on)
            AttackSI(27101202,on,200)
    elif job == 2712: #lumi fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,20040216): #Light Mode
                AttackAuto(27121100,on)
            elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
                AttackSemiNDMagic(27111303,27111303,1.77,on)
                #AttackAuto(27111303,on)
            else:                              #Dark Mode
                #AttackSemiNDOnce(27121202,27001201,0.96,on)
                AttackSI(27101202,on,200)
    elif job == 3101: #DA first job
        AttackAuto(31011000,on)
    elif job in DemonAvengerJobs and field_id in curbrockhideout:
        AttackAuto(31011000,on)
    elif job == 3120: #DA 2nd
        #AttackSemiNDMagic(31201010,31201010,0.66,on)
        AttackSIND(31201010,on,100)
        #AttackAuto(31011000,on)
    elif job == 3121 or job == 3122: #DA third job and fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(31211010,31211010,0.78,on)
    elif job == 3100 or job == 3110 or job == 3111: #DS first - third job
        #Key.Set(attack_key,1,31000004)31001008
        if SCLib.GetVar("DoingJobAdv"):
            AttackSI(31001008,100,on)
        else:
            AttackSemiNDMagic(31001008,31001008,0.55,on)
    elif job == 3112: #DS fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSI(31121010,on,16)
            AttackSemiNDMagic(31121010,31121010,0.66,on)
    elif job == 2300: #Mercedes 1st 
        AttackAuto(23001000,on)
    elif job in MercedesJobs and field_id in curbrockhideout:
        AttackAuto(23001000,on)
    elif job ==2310: #Mercedes 2nd
        AttackAuto(23101000,on)
        #AttackSIND(23101007,on,250)
        #AttackSIND(23100004,on,300)
    elif job ==2311: #Mercedes 3rd
        #AttackAuto(23111000,on)
        '''
        attack_key = 0x44
        Key.Set(attack_key,1,23111000)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetLineEdit("SISkillID",str(23111002))
        Terminal.SetSpinBox("SkillInjection",200)
        Terminal.SetCheckBox("Melee No Delay",on)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetCheckBox("Skill Injection", on)
        '''
        AttackSemiNDMagic(23111000,23111002,0.54,on)
        #AttackSIND(23111000,on,250)
    elif job == 2312: #Mercedes 4th
        #AttackAuto(23111000)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            '''
            attack_key = 0x44
            Key.Set(attack_key,1,23111000)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",100)
            Terminal.SetLineEdit("SISkillID",str(23111002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
            '''
            #AttackAuto(23111000,on)
            #AttackSIND(23120013,on,150)
            AttackSemiNDMagic(23120013,23111002,0.54,on)
    elif job == 4100: #Hayato 1st 41001004
        AttackSI(41001004,on,100)
    elif job in HayatoJobs and field_id in curbrockhideout:
        AttackSI(41001004,on,100)
    elif job == 4110: #Hayato 2nd 41101000
        AttackSemiNDMagic(41101000,41101000,0.45,on)
    elif job == 4111: #Hayato 3rd 41111011
        AttackSemiNDMagic(41111011,41111011,0.45,on)
    elif job == 4112: #Hayato 4th 41121011
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(41121011,41121011,0.45,on)
    elif job == 3600:#Xenon 1st 36001000
        AttackSemiNDMagic(36001000,36001000,1.08,on)
    elif job in XenonJobs and field_id in curbrockhideout:
        AttackSI(36001000,on,150)
    elif job == 3610:#Xenon 2nd 36101000
        AttackSemiNDMagic(36101000,36101000,0.99,on)
    elif job == 3611:#Xenon 3rd 36111000
        #AttackSemiNDMagic(36111000,36111000,1.8,on)
        AttackSemiNDMagic(36111009,36111009,0.81,on)
        #AttackSemiNDMagic(36111010,36111010,0.72,on)
    elif job == 3612:#Xenon 4th 36121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(36121001) >= 1:
                AttackSemiNDMagic(36121011,36121011,1.38,on)
            else:
                AttackSI(36121000,on,110)
    elif job == 2400: #Phantom 1st 24001000
        AttackSemiNDMagic(24001000,24001000,0.81,on)
    elif job in PhantomJobs and field_id in curbrockhideout:
        AttackAuto(24001000,on)
    elif job == 2410: #Phantom 2nd 24101000
        AttackSemiNDMagic(24101000,24101000,0.99,on)
    elif job == 2411: #Phantom 3rd 24111000
        AttackSemiNDMagic(24111000,24111000,0.99,on)
    elif job == 2412: #Phantom 4th 24121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(24121010) >= 1 and Character.GetSkillLevel(24121000) >= 1:
                AttackSemiNDMagic(24121010,24121010,1.08,on)
                #SetSIND("24121010;24121000",140,on)
            elif Character.GetSkillLevel(24121010) >= 1:
                AttackSemiNDMagic(24121010,24121010,1.08,on)
            else:
                AttackSI(24121000,on,150)
    elif job == 15000: #Illium Pre 1st
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job in IlliumJobs: #Illium 1st+2nd+3rd+4th
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",on)
        Terminal.SetCheckBox("bot/illium/summon_control",on)
        Terminal.SetCheckBox("General FMA",on)
    elif job in CadenaJobs: #Cadena 1st + 2nd + 3rd 64001006 or 64001001
        if job != CadenaJobs[-1]:
            AttackSIND("64001001;64001006",on,100)
        else:
            if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
                #AttackSIND(32120055,32120055,0.45,on)
                #AttackSIND("32120055;64001001",on,100)
                AttackSemiNDMagic(32120055,32120055,0.45,on)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                BindSkill(32121052)
            else:
                AttackSIND("64120000;64001001",on,100)
    elif job in ArkJobs: #Ark 1st + 2nd + 3rd 155001100
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(155001100,155001100,0.85,on)
    elif job == 2001: #Evan pre 1st job
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 2200: #Evan 1st 22001010 AA
        AttackAuto(22001010,on)
    elif job in EvanJobs and field_id in curbrockhideout:
        if field_id == 600050020:
            AttackSIND(22110010,on,100)
        else:
            AttackAuto(22001010,on)
            Key.Set(attack_key,1,22001010)
    elif job == 2211: #Evan 2nd 22110010 SI/ND
        AttackSIND(22110010,on,100)
        
    elif job == 2214: #Evan 3rd 22140010 SI/ND
        AttackSIND(22140010,on,100)
        
    elif job == 2217: #Evan 4th 22170061 SI/ND
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(22170061,on,100)
        
    elif job == 0:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 100: #Swordman
        AttackAuto(1001005,on)
    elif job == 110: #fighter 1101011
        AttackAuto(1101011,on)
    elif job in HeroJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 111: #crusader 1111010
        AttackSIND(1111010,on,450)
    elif job == 112: #Hero 1120017
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSIND(1120017,on,400)
            AttackSemiNDMagic(1120017,1120017,0.6,on)
    elif job == 120: #Page 1201011
        AttackSI(1201011,on)
    elif job in PaladinJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 121: #White knight 1211008
        #AttackAuto(1211008,on)
        AttackSI(1201011,on)
    elif job == 122: #Paladin 1211008
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1221004,1221004,0.81,on)
            '''
            while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame():
                for x in range(1,8,1):
                    Character.UseSkill(1221004)
                    time.sleep(0.02)
                time.sleep(0.02)
                Character.UseSkill(1221004)
                time.sleep(0.80)
            '''
    elif job == 130: #Spearman 1301011
        AttackSemiND(1301011,1301011,0.81,on)
        
    elif job in DarkknightJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 131: #Berserker
        AttackSemiND(1301011,1301011,0.81,on)
        
    elif job == 132: #Dark Knight
        #AttackAuto(1321012,on)
        #AttackSIND(1321012,on,450)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1321012,1321012,0.84,on)
    elif job == 200: #Mage
        AttackAuto(2001008,on)
        
    elif job in ILMageJobs and field_id in curbrockhideout: #1001005
        AttackAuto(2001008,on)
    elif job == 220: #IL wizard
        AttackAuto(2201005,on)
        
    elif job == 221: #IL mage
        AttackAuto(2211002,on)
        
    elif job == 222: #IL archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2221006,on)

        
    elif job in FPMageJobs and field_id in curbrockhideout: #1001005
        AttackSI(2101004,on,100,"SIRadioMagic") 
    elif job == 210: #FP wizard
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 211: #FP mage
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 212: #FP archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2121006,on)
        
    elif job in BishopJobs and field_id in curbrockhideout: #1001005
        AttackAuto(2001008,on)
    elif job == 230: #cleric
        AttackAuto(2301005,on)
    elif job == 231: #priest
        AttackAuto(2311004,on)
    elif job == 232: #Bishop
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackSI(2321007,on,100,"SIRadioMagic")
    elif job == 300: #Archer
        AttackAuto(3001004,on)
        
    elif (job in BowmasterJobs or job in MarksmanJobs) and field_id in curbrockhideout: #1001005
        AttackAuto(3001004,on)
    elif job == 310: #Hunter
        AttackAuto(3101005,on)
        
    elif job == 311: #Ranger
        AttackAuto(3111003,on)
        #AttackSIND(3111003,on,300)
        
    elif job == 312: #Bowmaster
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(3121015,on,600)
        
    elif job == 320: #Crossbowman
        AttackAuto(3201005,on)
    elif job == 321: #Sniper
        AttackAuto(3211009,on)
        #AttackSIND(3211009,on,400)
    elif job == 322: #Marksman
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(3221017,on)
    elif job == 400: #Thief
        
        if SCLib.GetVar("DualBlade"):
            if Character.GetSkillLevel(4001013) == 0:
                LevelSkill(4001013)
            AttackAuto(4001013,on)
        else:
            AttackAuto(4001334,on)
        if Character.GetSkillLevel(4001013) >= 1:
            SCLib.UpdateVar("DualBlade",True)
        else:
            SCLib.UpdateVar("DualBlade",False)
        
    elif job == 410: #Assassin
        AttackSI(4101008,on)
        
    elif job in NightlordJobs and field_id in curbrockhideout: #1001005
        AttackAuto(4101008,on)
    elif job == 411: #Hermit
        AttackSI(4111015,on)
        
    elif job == 412: #nightlord
        #print(Character.GetSkillLevel(32121052))
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetSpinBox("KamiOffsetX", -85)
            if Character.GetSkillLevel(4121017) >= 1:
                AttackSemiNDMagic(4121017,4121017,1.0,on)
            else:
                AttackSI(4111015,on)
        
    elif job == 420: #Bandit
        AttackSI(4201012,on)
        
    elif job in ShadowerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(4001334,on)
    elif job == 421: #Chief Bandit
        AttackSI(4211002,on)
        
    elif job == 422: #Shadower
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(4221007,on)
            #AttackSemiNDMagic(4221007,4221007,1.1,on)
        
    elif job == 430: #dualblade
        if Character.GetSkillLevel(4001013) == 0:
            LevelSkill(4001013)
        elif Character.GetSkillLevel(4000012) < 10:
            LevelSkill(4000012)
        elif Character.GetSkillLevel(4001011) < 5:
            LevelSkill(4001011)
        elif Character.GetSkillLevel(4001003) < 10:
            LevelSkill(4001003)
        elif Character.GetSkillLevel(4001013) < 10:
            LevelSkill(4001013)
        AttackAuto(4001013,on)
    elif job == 431: #dualblade
        AttackAuto(4001013,on)
    elif job == 432:
        AttackSIND(4321004,on,450)
    elif job == 433:
        #AttackAuto(4321004,on)
        AttackSIND(4321004,on,450)
    elif job == 434: #dual blade 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(4341004,4341004,0.74,on)
    elif job == 500: #Pirate
        AttackAuto(5001002,on)
    elif job == 501: #Cannoneer Pirate
        #AttackAuto(5011000,on)
        AttackSIND(5011002,on,200)
    elif job in BuccaneerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5101012,on)
    elif job in CorsairJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5201001,on)
    elif job == 510: #Brawler
        AttackAuto(5101012,on)
    elif job == 511: #Marauder
        AttackAuto(5111002,on)
    elif job == 512: #Buccaneer
        #AttackAuto(5121007,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5121017,5121007,1.25,on)
    elif job == 520: #Gunslinger
        AttackAuto(5201001,on)
    elif job == 521: #Outlaw
        AttackAuto(5211008,on)
    elif job == 522: #Corsair
        #if level < 160:
        #    AttackSIND(5221017,on,350)
        #else:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5221017,5221017,0.85,on)
    elif job == 530: #Cannoneer
        #AttackAuto(5301001,on)
        #AttackSIND(5011002,on,200)
        if Character.GetSkillLevel(5301000) >= 1:
            AttackSIND("5301000;5011002",on,300)
            #AttackSemiNDMagic(5301000,5301000,0.90,on)
        else:
            attack_key = 0x44
            Key.Set(attack_key,1,5301001)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",400)
            Terminal.SetLineEdit("SISkillID",str(5011002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
    elif job in CannoneerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5301001,on)
    elif job == 531: #Cannon Trooper
        '''
        if Terminal.GetCheckBox("Mob Falldown"):
            AttackAuto(5311000,on)
        else:
            AttackAuto(5301001,on)
            Terminal.SetCheckBox("Speedy Gonzales",True)
        '''
        if Character.GetSkillLevel(5311000) >= 1:
            #AttackSemiNDMagic(5311000,5311000,0.96,on)
            AttackSIND("5311000;5011002",on,250)
        else:
            attack_key = 0x44
            Key.Set(attack_key,1,5301001)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",400)
            Terminal.SetLineEdit("SISkillID",str(5011002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
    elif job == 532: #Cannon Master
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND("5321000;5011002",on,250)
            #AttackSemiNDMagic(5321000,5321000,0.95,on)
    elif job == 508: #Jett 1sts
        AttackAuto(5081020,on)
    elif job in JettJobs and field_id in curbrockhideout:
        AttackAuto(5081020,on)
    elif job == 570: #Jett 2nd
        #AttackAuto(5081020,on)
        if Character.GetSkillLevel(5701011) >= 1:
            #AttackSemiNDMagic(5701011,5701011,0.2,on,attackSpeed=4)
            AttackSIND(5701011,on,150)
        else:
            AttackAuto(5701010,on)
    elif job == 571: #Jett 3rd
        if Character.GetSkillLevel(5710020) >= 1:
            #AttackSemiNDMagic(5710020,5710020,0.9,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
        else:
            AttackSIND(5701011,on,150)
    elif job == 572: #Jett 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSemiNDMagic(5710020,5710020,0.4,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
    elif job == 1100: #Dawn warrior 1st
        AttackSI(11001020,on)
    elif job in DawnWarriorJobs and field_id in curbrockhideout: #1001005
        AttackAuto(11001020,on)
    elif job == 1110: #Dawn Warrior 2nd
        #AttackAuto(11101120,on)
        AttackSIND(11101120,on,600)
    elif job == 1111: #Dawn Warrior 3rd
        AttackSI(11111120,on)
        #AttackAuto(11111220,on)
    elif job == 1112: #Dawn Warrior 4th
        dummySkill = 11001020
        dummyDelay = 0.81
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,11111022):
                AttackSemiNDMagic(11121203,dummySkill,dummyDelay,on)
    elif job == 1200: #BW 1st
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
        ToggleLoot(False)
    elif job in BlazeWizardJobs and field_id in curbrockhideout: #1001005
        AttackAuto(12001021,on)
        Terminal.SetCheckBox("Full Map Attack",False)
    elif job == 1210: #BW 2nd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1211: #BW 3rd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1212: #BW 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:           
            #if level < 140:
            Terminal.SetCheckBox("Full Map Attack",True)
            AttackAuto(12001020,on)
                
            #elif level >= 140:
            #    Terminal.SetCheckBox("Full Map Attack",False)
            #    AttackSIND(12121055,on,31)
            
    elif job == 1300: #Wind Archer 1st
        AttackAuto(13001020,on)
    elif job in WindArcherJobs and field_id in curbrockhideout: #1001005
        AttackAuto(13001020,on)
    elif job == 1310: #Wind Archer 2nd
        if Character.GetSkillLevel(13101020) >= 1:
            AttackSI(13101020,on)
        else:
            AttackAuto(13001020,on)
    elif job == 1311: #Wind Archer 3rd
        #AttackAuto(13111020,on)
        AttackSI(13101020,on)
    elif job == 1312: #Wind Archer 4th
        #AttackAuto(13121002,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(13121002,on,siOption = "SIRadioShoot")
    elif job == 1400: #Night Walker 1st
        AttackAuto(14001020,on)
    elif job in NightWalkerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(14001020,on)
    elif job == 1410: #Night Walker 2nd
        AttackSI(14101020,on)
    elif job == 1411: #Night Walker 3rd
        AttackAuto(14111022,on)
    elif job == 1412: #Night Walker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(14111022,on)
    elif job == 1500: #Thunder breaker 1st
        #AttackAuto(15001020,on)
        if Character.GetSkillLevel(15001021) >= 1:
            #AttackSIND(15001021,on,600)
            AttackSemiNDMagic(15001021,15001021,0.8,on)
        else:
            AttackAuto(15001020,on)
    elif job in ThunderBreakerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(15001020,on)
    elif job == 1510: #Thunder breaker 2nd
        #AttackAuto(15101020,on)
        AttackSemiNDMagic(15101020,15101020,0.72,on)
    elif job == 1511: #Thunder breaker 3rd
        #AttackAuto(15111020,on)
        AttackSemiNDMagic(15111020,15111020,0.9,on)
    elif job == 1512: #Thunder breaker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(15121002,15121002,1.08,on)
            #30 * math.ceil(BaseDelay * (14)/480)
            #AttackSIND(15121002,on,500)
        #AttackSIND(15111020,on,300)
        #AttackAuto(15121001,on)
    elif job == 3300: #Wild Hunter 1st
        AttackAuto(33001105,on)
    elif job in WildHunterJobs and field_id in curbrockhideout: #1001005
        AttackAuto(33001105,on)
    elif job == 3310: #Wild Hunter 2nd
        #AttackAuto(33101113,on)
        AttackSI(33101215,on)
    elif job == 3311: #Wild Hunter 3rd
        AttackAuto(33111112,on)
        #AttackSI(33111010,on,100,"SIRadioMagic")
    elif job == 3312: #Wild Hunter 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(33111112,on)
    elif job == 3200: #Battle Mage 1st
        AttackSI(32001014,on)
    elif job in BattleMageJobs and field_id in curbrockhideout: #1001005
        AttackSI(32001014,on)
    elif job == 3210: #Battle Mage 2nd
        #AttackSI(32100010,on)
        AttackSIND(32101001,on,250)
    elif job == 3211: #Batlle Mage 3rd
        #AttackSI(32110017,on)
        AttackSIND(32101001,on,250)
    elif job == 3212: #Battle Mage 4th
        if level >= 160:
            if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
                AttackSemiNDMagic(32120055,32120055,0.45,on)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            if SCLib.GetVar("DoingZakum"):
                #AttackAuto(32121002,on)
                AttackSIND(32101001,on,250)
            else:
                #AttackSI(32120019,on)
                AttackSIND(32101001,on,250)
    elif job == 3700: #Blaster 1st
        Terminal.SetCheckBox("General FMA",False)
        AttackAuto(37001000,on)
    elif job in BlasterJobs and field_id in curbrockhideout: #1001005
        #Terminal.SetCheckBox("General FMA",on)
        Terminal.SetCheckBox("General FMA",False)
        AttackAuto(37001000,on)
    elif job == 3710: #Blaster 2nd
        #Terminal.SetCheckBox("General FMA",on)
        Terminal.SetCheckBox("General FMA",False)
        AttackAuto(37001000,on)
    elif job == 3711: #Blaster 3rd
        #AttackAuto(37001000,on)
        AttackSI(37110006,on,80)
        Terminal.SetCheckBox("General FMA",on)
        #Terminal.SetCheckBox("General FMA",on)
    elif job == 3712: #Blaster 4th
        #AttackAuto(37001000,on)
        Terminal.SetCheckBox("General FMA",False)
        vulcan()
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(37121000,on,80)
    elif job == 3500: #Mechanic 1st
        AttackAuto(35001004,on)
    elif job in MechanicJobs and field_id in curbrockhideout: #1001005
        AttackAuto(35001004,on)
    elif job == 3510: #Mechanic 2nd
        AttackAuto(35101001,on)
    elif job == 3511: #Mechanic 3rd
        AttackAuto(35111006,on)
    elif job == 3512: #Mechanic 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(35111015,35111015,0.84,on)
            #AttackSI(35121015,on,250)
        #AttackAuto(35111006,on)
    elif job == 11212: #Beast Tamer
        #if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
        #    AttackSemiNDMagic(32120055,32120055,0.45,on)
        #elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
        #    BindSkill(32121052)
        #else:
        if Character.HasBuff(2,110001501):
            if Character.GetSkillLevel(112000003) >= 1:
                #AttackSIND(112000003,on,450)
                AttackSemiNDMagic(112000003,112001008,0.38,on)
            else:
                if level <= 17:
                    AttackAuto(112000000,on)
                    
                elif level >= 17 and (not useExploit or SCLib.GetVar("DoingZakum")):
                    Terminal.SetCheckBox("Auto Attack", False)
                    Terminal.SetCheckBox("Skill Injection", False)
                    Terminal.SetCheckBox("Melee No Delay",False)
                    count = 0
                    if on and not Terminal.IsRushing():
                        while count < 100 and len(Field.GetMobs())>0: #constantly presses control to simulate human actions
                            Key.Down(0x11)
                            time.sleep(0.1)
                            Key.Up(0x11)
                            time.sleep(0.1)
                            count += 1
                            if len(Field.GetMobs())==0:
                                break
    elif job == 2000:#Aran pre
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
        
    elif job == 2100 or job == 2110: #Aran 1st 21000007
        AttackSI(21000006,on,80)
        #AttackSemiNDMagic(21000006,21000006,0.4,on)
            

    elif job == 2111 or job == 2112: #Aran 3rd
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(21111021,21111021,0.81,on)
            #if Character.HasBuff(2,21110016):
            #    AttackSIND(21111021,on,450)
            #else:
            #    AttackSIND(21111021,on,400)
            #AttackSemiNDMagic(21111021,21111021,0.65,on)
            #Terminal.SetCheckBox("Speedy Gonzales",True)
            '''
            elif job == 2110 or job == 2111 or job == 2112: #Aran 2nd+3rd+4th 21000007
                Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
                Key.Set(attack_key,1,21001010)
                Terminal.SetLineEdit("SISkillID","21100018")
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetSpinBox("SkillInjection",30)
                Terminal.SetCheckBox("Auto SP",True)
                Terminal.SetCheckBox("Melee No Delay",on)
                #Terminal.SetRadioButton("SIRadioMagic",True)
                Terminal.SetCheckBox("Auto Attack", False)
                Terminal.SetComboBox("AttackKey",33)
                Terminal.SetSpinBox("autoattack_spin",100)
            '''
    elif job == 14200:# Kinesis 1st
        AttackSemiNDMagic(142001001,142001001,0.63,on,attackSpeed = 5)
    elif job in KinesisJobs and field_id in curbrockhideout:
        AttackAuto(142001001,on)
    elif job == 14210: #Kinesis 2nd 142101002
        AttackSemiNDMagic(142101002,142101002,0.79,on,attackSpeed = 5)
        #AttackAuto(142101002,on)
    elif job == 14211 or job == 14212: #Kinesis 3rd + 4th 142111002
        #
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if job == 14211:
                Terminal.SetCheckBox("Instant Final Smash",True)
            else:
                Terminal.SetCheckBox("Instant Final Smash",False)
            AttackAuto(142111002,on)
            #AttackSemiNDMagic(142101002,142101002,0.79,on,attackSpeed = 5)
        
    elif job == 6500: #AB 1st
        AttackSemiNDMagic(60011216,60011216,0.6,on)
    elif job == 6510: #AB 2nd
        AttackSemiNDMagic(65001100,65001100,0.57,on)
    elif job == 6511: #AB 3rd
        #AttackSI(65111002,on,100,"SIRadioMagic")
        AttackSemiNDMagic(65111002,65111002,1.2,on)
    elif job == 6512: #AB 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if SCLib.GetVar("DoingZakum"):
                AttackSI(65121008,on)
            else:
                AttackSemiNDMagic(65121100,65111002,1.2,on)
    elif job in KaiserJobs and job != KaiserJobs[3]: #Kaiser 1st 2nd 3rd 4th
        AttackSemiNDMagic(61001005,61001005,0.36,on)
    elif job == KaiserJobs[3]:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(61001005,61001005,0.36,on)
    elif job == 2500: #Shade 1st
        AttackAuto(25001000,on)
    elif job == 2510: #Shade 2nd
        AttackSemiNDMagic(25101000,25101000,1.19,on)
    elif job == 2511: #Shade 3rd
        AttackSIND(25110001,on,300)
        #AttackSemiNDMagic(25110001,2511001,0.99,on)
        #AttackSIND(25111000,on,800)
    elif job == 2512: #Shade 4th
        #AttackSI(25120003,on,100)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(25121000) >= 1:
                AttackSemiNDMagic(25121000,25121000,0.63,on)
            else:
                AttackSIND(25110001,on,300)
    elif job == 5100: #Mihile 1st
        AttackAuto(51001004,on)
        #AttackSemiNDMagic(51001004,51001004,0.96,on)
    elif job in MihileJobs and field_id in curbrockhideout:
        AttackAuto(51001004,on)
    elif job == 5110: #Mihile 2nd
        #AttackSIND(51101005,on,800)
        AttackSemiNDMagic(51101005,51001004,0.96,on)
    elif job == 5111: #Mihile 3rd
        AttackSemiNDMagic(51111006,51111006,0.84,on)
        #AttackSIND(51111006,on,600)
    elif job == 5112: #Mihile 4th
        delay = 0.84
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(51121009,51111006,0.84,on)
            #AttackSIND(51121009,on,400)
    else:
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Skill Injection", False)
        #print("Not any of the listed jobs, not going to attack for safety")
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)
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
                        ToggleAttack(True)
                        
                        
                        print("Killing Blazing Imps")
                    else:
                        ToggleAttack(False)
                        toggleKami(False)
                        
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
                ToggleAttack(True)
                toggleKami(True)
                
                toggleNoBossMapEffect(True)
                
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
                        ToggleAttack(False)
                        
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
                        ToggleAttack(True)
                        
                        
                        print("Still some more Blazing imp to kill")
                    else:
                        print("Imps are dead")
                        ToggleAttack(False)
                        
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
                ToggleAttack(True)
                toggleKami(True)
                
                toggleNoBossMapEffect(True)
                
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
                        ToggleAttack(False)
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
                        
                        ToggleAttack(False)

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
                        
                        ToggleAttack(True)
                        
                        print("Need to kill some more Blazing Imps to enter next room")
                    else:
                        ToggleAttack(False)
                        toggleKami(False)
                        
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
                ToggleAttack(True)
                
                toggleNoBossMapEffect(True)
                
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
                        ToggleAttack(False)
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
                            ToggleAttack(False)
                            

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
                        ToggleAttack(True)
                        
                        
                        print("Need to kill som more Pointy imps to enter next map")
                    else:
                        toggleKami(False)
                        ToggleAttack(False)
                        
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
                ToggleAttack(True)
                
                DidSpawn()
                if pos.x != -410:
                    Character.Teleport(-410,434)
                toggleNoBossMapEffect(True)
                
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
                        ToggleMobDisarm(True)
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
                        ToggleAttack(False)
                        ToggleMobDisarm(False)
                        
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
                                
                                ToggleAttack(True)
                                
                                print("Need to kill some more Blazing Imps to enter next room")
                            else:
                                ToggleAttack(False)
                                toggleKami(False)
                                
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
                        ToggleAttack(True)
                        
                        toggleNoBossMapEffect(True)
                        
                        toggleKami(True)
                        print("Fighting boss standby")
                    else:
                        ToggleAttack(False)
                        toggleKami(False)
                        chest = Field.FindMob(8920106)
                        newX = chest.x -30
                        TimeOutCount()
                        if chest.valid:
                            DidSpawn()
                            print("Attacking chest to get the loot")
                            ToggleAttack(False)
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
                                    ToggleAttack(False)
                                    
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
                                ToggleAttack(True)
                                
                                
                                print("Still some more Blazing imp to kill")
                            else:
                                print("Imps are dead")
                                ToggleAttack(False)
                                
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
                        ToggleAttack(True)
                        toggleKami(True)
                        
                        toggleNoBossMapEffect(True)
                        
                        print("Killing Pierre, standby")
                    else:
                        toggleKami(False)
                        ToggleAttack(False)
                        chest = Field.FindMob(8900103)
                        newX = chest.x -50
                        TimeOutCount()
                        if chest.valid:
                            print("Attacking Chest to get loot")
                            DidSpawn()
                            ToggleAttack(False)
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
                                
                                ToggleAttack(False)
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
                                ToggleAttack(True)
                                
                                
                                print("Killing Blazing Imps")
                            else:
                                ToggleAttack(False)
                                toggleKami(False)
                                
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
                        ToggleAttack(True)
                        
                        toggleKami(True)
                        toggleNoBossMapEffect(True)
                        
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
                                ToggleAttack(False)
                                
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
                                ToggleAttack(True)
                                
                                
                                print("Need to kill som more Pointy imps to enter next map")
                            else:
                                toggleKami(False)
                                ToggleAttack(False)
                                
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
                        ToggleAttack(True)
                        
                        DidSpawn() #-410 434
                        if pos.x != boss.x-120:
                            Character.Teleport(boss.x-120,434)
                        toggleNoBossMapEffect(True)
                        
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
                                ToggleAttack(False)
                                
    elif KillZakumDaily == False and (fieldID == TheDoorToZakum or fieldID == EntranceToZakumAlter):
        toggleKami(False)
        toggleHyperTeleportRock(False)
        
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
        ToggleAttack(False)
        
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
                    ToggleAttack(False)
                    
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
                ToggleAttack(True)
                
                if pos.x != -313:
                    Character.Teleport(-313, 84)
                else:
                    print("Fighting Zakum StandBy")
            else:
                if HasSpawned:
                    print("Zakum is dead, waiting 10 sec before continue")
                    toggleKami(False)
                    
                    Terminal.SetCheckBox("Kami Loot",True)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(5)
                    ToggleAttack(False)
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