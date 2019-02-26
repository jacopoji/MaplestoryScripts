import Character
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time
import GameState
import datetime

def RushCheck(ID):
    if (ID == 450007210 or ID == 450007230) and Field.GetID() < 450007200:
        Terminal.Rush(450007030)
        while Terminal.IsRushing():
            time.sleep(1)   
        Terminal.Rush(450007040)
        while Terminal.IsRushing():
            time.sleep(1)
        while Field.GetID() != 450007200:
            Character.TalkToNpc(3003533)
            time.sleep(3)
    if Field.GetID() != ID:
        Terminal.Rush(ID)
        while Terminal.IsRushing():
            time.sleep(1)
        
def RushAndComplete(completemap, questid, npcid):
    if Field.GetID() != completemap:
        Terminal.Rush(completemap)
        while Terminal.IsRushing():
            time.sleep(1)
    else:
        if Character.GetPos().x < -800 or Character.GetPos().x > 675:
            Character.Teleport(-800, 153)
            time.sleep(2)
        Quest.CompleteQuest(questid, npcid)
        time.sleep(1)

if GameState.IsInGame():
    time.sleep(1)
    while Quest.GetQuestState(34773) != 2:
        time.sleep(1)
        Terminal.SetRushByLevel(False)
        daily1 = Quest.GetQuestState(34780)
        daily2 = Quest.GetQuestState(34781)
        daily3 = Quest.GetQuestState(34782)
        daily4 = Quest.GetQuestState(34783)
        daily5 = Quest.GetQuestState(34784)
        daily6 = Quest.GetQuestState(34785)
        daily7 = Quest.GetQuestState(34786)
        daily8 = Quest.GetQuestState(34787)
        daily9 = Quest.GetQuestState(34788)
        daily10 = Quest.GetQuestState(34789)
        daily11 = Quest.GetQuestState(34790)
        daily12 = Quest.GetQuestState(34791)
        daily13 = Quest.GetQuestState(34792)
        daily14 = Quest.GetQuestState(34793)
        daily15 = Quest.GetQuestState(34794)
        daily16 = Quest.GetQuestState(34795)
        daily17 = Quest.GetQuestState(34796)
        daily18 = Quest.GetQuestState(34797)
        daily19 = Quest.GetQuestState(34798)
        daily20 = Quest.GetQuestState(34799)
        completedaily = Quest.GetQuestState(34773)
            
        while Field.GetID() < 450007000:
            esfera = Packet.COutPacket(0x02CC)
            esfera.EncodeBuffer("00 00 00 90 D2 1A")
            Packet.SendPacket(esfera)
            time.sleep(5)
        
        while Quest.GetQuestState(34772) != 2:
            RushCheck(450007040)
            if Quest.GetQuestState(34772) == 0:
                Quest.StartQuest(34772, 3003530)
                time.sleep(1)
            else:
                Quest.CompleteQuest(34772, 3003530)
                time.sleep(1)
                
        if completedaily == 0:
            Terminal.ChangeStatus('Esfera Daily Started')
            Quest.StartQuest(34773, 3003530)
            Npc.ClearSelection()
            Npc.RegisterSelection("Those are all the requests I want to swap out.")
            time.sleep(5)
                
        if daily1 == 1:
            if Quest.CheckCompleteDemand(34780, 3003530):
                RushCheck(450007010)
            elif Quest.CheckCompleteDemand(34780, 3003530) == False:
                RushAndComplete(450007040, 34780, 3003530)
    
        elif daily2 == 1:
            if Quest.CheckCompleteDemand(34781, 3003530):
                RushCheck(450007030)
            elif Quest.CheckCompleteDemand(34781, 3003530) == False:
                RushAndComplete(450007040, 34781, 3003530)
        
        elif daily3 == 1:
            if Quest.CheckCompleteDemand(34782, 3003530):
                RushCheck(450007050)
            elif Quest.CheckCompleteDemand(34782, 3003530) == False:
                RushAndComplete(450007040, 34782, 3003530)

        elif daily4 == 1:
            if Quest.CheckCompleteDemand(34783, 3003530):
                RushCheck(450007070)
            elif Quest.CheckCompleteDemand(34783, 3003530) == False:
                RushAndComplete(450007040, 34783, 3003530)   
        
        elif daily5 == 1:
            if Quest.CheckCompleteDemand(34784, 3003530):
                RushCheck(450007110)
            elif Quest.CheckCompleteDemand(34784, 3003530) == False:
                RushAndComplete(450007040, 34784, 3003530)
                        
        elif daily6 == 1:
            if Quest.CheckCompleteDemand(34785, 3003530):
                RushCheck(450007130)
            elif Quest.CheckCompleteDemand(34785, 3003530) == False:
                RushAndComplete(450007040, 34785, 3003530)   
            
        elif daily7 == 1:
            if Quest.CheckCompleteDemand(34786, 3003530):
                RushCheck(450007140)
            elif Quest.CheckCompleteDemand(34786, 3003530) == False:
                RushAndComplete(450007040, 34786, 3003530)
                        
        elif daily8 == 1:
            if Quest.CheckCompleteDemand(34787, 3003530):
                RushCheck(450007160)
            elif Quest.CheckCompleteDemand(34787, 3003530) == False:
                RushAndComplete(450007040, 34787, 3003530)

        elif daily9 == 1:
            if Quest.CheckCompleteDemand(34788, 3003530):
                RushCheck(450007210)
            elif Quest.CheckCompleteDemand(34788, 3003530) == False:
                RushAndComplete(450007040, 34788, 3003530)
            
        elif daily10 == 1:
            if Quest.CheckCompleteDemand(34789, 3003530):
                RushCheck(450007230)
            elif Quest.CheckCompleteDemand(34789, 3003530) == False:
                RushAndComplete(450007040, 34789, 3003530)

        elif daily11 == 1:
            if Quest.CheckCompleteDemand(34790, 3003530):
                RushCheck(450007010)
            elif Quest.CheckCompleteDemand(34790, 3003530) == False:
                RushAndComplete(450007040, 34790, 3003530)

        elif daily12 == 1:
            if Quest.CheckCompleteDemand(34791, 3003530):
                RushCheck(450007030)
            elif Quest.CheckCompleteDemand(34791, 3003530) == False:
                RushAndComplete(450007040, 34791, 3003530)
            
        elif daily13 == 1:
            if Quest.CheckCompleteDemand(34792, 3003530):
                RushCheck(450007050)
            elif Quest.CheckCompleteDemand(34792, 3003530) == False:
                RushAndComplete(450007040, 34792, 3003530)
                                    
        elif daily14 == 1:
            if Quest.CheckCompleteDemand(34793, 3003530):
                RushCheck(450007070)
            elif Quest.CheckCompleteDemand(34793, 3003530) == False:
                RushAndComplete(450007040, 34793, 3003530)
                        
        elif daily15 == 1:
            if Quest.CheckCompleteDemand(34794, 3003530):
                RushCheck(450007110)
            elif Quest.CheckCompleteDemand(34794, 3003530) == False:
                RushAndComplete(450007040, 34794, 3003530)
                        
        elif daily16 == 1:
            if Quest.CheckCompleteDemand(34795, 3003530):
                RushCheck(450007130)
            elif Quest.CheckCompleteDemand(34795, 3003530) == False:
                RushAndComplete(450007040, 34795, 3003530)
                        
        elif daily17 == 1:
            if Quest.CheckCompleteDemand(34796, 3003530):
                RushCheck(450007140)
            elif Quest.CheckCompleteDemand(34796, 3003530) == False:
                RushAndComplete(450007040, 34796, 3003530)
                        
        elif daily18 == 1:
            if Quest.CheckCompleteDemand(34797, 3003530):
                RushCheck(450007160)
            elif Quest.CheckCompleteDemand(34797, 3003530) == False:
                RushAndComplete(450007040, 34797, 3003530)
                
        elif daily19 == 1:
            if Quest.CheckCompleteDemand(34798, 3003530):
                RushCheck(450007210)
            elif Quest.CheckCompleteDemand(34798, 3003530) == False:
                RushAndComplete(450007040, 34798, 3003530)
                    
        elif daily20 == 1:
            if Quest.CheckCompleteDemand(34799, 3003530):
                RushCheck(450007230)
            elif Quest.CheckCompleteDemand(34799, 3003530) == False:
                RushAndComplete(450007040, 34799, 3003530)
                
        elif completedaily == 1:
            if Quest.CheckCompleteDemand(34773, 3003530) == False:
                RushAndComplete(450007040, 34773, 3003530)
                Terminal.ChangeStatus('Esfera Daily Completed')
                
    while Field.GetID() > 450007000:
        nameless = Packet.COutPacket(0x02CC)
        nameless.EncodeBuffer("00 00 68 78 D2 1A")
        Packet.SendPacket(nameless)
        time.sleep(5)
else:
    time.sleep(1)