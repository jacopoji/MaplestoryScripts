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
import GameState
import Party
# credits: leroy.jenkins93

usingKami = False

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
		

	
if GameState.IsInGame():
	time.sleep(1)
	currentMap  = Field.GetID()
	jobid = Character.GetJob()
	jobid = Character.GetJob()
	level = Character.GetLevel()


	if level >=200: 
		Terminal.SetRushByLevel(False)
		# --------------------------------------------------------
		# 5TH JOB QUESTS BELOW
		# --------------------------------------------------------
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

		if currentMap == 270010111:
			time.sleep(1)
			pos = Character.GetPos()
			if pos.x != -493 and pos.y != -868:
				Terminal.SetCheckBox("Kami Vac",False)
				Character.Teleport(-493, -868)
			time.sleep(5)
		
		if Quest.GetQuestState(1481) !=2:
			if Quest.GetQuestState(1481) == 0:
				Quest.StartQuest(1481,2140000)
			else:
				Quest.CompleteQuest(1481, 2140000)
		
		if Terminal.IsRushing():
			time.sleep(1)
		# if we qualify for 5th job, start the quest. 
		elif erdaCall != 2:
			if erdaCall == 0:
				Quest.StartQuest(1460, 2140001)
				time.sleep(1)
				
			# if the quest was accepted, hand it in 
			if Quest.CheckCompleteDemand(1460, 2140001) == 0:
				if currentMap != 270010111:
					Terminal.Rush(270010111)
				
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
							
					elif Quest.CheckCompleteDemand(1462, 1540942) == 0:
						if jobid == 6512:
							Npc.ClearSelection()
							Npc.RegisterSelection("Everyone ")
							time.sleep(1)
							Quest.CompleteQuest(1462, 1540942)
						elif jobid == 3512 or jobid == 3612 or jobid == 6412:
							Npc.ClearSelection()
							Npc.RegisterSelection("My ")
							time.sleep(1)
							Quest.CompleteQuest(1462, 1540942)
						elif jobid == 2712:
							Npc.ClearSelection()
							Npc.RegisterSelection(" ")
							time.sleep(1)
							Quest.CompleteQuest(1462, 1540942)
						else:
							Npc.ClearSelection()
							Npc.RegisterSelection(" ")
							time.sleep(1)
							Quest.CompleteQuest(1462, 1540942)
					
				# and now maple stone is in inventory
				# next lets get the grandis one
				elif grandisStoneQuest != 2:
					if grandisStoneQuest == 0:
						# if we are still stuck in the maple goddess room
						if currentMap == 450000000:
							# now get out of the room
							Terminal.SetCheckBox("Kami Vac",False)
							time.sleep(2)
							Character.Teleport(-487, 95)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							
						elif currentMap != 450000110 and currentMap != 450000010:
							if currentMap != 400000001:
								Terminal.Rush(400000001)
							time.sleep(2)
							Character.Teleport(-4, 27)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							 
						
						elif currentMap == 450000010:
							# stone room w/ my boy the dragon
							Quest.StartQuest(1463, 1540943)
							 
							
					elif Quest.CheckCompleteDemand(1463, 1540943) != 0:
						# if its not done, then we have to kill magnus
						if currentMap == 450000010:
							time.sleep(2)
							Character.Teleport(-498, 95)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							 
							
						# so we need to rush to magnus' room
						# make sure you've finished the prequests or you have a return scroll
						# im assuming prequests not done (so I'm going to do them after I get to the room)
						elif currentMap == 401000000:
							Character.Teleport(-97, 93)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							 
							
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
							 
						
						elif currentMap == 401060399:
							# magnus lobby room
							Party.CreateParty()
							Character.Teleport(1801, -1450)
							time.sleep(2)
							Npc.ClearSelection()
							Npc.RegisterSelection("Enter the Tyrant's Throne")
							Character.EnterPortal()
							time.sleep(2)
							 
							
						elif currentMap >= 401060300 and currentMap <= 401060398:
							# tyrant's room
							print("in tyrant's room")
							#Terminal.SetCheckBox("Kami Vac",True)
							while Character.GetPos().x not in range(1400,1600):
								Character.AMoveX(1525)

						else:
							if currentMap != 401000002:
								Terminal.Rush(401000002)
							print("Using return scroll")
							Inventory.UseItem(2030000)
							time.sleep(2)
							Terminal.Rush(401000000)
					
					elif Quest.CheckCompleteDemand(1463, 1540943) == 0:
						if currentMap >= 401060300 and currentMap <= 401060398:
							print("teleporting out of tyrant's room")
							Terminal.SetCheckBox("Kami Vac",False)
							Character.Teleport(592, -1347)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							 
						elif currentMap == 401060399:
							Character.Teleport(809, -1387)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
						
						elif currentMap == 401000001:
							Character.Teleport(-410, 343)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)

						elif currentMap != 450000110 and currentMap != 450000010:
							if currentMap != 400000001:
								Terminal.Rush(400000001)
							time.sleep(2)
							Character.Teleport(-4, 27)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							 
						
						elif currentMap == 450000010:
							# stone room w/ my boy the dragon
							Quest.CompleteQuest(1463, 1540943)
							 
							
				elif tynerumStoneQuest != 2:
					if tynerumStoneQuest == 0:
						# dragon goddess room
						if currentMap == 450000010:
							Character.Teleport(-497, 95)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							 
						
						# if we are not in the tynerum goddess room, rush to deserted camp and enter it
						elif currentMap != 450000120 and currentMap != 450000020 and currentMap != 105300304 and currentMap!= 105300305:
							if currentMap != 105300000:
								Terminal.Rush(105300000)
							time.sleep(2)
							Character.Teleport(-657, -175)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							 
							
						# if we are in the room, start the quest
						elif currentMap == 450000020:
							Quest.StartQuest(1464, 1540944)
							time.sleep(2)
							 
							
					elif Quest.CheckCompleteDemand(1464, 1540944) != 0:
						# if its not done, we need to rush to top of dwt
						# look for the portal that has her in it
						
						# rush to upper left stem to check here first
						Terminal.Rush(105300300)
						time.sleep(10)
						#1540941 horizon portal
						Terminal.SetCheckBox("Kami Vac",False)
						Terminal.SetCheckBox("Skill Injection",False)
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
								time.sleep(1)
							
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
								 time.sleep(1)
							
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
								 time.sleep(1)
							
					elif Quest.CheckCompleteDemand(1464, 1540944) == 0:
						# if the quest is done, hand it in 
						if currentMap != 450000120 and currentMap != 450000020 and currentMap != 105300304 and currentMap!= 105300305:
							if currentMap != 105300000:
								Terminal.Rush(105300000)
							time.sleep(2)
							Character.Teleport(-657, -175)
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
							Character.EnterPortal()
							time.sleep(2)
						else:
							time.sleep(1)
							Quest.CompleteQuest(1464, 1540944)
							
						 
						
			elif Quest.CheckCompleteDemand(1461, 2140001) == 0:
				Quest.CompleteQuest(1461, 2140001)
				time.sleep(2)
				Character.Teleport(-495, -100)
				time.sleep(2)
				Character.EnterPortal()
				time.sleep(2)
				 
				
		elif recordOfPower != 2:
			# record of power comes after we get the stones
			if currentMap == 450000020:
				Character.Teleport(-495, -100)
				time.sleep(2)
				Character.EnterPortal()
				time.sleep(2)
				 
			
			# if not started yet
			if recordOfPower == 0:
				Quest.StartQuest(1465, 2140001)
				Terminal.SetRushByLevel(True)
				
			elif Quest.CheckCompleteDemand(1465, 2140001) == 0:
				# if its completed, hand it in
				Quest.CompleteQuest(1465, 2140001)
				 	
				
			# elif Quest.CheckCompleteDemand(1465, 2140001) != 0:
			else:
				Terminal.SetCheckBox("Rush By Level",True)
				if usingKami == True:
					Terminal.SetCheckBox("Kami Vac",True)
				else:
					Terminal.SetCheckBox("Kami Vac",False)
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
		else:
			Terminal.SetRushByLevel(True)