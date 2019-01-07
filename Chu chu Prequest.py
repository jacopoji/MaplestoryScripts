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
import GameState


Terminal.SetRushByLevel(False)
print("Starting preq")
if GameState.IsInGame():
    time.sleep(1)
    jobid = Character.GetJob()
    level = Character.GetLevel()
    if Terminal.IsRushing():
        time.sleep(3)

    fieldid = Field.GetID()
    quest1 = Quest.GetQuestState(34200)
    quest2 = Quest.GetQuestState(34201)
    quest3 = Quest.GetQuestState(34202)
    quest4 = Quest.GetQuestState(34203)
    quest5 = Quest.GetQuestState(34204)
    quest6 = Quest.GetQuestState(34205)
    quest7 = Quest.GetQuestState(34206)
    quest8 = Quest.GetQuestState(34207)
    quest9 = Quest.GetQuestState(34208)
    quest10 = Quest.GetQuestState(34209)
    quest11 = Quest.GetQuestState(34210)
    quest12 = Quest.GetQuestState(34211)
    quest13 = Quest.GetQuestState(34212)
    quest14 = Quest.GetQuestState(34213)
    quest15 = Quest.GetQuestState(34214)
    quest16 = Quest.GetQuestState(34215)
    quest17 = Quest.GetQuestState(34216)
    quest18 = Quest.GetQuestState(34217)
    quest19 = Quest.GetQuestState(34218)

    if fieldid == 450002000:
        Character.Teleport(1084, 138)
        time.sleep(2)

    if fieldid == 450002010:
        Character.Teleport(667, -588)
        time.sleep(3)
        Key.Press(0x26)
        time.sleep(1)



    fakesymbol = Inventory.FindItemByID(1712002)  # enter ID
    if fakesymbol.valid:
        Inventory.SendChangeSlotPositionRequest(1, fakesymbol.pos, -1601, -1)

    if quest8 == 0 and quest7 == 2 and quest9 != 2:
        time.sleep(1)
        Npc.RegisterSelection("Delicious")
        time.sleep(1)
        Npc.RegisterSelection("Beefy")
        time.sleep(1)
        Npc.RegisterSelection("Bite of Heaven")

    if quest1 != 2:
        if quest1 == 0:
            Terminal.Rush(450002000)
            time.sleep(5)
            if fieldid != 450002201:
                Terminal.Rush(450002201)
            elif fieldid == 450002201:
                Quest.StartQuest(34200, 3003156)

    elif quest2 != 2:
        if quest2 == 0:
            if fieldid != 450002000:
                Terminal.Rush(450002000)
            elif fieldid == 450002000:
                Quest.StartQuest(34201, 3003150)

    elif quest3 != 2:
        if quest3 == 0:
            if fieldid != 450002000:
                Terminal.Rush(450002000)
            elif fieldid == 450002000:
                Quest.StartQuest(34202, 3003152)
    elif quest4 != 2:
        if quest4 == 0:
            if fieldid != 450002000:
                Terminal.Rush(450002000)
            elif fieldid == 450002000:
                Quest.StartQuest(34203, 3003152)
        elif quest4 == 1:
            if Quest.CheckCompleteDemand(34203, 3003152) == 0:
                if fieldid != 450002000:
                    Terminal.Rush(450002000)
                else:
                    Quest.CompleteQuest(34203, 3003152)
            else:
                if fieldid != 450002001:
                    Terminal.Rush(450002001)

    elif quest5 != 2:
        if quest5 == 0:
            if fieldid != 450002000:
                Terminal.Rush(450002000)
            elif fieldid == 450002000:
                Quest.StartQuest(34204, 3003152)

    elif quest6 != 2:
        if quest6 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34205, 0000000)
        elif quest6 == 1:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.CompleteQuest(34205, 3003151)

    elif quest7 != 2:
        if quest7 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34206, 3003151)

    elif quest8 != 2:
        if quest8 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34207, 3003151)
        if quest8 == 1:
            if Quest.CheckCompleteDemand(34207, 3003151) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34207, 3003151)
            else:
                if fieldid != 450002002:
                    Terminal.Rush(450002002)
    elif quest9 != 2:
        if quest9 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34208, 3003151)
        if quest9 == 1:
            if Quest.CheckCompleteDemand(34208, 3003151) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34208, 3003151)
            else:
                if fieldid != 450002004:
                    Terminal.Rush(450002004)

    elif quest10 != 2:
        if quest10 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34209, 3003153)
        if quest10 == 1:
            if Quest.CheckCompleteDemand(34209, 3003153) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34209, 3003153)
            else:
                if fieldid != 450002009:
                    Terminal.Rush(450002009)

    elif quest11 != 2:
        if quest11 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34210, 3003153)
        if quest11 == 1:
            if Quest.CheckCompleteDemand(34210, 3003153) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34210, 3003153)
            else:
                if fieldid != 450002007:
                    Terminal.Rush(450002007)

    elif quest12 != 2:
        if quest12 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34211, 3003154)
        if quest12 == 1:
            if Quest.CheckCompleteDemand(34211, 3003154) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34211, 3003154)
            else:
                if fieldid != 450002012:
                    Terminal.Rush(450002012)

    elif quest13 != 2:
        if quest13 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34212, 3003154)
        if quest13 == 1:
            if Quest.CheckCompleteDemand(34212, 3003154) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34212, 3003154)
            else:
                if fieldid != 450002014:
                    Terminal.Rush(450002014)

    elif quest14 != 2:
        if quest14 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34213, 3003155)
        if quest14 == 1:
            if Quest.CheckCompleteDemand(34213, 3003155) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34213, 3003155)
            else:
                if fieldid != 450002017:
                    Terminal.Rush(450002017)


    elif quest15 != 2:
        if quest15 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            elif fieldid == 450002023:
                Quest.StartQuest(34214, 3003155)
        if quest15 == 1:
            if Quest.CheckCompleteDemand(34214, 3003155) == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34214, 3003155)
            else:
                if fieldid != 450002019:
                    Terminal.Rush(450002019)


    elif quest16 != 2:
        print("q16")
        if quest16 == 0:
            if fieldid != 450002023:
                Terminal.Rush(450002023)
            else:
                Quest.StartQuest(34215, 3003151)
        if quest16 == 1:
            if Quest.CheckCompleteDemand(34215, 3003151) == 0:
                if fieldid == 450002251 or fieldid == 450002250 and Quest.CheckCompleteDemand(34215, 3003151) == 0:
                    Character.Teleport(11, 138)
                    time.sleep(1)
                    Key.Press(0x26)
                elif fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.CompleteQuest(34215, 3003151)
            else:
                if fieldid != 450002251:
                    Terminal.Rush(450002010)

    elif quest17 != 2:
        print("q17")
        if quest17 == 0:
            if fieldid != 450002000:
                Terminal.Rush(450002000)
            elif fieldid == 450002000:
                Quest.StartQuest(34216, 3003150)

    elif quest18 != 2:
        print("q18")
        if quest18 == 0:
            if fieldid != 450002021:
                Terminal.Rush(450002021)
            elif fieldid == 450002021:
                Quest.StartQuest(34217, 3003156)

    elif quest19 != 2:
        if quest19 == 0:
            if fieldid != 450002021:
                Terminal.Rush(450002021)
            elif fieldid == 450002021:
                Quest.StartQuest(34218, 3003156)

