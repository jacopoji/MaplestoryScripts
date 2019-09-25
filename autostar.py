import Character
import Context
import DataType
import Inventory
import Packet
import time
import GameState

# leroy.jenkins93
# credit to @mahorori for star catching
# last updated: v205
# v205

# change this to the maximum number of stars you want.
# set it to 100 if you want to go to the maximum number of stars
starTo = 17

# change this to true if you want to use safeguard for stars 13-17
safeguard = True

# change this to true if you want to star whatever item is in equip inventory slot 1
fIStar = True

# change this to true if you want to star all items in your inventory
aIStar = False

# change this to true if you want to star all equipped items
eStar = False

# add the item id for items you want to ignore, separated by a comma
# ex: whitelist = [111111, 222222, 333333]
whitelist = []

# sf header and recv
StarForceHeader = 0x013A
StarForceRecv = 0x0154
StarForceOpcode = 0x34
StarCatchingOpcode = 0x35

##############################################################################################
##############################################################################################
##############################################################################################
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
# DO NOT MODIFY ANYTHING BELOW THIS POINT
padding = 20

# CRand32
class CRand32:
   def __init__(self, s1, s2, s3):
       self.m_s1 = s1
       self.m_past_s1 = s1
       self.m_s2 = s2
       self.m_past_s2 = s2
       self.m_s3 = s3
       self.m_past_s3 = s3

   def Random(self):
       self.m_past_s1 = self.m_s1
       self.m_past_s2 = self.m_s2
       self.m_past_s3 = self.m_s3
       self.m_s1 = ((((self.m_s1 >> 6) ^ (self.m_s1 << 12)) & 0x00001FFF) ^ (self.m_s1 >> 19) ^ (self.m_s1 << 12))  & 0xFFFFFFFF
       self.m_s2 = ((((self.m_s2 >> 23) ^ (self.m_s2 << 4)) & 0x0000007F) ^ (self.m_s2 >> 25) ^ (self.m_s2 << 4)) & 0xFFFFFFFF
       self.m_s3 = ((((self.m_s3 << 17) ^ (self.m_s3 >> 8)) & 0x001FFFFF) ^ (self.m_s3 << 17) ^ (self.m_s3 >> 11)) & 0xFFFFFFFF
       return (self.m_s1 ^ self.m_s2 ^ self.m_s3) & 0xFFFFFFFF

def GenSecretCode(seed):
   seed *= 0x45C82BE5
   seed -= 0x2D09A4AB
   seed &= 0xFFFFFFFF
   msrand = CRand32(seed | 0x100000, seed | 0x1000, seed | 0x10)
   return msrand.Random()

def toHex(val, nbits):
   return ((val + (1 << nbits)) % (1 << nbits))

def starItem(pos, currStar, itemMaxStar, userMaxStar, itemid):
   print('{0} {1}'.format("Position: ".ljust(padding), str(pos)))
   slotStartingMeso = Character.GetMeso()
   slotStartingStar = currStar
   currCode = None

   if itemid in whitelist:
       return

   while currStar < userMaxStar and currStar < itemMaxStar and Inventory.GetItem(1, pos).valid:   
       if GameState.IsInGame():
           print("#-----------------------Star-----------------------#")
           print('{0} {1}'.format("Starring From: ".ljust(padding), str(currStar)))
           print('{0} {1}'.format("User Max stars: ".ljust(padding), str(userMaxStar)))
           print('{0} {1}'.format("Item max stars: ".ljust(padding), str(itemMaxStar)))
           print('{0} {1}'.format("Item ID: ".ljust(padding), str(itemid)))
      
           beforeMeso = Character.GetMeso()
      
           cPacket = Packet.COutPacket(StarForceHeader)
           cPacket.Encode1(StarCatchingOpcode)
           Packet.SendPacket(cPacket)

           ciPacket = Packet.WaitForRecv(StarForceRecv, 10000)
           if ciPacket.GetRemaining() != 12 or ciPacket.ReadLong(1) != StarCatchingOpcode:
               print('star catching packet error', flush=True)
               return

           level = ciPacket.ReadLong(1)
           # 0130 01 053ADEC9 FFF5 [01] 678C8108 00000001 FFFFFFFF 01 00
           # 0130 01 058B16B9 FFF5 [01] 54A8F589 00000001 FFFFFFFF 00 00
           # star the item
           oPacket = Packet.COutPacket(StarForceHeader)
           oPacket.Encode1(1)
           oPacket.Encode4(int(time.monotonic()*1000))
           oPacket.Encode2(toHex(pos, 16))
           oPacket.Encode1(1)
           oPacket.Encode4(GenSecretCode(ciPacket.ReadLong(4)))
           oPacket.Encode4(1)
           oPacket.Encode4(0xFFFFFFFF)
           if safeguard and currStar in range(12, 17):
               oPacket.Encode1(1)
               print("SAFEGUARDING")
           else:
               oPacket.Encode1(0)
           oPacket.Encode1(1)
           Packet.SendPacket(oPacket)
    
           # wait for recv
           iPacket = Packet.WaitForRecv(StarForceRecv, 10000)
          
           afterMeso = Character.GetMeso()
           iCosted = beforeMeso - afterMeso
           print('{0} {1:,}'.format("Meso Cost of Star: ".ljust(padding), iCosted))
           print('{0} {1}'.format("iPacket remaining: ".ljust(padding), iPacket.GetRemaining()), flush = True)
      
           # update current star counter
           currStar = Inventory.GetItem(1, pos).currentStar

           # get max star again in case item blew up
           # item blown up means itemMaxStar = 0
           itemMaxStar = Inventory.GetItem(1, pos).maxStar
      
   slotEndingMeso = Character.GetMeso()
   slotEndingStar = currStar
   slotTotalCost = slotStartingMeso - slotEndingMeso
   if (slotStartingMeso - slotEndingMeso) != 0:
       print('{0} {1:,} meso from star {2} to {3}\n'.format("Total Cost: ".ljust(padding), slotTotalCost, str(slotStartingStar), str(slotEndingStar)), flush = True)
    
def main():
   if GameState.IsInGame():
       if aIStar:
           items = Inventory.GetItems(1)
           for item in items:
               starItem(item.pos, item.currentStar, item.maxStar, starTo, item.id)
        
       elif fIStar:
           # star first item in inventory
           item = Inventory.GetItem(1, 1)
           if item.valid:
               starItem(1, item.currentStar, item.maxStar, starTo, item.id)
        
       if eStar:
           for x in range(-100, 0):
               item = Inventory.GetItem(1, x)
               if item.valid:
                   starItem(x, item.currentStar, item.maxStar, starTo, item.id)
      
main()
