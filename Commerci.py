import Character
import Field
import GameState
import Npc
import Quest
import Terminal
import time

Terminal.SetRushByLevel(False)

while True:
    time.sleep(1)
    level = Character.GetLevel()

    if not GameState.IsInGame():
        continue

    if Terminal.IsRushing():
        continue

    if level < 140:
        continue

    fieldID = Field.GetID()

    # Gets statuses on quests required for solo voyages
    quest1 = Quest.GetQuestState(17600)
    quest2 = Quest.GetQuestState(17601)
    quest3 = Quest.GetQuestState(17602)
    quest4 = Quest.GetQuestState(17603)
    quest5 = Quest.GetQuestState(17608)
    quest6 = Quest.GetQuestState(17610)
    quest7 = Quest.GetQuestState(17611)
    quest8 = Quest.GetQuestState(17612)
    quest9 = Quest.GetQuestState(17613)
    quest10 = Quest.GetQuestState(17614)
    quest11 = Quest.GetQuestState(17003)
    quest12 = Quest.GetQuestState(17004)

    # Completing [Commerci Republic] Neinheart's Call
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(17600, 1101002)
        elif quest1 == 1:
            Quest.CompleteQuest(17600, 1101002)

    # Completing [Commerci Republic] In the Name of the Empress
    elif quest2 != 2:
        if quest2 == 0:
            if fieldID != 130000000:
                Terminal.Rush(130000000)
            else:
                Quest.StartQuest(17601, 1101000)
        elif quest2 == 1:
            Quest.CompleteQuest(17601, 1101000)

    # Completing [Commerci Republic] Neinheart's Request
    elif quest3 != 2:
        if quest3 == 0:
            if fieldID != 130000000:
                Terminal.Rush(130000000)
            else:
                Quest.StartQuest(17602, 1101002)
        elif quest3 == 1:
            if fieldID != 104000000:
                Terminal.Rush(104000000)
            else:
                Quest.CompleteQuest(17602, 9390200)

    # Completing [Commerci Republic] Parbell, World's 'Greatest' Explorer
    elif quest4 != 2:
        if quest4 == 0:
            if fieldID != 104000000:
                Terminal.Rush(104000000)
            else:
                Quest.StartQuest(17603, 9390200)

    # Completing [Commerci Republic] After a Pleasant Voyage
    elif quest5 != 2:
        if quest5 == 1:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.CompleteQuest(17608, 9390201)

    # Completing [Commerci Republic] Berry Concerned 1
    elif quest6 != 2:
        if quest6 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17610, 9390201)
                time.sleep(1)
        elif quest6 == 1:
            if Quest.CheckCompleteDemand(17610, 9390201) == 0:
                if fieldID != 865010200:
                    Terminal.Rush(865010200)
                else:
                    Quest.CompleteQuest(17610, 9390201)
            else:
                if fieldID != 865010100:
                    Terminal.Rush(865010100)

    # Completing [Commerci Republic] Berry Concerned 2
    elif quest7 != 2:
        if quest7 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17611, 9390201)
                time.sleep(1)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(17611, 9390201) == 0:
                if fieldID != 865010200:
                    Terminal.Rush(865010200)
                else:
                    Quest.CompleteQuest(17611, 9390201)
            else:
                if fieldID != 865010000:
                    Terminal.Rush(865010000)

    # Completing [Commerci Republic] The Problem with Presumptions
    elif quest8 != 2:
        if quest8 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Npc.RegisterSelection("(There's no better time to tell him the truth.)")
                Quest.StartQuest(17612, 9390201)

    # Completing [Commerci Republic] The Minister's Son
    elif quest9 != 2:
        if quest9 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17613, 9390201)
        elif quest9 == 1:
            if Quest.CheckCompleteDemand(17613, 9390241) == 0:
                if fieldID not in [865010200, 865090001]:
                    Terminal.Rush(865010200)
                else:
                    Quest.CompleteQuest(17613, 9390241)
            else:
                if fieldID not in [865010200, 865090001]:
                    Terminal.Rush(865010200)
                else:
                    if fieldID == 865010200:
                        Character.AMoveX(851)

    # Completing [Commerci Republic] Ciao, Until Next Time
    elif quest10 != 2:
        if quest10 == 0:
            if fieldID != 865010200:
                Terminal.Rush(865010200)
            else:
                Quest.StartQuest(17614, 9390241)
        elif quest10 == 1:
            if fieldID != 865000000:
                Terminal.Rush(865000000)

    # Completing [Commerci] Get Rich Quick
    elif quest11 != 2:
        if quest11 == 0:
            Quest.StartQuest(17003, 9010010)
        elif quest11 == 1:
            if fieldID != 865000001:
                if fieldID != 865000000:
                    Terminal.Rush(865000000)
                else:
                    Character.Teleport(-137, 526)
                    Character.EnterPortal()
            else:
                Quest.CompleteQuest(17003, 9390220)

    # Completing [Commerci] Making a Buck
    elif quest12 != 2:
        if quest12 == 0:
            if fieldID != 865000001:
                if fieldID != 865000000:
                    Terminal.Rush(865000000)
                else:
                    Character.Teleport(-137, 526)
                    Character.EnterPortal()
            else:
                Quest.StartQuest(17004, 9390220)

    # We're done!
    else:
        break
