import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCLib
except:
	print("Couldn't find SunCat module")

isHardMode = True
usingParty = True
	
kamiOffsetX = -100
kamiOffsetY = -50

#Don't touch these
startingMap = 450002023
exitMap = 450002024
hungryMutoMaps = [921170050, 921170100, 921170101, 921170102, 921170103, 921170104, 921170105]
allIngredients = []
allRecipes = []

currentRecipe = None

class Ingredient:
	name = ""
	mobID = 0
	itemID = 0
	
	def __init__(self, nm, mid, iid):
		self.name = nm
		if isHardMode:
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
		#SunCat.KamiTP(1398, 115)
		#time.sleep(2)
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

def InitAll():
	if Field.GetID() == startingMap:
		print('Starting...')
		SunCat.HookChuChu()
		InitRecipes()
		
		Terminal.SetCheckBox("Auto NPC", True)
		
		changeChannel()
		
		if usingParty:
			time.sleep(10)
		
		retryCount = 0
		
		tryAgain = True
		
		while tryAgain:
			if retryCount > 3:
				print("Failed to enter ChuChu, have you already done it 3 times?")
				break
			Npc.ClearSelection()
			Npc.RegisterSelection("Enter <Hungry Muto>")
			if isHardMode:
				Npc.RegisterSelection("Hard")
			else:
				Npc.RegisterSelection("Normal")
			Character.TalkToNpc(3003166)
			time.sleep(5)
			
			if Field.GetID() == startingMap:
				print("Creating a new party...")
				leaveParty()
				createParty()
				retryCount += 1
				time.sleep(1)
			elif Field.GetID() in hungryMutoMaps:
				print("Starting ChuChuPQ!")
				tryAgain = False
				DoChuChu()
			else:
				tryAgain = False
				print("Not in ChuChuPQ!")
				SunCat.UnhookChuChu()
	else:
		print("Not in ChuChu Entry Map!")
		
def DoChuChu():
	dcExit = False
	
	while Field.GetID() != exitMap:
		currentRecipe = allRecipes[SunCat.GetRecipe()]
		print("Doing Recipe: " + currentRecipe.name)
		for i in range(len(currentRecipe.ingredients)):
			print("Getting " + str(currentRecipe.amounts[i]) + "x " + currentRecipe.ingredients[i].name)
			currentRecipe.ingredients[i].GetIngredient(currentRecipe.amounts[i])
		
		if GameState.IsInGame() == False:
			dcExit = True
			break
		time.sleep(3)
	
	if dcExit == False:
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
		time.sleep(5)
	else:
		SunCat.StopTP()
		SunCat.UnhookChuChu()
		print("You either disconnected or crashed, PQ didn't complete properly")
			
if SCLib.CheckVersion(20):
	if GameState.IsInGame():
		InitAll()
	else:
		print('Not in game!')
