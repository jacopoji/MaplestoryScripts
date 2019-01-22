import os, sys, Quest, Inventory, Packet, Login, Character, GameState, Field, Terminal, time, Key, Npc, Party

sendFame = 0x1B0
recvFame = 0x69C

delay = 0 # Raise if you are having any issues.

def openRPSWindow():
    oPacket = Packet.COutPacket(sendFame)
    oPacket.EncodeBuffer("10 03 00")
    Packet.SendPacket(oPacket)

def sendRPSRequest(character):
    oPacket = Packet.COutPacket(sendFame)
    oPacket.Encode1(0x15)
    oPacket.Encode4(character)
    Packet.SendPacket(oPacket)

def sendRPSAction():
    oPacket = Packet.COutPacket(sendFame)
    oPacket.EncodeBuffer("64 00")
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
        openRPSWindow()
        Packet.WaitForRecv(recvFame, 3000)
        sendRPSRequest(getLocal(False))
        iPacket = Packet.WaitForRecv(recvFame, 10000)
        if iPacket.GetRemaining() > 0:
            sendRPSAction()
        time.sleep(delay)
    else:
        print("Defame client not in map.")