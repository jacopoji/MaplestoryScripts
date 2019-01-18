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
import GameState

Terminal.SetRushByLevel(False)

if GameState.IsInGame():
        time.sleep(2) #no stress cpu 
        jobid = Character.GetJob()
        level = Character.GetLevel()
        if jobid == -1 or level == -1:
            time.sleep(1)
        field_id = Field.GetID()
        quest_req = Quest.GetQuestState(31802)
        quest1 = Quest.GetQuestState(31804)
        quest2 = Quest.GetQuestState(31805)
        quest3 = Quest.GetQuestState(31806)
        quest4 = Quest.GetQuestState(31808)
        quest5 = Quest.GetQuestState(31809)
        quest8 = Quest.GetQuestState(31814)
        quest9 = Quest.GetQuestState(31813)
        quest10 = Quest.GetQuestState(31816)
        quest11 = Quest.GetQuestState(31818)
        quest13 = Quest.GetQuestState(31821)
        quest14 = Quest.GetQuestState(31823)
        quest15 = Quest.GetQuestState(31824)
        quest16 = Quest.GetQuestState(31825)
        quest17 = Quest.GetQuestState(31826)
        quest18 = Quest.GetQuestState(31827)
        quest19 = Quest.GetQuestState(31828)
        quest20 = Quest.GetQuestState(31829)
        quest21 = Quest.GetQuestState(31830)
        quest22 = Quest.GetQuestState(31832)
        quest23 = Quest.GetQuestState(31833)
        quest24 = Quest.GetQuestState(31854)
        quest25 = Quest.GetQuestState(31504)
        quest26 = Quest.GetQuestState(31505)

        #Talk to Edea and Piston
        if quest_req != 2:
                print("Need to talk")
        if quest1 != 2:
                    if field_id != 401000001:
                            Terminal.Rush(401000001)
                    elif quest1 == 0:
                            Quest.StartQuest(31804, 3001000)
                    elif quest1 == 1:
                            Quest.CompleteQuest(31804, 3001001)

        #kill the hounds
        elif quest2 != 2:
                    if quest2 == 0:
                            if field_id != 401000001:
                                    Terminal.Rush(401000001)
                            else:
                                    Quest.StartQuest(31805, 3001001)
                    elif quest2 == 1:
                            if Quest.CheckCompleteDemand(31805, 3001001) == 0:
                                    if field_id != 401000001:
                                            Terminal.Rush(401000001)
                                    else:
                                            Quest.CompleteQuest(31805, 3001001)
                            else:
                                    if field_id != 401010000:
                                            time.sleep(1)
                                            Terminal.Rush(401010000)
                                    else:
                                            time.sleep(1)
        #the mini dungeon
        elif quest3 != 2:
                    if quest3 == 0:
                            if field_id != 401000001:
                                    Terminal.Rush(401000001)
                            else:
                                    Quest.StartQuest(31806, 3001000)
                                    time.sleep(2)
                    elif quest3 == 1:
                            if Quest.CheckCompleteDemand(31806, 3001000) == 0:
                                    if field_id != 401000001:
                                            Terminal.Rush(401000001)
                                    else:
                                            Quest.CompleteQuest(31806, 3001000)
                            else:
                                    if field_id == 401070100:
                                            time.sleep(1)
                                            portal = Field.FindPortal("east00")
                                            pos = Character.GetPos()
                                            if portal.valid and pos.x != portal.x:
                                                    time.sleep(7)
                                                    Terminal.SetCheckBox("Kami Vac",False)
                                                    Character.Teleport(portal.x, portal.y-20)
                                                    time.sleep(1)
                                            time.sleep(3)
                                            Character.EnterPortal()
                                            time.sleep(0.1)
                                            Character.EnterPortal() #incase 1st doesn't register
                                            Terminal.SetCheckBox("Kami Vac",True)
                                    elif field_id == 401070200:
                                            time.sleep(1)
                                            portal = Field.FindPortal("east00")
                                            pos = Character.GetPos()
                                            if portal.valid and pos.x != portal.x:
                                                    time.sleep(7)
                                                    Terminal.SetCheckBox("Kami Vac",False)
                                                    Character.Teleport(portal.x, portal.y-20)
                                                    time.sleep(1)
                                            time.sleep(3)
                                            Character.EnterPortal()
                                            time.sleep(0.1)
                                            Character.EnterPortal() #incase 1st doesn't register
                                            Terminal.SetCheckBox("Kami Vac",True)
        #Talk to the guy outside the barracks
        elif quest4 != 2:
                    if quest4 == 0:
                            if field_id != 401000001:
                                    Terminal.Rush(401000001)
                            else:
                                    Quest.StartQuest(31808, 3001000)
                    elif quest4 == 1:
                            if field_id != 401000000:
                                    Terminal.Rush(401000000)
                            else:
                                    Quest.CompleteQuest(31808, 3001008)

        #kill dinogoth
        elif quest5 != 2:
                    if quest5 == 0:
                            if field_id != 401000000:
                                    Terminal.Rush(401000000)
                            else:
                                    Quest.StartQuest(31809, 3001008)
                    elif quest5 == 1:
                            if Quest.CheckCompleteDemand(31809, 3001008) == 0:
                                    if field_id != 401000000:
                                            Terminal.Rush(401000000)
                                    else:
                                            Quest.CompleteQuest(31809, 3001008)
                            else:
                                    if field_id != 401030000:
                                            time.sleep(1)
                                            Terminal.Rush(401030000)
                                    else:
                                            time.sleep(1)
        #Find the old guy, no need to map rush
        elif quest10 != 2:
                    if quest10 == 0:
                            if field_id != 401000001:
                                    Terminal.Rush(401000001)
                            else:
                                    Quest.StartQuest(31816, 3001000)
                    elif quest10 == 1:
                            if field_id != 401020100:
                                    time.sleep(1)
                                    Terminal.Rush(401020100)
                            else:
                                    Quest.CompleteQuest(31816, 3001002)
        #Get Dinor Sirloin 
        elif quest11 != 2:
                    if quest11 == 0:
                            if field_id != 401020100:
                                    Terminal.Rush(401020100)
                            else:
                                    Quest.StartQuest(31818, 3001002)
                    elif quest11 == 1:
                            if Quest.CheckCompleteDemand(31818, 3001002) == 0:
                                    if field_id != 401020100:
                                            Terminal.Rush(401020100)
                                    else:
                                            Quest.CompleteQuest(31818, 3001002)
                            else:
                                    if field_id != 401020000:
                                            Terminal.Rush(401020000) #need to rush here.
                                    else:
                                            time.sleep(1)
        elif quest13 != 2:
                    if quest13 == 0:
                            if field_id != 401020100:
                                    Terminal.Rush(401020100)
                            else:
                                    Quest.StartQuest(31821, 3001002)
                    elif quest13 == 1:
                            if field_id != 401020300:
                                    Terminal.Rush(401020300)
                            else:
                                    item = Inventory.FindItemByID(2430947)
                                    if item.valid:
                                            Inventory.UseItem(2430947)
                                            time.sleep(1)
                                    Quest.CompleteQuest(31821, 3001004) 
        elif quest14 != 2:
                    if quest14 == 0:
                            if field_id != 401020300:
                                    Terminal.Rush(401020300)
                            else:
                                    Quest.StartQuest(31823, 3001004)
                    elif quest14 == 1:
                            if Quest.CheckCompleteDemand(31823, 3001004) == 0:
                                    if field_id != 401020300:
                                            Terminal.Rush(401020300)
                                    else:
                                            Quest.CompleteQuest(31823, 3001004)
                            else:
                                    if field_id != 401030200:
                                            #do not need to rush here
                                            time.sleep(1)
                                            Terminal.Rush(401030200)
                                    else:
                                            time.sleep(1)
                                        
        elif quest15 != 2:
                    if quest15 == 0:
                            if field_id != 401020300:
                                    Terminal.Rush(401020300)
                            else:
                                    Quest.StartQuest(31824, 00000000) #only need to accept (auto complete i guess)

        #dinoram claws           
        elif quest16 != 2:
                    if quest16 == 0:
                            if field_id != 401020300:
                                    Terminal.Rush(401020300)
                            else:
                                    Quest.StartQuest(31825, 3001005)
                    elif quest16 == 1:
                            if Quest.CheckCompleteDemand(31825, 3001005) == 0:
                                    if field_id != 401020300:
                                            Terminal.Rush(401020300)
                                    else:
                                            Quest.CompleteQuest(31825, 3001005)
                            else:
                                    if field_id != 401020000:
                                            #automatically rushes here
                                            time.sleep(1)
                                            Terminal.Rush(401020000)
                                    else:
                                            time.sleep(1)
                                        
        elif quest17 != 2:
                    if quest17 == 0:
                            if field_id != 401020300:
                                    Terminal.Rush(401020300)
                            else:
                                    Quest.StartQuest(31826, 00000000) #only need to accept (auto complete i guess)
        
        #Yellow Speeyor Torn fur coat
        elif quest18 != 2:
                    if quest18 == 0:
                            if field_id != 401020300:
                                    Terminal.Rush(401020300)
                            else:
                                    Quest.StartQuest(31827, 3001004)
                    elif quest18 == 1:
                            if Quest.CheckCompleteDemand(31827, 3001004) == 0:
                                    if field_id != 401020300:
                                            Terminal.Rush(401020300)
                                    else:
                                            Quest.CompleteQuest(31827, 3001004)
                            else:
                                    if field_id != 401020200:
                                            time.sleep(1)
                                            Terminal.Rush(401020200)
                                    else:
                                            time.sleep(1)
        #back to edea                           
        elif quest19 != 2:
                    if quest19 == 0:
                            if field_id != 401020100:
                                    time.sleep(1)
                                    Terminal.Rush(401020100)
                            else:
                                    Quest.StartQuest(31828, 3001002)
                    elif quest19 == 1:
                            if field_id != 401000001:
                                    time.sleep(1)
                                    Terminal.Rush(401000001)
                            else:
                                    Quest.CompleteQuest(31828, 3001000)
        #ores
        elif quest20 != 2:
                    if quest20 == 0:
                            if field_id != 401000001:
                                    Terminal.Rush(401000001)
                            else:
                                    Quest.StartQuest(31829, 3001000)
                    elif quest20 == 1:
                            if Quest.CheckCompleteDemand(31829, 3001000) == 0:
                                    if field_id != 401000001:
                                            Terminal.Rush(401000001)
                                    else:
                                            Quest.CompleteQuest(31829, 3001000)
                            else:
                                    if field_id != 401030300:
                                            time.sleep(1)
                                            Terminal.Rush(401030300)
                                    else:
                                            time.sleep(1)
        #mini dungeon
        elif quest21 != 2:
                    if quest21 == 0:
                            if field_id != 401000001:
                                    Terminal.Rush(401000001)
                            else:
                                    Quest.StartQuest(31830, 3001000)
                    elif quest21 == 1:
                            if field_id == 401000001:
                                    time.sleep(1)
                            elif field_id == 401070600:
                                    portal = Field.FindPortal("east00")
                                    pos = Character.GetPos()
                                    if portal.valid and portal.x != pos.x:
                                            time.sleep(7)
                                            Terminal.SetCheckBox("Kami Vac",False)
                                            Character.Teleport(portal.x, portal.y-20)
                                            time.sleep(1)
                                    time.sleep(3)
                                    Character.EnterPortal()
                                    time.sleep(0.1)
                                    Character.EnterPortal() #incase 1st doesn't register
                                    Terminal.SetCheckBox("Kami Vac",True)
                            elif field_id == 401070700:
                                    portal = Field.FindPortal("east00")
                                    pos = Character.GetPos()
                                    if portal.valid and portal.x != pos.x:
                                            time.sleep(7)
                                            Terminal.SetCheckBox("Kami Vac",False)
                                            Character.Teleport(portal.x, portal.y-20)
                                            time.sleep(1)
                                    time.sleep(3)
                                    Character.EnterPortal()
                                    time.sleep(0.1)
                                    Character.EnterPortal() #incase 1st doesn't register
                                    Terminal.SetCheckBox("Kami Vac",True)
                            elif field_id == 401070800:
                                    portal = Field.FindPortal("east00")
                                    pos = Character.GetPos()
                                    if portal.valid and portal.x != pos.x:
                                            time.sleep(7)
                                            Terminal.SetCheckBox("Kami Vac",False)
                                            Character.Teleport(portal.x, portal.y-20)
                                            time.sleep(1)
                                    time.sleep(3)
                                    Character.EnterPortal()
                                    time.sleep(0.1)
                                    Character.EnterPortal() #incase 1st doesn't register
                                    Terminal.SetCheckBox("Kami Vac",True)
                            elif field_id == 401070900:
                                    portal = Field.FindPortal("east00")
                                    pos = Character.GetPos()
                                    if portal.valid and portal.x != pos.x:
                                            time.sleep(7)
                                            Terminal.SetCheckBox("Kami Vac",False)
                                            Character.Teleport(portal.x, portal.y-20)
                                            time.sleep(1)
                                    time.sleep(3)
                                    Character.EnterPortal()
                                    time.sleep(0.1)
                                    Character.EnterPortal() #incase 1st doesn't register
                                    Terminal.SetCheckBox("Kami Vac",True)
                            else:
                                    time.sleep(1)
                                
        elif quest22 != 2:
                if quest22 == 0:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.StartQuest(31832, 3001100)
                elif quest22 == 1:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.CompleteQuest(31832, 3001100)
        elif quest23 != 2:
                if quest23 == 0:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.StartQuest(31833, 00000000)
                elif quest23 == 1:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.CompleteQuest(31833, 3001100) 
        elif quest24 != 2:
                if quest24 == 0:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.StartQuest(31854, 1540447)
                elif quest24 == 1:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.CompleteQuest(31854, 0)

        elif quest25 != 2:
                if quest25 == 0:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.StartQuest(31504, 3001100)
                elif quest25 == 1:
                        if Quest.CheckCompleteDemand(31504, 3001100) == 0:
                                if field_id != 401040000:
                                        time.sleep(1)
                                        Terminal.Rush(401040000)
                                else:
                                        Quest.CompleteQuest(31504, 3001100)
                        else:
                                if field_id != 401052000:
                                        time.sleep(1)
                                        Terminal.Rush(401052000)
                                else:
                                        time.sleep(1)

        elif quest26 != 2:
                if quest26 == 0:
                        if field_id != 401040000:
                                Terminal.Rush(401040000)
                        else:
                                Quest.StartQuest(31505, 3001100)
                elif quest26 == 1:
                        if Quest.CheckCompleteDemand(31505, 3001100) == 0:
                                if field_id != 401040000:
                                        time.sleep(1)
                                        Terminal.Rush(401040000)
                                else:
                                        Quest.CompleteQuest(31505, 3001100)
                        else:
                                if field_id != 401052002:
                                        time.sleep(1)
                                        Terminal.Rush(401052002)
                                else:
                                        time.sleep(1)