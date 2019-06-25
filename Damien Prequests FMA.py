import Character
import DataType
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time

Terminal.SetRushByLevel(False)

while True:
    time.sleep(2)
    field_id = Field.GetID()
    jobid = Character.GetJob()
    level = Character.GetLevel()
    pos = Character.GetPos()
    if jobid == -1 or level == -1:
      #not in game
      continue
    if Terminal.IsRushing():
      continue
#if the script doesn't start right away, then go to any Victoria Island or Ossyria map
    elif field_id >= 100000000 and field_id <= 340000000:
      oPacket = Packet.COutPacket(0x019A)
      oPacket.Encode2(0x0002)
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x022B) 
      oPacket.EncodeBuffer("[010000000100000004000000]")
      Packet.SendPacket(oPacket)
    elif field_id == 350140000:
      oPacket = Packet.COutPacket(0x00D3)
      oPacket.Encode4(int(time.monotonic()*1000))#S/O to Qybah for showing me how to do this
      oPacket.Encode4(0x00532A20)
      oPacket.Encode1(0xFD)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x000F009A)
      oPacket.Encode1(0x00)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x00000000)
      oPacket.Encode2(0x7B30)
      oPacket.Encode1(0x00)
      Packet.SendPacket(oPacket)
      time.sleep(6)
      oPacket = Packet.COutPacket(0x00D3) 
      oPacket.Encode4(int(time.monotonic()*1000))
      oPacket.Encode4(0x00532A20)
      oPacket.Encode1(0xFD)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x000F009B)
      oPacket.Encode1(0x00)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x00000000)
      oPacket.Encode2(0x7B30)
      oPacket.Encode1(0x00)
      Packet.SendPacket(oPacket)
      time.sleep(6)
    elif field_id == 350140100:
      Character.TalkToNpc(1540899)
      Npc.ClearSelection()
      Npc.RegisterSelection("Fight together.")
      time.sleep(2)
      Character.TalkToNpc(1540896)
      Npc.ClearSelection()
      Npc.RegisterSelection("Fight together.")
      time.sleep(2)
      portal = Field.FindPortal("out_350140100")
      Character.Teleport(portal.x, portal.y-10)
      Character.EnterPortal()
      time.sleep(1)
      Character.EnterPortal()
      time.sleep(1)
    elif field_id == 350140152:
      continue
    elif field_id == 350140160:
      continue
    elif field_id == 350140200:
      continue
    elif field_id == 350140220:
      Packet.WaitForRecv(0x031E)
      oPacket = Packet.COutPacket(0x00D3) #Skip video
      oPacket.Encode4(int(time.monotonic()*1000))
      oPacket.Encode4(0x00532A20)
      oPacket.Encode1(0xFD)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x000F009C)
      oPacket.Encode1(0x00)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x00000000)
      oPacket.Encode2(0x7B30)
      oPacket.Encode1(0x00)
      Packet.SendPacket(oPacket)
      time.sleep(3)
      break
    elif field_id == 350140500:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x00BA)
      oPacket.Encode1(0x09)
      oPacket.Encode4(int(time.monotonic()*1000))
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x00BA)
      oPacket.Encode1(0x08)
      oPacket.Encode4(int(time.monotonic()*1000))
      Packet.SendPacket(oPacket)
      time.sleep(6)
      oPacket = Packet.COutPacket(0x0149)#Enter in battleground
      oPacket.Encode1(0x01)
      oPacket.Encode4(0x74700004)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0x021B)
      oPacket.Encode2(0xF931)
      Packet.SendPacket(oPacket)
      time.sleep(7)
    elif field_id >= 350140600 and field_id <= 350140650:
      time.sleep(7)
      pos = Character.GetPos()
    if pos.y == 75:
      Character.Teleport(-394,-669)
      oPacket = Packet.COutPacket(0x01C1)#Mercedes packet
      oPacket.Encode4(0x00000000)
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350140600 and field_id <= 350140650:
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149)#First Portal
      oPacket.Encode1(0x02)
      oPacket.Encode4(0x6F630005)
      oPacket.Encode2(0x306C)
      oPacket.Encode1(0x30)
      oPacket.Encode2(0x02A4)
      oPacket.Encode2(0xFA15)
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x01C1)#Evan packet
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350140700 and field_id <= 350140750:
      time.sleep(1)
      pos = Character.GetPos()
    if pos.y == 91:
      Character.Teleport(-386,-513)
    elif field_id >= 350140700 and field_id <= 350140750:
      time.sleep(10)
      Key.Press(8)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000000)
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
      time.sleep(6)
      oPacket = Packet.COutPacket(0x0149)#Second Portal
      oPacket.Encode1(0x03)
      oPacket.Encode4(0x74700004)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0xFF8F)
      oPacket.Encode2(0xF76B)
      Packet.SendPacket(oPacket)
      time.sleep(3)
    elif field_id >= 350140800 and field_id <= 350140850:
      time.sleep(10)
      pos = Character.GetPos()
    if pos.y == 36:
      Character.Teleport(-616,-923)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000000)
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350140800 and field_id <= 350140850:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149)#Third Portal
      oPacket.Encode1(0x04)
      oPacket.Encode4(0x74700004)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0x009C)
      oPacket.Encode2(0xFA45)
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350140900 and field_id <= 350141050:
      time.sleep(2)
      oPacket = Packet.COutPacket(0x00BA)
      oPacket.Encode1(0x0A)
      oPacket.Encode4(int(time.monotonic()*1000))
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x00BA)
      oPacket.Encode1(0x0B)
      oPacket.Encode4(int(time.monotonic()*1000))
      Packet.SendPacket(oPacket)
      time.sleep(6)
      oPacket = Packet.COutPacket(0x0149)#Enter in battlegound
      oPacket.Encode1(0x01)
      oPacket.Encode4(0x756F0005)
      oPacket.Encode1(0x74)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0x02A4)
      oPacket.Encode2(0xFD9B)
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149)#Just in case
      oPacket.Encode1(0x01)
      oPacket.Encode4(0x74700004)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0x019E)
      oPacket.Encode2(0xFC23)
      Packet.SendPacket(oPacket)
      time.sleep(1)
    elif field_id >= 350141100 and field_id <= 350141150:
      time.sleep(8)
      pos = Character.GetPos()
    if pos.y == -180:
      Character.Teleport(-471,-913)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000000)
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350141100 and field_id <= 350141150:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149)#First Portal
      oPacket.Encode1(0x02)
      oPacket.Encode4(0x74700004)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0xFD0E)
      oPacket.Encode2(0xF46E)
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350141200 and field_id <= 350141250:
      time.sleep(1)
      pos = Character.GetPos()
    if pos.y == 268:
      Character.Teleport(222,-283)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000000)
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350141200 and field_id <= 350141250:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149)#Second Portal
      oPacket.Encode1(0x03)
      oPacket.Encode4(0x74700004)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0x02CB)
      oPacket.Encode2(0xFC72)
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350141300 and field_id <= 350141350:
      time.sleep(1)
      pos = Character.GetPos()
    if pos.y == -342:
      Character.Teleport(-34,-787)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000000)
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350141300 and field_id <= 350141350:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149)#Third Portal
      oPacket.Encode1(0x04)
      oPacket.Encode4(0x74700004)
      oPacket.Encode2(0x3030)
      oPacket.Encode2(0x0329)
      oPacket.Encode2(0xFBDC)
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350142000 and field_id <= 350142009:
      time.sleep(3)
      oPacket = Packet.COutPacket(0x00D3) 
      oPacket.Encode4(int(time.monotonic()*1000))
      oPacket.Encode4(0x00532A20)
      oPacket.Encode1(0xFD)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x000F009D)
      oPacket.Encode1(0x00)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x00000000)
      oPacket.Encode2(0x7B30)
      oPacket.Encode1(0x00)
      Packet.SendPacket(oPacket)
      time.sleep(5)
      Key.Press(8)
      time.sleep(2)
      Character.EnterPortal()
      time.sleep(2)
      Character.EnterPortal()
      time.sleep(10)
    elif field_id >= 350160000 and field_id <= 350160009:
      time.sleep(5)
      Key.Press(8)
      time.sleep(1)
      Character.EnterPortal()
      time.sleep(2)
      Character.EnterPortal()
    elif field_id >= 350160300 and field_id <= 350160309:
      continue
    elif field_id >= 350160320 and field_id <= 350160329:#Boss map
      time.sleep(5)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350160340 and field_id <= 350160349:#Boss map
      continue
    elif field_id >= 350160360 and field_id <= 350160369:#Boss map
      time.sleep(5)
      oPacket = Packet.COutPacket(0x01C1)
      oPacket.Encode4(0x00000007)
      Packet.SendPacket(oPacket)
    elif field_id >= 350143000 and field_id <= 350143009:#Boss defeated
      continue
    elif field_id >= 350144050 and field_id <= 350144059:
      continue
    elif field_id >= 350144100 and field_id <= 350144109:
      continue
    elif field_id >= 350144200 and field_id <= 350144209:
      time.sleep(3)
      oPacket = Packet.COutPacket(0x00D3)#Skips boring cutscene
      oPacket.Encode4(int(time.monotonic()*1000))
      oPacket.Encode4(0x00532A20)
      oPacket.Encode1(0xFD)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x000F009E)
      oPacket.Encode1(0x00)
      oPacket.Encode1(0x00)
      oPacket.Encode4(0x00000000)
      oPacket.Encode2(0x7B30)
      oPacket.Encode1(0x00)
      Packet.SendPacket(oPacket)
      time.sleep(3)
    elif field_id == 913050010:
      time.sleep(2)
      oPacket = Packet.COutPacket(0x030D) 
      oPacket.Encode4(int(time.monotonic()*1000))
      oPacket.Encode4(0x000001FA)
      Packet.SendPacket(oPacket)
    elif field_id == 807000000:
      break#By Cotopian