import os, sys, Terminal, Character, time, GameState, Packet, Npc, Inventory, Field, DataType, Key, Quest

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")


	
#################################################################################################################################################
#																																				#
#							Boldmold @ Gamekillers forums, Be sure to leave a like if you enjoy the script										#
#																																				#
#################################################################################################################################################

#VersionV004.3
#Updated for Maplestory Patch V.197.3.0

#HotKey for pushing updated script while script is active. Enter Virtual-Key Codes (https://docs.microsoft.com/nb-no/windows/desktop/inputdev/virtual-key-codes)
HotKey = 0x7A #F11 Default

#Are you using Hyper teleport rock?
usingHyperTeleportRock = True

#Did you block Opcode "0622" Under Packets/Settings in Terminal? Change to "True" If not then "False"
BlockedBuyHeader	=	False #DO NOT CHANGE THIS VARIABLE, WORKING ON A FIX

#Are you using "Kami Vac"? change to "True" if not then "False"
usingkami		=		True

#What bosses do you want to  do? Change to "True" if not "False"
DoZakumDaily	=		True
DoHilla			=		False
DoHorntail		=		False
DoMagnus		=		False
DoLucid			=		False
DoCrimsonQueen	=		False
DoPierre		=		False
DoVonBon		=		False
DoVellum		=		False
DoGollux		=		False

#What Diff do you want for The Bosses? Change to "True" others to "False"
ZakumEasy		=		False
ZakumNormal		=		True
ZakumChaos		=		False
#-----------------------------
HillaNormal		=		False
HillaHard		=		True
#-----------------------------
HorntailEasy	=		False
HorntailNormal	=		False
HorntailChaos	=		True
#-----------------------------
#MagnusEasy		=		False, To be added
#MagnusNormal	=		False, To be added
MagnusHard		=		False
#-----------------------------
LucidNormal		=		False #Untested, If Intense Power Crystal drops will continue after 20sec. Diddnt have high enough range..
#LucidHard		=		False, Will be added later.. Might take a while
#-----------------------------
CrimsonQueenNormal	=	True
CrimsonQueenChaos	=	False
#-----------------------------
PierreNormal	=		True
PierreChaos		=		False
#-----------------------------
VonBonNormal	=		True
VonBonChaos		=		False
#-----------------------------
VellumNormal	=		True
VellumChaos		=		False
#-----------------------------
#GolluxEasy		=		False	#Kill everything
#GolluxNormal	=		False	#Kill 2 Shoulders
GolluxHard		=		False
GolluxChaos		=		True


#Holy Shit.. I need a GUI..

#########################################################################################################################################
#																																		#
#												Do not change anything below this line!													#
#																																		#
#########################################################################################################################################






#BossesPersistVars
SCLib.PersistVar("KillZakumDaily", DoZakumDaily)
SCLib.PersistVar("KillHilla", DoHilla)
SCLib.PersistVar("KillHorntail", DoHorntail)
SCLib.PersistVar("KillMagnus", DoMagnus)
SCLib.PersistVar("KillLucid", DoLucid)
SCLib.PersistVar("KillCrimsonQueen", DoCrimsonQueen)
SCLib.PersistVar("KillPierre", DoPierre)
SCLib.PersistVar("KillVonBon", DoVonBon)
SCLib.PersistVar("KillVellum", DoVellum)
SCLib.PersistVar("KillGollux", DoGollux)
SCLib.PersistVar("ZakumChaos", ZakumChaos)
SCLib.PersistVar("HasSpawned", False)
SCLib.PersistVar("NowLockedVar", False)
#KannaSkillsPersistVar / Will toggle skills if they are set when script is run
charm_fma = Terminal.GetCheckBox("charm_fma")
MonkeySpiritsNDcheck = Terminal.GetCheckBox("MonkeySpiritsNDcheck")
Summon_Kishin = Terminal.GetCheckBox("Summon Kishin")
SCLib.PersistVar("MonkeySpiritsNDcheck", MonkeySpiritsNDcheck)
SCLib.PersistVar("charm_fma", charm_fma)
SCLib.PersistVar("Summon_Kishin", Summon_Kishin)
SCLib.StartVars(100)

KillZakumDaily = SCLib.GetVar("KillZakumDaily")
ZakumChaos = SCLib.GetVar("ZakumChaos")
KillHilla = SCLib.GetVar("KillHilla")
KillHorntail = SCLib.GetVar("KillHorntail")
KillMagnus = SCLib.GetVar("KillMagnus")
KillLucid = SCLib.GetVar("KillLucid")
KillCrimsonQueen = SCLib.GetVar("KillCrimsonQueen")
KillPierre = SCLib.GetVar("KillPierre")
KillVonBon = SCLib.GetVar("KillVonBon")
KillVellum = SCLib.GetVar("KillVellum")
KillGollux = SCLib.GetVar("KillGollux")
HasSpawned = SCLib.GetVar("HasSpawned")
NowLockedVar = SCLib.GetVar("NowLockedVar")
SCHotkey.StartHotkeys(100)
def KillPersistVarThred():
	SCLib.StopVars()
	time.sleep(1)
SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F11

if GameState.IsInGame() and not Terminal.IsRushing():
	time.sleep(1)

	fieldID = Field.GetID()
	pos = Character.GetPos()
	CurrentChannel = GameState.GetChannel()
	job = Character.GetJob()

	
	#MapID to MapName
	NorthDesertRoad1 = 260020100
	PeakOfTheBigNest = 240040600
	CheifsResidence = 211000001
	TheDoorToZakum = 211042300
	EntranceToEasyZakumsAltar = 211042402
	EasyZakumsAltar = 280030200
	EntranceToZakumAlter = 211042400
	ZakumsAltar = [280030100,280030101]
	EntranceToChaosZakumsAltar = 211042401
	ChaosZakumAltar = 280030000
	AzwanRefugeZone = 262000000
	HillasTowerEntrance = 262030000
	GloomyCorridor1 = 262031100
	GloomyCorridor2 = 262031200
	HillasTower = 262031300
	Corridor1 = 262030100
	Corridor2 = 262030200
	HillasTowerNormal = 262030300
	AzwanObelisk = 262010000
	CaveOfLifeEntrance = 240050000
	EntranceToHorntailsCave = 240050400
	TheCaveOfTrialEasy1 = 240060002
	TheCaveOfTrialEasy2 = 240060102
	TheCaveOfTrialNormal1 = [240060005,240060000]
	TheCaveOfTrialNormal2 = [240060105,240060100]
	HorntailsCaveNormal = [240060200,240060205]
	HorntailsCaveEasy = 240060300
	TryantsCastleSittingRoomEntry = 401053002
	HeliseumHeightsEntry = 401060000
	TyrantsThroneHard = [401060100,401060101]
	NightmareClockTower = 450004000
	DreamingForestNormal = 450004150
	ColossalRoot = 105200000
	SouthGardenNormal = [105200300,105200301,105200302,105200303,105200304,105200305,105200306,105200307,105200308,105200309]
	QueensCastleNormal = [105200310,105200311,105200312,105200313,105200314,105200315,105200316,105200317,105200318,105200319]
	WestGardenNormal = [105200200,105200201,105200202,105200203,105200204,105200205,105200206,105200207,105200208,105200209]
	AfternoonTeaTableNormal = [105200210,105200211,105200212,105200213,105200214,105200215,105200216,105200217,105200218,105200219]
	EastGardenNormal = [105200100,105200101,105200102,105200103,105200104,105200105,105200106,105200107,105200108,105200109]
	TerporalCrevasseNormal = [105200110,105200111,105200112,105200113,105200114,105200115,105200116,105200117,105200118,105200119]
	NorthGardenNormal = [105200400,105200401,105200402,105200403,105200404,105200405,105200406,105200407,105200408,105200409]
	AbyssalCaveNormal = [105200410,105200411,105200412,105200413,105200414,105200415,105200416,105200417,105200418,105200419]
	MemoriesOfTheHeartTree = 863010000
	RoadToGollux = [863010100, 863010101]
	GolluxLowerRightTorso = 863010400
	GolluxUpperRightTorso = 863010410
	GolluxUpperLeftArm = [863010420, 863010420]
	GolluxHeart = 863010500
	GolluxHead = 863010600
	CastleCrimsonChaos = [105200710,105200711,105200712,105200713,105200714,105200715,105200716,105200717,105200718,105200719]
	SouthGardenChaos = [105200700,105200701,105200702,105200703,105200704,105200705,105200706,105200707,105200708,105200709]
	ChaosHorntailsCave = [240060201,240060206]
	TheCaveOfTrialChaos1 = [240060001,240060006]
	TheCaveOfTrialChaos2 = [240060101,240060106]
	NorthGardenChaos = [105200800,105200801,105200802,105200803,105200804,105200805,105200806,105200807,105200808,105200809]
	EastGardenChaos = [105200500,105200501,105200502,105200503,105200504,105200505,105200506,105200507,105200508,105200509]
	WestGardenChaos = [105200600,105200601,105200602,105200603,105200604,105200605,105200606,105200607,105200608,105200609]
	AfternoonTeaTableChaos = [105200610,105200611,105200612,105200613,105200614,105200615,105200616,105200617,105200618,105200619]
	TerporalCrevasseChaos = [105200510,105200511,105200512,105200513,105200514,105200515,105200516,105200517,105200518,105200519]
	AbyssalCaveChaos = [105200810,105200811,105200812,105200813,105200814,105200815,105200816,105200817,105200818,105200819]
	GolluxHeartLoot = 863010700
	CaveOfLifeEntrance1 = 240040700
	TheCaveOfTrials3Zakum = 211042200
	
	#NPC ID to NPC Name
	NpcTylusWarriorInstructor = 2020008
	NpcRobeiraMagicianInstructor = 2020009
	NpcReneBowmanInstructor = 2020010
	NpcArecThiefInstructor = 2020011
	NpcPedroPirateInstructor = 2020013
	EncryptedSlateOfTheSquad = 2083000
	
	#MobNameToMobID
	EasyZakumv1 = 8800021
	EasyZakumv2 = 8800020
	EasyZakum = 8800022
	NormalZakum = 8800002
	NormalZakumv1 = 8800000
	NormalZakumv2 = 8800001
	ChaosZakum = 8800100
	ChaosZakumv1 = 8800101
	ChaosZakumv2 = 8800102
	SilverHairedHilla = 8870100
	NormalHilla = 8870000
	HorntailsLeftHeadEasy = 8810200
	HorntailsRightHeadEasy = 8810201
	HorntailsLeftHeadNormal = 8810000
	HorntailsRightHeadNormal = 8810001
	NormalHorntail = 8810018
	EasyHorntail = 8810214
	HardMagnus = 8880000
	HardMagnusv1 = 8880002
	HardMagnusv2 = 8880010
	DreamingLucidNormal = 8880140
	NormalCrimsonQueen3 = 8920100
	NormalCrimsonQueen2 = 8920101
	NormalCrimsonQueen1 = 8920103
	NormalCrimsonQueen = 8920102
	NormalPierre = 8900100
	NormalPierrev2 = 8900102
	NormalPierrev3 = 8900101
	ChaosPierre = 8900000
	NormalVonBon = 8910100
	ChaosVonBon = 8910000
	NormalVellum = 8930100
	ChaosVellum = 8930000
	GolluxHeadBoss = 9390600
	GolluxEyes = 9390601
	GolluxCrystal = 9390602
	ChaosCrimsonQueen = 8920000
	ChaosCrimsonQueen1 = 8920001
	ChaosCrimsonQueen2 = 8920002
	ChaosCrimsonQueen3 = 8920003
	ChaosCrimsonQueenChest = 8920006
	ChaosHorntail = 8810118
	ChaosHorntail1 = 8810119
	ChaosHorntail2 = 8810120
	ChaosHorntail3 = 8810121
	ChaosHorntail4 = 8810122
	ChaosHorntailsLeftHead = 8810100
	ChaosHorntailsRightHead = 8810101
	
	ElitePikemanSkeleknightNormal = 8870001
	ElitePikemanSkeleKnight = 8870101
	ElitePikemanSkeleKnight2 = 8870102
	ElitePikemanSkeleknightNormal2 = 8870002
	BloodFang = 8870103
	BloodFang2 = 8870104
	BloodFangNormal2 = 8870004
	BloodFangNormal = 8870003
	
	#Jobs
	KannaJobs = [4200, 4210, 4211, 4212]
	
	#Packets that needs updateing every patch
	def KannaSkills(on):
		if job in KannaJobs:
			if SCLib.GetVar("Summon_Kishin"):
				Terminal.SetCheckBox("Summon Kishin", on)
			if SCLib.GetVar("MonkeySpiritsNDcheck"):
				Terminal.SetCheckBox("MonkeySpiritsNDcheck", on)
			if SCLib.GetVar("charm_fma"):
				Terminal.SetCheckBox("charm_fma", on)
	def EnterParty():
		StartParty = Packet.COutPacket(0x01A3) #Header
		StartParty.Encode1(0x01)
		StartParty.Encode1(0x01)
		StartParty.EncodeString("Let's party!")
		Packet.SendPacket(StartParty)
	def EnterNormalBossPacket():
		print("Sending EnterNormal Packet")
		Enter = Packet.COutPacket(0x00EC)
		Enter.EncodeBuffer("[0601] 00000000")
		Packet.SendPacket(Enter)
	def BuyGnarledWoodenKey():
		BuyKey = Packet.COutPacket(0x00ED)
		BuyKey.EncodeBuffer("00 0000 003D8C4B 0001 00000000 000186A0")
		Packet.SendPacket(BuyKey)
		time.sleep(0.5)
		CloseShop = Packet.COutPacket(0x00ED)
		CloseShop.EncodeBuffer("[03]")
		Packet.SendPacket(CloseShop)
		time.sleep(0.5)
	def EnterChaosBossPacket():
		print("Sending EnterChaos Packet")
		Enter = Packet.COutPacket(0x00EC)
		Enter.EncodeBuffer("[0601] 00000001")
		Packet.SendPacket(Enter)
	def InteractCrimsonQueenNormal():
		print("Sending Intreact Packet")
		Interact = Packet.COutPacket(0x03E2)
		Interact.EncodeBuffer("[150E0000]")
		Packet.SendPacket(Interact)
		Interact1 = Packet.COutPacket(0x03E2)
		Interact1.EncodeBuffer("[180E0000]")
		Packet.SendPacket(Interact1)
		InteractReboot = Packet.COutPacket(0x03E2)
		InteractReboot.EncodeBuffer("[FA0D0000]")
		Packet.SendPacket(InteractReboot)
	def InteractCrimsonQueenChaos():
		print("Sending Intreact Packet")
		Interact = Packet.COutPacket(0x03E2)
		Interact.EncodeBuffer("[2B110000]")
		Packet.SendPacket(Interact)
		InteractReboot = Packet.COutPacket(0x03E2)
		InteractReboot.EncodeBuffer("[FA0D0000]")
		Packet.SendPacket(InteractReboot)
	def InteractVonBonNormal():
		print("Sending Interact Packet")
		Interact = Packet.COutPacket(0x03E2)
		Interact.EncodeBuffer("[8E0C0000]")
		Packet.SendPacket(Interact)
		InteractReboot = Packet.COutPacket(0x03E2)
		InteractReboot.EncodeBuffer("[730C0000]")
		Packet.SendPacket(InteractReboot)
	def InteractVonBonChaos():
		print("Sending Interact Packet")
		Interact = Packet.COutPacket(0x03E2)
		Interact.EncodeBuffer("[250F0000]")
		Packet.SendPacket(Interact)
		InteractReboot = Packet.COutPacket(0x03E2)
		InteractReboot.EncodeBuffer("[730C0000]")
		Packet.SendPacket(InteractReboot)
	def InteractVellumNormal():
		print("Sending Interact Packet")
		Interact = Packet.COutPacket(0x03E2)
		Interact.EncodeBuffer("[650E0000]")
		Packet.SendPacket(Interact)
		InteractReboot = Packet.COutPacket(0x03E2)
		InteractReboot.EncodeBuffer("[4A0E0000]")
		Packet.SendPacket(InteractReboot)
	def InteractVellumChaos():
		print("Sending Interact Packet")
		Interact = Packet.COutPacket(0x03E2)
		Interact.EncodeBuffer("[DD110000]")
		Packet.SendPacket(Interact)
		InteractReboot = Packet.COutPacket(0x03E2)
		InteractReboot.EncodeBuffer("[4A0E0000]")
		Packet.SendPacket(InteractReboot)
	def GolluxLootPacket():
		print("Sending Gollux Loot Packet")
		Interact = Packet.COutPacket(0x03E2)
		Interact.EncodeBuffer("[B6E70100]")
		Packet.SendPacket(Interact)
		Interact1 = Packet.COutPacket(0x03E2)
		Interact1.EncodeBuffer("[B5E70100]")
		Packet.SendPacket(Interact1)
	#Define normal functions
	def CheckCompleteStepAndDeliver(questid, questnpc):
		if Quest.CheckCompleteDemand(questid, questnpc) ==0:
			print("Delivering quest {0} at questnpc {1}".format(questid, questnpc))
			Quest.CompleteQuest(questid, questnpc)
	def toggleHyperTeleportRock(on):
		if usingHyperTeleportRock:
			Terminal.SetCheckBox("map/maprusher/hypertelerock", on)
		else:
			Terminal.SetCheckBox("map/maprusher/hypertelerock", False)
	def toggleSI(on):
		Terminal.SetCheckBox("Skill Injection", on)
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
	def toggleNoBossMapEffect(on):
		Terminal.SetCheckBox("No Boss Map Effect", on)
	def togglefullgodmode(on):
		Terminal.SetCheckBox("Full God Mode", on)
	def toggleKami(on):
		if usingkami:
			Terminal.SetCheckBox("Kami Vac", on)
	def togglebossfreeze(on):
		Terminal.SetCheckBox("main/boss_freeze", on)
	def GotoRootAbyss():
		toggleKami(False)
		toggleHyperTeleportRock(True)
		if fieldID != ColossalRoot:
			Terminal.Rush(ColossalRoot)
		else:
			toggleHyperTeleportRock(False)
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
				toggleHyperTeleportRock(False)
	def GotoLucid():
		toggleKami(False)
		toggleHyperTeleportRock(False)
		if fieldID != NightmareClockTower:
			print("Going To Lucid")
			Terminal.Rush(NightmareClockTower)
	def GotoHilla():
		toggleKami(False)
		toggleHyperTeleportRock(True)
		if fieldID != AzwanRefugeZone:
			if fieldID != NorthDesertRoad1:
				Terminal.Rush(NorthDesertRoad1)
			else:
				toggleHyperTeleportRock(False)
				time.sleep(0.5)
				print("Rushing to AzwanRefugeZone")
				Terminal.Rush(AzwanRefugeZone)
		else:
			if pos.x != 840:
				print("Teleporting to portal")
				Character.Teleport(840, 125)
			else:
				if not NowLockedVar:
					EnterParty()
					print("Entering HillasTowerEntrance")
					Npc.ClearSelection()
					Npc.RegisterSelection("Face Hilla herself. (Level 120 and above)")
					time.sleep(1)
					Character.EnterPortal()
					time.sleep(1)
				else:
					print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
					SCLib.UpdateVar("KillHilla", False)
					ResetNowLockedFunction()
	def GotoHorntail():
		toggleKami(False)
		toggleHyperTeleportRock(True)
		print("Going to Horntail")
		if fieldID != CaveOfLifeEntrance:
			if fieldID != PeakOfTheBigNest:
				Terminal.Rush(PeakOfTheBigNest)
			else:
				toggleHyperTeleportRock(False)
				time.sleep(0.5)
				Terminal.Rush(CaveOfLifeEntrance)
		else:
			EnterParty()
			Npc.ClearSelection()
			Character.TalkToNpc(EncryptedSlateOfTheSquad)
	def GotoMagnus():
		toggleKami(False)
		toggleHyperTeleportRock(False)
		print("Going to Magnus")
		if fieldID != HeliseumHeightsEntry:
			if fieldID != TryantsCastleSittingRoomEntry:
				Terminal.Rush(TryantsCastleSittingRoomEntry)
			else:
				if pos.x != -4506:
					Character.Teleport(-4506, 53)
				else:
					Npc.ClearSelection()
					Npc.RegisterSelection("Heliseum Heights Entry (Lv. 155+)")
					time.sleep(1)
					Character.EnterPortal()
					time.sleep(1)
	def GotoGollux():
		toggleHyperTeleportRock(True)
		toggleKami(False)
		print("Going to Gollux, MemoriesOfTheHeartTree")
		if Terminal.GetCheckBox("map/maprusher/hypertelerock"):
			Terminal.Rush(MemoriesOfTheHeartTree)
	#Zakum
	if KillZakumDaily == False and ZakumChaos == False and (fieldID == TheDoorToZakum or fieldID == EntranceToEasyZakumsAltar or fieldID == EntranceToZakumAlter):
		toggleKami(False)
		toggleHyperTeleportRock(False)
		KannaSkills(False)
		if fieldID == TheDoorToZakum:
			if pos.x != -3003:
				Character.Teleport(-3003, -220)
			else:
				Character.EnterPortal()
		elif (fieldID == TheDoorToZakum or fieldID == EntranceToEasyZakumsAltar or fieldID == EntranceToZakumAlter or fieldID == EntranceToChaosZakumsAltar or fieldID == TheCaveOfTrials3Zakum):
			if pos.x != -1599:
				Character.Teleport(-1599, -331)
			else:
				Character.EnterPortal()
	#Hilla			
	elif KillHilla == False and (fieldID == AzwanObelisk or fieldID == AzwanRefugeZone):
		toggleKami(False)
		toggleHyperTeleportRock(False)
		KannaSkills(False)
		if fieldID == AzwanObelisk:
			if pos.x != -674:
				Character.Teleport(-674, 152)
			else:
				Character.EnterPortal()
		elif fieldID == AzwanRefugeZone:
			if pos.x != -857:
				Character.Teleport(-857, 120)
			else:
				Character.EnterPortal()
	#Horntail
	elif KillHorntail == False and (fieldID == EntranceToHorntailsCave or fieldID == CaveOfLifeEntrance or fieldID == CaveOfLifeEntrance1):
		toggleKami(False)
		toggleHyperTeleportRock(False)
		KannaSkills(False)
		if fieldID == EntranceToHorntailsCave:
			Character.TalkToNpc(2083002)
		elif fieldID == CaveOfLifeEntrance:
			if pos.x != -335:
				Character.Teleport(-335, 255)
			else:
				Character.EnterPortal()
		elif fieldID == CaveOfLifeEntrance1:
			if pos.x != -206:
				Character.Teleport(-206, 312)
			else:
				Character.EnterPortal()
	#Zakum
	elif KillZakumDaily:
		toggleKami(False)
		toggleSI(False)
		KannaSkills(False)
		print("Doing Zakum")
		if ZakumEasy:
			print("Easy")
			if fieldID != EasyZakumsAltar:
				if fieldID != EntranceToEasyZakumsAltar:
					if fieldID != TheDoorToZakum:
						GetToTheDoorToZakum()
					elif pos.x != -720:
						NewY = pos.y -5
						Character.Teleport(-720, NewY)
					elif Inventory.GetItemCount(4001796) < 1:
						Npc.ClearSelection()
						Npc.RegisterSelection("Receive an offering for Zakum.")
						time.sleep(1)
						Npc.RegisterSelection("Easy Zakum")
						Character.TalkToNpc(2030008)
						time.sleep(1)
					else:
						print("Entering Portal to EntranceToEasyZakumsAltar")
						Npc.ClearSelection()
						Npc.RegisterSelection("Easy Zakum")
						time.sleep(1)
						Character.EnterPortal()
						time.sleep(1)
				else:
					if not NowLockedVar:
						toggleSI(False)
						print("Sending Packet to make sure we are in a party")
						EnterParty()
						print("Talking to Adobis to enter EasyZakumsAltar")
						Character.TalkToNpc(2030013)
					else:
						print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
						SCLib.UpdateVar("KillZakumDaily", False)
						ResetNowLockedFunction()
			else:
				NowLockedFunction()
				togglebossfreeze(True)
				boss2 = Field.FindMob(EasyZakumv2)
				boss1 = Field.FindMob(EasyZakumv1)
				boss = Field.FindMob(EasyZakum)
				if boss.valid or boss1.valid or boss2.valid:
					toggleSI(True)
					KannaSkills(True)
					DidSpawn()
					if usingkami:
						toggleKami(True)
						print("Fighting Zakum StandBy")
					else:
						if pos.x != -353:
							Character.Teleport(-353, 84)
						else:
							print("Fighting Zakum StandBy")
				else:
					if HasSpawned:
						print("Zakum is dead waiting 10 sec before continue")
						toggleKami(False)
						KannaSkills(False)
						time.sleep(10)
						Character.TalkToNpc(2030010)
						time.sleep(1)
						SCLib.UpdateVar("KillZakumDaily", False)
						ResetSpawn()
						ResetNowLockedFunction()
					else:
						stone = Inventory.FindItemByID(4001796)
						if stone.valid:
							toggleKami(False)
							if pos.x != -25:
								Character.Teleport(-25, 84)
							else:
								print("Dropping stone to spawn Zakum")
								Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)
		elif ZakumNormal:
			print("Normal")
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
						print("Sending Packet to make sure we are in a party")
						EnterParty()
						print("Talking to Adobis to enter ZakumsAltar")
						Character.TalkToNpc(2030013)
					else:
						print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
						SCLib.UpdateVar("KillZakumDaily", False)
						ResetNowLockedFunction()
			else:
				NowLockedFunction()
				togglebossfreeze(True)
				boss2 = Field.FindMob(NormalZakumv2)
				boss1 = Field.FindMob(NormalZakumv1)
				boss = Field.FindMob(NormalZakum)
				if boss.valid or boss1.valid or boss2.valid:
					toggleSI(True)
					KannaSkills(True)
					DidSpawn()
					if usingkami:
						toggleKami(True)
						print("Fighting Zakum StandBy")
					else:
						if pos.x != -353:
							Character.Teleport(-353, 84)
						else:
							print("Fighting Zakum StandBy")
				else:
					if HasSpawned:
						print("Zakum is dead, waiting 10 sec before continue")
						toggleKami(False)
						KannaSkills(False)
						time.sleep(10)
						Character.TalkToNpc(2030010)
						time.sleep(1)
						SCLib.UpdateVar("KillZakumDaily", False)
						ResetSpawn()
						ResetNowLockedFunction()
					else:
						stone = Inventory.FindItemByID(4001017)
						if stone.valid:
							toggleKami(False)
							if pos.x != -25:
								Character.Teleport(-25, 84)
							else:
								print("Dropping stone to spawn Zakum")
								Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)
	#Zakum Chaos
	elif ZakumChaos:
		print("Doing Zakum")
		print("Chaos")
		if fieldID != ChaosZakumAltar:
			if fieldID != EntranceToChaosZakumsAltar:
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
						print("Entering Portal to EntranceToChaosZakumsAltar")
						Npc.ClearSelection()
						Npc.RegisterSelection("Chaos Zakum")
						time.sleep(1)
						Character.EnterPortal()
						time.sleep(1)
			else:
				if not NowLockedVar:
					toggleSI(False)
					KannaSkills(False)
					print("Sending Packet to make sure we are in a party")
					EnterParty()
					print("Talking to Adobis to enter ChaosZakumAltar")
					Character.TalkToNpc(2030013)
				else:
					print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
					SCLib.UpdateVar("ZakumChaos", False)
					ResetNowLockedFunction()
		else:
			NowLockedFunction()
			togglebossfreeze(True)
			boss = Field.FindMob(ChaosZakum)
			boss1 = Field.FindMob(ChaosZakumv1)
			boss2 = Field.FindMob(ChaosZakumv2)
			if boss.valid or boss1.valid or boss2.valid:
				toggleSI(True)
				KannaSkills(True)
				DidSpawn()
				if usingkami:
					toggleKami(True)
					print("Fighting Zakum StandBy")
				else:
					if pos.x != -353:
						Character.Teleport(-353, 84)
					else:
						print("Fighting Zakum StandBy")
			else:
				if HasSpawned:
					print("Zakum is dead waiting 10 sec before continue")
					toggleKami(False)
					KannaSkills(False)
					time.sleep(10)
					Character.TalkToNpc(2030010)
					time.sleep(1)
					SCLib.UpdateVar("ZakumChaos", False)
					ResetSpawn()
					ResetNowLockedFunction()
				else:
					stone = Inventory.FindItemByID(4001017)
					if stone.valid:
						toggleKami(False)
						if pos.x != -25:
							Character.Teleport(-25, 84)
						else:
							print("Dropping stone to spawn Zakum")
							Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)
	#Hilla
	elif KillHilla:
		toggleKami(False)
		toggleSI(False)
		print("Doing Hilla")
		if HillaNormal:
			print("Normal")
			if fieldID != HillasTowerNormal:
				if fieldID != Corridor2:
					if fieldID != Corridor1:
						if fieldID != HillasTowerEntrance:
							print("Going to HillasTowerEntrance")
							GotoHilla()
						else:
							if pos.x != 546:
								Character.Teleport(546, 193)
							else:
								print("Entering Normal Hilla")
								Npc.ClearSelection()
								Npc.RegisterSelection("Normal Mode (Lv. 120+)")
								time.sleep(1)
								Character.EnterPortal()
								time.sleep(1)
					else:
						NowLockedFunction()
						toggleSI(True)
						toggleKami(True)
						togglebossfreeze(True)
						KannaSkills(True)
						mob = Field.FindMob(BloodFangNormal)
						if mob.valid:
							print("Killing BloodFangNormal to enter next room")
						if not mob.valid:
							mob = Field.FindMob(ElitePikemanSkeleknightNormal)
							if mob.valid:
								print("Killing ElitePikemanSkeleknightNormal to enter next room")
							if not mob.valid:
								toggleKami(False)
								print("No more ElitePikemanSkeleknightNormal to kill")
								if pos.x != 1267:
									Character.Teleport(1267, 192)
								else:
									Character.EnterPortal()
				else:
					toggleKami(True)
					toggleSI(True)
					togglebossfreeze(True)
					KannaSkills(True)
					mob = Field.FindMob(BloodFangNormal2)
					if mob.valid:
						print("Killing BloodFangNormal2 to enter next room")
					if not mob.valid:
						mob = Field.FindMob(ElitePikemanSkeleknightNormal2)
						if mob.valid:
							print("Killing ElitePikemanSkeleknightNormal2 to enter next room")
						if not mob.valid:
							toggleKami(False)
							print("No more ElitePikemanSkeleknightNormal2 to kill")
							if pos.x != 1267:
								Character.Teleport(1267, 192)
							else:
								Character.EnterPortal()
			else:
				boss = Field.FindMob(NormalHilla)
				if boss.valid:
					toggleSI(True)
					KannaSkills(True)
					DidSpawn()
					toggleKami(True)
					print("Fighting boss Standby")
				else:
					toggleSI(False)
					KannaSkills(False)
					if HasSpawned:
						toggleKami(False)
						print("HillaNormal Defeated Will continue in 10 sec")
						time.sleep(10)
						if pos.x != -768:
							Character.Teleport(-768, 192)
						else:
							ResetSpawn()
							toggleKami(False)
							time.sleep(0.5)
							Character.EnterPortal()
							time.sleep(1)
							SCLib.UpdateVar("KillHilla", False)
							ResetSpawn()
							ResetNowLockedFunction()
							toggleSI(True)
		elif HillaHard:
			print("Hard")
			if fieldID != HillasTower:
				if fieldID != GloomyCorridor2:
					if fieldID != GloomyCorridor1:
						if fieldID != HillasTowerEntrance:
							print("Going to HillasTowerEntrance")
							GotoHilla()
						else:
							if pos.x != 546:
								toggleKami(False)
								Character.Teleport(546, 193)
							else:
								print("Entering Hard Hilla")
								Npc.ClearSelection()
								Npc.RegisterSelection("Hard Mode (Lv. 170+, Extremely dangerous to solo)")
								time.sleep(1)
								Character.EnterPortal()
								time.sleep(1)
					else:
						NowLockedFunction()
						toggleSI(True)
						toggleKami(True)
						KannaSkills(True)
						togglebossfreeze(True)
						mob1 = Field.FindMob(BloodFang)
						if mob1.valid:
							print("Killing BloodFang to enter next room")
						if not mob1.valid:
							mob2 = Field.FindMob(ElitePikemanSkeleKnight)
							if mob2.valid:
								print("Killing ElitePikemanSkeleKnight to enter next room")
							if not mob2.valid:
								toggleKami(False)
								print("No more ElitePikemanSkeleKnight to kill")
								if pos.x != 1267:
									Character.Teleport(1267, 192)
								else:
									Character.EnterPortal()
				else:
					toggleKami(True)
					toggleSI(True)
					KannaSkills(True)
					mob = Field.FindMob(BloodFang2)
					if mob.valid:
						print("Killing BloodFang2 to enter next room")
					if not mob.valid:
						mob = Field.FindMob(ElitePikemanSkeleKnight2)
						if mob.valid:
							print("Killing ElitePikemanSkeleKnight2 to enter next room")
						if not mob.valid:
							toggleKami(False)
							print("No more ElitePikemanSkeleKnight2 to kill")
							if pos.x != 1267:
								Character.Teleport(1267, 192)
							else:
								Character.EnterPortal()
			else:
				boss = Field.FindMob(SilverHairedHilla)
				if boss.valid:
					toggleSI(True)
					KannaSkills(True)
					DidSpawn()
					toggleKami(True)
					print("Fighting boss Standby")
				else:
					toggleSI(False)
					KannaSkills(False)
					if HasSpawned:
						toggleKami(False)
						print("HillaHard Defeated Will continue in 10 sec")
						time.sleep(10)
						if pos.x != -768:
							Character.Teleport(-768, 192)
						else:
							ResetSpawn()
							time.sleep(0.5)
							Character.EnterPortal()
							time.sleep(1)
							SCLib.UpdateVar("KillHilla", False)
							ResetSpawn()
							ResetNowLockedFunction()
							toggleSI(True)
	#Horntail
	elif KillHorntail:
		HorntailPreQuest = Quest.GetQuestState(7313)
		if HorntailPreQuest == 0:
			print("Horntail Prequest not started or done, Starting quest before entery")
			if fieldID != CaveOfLifeEntrance1:
				Terminal.Rush(CaveOfLifeEntrance1)
			else:
				Quest.StartQuest(7313, 2081006)
				print("Horntail Prequest started")
		else:
			toggleKami(False)
			print("Doing Horntail")
			if HorntailEasy:
				print("Easy")
				if fieldID != HorntailsCaveEasy:
					if fieldID != TheCaveOfTrialEasy2:
						if fieldID != TheCaveOfTrialEasy1:
							if fieldID != EntranceToHorntailsCave:
								GotoHorntail()
							else:
								if not NowLockedVar:
									Npc.ClearSelection()
									Npc.RegisterSelection("Easy Mode (Level 130 or above)")
									time.sleep(1)
									Character.TalkToNpc(2083004)
									time.sleep(1)
								else:
									print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
									SCLib.UpdateVar("KillHorntail", False)
									ResetNowLockedFunction()
						else:
							NowLockedFunction()
							boss = Field.FindMob(HorntailsLeftHeadEasy)
							if boss.valid:
								toggleKami(True)
								KannaSkills(True)
								print("Horntails left head still alive standby")
							else:
								toggleKami(False)
								KannaSkills(False)
								if pos.x != 840:
									Character.Teleport(840, -165)
								else:
									Character.EnterPortal()
					else:
						boss = Field.FindMob(HorntailsRightHeadEasy)
						if boss.valid:
							toggleKami(True)
							KannaSkills(True)
							print("Horntails right head still alive standby")
						else:
							toggleKami(False)
							KannaSkills(False)
							if pos.x != -307:
								Character.Teleport(-307, -165)
							else:
								Character.EnterPortal()
				else:
					boss = Field.FindMob(EasyHorntail)
					if boss.valid:
						toggleSI(True)
						KannaSkills(True)
						DidSpawn()
						toggleKami(True)
						print("Horntail still alive Standby")
					else:
						if HasSpawned:
							toggleKami(False)
							print("Horntail Easy Is dead waiting 10 sec before continueing")
							time.sleep(10)
							Character.TalkToNpc(2083002)
							time.sleep(1)
							SCLib.UpdateVar("KillHorntail", False)
							ResetSpawn()
							ResetNowLockedFunction()
						else:
							toggleKami(False)
							toggleSI(False)
							KannaSkills(False)
							crystal = Field.FindReactor(2401300)
							if crystal.valid:
								if pos.x != 540:
									Character.Teleport(540, 15)
								else:
									Character.BasicAttack()
									time.sleep(2)			
			elif HorntailNormal:
				print("Normal")
				if fieldID not in HorntailsCaveNormal:
					if fieldID not in TheCaveOfTrialNormal2:
						if fieldID not in TheCaveOfTrialNormal1:
							if fieldID != EntranceToHorntailsCave:
								GotoHorntail()
							else:
								if not NowLockedVar:
									Npc.ClearSelection()
									Npc.RegisterSelection("Normal Mode (Level 130 or above)")
									time.sleep(1)
									Character.TalkToNpc(2083004)
									time.sleep(1)
								else:
									print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
									SCLib.UpdateVar("KillHorntail", False)
									ResetNowLockedFunction()
						else:
							NowLockedFunction()
							boss = Field.FindMob(HorntailsLeftHeadNormal)
							if boss.valid:
								toggleKami(True)
								KannaSkills(True)
								print("Horntails left head still alive standby")
							else:
								toggleKami(False)
								KannaSkills(False)
								if pos.x != 840:
									Character.Teleport(840, -165)
								else:
									Character.EnterPortal()
					else:
						boss = Field.FindMob(HorntailsRightHeadNormal)
						if boss.valid:
							toggleKami(True)
							KannaSkills(True)
							print("Horntails right head still alive standby")
						else:
							toggleKami(False)
							KannaSkills(False)
							if pos.x != -307:
								Character.Teleport(-307, -165)
							else:
								Character.EnterPortal()
				else:
					boss = Field.FindMob(NormalHorntail)
					if boss.valid:
						toggleSI(True)
						toggleKami(True)
						KannaSkills(True)
						DidSpawn()
						print("Horntail Normal still alive Standby")
					else:
						if HasSpawned:
							toggleKami(False)
							print("Horntail Normal Is dead waiting 10 sec before continueing")
							time.sleep(10)
							Character.TalkToNpc(2083002)
							time.sleep(1)
							SCLib.UpdateVar("KillHorntail", False)
							ResetSpawn()
							ResetNowLockedFunction()
						else:
							toggleSI(False)
							toggleKami(False)
							KannaSkills(False)
							crystal = Field.FindReactor(2401000)
							if crystal.valid:
								if pos.x != 540:
									Character.Teleport(540, 15)
								else:
									Character.BasicAttack()
									time.sleep(2)
			elif HorntailChaos:
				print("Chaos")
				if fieldID not in ChaosHorntailsCave:
					if fieldID not in TheCaveOfTrialChaos2:
						if fieldID not in TheCaveOfTrialChaos1:
							if fieldID != EntranceToHorntailsCave:
								GotoHorntail()
							else:
								if not NowLockedVar:
									Npc.ClearSelection()
									Npc.RegisterSelection("Chaos Mode (Level 135 or above)")
									time.sleep(1)
									Character.TalkToNpc(2083004)
									time.sleep(1)
								else:
									print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
									SCLib.UpdateVar("KillHorntail", False)
									ResetNowLockedFunction()
						else:
							NowLockedFunction()
							boss = Field.FindMob(ChaosHorntailsLeftHead)
							if boss.valid:
								toggleKami(True)
								KannaSkills(True)
								print("Horntails left head still alive standby")
							else:
								toggleKami(False)
								KannaSkills(False)
								if pos.x != 840:
									Character.Teleport(840, -165)
								else:
									Character.EnterPortal()
					else:
						boss = Field.FindMob(ChaosHorntailsRightHead)
						if boss.valid:
							toggleKami(True)
							KannaSkills(True)
							print("Horntails right head still alive standby")
						else:
							toggleKami(False)
							KannaSkills(False)
							if pos.x != -307:
								Character.Teleport(-307, -165)
							else:
								Character.EnterPortal()
				else:
					boss = Field.FindMob(ChaosHorntail)
					boss1 = Field.FindMob(ChaosHorntail1)
					boss2 = Field.FindMob(ChaosHorntail2)
					boss3 = Field.FindMob(ChaosHorntail3)
					boss4 = Field.FindMob(ChaosHorntail4)
					if boss.valid or boss1.valid or boss2.valid or boss3.valid or boss4.valid:
						toggleSI(True)
						KannaSkills(True)
						toggleKami(True)
						DidSpawn()
						print("Horntail still alive, Standby")
					else:
						if HasSpawned:
							toggleKami(False)
							print("Horntail Is dead waiting 10 sec before continueing")
							time.sleep(10)
							Character.TalkToNpc(2083002)
							time.sleep(1)
							SCLib.UpdateVar("KillHorntail", False)
							ResetSpawn()
							ResetNowLockedFunction()
						else:
							toggleSI(False)
							toggleKami(False)
							KannaSkills(False)
							crystal = Field.FindReactor(2401100)
							if crystal.valid:
								if pos.x != 540:
									Character.Teleport(540, 15)
								else:
									Character.BasicAttack()
									time.sleep(2)
	#Magnus
	elif KillMagnus:
		toggleKami(False)
		if MagnusHard:
			if fieldID not in TyrantsThroneHard:
				if fieldID != HeliseumHeightsEntry:
					GotoMagnus()
				else:
					if not NowLockedVar:
						if pos.x != 1799:
							Character.Teleport(1799, -1433)
						else:
							EnterParty()
							Npc.ClearSelection()
							Npc.RegisterSelection("Tyrant's Throne (Hard Mode, Lv. 175+)")
							time.sleep(1)
							Character.EnterPortal()
							time.sleep(1)
					else:
						print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
						SCLib.UpdateVar("KillMagnus", False)
						ResetNowLockedFunction()
			else:
				NowLockedFunction()
				boss = Field.FindMob(HardMagnus)
				boss1 = Field.FindMob(HardMagnusv1)
				boss2 = Field.FindMob(HardMagnusv2)
				if boss.valid or boss1.valid or boss2.valid:
					DidSpawn()
					togglebossfreeze(True)
					toggleNoBossMapEffect(True)
					toggleSI(True)
					if usingkami:
						toggleKami(True)
						print("Fighting Magnus standby")
					else:
						newX = boss.x + 100
						print("Fighting Magnus stand by")
						if pos.x != newX:
							Character.Teleport(newX, -1350)
							print("Moving into safe area")
							time.sleep(5)
						else:
							print("We are in the safe area, Checking position again in 5 sec")
				else:
					if HasSpawned:
						toggleKami(False)
						print("Hard Magnus is dead, Waiting 20sec before continuing")
						time.sleep(20)
						if pos.x != 1480:
							Character.Teleport(595, -1350)
						else:
							Character.EnterPortal()
							time.sleep(0.5)
							Character.EnterPortal()
							time.sleep(2)
							SCLib.UpdateVar("KillMagnus", False)
							ResetSpawn()
							ResetNowLockedFunction()
					else:
						KannaSkills(False)
						toggleSI(False)
	#Lucid
	elif KillLucid:
		print("Doing Lucid")
		toggleKami(False)
		if LucidNormal:
			if fieldID != DreamingForestNormal:
				if fieldID != NightmareClockTower:
					GotoLucid()
				else:
					if not NowLockedVar:
						Npc.ClearSelection()
						print("Entering Lucid Normal")
						Npc.RegisterSelection("Go fight Lucid.")
						Npc.RegisterSelection("Request to enter <Boss: Lucid (Normal)>.")
						time.sleep(1)
						Character.TalkToNpc(3003208)
						time.sleep(1)
					else:
						print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
						SCLib.UpdateVar("KillLucid", False)
						ResetNowLockedFunction()
			else:
				NowLockedFunction()
				boss = Field.FindMob(DreamingLucidNormal)
				if boss.valid:
					togglebossfreeze(True)
					toggleNoBossMapEffect(True)
					toggleKami(True)
					print("Fighting lucid standby")
				else:
					loot = Field.FindItem(4001886)
					if loot.valid:
						toggleKami(False)
						print("Lucid is dead, waiting 20 sec to continue")
						time.sleep(20)
						if pos.x != 22:
							Character.Teleport(22,46)
						else:
							Character.EnterPortal()						
	#CrimsonQueen
	elif KillCrimsonQueen:
		print("Doing Crimson Queen")
		toggleKami(False)
		if CrimsonQueenNormal:
			print("Normal")
			if CurrentChannel != 20:
				print("Change to Channel 20")
				Terminal.ChangeChannel(20)
			else:
				if fieldID not in QueensCastleNormal:
					if fieldID not in SouthGardenNormal:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != -776:
								Character.Teleport(-776, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
									if BlockedBuyHeader:
										Character.TalkToNpc(1064004)
										time.sleep(0.5)
										BuyGnarledWoodenKey()
									else:
										print("You Dont have a key to enter RootAbyss, Make sure to buy them in advance or Block (061E) Header in the Packets section")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterNormalBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120110)
							if mob.valid:
								toggleKami(True)
								KannaSkills(True)
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
						if chest.valid:
							DidSpawn()
							print("Attacking chest to get the loot")
							if pos.x != newX:
								Character.Teleport(newX, 130)
							else:
								Character.BasicAttack()
								time.sleep(5)
						else:
							if HasSpawned:
								print("CrimsonQueen and Chest Has been killed waiting 10 sec before continue")
								toggleKami(False)
								time.sleep(10)
								if pos.x != -849:
									Character.Teleport(-849, 132)
								else:
									Character.EnterPortal()
									time.sleep(0.5)
									Character.EnterPortal()
									time.sleep(1)
									SCLib.UpdateVar("KillCrimsonQueen", False)
									ResetSpawn()
									ResetNowLockedFunction()
							else:
								InteractCrimsonQueenNormal()
								KannaSkills(False)
								toggleSI(False)
		elif CrimsonQueenChaos:
			print("Chaos")
			if CurrentChannel != 15:
				print("Change to Channel 15")
				Terminal.ChangeChannel(15)
			else:
				if fieldID not in CastleCrimsonChaos:
					if fieldID not in SouthGardenChaos:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != -776:
								Character.Teleport(-776, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterChaosBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120112)
							if mob.valid:
								toggleKami(True)
								KannaSkills(True)
								toggleSI(True)
								print("Need to kill some more Blazing Imps to enter next room")
							else:
								toggleKami(False)
								toggleSI(False)
								KannaSkills(False)
								if pos.x != 1835:
									Character.Teleport(1835, 259)
								else:
									Character.EnterPortal()
						else:
							print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
							SCLib.UpdateVar("KillCrimsonQueen", False)
							ResetNowLockedFunction()
				else:
					NowLockedFunction()
					boss = Field.FindMob(ChaosCrimsonQueen)
					boss1 = Field.FindMob(ChaosCrimsonQueen1)
					boss2 = Field.FindMob(ChaosCrimsonQueen2)
					boss3 = Field.FindMob(ChaosCrimsonQueen3)
					if boss.valid or boss1.valid or boss2.valid or boss3.valid:
						toggleNoBossMapEffect(True)
						togglebossfreeze(True)
						toggleKami(True)
						KannaSkills(True)
						print("Fighting boss standby")
					else:	
						chest = Field.FindMob(ChaosCrimsonQueenChest)
						newX = chest.x -30
						if chest.valid:
							DidSpawn()
							print("Attacking chest to get the loot")
							if pos.x != newX:
								Character.Teleport(newX, 130)
							else:
								Character.BasicAttack()
								time.sleep(5)
						else:
							if HasSpawned:
								print("CrimsonQueen i dead and Chest Has been looted waiting 10 sec before continue")
								toggleKami(False)
								time.sleep(10)
								if pos.x != -849:
									Character.Teleport(-849, 132)
								else:
									Character.EnterPortal()
									time.sleep(0.5)
									Character.EnterPortal()
									time.sleep(1)
									SCLib.UpdateVar("KillCrimsonQueen", False)
									ResetSpawn()
									ResetNowLockedFunction()
							else:
								InteractCrimsonQueenChaos()
								KannaSkills(False)
								toggleSI(False)
	#Pierre
	elif KillPierre:
		print("Doing Pierre")
		toggleKami(False)
		if PierreNormal:
			print("Normal")
			if CurrentChannel != 20:
				print("Change to Channel 20")
				Terminal.ChangeChannel(20)
			else:
				if fieldID not in AfternoonTeaTableNormal:
					if fieldID not in WestGardenNormal:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != -288:
								Character.Teleport(-288, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
									if BlockedBuyHeader:
										Character.TalkToNpc(1064004)
										time.sleep(0.5)
										BuyGnarledWoodenKey()
									else:
										print("You Dont have a key to enter RootAbyss, Make sure to buy them in advance or Block (061E) Header in the Packets section")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterNormalBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120110)
							if mob.valid:
								toggleKami(True)
								toggleSI(True)
								KannaSkills(True)
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
						chest = Field.FindMob(8900103)
						newX = chest.x -50
						if chest.valid:
							print("Attacking Chest to get loot")
							DidSpawn()
							if pos.x != newX:
								Character.Teleport(newX, 550)
							else:
								Character.BasicAttack()
								time.sleep(7)
						else:
							if HasSpawned:
								print("PierreNormal and chest has been killed waiting 10 sec before continue")
								time.sleep(10)
								if pos.x != -382:
									print("Moving into position to enter portal")
									Character.Teleport(-382, 550)
								else:
									print("Entering portal")
									Character.EnterPortal()
									time.sleep(0.5)
									Character.EnterPortal()
									time.sleep(2)
									SCLib.UpdateVar("KillPierre", False)
									ResetSpawn()
									ResetNowLockedFunction()
							else:
								KannaSkills(False)
								toggleSI(False)
		elif PierreChaos:
			print("Chaos")
			if CurrentChannel != 15:
				print("Change to Channel 15")
				Terminal.ChangeChannel(15)
			else:
				if fieldID not in AfternoonTeaTableChaos:
					if fieldID not in WestGardenChaos:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != -288:
								Character.Teleport(-288, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
									if BlockedBuyHeader:
										Character.TalkToNpc(1064004)
										time.sleep(0.5)
										BuyGnarledWoodenKey()
									else:
										print("You Dont have a key to enter RootAbyss, Make sure to buy them in advance or Block (061E) Header in the Packets section")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterChaosBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120112)
							if mob.valid:
								toggleKami(True)
								toggleSI(True)
								KannaSkills(True)
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
					boss1 = Field.FindMob(ChaosPierre)
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
						chest = Field.FindMob(8900003)
						newX = chest.x -50
						if chest.valid:
							print("Attacking Chest to get loot")
							DidSpawn()
							if pos.x != newX:
								Character.Teleport(newX, 550)
							else:
								Character.BasicAttack()
								time.sleep(7)
						else:
							if HasSpawned:
								print("PierreNormal and chest has been killed waiting 10 sec before continue")
								time.sleep(10)
								if pos.x != -382:
									print("Moving into position to enter portal")
									Character.Teleport(-382, 550)
								else:
									print("Entering portal")
									Character.EnterPortal()
									time.sleep(0.5)
									Character.EnterPortal()
									time.sleep(2)
									SCLib.UpdateVar("KillPierre", False)
									ResetSpawn()
									ResetNowLockedFunction()
							else:
								KannaSkills(False)
								toggleSI(False)
	#VonBon
	elif KillVonBon:
		print("Doing Von Bon")
		toggleKami(False)
		if VonBonNormal:
			print("Normal")
			if CurrentChannel != 20:
				print("Change to Channel 20")
				Terminal.ChangeChannel(20)
			else:
				if fieldID not in TerporalCrevasseNormal:
					if fieldID not in EastGardenNormal:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != 245:
								Character.Teleport(245, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
									if BlockedBuyHeader:
										Character.TalkToNpc(1064004)
										time.sleep(0.5)
										BuyGnarledWoodenKey()
									else:
										print("You Dont have a key to enter RootAbyss, Make sure to buy them in advance or Block (061E) Header in the Packets section")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterNormalBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120110)
							if mob.valid:
								toggleKami(True)
								toggleSI(True)
								KannaSkills(True)
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
							print("VonBon is dead, Waiting 10 sec before continue")
							time.sleep(10)
							if pos.x != -1090:
								Character.Teleport(-1090, 453)
							else:
								Character.EnterPortal()
								time.sleep(0.5)
								Character.EnterPortal()
								time.sleep(1)
								SCLib.UpdateVar("KillVonBon", False)
								ResetSpawn()
								ResetNowLockedFunction()
						else:
							InteractVonBonNormal()
							toggleSI(False)
							KannaSkills(False)
		elif VonBonChaos:
			print("Chaos")
			if CurrentChannel != 15:
				print("Change to Channel 15")
				Terminal.ChangeChannel(15)
			else:
				if fieldID not in TerporalCrevasseChaos:
					if fieldID not in EastGardenChaos:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != 245:
								Character.Teleport(245, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
									if BlockedBuyHeader:
										Character.TalkToNpc(1064004)
										time.sleep(0.5)
										BuyGnarledWoodenKey()
									else:
										print("You Dont have a key to enter RootAbyss, Make sure to buy them in advance or Block (061E) Header in the Packets section")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterChaosBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120112)
							if mob.valid:
								toggleKami(True)
								toggleSI(True)
								KannaSkills(True)
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
					boss = Field.FindMob(ChaosVonBon)
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
							print("VonBon is dead, Waiting 10 sec before continue")
							time.sleep(10)
							if pos.x != -1090:
								Character.Teleport(-1090, 453)
							else:
								Character.EnterPortal()
								time.sleep(0.5)
								Character.EnterPortal()
								time.sleep(1)
								SCLib.UpdateVar("KillVonBon", False)
								ResetSpawn()
								ResetNowLockedFunction()
						else:
							InteractVonBonChaos()
							toggleSI(False)
							KannaSkills(False)
	#Vellum
	elif KillVellum:
		print("Doing Vellum")
		toggleKami(False)
		if VellumNormal:
			print("Normal")
			if CurrentChannel != 20:
				print("Change to Channel 20")
				Terminal.ChangeChannel(20)
			else:
				if fieldID not in AbyssalCaveNormal:
					if fieldID not in NorthGardenNormal:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != 732:
								Character.Teleport(732, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
									if BlockedBuyHeader:
										Character.TalkToNpc(1064004)
										time.sleep(0.5)
										BuyGnarledWoodenKey()
									else:
										print("You Dont have a key to enter RootAbyss, Make sure to buy them in advance or Block (061E) Header in the Packets section")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterNormalBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120111)
							if mob.valid:
								toggleKami(True)
								toggleSI(True)
								KannaSkills(True)
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
						toggleKami(True)
						toggleNoBossMapEffect(True)
						togglebossfreeze(True)
						print("Killin Vallum Standby")
					else:
						if HasSpawned:
							toggleKami(False)
							print("Vallum is dead, waiting 10 sec before continue")
							time.sleep(10)
							if pos.x != -1758:
								Character.Teleport(-1758, 440)
							else:
								Character.EnterPortal()
								time.sleep(0.5)
								Character.EnterPortal()
								time.sleep(1)
								SCLib.UpdateVar("KillVellum", False)
								ResetSpawn()
								ResetNowLockedFunction()
						else:
							InteractVellumNormal()
							KannaSkills(False)
							toggleSI(False)
		elif VellumChaos:
			print("Chaos")
			if CurrentChannel != 15:
				print("Change to Channel 15")
				Terminal.ChangeChannel(15)
			else:
				if fieldID not in AbyssalCaveChaos:
					if fieldID not in NorthGardenChaos:
						if fieldID != ColossalRoot:
							GotoRootAbyss()
						else:
							if pos.x != 732:
								Character.Teleport(732, 213)
							else:
								if Inventory.GetItemCount(4033611) < 1:
									print("Missing Gnarled Wooden Key")
									if BlockedBuyHeader:
										Character.TalkToNpc(1064004)
										time.sleep(0.5)
										BuyGnarledWoodenKey()
									else:
										print("You Dont have a key to enter RootAbyss, Make sure to buy them in advance or Block (061E) Header in the Packets section")
								else:
									EnterParty()
									Character.EnterPortal()
									EnterChaosBossPacket()
					else:
						if not NowLockedVar:
							mob = Field.FindMob(7120113)
							if mob.valid:
								toggleKami(True)
								toggleSI(True)
								KannaSkills(True)
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
					boss = Field.FindMob(ChaosVellum)
					if boss.valid:
						toggleSI(True)
						KannaSkills(True)
						DidSpawn()
						toggleKami(True)
						toggleNoBossMapEffect(True)
						togglebossfreeze(True)
						print("Killin Vallum Standby")
					else:
						if HasSpawned:
							toggleKami(False)
							print("Vallum is dead, waiting 10 sec before continue")
							time.sleep(10)
							if pos.x != -1758:
								Character.Teleport(-1758, 440)
							else:
								Character.EnterPortal()
								time.sleep(0.5)
								Character.EnterPortal()
								time.sleep(1)
								SCLib.UpdateVar("KillVellum", False)
								ResetSpawn()
								ResetNowLockedFunction()
						else:
							InteractVellumChaos()
							KannaSkills(False)
							toggleSI(False)
	#Gollux
	elif KillGollux:
		print("Doing Gollux")
		toggleKami(False)
		if fieldID != GolluxHeartLoot:
			if fieldID != GolluxHead:
				if fieldID != GolluxHeart:
					if fieldID not in GolluxUpperLeftArm:
						if fieldID != GolluxUpperRightTorso:
							if fieldID != GolluxLowerRightTorso:
								if fieldID not in RoadToGollux:
									if fieldID != MemoriesOfTheHeartTree:
										GotoGollux()
									else:
										if not NowLockedVar:
											if Inventory.GetItemCount(4033981) < 1:
												print("Missing Key, Talkto Guardian")
												Npc.ClearSelection()
												Npc.RegisterSelection("[Gollux] The Face of Fear")
												time.sleep(1)
												Character.TalkToNpc(9390120)
												time.sleep(1)
											else:
												if pos.x != -508:
													Character.Teleport(-508, -47)
												else:
													EnterParty()
													Character.EnterPortal()
													EnterNormalBossPacket()
										else:
											print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
											SCLib.UpdateVar("KillGollux", False)
											ResetNowLockedFunction()
								else:
									if GolluxChaos:
										if  Inventory.GetItemCount(2432091) < 1:
											print("Missing Gollux Head Teleport")
										else:
											Inventory.UseItem(2432091)
											time.sleep(2)
									else: 
										if pos.x != 1947:
											Character.Teleport(1947, -352)
										else:
											Character.EnterPortal()
							else:
								NowLockedFunction()
								mob1 = Field.FindMob(9390640)
								mob2 = Field.FindMob(9390632)
								if mob1.valid or mob2.valid:
									toggleKami(True)
									print("Need to kill the mobs to continue, standby")
								else:
									time.sleep(2)
									toggleKami(False)
									if pos.x != -1011:
										Character.Teleport(-1011, -356)
									else:
										Character.EnterPortal()
						else:
							mob1 = Field.FindMob(9390640)
							mob2 = Field.FindMob(9390632)
							if mob1.valid or mob2.valid:
								toggleKami(True)
								print("Need to kill the mobs to continue, standby")
							else:
								time.sleep(2)
								toggleKami(False)
								if pos.x != -127:
									Character.Teleport(-127, -441)
								else:
									Character.EnterPortal()
					else:
						mob1 = Field.FindMob(9390638)
						mob2 = Field.FindMob(9390631)
						if mob1.valid or mob2.valid:
							toggleKami(True)
							print("Need to kill the mobs to continue, standby")
						else:
							time.sleep(2)
							toggleKami(False)
							if pos.x != -522:
								Character.Teleport(-522, 130)
							else:
								Character.EnterPortal()
				else:
					if pos.x != 95:
						Character.Teleport(95, 72)
					else:
						Character.EnterPortal()
			else:
				NowLockedFunction()
				boss1 = Field.FindMob(GolluxEyes)
				boss = Field.FindMob(GolluxHeadBoss)
				boss2 = Field.FindMob(GolluxCrystal)
				if boss.valid or boss1.valid or boss2.valid:
					toggleKami(True)
					print("Killing boss standby")
				else:
					print("Gollux is dead waiting for next map to loot")
					time.sleep(20)
		else:
			print("In loot map")
			if Terminal.GetCheckBox("Pet Item Teleport"):
				Terminal.SetCheckBox("Pet Item Teleport", False)
			toggleKami(False)
			loot = Field.FindItem(4310097) #Gollux coin
			if loot.valid:
				DidSpawn()
				if not Terminal.GetCheckBox("Pet Item Teleport"):
					Terminal.SetCheckBox("Pet Item Teleport", True)
				print("Intense Gollux coin dropped, Will continue in 10 sec")
			else:
				if HasSpawned:
					time.sleep(10)
					if pos.x != 97:
						print("Teleporting to exit portal")
						Character.Teleport(97, 232)
					else:
						print("Entering Exit portal")
						Character.EnterPortal()
						time.sleep(2)
						ResetNowLockedFunction()
						ResetSpawn()
						SCLib.UpdateVar("KillGollux", False)
				else:
					print("Getting into position to send interaction packet")
					if pos.x != 90:
						Character.Teleport(90, 72)
					else:
						GolluxLootPacket()
		
	else:
		if fieldID != 100000000:
			toggleHyperTeleportRock(True)
			toggleKami(False)
			print("All bosses have been defeated! Returning to Henesys and deliver daily quests")
			Terminal.Rush(100000000)
		else:
			q1 = Quest.GetQuestState(26430) #ZakumNormal
			q2 = Quest.GetQuestState(26525) #VonBonNormal
			q3 = Quest.GetQuestState(26526) #PierreNormal
			q4 = Quest.GetQuestState(26527) #CrimsonQueenNormal
			q5 = Quest.GetQuestState(26528) #VellumNormal
			q6 = Quest.GetQuestState(26436) #Horntail Chaos
			q7 = Quest.GetQuestState(26433) #HillaHard
			q8 = Quest.GetQuestState(5870)
			q9 = Quest.GetQuestState(26435) #Zakum Chaos
			q10 = Quest.GetQuestState(26442) #Magnus Hard
			q11 = Quest.GetQuestState(26531) #Crimson Queen Chaos
			q12 = Quest.GetQuestState(26530) #Pierre Chaos
			q13 = Quest.GetQuestState(26529) #VonBon Chaos
			q14 = Quest.GetQuestState(26532) #Vellum Chaos
			
			if q1 != 2:
				CheckCompleteStepAndDeliver(26430, 9030200) #ZakumNormal
			elif q2 != 2:
				CheckCompleteStepAndDeliver(26525, 9030200) #VonBonNormal
			elif q3 != 2:
				CheckCompleteStepAndDeliver(26526, 9030200) #PierreNormal
			elif q4 != 2:
				CheckCompleteStepAndDeliver(26527, 9030200) #CrimsonQueenNormal
			elif q5 != 2:
				CheckCompleteStepAndDeliver(26528, 9030200) #VellumNormal
			elif q6 != 2:
				CheckCompleteStepAndDeliver(26436, 9030200) #HorntailChaos
			elif q7 != 2:
				CheckCompleteStepAndDeliver(26433, 9030200) #HillaHard
			elif q8 != 2:
				CheckCompleteStepAndDeliver(5870, 9030200) 
			elif q9 != 2:
				CheckCompleteStepAndDeliver(26435, 9030200) #Zakum Chaos
			elif q10 != 2:
				CheckCompleteStepAndDeliver(26442, 9030200) #Magnus Hard
			elif q11 != 2:
				CheckCompleteStepAndDeliver(26531, 9030200) #Crimson Queen Chaos
			elif q12 != 2:
				CheckCompleteStepAndDeliver(26530, 9030200) #Pierre Chaos
			elif q13 != 2:
				CheckCompleteStepAndDeliver(26529, 9030200) #VonBon Chaos
