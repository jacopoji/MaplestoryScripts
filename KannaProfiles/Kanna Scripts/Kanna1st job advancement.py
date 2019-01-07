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

Terminal.SetRushByLevel(False)

while True:
    time.sleep(2)
    jobid = Character.GetJob()
    level = Character.GetLevel()
    field_id = Field.GetID()
    if jobid == -1 or level == -1:
        #not in game
        continue
    if jobid == 4200 and level <= 12:
        if field_id == 807040000:
            quest_state = Quest.GetQuestState(57400)
            quest_state1 = Quest.GetQuestState(57401)
            quest_state2 = Quest.GetQuestState(57402)
            if quest_state != 2:
                if quest_state == 0:
                    Quest.StartQuest(57400, 000000)
            elif quest_state1 != 2:
                if quest_state1 == 0:
                    Quest.StartQuest(57401, 9130082)
                elif quest_state1 == 1:
                    Quest.CompleteQuest(57401, 9130082)
            elif quest_state2 != 2:
                if quest_state2 == 0:
                    Quest.StartQuest(57402, 000000)
                elif quest_state2 ==1:
                    portal = Field.FindPortal("east00")
                    if portal.valid:
                        Character.Teleport(portal.x, portal.y-10)
                        time.sleep(1)
                        Character.EnterPortal()
        elif field_id == 807040100:
            quest = Quest.GetQuestState(57402)
            if quest == 1:
                Quest.CompleteQuest(57402, 9130083)
            else:
                time.sleep(1)
                fan = Inventory.FindItemByID(1552000)
                time.sleep(1)
                petbox = Inventory.FindItemByID(2000021)
                time.sleep(1)
                if fan.valid:
                    Inventory.SendChangeSlotPositionRequest(1, fan.pos, -11, -1)
                    time.sleep(1)
                    continue
                elif petbox.valid:
                    Inventory.UseItem(243265)
                    time.sleep(1)
                    continue
                else:
                    Key.Set(0x11, 1, 42001000)
                    time.sleep(1)
                    break
    else:
        break
                        
                    
