import os, sys, Terminal, Character, time, GameState, Npc, Field, Quest, Party

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")

from AioAttackSettings import *
job = Character.GetJob()

#SCLib.PersistVar("KillHorntail", DoHorntail)


TheCaveOfTrialEasy1 = 240060002
TheCaveOfTrialEasy2 = 240060102
TheCaveOfTrialNormal1 = [240060005,240060000]
TheCaveOfTrialNormal2 = [240060105,240060100]
HorntailsCaveNormal = [240060200,240060205]
HorntailsCaveEasy = 240060300
ChaosHorntailsCave = [x for x in range(240060201,240060230)]
TheCaveOfTrialChaos1 = [x for x in range(240060001,240060030)]
TheCaveOfTrialChaos2 = [x for x in range(240060101,240060130)] 
CaveOfLifeEntrance = 240050000
EntranceToHorntailsCave = 240050400
CaveOfLifeEntrance1 = 240040700
PeakOfTheBigNest = 240040600

HorntailsLeftHeadEasy = 8810200
HorntailsRightHeadEasy = 8810201
HorntailsLeftHeadNormal = 8810000
HorntailsRightHeadNormal = 8810001
NormalHorntail = 8810018
EasyHorntail = 8810214
ChaosHorntail = 8810118
ChaosHorntail1 = 8810119
ChaosHorntail2 = 8810120
ChaosHorntail3 = 8810121
ChaosHorntail4 = 8810122
ChaosHorntailsLeftHead = 8810100
ChaosHorntailsRightHead = 8810101
EncryptedSlateOfTheSquad = 2083000

def ToggleKami(indicator):
    Terminal.SetCheckBox("Kami Vac",indicator)

def ToggleHyperTeleportRock(indicator):
    Terminal.SetCheckBox("map/maprusher/hypertelerock",indicator)

def ToggleFaceLeft(indicator):
    Terminal.SetCheckBox("flacc",indicator)

def GotoHorntail():
    ToggleKami(False)
    ToggleHyperTeleportRock(True)
    print("Going to Horntail")
    if Field.GetID() != CaveOfLifeEntrance:
        if Field.GetID() != PeakOfTheBigNest:
            Terminal.Rush(PeakOfTheBigNest)
        else:
            ToggleHyperTeleportRock(False)
            time.sleep(0.5)
            Terminal.Rush(CaveOfLifeEntrance)
    else:
        Party.CreateParty()
        Npc.ClearSelection()
        Character.TalkToNpc(2083000)

def LeaveHorntail():
    if (Field.GetID() == EntranceToHorntailsCave or Field.GetID() == CaveOfLifeEntrance or Field.GetID() == CaveOfLifeEntrance1):
        ToggleKami(False)
        ToggleHyperTeleportRock(False)
        
        if Field.GetID() == EntranceToHorntailsCave:
            Character.TalkToNpc(2083002)
        elif Field.GetID() == CaveOfLifeEntrance:
            if Character.GetPos().x != -335:
                Character.Teleport(-335, 255)
            else:
                Character.EnterPortal()
        elif Field.GetID() == CaveOfLifeEntrance1:
            if Character.GetPos().x != -206:
                Character.Teleport(-206, 312)
            else:
                Character.EnterPortal()

def ToggleLoot(indicator):
    Terminal.SetCheckBox("Kami Loot",indicator)
    Terminal.SetCheckBox("Auto Loot",indicator)

def MoveToXLocation(xPos):
    while Character.GetPos().x not in range(xPos-60,xPos+60):
        Character.AMoveX(xPos)

def ResetNowLockedFunction():
    SCLib.UpdateVar("NowLockedVar", False)
def NowLockedFunction():
    SCLib.UpdateVar("NowLockedVar", True)
def DidSpawn():
    SCLib.UpdateVar("HasSpawned", True)
def ResetSpawn():
    SCLib.UpdateVar("HasSpawned", False)

def KillHorntail(bossDifficulty):
    
    SCLib.PersistVar("HasSpawned", False)
    SCLib.PersistVar("NowLockedVar", False)
    HasSpawned = SCLib.GetVar("HasSpawned")
    NowLockedVar = SCLib.GetVar("NowLockedVar")
    SCLib.StartVars()
    if bossDifficulty == 0:
        HorntailEasy = True
        HorntailNormal = False
        HorntailChaos = False
    elif bossDifficulty == 1:
        HorntailEasy = False
        HorntailNormal = True
        HorntailChaos = False
    else:
        HorntailEasy = False
        HorntailNormal = False
        HorntailChaos = True

    HorntailPreQuest = Quest.GetQuestState(7313)
    if HorntailPreQuest == 0:
        print("Horntail Prequest not started or done, Starting quest before entery")
        if Field.GetID() != CaveOfLifeEntrance1:
            Terminal.Rush(CaveOfLifeEntrance1)
        else:
            Quest.StartQuest(7313, 2081006)
            print("Horntail Prequest started")
    else:
        #ToggleKami(False)
        print("Doing Horntail")
        if HorntailEasy:
            print("Easy")
            if Field.GetID() != HorntailsCaveEasy:
                if Field.GetID() != TheCaveOfTrialEasy2:
                    if Field.GetID() != TheCaveOfTrialEasy1:
                        if Field.GetID() != EntranceToHorntailsCave:
                            GotoHorntail()
                        else:
                            if not NowLockedVar:
                                Npc.ClearSelection()
                                Npc.RegisterSelection("Easy Mode (Level 130 or above)")
                                time.sleep(1)
                                Character.TalkToNpc(2083004)
                                time.sleep(1)
                            else:
                                print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                                SCLib.UpdateVar("KillHorntail", False)
                                ResetNowLockedFunction()
                    else:
                        NowLockedFunction()
                        boss = Field.FindMob(HorntailsLeftHeadEasy)
                        if boss.valid:
                            ToggleKami(False)
                            
                            if Character.GetPos().x != 522:
                                Character.Teleport(522, -40)
                            print("Horntails left head still alive standby")
                        else:
                            ToggleFaceLeft(True)
                            ToggleKami(False)
                            
                            if Character.GetPos().x != 840:
                                Character.Teleport(840, -165)
                            else:
                                Character.EnterPortal()
                else:
                    boss = Field.FindMob(HorntailsRightHeadEasy)
                    if boss.valid:
                        ToggleKami(False)
                        ToggleAttack(True)
                        if Character.GetPos().x != 9:
                            Character.Teleport(9, -40)
                        print("Horntails right head still alive standby")
                    else:
                        ToggleFaceLeft(False)
                        ToggleKami(False)
                        
                        if Character.GetPos().x != -307:
                            Character.Teleport(-307, -165)
                        else:
                            Character.EnterPortal()
            else:
                boss = Field.FindMob(EasyHorntail)
                if boss.valid:
                    ToggleAttack(True)
                    
                    DidSpawn()
                    ToggleKami(True)
                    print("Horntail still alive Standby")
                else:
                    if HasSpawned:
                        ToggleKami(False)
                        ToggleLoot(True)
                        print("Horntail Easy Is dead waiting 10 sec before continueing")
                        time.sleep(10)
                        Character.TalkToNpc(2083002)
                        time.sleep(1)
                        SCLib.UpdateVar("KillHorntail", False)
                        ToggleLoot(False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                    else:
                        ToggleKami(False)
                        ToggleAttack(False)
                        
                        crystal = Field.FindReactor(2401300)
                        if crystal.valid:
                            if Character.GetPos().x != 540:
                                Character.Teleport(540, 15)
                            else:
                                Character.BasicAttack()
                                time.sleep(2)			
        elif HorntailNormal:
            print("Normal")
            if Field.GetID() not in HorntailsCaveNormal:
                if Field.GetID() not in TheCaveOfTrialNormal2:
                    if Field.GetID() not in TheCaveOfTrialNormal1:
                        if Field.GetID() != EntranceToHorntailsCave:
                            GotoHorntail()
                        else:
                            if not NowLockedVar:
                                Npc.ClearSelection()
                                Npc.RegisterSelection("Normal Mode (Level 130 or above)")
                                time.sleep(1)
                                Character.TalkToNpc(2083004)
                                time.sleep(1)
                            else:
                                print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                                SCLib.UpdateVar("KillHorntail", False)
                                ResetNowLockedFunction()
                    else:
                        NowLockedFunction()
                        boss = Field.FindMob(HorntailsLeftHeadNormal)
                        if boss.valid:
                            ToggleKami(False)
                            ToggleAttack(True)
                            if Character.GetPos().x != 522:
                                Character.Teleport(522, -40)
                            print("Horntails left head still alive standby")
                        else:
                            ToggleFaceLeft(True)
                            ToggleKami(False)
                            
                            if Character.GetPos().x != 840:
                                Character.Teleport(840, -165)
                            else:
                                Character.EnterPortal()
                else:
                    boss = Field.FindMob(HorntailsRightHeadNormal)
                    if boss.valid:
                        ToggleKami(False)
                        
                        if Character.GetPos().x != 9:
                            Character.Teleport(9, -40)
                        print("Horntails right head still alive standby")
                    else:
                        ToggleFaceLeft(False)
                        ToggleKami(False)
                        
                        if Character.GetPos().x != -307:
                            Character.Teleport(-307, -165)
                        else:
                            Character.EnterPortal()
            else:
                boss = Field.FindMob(NormalHorntail)
                if boss.valid:
                    ToggleAttack(True)
                    ToggleKami(True)
                    
                    DidSpawn()
                    print("Horntail Normal still alive Standby")
                else:
                    if HasSpawned:
                        ToggleKami(False)
                        ToggleLoot(True)
                        print("Horntail Normal Is dead waiting 10 sec before continueing")
                        time.sleep(10)
                        Character.TalkToNpc(2083002)
                        time.sleep(1)
                        ToggleLoot(False)
                        SCLib.UpdateVar("KillHorntail", False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                    else:
                        ToggleAttack(False)
                        ToggleKami(False)
                        
                        crystal = Field.FindReactor(2401000)
                        if crystal.valid:
                            if Character.GetPos().x != 540:
                                Character.Teleport(540, 15)
                            else:
                                Character.BasicAttack()
                                time.sleep(2)
        elif HorntailChaos:
            print("Chaos")
            if Field.GetID() not in ChaosHorntailsCave:
                if Field.GetID() not in TheCaveOfTrialChaos2:
                    if Field.GetID() not in TheCaveOfTrialChaos1:
                        if Field.GetID() != EntranceToHorntailsCave:
                            GotoHorntail()
                        else:
                            if not NowLockedVar:
                                Npc.ClearSelection()
                                Npc.RegisterSelection("Chaos Mode (Level 135 or above)")
                                time.sleep(1)
                                Character.TalkToNpc(2083004)
                                time.sleep(1)
                            else:
                                print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                                SCLib.UpdateVar("KillHorntail", False)
                                ResetNowLockedFunction()
                    else:
                        NowLockedFunction()
                        boss = Field.FindMob(ChaosHorntailsLeftHead)
                        if boss.valid:
                            ToggleKami(False)
                            ToggleAttack(True)
                            while Character.GetPos().x not in range(500,570):
                                Character.AMoveX(522)
                            print("Horntails left head still alive standby")
                        else:
                            ToggleFaceLeft(True)
                            ToggleKami(False)
                            
                            if Character.GetPos().x != 840:
                                Character.Teleport(840, -165)
                            else:
                                Character.EnterPortal()
                else:
                    boss = Field.FindMob(ChaosHorntailsRightHead)
                    if boss.valid:
                        ToggleKami(False)
                        ToggleAttack(True)
                        while Character.GetPos().x not in range(-40,40):
                            Character.AMoveX(9)
                        print("Horntails right head still alive standby")
                    else:
                        ToggleFaceLeft(False)
                        ToggleKami(False)
                        
                        if Character.GetPos().x != -307:
                            Character.Teleport(-307, -165)
                        else:
                            Character.EnterPortal()
            else:
                boss = Field.FindMob(ChaosHorntail)
                boss1 = Field.FindMob(ChaosHorntail1)
                boss2 = Field.FindMob(ChaosHorntail2)
                boss3 = Field.FindMob(ChaosHorntail3)
                boss4 = Field.FindMob(ChaosHorntail4)
                if boss.valid or boss1.valid or boss2.valid or boss3.valid or boss4.valid:
                    ToggleAttack(True)
                    
                    #ToggleKami(True)
                    DidSpawn()
                    while Character.GetPos().x not in range(140,220):
                        Character.AMoveX(183)
                    print("Horntail still alive, Standby")
                else:
                    if HasSpawned:
                        ToggleKami(False)
                        ToggleLoot(False)
                        #print("Horntail Is dead waiting 10 sec before continueing")
                        print("Looting")
                        Terminal.SetCheckBox("Auto Loot",True)
                        MoveToXLocation(Field.GetRect().left)
                        time.sleep(1.5)
                        MoveToXLocation(Field.GetRect().right)
                        time.sleep(1.5)
                        MoveToXLocation(Field.GetRect().left)
                        time.sleep(1.5)
                        MoveToXLocation(Field.GetRect().right)
                        time.sleep(1.5)
                        MoveToXLocation(Field.GetRect().left)
                        time.sleep(1.5)
                        #time.sleep(10)
                        Character.TalkToNpc(2083002)
                        time.sleep(1)
                        SCLib.UpdateVar("KillHorntail", False)
                        ToggleLoot(False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                    else:
                        ToggleAttack(False)
                        ToggleKami(False)
                        
                        crystal = Field.FindReactor(2401100)
                        if crystal.valid:
                            if Character.GetPos().x != 540:
                                Character.Teleport(540, 15)
                            else:
                                Character.BasicAttack()
                                time.sleep(2)

if GameState.IsInGame():
    KillHorntail(2)