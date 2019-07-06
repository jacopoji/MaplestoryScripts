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
import GameState

def kami():
    Terminal.SetCheckBox("Kami Vac", False)


def spacemash():
    for _ in range(0, 40):
        space = 0x20
        Key.Down(space)
        time.sleep(0.1)
        Key.Up(space)

def kamioff():
    Terminal.SetCheckBox("Kami Vac", False)


def spacemash():
    for _ in range(0, 40):
        Key.Press(0x20)
        Key.Press(0x88)
   
Nonpc= Field.FindNpc(3003420)
npc2= Field.FindNpc(3003421)

Terminal.SetRushByLevel(False)
if Quest.GetQuestState(34250) == 0:
    print("Quest 1 not started")
    if Field.GetID() != 450006010:    
        Terminal.Rush(450006010)
    if Field.GetID() == 450006010:
        Quest.StartQuest(34250, 3003420)
if Quest.GetQuestState(34250) == 1:
    print("quest 1 started")
    if Quest.CheckCompleteDemand(34250, 3003420) != 0:
        Terminal.Rush(450006010)
        if Field.GetID() == 450006010:    
            kami()
    if Quest.CheckCompleteDemand(34250, 3003420) == 0:

        kamioff()
        if Field.GetID() != 450006010:    
            Terminal.Rush(450006010)
        if Field.GetID() == 450006010:
            if Character.GetPos() != Nonpc.x or Character.GetPos() != Nonpc.y:
                Character.Teleport(Nonpc.x,Nonpc.y)
            Quest.CompleteQuest(34250, 3003420)
if Quest.GetQuestState(34250) == 2:
    
    if Quest.GetQuestState(34251) == 0:
        Terminal.Rush(450006010)
        Quest.StartQuest(34251, 3003420)   
        print("quest 2 started") 
    if Quest.CheckCompleteDemand(34251, 3003421) == 0:
        Terminal.Rush(450006030)
        if Character.GetPos() != npc2.x or Character.GetPos() != npc2.y:
            Character.Teleport(npc2.x,npc2.y)
        Quest.CompleteQuest(34251, 3003421)
        print("quest 2 completed")
    if Quest.GetQuestState(34251) == 2:
        if Quest.GetQuestState(34252) == 0:
            if Field.GetID() != 450006030:
                Terminal.Rush(4500006030)
            if Field.GetID() == 450006030:    
                Quest.StartQuest(34252, 3003421)
        if Quest.GetQuestState(34252) == 1:
            if Quest.CheckCompleteDemand(34252, 3003421) != 0:
                Terminal.Rush(450006030)
                if Field.GetID() == 450006030:
                    kami()
            if Quest.CheckCompleteDemand(34252, 3003421) == 0:
                kamioff()
                if Field.GetID() != 450006030:
                    Terminal.Rush(450006030)
                if Field.GetID() == 450006030:
                    Character.Teleport(-767,-207)
                    Quest.CompleteQuest(34252, 3003421)
        if Quest.GetQuestState(34252) == 2:
            
            if Quest.GetQuestState(34253) == 0:
                print("quest 4 not started")
                Terminal.Rush(450006130)
                time.sleep(7)
                Terminal.Rush(450006110)
                Character.Teleport(-1967,-473)
                Quest.StartQuest(34253, 3003423)
            if Quest.GetQuestState(34253) == 1:
                if Quest.CheckCompleteDemand(34253, 3003423) != 0:
                    if Field.GetID() != 450006110:
                        Terminal.Rush(450006110)
                    if Field.GetID() == 450006110:
                        kami()
                if Quest.CheckCompleteDemand(34253, 3003424) == 0:
                    kamioff()
                    if Field.GetID() != 450006110:
                        Terminal.Rush(450006110)
                    if Field.GetID() == 450006110:    
                        Character.Teleport(-1967,-473)
                        Quest.CompleteQuest(34253,3003424)
            if Quest.GetQuestState(34253) == 2:
                if Quest.GetQuestState(34254) == 0:
                    print("Quest not completed")
                    if Field.GetID() != 450006130:
                        Terminal.Rush(450006130)
                    if Field.GetID() == 450006130:
                        pos=Character.GetPos()
                        if pos.x != 19 or pos.y != 24:
                            Character.Teleport(19, 24)
                            Quest.StartQuest(34254, 3003425)
                if Quest.GetQuestState(34254) == 1:
                    pos=Character.GetPos()
                    if pos.x != 1871 or pos.y != -449:
                        Character.Teleport(1871, -449)

                    Quest.CompleteQuest(34254, 3003426)
                if Quest.GetQuestState(34254) == 2:
                    if Quest.GetQuestState(34255) == 0:
                        if pos.x != 1871 or pos.y != -449:
                            Character.Teleport(1871, -449)
                        Quest.StartQuest(34255, 3003426)
                    if Quest.GetQuestState(34255) == 1:
                        if Quest.CheckCompleteDemand(34255, 3003426) != 0:
                            if Field.GetID() != 450006140:
                                Terminal.Rush(450006140)
                            if Field.GetID() == 450006140:
                                kami()
                        if Quest.CheckCompleteDemand(34255, 3003426) == 0:
                            kamioff() 
                            if Field.GetID() != 450006130:
                                Terminal.Rush(450006130)
                            if Field.GetID() == 450006130:
                                if pos.x != 1871 or pos.y != -449:
                                    Character.Teleport(1871, -449)
                                Character.Teleport(1871, -449)
                                Quest.CompleteQuest(34255, 3003426)   
                    if Quest.GetQuestState(34255) == 2:
                        if Quest.GetQuestState(34256) == 0:
                            if Field.GetID() != 450006130:
                                Terminal.Rush(450006130)
                            if Field.GetID() == 450006130:    
                                pos=Character.GetPos()
                                if pos.x != 1677 or pos.y != 24:
                                    Character.Teleport(1677, 24)
                                Quest.StartQuest(34256, 3003427)   
                        if Quest.GetQuestState(34256) == 1:
                            if Quest.CheckCompleteDemand(34256, 3003427) != 0:
                                if Field.GetID() != 450006160:
                                    Terminal.Rush(450006160) 
                                if Field.GetID() == 450006160:
                                    kami()
                            if Quest.CheckCompleteDemand(34256, 3003427) == 0:
                                kamioff() 
                                if Field.GetID() != 450006130:
                                    Terminal.Rush(450006130)
                                if Field.GetID() == 450006130:
                                    pos=Character.GetPos()
                                    if pos.x != 1677 or pos.y != 24:
                                        Character.Teleport(1677, 24)
                                    Quest.CompleteQuest(34256, 3003427)
                        if Quest.GetQuestState(34256) == 2:
                            if Quest.GetQuestState(34257) == 0:
                                if Field.GetID() != 450006130:
                                    Terminal.Rush(45000130)
                                if Field.GetID() == 450006130:
                                    Quest.StartQuest(34257, 3003427)
                            if Quest.GetQuestState(34257) == 1:
                                if Field.GetID() != 450006130:
                                    Terminal.Rush(45000130)
                                if Field.GetID() == 450006130:     
                                    pos= Character.GetPos()
                                    if pos.x != -341 or pos.y != 24:
                                        Character.Teleport(-341, 24)
                                    Quest.CompleteQuest(34257, 3003425)
                            if Quest.GetQuestState(34257) == 2:
                                if Quest.GetQuestState(34258) == 0:
                                    if Field.GetID() != 450006240:
                                        Terminal.Rush(450006240)
                                    if Field.GetID() == 450006240:
                                        Quest.StartQuest(34258, 3003428)
                                if Quest.GetQuestState(34258) == 1:
                                    if Field.GetID() != 450006240:
                                        Terminal.Rush(450006240)
                                    if Field.GetID() == 450006240:
                                        Quest.CompleteQuest(34258, 3003429)
                                if Quest.GetQuestState(34258) == 2:
                                    if Quest.GetQuestState(34259) == 0:
                                        if Field.GetID() != 450006240:
                                            Terminal.Rush(450006240)
                                        if Field.GetID() == 450006240:
                                            Quest.StartQuest(34259, 3003429) 
                                    if Quest.GetQuestState(34259) == 1:
                                        if Quest.CheckCompleteDemand(34259, 3003429) != 0:
                                            if Field.GetID() != 450006210:
                                                Terminal.Rush(450006210)
                                            if Field.GetID() == 450006210:
                                                item=Inventory.FindItemByID(2437666)
                                                if item.valid:
                                                    Inventory.UseItem(2437666)
                                                if not item.valid:
                                                    kami()
                                        if Quest.CheckCompleteDemand(34259, 3003429) == 0:
                                            if Field.GetID() != 450006240:
                                                Terminal.Rush(450006240)
                                            if Field.GetID() == 450006240:
                                                Quest.CompleteQuest(34259, 3003429)
                                    if Quest.GetQuestState(34259) == 2:
                                        if Quest.GetQuestState(34260)  == 0:
                                            if Field.GetID() != 450006240:
                                                Terminal.Rush(450006240)
                                            if Field.GetID() == 450006240:
                                                Quest.StartQuest(34260, 3003428)  
                                        if Quest.GetQuestState(34260) == 2:
                                            if Quest.GetQuestState(34261) == 0:
                                                if Field.GetID() != 450006240:
                                                    Terminal.Rush(450006240)
                                                if Field.GetID() == 450006240:
                                                    Quest.StartQuest(34261, 3003429)
                                            if Quest.GetQuestState(34261) == 1:
                                                if Quest.CheckCompleteDemand(34261, 3003429) != 0:
                                                    if Field.GetID() != 450006230:
                                                        Terminal.Rush(450006230)
                                                    if Field.GetID() == 450006230:
                                                        kami()
                                                if Quest.CheckCompleteDemand(34261, 3003429) == 0:
                                                    kamioff()
                                                    if Field.GetID() != 450006240:
                                                        Terminal.Rush(450006240)
                                                    if Field.GetID() == 450006240:
                                                        Quest.CompleteQuest(34261, 3003429)
                                            if Quest.GetQuestState(34261) == 2:
                                                if Quest.GetQuestState(34262) == 0:    
                                                    if Field.GetID() != 450006240:
                                                        Terminal.Rush(450006240)
                                                    if Field.GetID() == 450006240:
                                                        Quest.StartQuest(34262, 3003428)
                                                if Quest.GetQuestState(34262) == 2:
                                                    if Quest.GetQuestState(34263) == 0:
                                                        Terminal.Rush(450006300)
                                                        if Field.GetID() == 450006300:
                                                            Quest.StartQuest(34263, 3003430)
                                                    if Quest.GetQuestState(34263) == 1:
                                                        if Quest.CheckCompleteDemand(34263, 3003430) != 0:
                                                            if Field.GetID() != 450006300:
                                                                Terminal.Rush(450006300)
                                                            if Field.GetID() == 450006300:
                                                                kami()
                                                        if Quest.CheckCompleteDemand(34263, 3003430) == 0:
                                                            kamioff()
                                                            if Field.GetID() != 450006300:
                                                                Terminal.Rush(450006300)
                                                            if Field.GetID() == 450006300:
                                                                Quest.CompleteQuest(34263, 3003430)
                                                    if Quest.GetQuestState(34263) == 2:
                                                        if Quest.GetQuestState(34264) == 0:    
                                                            if Field.GetID() != 450006300:
                                                                Terminal.Rush(450006300)
                                                            if Field.GetID() == 450006300:
                                                                Quest.StartQuest(34264, 3003430)
                                                        if Quest.GetQuestState(34264)  == 1:
                                                            if Field.GetID() != 450006320:
                                                                Terminal.Rush(450006320)
                                                            if Field.GetID() == 450006320:
                                                                Quest.CompleteQuest(34264, 3003431)    
                                                        if Quest.GetQuestState(34264) == 2:
                                                            if Quest.GetQuestState(34265) == 0 :
                                                                Quest.StartQuest(34265, 3003431)
                                                            if Quest.GetQuestState(34265) == 1: 
                                                                if Quest.CheckCompleteDemand(34265, 3003431) != 0:    
                                                                    kami()
                                                                if Quest.CheckCompleteDemand(34265, 3003431) == 0:
                                                                    kamioff()
                                                                    Quest.CompleteQuest(34265, 3003431)
                                                            if Quest.GetQuestState(34265) == 2:    
                                                                if Quest.GetQuestState(34266) == 0:
                                                                    print("ff")                                                           
                                                                    Terminal.Rush(450006330)
                                                                    time.sleep(5)
                                                                    Terminal.Rush(450006240)
                                                                    time.sleep(5)
                                                                    Quest.StartQuest(34266, 3003429)
                                                                    time.sleep(5)
                                                                    spacemash()
                                                                    time.sleep(10)
                                                                    mob=Field.FindMob(8644420)
                                                                    if Field.GetID() == 940204030:
                                                                        Terminal.StopRush()
                                                                        Character.AMoveX(1565)
                                                                        Character.EnterPortal()

                                                                    if mob.valid:
                                                                        kami()
                                                                    if not mob.valid:
                                                                        kamioff()
                                                                        Character.Teleport(1569,95)
                                                                        Character.EnterPortal()
                                                                if Quest.GetQuestState(34266) == 2:
                                                                    if Quest.GetQuestState(34267) == 0:
                                                                        Quest.StartQuest(34267, 3003433)
                                                                    if Quest.GetQuestState(34267 ) == 1:
                                                                        if Field.GetID() == 450006240:    
                                                                            Character.Teleport(-825,25)
                                                                            Character.EnterPortal()
                                                                        if Field.GetID() == 450006400:
                                                                            Character.Teleport(1250,-510)
                                                                            time.sleep(5)
                                                                            Character.EnterPortal()

                                                                        mob= Field.FindMob(8644422)
                                                                        mob1= Field.FindMob(8644420)
                                                                        mob2= Field.FindMob(8644423)
                                                                        mob3=Field.FindMob(8644421)
                                                                        mob4= Field.FindMob(8644424)
                                                                        if mob.valid:
                                                                            kami()
                                                                        if mob1.valid:
                                                                            kami()
                                                                        if mob2.valid:
                                                                            kami()
                                                                        if mob3.valid:
                                                                            kami()
                                                                        if mob4.valid:
                                                                            kami()
                                                                            
                                                                        if not mob.valid:
                                                                            if not mob1.valid:
                                                                                if not mob2.valid:
                                                                                    if not mob3.valid:
                                                                                        if not mob4.valid:
                                                                                            print("mob not vlaid")
                                                                                            kamioff()
                                                                                            pos=Character.GetPos()
                                                                                            map1= 940204040
                                                                                            map2= 940204041
                                                                                            map3= 940204050
                                                                                            map4= 940204051
                                                                                            map5= 940204060
                                                                                            map6= 940204061
                                                                                            
                                                                                            if Field.GetID() == map1 :
                                                                                                print("map 1")
                                                                                                if pos.x != 1285 or pos.y != -741:
                                                                                                    Character.Teleport(1285,-741)
                                                                                                if pos.x == 1285 and pos.y == -741:
                                                                                                    Character.AMoveX(1)
                                                                                                    Character.EnterPortal()
                                                                                            
                                                                                            if Field.GetID() == map2 :
                                                                                                print("map 1")
                                                                                                if pos.x != 1285 or pos.y != -741:
                                                                                                    Character.Teleport(1285,-741)
                                                                                                if pos.x == 1285 and pos.y == -741:
                                                                                                    Character.AMoveX(1)
                                                                                                    Character.EnterPortal()
                                                                                            if Field.GetID() == map3 :
                                                                                                print("map 2)")
                                                                                                if pos.x != 1332 or pos.y != -741:
                                                                                                    Character.Teleport(1332,-741)
                                                                                                    Character.AMoveX(1)
                                                                                                if pos.x == 1332 and pos.y == -741:
                                                                                                    Character.AMoveX(-1)
                                                                                                    Character.EnterPortal()
                                                                                            if Field.GetID() == map4 :
                                                                                                print("map 2)")
                                                                                                if pos.x != 1332 or pos.y != -741:
                                                                                                    Character.Teleport(1332,-741)
                                                                                                    Character.AMoveX(1)
                                                                                                if pos.x == 1332 and pos.y == -741:
                                                                                                    Character.AMoveX(-1)
                                                                                                    Character.EnterPortal()
                                                                                            if Field.GetID() == map5 :
                                                                                                if pos.x != 1335 or pos.y != -741:
                                                                                                    Character.Teleport(1335,-741)
                                                                                                    Character.AMoveX(10)
                                                                                                if pos.x == 1335 and pos.y == -741:
                                                                                                    Character.AMoveX(-10)
                                                                                                    Character.EnterPortal()
                                                                                            if Field.GetID() == map6 :
                                                                                                print("map6")
                                                                                                if pos.x != 1335 or pos.y != -741:
                                                                                                    Character.Teleport(1335,-741)
                                                                                                    Character.AMoveX(10)
                                                                                                if pos.x == 1335 and pos.y == -741:
                                                                                                    Character.AMoveX(-10)
                                                                                                    Character.EnterPortal()
                                                                    if Field.GetID() == 450006440:
                                                                        Quest.StartQuest(34268, 3003435)
                                                                        Quest.StartQuest(34269, 3003434)
                                                                    if Field.GetID() == 940204070:
                                                                        time.sleep(60)
                                                                    if Quest.GetQuestState(34269) == 1:
                                                                        if Field.GetID() == 450006040:
                                                                            Quest.CompleteQuest(34269, 3003436)
                                                                    if Quest.GetQuestState(34269) == 2:
                                                                        if Quest.GetQuestState(34272) == 0:
                                                                            Quest.StartQuest(34272, 3003436)
                                                                        if Quest.GetQuestState(34272) == 2:
                                                                            if Quest.GetQuestState(34230) == 0:
                                                                                Terminal.Rush(450006130)
                                                                                Quest.StartQuest(34230, 3003432)
                                                                            if Quest.GetQuestState(34230) == 1:
                                                                                Quest.CompleteQuest(34230, 3003432)
                                                                            if Quest.GetQuestState(34230) == 2:
                                                                                if Quest.GetQuestState(34231) == 0:
                                                                                    Quest.StartQuest(34231, 3003432)
                                                                                if Quest.GetQuestState(34231) == 1:
                                                                                    if Quest.CheckCompleteDemand(34231, 3003432) != 0:
                                                                                        Terminal.Rush(450006150)
                                                                                        kami()
                                                                                    if Quest.CheckCompleteDemand(34231, 3003432) == 0:
                                                                                        kamioff() 
                                                                                        Terminal.Rush(450006130)
                                                                                        Quest.CompleteQuest(34231, 3003432)
                                                                                if Quest.GetQuestState(34231) == 2:
                                                                                    if Quest.GetQuestState(34232) == 0:
                                                                                        if Field.GetID() == 450006130:
                                                                                            Quest.StartQuest(34232 ,3003432)
                                                                                        if Field.GetID() == 940204310:                                            
                                                                                            mob= Field.FindMob(8644422)
                                                                                            mob1= Field.FindMob(8644420)
                                                                                            mob2= Field.FindMob(8644423)
                                                                                            mob3=Field.FindMob(8644421)
                                                                                            mob4= Field.FindMob(8644424)
                                                                                            if mob.valid :
                                                                                                kami()
                                                                                            elif mob1.valid:
                                                                                                kami()
                                                                                            elif mob2.valid:
                                                                                                kami()
                                                                                            elif mob3.valid:
                                                                                                kami()
                                                                                            elif mob4.valid:
                                                                                                kami()
                                                                                            elif not mob.valid: 
                                                                                                kamioff()
                                                                                                pos=Character.GetPos()
                                                                                                Character.Teleport(1305,-741)
                                                                                                Character.EnterPortal()
                                                                                        if Field.GetID() == 940204330:                                            
                                                                                            mob= Field.FindMob(8644422)
                                                                                            mob1= Field.FindMob(8644420)
                                                                                            mob2= Field.FindMob(8644423)
                                                                                            mob3=Field.FindMob(8644421)
                                                                                            mob4= Field.FindMob(8644424)
                                                                                            if mob.valid :
                                                                                                kami()
                                                                                            elif mob1.valid:
                                                                                                kami()
                                                                                            elif mob2.valid:
                                                                                                kami()
                                                                                            elif mob3.valid:
                                                                                                kami()
                                                                                            elif mob4.valid:
                                                                                                kami()
                                                                                            elif not mob.valid: 
                                                                                                kamioff()
                                                                                                pos=Character.GetPos()
                                                                                                Character.Teleport(1355,-741)
                                                                                                Character.EnterPortal()
                                                                                    if Quest.GetQuestState(34233) == 0:
                                                                                        if Field.GetID() == 450006130:
                                                                                            Quest.StartQuest(34233, 3003432)
                                                                                    if Quest.GetQuestState(34233) == 1:
                                                                                        Terminal.Rush(450006240)
                                                                                        Quest.CompleteQuest(34233, 3003471)
                                                                                    if Quest.GetQuestState(34233) == 2:
                                                                                        if Quest.GetQuestState(34234) == 0:
                                                                                            Quest.StartQuest(34234, 3003469)
                                                                                        if Quest.GetQuestState(34234) ==1:
                                                                                            if Quest.CheckCompleteDemand(34234,3003469) != 0:
                                                                                                kami()
                                                                                                Terminal.Rush(450006230)
                                                                                                time.sleep(15)
                                                                                                Terminal.Rush(450006300)
                                                                                                time.sleep(15)
                                                                                            if Quest.CheckCompleteDemand(34234,3003469) == 0:
                                                                                                kamioff()
                                                                                                Terminal.Rush(450006240)
                                                                                                Quest.CompleteQuest(34234,3003469)
                                                                                        if Quest.GetQuestState(34234) ==2:
                                                                                            if Quest.GetQuestState(34235) ==0:
                                                                                                print(Quest.GetQuestState(34235))
                                                                                                Terminal.Rush(450006330)
                                                                                                if Field.GetID()== 450006330:
                                                                                                    Quest.StartQuest(34235, 3003475)
                                                                                                red = Field.FindMob(8644429)
                                                                                                blue = Field.FindMob(8644428)
                                                                                                if red.valid:
                                                                                                    kami()
                                                                                                    Terminal.StopRush()
                                                                                                if blue.valid:
                                                                                                    kami()
                                                                                                    Terminal.StopRush()
                                                                                                if not red.valid:
                                                                                                    if not blue.valid:
                                                                                                        kamioff()
                                                                                                        if Field.GetID() == 940204350:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204351:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204352:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204353:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204354:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204355:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204356:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204357:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204358:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                                        if Field.GetID() == 940204359:
                                                                                                            Character.Teleport(3078,297)
                                                                                                            Character.EnterPortal()
                                                                                            if Quest.GetQuestState(34235) == 2:
                                                                                                if Quest.GetQuestState(34236) == 0:
                                                                                                    if Field.GetID() ==  450006330:
                                                                                                        Quest.StartQuest(34236, 3003475)
                                                                                                if Quest.GetQuestState(34236) == 2:
                                                                                                    if Quest.GetQuestState(34237) == 0:
                                                                                                        Terminal.Rush(450006240)
                                                                                                        Quest.StartQuest(34237, 0)
                                                                                                    if Quest.GetQuestState(34237) == 1:
                                                                                                        Terminal.Rush(450006240)
                                                                                                        Quest.CompleteQuest(34237, 3003469)
                                                                                                    if Quest.GetQuestState(34237) == 2:
                                                                                                        if Quest.GetQuestState(34238) == 0:
                                                                                                            Quest.StartQuest(34238, 3003471)
                                                                                                        if Quest.GetQuestState(34238) == 1:
                                                                                                            Quest.CompleteQuest(34238, 3003469)
                                                                                                        if Quest.GetQuestState(34238) == 2:
                                                                                                            if Quest.GetQuestState(34239) == 0:
                                                                                                                if Field.GetID() == 450006240 :
                                                                                                                    Quest.StartQuest(34239, 3003471)
                                                                                                                one=Field.FindMob(8644421)
                                                                                                                two=Field.FindMob(8644422)
                                                                                                                three=Field.FindMob(8644423)
                                                                                                                four=Field.FindMob(8644424)
                                                                                                                if one.valid:                
                                                                                                                    kami()
                                                                                                                    Terminal.StopRush()
                                                                                                                if two.valid:                
                                                                                                                    kami()
                                                                                                                    Terminal.StopRush()
                                                                                                                if three.valid:
                                                                                                                    kami()
                                                                                                                    Terminal.StopRush()
                                                                                                                if four.valid:
                                                                                                                    kami() 
                                                                                                                    Terminal.StopRush()

                                                                                                                if not one.valid:
                                                                                                                    if not two.valid:
                                                                                                                        if not three.valid:
                                                                                                                            if not four.valid:
                                                                                                                                kamioff() 
                                                                                                                                if Field.GetID() == 940204370:
                                                                                                                                    Character.Teleport(1286,-741)
                                                                                                                                    Character.EnterPortal()
                                                                                                                                if Field.GetID() == 940204390:
                                                                                                                                    Character.Teleport(1355,-741)
                                                                                                                                    Character.EnterPortal()
                                                                                                            if Quest.GetQuestState(34239) ==2:
                                                                                                                if Quest.GetQuestState(34240) == 0:                                                                        
                                                                                                                    Quest.StartQuest(34240, 3003472)  
                                                                                                                if Quest.GetQuestState(34240) == 1:
                                                                                                                    if Quest.CheckCompleteDemand(34240, 3003472) != 0:
                                                                                                                        kami()
                                                                                                                    if Quest.CheckCompleteDemand(34240, 3003472) == 0:
                                                                                                                        kamioff() 
                                                                                                                        Quest.CompleteQuest(34240, 3003472)
                                                                                                                if Quest.GetQuestState(34240) == 2:
                                                                                                                    if Quest.GetQuestState(34241) ==0:
                                                                                                                        Quest.StartQuest(34241, 3003473)  
                                                                                                                    if Quest.GetQuestState(34241) ==1:
                                                                                                                        if Quest.CheckCompleteDemand(34241, 3003473) !=0:
                                                                                                                            Terminal.Rush(450006030)
                                                                                                                            kami()
                                                                                                                        if Quest.CheckCompleteDemand(34241, 3003473) ==0:
                                                                                                                            kamioff()
                                                                                                                            Terminal.Rush(450006040)
                                                                                                                            Quest.CompleteQuest(34241,3003473)
                                                                                                                    if Quest.GetQuestState(34241) ==2:
                                                                                                                        if Quest.GetQuestState(34242) ==0:
                                                                                                                            if Field.GetID() == 450006040:
                                                                                                                                Quest.StartQuest(34242, 3003473)
                                                                                                                            erda=Field.FindMob(8644430)
                                                                                                                            if erda.valid:
                                                                                                                                kami()
                                                                                                                            if not erda.valid:
                                                                                                                                kamioff()
                                                                                                                                if Field.GetID() == 940204410:
                                                                                                                                    Character.Teleport(1286,-741)
                                                                                                                                    Character.EnterPortal()
                                                                                                                        if Quest.GetQuestState(34242) == 2:
                                                                                                                            if Quest.GetQuestState(34243) == 0:
                                                                                                                                Quest.StartQuest(34243, 3003432)
                                                                                                                            if Quest.GetQuestState(34243) == 2:
                                                                                                                                arcsymbol = Inventory.FindItemByID(1712005)
                                                                                                                                if arcsymbol.valid:
                                                                                                                                    Inventory.SendChangeSlotPositionRequest(1, arcsymbol.pos, -1604, -1)
                                                                                                                                print("you got the orb")                
                                                                                                                                                                    


            




