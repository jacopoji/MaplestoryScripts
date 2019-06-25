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
import GameState

time.sleep(2)
assert GameState.IsInGame()

field_id = Field.GetID()

def takePortal( portalstr ):
    portal = Field.FindPortal(portalstr)
    if portal.valid:
        Character.Teleport(portal.x, portal.y)
        time.sleep(1)
        Character.EnterPortal()
        time.sleep(1)

while Terminal.IsRushing():
  time.sleep(2)
if field_id == 350140100:
  time.sleep(15) #todo
  Terminal.SetLineEdit('SISkillID', '80001945')
  #Terminal.SetLineEdit('SIDelay', '1000') Let's play guess what the form labels names are !
  #Terminal.SetCheckBox('SkillInject', 1)
  #Terminal.SetCheckBox('GFMA', 1)
 
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
elif field_id == 350140220:
  #Packet.WaitForRecv(0x030B)    #0x0327 is youtube vid
  #oPacket = Packet.COutPacket(0x00D2) #Skip video
  time.sleep(3)
elif field_id == 350140500:
  time.sleep(8)
  takePortal('pt00')
elif field_id >= 350140600 and field_id <= 350140650:
  time.sleep(10)
  Character.Teleport(735,-1697)    #or tele -561 -1222
elif field_id >= 350140700 and field_id <= 350140750:
  time.sleep(1)
  pos = Character.GetPos()
  if pos.y == 91:
    Character.Teleport(-386,-513)
  time.sleep(11)
  takePortal('pt00')
elif field_id >= 350140800 and field_id <= 350140850:
  time.sleep(10)
  takePortal('pt00')
elif field_id >= 350140900 and field_id <= 350141050:
  time.sleep(5)
  Key.Press(0x08)
  time.sleep(1)
  Character.EnterPortal()
elif field_id >= 350141100 and field_id <= 350141150:
  time.sleep(10)
  Character.Teleport(-762,-2784)
  time.sleep(1)
elif field_id >= 350141200 and field_id <= 350141250:
  time.sleep(10)
  Character.Teleport(716,-1050)
  time.sleep(1)
  Character.EnterPortal()
elif field_id >= 350141300 and field_id <= 350141350:
  time.sleep(10)
  Character.Teleport(809,-1150)
  time.sleep(1)
  Character.EnterPortal()
elif field_id >= 350142000 and field_id <= 350142009:
  time.sleep(3)
elif field_id >= 350160000 and field_id <= 350160009:
  takePortal('pt_enterS')
elif field_id >= 350160320 and field_id <= 350160329:#Boss map
  time.sleep(5)
#350144400 credits map
elif field_id == 913050010:
  print("#hashtag give script writers free terminal") #completed
  time.sleep(2)
#Orginal credits to Cotopian, new and ""improved"" by Lapig