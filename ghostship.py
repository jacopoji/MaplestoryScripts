import Quest, Key, GameState, Terminal, time, DataType, Character, Field, Npc, Inventory, Packet
class QuestInfo:
    questStates = [Quest.GetQuestState(4510), Quest.GetQuestState(4511), Quest.GetQuestState(4512), Quest.GetQuestState(4513), Quest.GetQuestState(5560)]

    def KillQuest(questID, startNPC, endNPC, startMap, endMap, KillingMap):
        if Quest.GetQuestState(questID) == 1:
            if Quest.CheckCompleteDemand(questID, startNPC):
                Terminal.Rush(KillingMap)
                Terminal.SetCheckBox("Kami Vac", True)
            else:
                if Field.GetID() != endMap:
                    Terminal.Rush(endMap)
                else:
                    Terminal.SetCheckBox("Kami Vac", False)
                    if Character.GetPos().x != Field.FindNpc(endNPC).x:
                        Character.Teleport(Field.FindNpc(endNPC).x, Field.FindNpc(endNPC).y)
                    else:
                        Quest.CompleteQuest(questID, endNPC)
                        time.sleep(1)
                        Key.Press(0x20)
        elif Quest.GetQuestState(questID) == 0:
            Terminal.SetCheckBox("Kami Vac", False)
            if Field.GetID() != startMap:
                Terminal.Rush(startMap)
            else:
                if Character.GetPos().x != Field.FindNpc(startNPC).x:
                    Character.Teleport(Field.FindNpc(startNPC).x, Field.FindNpc(startNPC).y)
                else:
                    Quest.StartQuest(questID, startNPC)
    def KillQuestSpecial(questID, startNPC, endNPC, startMap, endMap, KillingMap):
        if Quest.GetQuestState(questID) == 1:
            if Quest.CheckCompleteDemand(questID, startNPC):
                Terminal.Rush(KillingMap)
                Terminal.SetCheckBox("Kami Vac", True)
            else:
                if Field.GetID() != endMap:
                    Terminal.Rush(endMap)
                else:
                    Terminal.SetCheckBox("Kami Vac", False)
                    if Character.GetPos().x != Field.FindNpc(endNPC).x:
                        Character.Teleport(Field.FindNpc(endNPC).x, Field.FindNpc(endNPC).y)
                    else:
                        CompletePacket = Packet.COutPacket(0x0155)
                        CompletePacket.EncodeBuffer("02 0000119F 008D730E 00000000 FF1E 0055 00000000")
                        Packet.SendPacket(CompletePacket)
        elif Quest.GetQuestState(questID) == 0:
            Terminal.SetCheckBox("Kami Vac", False)
            if Field.GetID() != startMap:
                Terminal.Rush(startMap)
            else:
                if Character.GetPos().x != Field.FindNpc(startNPC).x:
                    Character.Teleport(Field.FindNpc(startNPC).x, Field.FindNpc(startNPC).y)
                else:
                    Quest.StartQuest(questID, startNPC)

    def DoubleKillQuest(questID, startNPC, endNPC, startMap, endMap, KillingMap1, KillingMap2):
        KillingMaps = [KillingMap1, KillingMap2]
        if Quest.GetQuestState(questID) == 1:
            if Quest.CheckCompleteDemand(questID, startNPC):
                for map in KillingMaps:
                    Terminal.Rush(map)
                    Terminal.SetCheckBox("Kami Vac", True)
                    time.sleep(20)
            else:
                if Field.GetID() != endMap:
                    Terminal.Rush(endMap)
                else:
                    Terminal.SetCheckBox("Kami Vac", False)
                    if Character.GetPos().x != Field.FindNpc(endNPC).x:
                        Character.Teleport(Field.FindNpc(endNPC).x, Field.FindNpc(endNPC).y)
                    else:
                        CompletePacket = Packet.COutPacket(0x0155) #0155 02 0000119E 008D730E 00000000 FF46 00B1 00000000
                        CompletePacket.EncodeBuffer('02 0000119E 008D730E 00000000 FF46 0055 00000000')
                        Packet.SendPacket(CompletePacket)
        elif Quest.GetQuestState(questID) == 0:
            Terminal.SetCheckBox("Kami Vac", False)
            if Field.GetID() != startMap:
                Terminal.Rush(startMap)
            else:
                if Character.GetPos().x != Field.FindNpc(startNPC).x:
                    Character.Teleport(Field.FindNpc(startNPC).x, Field.FindNpc(startNPC).y)
                else:
                    Quest.StartQuest(questID, startNPC)

    def specialQuest():
        if Quest.GetQuestState(5560) == 1 and Quest.GetQuestState(4513) == 1: #started
            if Quest.CheckCompleteDemand(4513, 9270030):
                if Field.GetID() != 541010100:
                    if Field.GetID() == 541010060:
                        Terminal.Rush(541010100)
                    else:
                        Terminal.Rush(541010060)
                else:
                    whiteEssence = Inventory.FindItemByID(4000381)
                    if whiteEssence.valid:
                        if Character.GetPos().x != -145:
                            Terminal.SetCheckBox("Kami Vac", False)
                            Character.Teleport(-145, 225)
                        else:
                            Inventory.SendChangeSlotPositionRequest(4, whiteEssence.pos, 0, 1)
                            time.sleep(1)
                    else:
                        time.sleep(1)

            elif not Quest.CheckCompleteDemand(4513, 9270030):
                if Field.GetID() != 541000000:
                    if Field.GetID() == 541010100:
                        Character.TalkToNpc(9270033)
                    else:
                        Terminal.Rush(541000000)
                else:
                    if Character.GetPos().x != Field.FindNpc(9270030).x:
                        Character.Teleport(Field.FindNpc(9270030).x, Field.FindNpc(9270030).y)
                    else:
                        Quest.CompleteQuest(4513, 9270030)
        else:
            if Quest.GetQuestState(5560) == 0:
                if Field.GetID() != 541000000:
                    Terminal.Rush(541000000)
                    Terminal.SetCheckBox("Kami Vac", False)
                    time.sleep(1)
                else:
                    Quest.StartQuest(5560, 9270030)
            elif Quest.GetQuestState(4513) == 0:
                if Field.GetID() != 541000000:
                    Terminal.Rush(541000000)
                    Terminal.SetCheckBox("Kami Vac", False)
                    time.sleep(1)
                else:
                    Npc.ClearSelection()
                    Npc.RegisterSelection("Why are you still here? I thought that you were going to set sail")
                    Npc.RegisterSelection("What are you hiding from me")
                    Quest.StartQuest(4513, 9270030)

if GameState.IsInGame() and not Terminal.IsRushing():
    if QuestInfo.questStates[0] != 2:
        QuestInfo.DoubleKillQuest(4510, 9270030, 9270030, 541000000, 541000000, 541000200, 541010010)
    elif QuestInfo.questStates[1] != 2:
        QuestInfo.KillQuestSpecial(4511, 9270030, 9270030, 541000000, 541000000, 541010010)
    elif QuestInfo.questStates[2] != 2:
        QuestInfo.KillQuest(4512, 9270030, 9270030, 541000000, 541000000, 541010050)
    elif QuestInfo.questStates[3] != 2:
        QuestInfo.specialQuest()
    elif QuestInfo.questStates[4] != 2:
        if Field.GetID() != 541000000:
            Terminal.Rush(541000000)
        else:
            if Character.GetPos().x != Field.FindNpc(9270030).x:
                Terminal.SetCheckBox("Kami Vac", False)
                Character.Teleport(Field.FindNpc(9270030).x, Field.FindNpc(9270030).y)
            else:
                Quest.CompleteQuest(5560, 9270030)
