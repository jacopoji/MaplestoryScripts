import Packet,Terminal,Character,GameState,time,Field
job = Character.GetJob()
header = 4401
jobs = [3510,3511,3512]
if not Terminal.IsRushing() and job in jobs:
    while GameState.IsInGame() and not Terminal.IsRushing() and Field.GetMobCount()>0:
        time.sleep(0.2)#delay
        oPacket = Packet.COutPacket(0x0144)
        oPacket.Encode4(int(time.monotonic()*1000))
        oPacket.Encode4(0x0217994A)#skill ID
        oPacket.Encode1(0x01)#skill level
        oPacket.EncodeBuffer("00")
        oPacket.Encode4(0x00000000)
        oPacket.Encode1(0x0F)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x00000000)
        oPacket.Encode2(0x0000)
        oPacket.Encode1(0x00)
        Packet.SendPacket(oPacket)