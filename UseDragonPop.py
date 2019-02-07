import Character, Context, DataType, Field, Inventory, Key, Npc, Packet, Quest, Terminal, time, GameState, sys, Login

#if not any("SunCat" in s for s in sys.path):
#    sys.path.append(os.getcwd() + "\SunCat")

#try:
#	import SunCat, SCLib, SCHotkey
#except:
#	print("Couldn't find SunCat module")

#buffs = Character.GetBuffs()
#for buff in buffs:
#	print("Current Buff Id: {}; Remaining Time: {}".format(buff.id,buff.timeLeft))
#print(Character.HasBuff(2,80002280))
#Inventory.UseItem(5000241)
def buy_cubes():
	buy_count = 0
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
		if not GameState.IsInGame():
			break
	while buy_count < 1:
		time.sleep(2)
		start_slot += 1
		print("Buying cube pack number {}".format(buy_count+1))
		buy_cube_packet = Packet.COutPacket(0x0540)
		buy_cube_packet.EncodeBuffer("55 052F841E 044AA200")
		Packet.SendPacket(buy_cube_packet)
		rPacket = Packet.WaitForRecv(0x06D3,15000)
		rPacket.Skip(1)
		x = rPacket.ReadLong(4)
		time.sleep(1)
		out = hex(x)
		out = '0x' + out[2:].zfill(8)
		first_byte = out[8:10]
		second_byte = out[6:8]
		third_byte = out[4:6]
		fourth_byte = out[2:4]
		take_out = Packet.COutPacket(0x0540)
		take_out.EncodeBuffer("0F {} {} {} {} 00 00 00 00 79 3D 4D 00 05 {} 00".format(first_byte,second_byte,third_byte,fourth_byte,hex(start_slot).split('x')[1].zfill(2)))
		print("0F {} {} {} {} 00 00 00 00 05 {} 00".format(first_byte,second_byte,third_byte,fourth_byte,hex(start_slot).split('x')[1].zfill(2)))
		Packet.SendPacket(take_out)
		print("out is {}".format(out))
		buy_count += 1

buy_cubes()
#Key.Press(0xA2)
#users = Terminal.GetLocalUsers()
#for user in users:
#	print(user.clientid,":",user.mapid)
#Terminal.LeaveCashShop()
#oPacket = Packet.COutPacket(herb_header)
#oPacket.EncodeBuffer("2F F8 04 00")
#Packet.SendPacket(oPacket)
#print("sending out packet to interact with herb!!!!")
#print("finding necklace")
#items = Inventory.GetItems(5)
#print('sdasd',Inventory.FindItemByID(5062009).valid)
#oPacket = Packet.COutPacket(herb_header)
#buy_header = 0x04EE
#collide_header = 0x00FC
#buy_ticket_packet = Packet.COutPacket(buy_header)
#buy_ticket_packet.EncodeBuffer("54 052F83EE 003567E0")
#Packet.SendPacket(buy_ticket_packet)
#dummy = Packet.WaitForRecv(0x066F,100000)
#rPacket = Packet.WaitForRecv(0x066F,100000000)
#print(rPacket)
#rPacket.Skip(3)
#rPacket.ReadLong(8)
#rPacket.Skip(rPacket.GetRemaining())
#print(dummy.GetRemaining())
#print(dummy.ReadStr())
#rPacket.Skip(1)
#x = rPacket.ReadLong(2)

#time.sleep(0.5)
#out = hex(x)
#first = out[4:6]
#last = out[2:4]
#take_out = Packet.COutPacket(buy_header)
#take_out.EncodeBuffer("0F {} {} 4C 05 00 00 00 00 05 01 00".format(first,last))
#print("0F {} {} 4C 05 00 00 00 00 05 01 00".format(first,last))
#Packet.SendPacket(take_out)
#print(Inventory.GetItemSlotCount(5))
#print(rPacket.ReadStr())
#potential_header = 0x0133
#oPacket = Packet.COutPacket(collide_header)
#oPacket.EncodeBuffer("** ** ** ** 01")
#04EE 54 052F83EE 003567E0
 #03E3 [C7323C0B] channel7 
#03E3 [4835CA0B] channel2 03E3 [F2A6DC0B] #03E3 [FC0E430B]
#print("Sending out packet to interact with herb")
#Packet.SendPacket(oPacket)
#result = Packet.WaitForRecv(0x066F,10000)
#print(result)
#while result.GetRemaining() > 0:
#	print(result.ReadLong(2))
#packet = str(result)
#print(packet)
#time.sleep(1)

#Terminal.LeaveCashShop()
#Character.TalkToNpc(8650012)
#quest_item = Inventory.FindItemByID(4009286)
#if quest_item.valid:
#	Inventory.SendChangeSlotPositionRequest(4, quest_item.pos, 0, 1)

#item = Inventory.FindItemByID(1032022)
#if item.valid:
#	print(item.pos)
'''
def collide_items():
	oPacket = Packet.COutPacket(collide_header)
	oPacket.EncodeBuffer("** ** ** ** 01")
	Packet.SendPacket(oPacket)

equip_slot = 1
remain_slots = Inventory.GetEmptySlotCount(equip_slot)
max_slots = Inventory.GetItemSlotCount(equip_slot)
for slots in accessory_slot_list:
	if remain_slots > 0:
		Inventory.SendChangeSlotPositionRequest(1, slots,max_slots, -1)
		time.sleep(0.5)
		collide_items()
		time.sleep(1)

def reveal_potential(itemPos):
	oPacket = Packet.COutPacket(potential_header)
	oPacket.EncodeBuffer("** ** ** 00 7F 00")
	oPacket.Encode2(itemPos)
	Packet.SendPacket(oPacket)
	rPacket = Packet.WaitForRecv(0x0254,5000)

item_list = Inventory.GetItems(1)
for item in item_list:
	if item.grade >= 1:
		reveal_potential(item.pos)
'''