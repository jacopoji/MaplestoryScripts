#01D8 00000000 057BF613 silver
#01D8 00000000 057BF612 opal
#01D8 00000000 057C1EAD arrow for bow
#01D8 00000000 057C1EAE arrow for crossbow
import Field, Character, Terminal, time, Quest, GameState, Inventory, Party, Packet,sys,os,Key,json, Login,Npc

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")
crafting_header = 0x01D8
craft_recv_header = 0x005F

def rush_to_ardentmill():
    if Field.GetID() != 550000000:
        Terminal.Rush(550000000)
        time.sleep(2)
    elif Character.GetPos().x !=2506:
        time.sleep(1)
        Character.Teleport(2506,10)
    else:
        time.sleep(0.5)
        Character.EnterPortal()

def leave_ardentmill():
    if Character.GetPos().x != 976:
        Character.Teleport(976,-190)
    else:
        Character.EnterPortal()

def extract_item():
    pensalir_mage_cape = 1102719
    pensalir_mage_helmet = 1004230
    pensalir_mage_gloves = 1082609
    pensalir_mage_shoes = 1072968
    pensalir_mage_overall = 1052800
    utgard_fan = 1552102
    pensalir_equips =[pensalir_mage_cape,pensalir_mage_gloves,pensalir_mage_helmet,pensalir_mage_shoes,pensalir_mage_overall,utgard_fan]

    ardentmill = 910001000
    ardentmill_x = 302
    ardentmill_y = 530
    if Field.GetID()!=ardentmill:
        rush_to_ardentmill()
    elif Character.GetPos.x != ardentmill_x:
        time.sleep(1)
        Character.Teleport(ardentmill_x,ardentmill_y)
    else:
        items = Inventory.GetItems(1)
        for item in items:
            if item.id in pensalir_equips:
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
                time.sleep(0.5)

#0100 05D2BC8D 01 0002 0000 0001
#028A 003ECA1C 00000000 00000000
#04A8 00 01 000000F8 00 00000000 931A49F1 00000000 0017AEE6 003ECA1C 00 0144 021C 00000000 00000000 0000000000000000 00000000 0000000000000000 00000000 0000000000000000 00 00 0144 021C 00000000 00 [008005BB46E61702] 00 00 0000 00 00000000 01 00
#04A8 00 00 000000F8
#03EC 01 05D2C42B 0144 021C 000000F8 6716220F 01 00050FBE 00050FBE
#006A 00 05D2C42B 00 00 0017AEE6 00000001
#04AA 02 000000F8
#01D8 [01000000] 00000000 00000001 [603C7C05E6AE17007C9300003601001C0100000002000000]
#sn in hex 0x1c 00 01 36 00 00 93 7c

#01D8 [01000000] 00000000 00000001 [603C7C05C6520F00599700002A01004C0100000002000000]
#01D8 [01000000] 00000000 00000001 [603C7C05C6520F00459900002A01004C0100000003000000]


