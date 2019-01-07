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
def TeleQuest(startRush, killingMap, endRush, questState, questID, npcStartID, npcEndID, startX, startY, endX, endY):
    if currentMap != startRush and questState == 0:
        Terminal.Rush(startRush)
        time.sleep(2)

    if questState == 0:
        # accept it
        if startX != 0 and startY != 0:
            Character.Teleport(startX, startY)
            time.sleep(2)

        time.sleep(2)
        Quest.StartQuest(questID, npcStartID)
        time.sleep(2)

    elif Quest.CheckCompleteDemand(questID, npcEndID) == 0:
        if currentMap != endRush:
            Terminal.Rush(endRush)
            time.sleep(2)

        if endX != 0 and endY != 0:
            Character.Teleport(endX, endY)
            time.sleep(2)

        Quest.CompleteQuest(questID, npcEndID)

    else:
        Terminal.Rush(killingMap)
        time.sleep(5)


def NonTeleQuest(startRush, killingMap, endRush, questState, questID, npcStartID, npcEndID):
    if currentMap != startRush and questState == 0:
        Terminal.Rush(startRush)
        time.sleep(2)

    if questState == 0:
        # accept it
        time.sleep(2)
        Quest.StartQuest(questID, npcStartID)
        time.sleep(2)

    elif Quest.CheckCompleteDemand(questID, npcEndID) == 0:
        if currentMap != endRush:
            Terminal.Rush(endRush)
            time.sleep(2)
        Quest.CompleteQuest(questID, npcEndID)

    else:
        # quest is in progress
        Terminal.Rush(killingMap)
        time.sleep(5)
# created by: leroy.jenkins93, Marik
Terminal.SetRushByLevel(False)

while True:
    time.sleep(1)
    currentMap = Field.GetID()
    jobid = Character.GetJob()
    level = Character.GetLevel()

    if jobid == -1 or level == -1:
        # not in game
        continue

    if Terminal.IsRushing():
        time.sleep(1)
        continue
    fieldid = Field.GetID()

    if level >= 220:

        festival = Quest.GetQuestState(34300)
        dreamsAndIllusions = Quest.GetQuestState(34301)
        partyNeverEnds = Quest.GetQuestState(34302)
        maskOfYourOwn = Quest.GetQuestState(34303)
        concentrationProblem = Quest.GetQuestState(34304)
        lucidDreams = Quest.GetQuestState(34305)

        centerStreet = Quest.GetQuestState(34306)
        awakenedOnes = Quest.GetQuestState(34307)
        findingAwakened = Quest.GetQuestState(34308)
        insideDream = Quest.GetQuestState(34309)
        oldMusicBox = Quest.GetQuestState(34310)
        elizabeth1 = Quest.GetQuestState(34311)
        elizabeth2 = Quest.GetQuestState(34312)
        elizabeth3 = Quest.GetQuestState(34313)

        plates1 = Quest.GetQuestState(34314)
        plates2 = Quest.GetQuestState(34315)
        awakenedTown = Quest.GetQuestState(34316)

        lucidNightmare = Quest.GetQuestState(34317)
        secondMusicBox = Quest.GetQuestState(34318)
        toTheBallroom = Quest.GetQuestState(34319)
        dressCode = Quest.GetQuestState(34320)
        masqueradeCitizen = Quest.GetQuestState(34321)
        darkMask = Quest.GetQuestState(34322)
        dreamkeepers = Quest.GetQuestState(34323)
        ballroomAgain = Quest.GetQuestState(34324)
        masqueradeMask = Quest.GetQuestState(34325)
        fallen = Quest.GetQuestState(34326)

        clocktower1 = Quest.GetQuestState(34327)
        clocktower2 = Quest.GetQuestState(34328)
        clocktower3 = Quest.GetQuestState(34329)
        clocktower4 = Quest.GetQuestState(34330)

        lachsymbol = Inventory.FindItemByID(1712003)  # enter ID
        if lachsymbol.valid:
            Inventory.SendChangeSlotPositionRequest(1, lachsymbol.pos, -1602, -1)
            time.sleep(5)

        # First quest. Starts by rushing to lachelein main town
        if festival != 2:
            # if not accepted, rush to the town
            if festival == 0:
                Terminal.Rush(450003000)

            if festival == 1:
                if Quest.CheckCompleteDemand(34300, 3003202) == 0:
                    Quest.CompleteQuest(34300, 3003202)
                    # need to talk to the 3 NPC
                else:
                    # cat mask
                    Character.TalkToNpc(3003225)
                    time.sleep(3)

                    # rabbit mask
                    Character.TalkToNpc(3003226)
                    time.sleep(3)

                    # flutist mask
                    Character.TalkToNpc(3003227)
                    time.sleep(3)
            else:
                continue

        elif dreamsAndIllusions != 2:
            if dreamsAndIllusions == 0:
                Terminal.Rush(450003100)
                time.sleep(1)
                Quest.StartQuest(34301, 3003209)

        elif partyNeverEnds != 2:
            if partyNeverEnds == 0:
                Terminal.Rush(450003100)
                time.sleep(1)
                Quest.StartQuest(34302, 3003209)

            elif Quest.CheckCompleteDemand(34302, 3003209) == 0:
                if partyNeverEnds == 1:
                    if Field.GetID() == 450003100:
                        Quest.CompleteQuest(34302, 3003209)
                    elif fieldid == 450003720:
                        Character.Teleport(-877, 51)
                        time.sleep(2)
                        Key.Press(0x26)
                        time.sleep(1)
                    elif fieldid != 450003100 and fieldid != 450003720:
                        Terminal.Rush(450003100)
            else:
                Character.MoveX(171, 20000)
                continue

        elif maskOfYourOwn != 2:
            NonTeleQuest(450003100, 450003200, 450003100, maskOfYourOwn, 34303, 3003201, 3003209)

        elif concentrationProblem != 2:
            NonTeleQuest(450003100, 450003220, 450003100, concentrationProblem, 34304, 3003209, 3003209)

        elif lucidDreams != 2:
            NonTeleQuest(450003100, 450003100, 450003100, lucidDreams, 34305, 3003201, 3003209)

        elif centerStreet != 2:
            TeleQuest(450003100, 450003100, 450003000, centerStreet, 34306, 3003201, 3003202, 0, 0, 519, 78)

        elif awakenedOnes != 2:
            if awakenedOnes == 0:
                Terminal.Rush(450003000)
                time.sleep(1)
                Quest.StartQuest(34307, 3003202)

            elif Quest.CheckCompleteDemand(34307, 3003202) == 0:
                Quest.CompleteQuest(34307, 3003202)

            else:
                Character.Teleport(1720, 78)
                time.sleep(3)
                Character.TalkToNpc(3003228)
                time.sleep(3)
                Character.TalkToNpc(3003229)
                time.sleep(3)

                Character.Teleport(380, 75)
                time.sleep(2)
                Character.TalkToNpc(3003215)

        elif findingAwakened != 2:
            if findingAwakened == 0:
                Terminal.Rush(450003000)
                time.sleep(1)
                Npc.ClearSelection()
                Npc.RegisterSelection("Shrimp Mask")
                Quest.StartQuest(34308, 3003202)

            else:
                # this quest is auto completed, so just hand it in
                Quest.CompleteQuest(34308, 3003215)

        elif insideDream != 2:
            NonTeleQuest(450003100, 450003100, 450003100, insideDream, 34309, 3003209, 3003214)

        elif oldMusicBox != 2:
            TeleQuest(450003100, 450003330, 450003330, oldMusicBox, 34310, 3003209, 3003203, 0, 0, 2232, 78)

        elif elizabeth1 != 2:
            TeleQuest(450003330, 450003330, 450003330, elizabeth1, 34311, 3003239, 3003235, 0, 0, 1437, 78)

        elif elizabeth2 != 2:
            TeleQuest(450003330, 450003300, 450003330, elizabeth2, 34312, 3003235, 3003235, 0, 0, 1437, 78)

        elif elizabeth3 != 2:
            TeleQuest(450003330, 450003310, 450003330, elizabeth3, 34313, 3003235, 3003239, 0, 0, 1437, 78)

        elif plates1 != 2:
            TeleQuest(450003330, 450003340, 450003330, plates1, 34314, 3003238, 3003238, 1061, 78, 1061, 78)

        elif plates2 != 2:
            TeleQuest(450003330, 450003350, 450003330, plates2, 34315, 3003223, 3003223, 1061, 78, 1061, 78)

        elif awakenedTown != 2:
            # just complete this one, don't accept
            if currentMap == 450003100:
                Quest.CompleteQuest(34316, 3003209)

            else:
                Terminal.Rush(450003100)

        elif lucidNightmare != 2:
            NonTeleQuest(450003100, 450003100, 450003100, lucidNightmare, 34317, 3003209, 3003220)

        elif secondMusicBox != 2:
            NonTeleQuest(450003100, 450003100, 450003100, secondMusicBox, 34318, 3003220, 3003209)

        elif toTheBallroom != 2:
            Npc.ClearSelection()
            Npc.RegisterSelection("I don't know")
            TeleQuest(450003100, 450003430, 450003430, toTheBallroom, 34319, 3003201, 3003205, 0, 0, 249, 78)

        elif dressCode != 2:
            TeleQuest(450003430, 450003400, 450003430, dressCode, 34320, 3003241, 3003241, 249, 78, 249, 78)

        elif masqueradeCitizen != 2:
            TeleQuest(450003430, 450003410, 450003430, masqueradeCitizen, 34321, 3003243, 3003243, 1118, 33, 1118, 33)

        elif darkMask != 2:
            TeleQuest(450003430, 450003440, 450003440, darkMask, 34322, 3003218, 3003211, 1118, 33, -345, -652)

        elif dreamkeepers != 2:
            TeleQuest(450003440, 450003440, 450003440, dreamkeepers, 34323, 3003206, 3003206, -345, -652, -345, -652)

        elif ballroomAgain != 2:
            TeleQuest(450003440, 450003430, 450003430, ballroomAgain, 34324, 3003206, 3003205, -345, -652, 0, 78)

        elif masqueradeMask != 2:
            TeleQuest(450003430, 450003450, 450003430, masqueradeMask, 34325, 3003224, 3003224, 1118, 33, 1118, 33)

        elif fallen != 2:
            TeleQuest(450003100, 450003500, 450003500, fallen, 34326, 3003209, 3003216, 0, 0, 33, -217)

        elif clocktower1 != 2:
            TeleQuest(450003500, 450003500, 450003500, clocktower1, 34327, 3003216, 3003216, 33, -217, 33, -217)

        elif clocktower2 != 2:
            TeleQuest(450003510, 450003510, 450003510, clocktower2, 34328, 3003222, 3003222, 368, -195, 368, -195)

        elif clocktower3 != 2:
            TeleQuest(450003520, 450003520, 450003520, clocktower3, 34329, 3003219, 3003219, 139, -580, 139, -580)

        elif clocktower4 != 2:
            TeleQuest(450003530, 450003530, 450003530, clocktower4, 34330, 3003210, 3003210, 588, -375, 588, -375)

        elif clocktower4 == 2 and fieldid == 450003530: 
            Terminal.Rush(450003000)
            time.sleep(5)
            Terminal.SetRushByLevel(True)
            break


