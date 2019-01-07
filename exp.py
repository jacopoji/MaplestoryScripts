import Inventory
import Character
import GameState
import time
import Packet
import Field


if GameState.IsInGame() and Field.GetMobCount() > 0:
    oPacket = Packet.COutPacket(0x00DB)
    oPacket.EncodeBuffer(
        "** ** ** ** 3BA33DA7 FF 00 00000001 00 00 020EFCF7 0083E5A8 020EFCF7 01 00000000 00000000 00 00 00 00000000 00000000 00000000 00")
    for x in range(0, 130):
        Packet.SendPacket(oPacket)
        time.sleep(0.005)
    time.sleep(31)
    print('packet')
else:
    time.sleep(10)
    print('else')