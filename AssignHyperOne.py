import GameState, Context, Packet, Terminal, time

skillID = 5121054 #SKILL ID THAT U WANT TO STEAL

def grabSkill():
    oPacket = Packet.COutPacket(0x01F0)
    oPacket.Encode4(int(time.monotonic()*1000))
    oPacket.Encode4(skillID)
    Packet.SendPacket(oPacket)
    time.sleep(1)

def bindSkill():
    oPacket = Packet.COutPacket(0x01BC)
    oPacket.EncodeBuffer("00 00 00 00 01 00 00 00 49 00 00 00 01")
    oPacket.Encode4(skillID)
    Packet.SendPacket(oPacket)
    time.sleep(1)

if GameState.IsInGame():
    grabSkill()
    bindSkill()
    Terminal.ChangeChannel(0)
    time.sleep(10)