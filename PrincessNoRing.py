'''
*********************************************************************************************
**  PNOPrequest.py                                                                         **
**  PREQUESTS                                          **      
**                                              **                                              
**  Created by raech on 09/07/19.                                          **
*********************************************************************************************
'''
####################
## User Variables ##
####################
useKami = False
useFallLegit = True
useSI = False
onlyKanna = False

# God Mod Options
useGM = False
#"Full God Mode"
#"30 Sec God Mode"
#"Guard God Mode"
gmType =  "30 Sec God Mode"

# Virtual Key Codes
# http://nehe.gamedev.net/article/msdn_virtualkey_codes/15009/
# Q Key
potionKey       = 0x51
autoAttackKey   = 0x41
# A key

# Auto Pot (if you dont want to use godMode)
# 2020013 = Reinder Milk
potionID = 2020013

# Auto ATK for the Heroes
kannaID  = 80011049
ayameID  = 80011070
hayatoID = 80011036

# Mr Ali Option
useAli = False

#############################################
# if you feel some timers are a bit fast/slow, change these (seconds)
talkTime = 3
teleportTime = 1
walkTime = 1
questTime = 2
rushTime = 10
dropTime = 2
fckingCancerQuest = 30

debugMSG = False
#############################################
sendPacket = True
sendHeader = 0x42D
recvHeader = 0x528

def SendingPacket():
    for reactor in Field.GetReactors():
        if reactor.valid:
            oPacket = Packet.COutPacket(sendHeader)
            oPacket.Encode4(int(reactor.oid)) 
            Packet.SendPacket(oPacket)
            iPacket = Packet.WaitForRecv(recvHeader, 1000)

############################################################################################################################
######################################## Don't Touch Below #################################################################
############################################################################################################################

import Character
import Field
import Inventory
import Quest
import Npc
import Terminal
import time
import GameState
import Key
import Packet
import Party

def EnterPortal(pos, enter=True):
    _map = Field.GetID()
    _portal = Field.FindPortal(pos)
    _char = Character.GetPos()

    if not (_portal.x - 10 < _char.x < _portal.x + 10) or not (_portal.y - 5 < _char.y < _portal.y +5):
        Character.Teleport(_portal.x, _portal.y)
        time.sleep(teleportTime)
  
    if enter:
        Character.EnterPortal()

    time.sleep(teleportTime)

def MoveToNpc(id, limit=False):
    _npc = Field.FindNpc(id)
    _char = Character.GetPos()

    if limit:
        npcDistance = 2
    else:
        npcDistance = 500

    if not (_npc.x - npcDistance < _char.x < _npc.x + npcDistance):
        # too far i assume? test this distance
        Character.Teleport(_npc.x, _npc.y)
        time.sleep(teleportTime)
  
    time.sleep(teleportTime)

def QuestCompleted(id):
    if Quest.GetQuestState(id) != 2:
        return False
    else:
        return True

def QuestStage(id):
    if Quest.GetQuestState(id) == 1:
        return 1
    elif Quest.GetQuestState(id) == 0:
        return -1
    else:
        print("something wrong with ", id)
        return 0

def QuestInProgress(quest, npc):
    if Quest.CheckCompleteDemand(quest, npc) != 0:
        return True
    else:
        return False

def StartingQuest(quest, npc):
    if QuestStage(quest) < 0:
        _npc = Field.FindNpc(npc)
        if _npc.valid:
            MoveToNpc(npc)
      
        if debugMSG:
            print("Started Quest: ", quest)
        Quest.StartQuest(quest, npc)
        time.sleep(questTime)

def CompletingQuest(quest, npc, map):
    if not QuestCompleted(quest):
        _map = Field.GetID()
        _npc = Field.FindNpc(npc)
        if _map != map:
            #Terminal.Rush(map)
            #time.sleep(rushTime)
            if debugMSG:
                print("wrongmap")
        else:
            if _npc.valid:
                MoveToNpc(npc)
            if debugMSG:
                print("Completed Quest: ", quest)
            Quest.CompleteQuest(quest, npc)
            time.sleep(questTime)

# Terminal Toggles
def TerminalATK(flag, quest=False):
    if not quest:
        if useSI:
            Terminal.SetCheckBox("Skill Injection", flag)
        else:
            Terminal.SetCheckBox("Auto Attack", flag)
    else:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("General FMA", False)
        Terminal.SetCheckBox("Full Map Attack", False)
        Terminal.SetCheckBox("Melee No Delay", False)
        Terminal.SetCheckBox("Auto Attack", flag)

    if useKami:
        Terminal.SetCheckBox("Kami Vac", flag)
    elif useFallLegit:
        Terminal.SetCheckBox("Legit Vac", flag)
        Terminal.SetCheckBox("Mob Falldown", flag)
        if flag:
            _left  = Field.GetRect().left
            _right = Field.GetRect().right
            _mid = (_left + _right) / 2
            if not (_mid -10 < Character.GetPos().x < _mid + 10):
                Character.AMoveX(int(_mid))
                time.sleep(walkTime)

# Prequest
# Hieizan Temple -> Regards, Takeda Shingen
def CheckQuestMap(mapid, forward=True):
    TerminalATK(False)
    _map = Field.GetID()
    momijigaoka = 807000000
    fieldmap1 = 811000001
    fieldmap2 = 811000004
    fieldmap3 = 811000006
  
    if _map != mapid and forward:
        if _map != momijigaoka and (_map < 811000000 or _map > 811000010):
            print("Moving to Momijigaoka")
            Terminal.Rush(momijigaoka)
        elif _map == momijigaoka:
            Terminal.StopRush()
            EnterPortal("west00")
        elif _map == fieldmap1:
            Terminal.StopRush()
            EnterPortal("out02")
        elif _map == fieldmap2:
            Terminal.StopRush()
            EnterPortal("out01")
        elif _map == fieldmap2+1:
            Terminal.StopRush()
            EnterPortal("out01")
  
    elif _map != mapid and not forward:
        if _map != momijigaoka and (_map < 811000000 or _map > 811000010):
            print("Moving to Momijigaoka")
            Terminal.Rush(momijigaoka)
        elif _map == fieldmap1:
            Terminal.StopRush()
            EnterPortal("out00")
        elif _map == fieldmap2:
            Terminal.StopRush()
            EnterPortal("out00")
        elif _map == fieldmap2+1:
            Terminal.StopRush()
            EnterPortal("out00")
        elif _map == fieldmap3:
            Terminal.StopRush()
            EnterPortal("out00")
  
def Hieizan(_map):
    takeda = 9130102
    mouri = 9130008
    ayame = 9130103
    sakuno = 9130104

    momijigaoka = 807000000

    q1 = 58901
    q2 = q1 + 1
    q3 = q2 + 1
    q4 = q3 + 4
    q5 = q4 + 1
    q6 = q5 + 1
    q7 = q6 + 1
    q8 = q7 + 1
    q9 = q8 + 2

    if not QuestCompleted(q1):
        TerminalATK(False)
        mapid = 811000001
        CheckQuestMap(mapid)
        StartingQuest(q1, takeda)
        CompletingQuest(q1, takeda, mapid)
  
    if not QuestCompleted(q2) and QuestCompleted(q1):
        mapid = 811000001
        CheckQuestMap(mapid)
        StartingQuest(q2, takeda)
        itemid = 4034126
        if QuestInProgress(q2, takeda): # and Inventory.GetItemCount(itemid) < 30:
            TerminalATK(True)
        else:
            TerminalATK(False)
            CompletingQuest(q2, takeda, mapid)

    if not QuestCompleted(q3) and QuestCompleted(q2):
        itemid = 4009286
        StartingQuest(q3, takeda)
        if QuestInProgress(q3, takeda):
            if Inventory.GetItemCount(itemid) < 20:
                mapid = 811000004
                CheckQuestMap(mapid)
                TerminalATK(True)
            else:
                mapid = 811000006
                TerminalATK(False)
                CheckQuestMap(mapid)
                if _map == mapid:
                    if (Character.GetPos().x != -8) and Character.GetPos().y != -628:
                        Character.Teleport(-8, -628)
                        time.sleep(teleportTime)
                    else:
                        questItem = Inventory.FindItemByID(itemid)
                        if questItem.valid:
                            TerminalATK(False)
                            for x in range(20):
                                Inventory.SendChangeSlotPositionRequest(4, questItem.pos, 0, 1)
                                time.sleep(dropTime)
                                SendingPacket()
                                if not QuestInProgress(q3, takeda):
                                    break;
                            mapid = 811000001
                            CheckQuestMap(mapid, False)
        else:
            mapid = 811000001
            herbid = 4034128
            if Inventory.GetItemCount(herbid) > 0:
                CheckQuestMap(mapid, False)
            else:
                CheckQuestMap(mapid)
            StartingQuest(q3, takeda)
            CompletingQuest(q3, takeda, mapid)

    if not QuestCompleted(q4) and QuestCompleted(q3):
        mapid = 811000001
        if _map > mapid:
            CheckQuestMap(mapid, False)
        StartingQuest(q4, takeda)
        time.sleep(questTime)
        CheckQuestMap(momijigaoka, False)
        CompletingQuest(q4, mouri, momijigaoka)
    elif QuestCompleted(q4):
        if _map == momijigaoka:
            EnterPortal("west00")

    if not QuestCompleted(q5) and QuestCompleted(q4):
        StartingQuest(q5, ayame)

    if not QuestCompleted(q6) and QuestCompleted(q5):
        StartingQuest(q6, sakuno)

    if not QuestCompleted(q7) and QuestCompleted(q6):
        StartingQuest(q7, ayame)

    if not QuestCompleted(q8) and QuestCompleted(q7):
        StartingQuest(q8, ayame)
        CompletingQuest(q8, ayame, _map)

    if not QuestCompleted(q9) and QuestCompleted(q8):
        StartingQuest(q9, ayame)

def CheckInstanceMap(mapid, dir, forward=True):
    _map = Field.GetID()
    entrance = 811000014
    field1 = 811000098
    field2 = 811000097
    down1 = 811000015
    down2 = down1 + 1
    down3 = down2 + 1
    well1 = down3 + 1

    templeEntrance = 811000019
    boss1 = 811000020

    nBossEntry  = 811000025
    nBoss1      = nBossEntry + 1
    nBoss2      = nBoss1 + 1
    nBoss3      = nBoss2 + 2

    lastBossEntry = nBossEntry + 3

    if _map != mapid:
        if dir != "momi":
            Terminal.StopRush()

        if forward:
            if _map == entrance and dir == "up":
                EnterPortal("out01")
            if _map == field1 and dir == "up":
                EnterPortal("out01")
            if _map == entrance and dir == "down":
                EnterPortal("out02")
            if _map == down1 and dir == "down":
                EnterPortal("out01")
            if _map == down2 and dir == "down":
                EnterPortal("out01")
            if _map == down3 and dir == "down":
                EnterPortal("out01")
            if _map == templeEntrance and dir == "mid":
                EnterPortal("in00")
            if _map == entrance and dir == "right":
                EnterPortal("out02")
            if _map == down1 and dir == "right":
                EnterPortal("out01")
            if _map == down2 and dir == "right":
                EnterPortal("out01")
            if _map == down3 and dir == "right":
                EnterPortal("out01")
            if _map == templeEntrance-1 and dir == "right":
                EnterPortal("out01")
            if _map == templeEntrance and dir == "right":
                EnterPortal("out01")
            if _map == templeEntrance+1 and dir == "right":
                EnterPortal("out01")
            if _map == boss1+1 and dir == "right":
                EnterPortal("out01")
            if _map == nBossEntry and dir == "right":
                EnterPortal("out01")
            if _map == lastBossEntry and dir == "right":
                EnterPortal("in00")
        else:
            if _map == field1 and dir == "up":
                EnterPortal("out00")
            if _map == field2 and dir == "up":
                EnterPortal("out00")
            if _map == down1 and dir == "down":
                EnterPortal("out00")
            if _map == down2 and dir == "down":
                EnterPortal("out00")
            if _map == down3 and dir == "down":
                EnterPortal("out00")
            if _map == boss1 and dir == "mid":
                EnterPortal("out00")
            if _map == nBoss3 and dir == "mid2":
                EnterPortal("out00")
            if _map == nBoss2 and dir == "mid2":
                EnterPortal("out00")
            if _map == nBoss1 and dir == "mid2":
                EnterPortal("out00")

  

# Kanna Ring
def KannaRing(_map, hero):
    dcMap = 811000013
    momijigaoka = 807000000
    childMap = 811000014
    ayameMap = 811000008

    child = 9130107
    child2 = child + 1
    ayame = 9130103
    princess = 9130116
    gourdid = 2432732
    qAyame = 58916

    if hero == "kanna":
        q1 = 58941
        q2 = q1 + 1
        q3 = q2 + 1
        q4 = q3 + 1
        q5 = q4 + 1
        q6 = q5 + 1
        q7 = q6 + 1
        q8 = 58963
        q9 = q8 + 1
        q10 = 58965
        q11 = q10 + 1
        q12 = q11 + 1
        q13 = q12 + 1
    elif hero == "hayato":
        q1 = 58928
        q2 = q1 + 1
        q3 = q2 + 1
        q4 = q3 + 1
        q5 = q4 + 1
        q6 = q5 + 1
        q7 = q6 + 1
        q8 = q7 + 1
        q9 = q8 + 1
        q10 = 58937
        q11 = q10 + 1
        q12 = q11 + 1
        q13 = q12 + 1
    elif hero == "ayameHero":
        q1 = 58914
        q2 = 58915
        q3 = 58917
        q4 = 58918
        q5 = 58919
        q6 = 58920
        q7 = q6 + 1
        q8 = q7 + 1
        q9 = q8 + 1
        q10 = q9 + 1
        q11 = q10 + 1
        q12 = q11 + 1
        q13 = q12 + 1


    if _map == momijigaoka:
        TerminalATK(False, True)
        EnterPortal("west00")
    elif _map == dcMap:
        TerminalATK(False, True)
        EnterPortal("out00")
    elif _map == ayameMap:
        TerminalATK(False, True)
        gourd = Inventory.FindItemByID(gourdid)
        if not gourd.valid:
            MoveToNpc(ayame)
            Npc.ClearSelection()
            time.sleep(talkTime)
            #Character.TalkToNpc(ayame)
            time.sleep(talkTime)
            Npc.RegisterSelection('Talk to Ayame.')
            time.sleep(talkTime)
            Character.TalkToNpc(ayame)
            #Npc.RegisterSelection('Metamorph')
            Npc.RegisterSelection('Receive another Metamorph Potion')
            time.sleep(talkTime)
        else:
            Npc.ClearSelection()
            Inventory.UseItem(gourdid)
            if hero == "kanna":
                Npc.RegisterSelection('Kanna')
            if hero == "hayato":
                Npc.RegisterSelection('Hayato')
            if hero == "ayameHero":
                Npc.RegisterSelection('Ayame')
    elif _map == 811000099:
        #bug might be here
        bugQuest = 58913
        if QuestStage(bugQuest) < 0:
            print('hi')
            StartingQuest(bugQuest, ayame)
        else:
            TerminalATK(False, True)
            print("setting up skills")
            if useGM:
                Terminal.SetCheckBox(gmType, True)
            if not useAli and not useGM:
                Key.Set(potionKey, 2, potionID)
            time.sleep(teleportTime)
            if hero == "hayato":
                Key.Set(autoAttackKey, 1, hayatoID)
            if hero == "kanna":
                Key.Set(autoAttackKey, 1, kannaID)
            if hero == "ayameHero":
                Key.Set(autoAttackKey, 1, ayameID)
            time.sleep(teleportTime)
            EnterPortal("out00")
    else:
        if not QuestCompleted(q1):
            mapid = 811000098
            StartingQuest(q1, child)
            if QuestInProgress(q1, child):
                if Character.GetPos().x != 91:
                    Character.Teleport(91, 62)
                    time.sleep(teleportTime)
                else:
                    if sendPacket:
                        print("sending packet")
                        SendingPacket()

            else:
                CompletingQuest(q1, child, childMap)

        if not QuestCompleted(q2) and QuestCompleted(q1):
            if hero == "ayameHero" and QuestCompleted(q2):
                if debugMSG:
                    print('we should be fcking done hre')
            else:
                if not QuestCompleted(q2) and not QuestCompleted(qAyame):
                    StartingQuest(q2, child)
                if hero == "ayameHero" and not QuestCompleted(qAyame):
                    #StartingQuest(q2, child)
                    StartingQuest(qAyame, child)
                    if QuestInProgress(qAyame,  child):
                        mapid = 811000098
                        if _map != mapid:
                            CheckInstanceMap(mapid, "up")
                        else:
                            TerminalATK(True, True)
                    else:
                        mapid = childMap
                        TerminalATK(False, True)
                        CheckInstanceMap(childMap, "up", False)
                        if _map == childMap:
                            CompletingQuest(qAyame, child, _map)
                else:
                    if QuestInProgress(q2, child) and hero != "ayameHero":
                        mapid = 811000098
                        if _map != mapid:
                            CheckInstanceMap(mapid, "up")
                        else:
                            TerminalATK(True, True)
                    else:
                        if hero != "ayameHero":
                            TerminalATK(False, True)
                            CheckInstanceMap(childMap, "up", False)
                            if _map == childMap:
                                CompletingQuest(q2, child, childMap)

        if hero == "ayameHero":
            q2 = qAyame
        if not QuestCompleted(q3) and QuestCompleted(q2):
            StartingQuest(q3, child)
            if QuestInProgress(q3, child):
                mapid = 811000098
                if _map != mapid:
                    CheckInstanceMap(mapid, "up")
                else:
                    TerminalATK(True, True)
            else:
                TerminalATK(False, True)
                CheckInstanceMap(childMap, "up", False)
                CompletingQuest(q3, child, childMap)

        if not QuestCompleted(q4) and QuestCompleted(q3):
            StartingQuest(q4, child)
            if QuestInProgress(q4, child):
                mapid = 811000015
                if _map != mapid:
                    CheckInstanceMap(mapid, "down")
                else:
                    TerminalATK(True, True)
            else:
                TerminalATK(False, True)
                CheckInstanceMap(childMap, "down", False)
                CompletingQuest(q4, child, childMap)

        if not QuestCompleted(q5) and QuestCompleted(q4) and QuestCompleted(q3):
            StartingQuest(q5, child)
            if QuestInProgress(q5, child):
                mapid = 811000016
                if _map != mapid:
                    CheckInstanceMap(mapid, "down")
                else:
                    TerminalATK(True, True)
            else:
                TerminalATK(False, True)
                CheckInstanceMap(childMap, "down", False)
                CompletingQuest(q5, child, childMap)

        if not QuestCompleted(q6) and QuestCompleted(q5):
            StartingQuest(q6, child)
            if QuestInProgress(q6, child):
                mapid = 811000017
                if _map != mapid:
                    CheckInstanceMap(mapid, "down")
                else:
                    TerminalATK(True, True)
            else:
                TerminalATK(False, True)
                CheckInstanceMap(childMap, "down", False)
                CompletingQuest(q6, child, childMap)

        if not QuestCompleted(q7) and QuestCompleted(q6):
            TerminalATK(False, True)
            StartingQuest(q7, child)
            if QuestInProgress(q7, child):
                mapid = 811000018
                CheckInstanceMap(mapid, "down")
                CompletingQuest(q7, child2, mapid)

        if not QuestCompleted(q8) and QuestCompleted(q7):
            StartingQuest(q8, child2)
            if QuestInProgress(q8, child2):
                mapid = 811000018
                CheckInstanceMap(mapid, "down")
                if _map == mapid:
                    if Character.GetPos().x != 87:
                        Character.Teleport(87, 62)
                    else:
                        if sendPacket:
                            print("sending packet")
                            SendingPacket()

        if not QuestCompleted(q9) and QuestCompleted(q8):
            if Party.IsInParty():
                Party.LeaveParty()
            mapid = 811000020
            StartingQuest(q9, 0)
            if QuestInProgress(q9, 0):
                CheckInstanceMap(mapid, "mid")
                if _map == mapid:
                    if len(Field.GetMobs()) > 0:
                        TerminalATK(True, True)
                    else:
                        TerminalATK(False, True)
            else:
                CompletingQuest(q9, 0, mapid)
                CheckInstanceMap(mapid-1, "mid", False)

        if not QuestCompleted(q10) and QuestCompleted(q9):
            mapid = 811000021
            StartingQuest(q10, 0)
            StartingQuest(58950, 0) # extra quest somehow
            if QuestInProgress(q10, 0):
                CheckInstanceMap(mapid, "right")
      
        if not QuestCompleted(q11) and QuestCompleted(q10):
            mapid = 811000025
            StartingQuest(q11, 0)
            if QuestInProgress(q11, 0):
                CheckInstanceMap(mapid, "right")
                if len(Field.GetMobs()) > 0:
                    TerminalATK(True, True)
                else:
                    TerminalATK(False, True)
            else:
                CompletingQuest(q11, 0, mapid)

        if not QuestCompleted(q12) and QuestCompleted(q11):
            mapid = 811000025
            boss1 = mapid + 1
            boss2 = boss1 + 1
            boss3 = boss2 + 2
            if _map == mapid:
                EnterPortal("in00")
            elif _map == boss1:
                if len(Field.GetMobs()) > 0:
                    TerminalATK(True, True)
                else:
                    TerminalATK(False, True)
                    EnterPortal("next00")
            elif _map == boss2:
                if len(Field.GetMobs()) > 0:
                    TerminalATK(True, True)
                else:
                    TerminalATK(False, False)
                    EnterPortal("next00")
            elif _map == boss3:
                StartingQuest(q12, princess)

        if not QuestCompleted(q13) and QuestCompleted(q12):
            mapid = 811000025
            lastTemp = 811000028
            lastDest = 811000033
            StartingQuest(q13, 0)
            if QuestInProgress(q13, 0):
                if _map != mapid and _map != lastTemp and _map != lastDest:
                    CheckInstanceMap(mapid, "mid2", False)
                if (_map == mapid or _map == lastTemp) and _map != lastDest:
                    CheckInstanceMap(lastDest, "right")
                if _map == lastDest:
                    if len(Field.GetMobs()) > 0:
                        TerminalATK(True, True)
                    else:
                        TerminalATK(False, True)
            else:
                TerminalATK(False, True)
                if _map == lastDest and Character.GetPos().x != -147:
                    Character.Teleport(-147, -195)
                    time.sleep(teleportTime)
                else:
                    if _map != lastDest:
                        CheckInstanceMap(lastDest, "right")
                    else:
                        if sendPacket:
                            print("sending packet")
                            SendingPacket()

                        CompletingQuest(q13, 0, lastDest)


# Main Loop
def Main():
    if GameState.IsInGame() and not Terminal.IsRushing() and not Terminal.IsSolvingRune():
        hieizanLastQuest = 58913
        ayame = 9130103
        princess = ayame + 1
      
        kannaring = 1113155
        hayatoshoulder = 1152171
        ayametreasure = 1132275

        _map = Field.GetID()
        if not QuestCompleted(hieizanLastQuest-2) and QuestInProgress(hieizanLastQuest, ayame):
            Hieizan(_map)
        else:
            if onlyKanna:
                if Inventory.GetItemCount(kannaring) == 0:
                    KannaRing(_map, "kanna")
                else:
                    print('we are done')
            else:
                if Inventory.GetItemCount(kannaring) > 0 and Inventory.GetItemCount(hayatoshoulder) == 0:
                    KannaRing(_map, "hayato")
                elif Inventory.GetItemCount(kannaring) > 0 and Inventory.GetItemCount(hayatoshoulder) > 0 and Inventory.GetItemCount(ayametreasure) == 0:
                    KannaRing(_map, "ayameHero")
                elif Inventory.GetItemCount(kannaring) == 0:
                    KannaRing(_map, "kanna")
                else:
                    # pno quest line
                    if Inventory.GetItemCount(4034142) > 0:
                        if not QuestCompleted(hieizanLastQuest):
                            CompletingQuest(hieizanLastQuest, ayame, _map)
                        else:
                            if not QuestCompleted(58950):
                                CompletingQuest(58950, princess, _map)
                    print("we're done here")


Main()