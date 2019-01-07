import Packet, datetime, GameState

if GameState.IsInGame() and datetime.datetime.utcnow().second % 3 == 0:
    IlliumPacket = Packet.COutPacket(0x02BA)
    IlliumPacket.EncodeBuffer('[62295010]')
    Packet.SendPacket(IlliumPacket)
    Ark = Packet.COutPacket(0x034B)
    Ark.EncodeBuffer("05 00 00 00 02 B6 C4 04")
    Packet.SendPacket(Ark)