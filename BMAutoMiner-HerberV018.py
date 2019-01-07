import os, sys, Character, GameState, Field, DataType, Terminal, time, Key

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")

#Version V018
#################################################################################################################################################
#																																				#
#							Boldmold @ Gamekillers forums, Be sure to leave a like if you enjoy the script										#
#																																				#
#################################################################################################################################################

###NPC ChatKey, Key for harvesting###	https://docs.microsoft.com/nb-no/windows/desktop/inputdev/virtual-key-codes
NpcChat = 0x20 #(Spacebar Default)

###Eneter Maps you want to check###
maps = [450005220,450005230,450005241] #List all the maps you want to check, You can list as many as you want.
LastMapID = 450005241 #the MapID of the last map in the list above

####Enter ID of the Herb/Ore's you want the script to look for and harvest.###
collectID = [200000,200001,200002,200003,200004,200005,200006,200007,200008,200009,200010,200011,200012,200013,100000,100001,100002,100003,100004,100005,100006,100007,100008,100009,100010,100011,100012,100013] #Enter CollectID's you want to harvest

###list of maps, Add maps of your liking###
#Arcana maps [450005530,450005550,450005520,450005510,450005500,450005440,450005431,450005432,450005430,450005420,450005412,450005411,450005410]
#Temple of time maps [270010100,270010200,270010300,270010400,270010500,270020100,270020200,270020300,270020400,270020500,270030100,270030200,270030300,270030400,270030500]
#Vanishing Journey maps [450001111,450001110,450001112,450001114,450001261,450001113,450001210,450001215,450001218,450001216,450001217,450001211,450001212,450001213,450001214,450001010,450001011,450001012,450001013,450001014,450001015,450001016,450001260]
#Kerning Tower 5,6 floor [103041140,103041145,103041147,103041150,103041155,103041157]
#Expert  Harvesting Farm [910001014]


###ID LIST###
###Ores###
#Silver Vein: 200000
#Magenta Vein: 200001
#Blue Vein: 200002
#Brown Vein: 200003
#Emerald Vein: 200004
#Gold Vein: 200005
#Aquamarine Vein: 200006
#Red Vein: 200007
#Black Vein: 200008
#Purple Vein: 200009
#Vein: 200010
#Heartstone Vein: 200011
#Mysterious : 200012
#Legendary : 200013

###Herbs###
#Silver Herb: 100000
#Magenta Herb: 100001
#Blue Herb: 100002
#Brown Herb: 100003
#Emerald Herb: 100004
#Gold Herb: 100005
#Aquamarine Herb: 100006
#Red Herb: 100007
#Black Herb: 100008
#Purple Herb: 100009
#Herb: 100010
#Heart Herb: 100011
#Mysterious: 100012
#Legendary: 100013

###Expand the list for easier changes :)


#########################################################################################################################################
#																																		#
#												Do not change anything below this line!													#
#																																		#
#########################################################################################################################################


SCLib.PersistVar("noReactorInMap", False)
SCLib.PersistVar("MapNumber", 0)
SCLib.PersistVar("TeleportAttempt", 0)
SCLib.PersistVar("HarvestAttempt", 0)
SCLib.PersistVar("TeleportCount",0)
SCLib.StartVars(20)
HasLooted = SCLib.GetVar("noReactorInMap")
TeleportAttempt = SCLib.GetVar("TeleportAttempt")
HarvestAttempt = SCLib.GetVar("HarvestAttempt")
fieldID = Field.GetID()
pos = Character.GetPos()
CurrentChannel = GameState.GetChannel()
NewChannel = CurrentChannel +1

def ChangeChannels():
	if CurrentChannel == 20:
		if fieldID == LastMapID:
			print("Changing Channel to 1")
			time.sleep(0.5)
			Terminal.ChangeChannel(1)
			time.sleep(3)
			print("Resetting back to first map")
			SCLib.UpdateVar("MapNumber", 0)
			time.sleep(3)
		else:
			print("Changing channel to 1")
			time.sleep(0.5)
			Terminal.ChangeChannel(1)
			time.sleep(3)
			SCLib.UpdateVar("MapNumber", SCLib.GetVar("MapNumber")+1)
			print("Changing map to {0}".format(SCLib.GetVar("MapNumber")))
	else:
		print("Changing channel to {0}".format(NewChannel))
		time.sleep(0.5)
		Terminal.ChangeChannel(NewChannel)
		time.sleep(3)
def ResetTeleportAttempt():
	SCLib.UpdateVar("TeleportAttempt", 0)
def ResetHarvestAttempt():
	SCLib.UpdateVar("HarvestAttempt", 0)
if GameState.IsInGame() and not Terminal.IsRushing():
	time.sleep(1)
	
	
	for harvest in collectID:
		herbore = Field.FindReactor(harvest)
		if herbore.valid:
			print("Found herb/Ore with ID {0}".format(herbore.id))
			SCLib.UpdateVar("noReactorInMap", False)
			break
		else:
			print("Did not find any herb/Ore with ID {0}".format(harvest))
			SCLib.UpdateVar("noReactorInMap", True)
	if herbore.valid:
		if Field.GetCharacterCount() != 0:
			ChangeChannels()
		else:
			maxX = herbore.x -1
			minX = herbore.x -60
			maxY = herbore.y +10
			minY = herbore.y -10
			newX = herbore.x -1
			newY = herbore.y -9
			if pos.x < minX or pos.x > maxX or pos.y < minY or pos.y > maxY:
				if TeleportAttempt < 3:
					ResetHarvestAttempt()
					print("Teleporting Attempt {0}".format(SCLib.GetVar("TeleportAttempt")+1))
					Character.Teleport(newX, newY)
					SCLib.UpdateVar("TeleportAttempt", SCLib.GetVar("TeleportAttempt")+1)
					SCLib.UpdateVar("TeleportCount", SCLib.GetVar("TeleportCount")+1)
					print("Has already teleported {} times in this map".format(SCLib.GetVar("TeleportCount")))
				else:
					if Terminal.GetCheckBox("Pet Item Teleport"):
						Terminal.SetCheckBox("Pet Item Teleport", False)
					else:
						ResetTeleportAttempt()
						time.sleep(0.5)
						ChangeChannels()
			else:
				if not Terminal.GetCheckBox("Pet Item Teleport"):
					Terminal.SetCheckBox("Pet Item Teleport", True)
				else:
					ResetTeleportAttempt()
					if HarvestAttempt < 4:
						print("Harvesting attempt {0}".format(SCLib.GetVar("HarvestAttempt")+1))
						time.sleep(0.5)
						Key.Press(NpcChat)
						time.sleep(4)
						SCLib.UpdateVar("HarvestAttempt", SCLib.GetVar("HarvestAttempt")+1)
					else:
						ChangeChannels()
	else:
		if HasLooted:
			ResetHarvestAttempt()
			if Terminal.GetCheckBox("Pet Item Teleport"):
				Terminal.SetCheckBox("Pet Item Teleport", False)
			else:
				if fieldID != maps[SCLib.GetVar("MapNumber")]:
					Terminal.Rush(maps[SCLib.GetVar("MapNumber")])
					SCLib.UpdateVar("TeleportCount",0)
				else:
					ChangeChannels()
					SCLib.UpdateVar("TeleportCount",0)
	if SCLib.GetVar("TeleportCount")>=6:
		ResetHarvestAttempt()
		print("Reached teleporting limit")
		if Terminal.GetCheckBox("Pet Item Teleport"):
			Terminal.SetCheckBox("Pet Item Teleport", False)
		else:
			if fieldID != maps[SCLib.GetVar("MapNumber")]:
				Terminal.Rush(maps[SCLib.GetVar("MapNumber")])
				SCLib.UpdateVar("TeleportCount",0)
			else:
				ChangeChannels()
				SCLib.UpdateVar("TeleportCount",0)
if GameState.IsInGame() and Terminal.IsRushing():
	if fieldID == 270000200:
		Terminal.StopRush()