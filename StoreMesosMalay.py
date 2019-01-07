import Character
import Packet
import Terminal
import time
import GameState
import Field

header = 0x00F0
block_header = 0x064E
job = Character.GetJob()
level = Character.GetLevel()
storage_map_id = 550000000
storage_npc_id = 9270054
profile_path = 'C:/Users/Jacopo/Desktop/TerminalManager/terminalProfiles/StoreMesos.xml'

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
else:
    print("Still farming for mesos, sleep 30seconds")
    time.sleep(30)

    #end of code
#00E8 [08] close storage
#block 05E7

#block 063B