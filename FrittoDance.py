import Packet
import time
import GameState
import Quest
import Npc
import Field
import Character
import Terminal

SendPacketHeader = 0x050D
ReceivePacketHeader = 0x05F0


danceMap = 993057000

def ParsePacket(BrimGang):
    Result.Skip(16)
    BytesWanted_1 = Result.ReadLong(8)
    BytesWanted.append(BytesWanted_1)
    x = 0
    while x < Result.GetRemaining():
        Result.Skip(12)
        Boom = Result.ReadLong(8)
        BytesWanted.append(Boom)
        x = x +1

def Exploit(FrogGang):
    x = 0
    while x < len(FrogGang):
        BrimShit = Packet.COutPacket(SendPacketHeader)
        BrimShit.Encode4(0)
        BrimShit.Encode4(x)
        BrimShit.Encode8(FrogGang[x])
        Packet.SendPacket(BrimShit)
        x = x + 1

def LeaveDance():
    leavePacket = Packet.COutPacket(0x050E)
    Packet.SendPacket(leavePacket)

if Terminal.GetProperty("count",-1) == -1:
    Terminal.SetProperty("count",0)

if Terminal.GetProperty("danceDone",None) is None:
    Terminal.SetProperty("danceDone",False)

if not GameState.IsInGame():
    Terminal.SetProperty("count",0)
    Terminal.SetProperty("danceDone",False)
    Terminal.SetProperty("Once",True)
#print(Terminal.GetProperty("danceDone",None))
if GameState.IsInGame():
    if not Terminal.GetProperty("danceDone",None):
        if Field.GetID() not in range(danceMap,danceMap+20):
            #print("Not in dance map")
            if Field.GetID() == 993050000:
                if Character.GetPos().x != 1704:
                    Character.Teleport(1704,35)
                    time.sleep(0.3)
                else:
                    if Quest.GetQuestState(16817) == 0 and Terminal.GetProperty("Once",True):
                        Npc.ClearSelection()
                        Npc.RegisterSelection("all")
                        Quest.StartQuest(16817, 9062081)
                        Terminal.SetProperty("Once",False)
                    else:
                        Quest.StartQuest(16827, 9062081)
            else:
                #print("Not done quest")
                if Quest.GetQuestState(16731) != 2:
                    print("1")
                    Quest.StartQuest(16731, 9010010)
                else:
                    Quest.StartQuest(16742, 9010010)
        else:
            Result = Packet.WaitForRecv(0x05F0, 60000)
            if Result.GetRemaining() > 0:
                BytesWanted = []
                ParsePacket(Result)
                Result = Packet.WaitForRecv(0x04C6, 10000)
                if Result.GetRemaining() > 0:
                    Exploit(BytesWanted)
            Terminal.SetProperty("count",Terminal.GetProperty("count",-1)+1)
            #count += 1
            print("Count = ",Terminal.GetProperty("count",-1))
            if Terminal.GetProperty("count",-1) >= 6:
                time.sleep(1)
                LeaveDance()
                time.sleep(0.8)
                Terminal.SetProperty("danceDone",True)
    else:
        if Field.GetID() == 993050000:
            if Character.GetPos().x != 2464:
                Character.Teleport(2464,35)
            else:
                Character.EnterPortal()
                time.sleep(0.3)
            print("Need to leave map")
        else:
            time.sleep(1)
            Terminal.Logout()
            Terminal.SetLineEdit("LoginChar",str(int(Terminal.GetLineEdit("LoginChar"))+1))