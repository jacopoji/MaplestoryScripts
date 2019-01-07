import Quest
import time
import GameState

inner1 = Quest.GetQuestState(12394)
inner2 = Quest.GetQuestState(12395)
inner3 = Quest.GetQuestState(12396)
if GameState.IsInGame():
    time.sleep(2)
    if inner1 !=2:
        Quest.StartQuest(12394, 9010000)
    elif inner2 !=2:
        Quest.StartQuest(12395, 9010000)
    elif inner3 !=2:
        Quest.StartQuest(12396, 9010000)