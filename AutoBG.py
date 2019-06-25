import Character
import DataType
import Field
import Terminal
import time
import GameState
import random

all = [610051300, 610051400, 610051500, 610051600, 610051700, 610051800, 610051900, 610052000, 610050100, 610050200, 610050600, 610050700, 610050800, 610051200, 610050300, 610050400, 610050500, 610050900, 610051000, 610051100]
boss = [9480235, 9480236, 9480237, 9480238, 9480239]
eqp = [1004549, 1012535, 1052952, 1082658, 1102840, 1113185, 1122312, 1132289, 1152191]
KannaJobs = [4200, 4210, 4211, 4212]
mech_jobs = [3510,3511,3512]

######Black gate
def BossCheck():
	print("Waiting for boss to spawn...")
	time.sleep(10)
	for mob in boss:
		print("Checking for boss: " + str(mob) + "...")
		while Field.FindMob(mob).valid and GameState.IsInGame():
			print("Boss found: " + str(mob) + ", killing boss...")
			time.sleep(6)
	for item in eqp:
		print("Checking for item: " + str(item) + "...")
		while Field.FindItem(item).valid and GameState.IsInGame():
			#Terminal.SetCheckBox("Kami Vac",False)
			print("item found with id:" + str(item) + ", waiting until item looted")
			time.sleep(9)
	for mob in boss:
		print("Checking for boss: " + str(mob) + "...")
		while Field.FindMob(mob).valid and GameState.IsInGame():
			print("Boss found: " + str(mob) + ", killing boss...")
			time.sleep(6)
	for item in eqp:
		print("Checking for item: " + str(item) + "...")
		while Field.FindItem(item).valid and GameState.IsInGame():
			#Terminal.SetCheckBox("Kami Vac",False)
			print("item found with id:" + str(item) + ", waiting until item looted")
			time.sleep(9)
	print("no boss found or boss killed")
	time.sleep(6)


def EnterPortal(name):
    time.sleep(0.5)
    portal = Field.FindPortal(name)
    pos = Character.GetPos()
    if pos.x != portal.x:
        print("Portal " + str(name) + " found, teleporting...")
        Character.Teleport(portal.x, portal.y-20)
        time.sleep(0.5)
        print("Teleported to portal: " + str(name)+"...")
    print("Trying to enter portal...")
    while GameState.IsInGame() and Character.GetPos().x == portal.x:
        if Field.GetID() == 610050000:
            break
        Character.EnterPortal()
        time.sleep(0.5)

def toggleAttack(on):
    if job == 3712:
        Terminal.SetLineEdit("SISkillID","37121003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 6512:
        Terminal.SetLineEdit("SISkillID","65121008")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 3512:
        mech_att(on)
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection",False)
    elif job == 2512:
        Terminal.SetLineEdit("SISkillID","25120003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 4112:
        Terminal.SetLineEdit("SISkillID","41121011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 11212: #beast tamer
        Terminal.SetLineEdit("SISkillID","112000002")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",200)
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        count = 0
        if on:
            while count < 50 and Field.GetMobCount()>0:
                Key.Down(0x44)
                time.sleep(0.1)
                Key.Up(0x44)
                time.sleep(0.1)
                Key.Press(0x44)
                count += 1
    elif job == 15212:
        Terminal.SetLineEdit("SISkillID","152121041")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",30)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 3112:
        Terminal.SetLineEdit("SISkillID","31121010")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    elif job == 1212:
        Terminal.SetLineEdit("SISkillID","12121055")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 572:
        Terminal.SetLineEdit("SISkillID","5710020")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 132 or job == 2412: #DK or phantom
        Terminal.SetLineEdit("SISkillID","1311011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 15512: #ark
        Terminal.SetLineEdit("SISkillID","155121007")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",30)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
    elif job == 6412: #Cadena
        Terminal.SetLineEdit("SISkillID","64121011")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetRadioButton("bot/si_cadena",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetCheckBox("Melee No Delay",on)

    elif job not in KannaJobs:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        if on:
            if not Terminal.GetCheckBox("Auto Attack"):
                print("Toggle Skill Injection "+str(on))
                Terminal.SetCheckBox("Auto Attack", on)
        else:
            if Terminal.GetCheckBox("Auto Attack"):
                print("Toggle Skill Injection "+str(on))
                Terminal.SetCheckBox("Auto Attack", on)
    if job not in KannaJobs:
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
        '''
    elif job == 3612: #xenon
        Terminal.SetLineEdit("SISkillID","36121000")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        if on:
            if not Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
        else:
            if Terminal.GetCheckBox("Skill Injection"):
                Terminal.SetCheckBox("Skill Injection", on)
    '''

if GameState.IsInGame():
    map = Field.GetID()
    channel = GameState.GetChannel()
    #Terminal.SetCheckBox("Kami Vac",True)
    job = Character.GetJob()
    #toggleAttack(True)
    if Terminal.IsRushing():
        print("Rushing... Please wait...")
        time.sleep(4)
    # IF FOR SOME REASON U END UP IN HENE
    elif map == 100000000:
        Terminal.Rush(610050000)
    # IF AT BDF MAIN MAP
    elif map == 610050000:
        time.sleep(5)
        if channel == 20:
            channel = 1
        else:
            channel += 1
        Terminal.ChangeChannel(channel)
        while Terminal.IsRushing():
            time.sleep(3)
        print("Current channel" + str(GameState.GetChannel()))
        print("Rushing to starting map")
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610050100)
        else:
            print("Still has ring")

    elif map == 610050100:
        print("Arrived in " + str(map) + "...")
        BossCheck()
        # EnterPortal("south00")
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610051500)
        else:
            print("Still has ring")

    elif map == 610051500:
        print("Arrived in " + str(map) + "...")
        BossCheck()
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610050000)
        else:
            print("Still has ring")
        # BACK TO STARTING POINT

else:
    print("Not in game... Logging in...")
    time.sleep(3)