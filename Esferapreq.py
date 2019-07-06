import os, sys

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")

try:
    import SunCat, SCHotkey, SCLib
except:
    print("Couldn't find SunCat module")
import Character
import Context
import DataType
import Field
import Inventory
import Key
import Npc
import Quest
import Terminal
import time
import Party
import GameState

def kami():
    Terminal.SetCheckBox("Kami Vac", True)


def spacemash():
    for _ in range(0, 40):
        space = 0x20
        Key.Down(space)
        time.sleep(0.1)
        Key.Up(space)

def kamioff():
    Terminal.SetCheckBox("Kami Vac", False)
pos= Character.GetPos()
def basecamp():
    if Field.GetID() == 450007040:
        if pos.x != -1196 or pos.y !=-395:
            Character.Teleport(-1196,-395)

def rightmash():
    for _ in range ( 0, 40) :
        right=0x27
        Key.Down(right)
        time.sleep(0.1)
        Key.Up(right)

def leftmash():
    for _ in range ( 0, 40) :
        left=0x25
        Key.Down(left)
        time.sleep(0.1)
        Key.Up(left)        


Terminal.SetRushByLevel(False)
if Character.GetLevel() >= 235:
    if Quest.GetQuestState(34562) == 0:
        Quest.CompleteQuest(34562, 3003541)
    if Quest.GetQuestState(34562) == 2:
        if Quest.GetQuestState(34563) == 0:
            Quest.StartQuest(34563, 3003541)
        if Quest.GetQuestState(34563) == 1:
            if Quest.CheckCompleteDemand(34563, 3003542) != 0:
                Terminal.Rush(450007010)
                kami()
            if Quest.CheckCompleteDemand(34563, 3003542) == 0:
                kamioff() 
                Character.Teleport(-89,-205)
                Quest.CompleteQuest(34563, 3003542)
        if Quest.GetQuestState(34563) == 2:
            if Quest.GetQuestState(34564) == 0:
                Quest.StartQuest(34564,3003542)
            if Quest.GetQuestState(34564) == 1:
                Terminal.Rush(450007030)
                if Field.GetID() == 450007030:
                    Character.Teleport(44,-205)
                Quest.CompleteQuest(34564, 3003543)
            if Quest.GetQuestState(34564) == 2:
                if Quest.GetQuestState(34565) == 0:
                    if Field.GetID() == 450007030:
                        Character.Teleport(44,-205)
                    Quest.StartQuest(34565, 3003543)
                if Quest.GetQuestState(34565) == 1:
                    if Quest.CheckCompleteDemand(34565, 3003542) != 0:
                        Terminal.Rush(450007030)
                        kami()
                    if Quest.CheckCompleteDemand(34565, 3003542) == 0:
                        kamioff()
                        Character.Teleport(44,-205)
                    Quest.CompleteQuest(34564, 3003543)
                if Quest.GetQuestState(34565) == 2:
                    if Quest.GetQuestState(34566) == 0:
                        Quest.StartQuest(34566,3003543)
                    if Quest.GetQuestState(34566) == 1:
                        basecamp()
                        Quest.CompleteQuest(34566, 3003532)
                    if Quest.GetQuestState(34566) == 2:
                        if Quest.GetQuestState(34567) == 0:
                            basecamp()
                            Quest.StartQuest(34567,3003531)
                        if Quest.GetQuestState(34567) == 1:
                            Terminal.Rush(450007050)
                            if pos.x != 44:
                                Character.Teleport(44,-205)
                            Quest.CompleteQuest(34567,3003544)
                        if Quest.GetQuestState(34567) == 2:
                            if Quest.GetQuestState(34568) == 0:
                                Quest.StartQuest(34568, 3003544)
                            if Quest.GetQuestState(34568) == 1:
                                if Quest.CheckCompleteDemand(34568, 3003544) != 0:
                                    Terminal.Rush(450007050)
                                    kami()
                                if Quest.CheckCompleteDemand(34568, 3003544) == 0:
                                    kamioff()
                                    Character.Teleport(44,-205)
                                    time.sleep(3)
                                    Quest.CompleteQuest(34568,3003544)
                                    time.sleep(3)
                            if Quest.GetQuestState(34568) == 2:
                                if Quest.GetQuestState(34569) == 0:
                                    Quest.StartQuest(34569,3003544)
                                if Quest.GetQuestState(34569) ==1:
                                    Terminal.Rush(450007070)
                                    Quest.CompleteQuest(34569,3003545)
                                if Quest.GetQuestState(34569) ==2:
                                    if Quest.GetQuestState(34570) == 0:
                                        Quest.StartQuest(34570,3003545)
                                    if Quest.GetQuestState(34570) == 1:
                                        if Quest.CheckCompleteDemand(34570, 3003545) != 0:
                                            Terminal.Rush(450007070)
                                            kami()
                                        if Quest.CheckCompleteDemand(34570, 3003545) == 0:
                                            kamioff()
                                            Character.Teleport(44,-205)
                                            time.sleep(3)
                                            Quest.CompleteQuest(34570,3003545)
                                            time.sleep(3)
                                    if Quest.GetQuestState(34570) == 2:
                                        if Quest.GetQuestState(34571) ==0:
                                            basecamp()
                                            Quest.StartQuest(34571,3003530)
                                        if Quest.GetQuestState(34571) ==1:
                                            Quest.CompleteQuest(34571,3003546)
                                            time.sleep(3)
                                        if Quest.GetQuestState(34571) == 2:
                                            if Quest.GetQuestState(34572) == 0:
                                                Quest.StartQuest(34572,3003546)
                                            if Quest.GetQuestState(34572) == 1:
                                                if Quest.CheckCompleteDemand(34572, 3003547) != 0:
                                                    Terminal.Rush(450007110)
                                                    kami()
                                                if Quest.CheckCompleteDemand(34572, 3003547) == 0:
                                                    kamioff()
                                                    Character.Teleport(-69,-12)
                                                    time.sleep(3)
                                                    Quest.CompleteQuest(34572,3003547)
                                                    time.sleep(3)
                                            if Quest.GetQuestState(34572) == 2:
                                                if Quest.GetQuestState(34573) == 0:
                                                    Quest.StartQuest(34573,3003547)
                                            if Quest.GetQuestState(34573) == 1:
                                                Terminal.Rush(450007130)
                                                Quest.CompleteQuest(34573,3003548)
                                            if Quest.GetQuestState(34573) ==2:
                                                if Quest.GetQuestState(34574) == 0:
                                                    Quest.StartQuest(34574,3003548)
                                                if Quest.GetQuestState(34574) == 1:

                                                    if Quest.CheckCompleteDemand(34574, 3003548) != 0:
                                                        Terminal.Rush(450007130)
                                                        kami()
                                                    if Quest.CheckCompleteDemand(34574, 3003548) == 0:
                                                        kamioff()
                                                        Character.Teleport(-69,-12)
                                                        time.sleep(3)
                                                        Quest.CompleteQuest(34574,3003548)
                                                        time.sleep(3)
                                                if Quest.GetQuestState(34574) == 2:
                                                    if Quest.GetQuestState(34575) == 0:
                                                        Quest.StartQuest(34575,3003548)
                                                    if Quest.GetQuestState(34575) == 1:
                                                        Terminal.Rush(450007140)
                                                        Quest.CompleteQuest(34575,3003552)
                                                    if Quest.GetQuestState(34575) == 2:
                                                        if Quest.GetQuestState(34576) == 0:
                                                            Quest.StartQuest(34576,3003552)
                                                        if Quest.GetQuestState(34576) == 1:
                                                            if Quest.CheckCompleteDemand(34576, 3003552) != 0:
                                                                kami()
                                                            if Quest.CheckCompleteDemand(34576, 3003552) == 0:
                                                                kamioff()
                                                                Quest.CompleteQuest(34576,3003552)
                                                        if Quest.GetQuestState(34576) == 2:
                                                            if Quest.GetQuestState(34577) == 0:
                                                                Quest.StartQuest(34577,3003552)
                                                            if Quest.GetQuestState(34577) == 1:
                                                                Terminal.Rush(450007160)
                                                                Quest.CompleteQuest(34577,3003553)
                                                            if Quest.GetQuestState(34577) == 2:
                                                                if Quest.GetQuestState(34578) == 0:
                                                                    Quest.StartQuest(34578,3003553)
                                                                if Quest.GetQuestState(34578) == 1:
                                                                    if Quest.CheckCompleteDemand(34578, 3003553) != 0:
                                                                        kami()
                                                                    if Quest.CheckCompleteDemand(34578, 3003553) == 0:
                                                                        kamioff()
                                                                        Quest.CompleteQuest(34578,3003553)
                                                                if Quest.GetQuestState(34578) == 2:
                                                                    if Quest.GetQuestState(34579) == 0:
                                                                        if Field.GetID() == 450007160:
                                                                            Terminal.Rush(450007170)
                                                                        Quest.StartQuest(34579,3003551)
                                                                        if Field.GetID() == 450007410:
                                                                            rightmash()
                                                                            leftmash()
                                                                    if Quest.GetQuestState(34579) == 2:
                                                                        if Quest.GetQuestState(34580) == 0:
                                                                            Quest.StartQuest(34580, 3003551)
                                                                        if Quest.GetQuestState(34580) == 1:
                                                                            if Field.GetID() == 450007420:
                                                                                kami()
                                                                            Quest.CompleteQuest(34580, 3003554)
                                                                        if Quest.GetQuestState(34580) == 2:
                                                                            if Quest.GetQuestState(34581) == 0:
                                                                                if Field.GetID() == 450007040:
                                                                                    Character.TalkToNpc(3003533)
                                                                                if Field.GetID() == 450007200:
                                                                                    Quest.StartQuest(34581,3003555)
                                                                            if Quest.GetQuestState(34581) == 1:
                                                                                Terminal.Rush(450007210)
                                                                                Quest.CompleteQuest(34581,3003556)
                                                                            if Quest.GetQuestState(34581) == 2:
                                                                                if Quest.GetQuestState(34582) == 0:
                                                                                    Quest.StartQuest(34582,3003556)
                                                                                if Quest.GetQuestState(34582) ==1:
                                                                                    if Quest.CheckCompleteDemand(34582, 3003556) != 0:
                                                                                        kami()
                                                                                    if Quest.CheckCompleteDemand(34582, 3003556) == 0:
                                                                                        kamioff()
                                                                                        Quest.CompleteQuest(34582,3003556)
                                                                                if Quest.GetQuestState(34582) ==2:
                                                                                    if Quest.GetQuestState(34583) ==0:
                                                                                        Quest.StartQuest(34583,3003556)
                                                                                    if Quest.GetQuestState(34583) ==1:
                                                                                        Terminal.Rush(450007230)
                                                                                        Quest.CompleteQuest(34583,3003557)
                                                                                    if Quest.GetQuestState(34583) ==2:
                                                                                        if Quest.GetQuestState(34584) ==0:
                                                                                            Quest.StartQuest(34584, 3003557)
                                                                                        if Quest.GetQuestState(34584) ==1:
                                                                                            if Quest.CheckCompleteDemand(34584, 3003557) != 0:
                                                                                                kami()
                                                                                            if Quest.CheckCompleteDemand(34584, 3003557) == 0:
                                                                                                kamioff()
                                                                                                Quest.CompleteQuest(34584,3003557)
                                                                                        if Quest.GetQuestState(34584) ==2:
                                                                                            if Quest.GetQuestState(34585)== 0:
                                                                                                Quest.StartQuest(34585, 3003558)
                                                                                            if Quest.GetQuestState(34585)== 1:
                                                                                                Party.CreateParty()
                                                                                                Npc.RegisterSelection("Go to Diffraction Hall")
                                                                                                Character.TalkToNpc(3003560)
                                                                                                Npc.ClearSelection()
                                                                                                if Field.GetID() == 450008450:
                                                                                                    kami()
                                                                                                if Field.GetID() == 450007510:
                                                                                                    kamioff()
                                                                                                    Character.TalkToNpc(3003563)
                                                                                                    Character.TalkToNpc(3003559)
                                                                                            arcsymbol = Inventory.FindItemByID(1712006)
                                                                                            if arcsymbol.valid:
                                                                                                Inventory.SendChangeSlotPositionRequest(1, arcsymbol.pos, -1605, -1)
                                                                                            print("you got the orb")                
                                                                                                                            

                                                                                        








                                                
                                                

                                            



                
                    

        