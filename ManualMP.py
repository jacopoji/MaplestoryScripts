import Character, GameState, Context, DataType, Field, Inventory, Key, Npc, Packet, Quest, Terminal, time, Party,sys,os

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "/SunCat")

try:
	import SunCat, SCLib, SCHotkey
except:
	print("Couldn't find SunCat module")
do_MP_count = 7
buy_tickets = 5
#User Options
#CHANGE THESE VARIABLES
mapSleep = 2.0 #Delay in between entering and exiting map
shortSleep = 0.2 #Increase if lagging
HotKey = 0x78
#DEFINE MP DUNGEON OPTIONS
mossy_tree_forest = "Mossy Tree Forest (Lv.115-124)"
sky_forest = "Sky Forest Training Center (Lv.120-129)"
secret_pirate = "Secret Pirate Hideout (Lv.125-134)"
other_world = "Otherworld Battleground (Lv.135-144)"
dangerous_forest = "Dangerously Isolated Forest (Lv.140-149)"
forbidden_time = "Forbidden Time (Lv.145-154)"
clandestine_ruins = "Clandestine Ruins (Lv.150-159)"
ruined_city = "Ruined City"
leopard_portal = (493,92)
tiger_portal = (661,92)

buy_ticket_header = 0x0508
recv = 0x0684
collide_header = 0x00FE
KannaJobs = [4200, 4210, 4211, 4212]
if SCLib.GetVar("MPDone") is None:
    SCLib.PersistVar("MPDone", False)
if SCLib.GetVar("DoingMP") is None:
	SCLib.PersistVar("DoingMP",False)
if SCLib.GetVar("retry_count") is None:
	SCLib.PersistVar("retry_count",0)
SCLib.StartVars(100)
def KillPersistVarThred():
    print("Stopping vars")
    SCLib.StopVars()
    time.sleep(1)
SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F9

def dungeonSelector():
	charLvl = Character.GetLevel()
	
	if charLvl in range(115,125):
		return (leopard_portal,mossy_tree_forest)
	elif charLvl in range(125,135):
		return (leopard_portal,secret_pirate)
	elif charLvl in range(135,144):
		return (leopard_portal,other_world)
	elif charLvl in range(145,155):
		return (leopard_portal,forbidden_time)
	elif charLvl in range(155,160):
		return (leopard_portal,clandestine_ruins)
	elif charLvl in range(160,250):
		return (tiger_portal,ruined_city)
	#return (leopard_portal,mossy_tree_forest)

def rushToMP():
    fieldid = Field.GetID()
    rushToMPFlag = True
    if fieldid != 951000000:
        while rushToMPFlag:
            field_id_check = Field.GetID()
            if field_id_check == 100000000:
                Character.Teleport(3133,334)
                Character.TalkToNpc(9071003)
                time.sleep(1)
            else:
                Terminal.Rush(100000000)
                time.sleep(1)
            if field_id_check == 951000000:
                print("Complete rushToMP")
                rushToMPFlag = False

def enterDungeon():
	#fieldid = Field.GetID()
	enterDungeonFlag = True
	try_count = 0
	while enterDungeonFlag and try_count < 6:
		try_count += 1
		field_id_check = Field.GetID()
		token = dungeonSelector()
		print("Entering dungeon {}".format(token[1]))
		pos = Character.GetPos()
		if pos.x not in range(token[0][0]-5,token[0][0]+5):
			Character.Teleport(token[0][0],token[0][1])
		time.sleep(1)
		Npc.ClearSelection()
		Character.EnterPortal()
		Npc.RegisterSelection(token[1])
		time.sleep(1)
		if field_id_check != 951000000:
			print("Complete enterDungeon")
			enterDungeonFlag = False

def mapsMP():
    return Field.GetID() >= 952000000 and Field.GetID() <= 954080901

def collide_cash_items():
	oPacket = Packet.COutPacket(collide_header)
	oPacket.EncodeBuffer("** ** ** ** 05")
	Packet.SendPacket(oPacket)

def toggle_rush_by_level(indicator):
	Terminal.SetCheckBox("Rush By Level",indicator)
	Terminal.SetRushByLevel(indicator)

def buy_ticket():
	buy_count = 0
	collide_cash_items()
	time.sleep(0.5)
	total_slots = Inventory.GetItemSlotCount(5)
	empty_slots = Inventory.GetEmptySlotCount(5)
	start_slot = total_slots-empty_slots
	while not GameState.IsInCashShop():
		print("Entering cash shop")
		Terminal.EnterCashShop()
		time.sleep(2)
	while buy_count < buy_tickets:
		time.sleep(3)
		start_slot += 1
		print("Buying ticket number {}".format(buy_count+1))
		buy_ticket_packet = Packet.COutPacket(buy_ticket_header)
		buy_ticket_packet.EncodeBuffer("54 052F83EE 003567E0")
		Packet.SendPacket(buy_ticket_packet)
		rPacket = Packet.WaitForRecv(0x066F,100000000)
		rPacket.Skip(1)
		x = rPacket.ReadLong(3)
		time.sleep(1)
		out = hex(x)
		out = '0x' + out[2:].zfill(8)
		first_byte = out[8:10]
		second_byte = out[6:8]
		third_byte = out[4:6]
		fourth_byte = out[2:4]
		take_out = Packet.COutPacket(buy_ticket_header)
		take_out.EncodeBuffer("0F {} {} {} {} 00 00 00 00 05 {} 00".format(first_byte,second_byte,third_byte,fourth_byte,hex(start_slot).split('x')[1].zfill(2)))
		print("0F {} {} {} {} 00 00 00 00 05 {} 00".format(first_byte,second_byte,third_byte,fourth_byte,hex(start_slot).split('x')[1].zfill(2)))
		Packet.SendPacket(take_out)
		buy_count += 1

	time.sleep(1)
	print("Leaving cash shop")
	Terminal.LeaveCashShop()

def rush_out_MP():
	rush_out_flag = True
	while rush_out_flag:
		rush_out_field = Field.GetID()
		if rush_out_field == 951000000:
			Character.TalkToNpc(9071003)
		if rush_out_field != 951000000 and not mapsMP():
			rush_out_flag = False
		time.sleep(1)

def toggleKillSettings(on):
    if job == 3712:
        Terminal.SetLineEdit("SISkillID","37121003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 6512:
        Terminal.SetLineEdit("SISkillID","65121008")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 3512:
        mech_att(on)
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection",False)
        Terminal.SetCheckBox("Kami Vac",on)
    elif job == 2512:
        Terminal.SetLineEdit("SISkillID","25120003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 4112:
        Terminal.SetLineEdit("SISkillID","41121011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 11212: #beast tamer
        Terminal.SetLineEdit("SISkillID","112000002")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",200)
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        count = 0
        if on:
            while count < 50 and Field.GetMobCount()>0:
                Key.Down(0x44)
                time.sleep(0.1)
                Key.Up(0x44)
                time.sleep(0.1)
                Key.Press(0x44)
                count += 1
    elif job == 15212:
        Terminal.SetLineEdit("SISkillID","152121041")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",30)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 3112:
        Terminal.SetLineEdit("SISkillID","31121010")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 1212:
        Terminal.SetLineEdit("SISkillID","12121055")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 572:
        Terminal.SetLineEdit("SISkillID","5710020")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 132 or job == 2412: #DK or phantom
        Terminal.SetLineEdit("SISkillID","1311011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 15512: #ark
        Terminal.SetLineEdit("SISkillID","155121007")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 6412: #Cadena
        Terminal.SetLineEdit("SISkillID","64121011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetRadioButton("bot/si_cadena",True)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)

    elif job not in KannaJobs:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Kami Vac",on)
        if on:
            if not Terminal.GetCheckBox("Auto Attack"):
                print("Toggle Skill Injection "+str(on))
                Terminal.SetCheckBox("Auto Attack", on)
        else:
            if Terminal.GetCheckBox("Auto Attack"):
                print("Toggle Skill Injection "+str(on))
                Terminal.SetCheckBox("Auto Attack", on)
    if job not in KannaJobs:
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)

if not SCLib.GetVar("MPDone"):
	SCLib.UpdateVar("DoingMP",True)
	Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
	toggle_rush_by_level(False)
	job = Character.GetJob()
	if job == 4212:
		Terminal.SetCheckBox("bot/kanna_kami",True)
		Terminal.SetSpinBox("bot/kanna_kami_delay",5000)
	Terminal.SetSpinBox("AutoDieExp",70)

	if Party.IsInParty():
		Party.LeaveParty()
	if mapsMP():
		print("Waiting for Stages to clear")
		Terminal.SetCheckBox("Portal Teleport [Back Space]", True)
		time.sleep(mapSleep)
		while Field.GetMobCount() > 1:
			print("Mobs not all killed yet")
			time.sleep(2)
		time.sleep(1)
		time.sleep(shortSleep)
		Key.Press(0x08)
		time.sleep(shortSleep)
		time.sleep(0.5)
		Character.EnterPortal()
		time.sleep(mapSleep)
	elif SCLib.GetVar("retry_count") >= do_MP_count:
		#rush_out_flag = True
		SCLib.UpdateVar("MPDone",True)
		SCLib.UpdateVar("DoingMP",False)
		rush_out_MP()
		toggle_rush_by_level(True)
		Terminal.SetCheckBox("bot/kanna_kami",False)
		Terminal.SetCheckBox("map/maprusher/hypertelerock",False)
	else:
		print("Rushing to Monster Park")
		rushToMP()
		print("Entering Dungeon")
		time.sleep(1)