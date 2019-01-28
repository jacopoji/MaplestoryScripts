import Character
import Context
import DataType
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time
import Packet

Terminal.SetRushByLevel(False)

while True:
    time.sleep(1)
    jobid = Character.GetJob()
    level = Character.GetLevel()
    if jobid == -1 or level == -1:
        continue

    if Terminal.IsRushing():
        continue

    fieldid = Field.GetID()
    quest1 = Quest.GetQuestState(1466)
    quest2 = Quest.GetQuestState(34100)
    quest3 = Quest.GetQuestState(34101)
    quest4 = Quest.GetQuestState(34102)
    quest5 = Quest.GetQuestState(34103)
    quest6 = Quest.GetQuestState(34104)
    quest7 = Quest.GetQuestState(34105)
    quest8 = Quest.GetQuestState(34106)
    quest9 = Quest.GetQuestState(34107)
    quest10 = Quest.GetQuestState(34108)
    quest11 = Quest.GetQuestState(34109)
    quest12 = Quest.GetQuestState(34110)
    quest13 = Quest.GetQuestState(34111)
    quest14 = Quest.GetQuestState(34112)
    quest15 = Quest.GetQuestState(34113)
    quest16 = Quest.GetQuestState(34114)
    quest17 = Quest.GetQuestState(34115)
    quest18 = Quest.GetQuestState(34116)
    quest19 = Quest.GetQuestState(34117)
    quest20 = Quest.GetQuestState(34118)
    quest21 = Quest.GetQuestState(34119)
    quest22 = Quest.GetQuestState(34120)
    # Fakesymbol, enter at correct place and replace FAKESYMBOLID with item ID
    fakesymbol = Inventory.FindItemByID(1712000)  # enter ID
    if fakesymbol.valid:
        Inventory.SendChangeSlotPositionRequest(1, fakesymbol.pos, -1600, -1)
    # RealSymbol, enter at correct place and replace REALSYMBOLID with item ID
    realsymbol = Inventory.FindItemByID(1712001)  # enter ID
    if realsymbol.valid:
        Inventory.SendChangeSlotPositionRequest(1, realsymbol.pos, -1600, -1)
    if fieldid == 450001000:
        time.sleep(1)
        if Character.GetPos().x != -338:
            Character.Teleport(-338, -3)
    if fieldid == 450001340:
        time.sleep(1)
        if Character.GetPos().x != 563:
            Character.Teleport(563, 177)
    if fieldid == 450001350:
        time.sleep(1)
        if Character.GetPos().x != 1200:
            Character.Teleport(1200, 177)
    if quest1 != 2:
        if quest1 == 0:
            if fieldid != 270010111:
                Terminal.Rush(270010111)
            else:
                Quest.StartQuest(1466, 2140001)
        elif quest1 == 1:
            if Quest.CheckCompleteDemand(1466, 2140001) == 0:
                if fieldid != 270010111:
                    Terminal.Rush(270010111)
                else:
                    Quest.CompleteQuest(1466, 2140001)
                    time.sleep(3)
                    oPacket = Packet.COutPacket(0x00F4)
                    oPacket.Encode4(0x291000E6)
                    oPacket.Encode1(0x01)
                    oPacket.Encode2(0x0001)
                    oPacket.Encode2(0xF9C0)
                    oPacket.Encode2(0xFFFF)
                    Packet.SendPacket(oPacket)
                    time.sleep(3)

            else:
                if fieldid != 450001010:
                    Terminal.Rush(450001010)
                else:
                    continue
    elif quest2 != 2:
        if fieldid != 450001000:
            Terminal.Rush(450001000)
        else:
            if quest2 == 0:
                Quest.StartQuest(34100, 3003131)
            elif quest2 == 1:
                Quest.CompleteQuest(34100, 3003131)
    elif quest3 != 2:
        if fieldid != 450001000:
            Terminal.Rush(450001000)
        else:
            if quest3 == 0:
                Quest.StartQuest(34101, 3003131)
            elif quest3 == 1:
                Quest.CompleteQuest(34101, 3003111)
    elif quest4 != 2:
        if quest4 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34102, 3003111)
        elif quest4 == 1:
            if Quest.CheckCompleteDemand(34102, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34102, 3003111)

            else:
                if fieldid != 450001010:
                    Terminal.Rush(450001010)
                else:
                    continue
    elif quest5 != 2:
        if quest5 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34103, 3003111)
        elif quest5 == 1:
            if Quest.CheckCompleteDemand(34103, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34103, 3003111)
            else:
                if fieldid != 450001012:
                    Terminal.Rush(450001012)
                else:
                    continue
    elif quest6 != 2:
        if quest6 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34104, 3003111)
        elif quest6 == 1:
            if Quest.CheckCompleteDemand(34104, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34104, 3003111)
            else:
                if fieldid != 450001014:
                    Terminal.Rush(450001014)
                else:
                    continue
    elif quest7 != 2:
        if quest7 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34105, 3003111)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(34105, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34105, 3003111)
            else:
                if fieldid != 450001016:
                    Terminal.Rush(450001016)
                else:
                    continue
    elif quest8 != 2:
        if fieldid != 450001000:
            Terminal.Rush(450001000)
        else:
            if quest8 == 0:
                Quest.StartQuest(34106, 3003111)
            elif quest8 == 1:
                Quest.CompleteQuest(34106, 3003131)
    elif quest9 != 2:
        if fieldid != 450001005:
            Terminal.Rush(450001005)
        else:
            Quest.StartQuest(34107, 3003110)
    elif quest10 != 2:
        if fieldid != 450001105:
            Terminal.Rush(450001105)
        else:
            Quest.StartQuest(34108, 3003133)
    elif quest11 != 2:
        if fieldid != 450001100:
            Terminal.Rush(450001100)
        else:
            Quest.StartQuest(34109, 3003125)
    elif quest12 != 2:
        if fieldid != 450001100:
            Terminal.Rush(450001100)
        else:
            if quest12 == 0:
                Quest.StartQuest(34110, 3003134)
            elif quest12 == 1:
                Quest.CompleteQuest(34110, 3003125)
    elif quest13 != 2:
        if quest13 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34111, 3003125)
        elif quest13 == 1:
            if Quest.CheckCompleteDemand(34111, 3003125) == 0:
                if fieldid != 450001100:
                    Terminal.Rush(450001100)
                else:
                    Quest.CompleteQuest(34111, 3003125)
            else:
                if fieldid != 450001110:
                    Terminal.Rush(450001110)
                else:
                    continue
    elif quest14 != 2:
        if quest14 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34112, 3003125)
        elif quest14 == 1:
            if Quest.CheckCompleteDemand(34112, 3003125) == 0:
                if fieldid != 450001100:
                    Terminal.Rush(450001100)
                else:
                    Quest.CompleteQuest(34112, 3003125)
            else:
                if fieldid != 450001112:
                    Terminal.Rush(450001112)
                else:
                    continue
    elif quest15 != 2:
        if quest15 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34113, 00000000)
        elif quest15 == 1:
            if Quest.CheckCompleteDemand(34113, 0000000) == 0:
                if fieldid != 450001100:
                    Terminal.Rush(450001100)
                else:
                    Quest.CompleteQuest(34113, 0000000)
            else:
                if fieldid != 450001114:
                    Terminal.Rush(450001114)
                else:
                    continue
    elif quest16 != 2:
        if quest16 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34114, 3003135)
        elif quest16 == 1:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.CompleteQuest(34114, 3003126)
        else:
            continue
    elif quest17 != 2:
        if quest17 == 0:
            Quest.StartQuest(34115, 3003127)
            time.sleep(10)
        elif quest == 1:
            time.sleep(5)
        else:
            continue
    elif quest18 != 2:
        if quest18 == 0:
            if fieldid != 450001210:
                Terminal.Rush(450001210)
            else:
                Quest.StartQuest(34116, 3003128)
        elif quest18 == 1:
            if Quest.CheckCompleteDemand(34116, 3003114) == 0:
                if fieldid == 450001210:
                    Character.Teleport(1125, -29)
                    time.sleep(1)
                    Quest.CompleteQuest(34116, 3003114)
                elif fieldid != 450001210:
                    Terminal.Rush(450001210)
                else:
                    Quest.CompleteQuest(34116, 3003114)
            else:
                if fieldid != 450001210:
                    Terminal.Rush(450001210)
                else:
                    continue

    elif quest19 != 2:
        if quest19 == 0:
            if fieldid != 450001215:
                Terminal.Rush(450001215)
            else:
                Quest.StartQuest(34117, 3003129)
        elif quest19 == 1:
            if Quest.CheckCompleteDemand(34117, 3003115) == 0:
                if fieldid == 450001215:
                    Character.Teleport(1460, -35)
                    time.sleep(1)
                    Quest.CompleteQuest(34117, 3003115)
                elif fieldid != 450001215:
                    Terminal.Rush(450001215)
            else:
                if fieldid != 450001215:
                    Terminal.Rush(450001215)
                else:
                    continue

    elif quest20 != 2:
        if quest20 == 0:
            if fieldid != 450001218:
                Terminal.Rush(450001218)
            else:
                Quest.StartQuest(34118, 3003130)
        elif quest20 == 1:
            if Quest.CheckCompleteDemand(34118, 3003116) == 0:
                if fieldid == 450001218:
                    Character.Teleport(1441, 177)
                    time.sleep(1)
                    Quest.CompleteQuest(34118, 3003116)
                elif fieldid != 450001218:
                    Terminal.Rush(450001218)
            else:
                if fieldid != 450001218:
                    Terminal.Rush(450001218)
                else:
                    continue
    elif quest21 != 2:
        if quest21 == 0:
            Terminal.Rush(450001219)
            time.sleep(5)
            if fieldid == 450001219:
                time.sleep(5)
                Terminal.Rush(450001340)
        if quest21 == 1:
            if Quest.CheckCompleteDemand(34119, 3003140) == 0:
                if fieldid != 450001219:
                    Terminal.Rush(450001219)
                    Quest.CompleteQuest(34119, 3003140)
                else:
                    Quest.CompleteQuest(34119, 3003140)
            else:
                continue
    elif quest22 != 2:
        if quest22 == 0:
            Terminal.Rush(450001250)
            Quest.StartQuest(34120, 3003143)
            time.sleep(10)
            oPacket = Packet.COutPacket(0x00F4)
            oPacket.Encode4(0x2951FDBD)
            oPacket.Encode1(0x01)
            oPacket.Encode2(0x0001)
            oPacket.Encode2(0xF9C0)
            oPacket.Encode2(0xFFFF)
            time.sleep(5)
        else:
            continue
    elif fieldid != 450001000:
        Terminal.Rush(450001000)
        time.sleep(2)
        Terminal.SetRushByLevel(True)
        break
