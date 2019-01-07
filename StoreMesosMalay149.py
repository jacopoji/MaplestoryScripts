import Character
import Packet
import Terminal
import time
import GameState
import Field, Inventory

header = 0x00F0
block_header = 0x064E
crafting_header = 0x01D8
craft_recv_header = 0x0311

job = Character.GetJob()
level = Character.GetLevel()
storage_map_id = 550000000
storage_npc_id = 9270054
profile_path = 'C:/Users/Jacopo/Desktop/TerminalManager/terminalProfiles/StoreMesos149.xml'

pensalir_mage_cape = 1102719
pensalir_mage_helmet = 1004230
pensalir_mage_gloves = 1082609
pensalir_mage_shoes = 1072968
pensalir_mage_overall = 1052800
utgard_fan = 1552102
pensalir_equips =[pensalir_mage_cape,pensalir_mage_gloves,pensalir_mage_helmet,pensalir_mage_shoes,pensalir_mage_overall,utgard_fan]
collectID = [200000,200001,200002,200003,200004,200005,200006,200007,200008,200009,200010,200011,200012,200013,100000,100001,100002,100003,100004,100005,100006,100007,100008,100009,100010,100011,100012,100013]
byebye_maps = range(551030001,551030020)

ardentmill = 910001000
ardentmill_x = 302
ardentmill_y = 530

def mine(reactor):
    pos = Character.GetPos()
    if reactor.valid:
        if pos.x != reactor.x:
            Character.AMoveX(reactor.x)
        elif pos.x == reactor.x and pos.y!=reactor.y:
            if pos.y < reactor.y:
                #go up
                pass

def toggle_rush_by_level(indicator):
	Terminal.SetCheckBox("Rush By Level",indicator)
	Terminal.SetRushByLevel(indicator)

def rush_to_ardentmill():
    while Field.GetID() != 910001000:
        if Field.GetID() != 550000000:
            Terminal.Rush(550000000)
            print("Rushing to Ardentmill portal")
            time.sleep(2)
        elif Character.GetPos().x !=2506:
            time.sleep(1)
            Character.Teleport(2506,10)
        else:
            time.sleep(0.5)
            Character.EnterPortal()

def leave_ardentmill():
    print("Leaving Ardentmill")
    if Character.GetPos().x != 976:
        Character.Teleport(976,-190)
        time.sleep(1)
    else:
        Character.EnterPortal()

def extract_item():
    if Field.GetID()!=ardentmill:
        rush_to_ardentmill()
    elif Character.GetPos().x != ardentmill_x:
        time.sleep(1.5)
        Character.Teleport(ardentmill_x,ardentmill_y)
        time.sleep(1.5)
    else:
        items = Inventory.GetItems(1)
        for item in items:
            if item.id in pensalir_equips:
                print("Extracting item on slot {}".format(item.pos))
                id = hex(item.id)[2:].zfill(6)
                first_byte = id[4:6]
                second_byte = id[2:4]
                third_byte = id[0:2]
                sn = hex(item.sn)[2:].zfill(16)
                byte8 = sn[0:2]
                byte7 = sn[2:4]
                byte6 = sn[4:6]
                byte5 = sn[6:8]
                byte4 = sn[8:10]
                byte3 = sn[10:12]
                byte2 = sn[12:14]
                byte1 = sn[14:16]
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
                Packet.WaitForRecv(craft_recv_header,1100)

def store_mesos():
    while True:
        if Field.GetID() == storage_map_id:
            print("Current Mesos before store = {}".format(Character.GetMeso()))
            Packet.BlockRecvHeader(block_header)
            Character.Teleport(2268,17)
            time.sleep(1)
            Character.TalkToNpc(storage_npc_id)
            time.sleep(1)
            oPacket = Packet.COutPacket(header)
            oPacket.EncodeBuffer("07 FFFFFFF903DC5401")
            Packet.SendPacket(oPacket)
            oPacket1 = Packet.COutPacket(header)
            oPacket1.Encode2(8)
            Packet.SendPacket(oPacket1)
            print("Completed meso storing")
            time.sleep(1)
            print("Current Mesos after store = {}".format(Character.GetMeso()))
            break
        else:
            Terminal.Rush(storage_map_id)
            print("Still rushing to storage")
            time.sleep(2)

if GameState.IsInGame():
    if job == 4212 and Character.GetMeso() == 29999999999:
        #if mesos =29999999999, which is max, store them in the storage   
        Terminal.SetRushByLevel(False)
        #Terminal.LoadProfile(r"C:\Users\Jacopo\Desktop\TerminalManager\terminalProfiles\StoreMesos.xml")
        store_mesos()
        #Next step is to change the AutoChar Number and then logon into the new created luminous and release control
        #Read AutoChar Number, +1 write to file.
        time.sleep(1)
        if Character.GetMeso() == 0:
            Terminal.Logout()
            time.sleep(1)
            Terminal.LoadProfile(profile_path)
    elif Inventory.GetEmptySlotCount(1) == 0 and not Terminal.IsRushing():
        toggle_rush_by_level(False)
        print("Starting extraction")
        for item in Inventory.GetItems(1):
            if item.id in pensalir_equips:
                extract_item()
        leave_ardentmill()
        time.sleep(0.5)
        toggle_rush_by_level(True)
    else:
        print("Still farming for mesos, sleep 30seconds")
        if Field.GetID() == ardentmill:
            leave_ardentmill()
        else:
            time.sleep(30)
'''
    elif Field.GetId() in byebye_maps:
        for reactors in collectID:
            find_reactor = Field.FindReactor(reactors)
            if find_reactor.valid:
                mine(find_reactor)
        time.sleep(30)
'''
    #end of code
#00E8 [08] close storage
#block 05E7

#block 063B


#c0001340000d215