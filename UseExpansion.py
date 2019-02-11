import Inventory,Packet,Character,Terminal

def use_expansion_packet():
    item = Inventory.FindItemByID(2350003)
    if item.valid:
        usePacket = Packet.COutPacket(useExpansionHeader)
        usePacket.EncodeBuffer("[{}00B3DB2300]".format(hex(item.pos).split('x')[1].zfill(2)))
        Packet.SendPacket(usePacket)
use_expansion_packet()
Terminal.ChangeChannel(2)