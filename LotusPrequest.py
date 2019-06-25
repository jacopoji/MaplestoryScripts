import os
import sys
import Packet
import Character
import GameState
import Field
import time
import Npc
import Terminal
import Key
import Quest
import functools

print = functools.partial(print, flush=True, end="\n")
# Auto Lotus Act5+6
# Author: Comicals

UseKami = True
UseSI = True


############################################
def SetAttack(toggle=True, kami=True):
    if toggle:
        if UseKami and kami:
            CheckBox("Kami Vac", True)
        else:
            CheckBox("Kami Vac", False)

        if UseSI:
            CheckBox("Skill Injection", True)
        else:
            CheckBox("Skill Injection", False)
            CheckBox("MonkeySpiritsNDcheck", False)
            CheckBox("Auto Attack", True)
    else:
        CheckBox("Kami Vac", False)
        CheckBox("Auto Attack", False)
        CheckBox("Skill Injection", False)


def ToPortal(portal, enter=True):
    map = Field.GetID()
    portal = Field.FindPortal(portal)
    if portal.valid:
        AAFlag = False
        kamiFlag = False
        if Terminal.GetCheckBox("Auto Attack"):
            AAFlag = True
            CheckBox("Auto Attack", False)
        if Terminal.GetCheckBox("Kami Vac"):
            kamiFlag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)

        if not (Character.GetPos().x < portal.x + 5 and Character.GetPos().x > portal.x - 5):
            Character.Teleport(portal.x, portal.y - 20)
            time.sleep(1)

        attempt = 0
        while enter and Field.GetID() == map and attempt < 3:
            attempt += 1
            Character.EnterPortal()
            time.sleep(1)

        if AAFlag:
            CheckBox("Auto Attack", True)
        if kamiFlag:
            CheckBox("Kami Vac", True)


def Teleport(x, y):
    CheckBox("Kami Vac", False)
    time.sleep(1)
    if not (Character.GetPos().x < x + 5 and Character.GetPos().x > x - 5):
        Character.Teleport(x, y - 5)


def ToNPC(npc, talk=False):
    npc = Field.FindNpc(npc)
    if npc.valid:
        flag = False
        if Terminal.GetCheckBox("Kami Vac"):
            flag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)

        if not (Character.GetPos().x < npc.x + 5 and Character.GetPos().x > npc.x - 5):
            Character.Teleport(npc.x, npc.y - 10)
            time.sleep(1)
            if talk:
                Character.TalkToNpc(npc)

        if flag:
            CheckBox("Kami Vac", True)


def DoQuest(id):
    if Quest.GetQuestState(id) != 2:
        return True
    else:
        return False


def NeedQuest(id):
    if Quest.GetQuestState(id) == 0:
        return True
    else:
        return False


def HasQuest(id):
    if Quest.GetQuestState(id) == 1:
        return True
    else:
        return False


def DoneQuest(id):
    if Quest.GetQuestState(id) == 2:
        return True
    else:
        return False


def InProgress(id, npc):
    if Quest.CheckCompleteDemand(id, npc) != 0:
        return True
    else:
        return False


def StartQuest(id, npc, tp=False):
    flag = False
    if Field.FindNpc(npc).valid and tp:
        if Terminal.GetCheckBox("Kami Vac"):
            flag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
        Character.Teleport(npc.x, npc.y - 10)

    print("Getting quest " + str(id))
    Quest.StartQuest(id, npc)
    time.sleep(1)

    if flag:
        CheckBox("Kami Vac", True)


def CompleteQuest(id, npc, tp=False):
    flag = False
    if Field.FindNpc(npc).valid and tp:
        if Terminal.GetCheckBox("Kami Vac"):
            flag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
        Character.Teleport(npc.x, npc.y - 10)

    print("Completing quest " + str(id))
    Quest.CompleteQuest(id, npc)
    time.sleep(1)


def CheckBox(set, value):
    if Terminal.GetCheckBox(set) != value:
        Terminal.SetCheckBox(set, value)


def CheckMap(map):
    if Field.GetID() == map:
        return True
    else:
        return False


def MapRange(map):
    if Field.GetID() >= map and Field.GetID() <= map + 1:
        return True
    else:
        return False


def MobExists(count=0):
    if len(Field.GetMobs()) > count:
        return True
    else:
        return False


def SpamKey(key):
    if key == "down":
        key = 0x28
    elif key == "alt":
        key = 0x12
    elif key == "ctrl":
        key = 0x11
    elif key == "up":
        key = 0x26
    delay = 0

    for i in range(5):
        delay += 0.2
        time.sleep(delay)
        Key.Down(key)
        time.sleep(0.1)
        Key.Up(key)


def SpamSpace():
    for i in range(20):
        Key.Down(0x20)
        time.sleep(0.05)
        Key.Up(0x20)


def Main():
    if GameState.IsInGame():
        if not Quest.GetQuestState(33284) == 2:
            if Terminal.IsRushing():
                Terminal.StopRush()

            CoreEnterance = 350060000
            Core = 350060160

            Lotus1 = 350060220
            Lotus2 = 350060240
            Lotus3 = 350060260

            BHCorrider = 350062000
            BHCorrider1 = 350062110
            BHCorrider2 = 350062120
            BHCorrider3 = 350062130
            BHCorrider4 = 350062150

            Quater = 350062400
            Gelimer = 350062410
            Gelimer2 = 350062500
            Escape1 = 350063000
            Escape2 = 350063001
            Escape3 = 350063002
            Escape4 = 350063003
            Escape5 = 350063004
            currentMap = Field.GetID()

            if not 350060000 <= Field.GetID() <= 350063500:
                Terminal.Rush(350061000)
                time.sleep(5)

            if currentMap == CoreEnterance:
                SetAttack(False)
                ToPortal("bossIn00")

            if currentMap in range(Core, Core + 10):
                SetAttack(True)

            if MapRange(Lotus1) or MapRange(Lotus2) or MapRange(Lotus3):
                SetAttack()

            if currentMap == 350061000:
                ToPortal("pt_350061000")

            elif currentMap == BHCorrider:
                SetAttack(False)
                ToPortal("In00")

            elif currentMap in range(BHCorrider1, BHCorrider1 + 10):
                if len(Field.GetMobs()) > 0:
                    SetAttack(True)
                else:
                    SetAttack(False)
                    ToPortal("east00")

            elif currentMap in range(BHCorrider3, BHCorrider3 + 10):
                if len(Field.GetMobs()) > 0:
                    SetAttack(True)
                else:
                    SetAttack(False)
                    ToPortal("east00")

            elif currentMap in range(BHCorrider4, BHCorrider4 + 10):
                if len(Field.GetMobs()) > 0:
                    SetAttack(True)
                else:
                    SetAttack(False)
                    ToPortal("east00")

            if currentMap == Quater:
                SetAttack(False)
                ToPortal("pt00")

            elif currentMap == Gelimer:
                Npc.ClearSelection()
                Npc.RegisterSelection("Please")
                time.sleep(2)
                SpamSpace()

            elif currentMap == Gelimer2:
                Character.MoveX(Field.FindPortal("pt00").x, 8000)
                # ToPortal("pt00")
                SpamSpace()

            elif currentMap == 350062900:
                ToPortal("out00")

            elif currentMap == Escape1:
                Character.MoveX(0, 5000)

            elif currentMap == Escape2:
                ToPortal("wet00")

            elif currentMap == Escape3:
                ToPortal("west00")

            elif currentMap == Escape4:
                time.sleep(2)
                ToPortal("pt00")

            elif currentMap == Escape5:
                SetAttack(False, False)
                Character.MoveX(200, 15000)
                # ToPortal("pt00")
                SpamKey("alt")

            elif currentMap == 350063200:
                quests = {
                    33281: 1540744,
                    33282: 1540745,
                    33283: 1540746,
                    33284: 1540729
                }

                for qid, npc in quests.items():
                    if DoQuest(qid):
                        StartQuest(qid, npc)
                        time.sleep(5)


Main()