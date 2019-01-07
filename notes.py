# gnarled wooden key id 4033611
#colossal root map id 105200000 make party
#trading post map id 865000001 leave party
#big spider familiar 9960295
#eye of time familiar 9960350
import Character, Context, DataType, Field, Inventory, Key, Npc, Packet, Quest, Terminal, time, GameState, sys, Login, os

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCLib, SCHotkey
except:
	print("Couldn't find SunCat module")
print("Sending out packet")
pensalir_mage_cape = 1102719
pensalir_mage_helmet = 1004230
pensalir_mage_gloves = 1082609
pensalir_mage_shoes = 1072968
pensalir_mage_overall = 1052800
utgard_fan = 1552102
pensalir_equips =[pensalir_mage_cape,pensalir_mage_gloves,pensalir_mage_helmet,pensalir_mage_shoes,pensalir_mage_overall,utgard_fan]

store_header = 0x00F0
block_header = 0x064E
crafting_header = 0x01D8
craft_recv_header = 0x005F
items = Inventory.GetItems(1)
for item in items:
    if item.id == pensalir_mage_helmet:
        print("Extracting item on slot {}".format(item.pos))
        id = '{:06x}'.format(item.id)
        first_byte = id[4:6]
        second_byte = id[2:4]
        third_byte = id[0:2]
        sn = hex(item.sn)
        byte8 = sn[2:4]
        byte7 = sn[4:6]
        byte6 = sn[6:8]
        byte5 = sn[8:10]
        byte4 = sn[10:12]
        byte3 = sn[12:14]
        byte2 = sn[14:16]
        byte1 = sn[16:18]
        oPacket1 = Packet.COutPacket(crafting_header)
        oPacket1.EncodeBuffer("01 00 00 00")
        oPacket1.EncodeBuffer("00 00 00 00")
        oPacket1.EncodeBuffer("01 00 00 00")
        oPacket1.EncodeBuffer("60 3C 7C 05") #format is item id 00 item sn 
        oPacket1.EncodeBuffer("{} {} {} 00".format(first_byte,second_byte,third_byte))
        oPacket1.EncodeBuffer("{} {} {} {}".format(byte1,byte2,byte3,byte4))
        oPacket1.EncodeBuffer("{} {} {} {}".format(byte5,byte6,byte7,byte8))
        oPacket1.EncodeBuffer("01 00 00 00")
        oPacket1.EncodeBuffer("{} 00 00 00".format(hex(item.pos).split('x')[1].zfill(2))) #slot
        Packet.SendPacket(oPacket1)
        time.sleep(1.2)