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
    map = Field.GetID()
    jobid = Character.GetJob()
    level = Character.GetLevel()
    if jobid == -1 or level == -1:
      #not in game
      continue
    if Terminal.IsRushing():
      continue
    if map == 100000000 or map == 867115950:
      break
    if map == 867117158:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x00BA) 
      oPacket.EncodeBuffer("07 ** ** ** **")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x00BA) 
      oPacket.EncodeBuffer("09 ** ** ** **")
      Packet.SendPacket(oPacket)
      time.sleep(7)
      Terminal.SetCheckBox("Full God Mode", True)
      time.sleep(0.5)
      Terminal.SetCheckBox("Auto NPC", True)
      time.sleep(0.5)
      Terminal.SetCheckBox("Portal Teleport [Back Space]", True)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x052C) 
      oPacket.EncodeBuffer("00000000")
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) 
      oPacket.EncodeBuffer("""01 "ATB4_in" FF80 013A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) 
      oPacket.EncodeBuffer("""01 "ATB4_in" FF80 013A""")
      Packet.SendPacket(oPacket)
      time.sleep(4)
    if map >= 867116100 and map <= 867116109:#B4
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4c_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4c_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4c_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4c_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4c_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4c_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4c_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4c_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4c_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4C_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4C_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4C_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4c_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4c_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4c_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4c_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4c_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4c_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4c_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4c_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4c_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4c_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4c_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4c_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4c_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4c_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4c_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4c_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4c_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4c_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""02 "ATB4_out" C433 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map == 867117150:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) 
      oPacket.EncodeBuffer("""03 "InnerStairs_out" 00FC FF4A""")
      Packet.SendPacket(oPacket)
    if map >= 867116250 and map <= 867116259:#B3
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3c_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3c_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3c_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3c_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3c_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3c_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3c_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3c_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3c_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3c_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3c_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3c_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3C_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3C_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3C_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3c_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3c_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3c_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3c_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3c_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3c_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3c_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3c_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3c_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3c_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3c_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3c_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3c_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3c_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3c_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3c_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3c_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3c_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""04 "ATB3_out" 20E8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map == 867117151:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) 
      oPacket.EncodeBuffer("""05 "OuterStairs_out" FEA2 FF5F""")
      Packet.SendPacket(oPacket)
    if map >= 867116400 and map <= 867116409:#B2
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2c_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2c_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2c_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2c_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2c_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2c_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2c_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2c_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2c_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2B_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2B_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2B_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2c_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2c_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2c_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2c_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2c_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2c_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2c_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2c_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2c_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""06 "ATB2_out" F3DA 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map == 867117152:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) 
      oPacket.EncodeBuffer("""07 "InnerStairs_out" 00F1 FF3C""")
      Packet.SendPacket(oPacket)
    if map >= 867116550 and map <= 867116559:#B1
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1c_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1c_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1c_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1c_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1c_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1c_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1c_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1c_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1c_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1c_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1c_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1c_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1c_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1c_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1c_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1c_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1c_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1c_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1c_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1c_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1c_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1c_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1c_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1c_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1c_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1c_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1c_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1C_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1C_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1C_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1c_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1c_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1c_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #13
      oPacket.EncodeBuffer("""08 "ATB1_out" F3D7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map == 867117153:
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) 
      oPacket.EncodeBuffer("""09 "InnerStairs_out" 00F1 FF4F""")
      Packet.SendPacket(oPacket)
    if map >= 867116600 and map <= 867116609:#1F
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""0A "ATF1_out" 0B48 FEE2""")
      Packet.SendPacket(oPacket)
    if map == 867117159:
      time.sleep(1)
      Character.TalkToNpc(9400456)
    if map >= 867116000 and map <= 867116009:#B4 JQ2
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4a_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4a_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4a_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4a_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4a_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4a_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4a_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4a_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4a_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4A_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4A_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4A_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4a_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4a_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4a_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4a_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4a_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4a_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4a_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4a_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4a_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4a_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4a_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4a_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4a_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4a_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4a_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4a_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4a_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4a_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""02 "ATB4_out" C433 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map >= 867116200 and map <= 867116209:#B3 JQ2
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3b_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3b_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3b_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3b_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3b_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3b_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3b_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3b_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3b_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3b_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3b_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3b_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3B_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3B_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3B_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3b_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3b_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3b_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3b_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3b_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3b_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3b_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3b_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3b_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3b_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3b_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3b_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3b_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3b_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3b_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3b_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3b_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3b_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""04 "ATB3_out" 20E8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map >= 867116300 and map <= 867116309:#B2 JQ2
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2a_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2a_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2a_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2a_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2a_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2a_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2a_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2a_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2a_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2A_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2A_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2A_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2a_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2a_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2a_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2a_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2a_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2a_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2a_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2a_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2a_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""06 "ATB2_out" F3DA 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map >= 867116500 and map <= 867116509:#B1 JQ2
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1b_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1b_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1b_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1b_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1b_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1b_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1b_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1b_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1b_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1b_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1b_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1b_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1b_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1b_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1b_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1b_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1b_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1b_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1b_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1b_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1b_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1b_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1b_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1b_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1b_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1b_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1b_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1B_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1B_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1B_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1b_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1b_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1b_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #13
      oPacket.EncodeBuffer("""08 "ATB1_out" F3D7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map >= 867116050 and map <= 867116059:#B4 JQ3
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4b_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4b_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""02 "b4b_00" FB87 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4b_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4b_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""02 "b4b_01" F6E1 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4b_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4b_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""0149 02 "b4b_02" EA4E 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4B_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4B_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""02 "ckpoint_B4B_0" E6DB 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4b_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4b_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""02 "b4b_03" E599 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4b_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4b_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""02 "b4b_04" DCD0 00E0""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4b_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4b_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""02 "b4b_06" D368 FF15""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4b_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4b_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""02 "b4b_07" CC46 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4b_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4b_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""02 "b4b_08" CA14 007E""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4b_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4b_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""02 "b4b_09" C73B 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""02 "ATB4_out" C433 0068""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map >= 867116150 and map <= 867116159:#B3 JQ3
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3a_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3a_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""04 "b3a_00" F4A1 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3a_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3a_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""04 "b3a_01" F778 FD70""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3a_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3a_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""04 "b3a_02_d_00" FA09 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3a_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3a_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""04 "b3a_03" FCB7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3A_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3A_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""04 "ckpoint_B3A_0" 075D 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3a_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3a_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""04 "b3a_04" 080E 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3a_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3a_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""04 "b3a_05" 0B55 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3a_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3a_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""04 "b3a_07" 13B4 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3a_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3a_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""04 "b3a_08" 16D9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3a_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3a_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""04 "b3a_09" 1AB3 FFCD""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3a_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3a_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""04 "b3a_10" 1CA7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""04 "ATB3_out" 20E8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map >= 867116350 and map <= 867116359:#B2 JQ3
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2b_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2b_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""06 "b2b_00" 1FD2 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2b_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2b_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""06 "b2b_01" 1D95 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2b_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2b_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""06 "b2b_02" 18D3 003C""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2B_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2B_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""06 "ckpoint_B2B_0" 0C0A 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2b_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2b_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""06 "b2b_04" 0B83 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2b_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2b_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""06 "b2b_05" FFAF 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2b_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2b_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""06 "b2b_06" F7B8 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(1)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""06 "ATB2_out" F3DA 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)
    if map >= 867116450 and map <= 867116459:#B1 JQ3
      time.sleep(2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1a_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1a_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #1
      oPacket.EncodeBuffer("""08 "b1a_00" F496 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1a_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1a_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #2
      oPacket.EncodeBuffer("""08 "b1a_01_00" F6F9 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1a_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1a_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #3
      oPacket.EncodeBuffer("""08 "b1a_02_00" F8AF 0010""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1a_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1a_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #4
      oPacket.EncodeBuffer("""08 "b1a_03_00" FA8A 0039""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1a_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1a_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #5
      oPacket.EncodeBuffer("""08 "b1a_04_00" FE03 FFFC""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1a_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1a_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #6
      oPacket.EncodeBuffer("""08 "b1a_05_00" FFA3 0025""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1a_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1a_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #7
      oPacket.EncodeBuffer("""08 "b1a_06_00" 01E9 0030""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1a_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1a_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #8
      oPacket.EncodeBuffer("""08 "b1a_08_00" 1AA6 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1a_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1a_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #9
      oPacket.EncodeBuffer("""08 "b1a_09_00" 2190 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1A_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1A_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #10
      oPacket.EncodeBuffer("""08 "ckpoint_B1A_0" 3066 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.2)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #11
      oPacket.EncodeBuffer("""08 "ATB1_half" 31A0 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1a_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1a_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #12
      oPacket.EncodeBuffer("""08 "elev_s_b1a_03" 2C38 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(0.5)
      oPacket = Packet.COutPacket(0x0149) #13
      oPacket.EncodeBuffer("""08 "ATB1_out" F3D7 004A""")
      Packet.SendPacket(oPacket)
      time.sleep(3)