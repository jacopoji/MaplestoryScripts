import os, sys, Terminal, Character, time, GameState, Packet, Npc, Inventory, Field, DataType, Key, Quest, Party

if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SunCat, SCHotkey, SCLib
except:
	print("Couldn't find SunCat module")

sys.path.append('C:/Users/Jacopo/Desktop/Scripts')
import headers


#SCLib.PersistVar("KillHorntail", DoHorntail)










CaveOfLifeEntrance = 240050000
EntranceToHorntailsCave = 240050400
TheCaveOfTrialEasy1 = 240060002
TheCaveOfTrialEasy2 = 240060102
TheCaveOfTrialNormal1 = [240060005,240060000]
TheCaveOfTrialNormal2 = [240060105,240060100]
HorntailsCaveNormal = [240060200,240060205]
HorntailsCaveEasy = 240060300
ChaosHorntailsCave = [240060201,240060206]
TheCaveOfTrialChaos1 = [240060001,240060006]
TheCaveOfTrialChaos2 = [240060101,240060106]

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

def ToggleKami(indicator):
    Terminal.SetCheckBox("Kami Vac",indicator)

def ToggleHyperTeleportRock(indicator):
    Terminal.SetCheckBox("map/maprusher/hypertelerock",indicator)

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
        Character.TalkToNpc(EncryptedSlateOfTheSquad)

def LeaveHorntail():
    if KillHorntail == False and (Field.GetID() == EntranceToHorntailsCave or Field.GetID() == CaveOfLifeEntrance or Field.GetID() == CaveOfLifeEntrance1):
        ToggleKami(False)
        ToggleHyperTeleportRock(False)
        KannaSkills(False)
        if Field.GetID() == EntranceToHorntailsCave:
            Character.TalkToNpc(2083002)
        elif Field.GetID() == CaveOfLifeEntrance:
            if pos.x != -335:
                Character.Teleport(-335, 255)
            else:
                Character.EnterPortal()
        elif Field.GetID() == CaveOfLifeEntrance1:
            if pos.x != -206:
                Character.Teleport(-206, 312)
            else:
                Character.EnterPortal()

def KillHorntail(bossDifficulty):
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
        ToggleKami(False)
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
                            KannaSkills(True)
                            if pos.x != 522:
                                Character.Teleport(522, -40)
                            print("Horntails left head still alive standby")
                        else:
                            toggleFaceLeft(True)
                            ToggleKami(False)
                            KannaSkills(False)
                            if pos.x != 840:
                                Character.Teleport(840, -165)
                            else:
                                Character.EnterPortal()
                else:
                    boss = Field.FindMob(HorntailsRightHeadEasy)
                    if boss.valid:
                        ToggleKami(False)
                        KannaSkills(True)
                        if pos.x != 9:
                            Character.Teleport(9, -40)
                        print("Horntails right head still alive standby")
                    else:
                        toggleFaceLeft(False)
                        ToggleKami(False)
                        KannaSkills(False)
                        if pos.x != -307:
                            Character.Teleport(-307, -165)
                        else:
                            Character.EnterPortal()
            else:
                boss = Field.FindMob(EasyHorntail)
                if boss.valid:
                    toggleSI(True)
                    KannaSkills(True)
                    DidSpawn()
                    ToggleKami(True)
                    print("Horntail still alive Standby")
                else:
                    if HasSpawned:
                        ToggleKami(False)
                        print("Horntail Easy Is dead waiting 5 sec before continueing")
                        time.sleep(5)
                        Character.TalkToNpc(2083002)
                        time.sleep(1)
                        SCLib.UpdateVar("KillHorntail", False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                    else:
                        ToggleKami(False)
                        toggleSI(False)
                        KannaSkills(False)
                        crystal = Field.FindReactor(2401300)
                        if crystal.valid:
                            if pos.x != 540:
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
                            KannaSkills(True)
                            if pos.x != 522:
                                Character.Teleport(522, -40)
                            print("Horntails left head still alive standby")
                        else:
                            toggleFaceLeft(True)
                            ToggleKami(False)
                            KannaSkills(False)
                            if pos.x != 840:
                                Character.Teleport(840, -165)
                            else:
                                Character.EnterPortal()
                else:
                    boss = Field.FindMob(HorntailsRightHeadNormal)
                    if boss.valid:
                        ToggleKami(False)
                        KannaSkills(True)
                        if pos.x != 9:
                            Character.Teleport(9, -40)
                        print("Horntails right head still alive standby")
                    else:
                        toggleFaceLeft(False)
                        ToggleKami(False)
                        KannaSkills(False)
                        if pos.x != -307:
                            Character.Teleport(-307, -165)
                        else:
                            Character.EnterPortal()
            else:
                boss = Field.FindMob(NormalHorntail)
                if boss.valid:
                    toggleSI(True)
                    ToggleKami(True)
                    KannaSkills(True)
                    DidSpawn()
                    print("Horntail Normal still alive Standby")
                else:
                    if HasSpawned:
                        ToggleKami(False)
                        print("Horntail Normal Is dead waiting 5 sec before continueing")
                        time.sleep(5)
                        Character.TalkToNpc(2083002)
                        time.sleep(1)
                        SCLib.UpdateVar("KillHorntail", False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                    else:
                        toggleSI(False)
                        ToggleKami(False)
                        KannaSkills(False)
                        crystal = Field.FindReactor(2401000)
                        if crystal.valid:
                            if pos.x != 540:
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
                            KannaSkills(True)
                            if pos.x != 522:
                                Character.Teleport(522, -40)
                            print("Horntails left head still alive standby")
                        else:
                            toggleFaceLeft(True)
                            ToggleKami(False)
                            KannaSkills(False)
                            if pos.x != 840:
                                Character.Teleport(840, -165)
                            else:
                                Character.EnterPortal()
                else:
                    boss = Field.FindMob(ChaosHorntailsRightHead)
                    if boss.valid:
                        ToggleKami(False)
                        KannaSkills(True)
                        if pos.x != 9:
                            Character.Teleport(9, -40)
                        print("Horntails right head still alive standby")
                    else:
                        toggleFaceLeft(False)
                        ToggleKami(False)
                        KannaSkills(False)
                        if pos.x != -307:
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
                    toggleSI(True)
                    KannaSkills(True)
                    ToggleKami(True)
                    DidSpawn()
                    print("Horntail still alive, Standby")
                else:
                    if HasSpawned:
                        ToggleKami(False)
                        print("Horntail Is dead waiting 5 sec before continueing")
                        time.sleep(5)
                        Character.TalkToNpc(2083002)
                        time.sleep(1)
                        SCLib.UpdateVar("KillHorntail", False)
                        ResetSpawn()
                        ResetNowLockedFunction()
                    else:
                        toggleSI(False)
                        ToggleKami(False)
                        KannaSkills(False)
                        crystal = Field.FindReactor(2401100)
                        if crystal.valid:
                            if pos.x != 540:
                                Character.Teleport(540, 15)
                            else:
                                Character.BasicAttack()
                                time.sleep(2)