import Quest
import time
import GameState
import Terminal

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "/SunCat")

try:
	import SunCat, SCLib, SCHotkey
except:
	print("Couldn't find SunCat module")

SCLib.StartVars()
###persist variables
if SCLib.GetVar("QuestDone") is None:
    SCLib.PersistVar("QuestDone", False)

preq = Quest.GetQuestState(55610)
quest = Quest.GetQuestState(52743)
#CompleteQuest(55612, 9330600) 
#CompleteQuest(52743, 9201269)
#CompleteQuest(52743, 9330277)
quest_number = 52743
quest_npc = 9201269
quest_npc2 = 9330277
grove_of_the_spirit_tree = 450005000
#print(SCLib.GetVar("QuestDone"))
if GameState.IsInGame() and SCLib.GetVar("QuestDone") == False:
    if SCLib.GetVar("QuestDone") == False:
        Quest.StartQuest(quest_number, quest_npc)
        Terminal.SetCheckBox("Rush By Level",True)

    if quest == 1:
        if Quest.CheckCompleteDemand(quest_number, quest_npc) == 0:
            Quest.CompleteQuest(quest_number, quest_npc2)
            Terminal.SetCheckBox("Rush By Level",False)
            Terminal.Rush(grove_of_the_spirit_tree)
            SCLib.UpdateVar("QuestDone",True)

        if Quest.CheckCompleteDemand(quest_number, quest_npc2) == 0:
            Quest.CompleteQuest(quest_number, quest_npc2)
            Terminal.SetCheckBox("Rush By Level",False)
            Terminal.Rush(grove_of_the_spirit_tree)
            SCLib.UpdateVar("QuestDone",True)
    else:
        time.sleep(1)

