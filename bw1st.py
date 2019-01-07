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

# Disable rushbylevel, no need to restore it before finishing script
Terminal.SetRushByLevel(False)

while True:
	# sleep 1second every loop so script won't abuse your CPU
	time.sleep(1)
	field_id = Field.GetID()
	jobid = Character.GetJob()
	level = Character.GetLevel()
	if jobid == -1 or level == -1:
		# not in game
		continue
	if jobid == 1200 and field_id == 130000000:
		# Beginner Magician's Wand
		wand = Inventory.FindItemByID(1372043)
		# Training Knight
		medal = Inventory.FindItemByID(1142066)
		# Mysterious cryptic chest for reboot
		petbox = Inventory.FindItemByID(2434265)
		# Noblesse potion
		potion = Inventory.FindItemByID(2000021)
		if wand.valid:
			Inventory.SendChangeSlotPositionRequest(1, wand.pos, -11, -1)
			continue
		elif medal.valid:
			Inventory.SendChangeSlotPositionRequest(1, medal.pos, -49, -1) #-49: GMS, -21: JMS
			continue
		elif petbox.valid:
			Inventory.UseItem(2434265)
			continue
		elif potion.valid:
			Key.Set(0x22, 2, 2000021)
		Key.Set(0x44, 1, 12001020)
		Terminal.SetRushByLevel(True)
		break
	elif jobid != 1000:
		# not Noblesse
		break

	#map 1
	if field_id == 130030000:
		quest_state = Quest.GetQuestState(20820)
		if quest_state == 0:
			Quest.StartQuest(20820, 1102101)
	#map 2
	elif field_id == 130030100:
		quest1 = Quest.GetQuestState(20821)
		quest2 = Quest.GetQuestState(20822)
		if quest1 != 2:
			if quest1 == 0:
				Quest.StartQuest(20821, 1102101)
			elif quest1 == 1:
				Quest.CompleteQuest(20821, 1102100)
		else:
			if quest2 == 0:
				Quest.StartQuest(20822, 1102100)
			elif quest2 == 1:
				Quest.CompleteQuest(20822, 1102101)
	#map 3
	elif field_id == 130030101:
		quest1 = Quest.GetQuestState(20823)
		quest2 = Quest.GetQuestState(20824)
		quest3 = Quest.GetQuestState(20825)
		quest4 = Quest.GetQuestState(20826)
		quest5 = Quest.GetQuestState(20827)
		if quest1 != 2:
			if quest1 == 0:
				Quest.StartQuest(20823, 1102101)
			elif quest1 == 1:
				Quest.CompleteQuest(20823, 1102101)
		elif quest2 != 2:
			if quest2 == 0:
				Quest.StartQuest(20824, 1102101)
			elif quest2 == 1:
				equip = Inventory.FindItemByID(1003769)
				if equip.valid:
					Inventory.SendChangeSlotPositionRequest(1, equip.pos, -1, -1)
				elif Character.GetEquippedItemIDBySlot(-1) == 1003769:
					Quest.CompleteQuest(20824, 1102101)
		elif quest3 != 2:
			if quest3 == 0:
				Quest.StartQuest(20825, 1102103)
			elif quest3 == 1:
				Quest.CompleteQuest(20825, 1102103)
		elif quest4 != 2:
			if quest4 == 0:
				Quest.StartQuest(20826, 1102103)
			elif quest4 == 1:
				Quest.CompleteQuest(20826, 1102112)
		elif quest5 != 2:
			if quest5 == 0:
				Quest.StartQuest(20827, 1102101)
			elif quest5 == 1:
				portal = Field.FindPortal("next00")
				if portal.valid:
					Character.Teleport(portal.x, portal.y)
					time.sleep(1)
					Character.EnterPortal()
					time.sleep(1)
	#map 4
	elif field_id == 130030102:
		quest1 = Quest.GetQuestState(20827)
		quest2 = Quest.GetQuestState(20828)
		if quest1 != 2:
			Quest.CompleteQuest(20827, 1102114)
		elif quest2 == 0:
			Quest.StartQuest(20828, 1102114)
		elif quest2 == 1:
			Character.Teleport(-2524, -173)
			time.sleep(1)
			Quest.CompleteQuest(20828, 1102101)
	#map 5
	elif field_id == 130030103:
		quest1 = Quest.GetQuestState(20829)
		quest2 = Quest.GetQuestState(20830)
		quest3 = Quest.GetQuestState(20831)
		quest4 = Quest.GetQuestState(20832)
		quest5 = Quest.GetQuestState(20833)
		if quest1 != 2:
			if quest1 == 0:
				Quest.StartQuest(20829, 1102102)
			if quest1 == 1:
				if Quest.CheckCompleteDemand(20829, 1102102) == 0:
					Quest.CompleteQuest(20829, 1102102)
				else:
					# kill mobs
					pos = Character.GetPos()
					if pos.y >= 29:
						# move up
						if pos.x < -430:
							# move right
							Character.AMoveX(-430)
						elif pos.x > -280:
							# move left
							Character.AMoveX(-280)
						else:
							Character.Jump()
					else:
						# move and attack
						mob = Field.FindMob(9300730)
						if mob.valid:
							if pos.x < mob.x:
								if pos.x < mob.x - 100:
									# move right
									Character.MoveX(mob.x - 100, 10000)
								else:
									# face right
									Character.AMoveX(pos.x + 1)
							else:
								if pos.x > mob.x + 100:
									# move left
									Character.MoveX(mob.x + 100, 10000)
								else:
									# face left
									Character.AMoveX(pos.x - 1)
							Character.BasicAttack()
		elif quest2 != 2:
			if quest2 == 0:
				Quest.StartQuest(20830, 1102101)
			elif quest2 == 1:
				Inventory.UseItem(2001555)
				time.sleep(1)
				Quest.CompleteQuest(20830, 1102101)
		elif quest3 != 2:
			if quest3 == 0:
				Quest.StartQuest(20831, 1102102)
			elif quest3 == 1:
				if Quest.CheckCompleteDemand(20831, 1102102) == 0:
					Quest.CompleteQuest(20831, 1102102)
				else:
					pos = Character.GetPos()
					if pos.y >= 29:
						# move up
						if pos.x < -430:
							# move right
							Character.AMoveX(-430)
						elif pos.x > -280:
							# move left
							Character.AMoveX(-280)
						else:
							Character.Jump()
					else:
						# move and attack and pickup
						dropitem = Field.FindItem(4000489)
						if dropitem.valid:
							if pos.x < dropitem.x - 25:
								# move right
								Character.MoveX(dropitem.x - 25, 10000)
							elif pos.x > dropitem.x + 25:
								# move left
								Character.MoveX(dropitem.x + 25, 10000)
							Character.LootItem()
						else:
							mob = Field.FindMob(9300730)
							if mob.valid:
								if pos.x < mob.x:
									if pos.x < mob.x - 100:
										# move right
										Character.MoveX(mob.x - 100, 10000)
									else:
										# face right
										Character.AMoveX(pos.x + 1)
								else:
									if pos.x > mob.x + 100:
										# move left
										Character.MoveX(mob.x + 100, 10000)
									else:
										# face left
										Character.AMoveX(pos.x - 1)
								Character.BasicAttack()
		elif quest4 != 2:
			Quest.StartQuest(20832, 1102102)
		elif quest5 != 2:
			Quest.StartQuest(20833, 1102113)
	elif field_id == 130030104:
		quest1 = Quest.GetQuestState(20833)
		quest2 = Quest.GetQuestState(20834)
		quest3 = Quest.GetQuestState(20835)
		if quest1 != 2:
			Quest.CompleteQuest(20833, 1102113)
		else:
			if quest2 != 2:
				if quest2 == 0:
					Quest.StartQuest(20834, 1102106)
				elif quest2 == 1:
					Quest.CompleteQuest(20834, 1102107)
			elif quest3 == 0: 
				Quest.StartQuest(20835, 1102107)
			elif quest3 == 1:
				Quest.CompleteQuest(20835, 1102112)
			elif quest3 == 2:
				Quest.StartQuest(20836, 1102102)
	elif field_id == 130030105:
		quest1 = Quest.GetQuestState(20836)
		quest2 = Quest.GetQuestState(20837)
		if quest1 != 2:
			Quest.CompleteQuest(20836, 1102102)
		elif quest2 == 0:
			Key.Set(0x43, 1, 10001244) # 'C'
			time.sleep(1)
			Quest.StartQuest(20837, 1102102)
		elif quest2 == 1:
			if Quest.CheckCompleteDemand(20837, 1102102) == 0:
				Quest.CompleteQuest(20837, 1102102)
			else:
				# kill mobs
				pos = Character.GetPos()
				if pos.y >= 30:
					# move up
					if pos.x < -430:
						# move right
						Character.AMoveX(-430)
					elif pos.x > -280:
						# move left
						Character.AMoveX(-280)
					else:
						Character.Jump()
				else:
					# move and attack
					mob = Field.FindMob(9300731)
					if mob.valid:
						Character.AMoveX(mob.x)
						Key.Press(0x43) # 'C'
	elif field_id == 130030106:
		quest1 = Quest.GetQuestState(20838)
		quest2 = Quest.GetQuestState(20839)
		if quest1 == 0:
			Quest.StartQuest(20838, 1102104)
		elif quest1 == 1:
			if Quest.CheckCompleteDemand(20838, 1102104) == 0:
				Quest.CompleteQuest(20838, 1102104)
			else:
				rope_x = 2201
				rope_y = -152
				reactor_x = 1861
				reactor_y = -212
				pos = Character.GetPos()
				if pos.y > rope_y:
					if pos.x < rope_x:
						Character.MoveX(rope_x - 50, 10000)
						Character.Jump()
						Character.MoveY(rope_y, 2000)
					elif pos.x > rope_x:
						Character.MoveX(rope_x + 50, 10000)
						Character.Jump()
						Character.MoveY(rope_y, 2000)
					else:
						Character.MoveY(rope_y, 10000)
				elif pos.y == rope_y:
					Character.MoveX(2160, 10000)
					Character.Jump()
				elif pos.y == reactor_y:
					if pos.x < reactor_x - 10:
						Character.MoveX(reactor_x - 10, 10000)
					elif pos.x > reactor_x + 10:
						Character.MoveX(reactor_x + 10, 10000)
					dropitem = Field.FindItem(4033670)
					if dropitem.valid:
						if pos.x < dropitem.x - 25:
							Character.MoveX(dropitem.x - 25, 10000)
						elif pos.x > dropitem.x + 25:
							Character.MoveX(dropitem.x + 25, 10000)
						Character.LootItem()
					else:
						Character.BasicAttack()
				else:
					# ??? reset pls ???
					Character.MoveX(2600, 20000)
		elif quest2 == 0:
			Quest.StartQuest(20839, 1102100)
		else:
			portal = Field.FindPortal("next00")
			if portal.valid:
				Character.Teleport(portal.x, portal.y)
				time.sleep(1)
				Character.EnterPortal()
				time.sleep(1)
	elif field_id == 130030006:
		portal = Field.FindPortal("west00")
		if portal.valid:
			Character.Teleport(portal.x, portal.y)
			time.sleep(1)
			Character.EnterPortal()
			time.sleep(1)

	elif field_id == 130000000:
		quest1 = Quest.GetQuestState(20839)
		quest2 = Quest.GetQuestState(20860)
		quest3 = Quest.GetQuestState(20862)
		if quest1 == 1:
			Character.Teleport(189, 88)
			time.sleep(1)
			Quest.CompleteQuest(20839, 1101000)
		elif quest1 == 2:
			if quest2 == 0:
				Quest.StartQuest(20860, 1101002)
			elif quest2 == 1:
				Quest.CompleteQuest(20860, 1101002)

			elif quest2 == 2:
				if quest3 == 0:
					Character.Teleport(-870, 88)
					time.sleep(1)
					Quest.StartQuest(20862, 1101004)
				elif quest3 == 1:
					Quest.CompleteQuest(20862, 1101004)