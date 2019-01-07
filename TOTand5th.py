import Character
import Context
import DataType
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time 

# credits: leroy.jenkins93

def rushAndDo(startRush, endRush, questState, questID, npcStartID, npcEndID):
	if currentMap  != startRush:
		Terminal.Rush(startRush)
		time.sleep(1)
	
	if currentMap  == 270000000:
		pos = Character.GetPos()
		if pos.x != -2387 and pos.y != -177:
			Character.Teleport(-2387, -177)
		
	if currentMap  == 270010111:
		pos = Character.GetPos()
		if pos.x != -493 and pos.y != -868:
			Character.Teleport(-493, -868)
			
	if questState == 0:
		# accept it
		time.sleep(1)
		Quest.StartQuest(questID, npcStartID)
		time.sleep(1)
		
	elif Quest.CheckCompleteDemand(questID, npcEndID) == 0:
		if currentMap  != endRush:
			Terminal.Rush(endRush)
			time.sleep(1)
		Quest.CompleteQuest(questID, npcEndID)

def KaoAndDo(startRush, endRush, questState, questID, npcStartID, npcEndID):
	if currentMap  != startRush and questState == 0:
		Terminal.Rush(startRush)
		time.sleep(1)
	
	if currentMap  == 270000000:
		pos = Character.GetPos()
		if pos.x != -2387 and pos.y != -177:
			Character.Teleport(-2387, -177)
		
	if currentMap  == 270010111:
		time.sleep(2)
		Character.Teleport(-493, -868)
		time.sleep(5)
			
	if questState == 0:
		# accept it
		time.sleep(1)
		Quest.StartQuest(questID, npcStartID)
		time.sleep(1)
		
	elif Quest.CheckCompleteDemand(questID, npcEndID) == 0:
		if currentMap  != endRush:
			Terminal.Rush(endRush)
			time.sleep(1)
		Quest.CompleteQuest(questID, npcEndID)
		

	
while True:
	time.sleep(1)
	currentMap  = Field.GetID()
	jobid = Character.GetJob()
	jobid = Character.GetJob()
	level = Character.GetLevel()

	if jobid == -1 or level == -1:
		#not in game
		continue

	if level >=200: 
		Terminal.SetRushByLevel(False)
		
		
		# then, get the queststate for the first set of quests
		# THESE QUESTS ARE FOR MEMORY LANE + KAO QUESTS FOR MEMORY LANE
		#------------------------------------------------------------------
		pathToPast = Quest.GetQuestState(3500)
		memLane1 = Quest.GetQuestState(3501)
		memLane2 = Quest.GetQuestState(3502)
		memLane3 = Quest.GetQuestState(3503)
		memLane4 = Quest.GetQuestState(3504)
		memLane5 = Quest.GetQuestState(3505)
		
		lostMemory = Quest.GetQuestState(3506)
		memoryKeeper = Quest.GetQuestState(3507)	# not sure
		
		# valid for kanna only
		if jobid == 4212:
			seekingLostMemory = Quest.GetQuestState(57465)
		
		# BaM = 3212
		# WH = 3312
		# Mech = 3512
		# Blaster = 3712
		# valid for resistance
		elif jobid == 3212 or jobid == 3312 or jobid == 3512 or jobid == 3712:
			seekingLostMemory = Quest.GetQuestState(3541)
		
		# BW = 1212
		# DW = 1112
		# WA = 1312
		# NW = 1412
		# TB = 1512
		# valid for cgynus
		elif jobid == 1112 or jobid == 1212 or jobid == 1312 or jobid == 1412 or jobid == 1512:
			seekingLostMemory = Quest.GetQuestState(3529)
			
		# hero = 112
		# pally = 122
		# dk = 132
		elif jobid == 112 or jobid == 122 or jobid == 132:
			seekingLostMemory = Quest.GetQuestState(3523)
			
		
		# FP mage = 212
		# IL mage = 222
		# Bishop = 232
		elif jobid == 212 or jobid == 222 or jobid == 232: 
			seekingLostMemory = Quest.GetQuestState(3524)
			
			
		# NL
		# SHAD
		# DB
		elif jobid == 412 or jobid == 422 or jobid == 434:
			seekingLostMemory = Quest.GetQuestState(3526)
			
			
		#--------------------------------------------------------------------
		
		regrets1 = Quest.GetQuestState(3508)
		regrets2 = Quest.GetQuestState(3509)
		regrets3 = Quest.GetQuestState(3510)
		regrets4 = Quest.GetQuestState(3511)
		regrets5 = Quest.GetQuestState(3512)
		frozenEmotions = Quest.GetQuestState(3513)
		emotionSeller = Quest.GetQuestState(3514)
		
		#--------------------------------------------------------------------
		
		oblivion1 = Quest.GetQuestState(3515)
		oblivion2 = Quest.GetQuestState(3516)
		oblivion3 = Quest.GetQuestState(3517)
		oblivion4 = Quest.GetQuestState(3518)
		oblivion5 = Quest.GetQuestState(3519)
		blessing = Quest.GetQuestState(3520)
		
		
		
		lostTempleKeeper = Quest.GetQuestState(3548)
		amnesiacTempleKeeper = Quest.GetQuestState(3549)
		bringingBackTheBrain = Quest.GetQuestState(3550)
		liquidMemoryMaker = Quest.GetQuestState(3551)
		tinglebrainPotion = Quest.GetQuestState(3552)
		bitByBit = Quest.GetQuestState(3553)
		makeThoseMemories = Quest.GetQuestState(3554)
		timeWanderer = Quest.GetQuestState(3555)
		inAName = Quest.GetQuestState(3556)
		
		
		# 5th job quests
		# quests
		erdaCall = Quest.GetQuestState(1460)
		goddessBlessing = Quest.GetQuestState(1461)
		
		mapleStoneQuest = Quest.GetQuestState(1462)
		grandisStoneQuest = Quest.GetQuestState(1463)
		tynerumStoneQuest = Quest.GetQuestState(1464)
		
		recordOfPower = Quest.GetQuestState(1465)
		
		# stones
		mapleStone = Inventory.FindItemByID(2435734)
		grandisStone = Inventory.FindItemByID(2435735)
		tynerumStone = Inventory.FindItemByID(2435736)
		
		if currentMap == 270010111:
			time.sleep(1)
			if pos.x != -493 and pos.y != -868:
				Character.Teleport(-493, -868)
			time.sleep(5)
		
		
		
		if Terminal.IsRushing():
			time.sleep(1)
			continue
		
		
		# if path to past isn't completed, start it and end it
		if pathToPast != 2:
			rushAndDo(270000000, 270000000, pathToPast, 3500, 2140000, 2140000)
			continue
			
		elif memLane1 != 2:
			rushAndDo(270010100, 270010100, memLane1, 3501, 2140000, 2140000)
			continue
			
		elif memLane2 != 2:
			rushAndDo(270010200, 270010200, memLane2, 3502, 2140000, 2140000)
			continue
			
		elif memLane3 != 2:
			rushAndDo(270010300, 270010300, memLane3, 3503, 2140000, 2140000)
			continue
			
		elif memLane4 != 2:
			rushAndDo(270010400, 270010400, memLane4, 3504, 2140000, 2140000)
			continue
			
		elif memLane5 != 2:
			rushAndDo(270010500, 270010500, memLane5, 3505, 2140000, 2140000)
			continue
				
		elif lostMemory != 2:
			rushAndDo(270000000, 270010111, lostMemory, 3506, 2140000, 2140001)
			continue
		
		elif memoryKeeper != 2:
			# this is the one where we go to the memory keeper and ask him for help
			if  currentMap  != 270010111 and memoryKeeper == 0:
				Terminal.Rush(270010111)
				time.sleep(10)
				Character.Teleport(-493,-868)
				time.sleep(1)
				
			if memoryKeeper == 0:
				pos = Character.GetPos()
				if pos.x != -493 and pos.y != -868:
					Character.Teleport(-493, -868)
				time.sleep(5)
				Quest.StartQuest(3507, 2140001)
				time.sleep(1)
				
			elif Quest.CheckCompleteDemand(3507, 2140001) == 0:
				if currentMap  != 270010111:
					Terminal.Rush(270010111)
					time.sleep(1)
				time.sleep(10)
				Character.Teleport(-493,-868)
				Quest.CompleteQuest(3507, 2140001)
				
			elif seekingLostMemory !=2:
				if seekingLostMemory == 0:
					# KANNA
					if jobid == 4212:
						if currentMap  != 807000000:
							Terminal.Rush(807000000)
							time.sleep(1)
							continue
						Quest.StartQuest(57465, 9130008)
						time.sleep(2)
					
					# BaM = 3212
					# WH = 3312
					# Mech = 3512
					# Blaster = 3712
					# valid for resistance
					elif jobid == 3212 or jobid == 3312 or jobid == 3512 or jobid == 3712:
						if currentMap != 310010000:
							Terminal.Rush(310010000)
							time.sleep(1)
							continue
						Quest.StartQuest(3541, 2151003)
						time.sleep(2)
						
					# Cygnus
					elif jobid == 1112 or jobid == 1212 or jobid == 1312 or jobid == 1412 or jobid == 1512:
						if currentMap != 130000000:
							Terminal.Rush(130000000)
							time.sleep(1)
							continue
						Quest.StartQuest(3529, 1101002)
						time.sleep(2)
						
						
					# hero
					# pally
					# dk
					elif jobid == 112 or jobid == 122 or jobid == 132:
						if currentMap != 102000003:
							Terminal.Rush(102000003)
							time.sleep(1)
							continue
						Quest.StartQuest(3523, 1022000)
						time.sleep(2)
						
						
					# FP mage
					# IL mage
					# bishop
					elif jobid == 212 or jobid == 222 or jobid == 232:
						if currentMap != 101000003:
							Terminal.Rush(101000003)
							time.sleep(1)
							continue
						Quest.StartQuest(3524, 1032001)
						time.sleep(2)
				
					# NL
					# SHAD
					# DB
					elif jobid == 412 or jobid == 422 or jobid == 434:
						if currentMap != 103000003:
							Terminal.Rush(103000003)
							time.sleep(1)
							continue
						Quest.StartQuest(3526, 1052001)
						time.sleep(2)
				
				if seekingLostMemory == 1:
					# KANNA
					if jobid == 4212:
						if currentMap  != 807000000:
							Terminal.Rush(807000000)
							time.sleep(1)
							continue
						Quest.CompleteQuest(57465, 9130008)
						
					# BaM = 3212
					# WH = 3312
					# Mech = 3512
					# Blaster = 3712
					# valid for resistance
					elif jobid == 3212 or jobid == 3312 or jobid == 3512 or jobid == 3712:
						if currentMap != 310010000:
							Terminal.Rush(310010000)
							time.sleep(1)
							continue
						Quest.CompleteQuest(3541, 2151003)
						time.sleep(2)
					
					# Cygnus
					elif jobid == 1112 or jobid == 1212 or jobid == 1312 or jobid == 1412 or jobid == 1512:
						if currentMap != 130000000:
							Terminal.Rush(130000000)
							time.sleep(1)
							continue
						Quest.CompleteQuest(3529, 1101002)
						
					
					# explorer warrior
					elif jobid == 112 or jobid == 122 or jobid == 132:
						if currentMap != 102000003:
							Terminal.Rush(102000003)
							time.sleep(1)
							continue
						Quest.CompleteQuest(3523, 1022000)
						
					
					# FP mage
					# IL mage
					# bishop
					elif jobid == 212 or jobid == 222 or jobid == 232:
						if currentMap != 101000003:
							Terminal.Rush(101000003)
							time.sleep(1)
							continue
						Quest.CompleteQuest(3524, 1032001)
						time.sleep(2)
						
						
					# NL
					# SHAD
					# DB
					elif jobid == 412 or jobid == 422 or jobid == 434:
						if currentMap != 103000003:
							Terminal.Rush(103000003)
							time.sleep(1)
							continue
						Quest.CompleteQuest(3526, 1052001)
						
			continue
		
		elif regrets1 != 2:
			rushAndDo(270020100, 270020100, regrets1, 3508, 2140000, 2140000)
			continue
			
		elif regrets2 != 2:
			rushAndDo(270020200, 270020200, regrets2, 3509, 2140000, 2140000)
			continue
			
		elif regrets3 != 2:
			rushAndDo(270020300, 270020300, regrets3, 3510, 2140000, 2140000)
			continue
			
		elif regrets4 != 2:
			rushAndDo(270020400, 270020400, regrets4, 3511, 2140000, 2140000)
			continue
			
		elif regrets5 != 2:
			rushAndDo(270020500, 270020500, regrets5, 3512, 2140000, 2140000)
			continue
		
		elif frozenEmotions != 2:
			# if we finish road of regrets, then we need to do this quest.
			# rush to sorcerers room and accept quest from keeper, hand it to sorcerer
			rushAndDo(270020211, 270020211, frozenEmotions, 3513, 2140000, 2140002)
			continue
			
		elif emotionSeller != 2:
			# now for this quest, we will rush to the room
			if currentMap  != 270020211:
				Terminal.Rush(270020211)
				time.sleep(1)
				
			if emotionSeller == 0:
				Quest.StartQuest(3514, 2140002)
				time.sleep(10)
			
			elif Quest.CheckCompleteDemand(3514, 2140002) == 0:
				# if its completed, rush to room and hand in
				if currentMap  != 270020211:
					Terminal.Rush(270020211)
					time.sleep(1)
				Quest.CompleteQuest(3514, 2140002)
				
			else:
				# so the quest isn't completed yet, but it is accepted
				# we need to drink that potion. 
				# MAKE SURE AUTO REVIVE IS TOGGLED
				Inventory.UseItem(2022337)
				time.sleep(5)
			continue
		
		
		elif oblivion1 != 2:
			rushAndDo(270030100, 270030100, oblivion1, 3515, 2140000, 2140000)
			continue
			
		elif oblivion2 != 2:
			rushAndDo(270030200, 270030200, oblivion2, 3516, 2140000, 2140000)
			continue
			
		elif oblivion3 != 2:
			rushAndDo(270030300, 270030300, oblivion3, 3517, 2140000, 2140000)
			continue
			
		elif oblivion4 != 2:
			rushAndDo(270030400, 270030400, oblivion4, 3518, 2140000, 2140000)
			continue
			
		elif oblivion5 != 2:
			rushAndDo(270030500, 270030500, oblivion5, 3519, 2140000, 2140000) 
			continue
			
		elif blessing != 2:
			KaoAndDo(270000000, 270030411, blessing, 3520, 2140000, 2140003)
			continue
			
		elif lostTempleKeeper != 2:
			KaoAndDo(270010200, 270010200, lostTempleKeeper, 3548, 2140007, 2140007)
			continue
		
		
		elif amnesiacTempleKeeper != 2:
			KaoAndDo(270000000, 270010111, amnesiacTempleKeeper, 3549, 2140000,2140001) 
			continue
				
		elif bringingBackTheBrain != 2:
			KaoAndDo(270010111, 270000000, bringingBackTheBrain, 3550, 2140001, 2140006)
			continue
		
		elif liquidMemoryMaker != 2:
			KaoAndDo(270000000, 270020211, liquidMemoryMaker, 3551, 2140000, 2140002)
			continue
			
		elif tinglebrainPotion != 2:
			# for this quest, we need to collect 50 of those items
			# first accept the quest
			if  currentMap  != 270020211 and tinglebrainPotion == 0:
				Terminal.Rush(270020211)
				time.sleep(1)
				
			if tinglebrainPotion == 0:
				Quest.StartQuest(3552, 2140002)
				time.sleep(1)
				
			elif Quest.CheckCompleteDemand(3552, 2140002) == 0:
				# if its completed, rush back to the room
				if currentMap  != 270020211:
					Terminal.Rush(270020211)
					time.sleep(1)
				Quest.CompleteQuest(3552, 2140002)
				
			else:
				# otherwise, we are doing it
				if Inventory.GetItemCount(4033171) < 50:
					if currentMap  != 270020100:
						Terminal.Rush(270020100)
						time.sleep(1)
						
				else:
					if currentMap  != 270020400:
						Terminal.Rush(270020400)
						time.sleep(1)
		
		elif bitByBit != 2:
			KaoAndDo(270020211, 270000000, bitByBit, 3553, 2140002, 2140006)
			continue
		
		elif makeThoseMemories != 2:
			KaoAndDo(270000000, 270030411, makeThoseMemories, 3554, 2140000, 2140003)
			continue
			
		elif timeWanderer != 2:
			KaoAndDo(270030411, 270000000, timeWanderer, 3555, 2140003, 2140000)
			continue
			
		elif inAName != 2:
			KaoAndDo(270000000, 270000000, inAName, 3556, 2140000, 2140006)
			continue
			

		# --------------------------------------------------------
		# 5TH JOB QUESTS BELOW
		# --------------------------------------------------------
		
		# if we qualify for 5th job, start the quest. 
		elif erdaCall != 2:
			if erdaCall == 0:
				Quest.StartQuest(1460, 2140001)
				time.sleep(1)
				
			# if the quest was accepted, hand it in 
			if Quest.CheckCompleteDemand(1460, 2140001) == 0:
				if currentMap != 270010111:
					Terminal.Rush(270010111)
					continue
				
				# we need to answer is questions
				Npc.ClearSelection()
				Npc.RegisterSelection("Something... odd")
				Npc.RegisterSelection("Erdas")
				Npc.RegisterSelection("That sounds super important")
				Npc.RegisterSelection("Wait, what")
				Quest.CompleteQuest(1460, 2140001)
					
				time.sleep(5)
				
				# now we need to talk to the erda
				Npc.ClearSelection()
				Npc.RegisterSelection("Nah, I'm good")
				Character.TalkToNpc(1540940)
				# and that will finish talking with the erda
				continue
		
				time.sleep(5)
				
				# came back out from erda flow
				Npc.ClearSelection()
				Npc.RegisterSelection("I... talked to them")
				Npc.RegisterSelection("That sounds sweet")
				Quest.CompleteQuest(1460, 2140001)
				
				
		
		elif goddessBlessing != 2:
			if goddessBlessing == 0:
				if currentMap != 270010111:
					Terminal.Rush(270010111)
					continue
				Quest.StartQuest(1461, 2140001)
			
			elif Quest.CheckCompleteDemand(1461, 2140001) != 0:
				# this quest is incomplete
				# we need to get the 3 stones and activate them
				# first get the maple world one since its the easiest
				if mapleStoneQuest != 2:
					if mapleStoneQuest == 0:
						# if we haven't gotten this stone yet, rush to bowman school
						if currentMap != 450000100 and currentMap != 450000000:
							if currentMap != 100000201:
								Terminal.Rush(100000201)
							time.sleep(2)
							Character.Teleport(229, -58)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(15)
							
						elif currentMap == 450000000:
							# we are in the currentMap to get the stone
							Quest.StartQuest(1462, 1540942)
							continue
							
					elif Quest.CheckCompleteDemand(1462, 1540942) == 0:
						Npc.ClearSelection()
						Npc.RegisterSelection("The people of Maple World")
						Quest.CompleteQuest(1462, 1540942)
					
				# and now maple stone is in inventory
				# next lets get the grandis one
				elif grandisStoneQuest != 2:
					if grandisStoneQuest == 0:
						# if we are still stuck in the maple goddess room
						if currentMap == 450000000:
							# now get out of the room
							time.sleep(2)
							Character.Teleport(-487, 95)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
							
						elif currentMap != 450000110 and currentMap != 450000010:
							if currentMap != 400000001:
								Terminal.Rush(400000001)
							time.sleep(2)
							Character.Teleport(-4, 27)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
						
						elif currentMap == 450000010:
							# stone room w/ my boy the dragon
							Quest.StartQuest(1463, 1540943)
							continue
							
					elif Quest.CheckCompleteDemand(1463, 1540943) != 0:
						# if its not done, then we have to kill magnus
						if currentMap == 450000010:
							time.sleep(2)
							Character.Teleport(-498, 95)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
							
						# so we need to rush to magnus' room
						# make sure you've finished the prequests or you have a return scroll
						# im assuming prequests not done (so I'm going to do them after I get to the room)
						elif currentMap == 401000000:
							Character.Teleport(-97, 93)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
							
						elif currentMap == 401000001:
							# here we need to do magnus prequests
							Quest.StartQuest(31851, 3001001)
							time.sleep(2)
							Quest.CompleteQuest(31851, 3001000)
							
							# and now we can do easy magnus
							Character.Teleport(277, 261)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
						
						elif currentMap == 401060399:
							# magnus lobby room
							Character.Teleport(1801, -1450)
							time.sleep(2)
							Npc.ClearSelection()
							Npc.RegisterSelection("Enter the Tyrant's Throne")
							Character.EnterPortal()
							time.sleep(2)
							continue
							
						elif currentMap >= 401060300 and currentMap <= 401060398:
							# tyrant's room
							continue
						
						else:
							if currentMap != 401000002:
								Terminal.Rush(401000002)
								continue
							Inventory.UseItem(2030000)
					
					elif Quest.CheckCompleteDemand(1463, 1540943) == 0:
						if currentMap >= 401060300 and currentMap <= 401060398:
							Character.Teleport(592, -1347)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
							
						elif currentMap != 450000110 and currentMap != 450000010:
							if currentMap != 400000001:
								Terminal.Rush(400000001)
							time.sleep(2)
							Character.Teleport(-4, 27)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
						
						elif currentMap == 450000010:
							# stone room w/ my boy the dragon
							Quest.CompleteQuest(1463, 1540943)
							continue
							
				elif tynerumStoneQuest != 2:
					if tynerumStoneQuest == 0:
						# dragon goddess room
						if currentMap == 450000010:
							Character.Teleport(-497, 95)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
						
						# if we are not in the tynerum goddess room, rush to deserted camp and enter it
						elif currentMap != 450000120 and currentMap != 450000020 and currentMap != 105300304 and currentMap!= 105300305:
							if currentMap != 105300000:
								Terminal.Rush(105300000)
							time.sleep(2)
							Character.Teleport(-657, -175)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							continue
							
						# if we are in the room, start the quest
						elif currentMap == 450000020:
							Quest.StartQuest(1464, 1540944)
							time.sleep(2)
							continue
							
					elif Quest.CheckCompleteDemand(1464, 1540944) != 0:
						# if its not done, we need to rush to top of dwt
						# look for the portal that has her in it
						
						# rush to upper left stem to check here first
						Terminal.Rush(105300300)
						time.sleep(30)
						portal = Field.FindPortal("pt_horizon")
						if portal.valid:
							Character.Teleport(portal.x, portal.y-20)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(3)
							Character.EnterPortal()
							time.sleep(3)
							
							currentMap  = Field.GetID()
							if currentMap != 105300300:
								continue
							
						# so the portal was invalid
						# go to stem crossroad
						Terminal.Rush(105300301)
						time.sleep(10)
						portal = Field.FindPortal("pt_horizon")
						if portal.valid:
							Character.Teleport(portal.x, portal.y-20)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(3)
							Character.EnterPortal()
							
							time.sleep(3)
							
							currentMap  = Field.GetID()
							if currentMap != 105300301:
								continue
							
						# that portal doesn't exist either, so rush to right stem
						Terminal.Rush(105300302)
						time.sleep(10)
						portal = Field.FindPortal("pt_horizon")
						if portal.valid:
							Character.Teleport(portal.x, portal.y-20)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(5)
							
							time.sleep(3)
							
							currentMap  = Field.GetID()
							if currentMap != 105300302:
								continue
							
					elif Quest.CheckCompleteDemand(1464, 1540944) == 0:
						# if the quest is done, hand it in 
						Quest.CompleteQuest(1464, 1540944)
						continue
						
			elif Quest.CheckCompleteDemand(1461, 2140001) == 0:
				Quest.CompleteQuest(1461, 2140001)
				time.sleep(2)
				Character.Teleport(-495, -100)
				time.sleep(2)
				Character.EnterPortal()
				time.sleep(2)
				continue
				
		elif recordOfPower != 2:
			# record of power comes after we get the stones
			if currentMap == 450000020:
				Character.Teleport(-495, -100)
				time.sleep(2)
				Character.EnterPortal()
				time.sleep(2)
				continue
			
			# if not started yet
			if recordOfPower == 0:
				Quest.StartQuest(1465, 2140001)
				Terminal.SetRushByLevel(True)
				
			elif Quest.CheckCompleteDemand(1465, 2140001) == 0:
				# if its completed, hand it in
				Quest.CompleteQuest(1465, 2140001)
				continue	
				
			# elif Quest.CheckCompleteDemand(1465, 2140001) != 0:
			else:
				time.sleep(2)
				Inventory.UseItem(2435734)
				time.sleep(2)
				Inventory.UseItem(2435735)
				time.sleep(2)
				Inventory.UseItem(2435736)
				time.sleep(2)
				
				Terminal.SetRushByLevel(True)
				# sleep for 30 seconds after trying to use the items
				time.sleep(30)
				continue
				
		else:
			Terminal.SetRushByLevel(True)
			break