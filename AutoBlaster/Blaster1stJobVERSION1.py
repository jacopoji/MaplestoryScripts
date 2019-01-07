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
	field_id = Field.GetID()
	jobid = Character.GetJob()
	level = Character.GetLevel()
	if jobid == -1 or level == -1:
		# not in game
		continue
	if jobid == 3000:
		if Terminal.IsRushing():
			time.sleep(1)
			continue
			
		if field_id == 931000000:
			# the beginning map
			Character.AMoveX(-96)
		
		elif field_id == 931000001:
			# move to the portal
			Character.AMoveX(1440)
			Character.EnterPortal()
			
		# and now we are in the room with vita
		elif field_id == 931000010:
			Character.TalkToNpc(2159006)
			time.sleep(5)
			
		elif field_id == 931000011:
			continue
			
		elif field_id == 931000012:
			Character.TalkToNpc(2159006)
			
		elif field_id == 931000013:
			Character.TalkToNpc(2159007)
			time.sleep(5)
			
		elif field_id == 931000020:
			time.sleep(2)
			Character.AMoveX(0)
			
		elif field_id == 931000021:
			continue
			
		elif field_id == 931000030:
			time.sleep(1)
			Character.AMoveX(342)
			Key.Press(0x20)
		
		
		
		else:
			# so we finished the beginner stuff
			# now we are in edelstein. 
			spillIt = Quest.GetQuestState(23000)
			kindergarten = Quest.GetQuestState(23001)
			police = Quest.GetQuestState(23002)
			doctor = Quest.GetQuestState(23003)
			streetsweeper = Quest.GetQuestState(23004)
			mascot = Quest.GetQuestState(23005)
			mysteriousInvitation = Quest.GetQuestState(23010)
			blasterPath = Quest.GetQuestState(23160)
			
			if spillIt != 2:
				if field_id != 310000000 and spillIt == 0:
					Terminal.Rush(310000000)
					time.sleep(1)
				
				if field_id == 310000000:
					pos = Character.GetPos()
					if pos.x != -1297 and pos.y != -14:
						Character.Teleport(-1297, -14)
						
				if spillIt == 0:
					Character.Teleport(-1297, -14)
					# we need to accept the quest.
					Quest.StartQuest(23000, 2152000)
					time.sleep(1)
					
				
				elif Quest.CheckCompleteDemand(23000, 2152000) != 0:
					if kindergarten != 2:
						if kindergarten == 0:
							if field_id != 310000000:
								Terminal.Rush(310000000)
							Quest.StartQuest(23001, 2152001)
							
						
						elif Quest.CheckCompleteDemand(23001, 2152001) != 0:
							if field_id != 310020000:
								Terminal.Rush(310020000)
								time.sleep(1)
							
							# and now we need to kill + loot 5 of the things
							pos = Character.GetPos()
							mob = Field.FindMob(150000)
							potDrop = Field.FindItem(4000595)	
							# to face right
							
							if potDrop.valid:
								if pos.y < potDrop.y + 75 and pos.y > potDrop.y -75:
									# on the same platform, so attack
									Character.AMoveX(potDrop.x)
									Character.LootItem()
									
								elif (potDrop.y < 100 or potDrop.y > 50) and pos.y != -14:
									# bottom platform
									Character.MoveX(-499, 10000)
									
								elif potDrop.y < -239 or potDrop.y > -389:
									if pos.y < -465:
										Character.JumpDown()
									if pos.x < 232 or pos.x > 263:
										Character.MoveX(248, 10000)
										time.sleep(1)
										Character.Jump()
										Character.AMoveY(-320)
									
								elif (potDrop.y < -539 or potDrop.y > -689) and potDrop.x < 206:
									if pos.y > -260:
										# all the way at the bottom
										if pos.x < -270 or pos.x > -230:
											Character.MoveX(-250, 10000)
										Character.MoveY(-260, 2000)
										
										if pos.x < -205 or pos.x > -165:
											Character.MoveX(-185, 10000)
										Character.MoveY(-615, 2000)
									elif pos.y <= -260:
										if pos.x < -205 or pos.x > -165:
											Character.MoveX(-185, 10000)
										Character.MoveY(-615, 2000)
								
								elif (potDrop.y < -539 or potDrop.y > -689) and potDrop.x >207:
									# top right platform
									if pos.y > -260:
										# all the way at the bottom
										if pos.x < 588 or pos.x > 628:
											Character.MoveX(608, 10000)
										Character.MoveY(-260, 2000)
										
										if pos.x < 527 or pos.x > 567:
											Character.MoveX(547, 10000)
										Character.MoveY(-615, 2000)
									elif pos.y <= -260:
										if pos.x < 527 or pos.x > 567:
											Character.MoveX(547, 10000)
										Character.MoveY(-615, 2000)
							
							
						
							
							elif mob.valid:
								if mob.y == pos.y:
									# on the same platform, so attack
									Character.AMoveX(mob.x)
									Character.BasicAttack()
									
								elif mob.y == -14 and pos.y != -14:
									# bottom platform
									Character.MoveX(-499, 10000)
									
								elif mob.y == -314:
									if pos.y < -465:
										Character.JumpDown()
									if pos.x < 232 or pos.x > 263:
										Character.MoveX(248, 10000)
										time.sleep(1)
										Character.Jump()
										Character.AMoveY(-320)
									
								elif mob.y == -614 and mob.x < 206:
									if pos.y > -260:
										# all the way at the bottom
										if pos.x < -270 or pos.x > -230:
											Character.MoveX(-250, 10000)
										Character.MoveY(-260, 2000)
										
										if pos.x < -205 or pos.x > -165:
											Character.MoveX(-185, 10000)
										Character.MoveY(-615, 2000)
									elif pos.y <= -260:
										if pos.x < -205 or pos.x > -165:
											Character.MoveX(-185, 10000)
										Character.MoveY(-615, 2000)
								
								elif mob.y == -614 and mob.x >207:
									# top right platform
									if pos.y > -260:
										# all the way at the bottom
										if pos.x < 588 or pos.x > 628:
											Character.MoveX(608, 10000)
										Character.MoveY(-260, 2000)
										
										if pos.x < 527 or pos.x > 567:
											Character.MoveX(547, 10000)
										Character.MoveY(-615, 2000)
									elif pos.y <= -260:
										if pos.x < 527 or pos.x > 567:
											Character.MoveX(547, 10000)
										Character.MoveY(-615, 2000)
									
						else:
							if field_id != 310000000:
								Terminal.Rush(310000000)
							time.sleep(1)
							pos = Character.GetPos()
							if pos.x != -1297 and pos.y != -14:
								Character.Teleport(-1297, -14)
							time.sleep(1)
							Npc.ClearSelection()
							Npc.RegisterSelection("Peace")
							
							Quest.CompleteQuest(23001, 2152001)
							
					
					elif police != 2:
						if police == 0:
							if field_id != 310000000:
								Terminal.Rush(310000000)
							Quest.StartQuest(23002, 2152003)
							
						elif Quest.CheckCompleteDemand(23002,2152003) != 0:
							# in progress. 
							if map != 310020100:
								Terminal.Rush(310020100)
								
							pos = Character.GetPos()
							mob = Field.FindMob(150001)	

							if mob.valid:
								# the mob exists. Find it, move to it, kill it
								if mob.y == pos.y:
									# on the same platform, so attack
									Character.AMoveX(mob.x)
									Character.BasicAttack()
								
								elif mob.y == -14:
									# bottom platform
									Character.MoveX(35, 10000)
								
								elif mob.y == -254 and mob.x < 651:
									if pos.y < -400:
										Character.JumpDown()
										
									if pos.x < 251 or pos.x > 281:
										Character.MoveX(266, 10000)
									Character.MoveY(-260, 2000)
									
								elif mob.y == -254 and mob.x > 651:
									if pos.y < -400:
										Character.JumpDown()
									
									if pos.x < 1064 or pos.x > 1094:
										Character.MoveX(1079, 10000)
									Character.MoveY(-260, 2000)
									
								elif mob.y == -434:
									if pos.y < -500:
										Character.JumpDown()
									
									if pos.y > -254:
										# we are on bot platform, so move up
										if pos.x < 251 or pos.x > 281:
											Character.MoveX(266, 10000)
										Character.MoveY(-260, 2000)
										
									elif pos.y > -434:
										if pos.x < 420 or pos.x > 450:
											Character.MoveX(435, 10000)
										Character.MoveY(-450, 2000)
									
								elif mob.y == -674 and mob.x < 620:
									# top left platform
									if pos.y > -254:
										# we are on bot platform, so move up
										if pos.x < 251 or pos.x > 281:
											Character.MoveX(266, 10000)
										Character.MoveY(-260, 2000)
										
									elif pos.y > -434:
										if pos.x < 420 or pos.x > 450:
											Character.MoveX(435, 10000)
										Character.MoveY(-450, 2000)
									
									elif pos.y > -674:
										if pos.x < 345 or pos.x > 375:
											Character.MoveX(360, 10000)
										Character.MoveY(-680, 2000)
										
								elif mob.y == -674 and mob.x > 620:
									if pos.y > -254:
										# we are on bot platform, so move up
										if pos.x < 251 or pos.x > 281:
											Character.MoveX(266, 10000)
										Character.MoveY(-260, 2000)
										
									elif pos.y > -434:
										if pos.x < 420 or pos.x > 450:
											Character.MoveX(435, 10000)
										Character.MoveY(-450, 2000)
										
									elif pos.y > -674:
										if pos.x < 980 or pos.x > 1008:
											Character.MoveX(993, 10000)
										Character.MoveY(-674, 2000)
						
						
						else: 
							if field_id != 310000000:
								Terminal.Rush(310000000)
							time.sleep(1)
							Npc.ClearSelection()
							Npc.RegisterSelection("How safe it is")
							
							Quest.CompleteQuest(23002, 2152003)
							
					
					elif doctor != 2:
						if doctor == 0:
							if field_id != 310000000:
								Terminal.Rush(310000000)
							Quest.StartQuest(23003, 2152004)
					
						elif Quest.CheckCompleteDemand(23003,2152004) != 0:
							if field_id != 310020000:
								Terminal.Rush(310020000)
								
							pos = Character.GetPos()
							item = Field.FindItem(4034738)
							
							if item.valid and (pos.y < item.y + 75 and pos.y > item.y -75):
								Character.AMoveX(item.x)
								Character.LootItem()
								
							else:
								if pos.x < 588 or pos.x > 628 or pos.y > item.y - 75:
									Character.MoveX(608, 10000)
								Character.MoveY(-260, 2000)
								Character.BasicAttack()
								
						else:
							if field_id != 310000000:
								Terminal.Rush(310000000)
							time.sleep(1)
							Npc.ClearSelection()
							Npc.RegisterSelection("Surround themselves in an environment that")
							
							Quest.CompleteQuest(23003, 2152004)
							
					elif streetsweeper != 2:
						if streetsweeper == 0:
							if field_id != 310000000:
								Terminal.Rush(310000000)
							Quest.StartQuest(23004, 2152002)
							
						elif Quest.CheckCompleteDemand(23004, 2152002) != 0:
							if field_id != 310020200:
								Terminal.Rush(310020200)
								time.sleep(1)
							
							# and now we need to kill + loot 5 of the things
							pos = Character.GetPos()
							mob = Field.FindMob(150002)
							item = Field.FindItem(4000597)
							
							if item.valid:
								if item.y > -100:
									# bottom platform
									if pos.y < -100:
										Character.JumpDown()
									Character.AMoveX(item.x)
									Character.LootItem()
									
								elif (pos.y < item.y + 75 and pos.y > item.y -75):
									Character.AMoveX(item.x)
									Character.LootItem()
									
								elif item.y < -299 and pos.y > -449:	
									if pos.y < -400:
										Character.JumpDown()
									# second platform
									if pos.x < 130 or pos.x >157:
										Character.MoveX(143, 10000)
									Character.MoveY(-380, 2000)
								
								elif item.y < -599 and pos.y > -749:
									if pos.y > -374:
										# bot platform, go up
										if pos.x < 130 or pos.x >157:
											Character.MoveX(143, 10000)
										Character.MoveY(-380, 2000)
										
									elif pos.y > -614:
										if pos.x < 35 or pos.x > 65:
											Character.MoveX(50, 10000)
										Character.MoveY(-625, 2000)
										
									elif pos.y > -674:
										Character.Teleport(-167, -674)
										
										
							
							elif mob.valid:
								if mob.y > -100:
									# bottom platform
									if pos.y < -100:
										Character.JumpDown()
									Character.AMoveX(mob.x)
									Character.BasicAttack()
									
								elif mob.y == pos.y:
									Character.AMoveX(mob.x)
									Character.BasicAttack()
									
								elif mob.y == -374:	
									if pos.y < -400:
										Character.JumpDown()
									# second platform
									if pos.x < 130 or pos.x >157:
										Character.MoveX(143, 10000)
									Character.MoveY(-380, 2000)
								
								elif mob.y == -674:
									if pos.y > -374:
										# bot platform, go up
										if pos.x < 130 or pos.x >157:
											Character.MoveX(143, 10000)
										Character.MoveY(-380, 2000)
										
									elif pos.y > -614:
										if pos.x < 35 or pos.x > 65:
											Character.MoveX(50, 10000)
										Character.MoveY(-625, 2000)
										
									elif pos.y > -674:
										Character.Teleport(-167, -674)
						
						else:
							if map != 310000000:
								Terminal.Rush(310000000)
								time.sleep(1)
							Character.Teleport(-800, -14)
							time.sleep(1)
							Npc.ClearSelection()
							Npc.RegisterSelection("Restriction on our freedom")
							Quest.CompleteQuest(23004, 2152002)
					
					elif mascot != 2:
						if mascot == 0:
							if map != 310000000:
								Terminal.Rush(310000000)
								time.sleep(1)
							Character.Teleport(-376, -14)
							time.sleep(0.5)
							Quest.StartQuest(23005, 2152005)
						
						elif Quest.CheckCompleteDemand(23005, 2152005) != 0:
							Character.Teleport(1020, -14)
							time.sleep(0.5)
							Character.TalkToNpc(2152019)
							time.sleep(1)

						else:
							Character.Teleport(-376, -14)
							time.sleep(0.5)
							Npc.ClearSelection()
							Npc.RegisterSelection("You'd live life as a puppet without even realizing")
							Quest.CompleteQuest(23005, 2152005)
							time.sleep(1)
					
				elif Quest.CheckCompleteDemand(23000, 2152000) == 0:
					# if its done, rush back to the map
					if field_id != 310000000:
						Terminal.Rush(310000000)
					Npc.ClearSelection()
					Npc.RegisterSelection("It's such a rush to help people!")
					Quest.CompleteQuest(23000, 2152000)
					time.sleep(1)  
	
			elif spillIt == 2:
				# we finished the preliminary quests. Now do mysteriuos invitation
				if mysteriousInvitation != 2:
					if mysteriousInvitation == 0:
						Quest.StartQuest(23010, 2152000)
						time.sleep(1)
					elif mysteriousInvitation == 1:
						Inventory.UseItem(2031010)
						time.sleep(1)
						Quest.CompleteQuest(23010, 2151003)
						time.sleep(1)
						
				elif blasterPath != 2:
					if blasterPath == 0:
						Quest.StartQuest(23160, 2151000)
						time.sleep(1)
					elif blasterPath == 1:
						Quest.CompleteQuest(23160, 2151000)
						time.sleep(1)
						
						
	
	# credits for this go to Qybah
	elif jobid == 3700:	
		subweapon = Inventory.FindItemByID(1353400)
		medal = Inventory.FindItemByID(1142242)
		weapon = Inventory.FindItemByID(1582000)
		petbox = Inventory.FindItemByID(2434265)
		if subweapon.valid:
			# type, equipslot, newslot(-10 is sub weapon), count(-1 to equip)
			Inventory.SendChangeSlotPositionRequest(1, subweapon.pos, -10, -1)
			continue
		elif medal.valid:
			# type, equipslot, newslot(-49 is medal), count(-1 to equip)
			Inventory.SendChangeSlotPositionRequest(1, medal.pos, -49, -1)
			continue
		elif petbox.valid:
			Inventory.UseItem(2434265)
			continue
		elif weapon.valid:
			Character.Jump()
			# type, equipslot, newslot(-11 is weapon), count(-1 to equip)
			Inventory.SendChangeSlotPositionRequest(1, weapon.pos, -11, -1)
			continue
		else:
			Key.Set(0x44, 1, 37001000)
			Terminal.SetRushByLevel(True)
			break
	
	else:	
		Terminal.SetRushByLevel(True)
		break