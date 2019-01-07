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

# created by: leroy.jenkins93

# https://strategywiki.org/wiki/MapleStory/Quests/Gate_to_the_Future#Lost_Emblem
################################### NOTES ###################################
# The purpose of this script is to let your bots enter stronghold
# automatically when they reach level 165+
# if you want, you can add on more quests so that it finishes the
# empress prequests too, but idk anyone who actually does empress anymore
# so I decided to leave it out.
#
# If a lot of you end up commenting in favor of adding empress, I might
# do it depending on how free I am
#############################################################################

Terminal.SetRushByLevel(False)

while True:
    time.sleep(1)
    currentMap = Field.GetID()
    jobid = Character.GetJob()
    level = Character.GetLevel()

    #-----------------------
    # quest ID and states
    #-----------------------
    exploringFuture = Quest.GetQuestState(31103)
    chiefAlex = Quest.GetQuestState(31104)
    henesysInRuins = Quest.GetQuestState(31105)
    fallOfCygnus = Quest.GetQuestState(31106)

    scoutingStronghold = Quest.GetQuestState(31124)
    piercingDefenses = Quest.GetQuestState(31125)
    lostEmblem = Quest.GetQuestState(31126)

    # after the above quests, you can enter stronghold


    if jobid == -1 or level == -1:
        #not in game
        continue
        
    if Terminal.IsRushing():
        time.sleep(1)
        continue

    if level >= 165:
        # if character is above level 165, rush to future henesys
        # this will automatically accept Exploring the future

        if currentMap == 271010000:
            Character.Teleport(-596, 154)
        
        # if this quest is not completed,
        if exploringFuture != 2:
            if currentMap != 271010000:
                Terminal.Rush(271010000)
                continue
            # if we are in the map, hand in the quest to alex
            Quest.CompleteQuest(31103, 2142001)
            
        elif chiefAlex != 2:
            # if not in map, rush to it
            if currentMap != 271010000:
                Terminal.Rush(271010000)
                continue
                
            if chiefAlex == 0:
                Quest.StartQuest(31104, 2142001)
            
            elif Quest.CheckCompleteDemand(31104, 2142001) == 0:
                # answer his quiz
                Npc.ClearSelection()
                Npc.RegisterSelection("Kerning City")
                Npc.RegisterSelection("You were a runaway")
                Npc.RegisterSelection("Stan")
                Npc.RegisterSelection("An old golden watch")
                Quest.CompleteQuest(31104, 2142001)
                
        elif henesysInRuins != 2:
            if currentMap != 271010000:
                Terminal.Rush(271010000)
                continue
                
            if henesysInRuins == 0:
                Quest.StartQuest(31105, 2142001)
      
            elif Quest.CheckCompleteDemand(31105, 2142002) == 0:
                Quest.CompleteQuest(31105, 2142002)
                
        elif fallOfCygnus != 2:
            if currentMap != 271010000:
                Terminal.Rush(271010000)
                continue
                
            if fallOfCygnus == 0:
                Quest.StartQuest(31106, 2142002)
                
            elif Quest.CheckCompleteDemand(31106, 2142002) == 0:
                Quest.CompleteQuest(31106, 2142002)
            
            
        elif scoutingStronghold != 2:
            if scoutingStronghold == 0:
                Terminal.Rush(271010000)
                time.sleep(1)
                # and then accept from alex
                Quest.StartQuest(31124, 2142001)
                continue
            
            elif Quest.CheckCompleteDemand(31124,2142001) == 0:
                Terminal.Rush(271010000)
                time.sleep(1)
                Quest.CompleteQuest(31124, 2142001)
                
            else:
                # quest is in progress, rush to stronghold entrance
                if currentMap == 271030010:
                    Character.Teleport(867, 148)
                    time.sleep(2)
                    Character.EnterPortal()
                    
                else:
                    Terminal.Rush(271030010)
                    
        elif piercingDefenses != 2:
            if piercingDefenses == 0:
                Terminal.Rush(271010000)
                time.sleep(1)
                # and then accept from alex
                Quest.StartQuest(31125, 2142001)
                continue
                
            elif Quest.CheckCompleteDemand(31125, 2142001) == 0:
                Terminal.Rush(271010000)
                time.sleep(1)
                Quest.CompleteQuest(31125, 2142001)
                
            else:
                # not done yet
                if currentMap != 271030010 or currentMap != 271030000:
                    Terminal.Rush(271030010)
                    
                else:
                    # we are in the map to get the item
                    # im assuming you have stable kill settings on
                    emblem = Field.FindItem(4032922)
                    if emblem.valid:
                        Character.Teleport(emblem.x, emblem.y)
                        time.sleep(2)
                        Character.LootItem()
                        time.sleep(2)
                        
        else:
            Terminal.SetRushByLevel(True)
                        