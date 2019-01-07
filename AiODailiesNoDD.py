# Arcane River Daily AiO v1.0
# 8/19/2018
# Credits: @SunCat @wbhmaybe @tave @mehodin
##########################################################################
# Set Daily quest to True whichver you like to have
VJ_Daily = True
ChuChu_Daily = True
DreamDefender_Daily = False
SpiritSavior_Daily = True

HotKey = 0x79
# VJ Configuration 
# set it to True if you like to have Nobody Allows evasion during VJ daily, otherwise False to use default evasion reaction
nobody_evasion = True


# Chuchu Configuration
isHardMode = True
kamiOffsetX = -100
kamiOffsetY = -50


# Dream defender Configuration
UseAA = False  # Set True if you want to use auto attack during Dream defender
UseSI = True  # Set True if you want to use SI during Dream defender


# Spirit Savior Configuration
npcChatKey = 0x20 #NPC chat key (default spacebar)
killTime = 1.2 #How long it takes you to kill the mob (can be set to a fraction)
waitTime = 0.5 #How long to wait after killing before picking up (for lag reasons)
roundWaitTime = 0.5 #How long to wait when handing in spirits
roundsPerRun = 15 #How many times you want to collect 5 spirits per run

##########################################################################
# DO NOT TOUCH BELOW
print("Starting Arcane River AiO script")

import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal, Context, Inventory, Key, Quest, Party
if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCLib, SCHotkey
except:
	print("Couldn't find SunCat module")
##########################
# Initial setup
##########################

SCLib.StartVars()
if SCLib.GetVar("ChuchuDone") is None:
    SCLib.PersistVar("ChuchuDone", False)
if SCLib.GetVar("DreamDone") is None:
    SCLib.PersistVar("DreamDone", False)
if SCLib.GetVar("SpiritDone") is None:
    SCLib.PersistVar("SpiritDone", False)
if SCLib.GetVar("DDCoinDone") is None:
    SCLib.PersistVar("DDCoinDone", False)
if SCLib.GetVar("DDCoin") is None:
    SCLib.PersistVar("DDCoin", Inventory.GetItemCount(4310227))
if SCLib.GetVar("SpiritCoin") is None:
    SCLib.PersistVar("SpiritCoin", Inventory.GetItemCount(4310235))
if SCLib.GetVar("defaultEva") is None:
    SCLib.PersistVar("defaultEva", Terminal.GetComboBox("HackingOpt"))
    
options = ['General FMA', 'Full Map Attack', 'Grenade Kami', 'Mob Falldown', 'Kami Vac', 'bot/kanna_kami', 'bot/si_no_wait', 'Skill Injection', 'Auto Attack']
for option in options:
    if SCLib.GetVar(option) is None:
        SCLib.PersistVar(option, Terminal.GetCheckBox(option))
    else:
        SCLib.UpdateVar(option, Terminal.GetCheckBox(option))

SCHotkey.StartHotkeys(100)
def KillPersistVarThred():
	print("Restarting SCLib variables")
	SCLib.StopVars()
	time.sleep(1)

SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F10

# check quest states
if Quest.GetQuestState(34120) != 2:
    print("You havn't completed VJ storyline quests yet. Disable VJ daily")
    VJ_Daily = False
if Quest.GetQuestState(34218) != 2:
    print("You havn't completed ChuChu storyline quests yet. Disable Chuchu daily")
    ChuChu_Daily = False
if Quest.GetQuestState(34330) != 2:
    print("You havn't completed Lachelein storyline quests yet. Disable Dream Defender daily")
    DreamDefender_Daily = False
if Quest.GetQuestState(34479) != 2:
    print("You havn't completed Arcana storyline quests yet. Disable Sirit Savior daily")
    SpiritSavior_Daily = False

Terminal.SetCheckBox("Rush By Level",False)

def RestoreSetting():
    print("restore terminal setting")
    for option in options:
        Terminal.SetCheckBox(option, SCLib.GetVar(option))

def Rush(mapid):
    if Terminal.IsRushing():
        time.sleep(1)
    elif Field.GetID() != mapid:
        time.sleep(1)
        Terminal.Rush(mapid)
##########################
# VJ daily
##########################
def RushCheck(ID): #define RushCheck to first check if you're in the map
	if map != ID: #if you're not in the map rush to the map
		Terminal.Rush(ID)
	else:
		time.sleep(1) #if you are, do nothing and check again in a second to not stress CPU <3
		
def RushAndComplete(completemap, questid, npcid):
    if map != completemap:
        Terminal.Rush(completemap)
    else:
        if completemap == 450001000:
            ToPortal("PV00", False)
            Quest.CompleteQuest(questid, npcid)
        else:
            ToNPC(npcid)
            Quest.CompleteQuest(questid, npcid)

def ToPortal(portal, enter=True):
    portal = Field.FindPortal(portal)
    if portal.valid:
        if not (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5):
            SunCat.Teleport(portal.x, portal.y-5)
            time.sleep(1)
            if enter:
                Character.EnterPortal()
                time.sleep(1)
        elif enter:
            time.sleep(1)
            Character.EnterPortal()

def ToNPC(npc):
    npc = Field.FindNpc(npc)
    if npc.valid:
        if not (Character.GetPos().x < npc.x+5 and Character.GetPos().x > npc.x-5):
            SunCat.Teleport(npc.x, npc.y-10)
    time.sleep(1)

def NobodyAllows():
    if Terminal.GetComboBox("HackingOpt") != 0:
        Terminal.SetComboBox("HackingOpt", 0)

def RestoreEvasion():
    Terminal.SetComboBox("HackingOpt", SCLib.GetVar("defaultEva"))
        
        
if VJ_Daily and Quest.GetQuestState(34129)!=2:
    print("Starting VJ daily")
    
while VJ_Daily and Quest.GetQuestState(34129)!=2:
    if GameState.IsInGame() and Quest.GetQuestState(34129)==0:
        if Field.GetID() != 450001000:
            RushCheck(450001000)
        else:
            ToPortal("PV00", False)
        
        Npc.ClearSelection()
        Npc.RegisterSelection("Those are all the quests I want to swap out")
        time.sleep(2)
        Quest.StartQuest(34129, 3003104)
        time.sleep(2)
        
    elif GameState.IsInGame() and Quest.GetQuestState(34129)==1:
        if nobody_evasion:
            NobodyAllows()

        map = Field.GetID()	
        time.sleep(1) #no stress CPU please
        daily0 = Quest.GetQuestState(34129)
        daily1 = Quest.GetQuestState(34130)
        daily2 = Quest.GetQuestState(34131)
        daily3 = Quest.GetQuestState(34132)
        daily4 = Quest.GetQuestState(34133)
        daily5 = Quest.GetQuestState(34134)
        daily6 = Quest.GetQuestState(34135)
        daily7 = Quest.GetQuestState(34136)
        daily8 = Quest.GetQuestState(34137)
        daily9 = Quest.GetQuestState(34138)
        daily10 = Quest.GetQuestState(34139)
        daily11 = Quest.GetQuestState(34140)
        daily12 = Quest.GetQuestState(34141)
        daily13 = Quest.GetQuestState(34142)
        daily14 = Quest.GetQuestState(34143)
        daily15 = Quest.GetQuestState(34144)
        daily16 = Quest.GetQuestState(34145)
        daily17 = Quest.GetQuestState(34146)
        daily18 = Quest.GetQuestState(34147)
        daily19 = Quest.GetQuestState(34148)
        daily20 = Quest.GetQuestState(34149)
        daily21 = Quest.GetQuestState(34150)
        if not Terminal.GetCheckBox("Kami Vac"):
            job = Character.GetJob()
            if job != 4212 and job != 15512:
                Terminal.SetCheckBox("Kami Vac", True)
        if Terminal.IsRushing():
            time.sleep(1)
            #loops so we can use statements like break and continue

        elif daily1 == 1: #if daily quest 1 is active
            if Quest.CheckCompleteDemand(34130, 3003104) == False: #if demand is met and can be turned in
                RushAndComplete(450001000, 34130, 3003104)
            else:#isn't ready to turn in
                RushCheck(450001010) #check if current map is killing map, if not rush there, check def above.
                
        elif daily2 == 1:
            if Quest.CheckCompleteDemand(34131, 3003104) == False:
                RushAndComplete(450001000, 34131, 3003104)
            else:
                RushCheck(450001012)
                        
        elif daily3 == 1:
            if Quest.CheckCompleteDemand(34132, 3003104) == False:
                RushAndComplete(450001000, 34132, 3003104)
            else:
                RushCheck(450001014)                

        elif daily4 == 1:
            if Quest.CheckCompleteDemand(34133, 3003104) == False:
                RushAndComplete(450001000, 34133, 3003104)	
            else:
                RushCheck(450001016)

        elif daily5 == 1:
            if Quest.CheckCompleteDemand(34134, 3003104) == False:
                RushAndComplete(450001000, 34134, 3003104)
            else:
                RushCheck(450001110)
                        
        elif daily6 == 1:
            if Quest.CheckCompleteDemand(34135, 3003104) == False:
                RushAndComplete(450001000, 34135, 3003104)
            else:
                RushCheck(450001112)		
            
        elif daily7 == 1:
            if Quest.CheckCompleteDemand(34136, 3003104) == False:
                RushAndComplete(450001000, 34136, 3003104)
            else:
                RushCheck(450001114)

        elif daily8 == 1:
            if Quest.CheckCompleteDemand(34137, 3003104) == False:
                RushAndComplete(450001000, 34137, 3003104)
            else:
                RushCheck(450001210)

        elif daily9 == 1:
            if Quest.CheckCompleteDemand(34138, 3003104) == False:
                RushAndComplete(450001000, 34138, 3003104)
            else:
                RushCheck(450001210)

        elif daily10 == 1:
            if Quest.CheckCompleteDemand(34139, 3003104) == False:
                RushAndComplete(450001000, 34139, 3003104)
            else:
                RushCheck(450001010)

        elif daily11 == 1:
            if Quest.CheckCompleteDemand(34140, 3003104) == False:
                RushAndComplete(450001000, 34140, 3003104)
            else:
                RushCheck(450001012)

        elif daily12 == 1:
            if Quest.CheckCompleteDemand(34141, 3003104) == False:
                RushAndComplete(450001000, 34141, 3003104)
            else:
                RushCheck(450001014)

        elif daily13 == 1:
            if Quest.CheckCompleteDemand(34142, 3003104) == False:
                RushAndComplete(450001000, 34142, 3003104)
            else:
                RushCheck(450001016)
                        
                        
        elif daily14 == 1:
            if Quest.CheckCompleteDemand(34143, 3003104) == False:
                RushAndComplete(450001000, 34143, 3003104)
            else:
                RushCheck(450001110)
                        
        elif daily15 == 1:
            if Quest.CheckCompleteDemand(34144, 3003104) == False:
                RushAndComplete(450001000, 34144, 3003104)
            else:
                RushCheck(450001112)
                
        elif daily16 == 1:
            if Quest.CheckCompleteDemand(34145, 3003104) == False:
                RushAndComplete(450001000, 34145, 3003104)
            else:
                RushCheck(450001114)
                
        elif daily17 == 1:
            if Quest.CheckCompleteDemand(34146, 3003104) == False:
                RushAndComplete(450001000, 34146, 3003104)
            else:
                RushCheck(450001210)
                        
        elif daily18 == 1:
            if Quest.CheckCompleteDemand(34147, 3003104) == False:
                RushAndComplete(450001000, 34147, 3003104)
            else:
                RushCheck(450001210)
                
        elif daily19 == 1:
            if Quest.CheckCompleteDemand(34148, 3003107) == False:
                Terminal.Rush(450001013)
                RushAndComplete(450001013, 34148, 3003107)
            else:
                RushCheck(450001013)
                        
        elif daily20 == 1:
            if Quest.CheckCompleteDemand(34149, 3003108) == False:
                Terminal.Rush(450001112)
                RushAndComplete(450001112, 34149, 3003108)
            else:
                RushCheck(450001112)

        elif daily21 == 1:
            if Quest.CheckCompleteDemand(34150, 3003109) == False:
                Terminal.Rush(450001216)
                RushAndComplete(450001216, 34150, 3003109)
            else:
                RushCheck(450001216)
                
        elif daily0 == 1:
            if Quest.CheckCompleteDemand(34129, 3003104) == False:
                Terminal.Rush(450001000)
                RushAndComplete(450001000, 34129, 3003104)
                RestoreEvasion()
                
if VJ_Daily and Quest.GetQuestState(34129)==2:
    print("Completed VJ daily")
    

##########################
##########################
# Chuchu daily
##########################
##########################
startingMap = 450002023
exitMap = 450002024
hungryMutoMaps = [921170050, 921170100, 921170101, 921170102, 921170103, 921170104, 921170105]
allIngredients = []
allRecipes = []

usingParty = False
currentRecipe = None
defaultCH = 0

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
	
	if curChannel != defaultCH:
		Terminal.ChangeChannel(defaultCH)
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
    Terminal.SetCheckBox("bot/si_no_wait", True)
    Terminal.SetCheckBox("Kami Vac", False)
    Terminal.SetCheckBox("General FMA", False)
    Terminal.SetCheckBox("Full Map Attack", False)
    Terminal.SetCheckBox("bot/kanna_kami", False)
    if Field.GetID() not in ([startingMap, exitMap]+hungryMutoMaps):
        Terminal.Rush(startingMap)
        if usingParty:
            time.sleep(5)

    if Field.GetID() == startingMap:
        print('Starting...')
        SunCat.HookChuChu()
        InitRecipes()
        
        Terminal.SetCheckBox("Auto NPC", True)
        
        changeChannel()
        
        
        retryCount = 0
        tryAgain = True
        
        while tryAgain:
            if retryCount > 3:
                print("Failed to enter ChuChu, have you already done it 3 times? Move to next daily")
                SCLib.UpdateVar("ChuchuDone", True)
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
                if not usingParty:
                    Party.LeaveParty()
                    Party.CreateParty()
                retryCount += 1
                time.sleep(2)
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
        
if ChuChu_Daily and not SCLib.GetVar("ChuchuDone"):
    print("Starting ChuChu daily")
    
while ChuChu_Daily and not SCLib.GetVar("ChuchuDone"):
    if Terminal.GetCheckBox("Grenade Kami"):
        Terminal.SetCheckBox("Grenade Kami",False)
    if SCLib.CheckVersion(20):
        if GameState.IsInGame():
            InitAll()
            if usingParty:
                time.sleep(10)
        else:
            print('Not in game!')
    
    Terminal.SetCheckBox("bot/si_no_wait", False)
    RestoreSetting()
    time.sleep(3)
    
if ChuChu_Daily and SCLib.GetVar("ChuchuDone"):
    print("Completed ChuChu daily")

##########################
##########################
# Dream Defender Daily
##########################
##########################
ptgo_up = Field.FindPortal('ptgo_up')
ptgo_down = Field.FindPortal('ptgo_down')
ptgo_left = Field.FindPortal('ptgo_left')
ptgo_right = Field.FindPortal('ptgo_right')
ptback_up = Field.FindPortal('ptback_up')
ptback_down = Field.FindPortal('ptback_down')
ptback_left = Field.FindPortal('ptback_left')
ptback_right = Field.FindPortal('ptback_right')

NIGHTMARE_BOX = [9833080, 9833081, 9833082, 9833083, 9833084]
DD_MAP = [921171000, 921171001, 921171002, 921171003, 921171004, 921171005]
DD_CLOCKMAP = 450003540
DD_ENTERMAP = 450004000
DD_EXITMAP = 921171100
SLEEP_TIME = 0.5

CoinNpc = [9010101, 9010102, 9010103, 9010104, 9010105]
Lache_Town = 450003000


def toggle_attack(flag):
    if UseAA:
        Terminal.SetCheckBox("Auto Attack", flag)
    if UseSI:
        Terminal.SetCheckBox("Skill Injection", flag)

def is_in_center(x, y):
    return x >= ptgo_left.x - 50 and x <= ptgo_right.x + 50 and y >= ptgo_up.y - 50 and y <= ptgo_down.y + 50

def is_in_left(x, y):
    return x >= ptback_left.x - 450 and x <= ptback_left.x + 450 and y >= ptback_left.y - 250 and y <= ptback_left.y + 250

def is_in_right(x, y):
    return x >= ptback_right.x - 450 and x <= ptback_right.x + 450 and y >= ptback_right.y - 250 and y <= ptback_right.y + 250

def is_in_up(x, y):
    return x >= ptback_up.x - 450 and x <= ptback_up.x + 450 and y >= ptback_up.y - 250 and y <= ptback_up.y + 250

def is_in_down(x, y):
    return x >= ptback_down.x - 450 and x <= ptback_down.x + 450 and y >= ptback_down.y - 250 and y <= ptback_down.y + 250

def room_of(x, y):
    if is_in_center(x, y):
        return 'center'
    elif is_in_up(x, y):
        return 'up'
    elif is_in_down(x, y):
        return 'down'
    elif is_in_left(x, y):
        return 'left'
    elif is_in_right(x, y):
        return 'right'
    else:
        return None

def find_one_box():
    print("Searching a Box")
    flag = False
    for box_id in NIGHTMARE_BOX:
        mob = Field.FindMob(box_id)
        if mob.valid:
            print("Found Mob", mob, box_id)
            flag = True
            return mob
    print("Found None")
    return None

def close_enough(x1, y1, x2, y2, distance):
    if (x1 - x2)**2 + (y1 - y2)**2 < distance**2:
        return True
    else:
        return False

def safe_teleport(x, y):
    toggle_attack(False)
    pos = Character.GetPos()
    if not close_enough(pos.x, pos.y, x, y, 1000):
        print('TOO FAR. NOT SAFE TO TELEPORT!!!')
        time.sleep(SLEEP_TIME)
        return
    Character.Teleport(x, y - 5)
    time.sleep(SLEEP_TIME)

def safe_enter_portal():
    start = Character.GetPos()
    Character.EnterPortal()
    time.sleep(SLEEP_TIME)
    end = Character.GetPos()
    if close_enough(start.x, start.y, end.x, end.y, 10):
        Character.EnterPortal()

def moving_to_room(from_room, to_room):
    if from_room is None or to_room is None or from_room == to_room:
        return

    print('Moving from %s to %s.' % (from_room, to_room))
    if from_room == 'center':
        if to_room == 'up' and ptgo_up.valid:
            safe_teleport(ptgo_up.x, ptgo_up.y)
        elif to_room == 'down' and ptgo_down.valid:
            safe_teleport(ptgo_down.x, ptgo_down.y)
        elif to_room == 'left' and ptgo_left.valid:
            safe_teleport(ptgo_left.x, ptgo_left.y)
        elif to_room == 'right' and ptgo_right.valid:
            safe_teleport(ptgo_right.x, ptgo_right.y)
        safe_enter_portal()
    elif to_room == 'center':
        if from_room == 'up' and ptback_up.valid:
            safe_teleport(ptback_up.x, ptback_up.y)
        elif from_room == 'down' and ptback_down.valid:
            safe_teleport(ptback_down.x, ptback_down.y)
        elif from_room == 'left' and ptback_left.valid:
            safe_teleport(ptback_left.x, ptback_left.y)
        elif from_room == 'right' and ptback_right.valid:
            safe_teleport(ptback_right.x, ptback_right.y)
        safe_enter_portal()
    else:
        moving_to_room(from_room, 'center')

def start_DD():
    print("Attempting to join Dream Defender")
    Party.LeaveParty()
    Disabler()
    if Terminal.GetCheckBox("Skill Injection"):
        Terminal.SetCheckBox("Skill Injection", False)
    Npc.ClearSelection()
    Npc.RegisterSelection("Dream")
    Npc.RegisterSelection("Stage")
    Character.TalkToNpc(9010100)
    time.sleep(3)

def leave_DD():
    print("Get reward and leave")
    Character.TalkToNpc(9010100)    
    time.sleep(3)

def GetCoin(npc):
    print("Receiving coins from", npc)
    retry=0
    while SCLib.GetVar("DDCoin") == Inventory.GetItemCount(4310227) and retry<3:
        Character.TalkToNpc(npc)
        time.sleep(3)
        retry+=1

def Disabler():
    if Terminal.GetCheckBox("General FMA"):
        Terminal.SetCheckBox("General FMA", False)
    if Terminal.GetCheckBox("Full Map Attack"):
        Terminal.SetCheckBox("Full Map Attack", False)
    if Terminal.GetCheckBox("Grenade Kami"):
        Terminal.SetCheckBox("Grenade Kami", False)
    if Terminal.GetCheckBox("Mob Falldown"):
        Terminal.SetCheckBox("Mob Falldown", False)
    if Terminal.GetCheckBox("Kami Vac"):
        Terminal.SetCheckBox("Kami Vac", False)
    if Terminal.GetCheckBox("bot/kanna_kami"):
        Terminal.SetCheckBox("bot/kanna_kami", False)
    
    if not (Terminal.GetCheckBox("General FMA") or Terminal.GetCheckBox("Full Map Attack") or Terminal.GetCheckBox("Grenade Kami") or Terminal.GetCheckBox("Mob Falldown") or Terminal.GetCheckBox("bot/kanna_kami") or Terminal.GetCheckBox("Kami Vac")):
        return True
    else:
        return False
        
def retreatDD():
	rPacket = Packet.COutPacket(SCLib.PacketHeader["RetreatDD"])
	rPacket.EncodeBuffer("[01000000]")
	Packet.SendPacket(rPacket)
        
if DreamDefender_Daily and not SCLib.GetVar("DreamDone"):
    print("Starting Dream Defender daily")

while DreamDefender_Daily and not SCLib.GetVar("DreamDone"):
    if Field.GetID() not in DD_MAP+[DD_CLOCKMAP, DD_ENTERMAP, DD_EXITMAP]:
        Rush(DD_CLOCKMAP)
    if Field.GetID() == DD_CLOCKMAP:
        ToPortal("top00")
        time.sleep(2)
        
    retryCount = 0
    while retryCount < 3 and Field.GetID() == DD_ENTERMAP:
        start_DD()
        retryCount += 1
        
    if retryCount == 3:
        print("Finished Dream Defender daily")
        SCLib.UpdateVar("DreamDone", True)
        break
    
    flag = True
    startStage = 0
    
    while GameState.IsInGame() and Field.GetID() in DD_MAP and Disabler():
        ptgo_up = Field.FindPortal('ptgo_up')
        ptgo_down = Field.FindPortal('ptgo_down')
        ptgo_left = Field.FindPortal('ptgo_left')
        ptgo_right = Field.FindPortal('ptgo_right')
        ptback_up = Field.FindPortal('ptback_up')
        ptback_down = Field.FindPortal('ptback_down')
        ptback_left = Field.FindPortal('ptback_left')
        ptback_right = Field.FindPortal('ptback_right')    
        
        if flag:
            startStage = SunCat.GetDDStage()
            flag = False
        
        if startStage != SunCat.GetDDStage():
            retreatDD()
        
        box = find_one_box()
        if box is None:
            print('Can not find any nightmare box. Wait.')
            toggle_attack(False)
            time.sleep(SLEEP_TIME*2)
        else:
            room_of_box = room_of(box.x, box.y)
            print(box.x, box.y)
            print('Found box in room: %s' % room_of_box)

            pos = Character.GetPos()
            room_of_char = room_of(pos.x, pos.y)
            print(pos.x, pos.y)
            print('The character is in room: %s' % room_of_char)

            if room_of_box == room_of_char:
                if close_enough(pos.x, pos.y, box.x, box.y, 50):
                    print('Close enough. Toggle AA. Wait.')
                    toggle_attack(True)
                    time.sleep(SLEEP_TIME)
                else:
                    print('Not close enough. Teleport to box.')
                    safe_teleport(box.x, box.y)
                    time.sleep(SLEEP_TIME)
            else:
                moving_to_room(room_of_char, room_of_box)
        time.sleep(SLEEP_TIME)
    '''
    while Field.GetID() in DD_MAP:
        Disabler()
        print("Cleared the starting floor, wait and fail on purpose to leave the map")
        time.sleep(3)
    '''
    if Field.GetID() == DD_EXITMAP:
        RestoreSetting()
        leave_DD()

if DreamDefender_Daily and SCLib.GetVar("DreamDone") and not SCLib.GetVar("DDCoinDone"):
    print("Finished Dream Defender daily, now getting extra coins")

while SCLib.GetVar("DreamDone") and not SCLib.GetVar("DDCoinDone"):
    print("Returning to Lachelein Main street")
    if Field.GetID() == DD_ENTERMAP:
        exitpt = Field.FindPortal("out00")
        Character.MoveX(exitpt.x+30, 4000)
        time.sleep(1)
        Character.EnterPortal()
        time.sleep(2)
    elif Field.GetID() != Lache_Town:
        Rush(Lache_Town)
        time.sleep(5)
    elif Field.GetID() == Lache_Town:
        print("Receiving coins from npcs")
        for npc in CoinNpc:
            SCLib.UpdateVar("DDCoin", Inventory.GetItemCount(4310227))
            GetCoin(npc)
        SCLib.UpdateVar("DDCoinDone", True)
        print("Finished getting extra coins")
        

if ChuChu_Daily and SCLib.GetVar("DreamDone"):
    print("Completed Dream Defender daily")


##########################
##########################
# Spirit Savior Daily
##########################
##########################
ssMapStart = 921172300
ssMapEnd = 921172399
mobArray = [8644101, 8644102, 8644103, 8644104, 8644105, 8644106, 8644107, 8644108, 8644109, 8644110, 8644111, 8644112]
baseX = -175
baseY = -491

def inSS():
	return Field.GetID() >= ssMapStart and Field.GetID() <= ssMapEnd

def doSS():
    Terminal.SetCheckBox("bot/si_no_wait", True)
    Terminal.SetCheckBox("main/boss_freeze", True)
    Terminal.SetCheckBox("Auto Buff", False)

    for i in range(roundsPerRun):
        killCount = 0
        
        mobsKilled = []
        
        while killCount < 5:
            if not GameState.IsInGame() or not inSS():
                print("Not in SS!")
                break

            curMob = ""
            
            for mobID in mobArray:
                mob = Field.FindMob(mobID)
                if mob.valid and mob not in mobsKilled:
                    curMob = mob
                    mobsKilled.append(mob)
                    break
            
            if curMob != "":
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
        
        SunCat.KamiTP(baseX, baseY)
        time.sleep(roundWaitTime)

    Terminal.SetCheckBox("bot/si_no_wait", False)
    Terminal.SetCheckBox("main/boss_freeze", False)
    Terminal.SetCheckBox("Auto Buff", True)

    SunCat.StopTP()
    print("Finished!")

        
while SpiritSavior_Daily and not SCLib.GetVar("SpiritDone") and SCLib.CheckVersion(19):
    if Terminal.GetCheckBox("General FMA"):
        Terminal.SetCheckBox("General FMA", False)
    if Terminal.GetCheckBox("Full Map Attack"):
        Terminal.SetCheckBox("Full Map Attack", False)
    if Terminal.GetCheckBox("Grenade Kami"):
        Terminal.SetCheckBox("Grenade Kami",False)
    if Terminal.GetCheckBox("charm_fma"):
        Terminal.SetCheckBox("charm_fma",False)

    if Field.GetID() not in list(range(ssMapStart, ssMapEnd+1))+[450005000, 921172400]:
        print("Rush to Arcana town")
        Rush(450005000)
    
    if Inventory.GetItemCount(4310235) == (SCLib.GetVar("SpiritCoin")+30):
        SCLib.UpdateVar("SpiritDone", True)
        print("You earned daily cap for spirit coin")
        print("Finished Spirit Savior Daily")
        break
    
    retryCount = 0
    while retryCount < 3 and Field.GetID() == 450005000:
        print("Attempting to join Spirit Savior")
        Party.LeaveParty()
        Npc.ClearSelection()
        Npc.RegisterSelection("Attempt <Spirit Savior>")
        time.sleep(1)
        Character.TalkToNpc(3003381)
        time.sleep(2)
        retryCount += 1
        
    if retryCount == 3:
        SCLib.UpdateVar("SpiritDone", True)
        print("Finished Spirit Savior Daily")
        break

    if GameState.IsInGame() and inSS():
        print("Starting Spirit Savior")
        doSS()

    while inSS():
        time.sleep(1)
    
    if Field.GetID() == 921172400:
        print("Leaving from exit map")
        SunCat.StopTP()
        time.sleep(3)
        Character.TalkToNpc(3003381)

    RestoreSetting()
    time.sleep(1)
    
if ChuChu_Daily and SCLib.GetVar("SpiritDone"):
    print("Completed Spirit Savior daily")

print("You've completed all dailies")
time.sleep(5)