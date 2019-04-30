import Terminal,time,math,Field,GameState,sys,os
if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "/SunCat")

try:
    import SunCat,SCLib, SCHotkey
except:
    print("Couldn't find SunCat module")
def SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    Terminal.SetCheckBox("Melee No Delay",True)
    count = 0
    if siSkill != 32120055:
        delay = 30*math.ceil(delay*1000 * (10+attackSpeed)/480)/1000
    print("The delay for skill {} is {}, starting si".format(siSkill,delay))
    while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetLineEdit("SISkillID",str(siSkill))
        Terminal.SetSpinBox("SkillInjection",17)
        time.sleep(0.017*9)
        #Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetCheckBox("Skill Injection",False)
        Terminal.SetLineEdit("SISkillID",str(dummySkill))
        #Terminal.SetCheckBox("Skill Injection",True)
        time.sleep(0.017*2)
        Terminal.SetCheckBox("Skill Injection",False)
        time.sleep(delay+0.05)
        #if Terminal.IsRushing():
        #    break
        if siSkill == 27111303 and not(Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219)):
            break
    print("Si ended due to break options")
def attackSemiNDMagic(siSkill,dummySkill,delay,on,attackSpeed = 4):
    try:
        SCLib.ThreadedFunction(SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed))
    except:
        x = 1

attackSemiNDMagic(42111011,42121000,0.6,True,4)