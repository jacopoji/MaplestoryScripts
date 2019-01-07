import os, sys, Field, Terminal, Quest, Npc, Inventory, Packet, GameState, time, DataType, Character, Key

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")

#SunCat's All-in-one Dailies

#Change these
#--------------------------------------------------
dailyVJ = True
dailyChuChu = True
dailyDD = False
dailySS = True

kamiOffsetX = -100
kamiOffsetY = -50

#ChuChu
chuChuHardMode = True

#Dream Defender
ddLevelSelect = 30 #This is the stage you will enter
ddExitLevel = 31 #This is the stage you will exit

#Spirit Savior
npcChatKey = 0x20 #NPC chat key (default spacebar)
killTime = 1.2 #How long it takes you to kill the mob (can be set to a fraction)
waitTime = 0.5 #How long to wait after killing before picking up (for lag reasons)
roundWaitTime = 0.5 #How long to wait when handing in spirits
roundsPerRun = 15 #How many times you want to collect 5 spirits per run
totalRuns = 1 #How many times you want to enter spirit savior

#--------------------------------------------------

#Don't touch anything below this
#--------------------------------------------------

symbolMaxTries = 20

#Vanishing Journey
vjQuests = []

vjMap = 450001000
vjNPC = 3003104

#ChuChu
ccStartingMap = 450002023
ccExitMap = 450002024
ccNpc = 3003166
hungryMutoMaps = [921170050, 921170100, 921170101, 921170102, 921170103, 921170104, 921170105]
allIngredients = []
allRecipes = []
currentRecipe = None

#Dream Defender
ddStartingMap = 450004000
ddMap = 921171000
ddMapEnd = 921171099
ddExitMap = 921171100
ddNpc = 9010100
ddPurpleBoxes = [9833080, 9833081, 9833082, 9833083, 9833084]
#ddYellowBox = 9833072
#ddFilterMobs = [9833090, 9833091]
ddRestX = 3400
ddRestY = -650

#Spirit Savior
ssStartingMap = 450005000
ssExitMap = 921172400
ssMapStart = 921172300
ssMapEnd = 921172399
ssMobArray = [8644101, 8644102, 8644103, 8644104, 8644105, 8644106, 8644107, 8644108, 8644109, 8644110, 8644111, 8644112]
ssBaseX = -175
ssBaseY = -491
ssNpc = 3003381
enemyMobs = [8644201, 8644301, 8644302, 8644303, 8644304, 8644305]

def initVars():
	SCLib.PersistVar("StartingMap", Field.GetID())
	SCLib.PersistVar("UsingKami", Terminal.GetCheckBox("Kami Vac"))
	SCLib.PersistVar("UsingSI", Terminal.GetCheckBox("Skill Injection"))
	SCLib.PersistVar("UsingFMA", Terminal.GetCheckBox("Full Map Attack"))
	SCLib.PersistVar("UsingGFMA", Terminal.GetCheckBox("General FMA"))
	SCLib.PersistVar("UsingWhitelist", Terminal.GetPushButton("Whitelist"))
	SCLib.PersistVar("UsingAutoBuff", Terminal.GetCheckBox("Auto Buff"))
	SCLib.PersistVar("CurDaily", "VJ")
	SCLib.PersistVar("CurQuest", None)
	SCLib.PersistVar("SymbolCount", 0)
	SCLib.PersistVar("CurSSRuns", 0)
	
	SCLib.PersistVar("CurStep", "StartingVJ")

	SCLib.PersistVar("RetryCount", 0)

	SCLib.StartVars()

def useSymbol(symbol):
	if symbol.valid and SCLib.GetVar("SymbolCount") < symbolMaxTries:
		oPacket = Packet.COutPacket(SCLib.PacketHeader["Symbols"])
		oPacket.Encode4(0x00000000)
		oPacket.Encode4(symbol.pos) #inv slot
		oPacket.Encode4(0xFFFFF9BB) #???
		Packet.SendPacket(oPacket)
		SCLib.UpdateVar("SymbolCount", SCLib.GetVar("SymbolCount") + 1)
		return True
	else:
		SCLib.UpdateVar("SymbolCount", 0)
		return False

class VJQuest:
	quest = None
	killmap = None
	completemap = None
	npc = None
	npcx = None
	npcy = None
	
	def __init__(self, q, km, cm=vjMap, n=vjNPC, snx=-1941, sny=60):
		self.quest = q
		self.killmap = km
		self.completemap = cm
		self.npc = n
		self.npcx = snx
		self.npcy = sny
		
	def IsActive(self):
		if Quest.GetQuestState(self.quest) == 1:
			return True
		return False
	
	def DoQuest(self):		
		if Quest.GetQuestState(self.quest) == 1:
			curMap = Field.GetID()
			SCLib.UpdateVar("CurQuest", self.quest)
			if Quest.CheckCompleteDemand(self.quest, self.npc):
				if curMap != self.killmap:
					Terminal.Rush(self.killmap)
			else:
				if curMap != self.completemap:
					Terminal.Rush(self.completemap)
				else:
					if Terminal.GetCheckBox("Kami Vac"):
						Terminal.SetCheckBox("Kami Vac", False)
					
					SunCat.Teleport(self.npcx, self.npcy)
					time.sleep(1)
					Quest.CompleteQuest(self.quest, self.npc)
					time.sleep(2)
					if SCLib.GetVar("UsingKami"):
						Terminal.SetCheckBox("Kami Vac", True)
					
					SCLib.UpdateVar("CurQuest", None)
					
def initVJ():
	vjQuests.append(VJQuest(34130, 450001010))
	vjQuests.append(VJQuest(34131, 450001012))
	vjQuests.append(VJQuest(34132, 450001014))
	vjQuests.append(VJQuest(34133, 450001016))
	vjQuests.append(VJQuest(34134, 450001110))
	vjQuests.append(VJQuest(34135, 450001112))
	vjQuests.append(VJQuest(34136, 450001114))
	vjQuests.append(VJQuest(34137, 450001210))
	vjQuests.append(VJQuest(34138, 450001210))
	vjQuests.append(VJQuest(34139, 450001010))
	vjQuests.append(VJQuest(34140, 450001012))
	vjQuests.append(VJQuest(34141, 450001014))
	vjQuests.append(VJQuest(34142, 450001016))
	vjQuests.append(VJQuest(34143, 450001110))
	vjQuests.append(VJQuest(34144, 450001112))
	vjQuests.append(VJQuest(34145, 450001114))
	vjQuests.append(VJQuest(34146, 450001210))
	vjQuests.append(VJQuest(34147, 450001210))
	vjQuests.append(VJQuest(34148, 450001013, 450001013, 3003107, 991, -898))
	vjQuests.append(VJQuest(34149, 450001112, 450001112, 3003108, 74, -710))
	vjQuests.append(VJQuest(34150, 450001216, 450001216, 3003109, -1079, -149))

def acceptVJ():
	curMap = Field.GetID()
	if curMap != vjMap:
		Terminal.Rush(vjMap)
		return

	if Terminal.GetCheckBox("Kami Vac"):
		Terminal.SetCheckBox("Kami Vac", False)
	
	Terminal.SetCheckBox("Auto NPC", True)
	SunCat.Teleport(-1941, 60)
	time.sleep(0.1)
	#Quest.StartQuest(34128, vjNPC)
	
	Npc.ClearSelection()
	#Npc.RegisterSelection("[Daily Quest] Vanishing Journey")
	Npc.RegisterSelection("Those are all")
	time.sleep(3)
	Quest.StartQuest(34129, vjNPC)
	time.sleep(3)
	#Character.TalkToNpc(vjNPC)
	#time.sleep(1)
	
	if SCLib.GetVar("UsingKami"):
		Terminal.SetCheckBox("Kami Vac", True)
		
	SCLib.UpdateVar("CurStep", "DoingVJ")
	
def doVJ():
	if dailyVJ:
		initVJ()
		
		counter = -1
		
		if SCLib.GetVar("CurStep") == "StartingVJ":
			print("Starting Vanishing Journey")
			acceptVJ()
		elif SCLib.GetVar("CurStep") == "DoingVJ":
			counter = 0
			for q in vjQuests:
				if q.IsActive():
					counter += 1
				
				if SCLib.GetVar("CurQuest") == None or SCLib.GetVar("CurQuest") == q.quest:
					q.DoQuest()
			if counter == 0:
				SCLib.UpdateVar("CurStep", "FinishedVJ")
		elif SCLib.GetVar("CurStep") == "FinishedVJ":
			print("Finishing VJ")
			if not Quest.CheckCompleteDemand(34129, vjNPC):
				Quest.CompleteQuest(34129, vjNPC)

			vjSymbol = Inventory.FindItemByID(1712001)
			if not useSymbol(vjSymbol):
				print("Finished VJ")
				SCLib.UpdateVar("CurDaily", "ChuChu")
				SCLib.UpdateVar("CurStep", "InitChuChu")
		
	else:
		print("Skipping VJ")
		SCLib.UpdateVar("CurDaily", "ChuChu")
		SCLib.UpdateVar("CurStep", "InitChuChu")
		
#ChuChu
class Ingredient:
	name = ""
	mobID = 0
	itemID = 0
	
	def __init__(self, nm, mid, iid):
		self.name = nm
		if chuChuHardMode:
			self.mobID = mid
		else:
			self.mobID = mid - 20
		self.itemID = iid
	
	def GetMob(self):
		mobCheck = Field.FindMob(self.mobID)
		if mobCheck.valid:
			return mobCheck
		
		return None
	
	def GetDrop(self):
		dropCheck = Field.FindItem(self.itemID)
		if dropCheck.valid:
			return dropCheck
			
		return None
	
	def HandIn(self):
		hiPacket = Packet.COutPacket(SCLib.PacketHeader["ChuChu"])
		hiPacket.Encode1(0x02)
		hiPacket.EncodeString("pt_mutoHotPot")
		hiPacket.EncodeBuffer("0592 0093")
		Packet.SendPacket(hiPacket)
		time.sleep(2)
	
	def GetIngredient(self, amount):
		curAmount = 0
		firstAmount = SunCat.GetChuChu()
		
		while curAmount < amount:
			if Field.GetID() not in hungryMutoMaps or GameState.IsInGame() == False:
				break
			curAmount = SunCat.GetChuChu()
			if curAmount == firstAmount:
				curAmount = 0
			
			curDrop = self.GetDrop()
			if curDrop is not None:
				if self.name == "Slurpy Fruit":
					while self.GetDrop() is not None:
						if Field.GetID() not in hungryMutoMaps or GameState.IsInGame() == False:
							break
						SunCat.KamiTP(curDrop.x, curDrop.y)
						Character.LootItem()
						time.sleep(0.1)
				else:
					SunCat.KamiTP(curDrop.x, curDrop.y)
					Character.LootItem()
			else:
				curMob = self.GetMob()
				if curMob is not None:
					SunCat.KamiTP(curMob.x + kamiOffsetX, curMob.y + kamiOffsetY)
			
			time.sleep(0.1)
		
		self.HandIn()

class Recipe:
	name = ""
	ingredients = []
	amounts = []
	
	def __init__(self, nm, igs, amts):
		self.name = nm
		self.ingredients = igs
		self.amounts = amts

def InitIngredients():
	allIngredients.append(Ingredient("Savory Fin", 9833054, 2435864))
	allIngredients.append(Ingredient("Tart Fins", 9833062, 2435865))
	allIngredients.append(Ingredient("Fresh Mane", 9833052, 2435860))
	allIngredients.append(Ingredient("Zesty Mane", 9833060, 2435861))
	allIngredients.append(Ingredient("Sweet Hoof", 9833050, 2435856))
	allIngredients.append(Ingredient("Spicy Hoof", 9833058, 2435857))
	allIngredients.append(Ingredient("Slimy Feather", 9833056, 2435868))
	allIngredients.append(Ingredient("Sticky Feather", 9833064, 2435869))
	allIngredients.append(Ingredient("Unpleasant Talon", 9833057, 2435870))
	allIngredients.append(Ingredient("Chewy Talon", 9833065, 2435871))
	allIngredients.append(Ingredient("Greasy Peel", 9833051, 2435858))
	allIngredients.append(Ingredient("Sour Peel", 9833059, 2435859))
	allIngredients.append(Ingredient("Crunchy Shell", 9833055, 2435866))
	allIngredients.append(Ingredient("Soft Shell", 9833063, 2435867))
	allIngredients.append(Ingredient("Soft Sole", 9833053, 2435862))
	allIngredients.append(Ingredient("Chewy Sole", 9833061, 2435863))
	allIngredients.append(Ingredient("Slurpy Fruit", 9833066, 2435872))
		
def InitRecipes():
	InitIngredients()
	
	#Easy Mobs
	allRecipes.append(Recipe("Fried Treat", [allIngredients[4], allIngredients[2]], [5, 10]))
	allRecipes.append(Recipe("Savory Stir Fry", [allIngredients[10], allIngredients[14]], [5, 10]))
	allRecipes.append(Recipe("Nummy Noodles", [allIngredients[4], allIngredients[2], allIngredients[0]], [5, 5, 10]))
	allRecipes.append(Recipe("Steamy Surprise", [allIngredients[10], allIngredients[14], allIngredients[12]], [5, 5, 10]))
	allRecipes.append(Recipe("Weird Wrap", [allIngredients[2], allIngredients[0], allIngredients[6]], [5, 5, 10]))
	allRecipes.append(Recipe("Gamey Soup", [allIngredients[0], allIngredients[12], allIngredients[8]], [5, 5, 10]))
	allRecipes.append(Recipe("Mystery Roast", [allIngredients[10], allIngredients[14], allIngredients[6], allIngredients[16]], [5, 5, 10, 1]))
	allRecipes.append(Recipe("Mystery Roast", [allIngredients[2], allIngredients[12], allIngredients[8], allIngredients[16]], [5, 5, 10, 1]))
	
	#Hard Mobs
	allRecipes.append(Recipe("Fried Squish", [allIngredients[5], allIngredients[3]], [5, 10]))
	allRecipes.append(Recipe("Dumpling Delights", [allIngredients[11], allIngredients[15]], [5, 10]))
	allRecipes.append(Recipe("Funky Pizza", [allIngredients[5], allIngredients[3], allIngredients[1]], [5, 5, 10]))
	allRecipes.append(Recipe("Juicy Buns", [allIngredients[11], allIngredients[15], allIngredients[13]], [5, 5, 10]))
	allRecipes.append(Recipe("Yucky Pickles", [allIngredients[3], allIngredients[1], allIngredients[7]], [5, 5, 10]))
	allRecipes.append(Recipe("Chewy Porridge", [allIngredients[1], allIngredients[13], allIngredients[9]], [5, 5, 10]))
	allRecipes.append(Recipe("Fruit Salad", [allIngredients[11], allIngredients[15], allIngredients[7], allIngredients[16]], [5, 5, 10, 1]))
	allRecipes.append(Recipe("Spicy Sausage", [allIngredients[3], allIngredients[13], allIngredients[9], allIngredients[16]], [5, 5, 10, 1]))
	
def changeChannel():
	print("Changing channel, please wait...")
	curChannel = GameState.GetChannel()
	
	while curChannel == GameState.GetChannel():
		Terminal.ChangeChannel(0)
		time.sleep(8)

def createParty():
	cpPacket = Packet.COutPacket(SCLib.PacketHeader["Party"])
	cpPacket.EncodeBuffer("01 00 10 00 42 65 73 74 20 70 61 72 74 79 20 65 76 65 72 21")
	Packet.SendPacket(cpPacket)

def leaveParty():
	lpPacket = Packet.COutPacket(SCLib.PacketHeader["Party"])
	lpPacket.EncodeBuffer("02 00")
	Packet.SendPacket(lpPacket)
	
def initChuChu():
	if Field.GetID() != ccStartingMap:
		Terminal.Rush(ccStartingMap)
	else:
		SunCat.HookChuChu()
		
		Terminal.SetCheckBox("Auto NPC", True)
		Terminal.SetCheckBox("Kami Vac", False)
		Terminal.SetCheckBox("Full Map Attack", False)
		Terminal.SetCheckBox("General FMA", False)
		Terminal.SetPushButton("Whitelist", False)
		
		changeChannel()
		
		SCLib.UpdateVar("CurStep", "StartingChuChu")

def startChuChu():
	if Field.GetID() != ccStartingMap:
		SCLib.UpdateVar("CurStep", "InitChuChu")
	else:
		retryCount = SCLib.GetVar("RetryCount")
		
		if retryCount > 3:
			SCLib.UpdateVar("RetryCount", 0)
			print("Finished ChuChu")
			SCLib.UpdateVar("CurStep", "FinishedChuChu")
			SunCat.UnhookChuChu()
		else:
			Npc.ClearSelection()
			Npc.RegisterSelection("Enter <Hungry Muto>")
			if chuChuHardMode:
				Npc.RegisterSelection("Hard")
			else:
				Npc.RegisterSelection("Normal")
			Character.TalkToNpc(ccNpc)
			time.sleep(5)
			
			if Field.GetID() == ccStartingMap:
				print("Failed to enter ChuChu, creating a new party...")
				leaveParty()
				createParty()
				SCLib.UpdateVar("RetryCount", retryCount + 1)
				time.sleep(1)
			elif Field.GetID() in hungryMutoMaps:
				print("Starting ChuChuPQ!")
				SCLib.UpdateVar("CurStep", "DoingChuChu")

def doingChuChu():
	if Field.GetID() != ccExitMap:
		currentRecipe = allRecipes[SunCat.GetRecipe()]
		for i in range(len(currentRecipe.ingredients)):
			print("Getting " + str(currentRecipe.amounts[i]) + "x " + currentRecipe.ingredients[i].name)
			currentRecipe.ingredients[i].GetIngredient(currentRecipe.amounts[i])
		
	else:
		time.sleep(0.5)
		SunCat.KamiTP(528, 138)
		time.sleep(0.5)
		SunCat.StopTP()
		SunCat.UnhookChuChu()
		Npc.ClearSelection()
		Npc.RegisterSelection("Claim")
		Character.TalkToNpc(3003166)
		time.sleep(1)
		print("Done! Sleeping for a few seconds to check for another run...")
		SCLib.UpdateVar("CurStep", "InitChuChu")
		time.sleep(5)

def finishChuChu():
	chuchuSymbol = Inventory.FindItemByID(1712002)
	if not useSymbol(chuchuSymbol):
		if SCLib.GetVar("UsingWhitelist"):
			Terminal.SetPushButton("Whitelist", True)
		SCLib.UpdateVar("CurDaily", "DD")
		SCLib.UpdateVar("CurStep", "StartingDD")
		
def doChuChu():
	if dailyChuChu:
		InitRecipes()
		
		if SCLib.GetVar("CurStep") == "InitChuChu":
			initChuChu()
		elif SCLib.GetVar("CurStep") == "StartingChuChu":
			startChuChu()
		elif SCLib.GetVar("CurStep") == "DoingChuChu":
			doingChuChu()
		elif SCLib.GetVar("CurStep") == "FinishedChuChu":
			finishChuChu()
	else:
		SCLib.UpdateVar("CurDaily", "DD")
		SCLib.UpdateVar("CurStep", "InitDD")
		
#Dream Defender
def initDD():
	if Field.GetID() != ddStartingMap:
		Terminal.Rush(ddStartingMap)
	else:		
		leaveParty()
		
		SunCat.HookDD()
		
		Terminal.SetCheckBox("Auto NPC", True)
		Terminal.SetCheckBox("Kami Vac", False)
		Terminal.SetCheckBox("Full Map Attack", False)
		Terminal.SetCheckBox("General FMA", False)
		
		#for mob in ddFilterMobs:
			#SunCat.FilterMob(mob)
			
		#SunCat.FilterMob(ddYellowBox)
		
		Npc.ClearSelection()
		Npc.RegisterSelection("Attempt")
		Npc.RegisterSelection(str(ddLevelSelect))
		time.sleep(2)
		Character.TalkToNpc(ddNpc)
		time.sleep(3)
		
		SCLib.UpdateVar("CurStep", "StartingDD")

def retreatDD():
	rPacket = Packet.COutPacket(SCLib.PacketHeader["RetreatDD"])
	rPacket.EncodeBuffer("[01000000]")
	Packet.SendPacket(rPacket)
		
def startDD():
	if Field.GetID() >= ddMap and Field.GetID() <= ddMapEnd:
		curStage = SunCat.GetDDStage()
		if curStage >= ddExitLevel:
			SunCat.StopTP()
			retreatDD()
			time.sleep(4)
		else:
			boxFound = False
			for box in ddPurpleBoxes:
				curBox = Field.FindMob(box)
				if curBox.valid:
					boxFound = True
					if SCLib.GetVar("UsingSI"):
						Terminal.SetCheckBox("Skill Injection", True)
					SunCat.KamiTP(curBox.x + kamiOffsetX, curBox.y + kamiOffsetY)
					break
		if boxFound == False:
			Terminal.SetCheckBox("Skill Injection", False)
			SunCat.KamiTP(ddRestX, ddRestY)
	elif Field.GetID() == ddExitMap:
		SunCat.StopTP()
		#SunCat.UnfilterMobs()
		Character.TalkToNpc(ddNpc)
	else:
		if SCLib.GetVar("RetryCount") < 3:
			print("Failed to enter DD... Retrying")
			SCLib.UpdateVar("RetryCount", SCLib.GetVar("RetryCount") + 1)
			SCLib.UpdateVar("CurStep", "InitDD")
		else:
			print("Finished DD")
			SunCat.UnhookDD()
			SCLib.UpdateVar("CurStep", "InitSS")
			SCLib.UpdateVar("CurDaily", "SS")
			SCLib.UpdateVar("RetryCount", 0)

def doDD():
	if dailyDD:
		if SCLib.GetVar("CurStep") == "InitDD":
			initDD()
		elif SCLib.GetVar("CurStep") == "StartingDD":
			startDD()
	else:
		SCLib.UpdateVar("CurDaily", "SS")
		SCLib.UpdateVar("CurStep", "InitSS")
	
#Spirit Savior
def inSS():
	return Field.GetID() >= ssMapStart and Field.GetID() <= ssMapEnd
	
def initSS():
	if Field.GetID() != ssStartingMap:
		Terminal.Rush(ssStartingMap)
	else:
		SunCat.Teleport(0, 139)
		
		leaveParty()
		
		Terminal.SetCheckBox("Auto NPC", True)
		Terminal.SetCheckBox("Kami Vac", False)
		Terminal.SetCheckBox("Full Map Attack", False)
		Terminal.SetCheckBox("General FMA", False)
		Terminal.SetCheckBox("Auto Buff", False)
		
		for mob in enemyMobs:
			SunCat.FilterMob(mob)
		
		Npc.ClearSelection()
		Npc.RegisterSelection("Attempt")
		Character.TalkToNpc(ssNpc)
		time.sleep(3)
		
		SCLib.UpdateVar("CurStep", "StartingSS")

def runSS():
	for i in range(roundsPerRun):
		killCount = 0
		
		mobsKilled = []
		
		while killCount < 5:
			if not GameState.IsInGame() or not inSS():
				print("Not in SS!")
				break

			curMob = None
			
			for mobID in ssMobArray:
				mob = Field.FindMob(mobID)
				if mob.valid and mob not in mobsKilled:
					curMob = mob
					mobsKilled.append(mob)
					break
			
			if curMob is not None:
				SunCat.KamiTP(curMob.x, curMob.y)
				time.sleep(killTime)
				Key.Press(npcChatKey)
				time.sleep(0.2)
				Key.Press(npcChatKey)
				time.sleep(waitTime)
				killCount += 1
			else:
				print("No mobs left!")
				time.sleep(3) #Wait for mobs to respawn - this should never be hit
		
		SunCat.KamiTP(ssBaseX, ssBaseY)
		time.sleep(roundWaitTime)
		
	SCLib.UpdateVar("CurSSRuns", SCLib.GetVar("CurSSRuns") + 1)
	SCLib.UpdateVar("CurStep", "FinishingSS")

def finishSS():
	if Field.GetID() == ssExitMap:
		Character.TalkToNpc(ssNpc)
		
		SunCat.StopTP()
		SunCat.UnfilterMobs()
		SCLib.UpdateVar("CurStep", "InitSS")
		time.sleep(5)

	
def startSS():
	if inSS():
		SCLib.UpdateVar("CurStep", "RunSS")
	else:
		if SCLib.GetVar("RetryCount") < 3 and SCLib.GetVar("CurSSRuns") < totalRuns:
			print("Failed to enter SS... Retrying")
			SCLib.UpdateVar("RetryCount", SCLib.GetVar("RetryCount") + 1)
			SCLib.UpdateVar("CurStep", "InitSS")
		else:
			print("Finished SS")
			SCLib.UpdateVar("CurDaily", "Return")
			SCLib.UpdateVar("RetryCount", 0)
	
def doSS():
	if dailySS:
		if SCLib.GetVar("CurStep") == "InitSS":
			initSS()
		elif SCLib.GetVar("CurStep") == "StartingSS":
			startSS()
		elif SCLib.GetVar("CurStep") == "RunSS":
			runSS()
		elif SCLib.GetVar("CurStep") == "FinishingSS":
			finishSS()
	else:
		SCLib.UpdateVar("CurDaily", "Return")
		SCLib.UpdateVar("RetryCount", 0)

if not Terminal.IsRushing():
	if SCLib.CheckVersion(22):
		initVars()
		curDaily = SCLib.GetVar("CurDaily")
		if GameState.IsInGame():
			if curDaily == "VJ":
				doVJ()
			elif curDaily == "ChuChu":
				doChuChu()
			elif curDaily == "DD":
				doDD()
			elif curDaily == "SS":
				doSS()
			elif curDaily == "Return":
				SCLib.UpdateVar("CurDaily", None)
				SCLib.UpdateVar("CurStep", "StartingVJ")
				print("Done! Back to botting...")
				if SCLib.GetVar("UsingKami"):
					Terminal.SetCheckBox("Kami Vac", True)
				if SCLib.GetVar("UsingSI"):
					Terminal.SetCheckBox("Skill Injection", True)
				if SCLib.GetVar("UsingFMA"):
					Terminal.SetCheckBox("Full Map Attack", True)
				if SCLib.GetVar("UsingGFMA"):
					Terminal.SetCheckBox("General FMA", True)
				if SCLib.GetVar("UsingAutoBuff"):
					Terminal.SetCheckBox("Auto Buff", True)
				
				Terminal.Rush(SCLib.GetVar("StartingMap"))
			else:
				SCLib.StartVars(5)
		else:
			#Handle all d/c's
			if SCLib.GetVar("CurStep") == "DoingChuChu":
				if Field.GetID() == ccExitMap:
					Character.TalkToNpc(3003166)
					time.sleep(5)
					SCLib.SetVar("CurStep", "InitChuChu")