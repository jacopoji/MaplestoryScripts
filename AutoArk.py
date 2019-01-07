import DataType, Character, Field, Inventory, Packet, Terminal, time, GameState, Quest, Key

def StartQuest(quest, npc, map):
	if Terminal.IsRushing():
		time.sleep(1)
	elif mapID != map:
		time.sleep(3)
		Terminal.Rush(map)
	else:
		location = Field.FindNpc(npc) #change
		if location.valid:
			if abs(Character.GetPos().x - location.x) > 400:
				Character.Teleport(location.x, location.y)
		time.sleep(1)
		Quest.StartQuest(quest, npc)
		time.sleep(1)

def CompleteQuest(quest, npc, map):
	if Terminal.IsRushing():
		time.sleep(1)
	elif mapID != map:
		time.sleep(3)
		Terminal.Rush(map)
	else:
		location = Field.FindNpc(npc)
		if location.valid:
			if abs(Character.GetPos().x - location.x) > 400:
				Character.Teleport(location.x, location.y)
		time.sleep(1)
		Quest.CompleteQuest(quest, npc)
		time.sleep(1)

def KillMobAndLoot(map):
	if Terminal.IsRushing():
		time.sleep(1)
	elif mapID != map:
		Terminal.Rush(map)
		time.sleep(3)
	else:
		Terminal.SetCheckBox("Kami Loot", True)
		Terminal.SetCheckBox("Auto Loot", True)
		enableKillMob()
	
def TakePortal(name):
	portal = Field.FindPortal(name)
	if portal.valid:
		if Character.GetPos().x != portal.x:
			Character.Teleport(portal.x, portal.y)
			time.sleep(1)
		else:
			Character.EnterPortal()

def enableKillMob():
	Terminal.SetCheckBox("Skill Injection", True)
	Terminal.SetCheckBox("General FMA", True)
	Terminal.SetCheckBox("Auto MP", True)
	Terminal.SetLineEdit("SISkillID", "155001100")
	Terminal.SetRadioButton("SkillInjection2", True)
	Terminal.SetSlider("sliderMP", 10)
	Terminal.SetComboBox("MPKey", 7)
	Terminal.SetSpinBox("KamiLoot", 10)
	Key.Set(0x22, 2, 2001506)

def disableKillMob():
	Terminal.SetCheckBox("General FMA", False)
	Terminal.SetCheckBox("Skill Injection", False)
	Terminal.SetCheckBox("Kami Loot", False)
	Terminal.SetCheckBox("Auto Loot", False)

def grabFamiliar():
	if Character.IsOwnFamiliar(9960098):
		time.sleep(5)
		Terminal.SetCheckBox("Rush By Level", True)
		Terminal.SetCheckBox("Skill Injection", True)
		Terminal.SetCheckBox("General FMA", True)
		Terminal.SetLineEdit("SISkillID", "155001100")
		Terminal.SetRadioButton("SkillInjection2", True)
		#can add your own stuff to do when it's finished like loading another profile or smth
	else:
		Terminal.SetCheckBox("Rush By Level", False)
		KillMobAndLoot(102010000)
		if Inventory.FindItemByID(2870098).valid:
			disableKillMob()
			time.sleep(2)
			Inventory.UseFamiliarCard(2870098)
			time.sleep(1)
		time.sleep(3)
	
if GameState.IsInGame():
	mapID = Field.GetID()
	if Character.GetJob() == 15001:
		if mapID == 402000615:
			Quest.StartQuest(34901, 0)
	elif Character.GetJob() == 15500:
		quest1 = Quest.GetQuestState(34915)
		quest2 = Quest.GetQuestState(34916)
		quest3 = Quest.GetQuestState(34917)
		quest4 = Quest.GetQuestState(34918)
		quest5 = Quest.GetQuestState(34919)
		quest6 = Quest.GetQuestState(34920)
		quest7 = Quest.GetQuestState(34921)
		quest8 = Quest.GetQuestState(34922)
		quest9 = Quest.GetQuestState(34923)
		quest10 = Quest.GetQuestState(34924)
		quest11 = Quest.GetQuestState(34925)
		quest12 = Quest.GetQuestState(34926)
		quest13 = Quest.GetQuestState(34927)
		quest14 = Quest.GetQuestState(34928)
		quest15 = Quest.GetQuestState(34929)
		quest16 = Quest.GetQuestState(34930)
		quest17 = Quest.GetQuestState(34931)
		quest18 = Quest.GetQuestState(34932)
		quest19 = Quest.GetQuestState(34933)
		quest20 = Quest.GetQuestState(34934)
		quest21 = Quest.GetQuestState(34935)
		quest22 = Quest.GetQuestState(34936)
		quest23 = Quest.GetQuestState(34937)
		quest24 = Quest.GetQuestState(34938)
		quest25 = Quest.GetQuestState(34902)
		if quest1 != 2:
			print("1")
			if quest1 == 0:
				StartQuest(34915, 3001406, 402000615)
			if mapID == 940205000:
				enableKillMob()
		elif quest2 != 2:	
			print("2")
			if quest2 == 0:
				disableKillMob()
				StartQuest(34916, 3001400, 402000600)
			elif quest2 == 1:
				disableKillMob()
				CompleteQuest(34916, 3001400, 402000600)
		elif quest3 != 2:
			print("3")
			if quest3 == 0:
				disableKillMob()
				StartQuest(34917, 3001400, 402000600)
			elif quest3 == 1:
				if Quest.CheckCompleteDemand(34917, 3001400):
					KillMobAndLoot(402000610)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34917, 3001400, 402000600)
		elif quest4 != 2:
			print("4")
			if quest4 == 0:
				disableKillMob()
				StartQuest(34918, 3001400, 402000600)
			elif quest4 == 1:
				disableKillMob()
				CompleteQuest(34918, 3001401, 402000600)
		elif quest5 != 2:
			print("5")
			if quest5 == 0:
				disableKillMob()
				StartQuest(34919, 3001401, 402000600)
			elif quest5 == 1:
				if Quest.CheckCompleteDemand(34919, 3001401):
					KillMobAndLoot(402000611)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34919, 3001401, 402000600)
		elif quest6 != 2:
			print("6")
			if quest6 == 0:
				disableKillMob()
				StartQuest(34920, 3001401, 402000600)
			elif quest6 == 1:
				CompleteQuest(34920, 3001402, 402000600)
		elif quest7 != 2:
			print("7")
			if quest7 == 0:
				disableKillMob()
				StartQuest(34921, 3001402, 402000600)
			elif quest7 == 1:
				if Quest.CheckCompleteDemand(34921, 3001402):
					KillMobAndLoot(402000612)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34921, 3001402, 402000600)
		elif quest8 != 2:
			print("8")
			if quest8 == 0:
				disableKillMob()
				StartQuest(34922, 3001402, 402000600)
			elif quest8 == 1:
				disableKillMob()
				CompleteQuest(34922, 3001403, 402000600)
		elif quest9 != 2:
			print("9")
			if quest9 == 0:
				disableKillMob()
				StartQuest(34923, 3001404, 402000613)
			elif quest9 == 1:
				if Quest.CheckCompleteDemand(34923, 3001404):
					KillMobAndLoot(402000613)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34923, 3001404, 402000613)
		elif quest10 != 2:
			print("10")
			if quest10 == 0:
				disableKillMob()
				StartQuest(34924, 3001400, 402000600)
			elif quest10 == 1:
				disableKillMob()
				CompleteQuest(34924, 3001405, 402000614)
		elif quest11 != 2:
			print("11")
			if quest11 == 0:
				disableKillMob()
				StartQuest(34925, 3001405, 402000614)
			elif quest11 == 1:
				disableKillMob()
				CompleteQuest(34925, 3001400, 402000600)
		elif quest12 != 2:
			print("12")
			if quest12 == 0:
				disableKillMob()
				StartQuest(34926, 3001402, 402000600)
			elif quest12 == 1:
				if Quest.CheckCompleteDemand(34926, 3001402):
					KillMobAndLoot(402000616)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34926, 3001402, 402000600)
		elif quest13 != 2:
			print("13")
			if quest13 == 0:
				disableKillMob()
				StartQuest(34927, 3001401, 402000600)
			elif quest13 == 1:
				if Quest.CheckCompleteDemand(34927, 3001401):
					KillMobAndLoot(402000617)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34927, 3001401, 402000600)
		elif quest14 != 2:
			print("14")
			if quest14 == 0:
				disableKillMob()
				StartQuest(34928, 3001400, 402000600)
			elif quest14 == 1:
				disableKillMob()
				CompleteQuest(34928, 3001407, 402000615)
		elif quest15 != 2:
			print("15")
			if quest15 == 0:
				disableKillMob()
				StartQuest(34929, 3001400, 402000600)		
			elif quest15 == 1:
				disableKillMob()
				CompleteQuest(34929, 3001408, 402000620)
		elif quest16 != 2:
			print("16")
			if quest16 == 0:
				disableKillMob()
				StartQuest(34930, 3001409, 402000621)
			elif quest16 == 1:
				if Quest.CheckCompleteDemand(34930, 3001409):
					KillMobAndLoot(402000621)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34930, 3001409, 402000621)
		elif quest17 != 2:
			print("17")
			if quest17 == 0:
				disableKillMob()
				StartQuest(34931, 3001410, 402000622)
			elif quest17 == 1:
				if Quest.CheckCompleteDemand(34931, 3001410):
					KillMobAndLoot(402000622)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34931, 3001410, 402000622)
		elif quest18 != 2:
			print("18")
			if quest18 == 0:
				disableKillMob()
				StartQuest(34932, 3001411, 402000630)
			elif quest18 == 1:
				disableKillMob()
				CompleteQuest(34932, 3001412, 402000631)
		elif quest19 != 2:
			print("19")
			if quest19 == 0:
				disableKillMob()
				StartQuest(34933, 3001412, 402000631)
			elif quest19 == 1:
				if Quest.CheckCompleteDemand(34933, 3001412):
					KillMobAndLoot(402000631)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34933, 3001412, 402000631)
		elif quest20 != 2:
			print("20")
			if quest20 == 0:
				disableKillMob()
				StartQuest(34934, 3001413, 402000633)
			elif quest20 == 1:
				if Quest.CheckCompleteDemand(34934, 3001413):
					KillMobAndLoot(402000633)
					time.sleep(5)
				else:
					disableKillMob()
					CompleteQuest(34934, 3001413, 402000633)
		elif quest21 != 2:
			print("21")
			if quest21 == 0:
				disableKillMob()
				StartQuest(34935, 3001414, 402000635)
			elif quest21 == 1:
				disableKillMob()
				CompleteQuest(34935, 3001416, 402000648)
		elif quest22 != 2:
			print("22")
			if quest22 == 0:
				disableKillMob()
				StartQuest(34936, 3001415, 402000648)
				time.sleep(2)
				while Field.GetID() == 402090006:
					Key.Press(0x20)
					Key.Press(0x88)
					print("press")
		elif quest23 != 2:
			print("23")
			if quest23 == 0:
				disableKillMob()
				StartQuest(34937, 3001417, 402000644)
			elif quest23 == 1:
				disableKillMob()
				CompleteQuest(34937, 3001417, 402000644)
		elif quest24 != 2:
			print("24")
			if quest24 == 0:
				if Field.GetID() == 402000644:
					disableKillMob()
					StartQuest(34938, 3001423, 402000644)
				elif Field.GetID() == 940205100:
					enableKillMob()
					time.sleep(3)
					TakePortal("next00")
				elif Field.GetID() == 940205200:
					enableKillMob()
					time.sleep(3)
					TakePortal("next00")
				elif Field.GetID() == 940205300:
					enableKillMob()
					time.sleep(3)
					TakePortal("next00")
		elif quest25 != 2:
			print("25")
			if quest25 == 0:
				disableKillMob()
				StartQuest(34902, 0, 402000640)
	elif Character.GetJob() == 15510:
		quest1 = Quest.GetQuestState(34939)
		quest2 = Quest.GetQuestState(34940)
		if quest1 != 2:
			if quest1 == 0:
				disableKillMob()
				StartQuest(34939, 0, 402000640)
			elif quest1 == 1:
				disableKillMob()
				CompleteQuest(34939, 0, 402000640)
		elif quest2 != 2:
			if quest2 == 0:
				if Field.GetID() == 402000640:
					disableKillMob()
					StartQuest(34940, 0, 402000640)
			elif Field.GetID() == 940205400:
				enableKillMob()
				time.sleep(3)
				TakePortal("next00")
			elif Field.GetID() == 940205500:
				enableKillMob()
				time.sleep(3)
				TakePortal("next00")
			elif Field.GetID() == 940205600:
				enableKillMob()
				time.sleep(3)
				TakePortal("next00")
			elif Field.GetID() == 940205900:
				enableKillMob()
				time.sleep(3)
		elif Character.GetLevel() >= 60:
			jobQuest = Quest.GetQuestState(34903)
			if jobQuest != 2:
				if jobQuest == 0:
					Quest.StartQuest(34903, 0)
					time.sleep(5)
				elif jobQuest == 1:
					Quest.CompleteQuest(34903, 0)
					time.sleep(5)
		else:
			grabFamiliar()
			time.sleep(3)
	elif Character.GetJob() == 15511:
		if Character.GetLevel() >= 100:
			jobQuest = Quest.GetQuestState(34904)
			if jobQuest != 2:
				if jobQuest == 0:
					Quest.StartQuest(34904, 0)
					time.sleep(5)
				elif jobQuest == 1:
					Quest.CompleteQuest(34904, 0)
					time.sleep(5)