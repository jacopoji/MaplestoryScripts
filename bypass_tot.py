import time, Quest, GameState, Packet

header =  0x0166

if GameState.IsInGame() and Quest.GetQuestState(1460) != 2:
   Tariq = Packet.COutPacket(header)
   Tariq.EncodeBuffer("01  000005B4 0020A761 0000 0000 0000 0000 0000")
   Packet.SendPacket(Tariq)
   time.sleep(3)
   bass711 = Packet.COutPacket(header)
   bass711.EncodeBuffer("02  000005B4 0020A761 0000 0000 0000 0000 0000")
   Packet.SendPacket(bass711)

if Quest.GetQuestState(1460) == 2:
   print("Complete")
else:
   print("Incomplete")