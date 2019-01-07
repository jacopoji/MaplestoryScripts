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


Terminal.SetRushByLevel(False)

while True:
	time.sleep(1)
	map = Field.GetID()
	job = Character.GetJob()
	level = Character.GetLevel()
	if job == -1 or level == -1:
		# not in game
		continue
		
	if job == 3711 and level >= 100:
		# can job advance.
		if Terminal.IsRushing():
			time.sleep(1)
			continue
			
		drill = Quest.GetQuestState(23165)
		missing = Quest.GetQuestState(23166)
		mad = Quest.GetQuestState(23167)
		weapon = Quest.GetQuestState(23168)
		master = Quest.GetQuestState(23169)
		
		if drill != 2:
			if map != 310010000:
				Terminal.Rush(310010000)
				time.sleep(1)
				continue
				
			if drill == 0:
				Quest.StartQuest(23165, 2152000)
				time.sleep(1)
				
			elif drill == 1:
				# complete it
				Quest.CompleteQuest(23165, 2151003)
		
		elif missing != 2:
			if missing == 0:
				if map != 310010000:
					Terminal.Rush(310010000)
					time.sleep(1)
				else:
					Quest.StartQuest(23166, 2151003)
				
			elif missing == 1:
				if Character.GetEquippedItemIDBySlot(-1) == 1003134:
					# gelimer's keycard
					keyCard = Inventory.FindItemByID(4032743)
					if not keyCard.valid and map != 310060000:
						# if we don't have the keycard and we aren't in 
						# Gelimer's map, then rush to it
						Terminal.Rush(310060000)
						continue
						
					elif not keyCard.valid and map == 310060000:
						# if we don't have the keycard and we are in 
						# Gelimer's map, then do his quest
						if mad == 0:
							Npc.ClearSelection()
							Npc.RegisterSelection("I'm a new member of the Black Wings")
							Npc.RegisterSelection("I was patrolling")
							Npc.RegisterSelection("An intruder?! You need to beef up security")
							Npc.RegisterSelection("Then allow me to patrol for you")
							Npc.RegisterSelection("I just offered out of loyalty")
							Quest.StartQuest(23167, 2154009)
						
						elif mad == 1:
							Quest.CompleteQuest(23167, 2154009)
							time.sleep(1)
							
					elif keyCard.valid and map == 310060000:
						# rush to the hidden map
						Terminal.Rush(310060221)
						time.sleep(1)
						
					elif keyCard.valid and map == 310060221:
						# enter the map that requires a keycard
						Character.Teleport(953,16)
						time.sleep(1)
						Character.EnterPortal()
						
					elif keyCard.valid and map >= 931000300 and map <= 931000303:
						pos = Character.GetPos()
						Character.MoveX(pos.x + 10000, 3000)
						
					else:
						# map with the job instructor
						Quest.CompleteQuest(23166, 2159488)
						time.sleep(1) # sleep 1 second
				
				else:
					# wear your hat or get a new one
					hat = Inventory.FindItemByID(1003134)
					if hat.valid:
						# wear the hat
						Inventory.SendChangeSlotPositionRequest(1, hat.pos, -1, -1)
						time.sleep(1) # sleep 1 second
						continue
						
					else:
						if map != 310040000:
							Terminal.Rush(310040000)
							continue
						else:
							Character.Teleport(1614, -812)
						# don't have the hat, so lets do the quest to get it
						buyHat = Quest.GetQuestState(23947)
						if buyHat == 0:
							Quest.StartQuest(23947, 2153000)
							
						elif buyHat == 1:
							Quest.CompleteQuest(23947, 2153000)
							
						else:
							# no money
							Terminal.SetRushByLevel(True)
							break
				
		elif weapon !=2:
			# need to kill the machine thing
			if weapon == 0:
				Quest.StartQuest(23168, 2159488)
				time.sleep(1) # sleep 1 second
			
			elif Quest.CheckCompleteDemand(23168, 2159488) != 0:
				# if not done, rush to the mob and kill
				if map == 931000313:
					portal = Field.FindPortal("west00")
					if portal.valid:
						Character.Teleport(portal.x, portal.y-10)
						time.sleep(1)
						Character.EnterPortal()
						time.sleep(1)
				
				else:
					# in the map to kill him, I assume you have SI/ND on
					continue
			
			else:
				# quest is completed
				if map == 931000323:
					portal = Field.FindPortal("east00")
					if portal.valid:
						Character.Teleport(portal.x, portal.y - 10)
						time.sleep(1) # sleep 1 second
						Character.EnterPortal()
						time.sleep(1) # sleep 1 second
						
				else:
					Quest.CompleteQuest(23168, 2159488)
					
		elif master != 2:
			if master == 0:
				if map != 310010000:
					continue
				
				else:
					Quest.StartQuest(23169, 2151000)
					time.sleep(1)
					
	elif jobid == 3712:
		# quest completed?
		# equip 1353403 and 1142245
		item1 = Inventory.FindItemByID(1353403)
		item2 = Inventory.FindItemByID(1142245)
		if item1.valid:
			# type, equipslot, newslot(-10 is sub weapon), count(-1 to equip)
			Inventory.SendChangeSlotPositionRequest(1, item1.pos, -10, -1)
			time.sleep(1) # sleep 1 second
			continue
		elif item2.valid:
			# type, equipslot, newslot(-21 is medal), count(-1 to equip)
			Inventory.SendChangeSlotPositionRequest(1, item2.pos, -49, -1)
			time.sleep(1) # sleep 1 second
			continue
		else:
			# PPAP
			Terminal.SetRushByLevel(True)
			break
			
	else:
		Terminal.SetRushByLevel(True)
		break