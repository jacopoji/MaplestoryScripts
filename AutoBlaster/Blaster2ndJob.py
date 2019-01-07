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
	job = Character.GetJob()
	level = Character.GetLevel()
	map = Field.GetID()
	
	if job == -1 or level == -1:
		continue
		
	if Terminal.IsRushing():
		time.sleep(1)
		continue
		
	if job == 3700 and level >= 30:
		
		if Terminal.IsRushing():
			time.sleep(1)
			continue
		
		# job advancement requirements are met
		jobAdvance = Quest.GetQuestState(23161)
		vengeance = Quest.GetQuestState(23162)
		
		if jobAdvance != 2:
			# if the quest is done and we aren't in the correct map, rush to it
			if map != 310010000:
				Terminal.Rush(310010000)
				time.sleep(1)
				
			if jobAdvance == 0:
				Quest.StartQuest(23161, 2152000) # accept it from old man
				time.sleep(1)
				
			elif jobAdvance == 1:
				# if complete, hand it in 
				Quest.CompleteQuest(23161, 2151000)
				time.sleep(1)
		
		elif vengeance != 2:
			pos = Character.GetPos()
			
			if vengeance == 0 and map != 310010000:
				Terminal.Rush(310010000)
				time.sleep(1)
				continue
				
			if vengeance == 0:
				Quest.StartQuest(23162, 2151000)
				time.sleep(1)
				
			elif Quest.CheckCompleteDemand(23162, 2151000) != 0:
				if map == 310010000:
					Terminal.Rush(310000000)
					time.sleep(1)
					
				elif map == 310000000:
					Character.Teleport(1864, -14)
					time.sleep(0.5)
					Character.EnterPortal()
					time.sleep(1)
				
				else:
					# we are int he map
					Character.TalkToNpc(2159100)	# talk to him to activate scene
					item = Field.FindItem(4034787)	# look for the item
					if item.valid:
						if pos.x < item.x -15 or pos.x > item.x + 15:
							Character.AMoveX(item.x)
						Character.LootItem()
					time.sleep(1)
				
			elif Quest.CheckCompleteDemand(23162, 2151000) == 0:
				if map != 310010000 and map != 310000000:
					Character.Teleport(-374, -14)
					time.sleep(1)
					Character.EnterPortal()
					time.sleep(1)
				elif map == 310010000:
					Quest.CompleteQuest(23162, 2151000)
					
				else:
					Terminal.Rush(310010000)
					time.sleep(1)
				
	# credits go to Qybah for this
	elif job == 3710:
		# job advancement complete
		item1 = Inventory.FindItemByID(1353402)
		item2 = Inventory.FindItemByID(1142243)
		if item1.valid:
			# type, equipslot, newslot(-10 is sub weapon), count(-1 to equip)
			Inventory.SendChangeSlotPositionRequest(1, item1.pos, -10, -1)
			time.sleep(1)
			continue
		elif item2.valid:
			# type, equipslot, newslot(-49 is medal), count(-1 to equip)
			Inventory.SendChangeSlotPositionRequest(1, item2.pos, -49, -1)
			time.sleep(1)
			continue
		else:
			# PPAP
			Terminal.SetRushByLevel(True)
			break
			
	else:
		Terminal.SetRushByLevel(True)
		break