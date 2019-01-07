import Character
import DataType
import Field
import Inventory
import Key
import Party
import Npc
import Packet
import Quest
import Terminal
import time
import GameState
import os, sys


OdaNobonaga = 9330279
# allClassroomID = [744000021, 744000022, 744000023, 744000024, 744000025, 744000026, 744000027, 744000028, 744000029, 744000030, 744000031, 744000032, 744000033, 744000034,
# 744000035, 744000036, 744000037, 744000038, 744000039, 744000040]
# allMobs = [9410203, 9410208, 9410212, 9410216, 9410211, 9410205, 9410204, 9410200, 9410210, 9410213, 9410202, 9410214, 9410215, 9410209, 9410219, 9410201, 9410199, 9410206, 9410207, 9410218, 9410248]
OdaCoinID = 4310075

"""
You can turn this on as soon as your in lobby, you dont need to enter it for it work. As long as you have the pass, it will walk to portal and enter on its own(No TP).

Change MobVacOption to 'False' if you have another way of killing the mob/boss like GFMA.

It is recommended you have a Pet but the script will not move forward until you have pick up the coin and it will tp you to the coin
periodically (Could have turn on Kami Loot but I felt it was unnecessary for 1 loot.)

"""

MobVacOption = False
KamiOption = True

Terminal.SetCheckBox("Mob Vac", MobVacOption)


def coinChecker():
    Terminal.SetCheckBox("Kami Vac", False)
    while Field.FindItem(OdaCoinID).valid:
        coinDrop = Field.FindItem(OdaCoinID)
        time.sleep(1)
        #Character.Teleport(coinDrop.x, coinDrop.y)
        time.sleep(1)

def lobbyRoom():
    Terminal.SetCheckBox("Kami Vac", False)

    if Party.IsInParty() == True:
        Party.LeaveParty()

    if Inventory.FindItemByID(4033766).valid or Inventory.FindItemByID(5252021).valid:
        print("At Lobby Moving to Portal")
        pos = Character.GetPos()
        if pos.x < 400:
            Character.AMoveX(395)
            time.sleep(3)
        elif pos.x > 435:
            Character.AMoveX(445)
            time.sleep(3)
        else:
            Character.EnterPortal()
            time.sleep(3)
    else:
        print("You need Pass to enter!")


def ranmmaruRoom():
    Terminal.SetCheckBox("Mob Vac", False)
    time.sleep(0.5)
    while Field.FindMob(9410248).valid:
        ranmmaru = Field.FindMob(9410248)
        if KamiOption == False:
            Character.Teleport(ranmmaru.x, ranmmaru.y)
            time.sleep(1)
        else:
            Terminal.SetCheckBox("Kami Vac", False)

    if Field.FindItem(OdaCoinID).valid:
        time.sleep(1)
        coinChecker()

    if Field.FindNpc(OdaNobonaga).valid:
        Terminal.SetCheckBox("Kami Vac", False)
        print("Talking to Oda")
        Character.TalkToNpc(OdaNobonaga)
        time.sleep(1)
        Character.TalkToNpc(OdaNobonaga)
        time.sleep(1)
        backPortal = Field.FindPortal('back')
        if backPortal.valid:
            print("Entering portal")
            Terminal.SetCheckBox("Kami Vac", False)
            if Character.GetPos().x not in range(backPortal.x-2,backPortal.x+2):
                Key.Press(0x08)
            time.sleep(1)
            Character.EnterPortal()


if GameState.IsInGame():

    if Field.GetID() == 744000020:
        lobbyRoom()

    elif Field.GetID()==744000741 or Field.GetID() == 744000041 or Field.GetID() == 744000441 or Field.GetID() == 744000241 or Field.GetID() == 744000141 or Field.GetID() == 744000341 or Field.GetID()==744000641:
        ranmmaruRoom()

    else:

        Terminal.SetCheckBox("Auto NPC", True)

        if KamiOption == True:
            Terminal.SetCheckBox("Kami Vac", False)
            Terminal.SetCheckBox("Mob Vac", False)

        if Field.FindItem(OdaCoinID).valid:
            coinChecker()

        if Field.FindNpc(OdaNobonaga).valid:
            Terminal.SetCheckBox("Kami Vac", False)
            print("Talking to Oda")
            Character.TalkToNpc(OdaNobonaga)
            time.sleep(0.5)
            Character.TalkToNpc(OdaNobonaga)
            time.sleep(0.5)
            Character.TalkToNpc(OdaNobonaga)
            time.sleep(0.5)


            print("Going to Next Portal")
            nextPortal = Field.FindPortal('next')
            if nextPortal.valid:
                print("next portal valid")
                if Character.GetPos().x not in range(nextPortal.x-2,nextPortal.x+2):
                    Key.Press(0x08)
                time.sleep(1.5)
                if Character.GetPos().x in range(nextPortal.x-2,nextPortal.x+2):
                    Character.EnterPortal()
