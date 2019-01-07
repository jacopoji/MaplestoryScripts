import Character
import Packet
import Terminal
import time
import GameState
import Field

header = 0x00EE
job = Character.GetJob()
level = Character.GetLevel()
storage_map_id = 540000000
storage_npc_id = 9270042

def store_mesos():
    while True:
        if Field.GetID() == storage_map_id:
            Character.TalkToNpc(storage_npc_id)
            time.sleep(1)
            oPacket = Packet.COutPacket(header)
            oPacket.EncodeBuffer("07 FFFFFFF903DC5401")
            Packet.SendPacket(oPacket)
            oPacket1 = Packet.COutPacket(header)
            oPacket1.Encode2(8)
            Packet.SendPacket(oPacket1)
            print("Completed meso storing")
            break
        else:
            Terminal.Rush(storage_map_id)
            print("Still rushing to storage")
            time.sleep(1)


if job == 4212 and Character.GetMeso() == 29999999999:
    #if mesos =29999999999, which is max, store them in the storage   
    Terminal.SetRushByLevel(False)
    #Terminal.LoadProfile(r"C:\Users\Jacopo\Desktop\TerminalManager\terminalProfiles\StoreMesos.xml")
    store_mesos()
    Terminal.Logout()
    #Next step is to change the AutoChar Number and then logon into the new created luminous and release control
    #Read AutoChar Number, +1 write to file.
    CharName = Character.GetName()
    print("Changing profiles for {}".format(CharName))
    while True:
        try:
            f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'r')
            print("Successfully read meso bank number")
        except OSError: #initialization if there is no existing file yet
            f= open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'w')
            f.write('0')
            f.close()
            print("Successfully initialized meso bank number to 0")
        else: #if no need for initialization, then read the value and change AutoChar Number
            f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'r')
            temp = f.read() #save read value to a temp holder
            Terminal.SetLineEdit("LoginChar", str(int(temp)+1))
            f.close()
            #done with the creation of new character and the script ends
            print("done with the creation of new character and the script ends")
            break

    #end of code
#00E8 [08] close storage
#block 05E7