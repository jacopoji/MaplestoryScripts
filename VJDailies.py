import Character
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time
import GameState
import datetime

def RushCheck(ID):
	Terminal.SetRushByLevel(False)
	if Field.GetID() != ID:
		Terminal.Rush(ID)
		while Terminal.IsRushing():
			time.sleep(1)
	time.sleep(10)
		
def RushAndComplete(completemap, questid, npcid):
	Terminal.SetRushByLevel(False)
	if Field.GetID() != completemap:
		Terminal.Rush(completemap)
		while Terminal.IsRushing():
			time.sleep(1)
	else:
		pos = Character.GetPos()
		if completemap == 450001000:
			if pos.x != -1941:
				Character.Teleport(-1941, 60)
		if completemap == 450001112:
			if pos.y != -710:
				Character.Teleport(108, -710)
		if completemap == 450001216:
			if pos.x != 1329:
				Character.Teleport(1329, 177)
		Quest.CompleteQuest(questid, npcid)
	time.sleep(2)

starthour = 21

if GameState.IsInGame() and datetime.datetime.now().hour == starthour:
	if Quest.GetQuestState(34129) != 2:
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
		completedaily = Quest.GetQuestState(34129)

		if completedaily == 0:
			Quest.StartQuest(34129, 3003104)
			Npc.ClearSelection()
			Npc.RegisterSelection("Those are all the quests I want to swap out.")
			time.sleep(5)
			
		if daily1 == 1:
			while Quest.CheckCompleteDemand(34130, 3003104):
				RushCheck(450001010)
			while Quest.CheckCompleteDemand(34130, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34130, 3003104)
						
		if daily2 == 1:
			while Quest.CheckCompleteDemand(34131, 3003104):
				RushCheck(450001012)
			while Quest.CheckCompleteDemand(34131, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34131, 3003104)
									
		if daily3 == 1:
			while Quest.CheckCompleteDemand(34132, 3003104):
				RushCheck(450001014)
			while Quest.CheckCompleteDemand(34132, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34132, 3003104)

		if daily4 == 1:
			while Quest.CheckCompleteDemand(34133, 3003104):
				RushCheck(450001016)
			while Quest.CheckCompleteDemand(34133, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34133, 3003104)	
		
		if daily5 == 1:
			while Quest.CheckCompleteDemand(34134, 3003104):
				RushCheck(450001110)
			while Quest.CheckCompleteDemand(34134, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34134, 3003104)
						
		if daily6 == 1:
			while Quest.CheckCompleteDemand(34135, 3003104):
				RushCheck(450001112)
			while Quest.CheckCompleteDemand(34135, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34135, 3003104)	
			
		if daily7 == 1:
			while Quest.CheckCompleteDemand(34136, 3003104):
				RushCheck(450001114)
			while Quest.CheckCompleteDemand(34136, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34136, 3003104)
						
		if daily8 == 1:
			while Quest.CheckCompleteDemand(34137, 3003104):
				RushCheck(450001210)
			while Quest.CheckCompleteDemand(34137, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34137, 3003104)

		if daily9 == 1:
			while Quest.CheckCompleteDemand(34138, 3003104):
				RushCheck(450001210)
			while Quest.CheckCompleteDemand(34138, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34138, 3003104)
			
		if daily10 == 1:
			while Quest.CheckCompleteDemand(34139, 3003104):
				RushCheck(450001010)
			while Quest.CheckCompleteDemand(34139, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34139, 3003104)

		if daily11 == 1:
			while Quest.CheckCompleteDemand(34140, 3003104):
				RushCheck(450001012)
			while Quest.CheckCompleteDemand(34140, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34140, 3003104)

		if daily12 == 1:
			while Quest.CheckCompleteDemand(34141, 3003104):
				RushCheck(450001014)
			while Quest.CheckCompleteDemand(34141, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34141, 3003104)
			
		if daily13 == 1:
			while Quest.CheckCompleteDemand(34142, 3003104):
				RushCheck(450001016)
			while Quest.CheckCompleteDemand(34142, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34142, 3003104)
									
		if daily14 == 1:
			while Quest.CheckCompleteDemand(34143, 3003104):
				RushCheck(450001110)
			while Quest.CheckCompleteDemand(34143, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34143, 3003104)
						
		if daily15 == 1:
			while Quest.CheckCompleteDemand(34144, 3003104):
				RushCheck(450001112)
			while Quest.CheckCompleteDemand(34144, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34144, 3003104)
						
		if daily16 == 1:
			while Quest.CheckCompleteDemand(34145, 3003104):
				RushCheck(450001114)
			while Quest.CheckCompleteDemand(34145, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34145, 3003104)
						
		if daily17 == 1:
			while Quest.CheckCompleteDemand(34146, 3003104):
				RushCheck(450001210)
			while Quest.CheckCompleteDemand(34146, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34146, 3003104)
						
		if daily18 == 1:
			while Quest.CheckCompleteDemand(34147, 3003104):
				RushCheck(450001210)
			while Quest.CheckCompleteDemand(34147, 3003104) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001000, 34147, 3003104)
				
		if daily19 == 1:
			while Quest.CheckCompleteDemand(34148, 3003107):
				RushCheck(450001013)
			while Quest.CheckCompleteDemand(34148, 3003107) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001013, 34148, 3003107)
					
		if daily20 == 1:
			while Quest.CheckCompleteDemand(34149, 3003108):
				RushCheck(450001112)
			while Quest.CheckCompleteDemand(34149, 3003108) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001112, 34149, 3003108)
										
		if daily21 == 1:
			while Quest.CheckCompleteDemand(34150, 3003109):
				RushCheck(450001216)
			while Quest.CheckCompleteDemand(34150, 3003109) == False and Inventory.GetEmptySlotCount(1) > 0:
				RushAndComplete(450001216, 34150, 3003109)
				
		if completedaily == 1:
			while Quest.CheckCompleteDemand(34129, 3003104) == False and Inventory.GetEmptySlotCount(1) > 2:
				RushAndComplete(450001000, 34129, 3003104)