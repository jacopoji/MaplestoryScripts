import Packet, Inventory, time, Terminal, GameState, random

randumb = random.randint(0, 3050) * 1000


#Change this number for the amount of nodes you want to use that are dropped from monsters (transferable within account)
AmountDropped = 200
#Change this number for the amount of nodes you want to use that are crafted (tradable)
AmountCrafted = 0

if GameState.IsInGame:
    Packet.BlockRecvHeader(0x006C)
    Packet.BlockRecvHeader(0x0332)
    Packet.BlockRecvHeader(0x0196)
    if Inventory.GetItemCount(2436324) >= AmountDropped:
        for i in range(AmountDropped):
            useNode = Packet.COutPacket(0x0111)
            useNode.Encode4(random.randint(162366415, 171995320))
            useNode.Encode2(Inventory.FindItemByID(2436324).pos)
            useNode.EncodeBuffer("00252CE4 00000001")
            Packet.SendPacket(useNode)
            time.sleep(0.05)
    if Inventory.GetItemCount(2435719) >= AmountCrafted:
        for i in range(AmountCrafted):
            useNode2 = Packet.COutPacket(0x0111)
            useNode2.Encode4(random.randint(162366415, 171995320))
            useNode2.Encode2(Inventory.FindItemByID(2435719).pos)
            useNode2.EncodeBuffer("00252A87 00000001")
            Packet.SendPacket(useNode2)
            time.sleep(0.05)
    time.sleep(15)
    Packet.UnBlockRecvHeader(0x006C)
    Packet.UnBlockRecvHeader(0x0332)
    Packet.UnBlockRecvHeader(0x0196)