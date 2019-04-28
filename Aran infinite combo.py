import Inventory
import Character
import GameState
import time
import Packet
import Field
import Terminal


if GameState.IsInGame() and not Terminal.IsRushing() and Field.GetMobCount() > 0:
    if not Character.HasBuff(1, 21110016):
        oPacket = Packet.COutPacket(0x01DB)
        oPacket.EncodeBuffer("014220ED")
    for x in range(0, 300):
        Packet.SendPacket(oPacket)
        time.sleep(0.005)
    print('Done.')
else:
    time.sleep(5)
    print('Wait...')