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
	field_id = Field.GetID()
	jobid = Character.GetJob()
	level = Character.GetLevel()
	if jobid == -1 or level == -1:
		#not in game
		continue
	if jobid != 1210 or level < 60:
		break
	if Terminal.IsRushing():
		time.sleep(1)
		continue
	quest1 = Quest.GetQuestState(20880)
	quest2 = Quest.GetQuestState(20881)
	quest3 = Quest.GetQuestState(20882)
	quest4 = Quest.GetQuestState(20883)
	if quest1 != 2:
		if quest1 == 0:
			Quest.StartQuest(20880, 1101002)
		elif quest1 == 1:
			if field_id == 222020100:
				portal = Field.FindPortal("in01")
				if portal.valid:
					Character.Teleport(portal.x, portal.y-20)
					time.sleep(1)
					Character.EnterPortal()
			elif field_id == 222020000:
				Quest.CompleteQuest(20880, 2040052)
			else:
				Terminal.Rush(222020000)
	elif quest2 != 2:
		if quest2 == 0:
			if field_id == 222020000:
				Quest.StartQuest(20881, 2040052)
			else:
				Terminal.Rush(222020000)
		elif quest2 == 1:
			if field_id == 222020000:
				portal = Field.FindPortal("in00")
				if portal.valid:
					Character.Teleport(portal.x, portal.y-20)
					time.sleep(1)
					Character.EnterPortal()
			elif field_id == 922030400:
				Quest.CompleteQuest(20881, 1104302)
			else:
				Terminal.Rush(222020000)
	elif quest3 != 2:
		if quest3 == 0:
			if field_id == 922030400:
				Quest.StartQuest(20882, 1104302)
		elif quest3 == 1:
			if field_id == 922030400:
				if Quest.CheckCompleteDemand(20882, 1104303) != 0:
					time.sleep(1) #bot should kill mobs cause of terminal settings
				else:
					Quest.CompleteQuest(20882, 1104303)
	elif quest4 != 2:
		if quest4 == 0:
			if field_id == 922030400:
				Quest.StartQuest(20883, 1104303)
		elif quest4 == 1:
			if field_id == 130000000:
				Quest.CompleteQuest(20883, 1101002)
			else:
				Terminal.Rush(130000000)