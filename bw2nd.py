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
import sys


Terminal.SetRushByLevel(False)

while True:
	time.sleep(1)

	field_id = Field.GetID()
	jobid = Character.GetJob()
	level = Character.GetLevel()
	if jobid == -1 or level == -1:
		#not in game
		continue

	if jobid >= 1200:
		medal = Inventory.FindItemByID(1142067)
		if medal.valid:
			Inventory.SendChangeSlotPositionRequest(1, medal.pos, -49, -1) #49: GMS , -21: JMS
			continue
		else:
			break
	elif level < 30:
		break

        if level < 30:
                break
	if Terminal.IsRushing():
		continue

	quest1 = Quest.GetQuestState(20870)
	quest2 = Quest.GetQuestState(20872)
	if quest1 == 0:
		Quest.StartQuest(20870, 1101002)
	elif quest1 == 1:
		if field_id != 130000000:
			Terminal.Rush(130000000)
		else:
			if Character.GetPos().x != -870:
				Character.Teleport(-870, 88)
				time.sleep(1)
			Quest.CompleteQuest(20870, 1101002)
	elif quest2 == 0:
		if field_id != 130000000:
			Terminal.Rush(130000000)
		else:
			if Character.GetPos().x != -870:
				Character.Teleport(-870, 88)
				time.sleep(1)
			Quest.StartQuest(20872, 1101004)
	elif quest2 == 1:
		if field_id == 913001000 or field_id == 913001001 or field_id == 913001002:
			if Quest.CheckCompleteDemand(20872, 1101004) == 0:
				# leave that map
				Character.TalkToNpc(1102001)
			else:
				# bot should be attacking now and killing mobs cause of the settings inside terminal (fma, flame orb hack auto att, blabla)
				time.sleep(1)
		elif field_id == 130020000:
			if Quest.CheckCompleteDemand(20872, 1101004) == 0:
				Terminal.Rush(130000000)
			else:
				portal = Field.FindPortal("in01")
				if portal.valid:
					Character.Teleport(portal.x, portal.y - 20)
					time.sleep(1)
					Character.EnterPortal()
		elif field_id == 130000000:
			if Quest.CheckCompleteDemand(20872, 1101004) == 0:
				if Character.GetPos().x != -870:
					Character.Teleport(-870, 88)
					time.sleep(1)
				Quest.CompleteQuest(20872, 1101004)
			else:
				Terminal.Rush(130020000)
		else:
			if Quest.CheckCompleteDemand(20872, 1101004) == 0:
				Terminal.Rush(130000000)
			else:
				Terminal.Rush(130020000)
