import GameState, Inventory, time
#Author: Comicals
#GMS v194.4

potReveal       = True
potStamp        = True

#For pot stamp
stampEverything = False
upToSlot        = 9

#Headers
revealHeader    = 0x013E
stampHeader     = 0x0132
########################################

def Reveal():
    for item in Inventory.GetItems(1):
        if item.grade > 0 and item.option1 == 0 and GameState.IsInGame():
            oPacket = Packet.COutPacket(revealHeader)
            oPacket.Encode4(int(time.monotonic()*1000)) #time
            oPacket.Encode2(0x007F)
            oPacket.Encode2(item.pos)
            Packet.SendPacket(oPacket)
            time.sleep(1)
           
def Stamp(upToSlot):
    silverStamp = 2049501
    if stampEverything:
        upToSlot = Inventory.GetItemSlotCount(1)

   
    currentSlot = 0
    for item in Inventory.GetItems(1):
        stamp = Inventory.FindItemByID(silverStamp)
   
        currentSlot+=1
        if currentSlot > upToSlot:
            break
        while item.grade > 0 and item.option1 > 0  and item.option3==0 \
        and stamp.valid and GameState.IsInGame():
            item    = Inventory.GetItem(1, item.pos)
            stamp   = Inventory.FindItemByID(silverStamp)
            if stamp.valid:
                oPacket = Packet.COutPacket(stampHeader)
                oPacket.Encode4(int(time.monotonic()*1000)) #time
                oPacket.Encode2(stamp.pos)
                oPacket.Encode2(item.pos)
                Packet.SendPacket(oPacket)
                time.sleep(1)
           
if potReveal:
    Reveal()
if potStamp:
    Stamp(upToSlot)