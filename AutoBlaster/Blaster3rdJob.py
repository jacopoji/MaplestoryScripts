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

# Contributors: leroy.jenkins93, Qybah, cp932
Terminal.SetRushByLevel(False)

while True:
	time.sleep(1)
	map = Field.GetID()
	job = Character.GetJob()
	level = Character.GetLevel()
	if job == -1 or level == -1:
		# not in game
		continue
		
	if job == 3710 and level >= 60:
		# can job advance.
		if Terminal.IsRushing():
			time.sleep(1)
			continue
			
		sparks = Quest.GetQuestState(23163)
		wrench = Quest.GetQuestState(23164)
		
		if sparks != 2:
			if sparks == 0:
				if map != 310010000:
					Terminal.Rush(310010000)
					time.sleep(1)
				Quest.StartQuest(23163, 2152000)
				
			elif sparks == 1:
				if map == 310010000:
					Quest.CompleteQuest(23163, 2151000)
				else:
					Terminal.Rush(310010000)
					
		elif wrench != 2:
			if wrench == 0:
				if map == 310010000:
					Quest.StartQuest(23164, 2151000)
					time.sleep(1)
					
				else:
					Terminal.Rush(310010000)
					
			elif Quest.CheckCompleteDemand(23164, 2151000) != 0:
				# need to kill generator thing
				if Character.GetEquippedItemIDBySlot(-1) == 1003134:
					# if you're wearing the hat, then we can just proceed with quest
					if map == 931000200 or map == 931000201:
						# kill him here (I assume you have fma/si/nd on)
						continue
					else:
						if map != 310050100:
							Terminal.Rush(310050100)
						Character.Teleport(793, 18)
						Character.EnterPortal()
						
				else:
					# we need the hat
					# check if you have it in your inventory
					hat = Inventory.FindItemByID(1003134)
					if hat.valid:
						# wear the hat
						Inventory.SendChangeSlotPositionRequest(1, hat.pos, -1, -1)
						time.sleep(1) # sleep 1 second
						continue
						
					else:
						# don't have the hat, so lets do the quest to get it
						hatQuest = Quest.GetQuestState(23946)
						if hatQuest != 2:
							if hatQuest == 0:
								if map != 310040000:
									Terminal.Rush(310040000)
									
								else:
									Character.Teleport(1614, -812)
									time.sleep(1)
									Quest.StartQuest(23946, 2153000)
									
							elif Quest.CheckCompleteDemand(23946, 2153000) == 0:
								Quest.CompleteQuest(23946, 2153000)
								
							else:
								if map != 310040000:
									Terminal.Rush(310040000)
									
								else:
									Character.Teleport(1614, -812)
									time.sleep(1)
							
						else:
							buyHat = Quest.GetQuestState(23947)
							if buyHat == 0:
								Quest.StartQuest(23947, 2153000)
								
							elif buyHat == 1:
								Quest.CompleteQuest(23947, 2153000)
								
							else:
								# no money
								Terminal.SetRushByLevel(True)
								break
			
			elif Quest.CheckCompleteDemand(23164, 2151000) == 0:
				# if we are done, then rush back to hand it in
				if map == 931000200:
					Character.Teleport(140, 18)
					time.sleep(1)
					Character.EnterPortal()
				
				elif map == 310010000:
					Quest.CompleteQuest(23164, 2151000)
				
				else:
					Terminal.Rush(310010000)
					
	elif job == 3711:
		# finished advancement
		item1 = Inventory.FindItemByID(1353402)
		item2 = Inventory.FindItemByID(1142244)
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
			Terminal.SetRushByLevel(True)
			break

	else:
		Terminal.SetRushByLevel(True)
		break