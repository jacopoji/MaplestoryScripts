import Character
import Field
import GameState
import Quest
import Inventory
import Packet
import Terminal
import time
import Npc
import Key



RushFM = False
#Set either True or False
#Setting RushFM to true will make the script do all of Cannoneer 1st job then leave your char in the fm
#Setting RushFM to False, will make the script do all of cannoneer 1st and 2nd job and then leave in fm xd


TrainingMap = 100040200 #Put a mapID of your choice here, one in range 10-30


CurrentMap = Field.GetID()


def shieee(value):
    if Character.GetLevel() >= 10:
        Terminal.SetSpinBox("autoattack_spin", 350)
    else:
        Terminal.SetSpinBox("autoattack_spin", 100)
    Terminal.SetCheckBox('30 Sec God Mode', value)
    Terminal.SetComboBox("AttackKey", 1)
    Terminal.SetCheckBox('Auto Attack', value)
    Terminal.SetCheckBox('Kami Vac', value)
    Terminal.SetCheckBox('Kami Loot', value)
    Terminal.SetCheckBox('Auto Loot', value)

def Autism():
    time.sleep(1)
    Key.Press(0x11)
    time.sleep(3)
    Key.Press(0x11)
    time.sleep(3)
    Key.Press(0x11)
    time.sleep(3)
    Key.Press(0x11)


Quest1 = Quest.GetQuestState(2573)
Quest2 = Quest.GetQuestState(2561)
Quest3 = Quest.GetQuestState(2560)
Quest4 = Quest.GetQuestState(2562)
Quest5 = Quest.GetQuestState(2563)
Quest6 = Quest.GetQuestState(2564)
Quest7 = Quest.GetQuestState(2565)
Quest8 = Quest.GetQuestState(2566)
Quest9 = Quest.GetQuestState(2567)
Quest10 = Quest.GetQuestState(2574)
Quest11 = Quest.GetQuestState(2568)
Quest12 = Quest.GetQuestState(2569)
Quest13 = Quest.GetQuestState(2570)

JobAdv1 = Quest.GetQuestState(1427)
JobAdv2 = Quest.GetQuestState(1428)
if GameState.IsInGame:
    Terminal.SetCheckBox('No Air Check', True)
    Terminal.SetCheckBox('Auto NPC', True)
    Terminal.SetCheckBox('No Blue Boxes', True)
    if CurrentMap == 3000600 and Quest1 == 0:
        Quest.StartQuest(2573, 1096000)
        time.sleep(60)
    elif Quest2 != 2:
        if CurrentMap == 3000100 and Quest2 != 2:
            if Quest2 == 0:
                Quest.StartQuest(2561, 1096003)
                time.sleep(2)
            elif Quest2 == 1:
                Cat = Inventory.FindItemByID(2010000)
                if Cat.valid:
                    Inventory.UseItem(2010000)
                    time.sleep(2)
                    Quest.CompleteQuest(2561, 1096003)
                else:
                    print('this mean yo dum ass dropped the apple, gonna forfeit quest')
                    oPacket = Packet.COutPacket(0x0166)
                    oPacket.EncodeBuffer("03 01 0A 00 00")
                    Packet.SendPacket(oPacket)
    elif Quest3 != 2:
        if CurrentMap == 3000100 and Quest3 != 2:
            if Quest3 == 0:
                Quest.StartQuest(2560, 1096003)
                time.sleep(2)
            elif Quest3 == 1:
                Quest.CompleteQuest(2560, 1096003)
    elif Quest4 != 2:
        if CurrentMap == 3000100 and Quest4 != 2:
            if Quest4 == 0:
                Npc.RegisterSelection('''Is there someone else there?''')
                Quest.StartQuest(2562, 1096003)
                time.sleep(3)
            elif Quest4 == 1:
                if CurrentMap == 3000100:
                    Character.Teleport(847, 118)
                    time.sleep(1)
                    Key.Press(0x26)
                    time.sleep(1)
                    Character.Teleport(-257, 164)
                    Quest.CompleteQuest(2562, 1096005)
                elif CurrentMap == 3000200:
                    Character.Teleport(-257, 164)
                    Quest.CompleteQuest(2562, 1096005)
    elif Quest5 != 2:
        if CurrentMap == 3000200 and Quest5 != 2:
            if Quest5 == 0:
                Quest.StartQuest(2563, 1096005)
                time.sleep(1)
            elif Quest5 == 1:
                Quest.CompleteQuest(2563, 1096005)
    elif Quest6 != 2:
        if CurrentMap == 3000200 and Quest6 != 1:
            if Quest6 == 0:
                Quest.StartQuest(2564, 1096005)
                time.sleep(1)
        elif Quest6 == 1 and Quest.CheckCompleteDemand(2564, 1096005) != 0:
            if CurrentMap != 3000300:
                Character.Teleport(382, 164)
                time.sleep(1)
                Key.Press(0x26)
            elif CurrentMap == 3000300:
                shieee(True)             
        elif Quest.CheckCompleteDemand(2564, 1096005) == 0:
            shieee(False)
            if CurrentMap == 3000200:
                Quest.CompleteQuest(2564, 1096005)
            elif CurrentMap != 3000200:
                Character.Teleport(-742, 168)
                time.sleep(1)
                Key.Press(0x26)
                time.sleep(1)
    elif Quest7 != 2:
        shieee(False)
        if CurrentMap == 3000200 and Quest7 == 0:
            Quest.StartQuest(2565, 1096005)
        elif Quest7 == 1 and Quest.CheckCompleteDemand(2565, 1096005) != 0:
            if CurrentMap == 3000400:
                Terminal.SetCheckBox('Auto Loot', True)
                Terminal.SetCheckBox('Kami Loot', True)
                Character.Teleport(-1286, 166)
                Autism()
                Character.Teleport(-998, 168)
                Autism()
                Character.Teleport(-785, 168)
                Autism()
            elif CurrentMap != 3000400:
                Character.Teleport(150, -175)
                time.sleep(1)
                Key.Press(0x26)
        elif Quest.CheckCompleteDemand(2565, 1096005) == 0:
            Terminal.SetCheckBox('Auto Loot', False)
            Terminal.SetCheckBox('Kami Loot', False)
            if CurrentMap == 3000200:
                Quest.CompleteQuest(2565, 1096005)
            elif CurrentMap != 3000200:
                Character.Teleport(-1764, 168)
                time.sleep(1)
                Key.Press(0x26)
    elif Quest8 != 2:
        if CurrentMap == 3000200 and Quest8 == 0:
            Quest.StartQuest(2566, 1096005)
        elif Quest8 == 1:
            if CurrentMap == 3000200 and Quest.CheckCompleteDemand(2566, 1096005) != 0:
                Character.Teleport(150, -175)
                time.sleep(1)
                Key.Press(0x26)
                time.sleep(1)
            if CurrentMap == 3000400 and Quest.CheckCompleteDemand(2566, 1096005) != 0:
                Character.Teleport(2308, 121)
                time.sleep(3)
                Key.Press(0x26)
            elif CurrentMap == 3000500 and Quest.CheckCompleteDemand(2566, 1096005) != 0:
                Character.Teleport(-567, 165)
                time.sleep(1)
                Character.TalkToNpc(1096010)
            elif CurrentMap == 3000500 and Quest.CheckCompleteDemand(2566, 1096005) == 0:
                Character.Teleport(-1120, 165)
                time.sleep(1)
                Key.Press(0x26)
            elif CurrentMap == 3000400 and Quest.CheckCompleteDemand(2566, 1096005) == 0:
                Character.Teleport(-1764, 168)
                time.sleep(1.5)
                Key.Press(0x26)
            elif CurrentMap == 3000200 and Quest.CheckCompleteDemand(2566, 1096005) == 0:
                Quest.CompleteQuest(2566, 1096005)
    elif Quest9 != 2:
        if CurrentMap == 3000200 and Quest9 == 0:
            Quest.StartQuest(2567, 1096005)
        elif CurrentMap == 3000400 and Quest9 == 0:
            Character.Teleport(-1764, 168)
            time.sleep(1)
            Key.Press(0x26)
            time.sleep(1)
        elif CurrentMap == 3000200 and Quest9 == 1:
            Character.Teleport(-1377, 164)
            time.sleep(1)
            Key.Press(0x26)
        elif CurrentMap == 3000100 and Quest9 == 1:
            Character.Teleport(-484, 260)
            time.sleep(2)
            Quest.CompleteQuest(2567, 1096003)
    elif Quest10 != 2:
        if CurrentMap == 3000100 and Quest10 == 0:
            Quest.StartQuest(2574, 1096003)
        elif CurrentMap != 3000100 and Quest10 == 0:
            Terminal.Rush(3000100)
        elif CurrentMap == 3000100 and Quest10 == 1:
            Character.Teleport(847, 118)
            time.sleep(1)
            Key.Press(0x26)
        elif CurrentMap == 3000200 and Quest10 == 1:
            Character.Teleport(-274, 164)
            time.sleep(1)
            Quest.CompleteQuest(2574, 1096005)
    elif Quest11 != 2:
        if CurrentMap == 3000200 and Quest11 == 0:
            Quest.StartQuest(2568, 1096005)
        elif CurrentMap == 912060500 and Quest11 == 1:
            Quest.CompleteQuest(2568, 1096006)
    elif Quest12 != 2:
        if CurrentMap == 912060500 and Quest12 == 0:
            Quest.StartQuest(2569, 1096006)
        elif CurrentMap != 912060500 and Quest12 == 0:
            Terminal.Rush(912060500)
        elif CurrentMap == 912060500 and Quest12 == 1:
            Quest.CompleteQuest(2569, 1096004)
    elif Quest13 != 2:
        if CurrentMap == 912060500 and Quest13 == 0:
            Quest.StartQuest(2570, 1096006)
        elif CurrentMap != 912060500 and Quest13 == 0:
            Terminal.Rush(912060500)
        elif Quest13 == 1:
            if CurrentMap != 120000101:
                Character.Teleport(420, 18)
                time.sleep(1)
                Key.Press(0x26)
            elif CurrentMap == 120000101 and Quest.CheckCompleteDemand(2570, 1090000) == 0:
                Quest.CompleteQuest(2570, 1090000)
    elif Quest13 == 2 and RushFM == True:
        if CurrentMap != 910000000:
            if CurrentMap != 100000100:
                Terminal.Rush(100000100)
            elif CurrentMap == 100000100:
                Character.Teleport(838, 154)
                time.sleep(1)
                Key.Press(0x26)
                print('Cannoneer @ FM')
    elif Quest13 == 2 and RushFM == False:
        SkillLevel = Character.GetSkillLevel(5011000)
        if 3 > SkillLevel:
            qPacket = Packet.COutPacket(0x014F)
            qPacket.EncodeBuffer("FF A1 2D 07 38 76 4C 00 01 00 00 00")
            Packet.SendPacket(qPacket)
        else:
            if SkillLevel > 1:
                Cannon = Inventory.FindItemByID(1532000)
                if Cannon.valid:
                    Position = Cannon.pos
                    if Position == 1:
                        sPacket = Packet.COutPacket(0x0106)
                        sPacket.EncodeBuffer("** ** ** 07 01 01 00 F5 FF FF FF")
                        Packet.SendPacket(sPacket)
                    elif Position != 1:
                        Inventory.SendChangeSlotPositionRequest(1, Position, 1, -1)
                else:
                    Key.Set(0x11, 1, 5011000)
                    Key.Set(0x44, 2, 2000006)
                    Terminal.SetSlider("sliderMP", 10)
                    Terminal.SetComboBox("MPKey", 33)
                    Terminal.SetCheckBox("ndmp", True)
                    Terminal.SetSpinBox("autoattack_spin", 100)
                    Terminal.SetComboBox("AttackKey", 1)
                    Terminal.SetCheckBox("Auto Buff", True)
                    Terminal.SetCheckBox("eliteCC", True)
                    Terminal.SetCheckBox("Auto Equip", True)
                    Terminal.SetCheckBox("Auto Rune", True)
                    Terminal.SetCheckBox("Auto SP", True)
                    Terminal.SetCheckBox("30 Sec God Mode", True)
                    Terminal.SetCheckBox("Auto Revive", True)
                    Terminal.SetCheckBox("filter_equip", True)
                    #Terminal.SetCheckBox("filter_use", True)
                    Terminal.SetCheckBox("filter_setup", True)
                    Terminal.SetCheckBox("filter_etc", True)
                    Terminal.SetCheckBox("filter_card", True)
                    Terminal.SetCheckBox("filter_recipe", True)
                    Terminal.SetSpinBox("FilterMeso", 40000)
                    Terminal.SetCheckBox("Auto Mission", True)
                    Terminal.SetCheckBox("Auto AP", True)
                    Terminal.SetPushButton("Item Filter", True)
                    Terminal.SetCheckBox("Mob Disarm", True)
                    Terminal.SetCheckBox("Familiar 0", True)
                    Terminal.SetComboBox("Familiar0", 1)
                    Terminal.SetCheckBox("Auto MP", True)
                    Terminal.SetCheckBox("Unlimited Vitality", True)
                    Terminal.SetCheckBox("Rush By Level", False)
                    if Character.IsOwnFamiliar(9960098):
                        Terminal.SetCheckBox("filter_familiar", True)
                        if CurrentMap == TrainingMap and Character.GetLevel() < 30:
                            shieee(True)
                        elif CurrentMap != TrainingMap and Character.GetLevel() < 30:
                            Terminal.Rush(TrainingMap)
                        elif Character.GetLevel() >= 30 and CurrentMap == TrainingMap:
                            shieee(False)
                            Terminal.Rush(120000101)
                            time.sleep(3)
                        else:
                            if JobAdv1 == 0 and CurrentMap == 120000101:
                                Quest.StartQuest(1427, 1096006)
                                time.sleep(1)
                            elif JobAdv1 == 0 and CurrentMap != 120000101:
                                Terminal.Rush(120000101)
                                time.sleep(5)
                            elif JobAdv1 == 1:
                                Quest.CompleteQuest(1427, 1090000)
                            elif JobAdv2 == 0:
                                Quest.StartQuest(1428, 1090000)
                                time.sleep(5)
                            elif JobAdv2 == 1:
                                if CurrentMap == 912040000 and Quest.CheckCompleteDemand(1428, 1090000) != 0:
                                    Terminal.SetCheckBox("filter_etc", False)
                                    shieee(True)
                                elif CurrentMap == 912040000 and Quest.CheckCompleteDemand(1428, 1090000) == 0:
                                    shieee(False)
                                    Character.Teleport(-290, 150)
                                    Key.Press(0x26)
                                elif CurrentMap == 120000101 and Quest.CheckCompleteDemand(1428, 1090000) == 0:
                                    Quest.CompleteQuest(1428, 1090000)
                                else:
                                    print('you prolly dced in the job adv room, forfeiting')
                                    kPacket = Packet.COutPacket(0x0166)
                                    kPacket.EncodeBuffer("03 94 05 00 00")
                                    Packet.SendPacket(kPacket)
                            else:
                                if CurrentMap != 910000000:
                                    if CurrentMap != 100000100:
                                        Terminal.Rush(100000100)
                                    elif CurrentMap == 100000100:
                                        Character.Teleport(838, 154)
                                        time.sleep(1)
                                        Key.Press(0x26)
                                        print('Cannoneer @ FM')
                    elif not Character.IsOwnFamiliar(9960098):
                        Boogie = Inventory.FindItemByID(2870098)
                        if Boogie.valid:
                            Inventory.UseFamiliarCard(2870098)
                        else:
                            if CurrentMap == 102010000:
                                shieee(True)
                            elif CurrentMap != 102010000:
                                Terminal.Rush(102010000)