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


Terminal.SetRushByLevel(False)

jobid = Character.GetJob()

def rush(map):
	now = Field.GetID()
	while Terminal.IsRushing():
		time.sleep(1)
	if now != map:
		Terminal.Rush(map)

if GameState.IsInGame() and jobid == 15000:
	map = Field.GetID()
	level = Character.GetLevel()
	jobid = Character.GetJob()
	pos = Character.GetPos()
	pet = Inventory.FindItemByID(2434265)
	if pet.valid:
		Key.Set(0x41, 2, 2001582)
		time.sleep(2)
		Inventory.UseItem(2434265)
		time.sleep(2)
	
	while Terminal.IsRushing():
		time.sleep(1)

	if level == 1 and map == 940202009:
		Character.Teleport(-3319, 79)
		time.sleep(2)
		
		
		time.sleep(1)
		Character.EnterPortal()
		time.sleep(4)

	if level == 1 and map == 940202011:
		Character.Teleport(-3400, 79)
		Character.MoveX(-3000, 5000)
		
	if map == 940202013 or map == 940202014 or map == 940202015:
		mob = Field.FindMob(2400418)
		if mob.valid:
			Character.MoveX(mob.x, 20000)
			Character.BasicAttack()
			
		else:
			Character.Teleport(832,813)
			time.sleep(1)
			Character.EnterPortal()
			
	# some questing begins here
	preparations = Quest.GetQuestState(34800)
	collecting = Quest.GetQuestState(34801)
	if preparations != 2:
		if preparations == 0:
			Quest.StartQuest(34800, 3001330)
			time.sleep(1)

		elif Quest.CheckCompleteDemand(34800, 3001330) != 0:
			Inventory.SendChangeSlotPositionRequest(1, 1, -11, -1)
			time.sleep(1)
			Inventory.UseItem(2000046)
			time.sleep(1)

		else:
			Quest.CompleteQuest(34800, 3001330)

	
	if collecting != 2:
		if collecting == 0:
			Quest.StartQuest(34801, 3001330)
			time.sleep(1)
		elif Quest.CheckCompleteDemand(34801, 3001330) != 0:
			if map == 940202012:
				Character.Teleport(13,813)
				time.sleep(1)
				Character.EnterPortal()
				time.sleep(1)
			if map == 940202015:
				mob = Field.FindMob(2400418)
				if mob.valid:
					Character.MoveX(mob.x, 10000)
					Character.BasicAttack()
				else:
					Character.Teleport(832,813)
					time.sleep(1)
					Character.EnterPortal()
					time.sleep(1)
			if map in range(940203000, 940203010) :
				mob = Field.FindMob(2400413)
				item = Field.FindItem(4036162)
				if item.valid:
					if item.y in range(pos.y - 50, pos.y + 50):
						Character.MoveX(item.x, 20000)
						Character.LootItem()
					elif item.y < 600:
						Character.MoveX(-146, 20000)
						time.sleep(2)
						Character.Jump()
						Character.MoveY(584, 3000)
						time.sleep(1)
					else:
						Character.JumpDown()
				elif mob.valid:
					if mob.y in range(pos.y - 50, pos.y + 50):
						Character.MoveX(mob.x, 10000)
						Character.BasicAttack()
					elif mob.y < 600:
						Character.MoveX(-146, 20000)
						time.sleep(2)
						Character.Jump()
						Character.MoveY(584, 1000)
						time.sleep(1)
					else:
						Character.JumpDown()
	
		else:
			
			Quest.CompleteQuest(34801, 3001330)
			Character.MoveX(803, 50000)
			Character.EnterPortal()

if GameState.IsInGame() and jobid == 15200 and not Terminal.IsRushing():
	map = Field.GetID()
	level = Character.GetLevel()
	jobid = Character.GetJob()
	pos = Character.GetPos()

	pet = Inventory.FindItemByID(2434265)
	
		
	grossular = Quest.GetQuestState(34802)
	combat = Quest.GetQuestState(34803)
	social = Quest.GetQuestState(34804)
	crystalGate = Quest.GetQuestState(34805)
	specialActivity = Quest.GetQuestState(34806)
	dean = Quest.GetQuestState(34807)
	divine1 = Quest.GetQuestState(34808)
	cries = Quest.GetQuestState(34809)
	gate2 = Quest.GetQuestState(34811)
	aftergate = Quest.GetQuestState(34812)
	verdantFlora = Quest.GetQuestState(34813)
	festival2 = Quest.GetQuestState(34814)
	festival3 = Quest.GetQuestState(34815)
	festival4 = Quest.GetQuestState(34816)
	jobadv = Quest.GetQuestState(34817)
	escape = Quest.GetQuestState(34718)
	
	if map == 402000526 and specialActivity != 2:
		Quest.StartQuest(34806, 0)
	
	if grossular != 2:
		if grossular == 0:
			rush(402000526)
			Quest.StartQuest(34802, 3001332)
			
		elif Quest.CheckCompleteDemand(34802, 3001332) != 0:
			if map != 402000511:
				rush(402000511)
			time.sleep(1)
			
		else:
			rush(402000526)
			Quest.CompleteQuest(34802, 3001332)
	
	elif combat != 2:
		if combat == 0:
			if map != 402000527:
				rush(402000527)
			Key.Press(0x11)
			time.sleep(3)
			Key.Press(0x11)
			Quest.StartQuest(34803, 3001333)
			
		elif Quest.CheckCompleteDemand(34803, 3001333) != 0:
			rush(402000531)
			if pos.x not in range(440,470):
				Character.MoveX(461, 20000)
		
		else:
			rush(402000527)
			Quest.CompleteQuest(34803, 3001333)
			
	elif social != 2:
		if social == 0:
			rush(402000530)
			Quest.StartQuest(34804, 3001360)
		
		elif Quest.CheckCompleteDemand(34804, 3001360) != 0:
			Character.TalkToNpc(3001314)
			time.sleep(3)
			Character.TalkToNpc(3001315)
			time.sleep(3)
			Character.TalkToNpc(3001316)
			time.sleep(3)
			Character.TalkToNpc(3001317)
			time.sleep(3)
			Character.TalkToNpc(3001318)
			
		else:
			Quest.CompleteQuest(34804, 3001360)
	
	elif crystalGate != 2:
		if crystalGate == 0:
			rush(402000530)
			Quest.StartQuest(34805, 3001334)
			time.sleep(2)
			
		elif Quest.CheckCompleteDemand(34805, 3001334) != 0:
			if map != 402000517:
				rush(402000517)
			
			else:
				time.sleep(1)
				# remove these lines if you're using mob vac
				Character.MoveX(1500, 50000)
				
		else:
			rush(402000530)
			while Terminal.IsRushing():
				time.sleep(1)
			Quest.CompleteQuest(34805, 3001334)
			rush(402000528)
	
	elif specialActivity != 2:
		if specialActivity == 0:
			Quest.StartQuest(34806, 0)
		
		else:
			rush(402000528)
			Quest.CompleteQuest(34806, 3001331)
			
	elif dean != 2:
		if dean == 0:
			rush(402000532)
			Quest.StartQuest(34807, 3001337)
			time.sleep(1)
			
		elif Quest.CheckCompleteDemand(34807, 3001337) != 0:
			rush(402000534)
			Character.MoveX(500, 10000)
			
		else:
			rush(402000532)
			Quest.CompleteQuest(34807, 3001337)
					
	elif divine1 != 2:
		if divine1 == 0: 
			rush(402000526)
			Quest.StartQuest(34808, 3001335)
			
		elif Quest.CheckCompleteDemand(34808, 3001335) != 0:
			rush(402000514)
			time.sleep(30)
			Quest.StartQuest(34809, 0)
			while True:
				if GameState.IsInGame():
					rush(402000513)
					cries = Quest.GetQuestState(34809)
					after = Quest.GetQuestState(34810)
					if cries != 2:
						if Quest.CheckCompleteDemand(34809, 3001338) != 0:
							rush(402000513)
							while Terminal.IsRushing():
								time.sleep(1)
						else:
							Quest.CompleteQuest(34809, 3001338)
					
					elif after != 2:
						if after == 0:
							Npc.ClearSelection()
							Npc.RegisterSelection("Choice 1")
							Quest.StartQuest(34810, 3001338)
							
					else:
						break
						
				else:
					break
				
		else:
			rush(402000526)
			Quest.CompleteQuest(34808, 3001335)
			rush(402000530)
	
	elif gate2 != 2:
		if gate2 == 0:
			rush(402000530)
			
		elif Quest.CheckCompleteDemand(34811, 3001334) != 0:
			Character.MoveX(0, 10000)
			rush(402000535)
			
		else:
			rush(402000530)
			Quest.CompleteQuest(34811, 3001334)
			
	elif aftergate != 2:
		if aftergate == 0:
			rush(402000530)
			Quest.StartQuest(34812, 0)
			time.sleep(5)
		
		elif Quest.CheckCompleteDemand(34812, 3001336) != 0:
			rush(402000501)
			
		else:
			Quest.CompleteQuest(34812, 3001336)
			
	elif verdantFlora != 2: 
		if verdantFlora == 0:
			rush(402000501)
			
			#E6 00 06 01 00 00 00 00
			Npc.ClearSelection()
			time.sleep(2)
			time.sleep(1)
			Quest.StartQuest(34813, 3001336)
			
			Npc.RegisterSelection("Of course!")
			time.sleep(2)
			
		elif Quest.CheckCompleteDemand(34813, 3001336) != 0:
			rush(402000502)
			Character.MoveX(1309, 10000)
			
		else:
			rush(402000501)
			while Terminal.IsRushing():
				time.sleep(1)
			Quest.CompleteQuest(34813, 3001336)
			time.sleep(5)
			rush(402000529)
			
	elif festival2 != 2:
		if festival2 == 0:
			rush(402000529)
			Quest.StartQuest(34814, 3001339)
			time.sleep(3)
			
		elif Quest.CheckCompleteDemand(34814, 3001339) != 0:
			rush(402000507)
			time.sleep(1)
			
		else:
			rush(402000529)
			Quest.CompleteQuest(34814, 3001339)
			time.sleep(1)
			
	elif festival3 != 2:
		if festival3 == 0:
			rush(402000529)
			Quest.StartQuest(34815, 3001339)
			time.sleep(3)
		
		elif Quest.CheckCompleteDemand(34815, 3001339) != 0:
			rush(402000509)
			time.sleep(1)
			
		else:
			rush(402000529)
			Quest.CompleteQuest(34815, 3001339)
			time.sleep(1)
			
	elif festival4 != 2:
		if festival4 == 0:
			rush(402000529)
			Quest.StartQuest(34816, 3001339)
			time.sleep(2)
			
		elif Quest.CheckCompleteDemand(34816, 3001339) != 0:
			rush(402000504)
			time.sleep(1)
			
		else:
			rush(402000529)
			Quest.CompleteQuest(34816, 3001339)
			time.sleep(1)
					
	elif jobadv != 2:
		if jobadv == 0:
			rush(402000529)
			Quest.StartQuest(34817, 3001339)
			time.sleep(2)
		
		elif Quest.CheckCompleteDemand(34817, 3001339) != 0:
			if map == 402000529:
				rush(402000504)
				
			elif map in range(940202100, 940202199):
				mob = Field.FindMob(2400420)
				if mob.valid:
					time.sleep(20)
					Character.MoveX(-500, 20000)
					time.sleep(1)
				else:
					Character.Teleport(1, -683)
					time.sleep(2)
					Character.EnterPortal()
					Character.EnterPortal()
					time.sleep(3)
			
			elif map in range(940202200, 940202299):
				Character.JumpDown()
				time.sleep(2)
				Character.JumpDown()
				time.sleep(10)
				Character.JumpDown()
				mob = Field.FindMob(2400420)
				mob2 = Field.FindMob(2400421)
				if mob.valid or mob2.valid:
					time.sleep(1)
					
				else:
					Character.Teleport(-583, -31)
					time.sleep(2)
					Character.EnterPortal()
					Character.EnterPortal()
					
			elif map in range(940202300, 940202399):
				Character.MoveX(35, 10000)
				Character.JumpDown()
				time.sleep(1)
				mob = Field.FindMob(2400421)
				if mob.valid:
					time.sleep(1)
				else:
					Character.Teleport(1,-638)
					time.sleep(1)
					Character.EnterPortal()
					
			elif map in range(940202400, 940202499):
				Character.Teleport(-1, -638)
				time.sleep(1)
				Character.EnterPortal()
		
		else:
			time.sleep(1)
			
	elif escape != 2:
		rush(940202032)
		Character.MoveX(915, 10000)
		Quest.CompleteQuest(34718, 3001344)
		time.sleep(10)

if GameState.IsInGame() and jobid == 15210 and not Terminal.IsRushing():
	map = Field.GetID()
	level = Character.GetLevel()
	jobid = Character.GetJob()
	pos = Character.GetPos()
	
	escape = Quest.GetQuestState(34818)
	lookback = Quest.GetQuestState(34820)
	if escape != 2:
		rush(940202032)
		Character.MoveX(332, 10000)
		Quest.CompleteQuest(34818, 3001344)
		time.sleep(10)
		
	elif map == 940202032 and escape == 2:
		Quest.StartQuest(34860, 0)
		Character.MoveX(332, 10000)
		Character.EnterPortal()

	elif map in range(940202500, 940202599):
		Character.MoveX(25, 10000)
		Character.EnterPortal()

	elif map in range(940202600, 940202699):	
		Character.MoveX(25, 10000)
		Character.EnterPortal()
			
	elif map in range(940202700, 940202799):
		Character.MoveX(25, 10000)
		Character.EnterPortal()
		
	elif map == 940202036:
		Character.MoveX(0, 200)
	
	elif map == 940202037:
		time.sleep(4)
		Character.Teleport(803,813)
		time.sleep(1)
		Character.EnterPortal()
		
	elif lookback != 2:
		if lookback == 0:
			rush(940202040)
			Quest.StartQuest(34820, 3001343)
			
		elif Quest.CheckCompleteDemand(34820, 3000002) == 0:
			rush(400000000)
			Quest.CompleteQuest(34820, 3000002)
	
	else:
		Terminal.SetRushByLevel(True)
			
	
	#Key.Press(0x11)






