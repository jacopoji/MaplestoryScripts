# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 12:14:48 2018

@author: Jacopo
"""

import Character
import Packet
import Terminal
import time
import GameState
import Field
import Login

header = 0x00F0
block_header = 0x064E
job = Character.GetJob()
level = Character.GetLevel()
profile_path = 'C:/Users/Jacopo/Desktop/TerminalManager/terminalProfiles/Lvl150Kanna.xml'

def withdraw_mesos():
    if Field.GetID() ==101000000: #wait till character gets to ellinia
        #1032006
        time.sleep(2)
        Packet.BlockRecvHeader(block_header)
        print("Current Mesos before withdraw = {}".format(Character.GetMeso()))
        Character.TalkToNpc(1032006)
        time.sleep(3)
        oPacket = Packet.COutPacket(header)
        oPacket.EncodeBuffer("07 00000006FC23ABFF")
        Packet.SendPacket(oPacket)
        oPacket1 = Packet.COutPacket(header)
        oPacket1.Encode2(8)
        #oPacket2.EncodeBuffer("08")
        Packet.SendPacket(oPacket1)
        time.sleep(1)
        print("Current Mesos after withdraw = {}".format(Character.GetMeso()))
        time.sleep(1)
        #Terminal.LoadProfile(r"C:\Users\Jacopo\Desktop\TerminalManager\terminalProfiles\kannaMesoFarmLVL170.xml")
    else:
        Terminal.Rush(101000000)
        time.sleep(1)

if GameState.GetLoginStep() == 2:
    Terminal.SetCheckBox("Auto Login",False)
    char = Login.GetChar(0)
    CharName = char.name
    print("Finding login bank number for {}".format(CharName))
    while True:
        try:
            f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'r')
            print("Successfully read meso bank number")
        except OSError: #initialization if there is no existing file yet
            f= open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'w')
            f.write('0')
            f.close()
            print("Successfully initialized meso bank number to 0")
        else: #if no need for initialization, then read the value and change AutoChar Number
            f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'r')
            temp = f.read() #save read value to a temp holder
            Terminal.SetLineEdit("LoginChar", str(int(temp)+1))
            f.close()
            print("done with the creation of new character and return login state")
            break
    Terminal.SetCheckBox("Auto Login",True)
    Terminal.SetCheckBox("settings/autochar",True)

while True:
    withdrawed_flag = False
    job = Character.GetJob()
    if job == -1:
        break
    if job == 2700 and Character.GetMeso() == 0:
        #if mesos =0 take out mesos from storage
        print("Withdrawing Mesos")
        withdraw_mesos()
        time.sleep(1)
        withdrawed_flag = True

    #successfully withdrawed money from storage and now need to change back to kanna
    if job == 2700 and Character.GetMeso() == 29999999999 and withdrawed_flag== True:
        f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'r')
        temp = f.read()
        f.close()
        f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'w')
        f.write(str(int(temp)+1)) #update the LoginChar Number to itself + 1
        f.close()
        Terminal.Logout()
        print("Loggin out and changing to Kanna farmer")
        time.sleep(1)
        Terminal.LoadProfile(profile_path)
        break

    elif job == 2700 and Character.GetMeso() != 0 and withdrawed_flag== False:
        f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'r')
        temp = f.read()
        f.close()
        f = open(r'C:\Users\Jacopo\Desktop\Scripts\StoreMeso\%s.txt' % CharName,'w')
        f.write(str(int(temp)+1)) #update the LoginChar Number to itself + 1
        f.close()
        Terminal.Logout()
        print("Logging out and going to next bank")
        break