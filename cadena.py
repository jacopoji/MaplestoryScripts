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

def EnterPortal(name):
	portal = Field.FindPortal(name)
	pos = Character.GetPos()
	if pos.x != portal.x:
		Character.Teleport(portal.x, portal.y-20)
	else:
		Character.EnterPortal()

if GameState.IsInGame():
	time.sleep(2)
	quest1 = Quest.GetQuestState(34600)
	quest2 = Quest.GetQuestState(34601)
	quest3 = Quest.GetQuestState(34602)
	quest4 = Quest.GetQuestState(34603)
	quest5 = Quest.GetQuestState(34656)
	quest6 = Quest.GetQuestState(34604)
	quest7 = Quest.GetQuestState(34605)
	quest8 = Quest.GetQuestState(34606)
	quest9 = Quest.GetQuestState(34607)
	quest10 = Quest.GetQuestState(34608)
	quest11 = Quest.GetQuestState(34609)
	quest12 = Quest.GetQuestState(34610)
	quest13 = Quest.GetQuestState(34611)
	quest14 = Quest.GetQuestState(34612)
	quest15 = Quest.GetQuestState(34613)
	quest16 = Quest.GetQuestState(34614)
	quest17 = Quest.GetQuestState(34615)
	quest18 = Quest.GetQuestState(34616)
	quest19 = Quest.GetQuestState(34617)
	quest20 = Quest.GetQuestState(34618)
	quest21 = Quest.GetQuestState(34619)
	quest22 = Quest.GetQuestState(34620)
	quest23 = Quest.GetQuestState(34621)
	quest24 = Quest.GetQuestState(34622)
	quest25 = Quest.GetQuestState(34623)
	quest26 = Quest.GetQuestState(34624)
	quest27 = Quest.GetQuestState(34625)
	mapid = Field.GetID()
	if quest1 != 2:
		if quest1 == 0:
			Quest.StartQuest(34600, 0)
			time.sleep(10)
		elif mapid == 940200500:
			EnterPortal("west00")
		elif mapid == 940200501:
			EnterPortal("up00")
	if quest2 != 2:
		if quest2 == 0:
			if mapid == 940200502:
				Quest.StartQuest(34601, 3001221)
			elif mapid == 940200600 or 940200601:
				Key.Press(0x11)
				time.sleep(1)
		elif quest2 == 1:
			Quest.CompleteQuest(34601, 3001221)
	elif quest3 != 2:
		if mapid == 402000002:
			if quest3 == 0:
				Quest.StartQuest(34602, 3001202)
				time.sleep(10)
			elif quest3 == 1:
				Npc.ClearSelection()
				Npc.RegisterSelection("remain")
				Npc.RegisterSelection("Never")
				Quest.CompleteQuest(34602, 3001202)
				time.sleep(8)
		else:
			Terminal.Rush(402000002)
	elif quest4 != 2:
		if mapid == 402000002:
			if quest4 == 0:
				Quest.StartQuest(34603, 3001202)
			elif quest4 == 1:
				if Quest.CheckCompleteDemand(34603, 3001202) == 0:
					Quest.CompleteQuest(34603, 3001202)
				else:
					Inventory.UseItem(2437264)
		else:
			Terminal.Rush(402000002)
	elif quest5 != 2:
		if mapid != 402000001:
			Terminal.Rush(402000001)
		else:
			if quest5 == 0:
				Quest.StartQuest(34656, 3001200)
	elif quest6 != 2:
		if mapid != 402000001:
			Terminal.Rush(402000001)
		else:
			if quest6 == 0:
				Quest.StartQuest(34604, 3001200)
			elif quest6 == 1:
				pos = Character.GetPos()
				if pos.x != -308:
					Character.Teleport(-308, 304)
				else:
					Quest.CompleteQuest(34604, 3001210)
	elif quest7 != 2:
		if quest7 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.StartQuest(34605, 3001210)
		elif quest7 == 1:
			if Quest.CheckCompleteDemand(34605, 3001210) == 0:
				if mapid != 402000001:
					Terminal.Rush(402000001)
				else:
					Quest.CompleteQuest(34605, 3001210)
			else:
				if mapid != 402000110:
					Terminal.Rush(402000110)
	elif quest8 != 2:
		if quest8 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.StartQuest(34606, 3001210)
		elif quest8 == 1:
			if Quest.CheckCompleteDemand(34606, 3001210) == 0:
				if mapid != 402000001:
					Terminal.Rush(402000001)
				else:
					Quest.CompleteQuest(34606, 3001210)
			else:
				if mapid != 402000111:
					Terminal.Rush(402000111)
	elif quest9 != 2:
		if quest9 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.StartQuest(34607, 3001210)
		elif quest9 == 1:
			if Quest.CheckCompleteDemand(34607, 3001210) == 0:
				if mapid != 402000001:
					Terminal.Rush(402000001)
				else:
					Quest.CompleteQuest(34607, 3001210)
			elif mapid != 402000112:
				Terminal.Rush(402000112)
	elif quest10 != 2:
		if quest10 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				pos = Character.GetPos()
				if pos.x != -308:
					Character.Teleport(-308, 304)
				else:
					Quest.StartQuest(34608, 3001210)
		if quest10 == 1:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.CompleteQuest(34608, 3001203)
	elif quest11 != 2:
		if quest11 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.StartQuest(34609, 3001210)
		elif quest11 == 1:
			if Quest.CheckCompleteDemand(34609, 3001210) == 0:
				if mapid != 402000001:
					Terminal.Rush(402000001)
				else:
					Quest.CompleteQuest(34609, 3001210)
			else:
				if mapid != 402000220:
					Terminal.Rush(402000220)
	elif quest12 != 2:
		if quest12 == 0:
			if mapid != 402000200:
				Terminal.Rush(402000200)
			else:
				Quest.StartQuest(34610, 3001218)
		elif quest12 == 1:
			Quest.CompleteQuest(34610, 3001218)
			Terminal.Sleep(3)
	elif quest13 != 2:
		if quest13 == 0:
			if mapid == 940200700:
				time.sleep(8)
				EnterPortal("next00")
				time.sleep(3)
			elif mapid == 940200800:
				time.sleep(8)
				EnterPortal("next00")
				time.sleep(3)
			elif mapid == 940200900:
				time.sleep(8)
				EnterPortal("next00")
				time.sleep(3)
			else:
				pos = Character.GetPos()
				if pos.x != -506:
					Character.Teleport(-506, 45)
					time.sleep(2)
				else:
					Quest.StartQuest(34611, 3001218)
		elif quest13 == 1:
			if mapid == 940200900:
				EnterPortal("next00")
				time.sleep(5)
			if mapid == 402000210:
				Quest.CompleteQuest(34611, 3001214)
	elif quest14 != 2:
		if quest14 == 0:
			Quest.StartQuest(34612, 3001214)
		elif quest14 == 1:
			Quest.CompleteQuest(34612, 3001214)
			time.sleep(2)
	elif quest15 != 2:
		if quest15 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				time.sleep(3)
				Quest.StartQuest(34613, 0)
		elif quest15 == 1:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.CompleteQuest(34613, 3001210)
				time.sleep(2)
	elif quest16 != 2:
		if quest16 == 0:
			Quest.StartQuest(34614, 0)
		elif quest16 == 1:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				pos = Character.GetPos()
				if pos.x != -98:
					Character.Teleport(-98, 304)
				else:
					Quest.CompleteQuest(34614, 3001226)
	elif quest17 != 2:
		if quest17 == 0:
			Quest.StartQuest(34615, 0)
			time.sleep(3)
		elif quest17 == 1:
			# Talk to Gusto
			Terminal.Rush(402000200)
			while Terminal.IsRushing():
				time.sleep(5)
			Character.TalkToNpc(3001218)
			time.sleep(3)

			# Talk to Corbo
			Terminal.Rush(402000100)
			while Terminal.IsRushing():
				time.sleep(5)
			Character.TalkToNpc(3001219)
			time.sleep(3)

			# Talk to Antuin
			Terminal.Rush(402000000)
			while Terminal.IsRushing():
				time.sleep(5)
			pos = Character.GetPos()
			if pos.x != -1639:
				Character.Teleport(-1639, 35-20)
				time.sleep(3)
			Character.TalkToNpc(3001212)
			time.sleep(8)
	elif quest18 != 2:
		if quest18 == 0:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.StartQuest(34616, 0)
		elif quest18 == 1:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.CompleteQuest(34616, 3001204)
	elif quest19 != 2:
		if quest19 == 0:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.StartQuest(34617, 3001204)
		elif quest19 == 1:
			if Quest.CheckCompleteDemand(34617, 3001204) == 0:
				if mapid != 402000000:
					Terminal.Rush(402000000)
				else:
					pos = Character.GetPos()
					if pos.x != -1639:
						Character.Teleport(-1639, 35 - 20)
					else:
						Quest.CompleteQuest(34617, 3001204)
			else:
				if mapid != 402000120:
					Terminal.Rush(402000120)
	elif quest20 != 2:
		if quest20 == 0:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.StartQuest(34618, 3001204)
		elif quest20 == 1:
			if Quest.CheckCompleteDemand(34618, 3001204) == 0:
				if mapid != 402000000:
					Terminal.Rush(402000000)
				else:
					pos = Character.GetPos()
					if pos.x != -1639:
						Character.Teleport(-1639, 35 - 20)
					else:
						Quest.CompleteQuest(34618, 3001204)
			else:
				if mapid != 402000121:
					Terminal.Rush(402000121)
	elif quest21 != 2:
		if quest21 == 0:
			while Field.GetID() == 940200507:
				Key.Press(0x20)
				Key.Up(0x20)
				time.sleep(0.1)
			else:
				pos = Character.GetPos()
				if pos.x != -1701:
					Character.Teleport(-1701, 27 - 20)
					time.sleep(3)
				Quest.StartQuest(34619, 3001204)
	elif quest22 != 2:
		if quest22 == 0:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.StartQuest(34620, 3001212)
		elif quest22 == 1:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.CompleteQuest(34620, 3001212)
	elif quest23 != 2:
		if quest23 == 0:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.StartQuest(34621, 0)
		elif quest23 == 1:
			if Quest.CheckCompleteDemand(34621, 3001228) == 0:
				if mapid != 402000000:
					Terminal.Rush(402000000)
				else:
					Quest.CompleteQuest(34621, 3001228)
			else:
				if mapid != 402000122:
					Terminal.Rush(402000122)
	elif quest24 != 2:
		if quest24 == 0:
			if mapid != 402000000:
				Terminal.Rush(402000000)
			else:
				Quest.StartQuest(34622, 0)
		elif quest24 == 1:
			if mapid != 402000301:
				Terminal.Rush(402000301)
			else:
				Quest.CompleteQuest(34622, 3001220)
	elif quest25 != 2:
		if quest25 == 0:
			if mapid == 940201000:
				time.sleep(1)
			elif mapid != 402000301:
				Terminal.Rush(402000301)
			else:
				Quest.StartQuest(34623, 3001223)
		elif quest25 == 1:
			if mapid == 402000301:
				Quest.CompleteQuest(34623, 3001211)
	elif quest26 != 2:
		if quest26 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.StartQuest(34624, 3001200)
		elif quest26 == 1:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.CompleteQuest(34624, 3001200)
	elif quest27 != 2:
		if quest27 == 0:
			if mapid != 402000001:
				Terminal.Rush(402000001)
			else:
				Quest.StartQuest(34625, 3001200)
		elif quest27 == 1:
			if mapid != 402000400:
				Terminal.Rush(402000400)
			else:
				Quest.CompleteQuest(34625, 3001205)
	if Character.GetJob() == 6400 and Character.GetLevel() >= 30:
		Quest.StartQuest(34657, 3001250)