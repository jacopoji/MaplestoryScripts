import os, sys, Quest, Inventory, Packet, Login, Character, GameState, Field, Terminal, time, Key, Npc, Party

sendFame = 0x1B0
recvFame = 0x69C


def sendRPSAction():
    oPacket = Packet.COutPacket(sendFame)
    oPacket.EncodeBuffer("64 02")
    Packet.SendPacket(oPacket)   

def sendAcceptRPS(ID):
    oPacket = Packet.COutPacket(sendFame)
    oPacket.Encode1(0x13)
    oPacket.Encode4(ID)
    oPacket.Encode1(0)
    oPacket.Encode1(0)
    Packet.SendPacket(oPacket)   

def closeRPSWindow():
    oPacket = Packet.COutPacket(sendFame)
    oPacket.EncodeBuffer("1C")
    Packet.SendPacket(oPacket)

def getLocal(state):
    if not state:
        for i in Field.GetCharacters():
            if Terminal.IsLocalUser(i.id):
                return i.id
    else:
        for i in Field.GetCharacters():
            if Terminal.IsLocalUser(i.id):
                return 1
        return 0 

if GameState.IsInGame():
    if getLocal(True) == 1:
        while True:
            iPacket = Packet.WaitForRecv(recvFame, 10000)
            if iPacket.GetRemaining() > 0:
                if iPacket.ReadLong(1) == 21:
                    iPacket.ReadLong(1)
                    iPacket.ReadStr()
                    tradeID = iPacket.ReadLong(4)
                    sendAcceptRPS(tradeID)
                    uPacket = Packet.WaitForRecv(recvFame, 10000)
                    if uPacket.GetRemaining() > 0:
                        sendRPSAction()
                        aPacket = Packet.WaitForRecv(recvFame, 10000)
                        if aPacket.GetRemaining() > 0:
                            closeRPSWindow()