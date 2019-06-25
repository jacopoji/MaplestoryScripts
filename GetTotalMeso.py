import os, sys, Terminal, Character, GameState, Login
# GetTotalMeseo.py
# Author: Comicals
# 10/16/18

startslot = 0
maxMeso = 29999999999


def LineEdit(line, value):
    if Terminal.GetLineEdit(line) != value:
        Terminal.SetLineEdit(line, value)

def CheckBox(set, value):
    if Terminal.GetCheckBox(set) != value:
        Terminal.SetCheckBox(set, value)
        
        
def CheckAccountMeso(max):
    totalMeso = 0
    while int(Terminal.GetLineEdit("LoginChar")) < max:
        if GameState.IsInGame():
            if Character.GetMeso() < maxMeso:
                f.write(Character.GetName()+": "+str(Character.GetMeso())+"\n")
                totalMeso = totalMeso + Character.GetMeso()
                print(Character.GetName(), "did not have max meso", Character.GetMeso())
                time.sleep(3)
                LineEdit("LoginChar", str(int(Terminal.GetLineEdit("LoginChar"))+1))
                Terminal.Logout()
            else:
                f.write(Character.GetName()+": "+str(Character.GetMeso())+"\n")
                totalMeso = totalMeso + Character.GetMeso()
                print(Character.GetName(), "has meso" ,Character.GetMeso())
                time.sleep(3)
                LineEdit("LoginChar", str(int(Terminal.GetLineEdit("LoginChar"))+1))
                Terminal.Logout()
        else:
            print("Not in game, waiting character to login", flush = True)
            time.sleep(10)
    CheckBox("Auto Login", False)
    
    return totalMeso
    
    

if GameState.GetLoginStep() == 2:
    max = Login.GetCharCount()
    
    LineEdit("LoginChar", str(startslot))
    CheckBox("LoginChar", False)
    CheckBox("Auto Login", True)
    
    f = open("MESO_"+Login.GetChar(0).name+".txt", "a")
    totalMeso = CheckAccountMeso(max)
    print("total meso :", totalMeso)
    
    f.write("\n Total meso: "+str(totalMeso))
    f.close()
else:
    print("must be in character screen to start the script")
    CheckBox("Auto Login", False)