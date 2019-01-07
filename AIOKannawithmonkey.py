#do Monster park how many times?
do_MP = True
do_MP_count = 2
buy_tickets = 1

#Starforce items or not
star_force = True
star_force_level = 10
safeguard = True
whitelist = []

#Zakum
DoZakumDaily=True

#Do IA rerolling
DoIA = True

#Do Cubing
DoCube = True
buy_cube_number = 10 # 720M
#Key to restart pers. variables
HotKey = 0x7A

#store mesos
storage_map_id = 550000000
storage_npc_id = 9270054

#headers that might need to be updated every game update
#headers updated for v199
store_header = 0x00F5
block_header = 0x0695
buy_ticket_header = 0x0539
recv = 0x06CB
SF_header = 0x0138
StarForceRecv = 0x014D
RerollHeader = 0x018F #does not need to be updated anymore
IARecv = 0x00E5 #does not need to be updated anymore
collide_header = 0x0104
potential_header = 0x013E
potential_recv = 0x0271
BlockBuyHeader = 0x067C
BuyItemHeader = 0x00F4
#oPacket.EncodeBuffer("** ** ** 00 7F 00 01 00") potential reveal
#rPacket = Packet.WaitForRecv(0x0254,5000)
#1oPacket.EncodeBuffer("14A3884B 01")  collide items
#packet is 04EE 54 052F83EE 003567E0
#wait for receive header 066F 0D [thing inside is the unique item id]
#take out item is packet 0x04EE [0F"UNIQUEITEMID"4C 05"ITEMSLOT"00]
level_149_exp = 39306677
#equip slot numbers
helmet_slot = -1
top_slot = -5
shoe_slot = -7
glove_slot = -8
cape_slot = -9
weapon_slot = -11
eye_slot = -3
face_slot = -2
earring_slot = -4
ring1_slot = -12
ring2_slot = -13
ring3_slot = -15
ring4_slot = -16
necklace_slot = -17
emblem_slot = -61
#pensalir gear
pensalir_mage_cape = 1102719
pensalir_mage_helmet = 1004230
pensalir_mage_gloves = 1082609
pensalir_mage_shoes = 1072968
pensalir_mage_overall = 1052800
utgard_fan = 1552102
#accessories
aquatic_letter_eye = 1022231
condensed_power_crystal = 1012478
half_earrings = 1032022
rose_earrings = 1032017
horntail_ring = 1113149
horntail_earrings = 1032241
horntail_necklace = 1122000
chaos_horntail_necklace = 1122076
kanna_ring = 1113155
greed_pendant = 1122219
blackgate_mask = 1012535
blackgate_necklace = 1122312
blackgate_ring = 1113185
#lists
equip_slot_list = [helmet_slot,top_slot,shoe_slot,glove_slot,cape_slot,weapon_slot]
equip_valid_list = [pensalir_mage_cape,pensalir_mage_gloves,pensalir_mage_helmet,pensalir_mage_overall,pensalir_mage_shoes,utgard_fan]
accessory_list = [aquatic_letter_eye,condensed_power_crystal,half_earrings,horntail_ring,horntail_necklace,chaos_horntail_necklace,kanna_ring,greed_pendant,blackgate_mask,blackgate_necklace,blackgate_ring]
accessory_slot_list = [eye_slot,face_slot,earring_slot,ring1_slot,ring2_slot,ring3_slot,ring4_slot,necklace_slot]
ring_list = [kanna_ring,blackgate_ring,horntail_ring]
face_list = [condensed_power_crystal,blackgate_mask]
eye_list = [aquatic_letter_eye]
earring_list = [half_earrings,rose_earrings,horntail_earrings]
necklace_list = [greed_pendant,blackgate_necklace,chaos_horntail_necklace,horntail_necklace]
blackgate_eqp = [1004549, 1012535, 1052952, 1082658, 1102840, 1113185, 1122312, 1132289, 1152191]

snail_pet_box = 2434265 
#no potential, item.grade = 0
#rare, item.grade = 1

####TODO LIST:
####Auto buy ticket					done
####AUTO ZAKUM                      done
####auto switch profile to farming  done
####AUTO buy cubes					done
####auto cube potentials			done
####Auto IA                         done

import Character,Context,DataType,Field,Inventory,Key,Npc,Packet,Quest,Terminal,time,GameState,sys,os,Party, json,math,Login

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "/SunCat")

try:
	import SunCat, SCLib, SCHotkey
except:
	print("Couldn't find SunCat module")

SCLib.StartVars()
###persist variables
if SCLib.GetVar("MPDone") is None:
    SCLib.PersistVar("MPDone", False)
if SCLib.GetVar("DoingMP") is None:
	SCLib.PersistVar("DoingMP",False)
if SCLib.GetVar("retry_count") is None:
	SCLib.PersistVar("retry_count",0)
if SCLib.GetVar("KillZakumDaily") is None:
	SCLib.PersistVar("KillZakumDaily", DoZakumDaily)
if SCLib.GetVar("HasSpawned") is None:
	SCLib.PersistVar("HasSpawned", False)
if SCLib.GetVar("NowLockedVar") is None:
	SCLib.PersistVar("NowLockedVar", False)
if SCLib.GetVar("DoingZakum") is None:
	SCLib.PersistVar("DoingZakum",False)
if SCLib.GetVar("zakum_retry_count") is None:
	SCLib.PersistVar("zakum_retry_count",0)
if SCLib.GetVar("cube_lock") is None:
	SCLib.PersistVar("cube_lock",False)
if SCLib.GetVar("checked_equip") is None:
	SCLib.PersistVar("checked_equip",False)	
if SCLib.GetVar("took_off") is None:
	SCLib.PersistVar("took_off",False)
if SCLib.GetVar("withdraw_flag") is None:
	SCLib.PersistVar("withdraw_flag",False)
if SCLib.GetVar("DoingBG") is None:
	SCLib.PersistVar("DoingBG",False)
if SCLib.GetVar("GettingEarring") is None:
	SCLib.PersistVar("GettingEarring",False)
if SCLib.GetVar("GetEarringDone") is None:
	SCLib.PersistVar("GetEarringDone",False)
if SCLib.GetVar("EquipMesoDone") is None:
	SCLib.PersistVar("EquipMesoDone",False)
if SCLib.GetVar("BuyingExpansion") is None:
	SCLib.PersistVar("BuyingExpansion",False)
if SCLib.GetVar("GettingLep") is None:
	SCLib.PersistVar("GettingLep",False)
if SCLib.GetVar("farm_counter") is None:
	SCLib.PersistVar("farm_counter",0)

HasSpawned = SCLib.GetVar("HasSpawned")
NowLockedVar = SCLib.GetVar("NowLockedVar")
KillZakumDaily = SCLib.GetVar("KillZakumDaily")
jobid = Character.GetJob()
level = Character.GetLevel()
field_id = Field.GetID()

#quest states
second_job_quest = Quest.GetQuestState(57458)
inner1 = Quest.GetQuestState(12394)
inner2 = Quest.GetQuestState(12395)
inner3 = Quest.GetQuestState(12396)

#DEFINE MP DUNGEON OPTIONS
mapSleep = 2.0 #Delay in between entering and exiting map
shortSleep = 0.2 #Increase if lagging
mossy_tree_forest = "Mossy Tree Forest (Lv.115-124)"
sky_forest = "Sky Forest Training Center (Lv.120-129)"
secret_pirate = "Secret Pirate Hideout (Lv.125-134)"
other_world = "Otherworld Battleground (Lv.135-144)"
dangerous_forest = "Dangerously Isolated Forest (Lv.140-149)"
forbidden_time = "Forbidden Time (Lv.145-154)"
clandestine_ruins = "Clandestine Ruins (Lv.150-159)"
leopard_portal = (493,92)
tiger_portal = (661,92)

#map ids
CheifsResidence = 211000001
TheDoorToZakum = 211042300
EntranceToZakumAlter = 211042400
ZakumsAltar = [280030100,280030101,280030102,280030103,280030104]
TheCaveOfTrials3Zakum = 211042200
blackgate_maps = [610050000,610051300, 610051400, 610051500, 610051600, 610051700, 610051800, 610051900, 610052000, 610050100, 610050200, 610050600, 610050700, 610050800, 610051200, 610050300, 610050400, 610050500, 610050900, 610051000, 610051100]
henesys = 100000000

#npc ids
NpcRobeiraMagicianInstructor = 2020009

#mob ids
NormalZakum = 8800002
NormalZakumv1 = 8800000
NormalZakumv2 = 8800001	
blackgate_boss = [9480235, 9480236, 9480237, 9480238, 9480239]


padding = 20

try:
	SCHotkey.StartHotkeys(100)
except:
	SCHotkey.StopHotkeys()
def KillPersistVarThred():
	print("Restarting SCLib variables")
	SCLib.StopVars()
	time.sleep(1)

SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F11

def toggle_rush_by_level(indicator):
	Terminal.SetCheckBox("Rush By Level",indicator)
	Terminal.SetRushByLevel(indicator)

def settings_first_job():
	if Terminal.GetCheckBox("Auto Attack"):
		Terminal.SetCheckBox("Auto Attack",False)
		Terminal.SetSpinBox("autoattack_spin",100)
		Terminal.SetComboBox("AttackKey",33)
	Terminal.SetSpinBox("SkillInjection", 100)
	Terminal.SetLineEdit("SISkillID","42001006")
	if not Terminal.GetCheckBox("Skill Injection"):
		Terminal.SetCheckBox("Skill Injection",True)
	if Terminal.GetComboBox("AttackKey") != 33:
		Terminal.SetSpinBox("autoattack_spin",100)
		Terminal.SetComboBox("AttackKey",33)
	if Terminal.GetCheckBox("bot/kanna_kami"):
		Terminal.SetCheckBox("bot/kanna_kami",False)
		Terminal.SetSpinBox("bot/kanna_kami_delay",1000)
	if Terminal.GetCheckBox("Legit Vac"):
		Terminal.SetCheckBox("Legit Vac",False)
	if not Terminal.GetCheckBox("Kami Vac"):
		Terminal.SetCheckBox("Kami Vac",True)
	if Terminal.GetCheckBox("charm_fma"):
		Terminal.SetCheckBox("charm_fma",False)
	if Terminal.GetCheckBox("MonkeySpiritsNDcheck"):
		Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
	if Terminal.GetCheckBox("Kami Loot"):
		Terminal.SetCheckBox("Kami Loot",False)
		Terminal.SetCheckBox("Auto Loot",False)
	if Terminal.GetCheckBox('filter_equip'):
		Terminal.SetCheckBox('filter_equip',False)
	if not Terminal.GetCheckBox("Auto Equip"):
		Terminal.SetCheckBox("Auto Equip",True)
	if not Terminal.GetCheckBox("Rush By Level"):
		Terminal.SetCheckBox("Rush By Level",True)
	Key.Set(0x44, 1, 42001000)
	Terminal.SetCheckBox("settings/mesologout",False)
	Terminal.SetCheckBox("Speedy Gonzales",False)
def settings_second_job():
	if Terminal.GetCheckBox("Auto Attack"):
		Terminal.SetCheckBox("Auto Attack",False)
	if Terminal.GetCheckBox("Legit Vac"):
		Terminal.SetCheckBox("Legit Vac",False)
	if Terminal.GetCheckBox("Skill Injection"):
		Terminal.SetCheckBox("Skill Injection",False)
	if not Terminal.GetCheckBox("charm_fma"):
		Terminal.SetSpinBox("charm_delay",100)
		Terminal.SetCheckBox("charm_fma",True)
	if not Terminal.GetCheckBox("bot/kanna_kami"):
		Terminal.SetCheckBox("bot/kanna_kami",True)
		Terminal.SetSpinBox("bot/kanna_kami_delay",20000)
	if Terminal.GetCheckBox("Kami Vac"):
		Terminal.SetCheckBox("Kami Vac",False)
	if Terminal.GetCheckBox("MonkeySpiritsNDcheck"):
		Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
	if Terminal.GetCheckBox("Kami Loot"):
		Terminal.SetCheckBox("Kami Loot",False)
		Terminal.SetCheckBox("Auto Loot",False)
	if Terminal.GetCheckBox('filter_equip'):
		Terminal.SetCheckBox('filter_equip',False)
	if not Terminal.GetCheckBox("Auto Equip"):
		Terminal.SetCheckBox("Auto Equip",True)
	if not Terminal.GetCheckBox("Rush By Level"):
		Terminal.SetCheckBox("Rush By Level",True)
	Terminal.SetCheckBox("settings/mesologout",False)
def settings_third_job():
	if Terminal.GetCheckBox("Legit Vac"):
		Terminal.SetCheckBox("Legit Vac",False)
	if Terminal.GetCheckBox("Skill Injection"):
		Terminal.SetCheckBox("Skill Injection",False)
	if not Terminal.GetCheckBox("charm_fma"):
		Terminal.SetSpinBox("charm_delay",100)
		Terminal.SetCheckBox("charm_fma",True)
	if not Terminal.GetCheckBox("Summon Kishin"):
		Terminal.SetCheckBox("Summon Kishin",True)
	if not Terminal.GetCheckBox("bot/kanna_kami"):
		Terminal.SetCheckBox("bot/kanna_kami",True)
		Terminal.SetSpinBox("bot/kanna_kami_delay",20000)
	if Terminal.GetCheckBox("Kami Vac"):
		Terminal.SetCheckBox("Kami Vac",False)
	if Terminal.GetCheckBox("MonkeySpiritsNDcheck"):
		Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
	if not Terminal.GetCheckBox("Auto Attack"):
		Terminal.SetCheckBox("Auto Attack",True)
		Terminal.SetSpinBox("autoattack_spin",7500)
		Terminal.SetComboBox("AttackKey",36)
	if Terminal.GetComboBox("AttackKey") != 36:
		Terminal.SetSpinBox("autoattack_spin",7500)
		Terminal.SetComboBox("AttackKey",36)
	if Terminal.GetCheckBox("Kami Loot"):
		Terminal.SetCheckBox("Kami Loot",False)
		Terminal.SetCheckBox("Auto Loot",False)
	if Terminal.GetCheckBox('filter_equip'):
		Terminal.SetCheckBox('filter_equip',False)
	if not Terminal.GetCheckBox("Auto Equip"):
		Terminal.SetCheckBox("Auto Equip",True)
	if not Terminal.GetCheckBox("Rush By Level"):
		Terminal.SetCheckBox("Rush By Level",True)
	Key.Set(0x47,1,42111003)
	Terminal.SetCheckBox("settings/mesologout",False)
def settings_fourth_job():
	level = Character.GetLevel()
	if not Terminal.GetCheckBox("Auto Attack"):
		Terminal.SetCheckBox("Auto Attack",True)
		Terminal.SetSpinBox("autoattack_spin",7500)
		Terminal.SetComboBox("AttackKey",36)
	if Terminal.GetComboBox("AttackKey") != 36:
		Terminal.SetSpinBox("autoattack_spin",7500)
		Terminal.SetComboBox("AttackKey",36)
	if Terminal.GetCheckBox("Legit Vac"):
		Terminal.SetCheckBox("Legit Vac",False)
	if Terminal.GetCheckBox("charm_fma"):
		Terminal.SetCheckBox("charm_fma",False)
	if not Terminal.GetCheckBox("Summon Kishin"):
		Terminal.SetCheckBox("Summon Kishin",True)
	if not Terminal.GetCheckBox("Grenade Kami"):
		Terminal.SetCheckBox("Grenade Kami",True)
	if not Terminal.GetCheckBox("MonkeySpiritsNDcheck"):
		Terminal.SetSpinBox("MonkeySpiritsNDdelay",100)
		Terminal.SetCheckBox("MonkeySpiritsNDcheck",True)
	if Terminal.GetCheckBox("Skill Injection"):
		Terminal.SetCheckBox("Skill Injection",False)
	if Terminal.GetCheckBox("bot/kanna_kami"):
		Terminal.SetCheckBox("bot/kanna_kami",False)
		Terminal.SetSpinBox("bot/kanna_kami_delay",20000)
	if Terminal.GetCheckBox("Kami Vac"):
		Terminal.SetCheckBox("Kami Vac",False)
	elif level < 100 and GameState.IsInGame():
		if Terminal.GetCheckBox("Kami Loot") or Terminal.GetCheckBox("Auto Loot"):
			Terminal.SetCheckBox("Kami Loot",False)
			Terminal.SetCheckBox("Auto Loot",False)
	if level <= 99 and GameState.IsInGame():
		Terminal.SetSpinBox("FilterMeso",50000)
		if not Terminal.GetCheckBox("Auto Equip"):
			Terminal.SetCheckBox("Auto Equip",True)
	elif level > 100 and level < 121:
		Terminal.SetSpinBox("FilterMeso",50000)
		if Terminal.GetCheckBox('filter_equip'):
			Terminal.SetCheckBox('filter_equip',False)
		if not Terminal.GetCheckBox('Kami Loot'):
			Terminal.SetCheckBox('Kami Loot',True)
		if not Terminal.GetCheckBox('Auto Loot'):
			Terminal.SetCheckBox('Auto Loot',True)
	elif level >= 149:
		Terminal.SetCheckBox("map/maprusher/hypertelerock",False)
		Terminal.SetSpinBox("FilterMeso",1000)
	elif level >= 121 and level < 149:
		Terminal.SetSpinBox("FilterMeso",1000)
		if not Terminal.GetCheckBox("Auto Equip"):
			Terminal.SetCheckBox("Auto Equip",True)
		if not Terminal.GetCheckBox("map/maprusher/hypertelerock"):
			Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
		if Terminal.GetCheckBox('filter_equip'):
			Terminal.SetCheckBox('filter_equip',False)
		if not Terminal.GetCheckBox('Kami Loot'):
			Terminal.SetCheckBox('Kami Loot',True)
		if not Terminal.GetCheckBox('Auto Loot'):
			Terminal.SetCheckBox('Auto Loot',True)
	Key.Set(0x47,1,42111003)
def mapID(id):
    if type(id) is int:
        return Field.GetID() == id
    else:
        return Field.GetID() in id

def rush(mapid):
    if not Terminal.IsRushing():
        print("Rushing to map ID: {0}".format(mapid))
        Terminal.Rush(mapid)
        time.sleep(2)
    else:
        time.sleep(1)

def get_earring():
	Terminal.SetSpinBox("FilterMeso",50000)
	if Terminal.GetCheckBox('filter_equip'):
		Terminal.SetCheckBox('filter_equip',False)
	if Terminal.GetCheckBox('Kami Loot'):
		Terminal.SetCheckBox('Kami Loot',False)
	if not Terminal.GetCheckBox('Auto Loot'):
		Terminal.SetCheckBox('Auto Loot',True)
	if Terminal.IsRushing():
		time.sleep(3)
		Terminal.StopRush()
	else:
		if field_id != 240010700:
			Terminal.Rush(240010700)
		elif field_id == 240010700:
			print("At Sky Nest 1 hunting for earring")
			for item in Field.GetItems():
				if item.id == half_earrings:
					Character.Teleport(item.x,item.y)
					time.sleep(3)
			time.sleep(10)

def check_meso_equip():
	if containMesosObtained(Inventory.GetItem(1,1)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 1,face_slot, -1)
		time.sleep(1.5)
	if containMesosObtained(Inventory.GetItem(1,2)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 2,eye_slot, -1)
		time.sleep(1.5)
	if containMesosObtained(Inventory.GetItem(1,3)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 3,earring_slot, -1)
		time.sleep(1.5)
	if containMesosObtained(Inventory.GetItem(1,4)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 4,necklace_slot, -1)
		time.sleep(1.5)
	if containMesosObtained(Inventory.GetItem(1,5)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 5,ring1_slot, -1)
		time.sleep(1.5)
	if containMesosObtained(Inventory.GetItem(1,6)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 6,ring2_slot, -1)
		time.sleep(1.5)
	if containMesosObtained(Inventory.GetItem(1,7)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 7,ring3_slot, -1)
		time.sleep(1.5)
	if containMesosObtained(Inventory.GetItem(1,8)):
		time.sleep(4)
		Inventory.SendChangeSlotPositionRequest(1, 8,ring4_slot, -1)
		time.sleep(1.5)
	if accountData["cubing_done"]:
		if accountData["earring"] == 1:
			if not containMesosObtained(Inventory.GetItem(1,earring_slot)):
				print("Did not equip meso obtained earring")
				for item in Inventory.GetItems(1):
					if item.id in earring_list and containMesosObtained(Inventory.GetItem(1,item.pos)):
						time.sleep(4)
						Inventory.SendChangeSlotPositionRequest(1, item.pos,earring_slot, -1)
		if accountData["face"] == 1:
			if not containMesosObtained(Inventory.GetItem(1,face_slot)):
				print("Did not equip meso obtained face")
				for item in Inventory.GetItems(1):
					if item.id in face_list and containMesosObtained(Inventory.GetItem(1,item.pos)):
						time.sleep(4)
						Inventory.SendChangeSlotPositionRequest(1, item.pos,face_slot, -1)
		if accountData["eye"] == 1:
			if not containMesosObtained(Inventory.GetItem(1,eye_slot)):
				print("Did not equip meso obtained eye")
				for item in Inventory.GetItems(1):
					if item.id in eye_list and containMesosObtained(Inventory.GetItem(1,item.pos)):
						time.sleep(4)
						Inventory.SendChangeSlotPositionRequest(1, item.pos,eye_slot, -1)
		if accountData["necklace"] == 1:
			if not containMesosObtained(Inventory.GetItem(1,necklace_slot)):
				print("Did not equip meso obtained necklace")
				for item in Inventory.GetItems(1):
					if item.id in necklace_list and containMesosObtained(Inventory.GetItem(1,item.pos)):
						time.sleep(4)
						Inventory.SendChangeSlotPositionRequest(1, item.pos,necklace_slot, -1)
		#TODO: check for ring?
def farmed_enough_accessories():
	count = 0
	for item in Inventory.GetItems(1):
		if item.id in ring_list and item.grade > 0:
			count += 1
	for item in Inventory.GetItems(1):
		if item.id in face_list and item.grade > 0:
			count += 1
			break
	for item in Inventory.GetItems(1):
		if item.id in earring_list and item.grade > 0:
			count += 1
			break
	for item in Inventory.GetItems(1):
		if item.id in eye_list and item.grade > 0:
			count += 1
			break
	for item in Inventory.GetItems(1):
		if item.id in necklace_list and item.grade > 0:
			count += 1
			break
	
	print("Accessory count = ",count)
	if count >= 5:
		return True
	else:
		return False

def buy_expansion():
	if Character.GetMeso() > 7900000:
		Character.TalkToNpc(2080001)
		time.sleep(0.5)
		print("Buying expansion via packet")
		Packet.BlockRecvHeader(BlockBuyHeader)
		time.sleep(0.5)
		BuyKey = Packet.COutPacket(BuyItemHeader)
		BuyKey.EncodeBuffer("00 0008 002517F5 0001 00000000 00788B60")
		Packet.SendPacket(BuyKey)
		time.sleep(0.5)
		CloseShop = Packet.COutPacket(BuyItemHeader)
		CloseShop.EncodeBuffer("[03]")
		Packet.SendPacket(CloseShop)
		time.sleep(0.5)
		Packet.UnBlockRecvHeader(BlockBuyHeader)

def toHex(val, nbits):
   return ((val + (1 << nbits)) % (1 << nbits))

def starItem(pos, currStar, itemMaxStar, userMaxStar, itemid):
   with open('starforceCosts.txt', 'a+') as sfCosts:
       #print('{0} {1}'.format("Position: ".ljust(padding), str(pos)))
       sfCosts.write('{0} {1}\n'.format("Position: ".ljust(padding), str(pos)))
       slotStartingMeso = Character.GetMeso()
       slotStartingStar = currStar
     
       if itemid in whitelist:
           return
       while currStar < userMaxStar and currStar < itemMaxStar and Inventory.GetItem(1, pos).valid:     
           if GameState.IsInGame():
               print("#-----------------------Star-----------------------#")
               print('{0} {1}'.format("Starring From: ".ljust(padding), str(currStar)))
               print('{0} {1}'.format("User Max stars: ".ljust(padding), str(userMaxStar)))
               print('{0} {1}'.format("Item max stars: ".ljust(padding), str(itemMaxStar)))
               print('{0} {1}'.format("Item ID: ".ljust(padding), str(itemid)))
             
               sfCosts.write("\t#-----------------------Star-----------------------#\n")
               sfCosts.write('\t{0} {1}\n'.format("Starring From: ".ljust(padding), str(currStar)))
               sfCosts.write('\t{0} {1}\n'.format("User Max stars: ".ljust(padding), str(userMaxStar)))
               sfCosts.write('\t{0} {1}\n'.format("Item max stars: ".ljust(padding), str(itemMaxStar)))
               sfCosts.write('\t{0} {1}\n'.format("Item ID: ".ljust(padding), str(itemid)))
             
               beforeMeso = Character.GetMeso()
             
               # star the item
               oPacket = Packet.COutPacket(SF_header)
               oPacket.Encode1(0x01)
               oPacket.EncodeBuffer("** ** ** **")
               oPacket.Encode2(toHex(pos, 16))
               oPacket.Encode1(0x00)
               oPacket.Encode4(0x00000001)
               oPacket.Encode4(0xFFFFFFFF)
               if safeguard and currStar in range(12, 17):
                   oPacket.Encode2(0x0101)
                   print("SAFEGUARDING")
                   sfCosts.write('\tSAFEGUARDING\n')
               else:
                   oPacket.Encode2(0x0100)
               Packet.SendPacket(oPacket)
           
               # wait for recv
               iPacket = Packet.WaitForRecv(StarForceRecv, 10000)
           
               if iPacket.GetRemaining() < 140:
                   print("Recv length too short (was: " + str(iPacket.GetRemaining()) + ")")
                   sfCosts.write("\tRecv length too short (was: " + str(iPacket.GetRemaining()) + ")\n")
                   break
                 
               afterMeso = Character.GetMeso()
               iCosted = beforeMeso - afterMeso
               print('{0} {1:,}'.format("Meso Cost of Star: ".ljust(padding), iCosted))
               print('{0} {1}'.format("iPacket remaining: ".ljust(padding), iPacket.GetRemaining()))
             
               sfCosts.write('\t{0} {1:,}\n'.format("Meso Cost of Star: ".ljust(padding), iCosted))
               sfCosts.write('\t{0} {1}\n'.format("iPacket remaining: ".ljust(padding), iPacket.GetRemaining()))

               # remove this line if you want faster stars
               # note: this is used as a delay (for safety, etc), so remove at your own risk
               Packet.WaitForRecv(StarForceRecv, 1000)
             
             
               # update current star counter
               currStar = Inventory.GetItem(1, pos).currentStar

               # get max star again in case item blew up
               # item blown up means itemMaxStar = 0
               itemMaxStar = Inventory.GetItem(1, pos).maxStar
             
       slotEndingMeso = Character.GetMeso()
       slotEndingStar = currStar
       slotTotalCost = slotStartingMeso - slotEndingMeso
       if (slotStartingMeso - slotEndingMeso) != 0:
           print('{0} {1:,} meso from star {2} to {3}\n'.format("Total Cost: ".ljust(padding), slotTotalCost, str(slotStartingStar), str(slotEndingStar)))
           sfCosts.write('{0} {1:,} meso from star {2} to {3}\n\n'.format("Total Cost: ".ljust(padding), slotTotalCost, str(slotStartingStar), str(slotEndingStar)))
       
################# MONSTER PARK
################# MONSTER PARK
################# MONSTER PARK
#57.19% -> 91.23%
def dungeonSelector():
    #charLvl = Character.GetLevel()
	'''
    if charLvl in range(115,125):
        return (leopard_portal,mossy_tree_forest)
    elif charLvl in range(125,135):
        return (leopard_portal,secret_pirate)
    elif charLvl in range(135,145):
        return (leopard_portal,other_world)
    elif charLvl in range(145,155):
        return (leopard_portal,forbidden_time)
    elif charLvl in range(155,160):
        return (leopard_portal,clandestine_ruins)
	'''
	return (leopard_portal,mossy_tree_forest)
def rushToMP():
	#fieldid = Field.GetID()
	rushToMPFlag = True
	while rushToMPFlag:
		if level_checker():
			break
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
		if level_checker():
			break
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
    return Field.GetID() >= 952000000 and Field.GetID() <= 954070599

def collide_cash_items():
	oPacket = Packet.COutPacket(collide_header)
	oPacket.EncodeBuffer("** ** ** ** 05")
	Packet.SendPacket(oPacket)

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
		rPacket = Packet.WaitForRecv(recv,100000000)
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
def level_checker():
	sixty_percent = level_149_exp * 0.7
	return (Character.GetExp() / level_149_exp) > sixty_percent
#################### ZAKUM
#################### ZAKUM
#################### ZAKUM
def ResetNowLockedFunction():
	if NowLockedVar:
		print("Resetting NowLockedVar back to False")
		SCLib.UpdateVar("NowLockedVar", False)
def NowLockedFunction():
	if not NowLockedVar:
		print("Boss Attempt started, Now locked for this boss")
		SCLib.UpdateVar("NowLockedVar", True)
def DidSpawn():
	if not HasSpawned:
		print("Updating HasSpawned to True")
		SCLib.UpdateVar("HasSpawned", True)
def ResetSpawn():
	if HasSpawned:
		print("Resetting HasSpawned back to False")
		SCLib.UpdateVar("HasSpawned", False)
def GetToTheDoorToZakum():
	print("Going to Zakum")
	if field_id != CheifsResidence:
		Terminal.Rush(CheifsResidence)
	else:
		TalkNPC = NpcRobeiraMagicianInstructor
		zakjob = [6995, 6996, 6997, 6998, 6999]
		for i in zakjob:
			ZakumCheck = Quest.GetQuestState(i)
			if ZakumCheck == 2:
				ZakumQuest = True
				break
			else:
				ZakumQuest = False
		if ZakumQuest:
			Npc.ClearSelection()
			Npc.RegisterSelection("I want to challenge Zakum.")
			time.sleep(1)
			Character.TalkToNpc(TalkNPC)
			time.sleep(1)
		else:
			Npc.ClearSelection()
			Npc.RegisterSelection("I want to try the Zakum quest.")
			time.sleep(1)
			Character.TalkToNpc(TalkNPC)
			time.sleep(1)

###############IA
###############IA
###############IA
###############IA
###############IA

def startupCheck():
    if os.path.exists('charIA.json'):
        with open('charIA.json') as f:
            return json.load(f)
    else:
        with open('charIA.json', "w+") as db_file:
            db_file.write(json.dumps({}))
            return {}


def writeJson(data):
    with open('charIA.json', 'w') as outfile:
        parsed = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(parsed)
        outfile.close()

def handleCharacter(data, characterId):
    if str(characterId) not in data:
        data[str(characterId)] = False

def finished(data, characterId):
    return data[str(characterId)]

def markFinished(data, characterId):
    data[str(characterId)] = True

charData = startupCheck()
charID = Character.GetID()
handleCharacter(charData, charID)

StatChooser = {
    "STR" : "strFX",
    "DEX" : "dexFX",
    "INT" : "intFX",
    "LUK" : "lukFX",
    "Jump" : "psdJump",
    "Movement Speed" : "psdSpeed",
    "DEF" : "pddX",
    "Max HP" : "mhpX",
    "Max MP" : "mmpX",
    "Attack" : "padX",
    "Magic Attack" : "madX",
    "Critical Rate" : "cr" ,
    "Attack Speed" : "actionSpeed",
    "STR2DEX%" : "str2dex",
    "DEX2STR%" : "dex2str",
    "INT2LUK%" : "int2luk",
    "LUK2DEX%" : "luk2dex",
    "MATT PER LEVEL" : "lv2mad",
    "MAXHP%" : "mhpR",
    "MAXMP%" : "mmpR",
    "Mesos Obtained" : "mesoR",
    "Avoidability" : "er",
    "Boss Damage" : "bdR",
    "Damage To Mobs" : "nbdR",
    "Damage To Towers" : "tdR",
    "Damage Inflicted with" : "abnormalDamR",
    "Attack per level" : "lv2pad",
    "Passive Level" : "passivePlus",
    "Multi Target" : "targetPlus",
    "Buff Duration %" : "bufftimeR",
    "Drop Rate" : "dropR",
}
Inv_Stats = {v: k for k, v in StatChooser.items()}

AbilityName = {
    70000000 : "STR +#strFX",
    70000001 : "DEX +#dexFX",
    70000002 : "INT +#intFX",
    70000003 : "LUK +#lukFX",
    70000004 : "Jump: +#psdJump",
    70000005 : "Movement Speed: +#psdSpeed",
    70000006 : "DEF: +#pddX",
    70000007 : "DEF: +#pddX",
    70000008 : "Max HP +#mhpX",
    70000009 : "Max MP +#mmpX",
    70000010 : "Jump +#psdJump",
    70000011 : "Movement Speed +#psdSpeed",
    70000012 : "Attack +#padX",
    70000013 : "Magic Attack +#madX",
    70000014 : "Critical Rate +#cr%",
    70000015 : "All Stats: +#strFX",
    70000016 : "Attack Speed +1 Level",
    70000017 : "STR: +#strFX",
    70000018 : "DEX: +#dexFX",
    70000019 : "INT: +#intFX",
    70000020 : "LUK: +#lukFX",
    70000021 : "#str2dex% of AP assigned to STR added to DEX",
    70000022 : "#dex2str% of AP assigned to DEX added to STR",
    70000023 : "#int2luk% of AP assigned to INT added to LUK",
    70000024 : "#luk2dex% of AP assigned to LUK added to DEX",
    70000025 : "Attack +1 for every #lv2pad levels",
    70000026 : "Magic Attack +1 for every #lv2mad levels",
    70000027 : "Max HP: +#mhpR%",
    70000028 : "Max MP: +#mmpR%",
    70000029 : "DEF: +#pddR%",
    70000030 : "DEF: +#pddR%",
    70000031 : "Max HP: +#mhpR%",
    70000032 : "Max MP +#mmpR%",
    70000033 : "Mesos Obtained: +#mesoR%",
    70000034 : "Avoidability +#er%",
    70000035 : "Boss Damage +#bdR%",
    70000036 : "+#nbdR% damage to normal monsters",
    70000037 : "+#tdR% damage to towers",
    70000038 : "#minionDeathProp% chance to instant-kill when attacking normal monsters in Aswan Liberation Supply Mode",
    70000039 : "+#abnormalDamR% damage when attacking targets inflicted with Stun, Blind, Freeze, or Incapacitation status.",
    70000040 : "Attack +1 every #lv2pad levels",
    70000041 : "Final Damage: +#pdd2dam% of DEF",
    70000042 : "Magic Attack +1 every #lv2mad levels",
    70000043 : "Critical Rate: +#cr%",
    70000044 : "All Stats: +#strFX",
    70000045 : "#nocoolProp% chance to skip cooldowns",
    70000046 : "Passive Skills: +#passivePlus Level (excludes Active Hybrids, 5th Job Skills)",
    70000047 : "Number of enemies hit by multi-target skill +#targetPlus",
    70000048 : "Buff skill duration +#bufftimeR%",
    70000049 : "Item Drop Rate +#dropR%",
    70000050 : "Mesos Obtained: +#mesoR%",
    70000051 : "STR +#strFX, DEX +#dexFX",
    70000052 : "STR +#strFX, INT +#intFX",
    70000053 : "STR +#strFX, LUK +#lukFX",
    70000054 : "DEX +#dexFX, INT +#intFX",
    70000055 : "DEX +#dexFX, LUK +#lukFX",
    70000056 : "INT +#intFX, LUK +#lukFX",
    70000057 : "DEX +#dexFX, STR +#strFX",
    70000058 : "INT +#intFX, STR +#strFX",
    70000059 : "LUK +#lukFX, STR +#strFX",
    70000060 : "INT +#intFX, DEX +#dexFX",
    70000061 : "LUK +#lukFX, DEX +#dexFX",
    70000062 : "LUK +#lukFX, INT +#intFX",
}

itemList = {
    70000000 : [AbilityName[70000000],[["strFX","x"],]],
    70000001 : [AbilityName[70000001],[["dexFX","x"],]],
    70000002 : [AbilityName[70000002],[["intFX","x"],]],
    70000003 : [AbilityName[70000003],[["lukFX","x"],]],
    70000004 : [AbilityName[70000004],[["psdJump","2*u(x/3)"],]],
    70000005 : [AbilityName[70000005],[["psdSpeed","2*u(x/3)"],]],
    70000006 : [AbilityName[70000006],[["pddX","10*x"],]],
    70000007 : [AbilityName[70000007],[["pddX","10*x"],]],
    70000008 : [AbilityName[70000008],[["mhpX","x*15"],]],
    70000009 : [AbilityName[70000009],[["mmpX","x*15"],]],
    70000010 : [AbilityName[70000010],[["psdJump","2*u(x/3)"],]],
    70000011 : [AbilityName[70000011],[["psdSpeed","2*u(x/3)"],]],
    70000012 : [AbilityName[70000012],[["padX","3*u(x/3)"],]],
    70000013 : [AbilityName[70000013],[["madX","3*u(x/3)"],]],
    70000014 : [AbilityName[70000014],[["cr","x"],]],
    70000015 : [AbilityName[70000015],[["lukFX","x"],["strFX","x"],["dexFX","x"],["intFX","x"],]],
    70000016 : [AbilityName[70000016],[["actionSpeed","-1"],]],
    70000017 : [AbilityName[70000017],[["strFX","x"],]],
    70000018 : [AbilityName[70000018],[["dexFX","x"],]],
    70000019 : [AbilityName[70000019],[["intFX","x"],]],
    70000020 : [AbilityName[70000020],[["lukFX","x"],]],
    70000021 : [AbilityName[70000021],[["str2dex","u(x/4)"],]],
    70000022 : [AbilityName[70000022],[["dex2str","u(x/4)"],]],
    70000023 : [AbilityName[70000023],[["int2luk","u(x/4)"],]],
    70000024 : [AbilityName[70000024],[["luk2dex","u(x/4)"],]],
    70000025 : [AbilityName[70000025],[["lv2pad","20-2*d(x/2)"],]],
    70000026 : [AbilityName[70000026],[["lv2mad","20-2*d(x/2)"],]],
    70000027 : [AbilityName[70000027],[["mhpR","x"],]],
    70000028 : [AbilityName[70000028],[["mmpR","x"],]],
    70000029 : [AbilityName[70000029],[["pddR","x"],]],
    70000030 : [AbilityName[70000030],[["pddR","x"],]],
    70000031 : [AbilityName[70000031],[["mhpR","x"],]],
    70000032 : [AbilityName[70000032],[["mmpR","x"],]],
    70000033 : [AbilityName[70000033],[["mesoR","u(x/2)"],["acc","u(x/2)"],]],
    70000034 : [AbilityName[70000034],[["er","u(x/2)"],["eva","u(x/2)"],]],
    70000035 : [AbilityName[70000035],[["bdR","x"],]],
    70000036 : [AbilityName[70000036],[["nbdR","u(x/4)"],]],
    70000037 : [AbilityName[70000037],[["tdR","2*u(x/3)"],]],
    70000038 : [AbilityName[70000038],[["minionDeathProp","u(x/4)"],]],
    70000039 : [AbilityName[70000039],[["abnormalDamR","u(x/4)"],]],
    70000040 : [AbilityName[70000040],[["lv2pad","20-2*d(x/2)"],]],
    70000041 : [AbilityName[70000041],[["pdd2dam","x*2+u(x/2)"],]],
    70000042 : [AbilityName[70000042],[["lv2mad","20-2*d(x/2)"],]],
    70000043 : [AbilityName[70000043],[["cr","x"],]],
    70000044 : [AbilityName[70000044],[["lukFX","x"],["strFX","x"],["dexFX","x"],["intFX","x"],]],
    70000045 : [AbilityName[70000045],[["nocoolProp","x"],]],
    70000046 : [AbilityName[70000046],[["passivePlus","1"],]],
    70000047 : [AbilityName[70000047],[["targetPlus","1"],]],
    70000048 : [AbilityName[70000048],[["bufftimeR","x+u(x/4)"],]],
    70000049 : [AbilityName[70000049],[["dropR","u(x/2)"],]],
    70000050 : [AbilityName[70000050],[["mesoR","u(x/2)"],]],
    70000051 : [AbilityName[70000051],[["strFX","x"],["dexFX","u(x/2)"],]],
    70000052 : [AbilityName[70000052],[["strFX","x"],["intFX","u(x/2)"],]],
    70000053 : [AbilityName[70000053],[["strFX","x"],["lukFX","u(x/2)"],]],
    70000054 : [AbilityName[70000054],[["dexFX","x"],["intFX","u(x/2)"],]],
    70000055 : [AbilityName[70000055],[["dexFX","x"],["lukFX","u(x/2)"],]],
    70000056 : [AbilityName[70000056],[["intFX","x"],["lukFX","u(x/2)"],]],
    70000057 : [AbilityName[70000057],[["dexFX","x"],["strFX","u(x/2)"],]],
    70000058 : [AbilityName[70000058],[["intFX","x"],["strFX","u(x/2)"],]],
    70000059 : [AbilityName[70000059],[["lukFX","x"],["strFX","u(x/2)"],]],
    70000060 : [AbilityName[70000060],[["intFX","x"],["dexFX","u(x/2)"],]],
    70000061 : [AbilityName[70000061],[["lukFX","x"],["dexFX","u(x/2)"],]],
    70000062 : [AbilityName[70000062],[["lukFX","x"],["intFX","u(x/2)"],]],
}

def calc(str, value):
    x = value
    return eval(str)

def u(value):
    return math.ceil(value)

def d(value):
    #Unsure, have yet gotten such line.
    return math.floor(value)

def GetLineValue(lineNumber, value, skillID):
    stats = {}
    if skillID in itemList:
        AccessSkillinfo = itemList[skillID]
        LineRep =  AccessSkillinfo[0]
        Arguments = AccessSkillinfo[1]
        for x in range(0, len(Arguments)):
            stat = Arguments[x][0]
            function = Arguments[x][1]
            #Handle attack speed
            if function == "-1":
                stats[stat] = -1
            else:
                LineRep = LineRep.replace("#" + stat,  str(calc(function, value)))
                stats[stat] = int(str(calc(function, value)))
        print("Line #" + lineNumber + "." + LineRep)
        return stats
    return None

def RerollIA():
    reroll = Packet.COutPacket(RerollHeader)
    reroll.Encode4(0)
    reroll.Encode4(0)
    Packet.SendPacket(reroll)


########Potentials
########Potentials
########Potentials
########Potentials
########Potentials
def startupCheck_cube(accountId):
    split_id = accountId.split("@")[0]
    if os.path.exists('info/{}.json'.format(split_id)):
        #print("Loading")
        with open('info/{}.json'.format(split_id)) as f:
            return json.load(f)
    else:
        print("Creating")
        with open('info/{}.json'.format(split_id), "w+") as db_file:
            db_file.write(json.dumps({}))
            return {}

def handleReady(data):
	if 'ready_for_cube' not in data:
		data['ready_for_cube'] = False
	if 'face_done' not in data:
		data['face_done'] = False
	if 'eye_done' not in data:
		data['eye_done'] = False
	if 'earring_done' not in data:
		data['earring_done'] = False
	if 'ring_done' not in data:
		data['ring_done'] = False
	if 'necklace_done' not in data:
		data['necklace_done'] = False
	if 'cubing_done' not in data:
		data['cubing_done'] = False
	if 'storage_number' not in data:
		data['storage_number'] = 0
	if 'storing_meso' not in data:
		data['storing_meso'] = False
	if 'kanna_pos' not in data:
		if jobid == 4212:
			data['kanna_pos'] = Terminal.GetLineEdit("LoginChar")
	if 'IGN' not in data or data['IGN'] == '':
		data['IGN'] = Character.GetName()
	if 'total_meso' not in data:
		if jobid == 4212:
			data['total_meso'] = int(data['storage_number']) * 30 + Character.GetMeso() / 1000000000
	if 'pet_expire' not in data:
		data['pet_expire'] = False

def initializeEquips(data):
	if 'equips' not in data:
		data['equips'] = []
	if 'cubing_done' not in data:
		data['cubing_done'] = False

def writeJson_cube(data,accountId):
    split_id = accountId.split("@")[0]
    with open('info/{}.json'.format(split_id), 'w') as outfile:
        parsed = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(parsed)
        outfile.close()

accountId = Terminal.GetLineEdit("LoginID")
accountData = startupCheck_cube(accountId)
initializeEquips(accountData)
handleReady(accountData)
writeJson_cube(accountData,accountId)
def collide_items():
	oPacket = Packet.COutPacket(collide_header)
	oPacket.EncodeBuffer("** ** ** ** 01")
	Packet.SendPacket(oPacket)

def reveal_potential(itemPos):
	if Character.GetMeso() > 500000:
		oPacket = Packet.COutPacket(potential_header)
		oPacket.EncodeBuffer("** ** ** 00 7F 00")
		oPacket.Encode2(itemPos)
		Packet.SendPacket(oPacket)
		rPacket = Packet.WaitForRecv(potential_recv,5000)
		print(rPacket)

#oPacket.EncodeBuffer("** ** ** 00 7F 00 01 00") potential reveal
#rPacket = Packet.WaitForRecv(0x0254,5000)
def take_off_equip():
	equip_slot = 1
	
	max_slots = Inventory.GetItemSlotCount(equip_slot)
	for slots in accessory_slot_list:
		remain_slots = Inventory.GetEmptySlotCount(equip_slot)
		item = Inventory.GetItem(1,slots)
		if remain_slots > 0:
			if item.valid:
				Inventory.SendChangeSlotPositionRequest(1, slots,max_slots, -1)
				time.sleep(1.5)
				collide_items()
				time.sleep(2.5)

def reveal_all_potential():
	print("revealing potentials")
	item_list = Inventory.GetItems(1)
	for item in item_list:
		if item.grade > 0 and item.option1 == 0 and GameState.IsInGame():
			#if item.sn not in accountData['equips']:
			#	accountData['equips'].append(item.sn)
			reveal_potential(item.pos)
			time.sleep(0.5)

def cube_item_ready():
	item1 = Inventory.GetItem(1,1)
	item2 = Inventory.GetItem(1,2)
	item3 = Inventory.GetItem(1,3)
	item4 = Inventory.GetItem(1,4)
	item5 = Inventory.GetItem(1,5)
	return item1 in accessory_list and item2 in accessory_list and item3 in accessory_list and item4 in accessory_list and item5 in accessory_list

def find_move_face():
	print("finding face")
	items = Inventory.GetItems(1)
	for i in reversed(range(1,5)):
		for item in items:
			if item.id in face_list:
				if item.grade == i:
					if item.pos != 1:
						print("found, moving")
						Inventory.SendChangeSlotPositionRequest(1,item.pos,1,-1)
						time.sleep(1.5)
					return

def find_move_eye():
	print("finding eye")
	items = Inventory.GetItems(1)
	for i in reversed(range(1,5)):
		for item in items:
			if item.id in eye_list:
				if item.grade == i:
					if item.pos != 2:
						print("found, moving")
						Inventory.SendChangeSlotPositionRequest(1,item.pos,2,-1)
						time.sleep(1.5)
					return

def find_move_earring():
	print("finding earring")
	items = Inventory.GetItems(1)
	for i in reversed(range(1,5)):
		for item in items:
			if item.id in earring_list:
				if item.grade == i:
					if item.pos != 3:
						print("found, moving")
						Inventory.SendChangeSlotPositionRequest(1,item.pos,3,-1)
						time.sleep(1.5)
					return

def find_move_necklace():
	print("finding necklace")
	items = Inventory.GetItems(1)
	for i in reversed(range(1,5)):
		for item in items:
			if item.id in necklace_list:
				if item.grade == i:
					if item.pos != 4:
						print("found, moving")
						Inventory.SendChangeSlotPositionRequest(1,item.pos,4,-1)
						time.sleep(1.5)
					return

def find_move_ring():
	print("finding rings")
	items = Inventory.GetItems(1)
	start_pos = 5
	for i in reversed(range(1,5)):
		for item in items:
			if start_pos == 9:
				print("max 4 rings")
				break
			if item.id in ring_list:
				if item.grade == i:
					to_item = Inventory.GetItem(1,start_pos)
					if item.id != to_item.id or to_item.grade==0 or (item.id == to_item.id and item.grade>to_item.grade):
						print("found ring, moving")
						Inventory.SendChangeSlotPositionRequest(1,item.pos,start_pos,-1)
						time.sleep(1.5)
						start_pos += 1
					elif item.pos == to_item.pos:
						print("moving to itself, pos+1")
						start_pos += 1

def buy_cubes():
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
		if GameState.IsInCashShop():
			break
	while buy_count < buy_cube_number:
		time.sleep(2)
		start_slot += 1
		print("Buying cube pack number {}".format(buy_count+1))
		buy_cube_packet = Packet.COutPacket(buy_ticket_header)
		buy_cube_packet.EncodeBuffer("55 052F841E 044AA200")
		Packet.SendPacket(buy_cube_packet)
		rPacket = Packet.WaitForRecv(recv,100000000)
		rPacket.Skip(1)
		x = rPacket.ReadLong(4)
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
		print("out is {}".format(out))
		buy_count += 1

	time.sleep(1)
	print("Leaving cash shop")
	Terminal.LeaveCashShop()

###### lvl 30 pet ######
def get_pet():
	if Quest.GetQuestState(61587) !=2 and Character.GetLevel()>= 30:
		Terminal.SetCheckBox("bot/puffram", True)
		time.sleep(10)
		Terminal.SetCheckBox("bot/puffram", False)
#########cubing

def handleToken(data, token,value):
    #print("{}: {}".format(token,value))
    if token not in data:
        data[token] = value

def finished_cube(data, accountId):
    return data[accountId]

def mark_ready_for_cube(data):
	data['ready_for_cube'] = True

def asOne_cube(data, equip):
    data[equip] = 1

def addOne_cube(data, equip):
    data[equip] += 1

def containMesosObtained(item):
    return item.option1 == 40650 or item.option2 == 40650 or item.option3 == 40650

###########store mesos
def store_mesos():
	while True:
		if Field.GetID() == storage_map_id:
			print("Current Mesos before store = {}".format(Character.GetMeso()))
			Packet.BlockRecvHeader(block_header)
			Character.Teleport(2268,17)
			time.sleep(1)
			Character.TalkToNpc(storage_npc_id)
			time.sleep(1)
			oPacket = Packet.COutPacket(store_header)
			oPacket.EncodeBuffer("07 FFFFFFF903DC5401")
			Packet.SendPacket(oPacket)
			oPacket1 = Packet.COutPacket(store_header)
			oPacket1.Encode2(8)
			Packet.SendPacket(oPacket1)
			print("Completed meso storing")
			time.sleep(1)
			print("Current Mesos after store = {}".format(Character.GetMeso()))
			Packet.UnBlockRecvHeader(block_header)
			break
		else:
			Terminal.Rush(storage_map_id)
			print("Still rushing to storage")
			time.sleep(2)

def withdraw_mesos():
	if Field.GetID() ==101000000: #wait till character gets to ellinia
		#1032006
		time.sleep(2)
		Packet.BlockRecvHeader(block_header)
		print("Current Mesos before withdraw = {}".format(Character.GetMeso()))
		Character.TalkToNpc(1032006)
		time.sleep(3)
		oPacket = Packet.COutPacket(store_header)
		oPacket.EncodeBuffer("07 00000006FC23ABFF")
		Packet.SendPacket(oPacket)
		oPacket1 = Packet.COutPacket(store_header)
		oPacket1.Encode2(8)
		#oPacket2.EncodeBuffer("08")
		Packet.SendPacket(oPacket1)
		time.sleep(1)
		print("Current Mesos after withdraw = {}".format(Character.GetMeso()))
		time.sleep(1)
		Packet.UnBlockRecvHeader(block_header)
		#Terminal.LoadProfile(r"C:\Users\Jacopo\Desktop\TerminalManager\terminalProfiles\kannaMesoFarmLVL170.xml")
	else:
		Terminal.Rush(101000000)
		time.sleep(3)

######Black gate
def BossCheck():
	print("Waiting for boss to spawn...")
	time.sleep(10)
	for mob in blackgate_boss:
		print("Checking for boss: " + str(mob) + "...")
		while Field.FindMob(mob).valid and GameState.IsInGame():
			print("Boss found: " + str(mob) + ", killing boss...")
			time.sleep(6)
	for item in blackgate_eqp:
		print("Checking for item: " + str(item) + "...")
		while Field.FindItem(item).valid and GameState.IsInGame():
			Terminal.SetCheckBox("Kami Vac",False)
			print("item found with id:" + str(item) + ", waiting until item looted")
			time.sleep(9)
	for mob in blackgate_boss:
		print("Checking for boss: " + str(mob) + "...")
		while Field.FindMob(mob).valid and GameState.IsInGame():
			print("Boss found: " + str(mob) + ", killing boss...")
			time.sleep(6)
	for item in blackgate_eqp:
		print("Checking for item: " + str(item) + "...")
		while Field.FindItem(item).valid and GameState.IsInGame():
			Terminal.SetCheckBox("Kami Vac",False)
			print("item found with id:" + str(item) + ", waiting until item looted")
			time.sleep(9)
	for mob in blackgate_boss:	
		print("Checking for boss: " + str(mob) + "...")
		while Field.FindMob(mob).valid and GameState.IsInGame():
			print("Boss found: " + str(mob) + ", killing boss...")
			time.sleep(6)
	for item in blackgate_eqp:
		print("Checking for item: " + str(item) + "...")
		while Field.FindItem(item).valid and GameState.IsInGame():
			Terminal.SetCheckBox("Kami Vac",False)
			print("item found with id:" + str(item) + ", waiting until item looted")
			time.sleep(9)
	print("no boss found or boss killed")
	time.sleep(2)


def EnterPortal(name):
    time.sleep(0.5)
    portal = Field.FindPortal(name)
    pos = Character.GetPos()
    if pos.x != portal.x:
        print("Portal " + str(name) + " found, teleporting...")
        Character.Teleport(portal.x, portal.y-20)
        time.sleep(0.5)
        print("Teleported to portal: " + str(name)+"...")
    print("Trying to enter portal...")
    while GameState.IsInGame() and Character.GetPos().x == portal.x:
        if Field.GetID() == 610050000:
            break
        Character.EnterPortal()
        time.sleep(0.5)

def CPU_hack(flag):
	Terminal.SetCheckBox("No Fade Stages",flag)
	Terminal.SetCheckBox("No Tile",flag)
	Terminal.SetCheckBox("No Map Object",flag)
	Terminal.SetCheckBox("No Letter Box",flag)
	Terminal.SetCheckBox("No Background",flag)
	Terminal.SetCheckBox("No Weather",flag)

if jobid == -1 and not accountData['storing_meso']:
	#print("Not logged in yet")
	time.sleep(2)

if Character.GetMeso() == 29999999999 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and jobid == 4212:
	#if mesos =29999999999, which is max, store them in the storage
	toggle_rush_by_level(False)
	#Terminal.LoadProfile(r"C:\Users\Jacopo\Desktop\TerminalManager\terminalProfiles\StoreMesos.xml")
	if accountData['storing_meso'] == False:
		store_mesos()
	#Next step is to change the AutoChar Number and then logon into the new created luminous and release control
	#Read AutoChar Number, +1 write to file.
	time.sleep(3)
	if Character.GetMeso() == 0:
		accountData['storing_meso'] = True
		writeJson_cube(accountData,accountId)
		print("logging out")
		Terminal.Logout()
		time.sleep(1)
#print(GameState.GetLoginStep())
if accountData['storing_meso'] and GameState.GetLoginStep() == 2:
	autochar_kanna = 19
	autochar_lumi = 11
	Terminal.SetCheckBox("Auto Login",False)
	Terminal.SetLineEdit("LoginChar", str(accountData['storage_number'] + 1))
	Terminal.SetComboBox("settings/autochar_job",autochar_lumi)
	Terminal.SetCheckBox("Auto Login",True)
	Terminal.SetCheckBox("settings/autochar",True)

if accountData['storing_meso'] and jobid == 2700 and Character.GetMeso() == 0:
	print("withdrawing mesos")
	toggle_rush_by_level(False)
	withdraw_mesos()
	time.sleep(2)
	SCLib.UpdateVar("withdraw_flag",True)
elif accountData['storing_meso'] and jobid == 2700 and Character.GetMeso() == 29999999999 and SCLib.GetVar("withdraw_flag"):
	#safe to say that storage is empty and can switch back to kanna
	accountData['storage_number'] = accountData['storage_number'] + 1
	accountData['storing_meso'] = False
	writeJson_cube(accountData,accountId)
	Terminal.Logout()
	Terminal.SetLineEdit("LoginChar", accountData['kanna_pos'])
	SCLib.UpdateVar("withdraw_flag",False)
	print("Logging out and changing to Kanna farmer")
	time.sleep(2)
elif accountData['storing_meso'] and jobid == 2700 and Character.GetMeso() != 0 and not SCLib.GetVar("withdraw_flag"):
	#need to update bank number but did not withdraw mesos
	accountData['storage_number'] = accountData['storage_number'] + 1
	writeJson_cube(accountData,accountId)
	Terminal.Logout()
	print("Logging out and changing to next bank")
	time.sleep(2)

#######First Job#######
if jobid == 4200 and level < 13:
	if field_id == 807040000:
		if Terminal.IsRushing():
			print("Stopping terminal rush")
			Terminal.StopRush()
		print("Doing First Job")
		Terminal.SetCheckBox("Kami Vac",False)
		toggle_rush_by_level(False)
		quest_state = Quest.GetQuestState(57400)
		quest_state1 = Quest.GetQuestState(57401)
		quest_state2 = Quest.GetQuestState(57402)
		print("Doing quests")
		if quest_state != 2:
			print("Quest 0")
			if quest_state == 0:
				Quest.StartQuest(57400, 000000)
		elif quest_state1 != 2:
			print("Quest 1")
			if quest_state1 == 0:
				Quest.StartQuest(57401, 9130082)
			elif quest_state1 == 1:
				Quest.CompleteQuest(57401, 9130082)
		elif quest_state2 != 2:
			print("Quest 3")
			if quest_state2 == 0:
				Quest.StartQuest(57402, 000000)
			elif quest_state2 ==1:
				portal = Field.FindPortal("east00")
				if portal.valid:
					print("Found portal at x={} y={}".format(portal.x,portal.y))
					Character.Teleport(portal.x, portal.y-10)
					time.sleep(1)
					Character.EnterPortal()
	elif field_id == 807040100:
		quest = Quest.GetQuestState(57402)
		if quest == 1:
			Quest.CompleteQuest(57402, 9130083)
			print("Returning control to rush by level")
			toggle_rush_by_level(True)
	else:
		time.sleep(1)
		fan = Inventory.FindItemByID(1552000)
		time.sleep(1)
		if fan.valid:
			print("Equipping fan")
			Inventory.SendChangeSlotPositionRequest(1, fan.pos, -11, -1)
			time.sleep(1)
		print("Setting up first job settings")
		Key.Set(0x44, 1, 42001000)
		settings_first_job()
		time.sleep(1)
if jobid == 4200 and (level >= 13 and level < 30):
	if not Terminal.GetCheckBox("Skill Injection") or Terminal.GetComboBox("AttackKey") != 33 or not Terminal.GetCheckBox("Auto Attack"):
		settings_first_job()
		print("Sleeping for 10 seconds to farm")
		time.sleep(10)
	if level < 120:
		Terminal.SetSpinBox("FilterMeso",50000)
	elif level >= 120:
		Terminal.SetSpinBox("FilterMeso",1000)
		
###### second job #########
if jobid == 4200 and level >= 30:
	print("Completing Second job")
	if second_job_quest == 0:
		print("Setting up shikigami fma")
		Quest.StartQuest(57458, 000000)
		settings_second_job()
		print("Sleeping for 10 seconds to farm")
		time.sleep(10)
	if level < 120:
		Terminal.SetSpinBox("FilterMeso",50000)
	elif level >= 120:
		Terminal.SetSpinBox("FilterMeso",1000)

if jobid == 4210 and not SCLib.GetVar("DoingMP"):
	if not Terminal.GetCheckBox("charm_fma"):
		settings_second_job()
		print("Sleeping for 10 seconds to farm")
		time.sleep(10)
	if level < 120:
		Terminal.SetSpinBox("FilterMeso",50000)
	elif level >= 120:
		Terminal.SetSpinBox("FilterMeso",1000)
###### third job #########
if jobid == 4211 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
	print("Now third job")
#	if Character.GetSP() == 0:
#		print("Setting Kishin Key to G")
#		Key.Set(0x47,1,42111003)
#		settings_third_job()
#		print("Sleeping for 10 seconds to farm")
#		time.sleep(10)
	if Terminal.GetComboBox("AttackKey") != 36 or not Terminal.GetCheckBox("Auto Attack") or not Terminal.GetCheckBox("charm_fma") or not Terminal.GetCheckBox("bot/kanna_kami"):
		settings_third_job()
		print("Sleeping for 10 seconds to farm")
		time.sleep(10)
	if level < 120:
		Terminal.SetSpinBox("FilterMeso",50000)
	elif level >= 120:
		Terminal.SetSpinBox("FilterMeso",1000)
###### fourth job ########
if jobid == 4212 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBG") and not SCLib.GetVar("BuyingExpansion") and not accountData['pet_expire']:
	if not Terminal.GetCheckBox("MonkeySpiritsNDcheck") or not Terminal.GetCheckBox("Grenade Kami"):
		print("Now fourth job")
		settings_fourth_job()
		if not Terminal.GetCheckBox("Rush By Level"):
			Terminal.SetCheckBox("Rush By Level",True)
		print("Sleeping for 30 seconds to farm")
		time.sleep(30)
	if level > 120 and level < 145 and not SCLib.GetVar("cube_lock"):
		print("level > 120 but < 149")
		settings_fourth_job()
		if not Terminal.GetCheckBox("Rush By Level"):
			Terminal.SetCheckBox("Rush By Level",True)
		print("Sleeping for 30 seconds to farm")
		time.sleep(30)
	elif not SCLib.GetVar("cube_lock") and accountData['ready_for_cube'] and not accountData['cubing_done']:
		print("ready for cube and now farming")
		settings_fourth_job()
		toggle_rush_by_level(True)
		get_pet() #here
		Terminal.SetCheckBox('filter_equip',True)
		Terminal.SetCheckBox("Auto Equip",False)
		Terminal.SetCheckBox("Kami Loot",False)
		Terminal.SetCheckBox("Auto Loot",False)
		Terminal.SetSpinBox("AutoDieExp",90)
		Terminal.SetSpinBox("AutoDieLevel",level)
		Terminal.SetComboBox("Familiar0",7)
		print("Sleeping for 30 seconds to farm")
		time.sleep(30)
	elif not SCLib.GetVar("cube_lock") and accountData['ready_for_cube'] and accountData['cubing_done']:
		print("cubing done and now farming with pet")
		settings_fourth_job()
		toggle_rush_by_level(True)
		Terminal.SetCheckBox('filter_equip',True)
		Terminal.SetCheckBox("Auto Equip",False)
		get_pet()
		Terminal.SetCheckBox("Kami Loot",False)
		Terminal.SetCheckBox("Auto Loot",False)
		Terminal.SetSpinBox("AutoDieExp",90)
		Terminal.SetSpinBox("AutoDieLevel",level)
		Terminal.SetComboBox("Familiar0",7)
		Terminal.SetCheckBox("settings/mesologout",True)
		if not SCLib.GetVar("EquipMesoDone"):
			Terminal.SetCheckBox('MonkeySpiritsNDcheck',False)
			Terminal.SetCheckBox("charm_fma",False)
			time.sleep(10)
			check_meso_equip()
			SCLib.UpdateVar("EquipMesoDone",True)
			Terminal.SetCheckBox('MonkeySpiritsNDcheck',True)
		if int(SCLib.GetVar("farm_counter")) >= 3:
			new_meso = int(accountData['storage_number']) * 30 + Character.GetMeso() / 1000000000
			print("Updating total mesos from {} to {}b".format(accountData['total_meso'],new_meso))
			if accountData['total_meso'] == new_meso:
				accountData['pet_expire'] = True
				print("Detected that pet has expired")
				Terminal.SendLog("This account's pet has expired")
				Terminal.ChangeStatus("#################Farming Done##############")
			accountData['total_meso'] = new_meso
			writeJson_cube(accountData,accountId)
			SCLib.UpdateVar("farm_counter",0)
		if not Terminal.IsAutoDying():
			SCLib.UpdateVar("farm_counter",int(SCLib.GetVar("farm_counter"))+1)
		print("Sleeping for 90 seconds to farm")
		time.sleep(90)
	elif not SCLib.GetVar("cube_lock") and not accountData['ready_for_cube'] and level >= 149:
		print("not ready for cube and farming equip")
		settings_fourth_job()
		toggle_rush_by_level(False)
		Terminal.SetCheckBox('filter_equip',False)
	if level >= 145 and not accountData["ready_for_cube"]:
		print("Not done cubing yet")
		if not Terminal.GetCheckBox("Kami Loot") or not Terminal.GetCheckBox("Auto Loot"):
			Terminal.SetCheckBox("Kami Loot",True)
			Terminal.SetCheckBox("Auto Loot",True)
			Terminal.SetSpinBox("AutoDieExp",70)
			Terminal.SetComboBox("Familiar0",2)


if accountData['pet_expire']:
	general_store = 240000002
	
	toggle_rush_by_level(False)
	if Terminal.IsRushing():
		time.sleep(5)
	elif field_id != general_store:
		Terminal.Rush(general_store)
		print("Done farming and rushing to general_store")
	else:
		#print("In general_store, waiting for user input")
		Terminal.ChangeStatus("#################Farming Done##############")

		new_meso = int(accountData['storage_number']) * 30 + Character.GetMeso() / 1000000000
		if accountData['total_meso'] != new_meso:
			print("Updating total mesos from {} to {}b".format(accountData['total_meso'],new_meso))
			accountData['total_meso'] = new_meso
			writeJson_cube(accountData,accountId)
		if Terminal.GetCheckBox("No Fade Stages"):
			CPU_hack(False)
			Terminal.ChangeChannel(0)
		Terminal.SetCheckBox("settings/mesologout",False)
		time.sleep(60)

###### lvl 50 hyper rock #######
if Quest.GetQuestState(61589) !=2 and Character.GetLevel() >= 50:
	print("Getting hyper rock")
	Npc.ClearSelection()
	Npc.RegisterSelection("Familiar")
	Npc.RegisterSelection("Teleport Rock")
	Npc.RegisterSelection("You get")
	Quest.StartQuest(61589, 9201253)
	time.sleep(10)
elif Quest.GetQuestState(61589) ==2:
	if Inventory.FindItemByID(2430450).valid:
		print("Using equip box lvl50")
		Inventory.UseItem(2430450)

###### lvl 60 tot ########
if Quest.GetQuestState(61590) !=2 and Character.GetLevel() >= 60:
	print("Getting tot badge")
	Npc.ClearSelection()
	Npc.RegisterSelection("Potential")
	Npc.RegisterSelection("Bonus Potential")
	Npc.RegisterSelection("Cube")
	Npc.RegisterSelection("Soul Weapon")
	Npc.RegisterSelection("gift")
	Quest.StartQuest(61590, 9201253)
	time.sleep(10)
elif Quest.GetQuestState(61590) ==2:
	if Inventory.FindItemByID(2430451).valid:
		print("Using equip box lvl60")
		Inventory.UseItem(2430451)

if Quest.GetQuestState(62390) !=2 and Character.GetLevel() >= 100:
	print("Getting Emblem")
	Quest.StartQuest(62390, 9130010)
	time.sleep(5)

if Character.GetLevel() >= 83 and GameState.IsInGame():
	# Big Spider
	if Character.IsOwnFamiliar(9960295) == False:
		print("Getting Big Spider")
		toggle_rush_by_level(False)
		# sleep 1 second every loop
		time.sleep(1)
		item = Inventory.FindItemByID(2870295)
		drop = Field.FindItem(2870295)
		pos = Character.GetPos()
		if drop.valid:
			Terminal.SetCheckBox("Auto Loot",True)
			if pos.x == drop.x and pos.y == drop.y:
				Character.LootItem()
			else:
				Character.Teleport(drop.x,drop.y)
				Character.LootItem()
		if item.valid:
			# use familiar
			print("Found big spider familiar")
			Inventory.UseFamiliarCard(2870295)
			toggle_rush_by_level(True)
			time.sleep(1)
			if not Terminal.GetCheckBox("Familiar 0"):
				Terminal.SetComboBox("Familiar0",2)
				Terminal.SetCheckBox("Familiar 0",True)
				Terminal.SetCheckBox("Auto Loot",False)
		else:
			if Field.GetID() == 310050600:
				# let bot kill mobs and pickup?
				print("Farming for big spider")
				time.sleep(3)
			else:
				# rush to the map
				print("Rushing to Big Spider map")
				if not Terminal.GetCheckBox("map/maprusher/hypertelerock"):
					Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
				Terminal.Rush(310050600)

if Character.IsOwnFamiliar(9960295) and GameState.IsInGame() and level >= 104 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("GettingEarring"):
	item = Inventory.FindItemByID(2871073)
	if not Character.IsOwnFamiliar(9961073):
		SCLib.UpdateVar("GettingLep",True)
		toggle_rush_by_level(False)
		drop = Field.FindItem(2871073)
		pos = Character.GetPos()
		if drop.valid:
			Terminal.SetCheckBox("Auto Loot",True)
			if pos.x == drop.x and pos.y == drop.y:
				Character.LootItem()
			else:
				Character.Teleport(drop.x,drop.y)
				Character.LootItem()
		if item.valid:
			print("Leprechaun Familiar Found!")
			Inventory.UseFamiliarCard(2871073)
			print("Using Familiar Card...")
			time.sleep(1)
			Terminal.SetCheckBox("Auto Loot",False)
		else:
			if mapID(610010001):
				print("Farming for Leprechaun Familiar...")
				time.sleep(3)
			else:
				Terminal.SetCheckBox("map/maprusher/hypertelerock", True)
				time.sleep(1)
				rush(600000000)
				time.sleep(1)
				if mapID(600000000):
					Terminal.SetCheckBox("map/maprusher/hypertelerock", False)
					time.sleep(1)
					rush(610010001)
	else:
		if mapID(600000000):
			SCLib.UpdateVar("GettingLep",False) 
			toggle_rush_by_level(True)
			Terminal.SetCheckBox("map/maprusher/hypertelerock", True)
			print("Returning controls to Rush By Level...")
			time.sleep(5)
		elif mapID(610010001):
			rush(600000000)


###### Inner ability #######
'''
if level > 70 and not SCLib.GetVar("MPDone") and not SCLib.GetVar("DoingZakum"):
	time.sleep(2)
	print("Doing IA")
	if inner1 !=2:
		Quest.StartQuest(12394, 9010000)
	elif inner2 !=2:
		Quest.StartQuest(12395, 9010000)
	elif inner3 !=2:
		Quest.StartQuest(12396, 9010000)
'''
###### Monster park starting at level 143
if (level >= 116 and level <= 149) and not SCLib.GetVar("MPDone") and not SCLib.GetVar("DoingZakum") and do_MP and Character.GetHP() > 0:
	SCLib.UpdateVar("DoingMP",True)
	Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
	toggle_rush_by_level(False)
	Terminal.SetCheckBox("bot/kanna_kami",True)
	Terminal.SetSpinBox("bot/kanna_kami_delay",5000)
	if level_checker():
		die_map = 100010000
		rush_out_MP()
		Terminal.Rush(die_map)
		Terminal.SetSpinBox("AutoDieExp",70)
		time.sleep(15)
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
		time.sleep(shortSleep)
		Key.Press(0x08)
		time.sleep(shortSleep)
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
		enterDungeon()
		time.sleep(1)
		SCLib.UpdateVar("retry_count",SCLib.GetVar("retry_count")+1)
		print("Count + 1")

#auto star force pensalir gear and accessories
if level >= 140 and star_force and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and Character.GetMeso()>= 5000000 and not SCLib.GetVar("cube_lock"):
	if accountData["cubing_done"]:
		for x in range(-100, 0):
			item = Inventory.GetItem(1, x)
			if item.valid and item.currentStar != star_force_level:
				starItem(x, item.currentStar, item.maxStar, star_force_level, item.id) 
	else:
		for equips in equip_slot_list:
			item = Inventory.GetItem(1,equips)
			if item.valid and item.id in equip_valid_list and item.currentStar != star_force_level:
				#print("Starforcing item {}".format(item.id))
				starItem(equips, item.currentStar, item.maxStar, star_force_level, item.id)
		for accessories in accessory_slot_list:
			item = Inventory.GetItem(1,accessories)
			if item.valid and item.id in accessory_list and item.currentStar != star_force_level:
				#print("Starforcing item {}".format(item.id))
				starItem(accessories, item.currentStar, item.maxStar, star_force_level, item.id)
	

#ZAKUM DAILY
if KillZakumDaily == False and (field_id == TheDoorToZakum or field_id == EntranceToZakumAlter) and not SCLib.GetVar("DoingMP"):
	if field_id == TheDoorToZakum:
		if pos.x != -3003:
			Character.Teleport(-3003, -220)
			time.sleep(0.5)
			Character.EnterPortal()
			SCLib.UpdateVar("DoingZakum",False)
			toggle_rush_by_level(True)
			Terminal.SetCheckBox("map/maprusher/hypertelerock",False)
	elif (field_id == TheDoorToZakum or field_id == EntranceToZakumAlter or field_id == TheCaveOfTrials3Zakum):
		if pos.x != -1599:
			Character.Teleport(-1599, -331)
			time.sleep(0.5)
			Character.EnterPortal()

if KillZakumDaily and level >= 120 and not SCLib.GetVar("DoingMP") and not accountData["cubing_done"]:
	print("Doing Zakum")
	Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
	toggle_rush_by_level(False)
	Terminal.SetCheckBox('filter_equip',False)
	SCLib.UpdateVar("DoingZakum",True)
	pos = Character.GetPos()
	if field_id not in ZakumsAltar:
		if field_id != EntranceToZakumAlter:
			if field_id != TheDoorToZakum:
				GetToTheDoorToZakum()
			else:
				if pos.x != -720:
					NewY = pos.y -5
					Character.Teleport(-720, NewY)
				elif Inventory.GetItemCount(4001017) < 1:
					Npc.ClearSelection()
					Npc.RegisterSelection("Receive an offering for Zakum.")
					time.sleep(1)
					Npc.RegisterSelection("Normal/Chaos Zakum")
					Character.TalkToNpc(2030008)
					time.sleep(1)
				else:
					print("Entering Portal to EntranceToZakumAlter")
					Npc.ClearSelection()
					Npc.RegisterSelection("Normal Zakum")
					time.sleep(1)
					Character.EnterPortal()
					time.sleep(1)
		else:
			if not NowLockedVar:
				if SCLib.GetVar("zakum_retry_count") >= 7:
					SCLib.UpdateVar("KillZakumDaily",False)
					ResetNowLockedFunction()
				else:
					Party.CreateParty()
					print("Talking to Adobis to enter ZakumsAltar")
					Character.TalkToNpc(2030013)
					SCLib.UpdateVar("zakum_retry_count",SCLib.GetVar("zakum_retry_count")+1)
					time.sleep(1)

			else:
				print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
				SCLib.UpdateVar("KillZakumDaily", False)
				ResetNowLockedFunction()
	else:
		print("In zakum altar")
		NowLockedFunction()
		boss2 = Field.FindMob(NormalZakumv2)
		boss1 = Field.FindMob(NormalZakumv1)
		boss = Field.FindMob(NormalZakum)
		if boss.valid or boss1.valid or boss2.valid:
			print("Boss valid")
			DidSpawn()
			if pos.x != -353:
				Character.Teleport(-353, 84)
			else:
				print("Fighting Zakum StandBy")
		else:
			if HasSpawned:
				print("Zakum is dead, waiting 10 sec before continue")
				time.sleep(5)
				face_drop = Field.FindItem(condensed_power_crystal)
				if face_drop.valid:
					print("Found condensed power crystal")
					Character.Teleport(face_drop.x,face_drop.y)
					Terminal.SetCheckBox("Auto Loot",True)
					time.sleep(3)
				eye_drop = Field.FindItem(aquatic_letter_eye)
				if eye_drop.valid:
					print("Found aquatic letter eye")
					Character.Teleport(eye_drop.x,eye_drop.y)
					Terminal.SetCheckBox("Auto Loot",True)
					time.sleep(3)
				face_check = Field.FindItem(condensed_power_crystal)
				eye_check = Field.FindItem(aquatic_letter_eye)
				time.sleep(5)
				if not face_check.valid and not eye_check.valid:
					print("Did not find accessory, leaving.")
					Character.TalkToNpc(2030010)
					time.sleep(1)
					SCLib.UpdateVar("KillZakumDaily", False)
					ResetSpawn()
					ResetNowLockedFunction()
					if field_id == TheDoorToZakum:
						if pos.x != -3003:
							Character.Teleport(-3003, -220)
							time.sleep(1)
							Character.EnterPortal()
							SCLib.UpdateVar("DoingZakum",False)
			else:
				print("Finding item in inventory to drop")
				stone = Inventory.FindItemByID(4001017)
				if stone.valid:
					if pos.x != -25:
						Character.Teleport(-25, 84)
					else:
						print("Dropping stone to spawn Zakum")
						Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)


############IA
############IA
############IA

if Character.GetHonorExp() > 60000:
	Terminal.SetSpinBox("special/IAStat",11)
elif Character.GetHonorExp() <= 60000:
	Terminal.SetSpinBox("special/IAStat",10)
	
'''
if Character.GetHP() > 0 and DoIA and level > 70 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("cube_lock"):
	#IA_count = 0
	#while IA_count < 5 :
#		print("Doing IA rerolling, number of rerolls = {}".format(IA_count))
#		IA_count += 1
	#print("Checking IA reroll")
	innerAbility1 = Quest.GetQuestState(12394)
	innerAbility2 = Quest.GetQuestState(12395)
	innerAbility3 = Quest.GetQuestState(12396)

	if innerAbility1 == 0:
		Terminal.SetCheckBox("Auto NPC", True)
		Quest.StartQuest(12394, 9010000)
	elif innerAbility2 == 0:
		Terminal.SetCheckBox("Auto NPC", True)
		Quest.StartQuest(12395, 9010000)
	elif innerAbility3 == 0:
		Terminal.SetCheckBox("Auto NPC", True)
		Quest.StartQuest(12396, 9010000)
	elif innerAbility3 == 2:
		if not Terminal.GetCheckBox("special/IAReset"):
			print("Enabling IA rerolling")
			Terminal.SetCheckBox("special/IAReset",True)
'''
'''
		RerollIA()
		Lines = { }
		for x in range(0, 3):
			result = Packet.WaitForRecv(IARecv, 1000)
			result.Skip(2)
			lineNum = result.ReadLong(2)
			id = result.ReadLong(4)
			value = result.ReadLong(2)
			Lines[id] = [lineNum, value]

		TotalLines = { }
		for key1, value1 in Lines.items():
			lineResults = GetLineValue(str(value1[0]), value1[1], key1)
			if (lineResults != None):
				for key, value in lineResults.items():
					if key in TotalLines:
						newVal = TotalLines[key] + value
						TotalLines[key] = newVal
					else:
						TotalLines[key] = value
			else:
				print("None Type:" + str(value1[0]) + ", "+ str(value1[1]) + ", "+ str(key1[1]))


		#should it be multiple choice? should it search for all requirments? (Right now only looks for 1 requirment)
		#CHANGE HERE
		statsWant = { StatChooser["Mesos Obtained"] : 8 }

		print("Total Stats Combined")
		for key, value in TotalLines.items():
			if key in statsWant:
				if (value >= statsWant[key]):
					print("Requirment Met: "+ Inv_Stats [key] + " +" + str(value))
					markFinished(charData, charID)
					writeJson(charData)
			else:
				print (Inv_Stats [key] + " +" + str(value))
		'''
#print(charID)
#####cubing
if not accountData['cubing_done'] and level >=145 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
	#plan
	#check if we have the items to cube
	#first mark the items we need to cube
	#keep a .json file for every character so that we know what items still need to be cubed
	#then buy
	SCLib.UpdateVar("DoingBG",False)
	el_nath = 211000000
	necklace = "necklace"
	eye = 'eye'
	face = 'face'
	earring = 'earring'
	ring = 'ring'
	cubeid = 5062009

	accountId = Terminal.GetLineEdit("LoginID")
	accountData = startupCheck_cube(accountId)
	for token in [necklace,eye,face,earring,ring]:
		handleToken(accountData, token, 0)
	handleReady(accountData)
	writeJson_cube(accountData,accountId)
	curr_map = Field.GetID()
	if curr_map != el_nath and not accountData['ready_for_cube'] and not SCLib.GetVar("checked_equip") :
		toggle_rush_by_level(False)
		SCLib.UpdateVar("cube_lock",True)
		if not Terminal.IsRushing():
			Terminal.Rush(el_nath)
			time.sleep(1)
		
	elif curr_map == el_nath and not accountData['ready_for_cube'] and not SCLib.GetVar("checked_equip") :
		toggle_rush_by_level(False)
		SCLib.UpdateVar("cube_lock",True)
		if not accountData['ready_for_cube']:
			print("Taking off equips and revealing potential")
			Terminal.SetCheckBox("Auto Equip",False)
			take_off_equip()
			time.sleep(1)
			take_off_equip()
			time.sleep(1)
			reveal_all_potential()
			time.sleep(1)
			find_move_face()
			time.sleep(1)
			find_move_earring()
			time.sleep(1)
			find_move_eye()
			time.sleep(1)
			find_move_necklace()
			time.sleep(1)
			find_move_ring()
			time.sleep(1)
			
			for equip_slot_number in range(1,9):
				item = Inventory.GetItem(1,equip_slot_number)
				for i in reversed(range(1,5)):
					if item.grade == i:
						if item.id in ring_list:
							if item.pos-4 > accountData[ring]:
								print(accountData[ring],item.pos-4)
								addOne_cube(accountData,ring)
						elif item.id in face_list:
							asOne_cube(accountData,face)
						elif item.id in eye_list:
							asOne_cube(accountData,eye)
						elif item.id in earring_list:
							asOne_cube(accountData,earring)
						elif item.id in necklace_list:
							asOne_cube(accountData,necklace)
						else:
							print("Something must have went wrong")
			writeJson_cube(accountData,accountId)
			accessory_count = 0
			for token in [necklace,eye,face,earring,ring]:
				accessory_count += accountData[token]
			not_ring_count = 0
			for token in [necklace,eye,face,earring]:
				not_ring_count += accountData[token]
			print("Number of accessories currently available for cube = {}".format(accessory_count))
			if accessory_count >= 5:
				mark_ready_for_cube(accountData)
				writeJson_cube(accountData,accountId)
			if accessory_count > 5:
				print("Too many rings")
				accountData['ring'] = 5-not_ring_count
				writeJson_cube(accountData,accountId)
			SCLib.UpdateVar("checked_equip",True)
			print("Checked equipments")
			SCLib.UpdateVar("cube_lock",False)
	if accountData['ready_for_cube'] and Inventory.FindItemByID(5062009).valid and not accountData['cubing_done']:
		#Face
		SCLib.UpdateVar("cube_lock",True)
		toggle_rush_by_level(False)
		cube_sleep_time = 0.75
		if curr_map != el_nath:
			Terminal.Rush(el_nath)
			time.sleep(1)
		elif not SCLib.GetVar("took_off"):
			take_off_equip()
			time.sleep(1)
			take_off_equip()
			time.sleep(1)
			reveal_all_potential()
			time.sleep(1)
			find_move_face()
			time.sleep(1)
			find_move_earring()
			time.sleep(1)
			find_move_eye()
			time.sleep(1)
			find_move_necklace()
			time.sleep(1)
			find_move_ring()
			time.sleep(1)
			SCLib.UpdateVar("took_off",True)
		else:
			for i in reversed(range(1,5)):
				if accountData['face'] == 1 and not accountData['face_done']:
					find_move_face()
					if not containMesosObtained(Inventory.GetItem(1,1)):
						print("Cubing face")
						item = Inventory.GetItem(1,1)
						if item.grade == i:
							if item.option1 == 0:
								reveal_potential(1)
							Inventory.UseCube(cubeid,1)
							time.sleep(cube_sleep_time)
							break
					elif containMesosObtained(Inventory.GetItem(1,1)):
						print("Face with meso obtained")
						accountData['face_done'] = True
						time.sleep(1)
						Inventory.SendChangeSlotPositionRequest(1, 1,face_slot, -1)
				elif accountData['face'] == 0:
					print("No face needs to be cubed")
					accountData['face_done'] = True
				#Eye
				if accountData['eye'] == 1 and not accountData['eye_done']:
					find_move_eye()
					if not containMesosObtained(Inventory.GetItem(1,2)):
						print("Cubing eye")
						item = Inventory.GetItem(1,2)
						if item.grade == i:
							if item.option1 == 0:
								reveal_potential(2)
							Inventory.UseCube(cubeid,2)
							time.sleep(cube_sleep_time)
							break
					elif containMesosObtained(Inventory.GetItem(1,2)):
						print("Eye with meso obtained")
						accountData['eye_done'] = True
						time.sleep(1)
						Inventory.SendChangeSlotPositionRequest(1, 2,eye_slot, -1)
				elif accountData['eye'] == 0:
					print("No eye needs to be cubed")
					accountData['eye_done'] = True
				#Earring
				if accountData['earring'] == 1 and not accountData['earring_done']:
					find_move_earring()
					if not containMesosObtained(Inventory.GetItem(1,3)):
						print("Cubing earring")
						item = Inventory.GetItem(1,3)
						if item.grade == i:
							if item.option1 == 0:
								reveal_potential(3)
							Inventory.UseCube(cubeid,3)
							time.sleep(cube_sleep_time)
							break
					elif containMesosObtained(Inventory.GetItem(1,3)):
						print("Earring with meso obtained")
						accountData['earring_done'] = True
						time.sleep(1)
						Inventory.SendChangeSlotPositionRequest(1, 3,earring_slot, -1)
				elif accountData['earring'] == 0:
					print("No earring needs to be cubed")
					accountData['earring_done'] = True
				#Necklace
				if accountData['necklace'] == 1 and not accountData['necklace_done']:
					find_move_necklace()
					if not containMesosObtained(Inventory.GetItem(1,4)):
						print("Cubing necklace")
						item = Inventory.GetItem(1,4)
						if item.grade == i:
							if item.option1 == 0:
								reveal_potential(4)
							Inventory.UseCube(cubeid,4)
							time.sleep(cube_sleep_time)
							break
					elif containMesosObtained(Inventory.GetItem(1,4)):
						print("Necklace with meso obtained")
						accountData['necklace_done'] = True
						time.sleep(1)
						Inventory.SendChangeSlotPositionRequest(1, 4,necklace_slot, -1)
				elif accountData['necklace'] == 0:
					print("No necklace needs to be cubed")
					accountData['necklace_done'] = True
				if accountData['ring'] != 0 and not accountData['ring_done']:
					number_of_rings = accountData['ring']
					print('Cubing rings')
					find_move_ring()
					if number_of_rings == 1:
						if not containMesosObtained(Inventory.GetItem(1,5)):
							item = Inventory.GetItem(1,5)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(5)
								Inventory.UseCube(cubeid,5)
								time.sleep(cube_sleep_time)
								break
						elif containMesosObtained(Inventory.GetItem(1,5)):
							print("Rings cubing done")
							accountData['ring_done'] = True
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 5,ring1_slot, -1)
					elif number_of_rings == 2:
						if not containMesosObtained(Inventory.GetItem(1,5)):
							item = Inventory.GetItem(1,5)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(5)
								Inventory.UseCube(cubeid,5)
								time.sleep(cube_sleep_time)
								break
						elif not containMesosObtained(Inventory.GetItem(1,6)):
							item = Inventory.GetItem(1,6)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(6)
								Inventory.UseCube(cubeid,6)
								time.sleep(cube_sleep_time)
								break
						elif containMesosObtained(Inventory.GetItem(1,5)) and containMesosObtained(Inventory.GetItem(1,6)):
							print("Rings cubing done")
							accountData['ring_done'] = True
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 5,ring1_slot, -1)
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 6,ring2_slot, -1)
					elif number_of_rings == 3:
						if not containMesosObtained(Inventory.GetItem(1,5)):
							item = Inventory.GetItem(1,5)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(5)
								Inventory.UseCube(cubeid,5)
								time.sleep(cube_sleep_time)
								break
						elif not containMesosObtained(Inventory.GetItem(1,6)):
							item = Inventory.GetItem(1,6)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(6)
								Inventory.UseCube(cubeid,6)
								time.sleep(cube_sleep_time)
								break
						elif not containMesosObtained(Inventory.GetItem(1,7)):
							item = Inventory.GetItem(1,7)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(7)
								Inventory.UseCube(cubeid,7)
								time.sleep(cube_sleep_time)
								break
						elif containMesosObtained(Inventory.GetItem(1,5)) and containMesosObtained(Inventory.GetItem(1,6)) and containMesosObtained(Inventory.GetItem(1,7)):
							print("Rings cubing done")
							accountData['ring_done'] = True
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 5,ring1_slot, -1)
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 6,ring2_slot, -1)
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 7,ring3_slot, -1)
					elif number_of_rings == 4:
						if not containMesosObtained(Inventory.GetItem(1,5)):
							item = Inventory.GetItem(1,5)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(5)
								Inventory.UseCube(cubeid,5)
								time.sleep(cube_sleep_time)
								break
						elif not containMesosObtained(Inventory.GetItem(1,6)):
							item = Inventory.GetItem(1,6)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(6)
								Inventory.UseCube(cubeid,6)
								time.sleep(cube_sleep_time)
								break
						elif not containMesosObtained(Inventory.GetItem(1,7)):
							item = Inventory.GetItem(1,7)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(7)
								Inventory.UseCube(cubeid,7)
								time.sleep(cube_sleep_time)
								break
						elif not containMesosObtained(Inventory.GetItem(1,8)):
							item = Inventory.GetItem(1,8)
							if item.grade == i:
								if item.option1 == 0:
									reveal_potential(8)
								Inventory.UseCube(cubeid,8)
								time.sleep(cube_sleep_time)
								break
						elif containMesosObtained(Inventory.GetItem(1,5)) and containMesosObtained(Inventory.GetItem(1,6)) and containMesosObtained(Inventory.GetItem(1,7)) and containMesosObtained(Inventory.GetItem(1,8)):
							print("Rings cubing done")
							accountData['ring_done'] = True
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 5,ring1_slot, -1)
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 6,ring2_slot, -1)
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 7,ring3_slot, -1)
							time.sleep(1)
							Inventory.SendChangeSlotPositionRequest(1, 8,ring4_slot, -1)
					elif accountData['ring'] == 0:
						accountData['ring_done'] = True
		writeJson_cube(accountData,accountId)
	elif accountData['ready_for_cube'] and not Inventory.FindItemByID(5062009).valid and not accountData['cubing_done']:
		print("Attempting to buy cubes")
		toggle_rush_by_level(False)
		if Character.GetMeso() > 800000000:
			toggle_rush_by_level(False)
			SCLib.UpdateVar("cube_lock",True)
			if Terminal.IsRushing():
				print("Still rushing")
				time.sleep(3)
			elif curr_map != el_nath:
				print("Rush to el_nath")
				Terminal.Rush(el_nath)
				time.sleep(3)
			else:
				buy_cubes()
		else:
			SCLib.UpdateVar("cube_lock",False)
			SCLib.UpdateVar("took_off",False)
			check_meso_equip()
			print('Not enough mesos, go back to farm')
	if accountData['ring_done'] and accountData['face_done'] and accountData['eye_done'] and accountData['earring_done'] and accountData['necklace_done']:
		accountData['cubing_done'] = True
		SCLib.UpdateVar("cube_lock",False)
		writeJson_cube(accountData,accountId)
elif accountData['cubing_done'] and SCLib.GetVar("cube_lock"):
	print("Cubing done, release cube lock")
	SCLib.UpdateVar("cube_lock",False)

if not SCLib.GetVar("GetEarringDone") and not accountData['ready_for_cube'] and not SCLib.GetVar("cube_lock") and SCLib.GetVar("checked_equip") and Character.GetHP() > 0 and level >= 145 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and accountData['earring'] == 0:
	SCLib.UpdateVar("GettingEarring",True)
	get_earring()
	for item in Inventory.GetItems(1):
		if item.id == half_earrings:
			if item.grade > 0 and item.option1 == 0:
				SCLib.UpdateVar("GettingEarring",False)
				SCLib.UpdateVar("GetEarringDone",True)
#####Black gate	
DoBlackGate = not accountData['ready_for_cube']
#print(SCLib.GetVar("cube_lock"))
if DoBlackGate and not SCLib.GetVar("cube_lock") and SCLib.GetVar("checked_equip") and Character.GetHP() > 0 and level >= 145 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("GettingEarring") and not SCLib.GetVar("GettingLep"):
    toggle_rush_by_level(False)
    map = Field.GetID()
    channel = GameState.GetChannel()
    print("Blackgate farming")
    SCLib.UpdateVar("DoingBG",True)
    if Terminal.GetCheckBox('filter_equip'):
        Terminal.SetCheckBox('filter_equip',False)
    if not Terminal.GetCheckBox('Kami Loot'):
        Terminal.SetCheckBox('Kami Loot',True)
    if not Terminal.GetCheckBox('Auto Loot'):
        Terminal.SetCheckBox('Auto Loot',True)
    Terminal.SetSpinBox("FilterMeso",0) 
    if Inventory.GetEmptySlotCount(1) == 0:
        if not Terminal.IsRushing():
            Terminal.Rush(henesys)
    if farmed_enough_accessories():
        print("farmed enough accessories")
        SCLib.UpdateVar("DoingBG",False)
        SCLib.UpdateVar("checked_equip",False)
    if Terminal.IsRushing():
        print("Rushing... Please wait...")
        #if map == 610050000:
        #    Terminal.StopRush()
        time.sleep(2)
    # IF FOR SOME REASON U END UP IN HENE
    elif map not in blackgate_maps:
        print("Rushing to blackgate")
        Terminal.Rush(610050000)
    # IF AT BDF MAIN MAP
    elif map == 610050000:
        time.sleep(2)
        if channel == 30:
            channel = 1
        else:
            channel += 1
        Terminal.ChangeChannel(channel)
        while Terminal.IsRushing():
            time.sleep(2)
        print("Current channel" + str(GameState.GetChannel()))
        print("Rushing to starting map")
        Terminal.Rush(610050100)

        #################################OUTER
    elif map == 610050100:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("south00")
        Terminal.Rush(610051200)
    elif map == 610051200:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("east00")
        Terminal.Rush(610051100)
    elif map == 610051100:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("east00")
        Terminal.Rush(610051000)
    elif map == 610051000:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        Terminal.Rush(610050900)
    elif map == 610050900:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("east00")
        Terminal.Rush(610050800)
    elif map == 610050800:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("north00")
        Terminal.Rush(610050700)
    elif map == 610050700:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("north00")
        Terminal.Rush(610050600)
    elif map == 610050600:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("west00")
        Terminal.Rush(610050500)
    elif map == 610050500:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("west00")
        Terminal.Rush(610050400)
    elif map == 610050400:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("west00")
        Terminal.Rush(610050300)
    elif map == 610050300:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("west00")
        Terminal.Rush(610050200)
    elif map == 610050200:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        Terminal.Rush(610051300)
    #####################################INNER
    elif map == 610051300:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("south00")
        Terminal.Rush(610052000)
    elif map == 610052000:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("east00")
        Terminal.Rush(610051900)
    elif map == 610051900:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("east00")
        Terminal.Rush(610051800)
    elif map == 610051800:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("north00")
        Terminal.Rush(610051700)
    elif map == 610051700:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("north00")
        Terminal.Rush(610051600)
    elif map == 610051600:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("west00")
        Terminal.Rush(610051500)
    elif map == 610051500:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        #EnterPortal("west00")
        Terminal.Rush(610051400)
    elif map == 610051400:
        print("Arrived in "+str(map)+"...")
        BossCheck()
        Terminal.Rush(610050000) #BACK TO STARTING POINT

if Character.GetMeso() >= 7900000 and accountData["cubing_done"] == True and Inventory.GetEmptySlotCount(2) < 3 and Inventory.GetEmptySlotCount(2) > 0 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
	store_map = 240000002
	print("Buying expansion item")
	toggle_rush_by_level(False)
	SCLib.UpdateVar("BuyingExpansion",True)
	if not Terminal.IsRushing():
		if Field.GetID() != store_map:
			Terminal.Rush(store_map)
			time.sleep(2)
		elif Field.GetID() == store_map:
			Terminal.SetPushButton("Use item",False)
			buy_expansion()
			Terminal.SetPushButton("Leave shop",True)
			time.sleep(1)
			Inventory.UseItem(2430965)
			Inventory.UseItem(2433937)
			time.sleep(2)
			Terminal.SetPushButton("Leave shop",False)
			buy_expansion()
			Terminal.SetPushButton("Leave shop",True)
			time.sleep(1)
			Inventory.UseItem(2430965)
			Inventory.UseItem(2433937)
			time.sleep(2)
			Terminal.SetPushButton("Leave shop",False)
			buy_expansion()
			Terminal.SetPushButton("Leave shop",True)
			time.sleep(1)
			Inventory.UseItem(2430965)
			Inventory.UseItem(2433937)
			time.sleep(2)
			Terminal.SetPushButton("Leave shop",False)
			buy_expansion()
			Terminal.SetPushButton("Leave shop",True)
			time.sleep(1)
			Inventory.UseItem(2430965)
			Inventory.UseItem(2433937)
			Terminal.SetPushButton("Leave shop",False)
			SCLib.UpdateVar("BuyingExpansion",False)
			Terminal.SetPushButton("Use item",True)
	else:
		print("Still rushing waiting to buy expansion")
		time.sleep(2)
