import Terminal,time,math,Field,GameState,sys,os,Character,Key,Packet
if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "/SunCat")

try:
    import SunCat,SCLib, SCHotkey
except:
    print("Couldn't find SunCat module")

KannaJobs = [4200, 4210, 4211, 4212]
LuminousJobs = [2700, 2710, 2711, 2712]
ArkJobs = [15500, 15510, 15511, 15512]

DemonAvengerJobs = [3101, 3120, 3121, 3122]
DemonSlayerJobs = [3100, 3110, 3111, 3112]
AranJobs = [2000,2100, 2110, 2111, 2112]
MercedesJobs = [2300, 2310, 2311, 2312]
HayatoJobs = [4100, 4110, 4111, 4112]

KaiserJobs = [6100, 6110, 6111, 6112]
MihileJobs = [5100, 5110, 5111, 5112]
AngelicBusterJobs = [6500, 6510, 6511, 6512]
XenonJobs = [3600, 3610, 3611, 3612]
PhantomJobs = [2400, 2410, 2411, 2412]
EvanJobs = [2200, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218]
ShadeJobs =[2005,2500,2510,2511,2512]
IlliumJobs = [15200,15210,15211,15212]
CadenaJobs = [6400,6410,6411,6412]
KinesisJobs = [14200,14210,14211,14212]
#explorer jobs
#thief
ShadowerJobs = [400,420,421,422]
NightlordJobs = [400,410,411,412]
DualbladeJobs = [400,430,431,432,433,434]
#warrior
HeroJobs = [100,110,111,112]
PaladinJobs = [100,120,121,122]
DarkknightJobs = [100,130,131,132]
#archer
BowmasterJobs = [300,310,311,312]
MarksmanJobs = [300,320,321,322]
#magician
ILMageJobs = [200,220,221,222]
FPMageJobs = [200,210,211,212]
BishopJobs = [200,230,231,232]
#pirate
BuccaneerJobs = [500,510,511,512]
CorsairJobs = [500,520,521,522]
CannoneerJobs = [501,530,531,532]
JettJobs = [508,570,571,572]

explorerFirstJobs = [100,200,300,400,500,501]
explorerSecondJobs = [110,120,130,210,220,230,310,320,410,420,430,510,520,530]
explorerThirdJobs = [111,121,131,211,221,231,311,321,411,421,431,511,521,531]
explorerFourthJobs = [112,122,132,212,222,232,312,322,412,422,432,434,512,522,532]

#Cygnus Jobs
DawnWarriorJobs = [1100,1110,1111,1112]
BlazeWizardJobs = [1200,1210,1211,1212]
WindArcherJobs  = [1300,1310,1311,1312]
NightWalkerJobs = [1400,1410,1411,1412]
ThunderBreakerJobs=[1500,1510,1511,1512]

cygnusFirstJobs = [1100,1200,1300,1400,1500]
cygnusSecondJobs= [1110,1210,1310,1410,1510]
cygnusThirdJobs = [1111,1211,1311,1411,1511]
cygnusFourthJobs= [1112,1212,1312,1412,1512]

#Resistance Jobs
BattleMageJobs = [3200, 3210, 3211, 3212]
WildHunterJobs = [3300, 3310, 3311, 3312]
BlasterJobs = [3700, 3710, 3711, 3712]
MechanicJobs = [3500,3510,3511,3512]

resistanceFirstJobs = [3200,3300,3500,3700]
resistanceSecondJobs = [3210,3310,3510,3710]
resistanceThirdJobs = [3211,3311,3511,3711]
resistanceFourthJobs= [3212,3312,3512,3712]

def vulcan():
    if GameState.IsInGame() and ((int(time.time())%8==0) or (Character.HasBuff(2, 37110009)==False and Character.HasBuff(2, 37120012)==False)):
        Vulcan = Packet.COutPacket(0x0151)
        Vulcan.Encode4(0x17D7AF14)
        Vulcan.EncodeBuffer("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        Packet.SendPacket(Vulcan)
    return
    
def attackAuto(skillid,on):
    attack_key = 0x44
    Key.Set(attack_key,1,skillid)
    Terminal.SetCheckBox("Skill Injection", False)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack", on)
    Terminal.SetComboBox("AttackKey",33)
    Terminal.SetSpinBox("autoattack_spin",100)

def attackSI(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)
    Terminal.SetRadioButton(siOption,True)

def attackSIND(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetRadioButton(siOption,True)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)
def SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    count = 0
    if siSkill != 32120055:
        delay = 30*math.ceil(delay*1000 * (10+attackSpeed)/480)/1000
    print("The delay for skill {} is {}, starting si".format(siSkill,delay))
    if siSkill in [5311000,5301000]:
        sleepTime = 0.161
    elif siSkill not in [25101000,25121000]:
        sleepTime = 0.211
    else:
        sleepTime = 0.101
    while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetLineEdit("SISkillID",str(siSkill))
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",17)
        time.sleep(sleepTime)
        #Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetLineEdit("SISkillID",str(dummySkill))
        time.sleep(0.043)
        Terminal.SetCheckBox("Skill Injection",False)
        time.sleep(delay+0.05)
        #if Terminal.IsRushing():
        #    break
        if (siSkill == 27111303 or siSkill == 27121303) and not(Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219)):
            break
        count += 1
    print("Si ended due to break options")
def attackSemiNDMagic(siSkill,dummySkill,delay,on,attackSpeed = 5):
    try:
        SCLib.ThreadedFunction(SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed))
    except:
        x = 1
def ToggleBuffs(buffid,skillid = None,toggleKami = False):
    short_sleep = 0.75
    if skillid is None:
        skillid = buffid
    if Character.GetSkillLevel(buffid) > 0:
        if Character.HasBuff(2, buffid) == False:
            autoAttack = Terminal.GetCheckBox("Auto Attack")
            skillInject = Terminal.GetCheckBox("Skill Injection")
            javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
            Terminal.SetCheckBox("Auto Attack",False)
            Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
            Terminal.SetCheckBox("Skill Injection",False)
            if toggleKami:
                ToggleKami(False)
            time.sleep(short_sleep)
            Character.UseSkill(skillid)
            #time.sleep(short_sleep)
            if job in BattleMageJobs:
                time.sleep(short_sleep)
                Character.UseSkill(32001014)
                #time.sleep(short_sleep)
            if Character.HasBuff(2, buffid) == True:
                if toggleKami:
                    ToggleKami(True)
            Terminal.SetCheckBox("Auto Attack",autoAttack)
            Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
            Terminal.SetCheckBox("Skill Injection",skillInject)
def setSIND(siSkill,delay,on):
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetLineEdit("SISkillID",siSkill)
    Terminal.SetCheckBox("Skill Injection",on)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetSpinBox("SkillInjection",delay)
attack_key = 0x44
pgup_key = 0x21
if GameState.IsInGame():
    job = Character.GetJob()
    if job == 1212 or job == 2312:
        Terminal.SetComboBox("Familiar0",1)
    else:
        Terminal.SetComboBox("Familiar0",5)
    if job == 3712: #Blaster
        print("Setting up settings for Blaster")
        attackSI(37110006,True,80)
        #attackSemiNDMagic(32120055,32120055,0.45,True)
        vulcan()
    elif job ==4212: #4th
        print("Setting up Settings for Kanna")
        #Terminal.SetSpinBox("charm_delay",100)
        #Terminal.SetCheckBox("Auto SP",True)
        #Terminal.SetCheckBox("charm_fma",True)
        #Terminal.SetCheckBox("Summon Kishin",False)
        #Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetCheckBox("Auto Attack",True)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Key.Set(0x47,1,42111003)
        attackSemiNDMagic(42111011,42121000,0.6,True,4)
    elif job == 1312:
        attackSemiNDMagic(32120055,32120055,0.45,True)
    elif job == 2712: #lumi fourth job
        print("Setting up Settings for Luminous")
            #Assign an Item, reboot potion, to Page up(0x21)
        attackSemiNDMagic(32120055,32120055,0.45,True)
        # if Character.HasBuff(2,20040216): #Light Mode
        #     attackAuto(27121100,True)
        # elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
        #     attackSemiNDMagic(27121303,27121303,1.26,True,5)
        #     #attackAuto(27111303,on)
        # else:                              #Dark Mode
        #     #attackSemiNDOnce(27121202,27001201,0.96,on)
        #     attackSI(27101202,True,200)
        Terminal.SetCheckBox("Full Map Attack",False)
    elif job == 3122: #DA fourth job
        print("Setting up Settings for DA") 
        #attackSemiNDMagic(31211010,31211010,0.78,True)
        #Execution 31221012
        attackSemiNDMagic(31221012,31221012,0.84,True)
    elif job == 1112: #Dawn warrior
        attackSemiNDMagic(32120055,32120055,0.45,True)
    elif job == 3112: #DS fourth job
        print("Setting up Settings for DS")
        attackSemiNDMagic(400011018,400011018,0.40,True,attackSpeed = 6)
        
    elif job == 2312: #Mercedes 4th
        print("Setting up Settings for Mercedes")
        Terminal.SetLineEdit("SISkillID","400031024")
        Terminal.SetSpinBox("SkillInjection",110)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
    elif job == 11212: #BeastTamer
        print("Setting up Settings for BeastTamer")
        attackSemiNDMagic(32120055,32120055,0.45,True) 
    elif job == 4112: #Hayato 4th 41121011
        print("Setting up Settings for Hayato")
        
        attackSemiNDMagic(32120055,32120055,0.45,True)
        
    elif job == 3612:#Xenon 4th 36121000
        print("Setting up Settings for Xenon")
        
        # Terminal.SetLineEdit("SISkillID","36121000")
        # Terminal.SetSpinBox("SkillInjection",80)
        # Terminal.SetCheckBox("Melee No Delay",False)
        
        # Terminal.SetRadioButton("SIRadioMelee",True)
        # Terminal.SetCheckBox("Auto Attack",False)
        # Terminal.SetCheckBox("Skill Injection", True)
        attackSemiNDMagic(32120055,32120055,0.45,True)
    elif job == 2412: #Phantom 4th 24121000
        print("Setting up Settings for Phantom")
        #setSIND("24121010;24121000",140,on)
        # Terminal.SetLineEdit("SISkillID","24121010;24121000")
        # Terminal.SetCheckBox("Auto Attack",False)
        # Terminal.SetCheckBox("Melee No Delay",True)
        # Terminal.SetRadioButton("SIRadioMelee",True)
        
        # Terminal.SetCheckBox("Skill Injection", True)
        # Terminal.SetSpinBox("SkillInjection",140)
        attackSemiNDMagic(32120055,32120055,0.45,True)
        
    elif job == 15212: #Illium 4th
        print("Setting up Settings for Illium")
        #setSIND("32120055;152121041",65,True)
        attackSemiNDMagic(32120055,32120055,0.45,True)
    elif job == 6412: # Cadena 4th job
        print("Setting up Settings for Cadena")
        #setSIND("64120000;64001001",100,True)
        #attackSIND(64001001,True,160,"si_cadena")
        attackSemiNDMagic(32120055,32120055,0.45,True)
        
    elif job == 15512: #Ark 4th 155121007 @50
        print("Setting up Settings for Ark")
        Terminal.SetLineEdit("SISkillID", "155001100")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetSpinBox("SkillInjection",700)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        
    elif job == 2217: #Evan 4th 22170061 SI/ND
        print("Setting up Settings for Evan")
        Terminal.SetLineEdit("SISkillID", "400021046")
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("dragon_kami",True)
        Terminal.SetCheckBox("Mob Falldown",False)
        
        Terminal.SetCheckBox("Legit Vac",True)
        Terminal.SetSpinBox("SkillInjection",80)
        Terminal.SetRadioButton("SIRadioDragon",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetSpinBox("autoattack_spin",2500)
        Terminal.SetCheckBox("Kami Vac",False)
        Terminal.SetCheckBox("Auto Attack",False)
    elif job == 2112: #Aran 4th 21000007
        print("Setting up Settings for Aran")
            #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,21001010)
        Terminal.SetLineEdit("SISkillID","21000006")
        
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetSpinBox("SkillInjection",75)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        
    elif job == 14212: # Kinesis 4th 142111002
        print("Setting up Settings for Kinesis")
            #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,142111002)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        
    elif job == 6512: #AB 4th
        print("Setting up Settings for AB")
        #attackSemiNDMagic(65121100,65001100,0.63,True,5)
        attackSemiNDMagic(32120055,32120055,0.45,True)
        # Terminal.SetLineEdit("SISkillID","400051011")
        # Terminal.SetCheckBox("Auto Attack", False)
        
        # Terminal.SetSpinBox("SkillInjection",0)
        # Terminal.SetCheckBox("Melee No Delay",False)
        # Terminal.SetRadioButton("SIRadioMagic",True)
        # Terminal.SetCheckBox("Skill Injection", True)
        # Terminal.SetCheckBox("General FMA",True)
        # Terminal.SetCheckBox("Kami Vac",False)
    elif job == 3512: #mechanic 4th 400051012
        #mech_att(on)
        attackSemiNDMagic(32120055,32120055,0.45,True)
        # print("Setting up Settings for Mechanic")
        # Terminal.SetRadioButton("SIRadioMelee",True)
        # Terminal.SetLineEdit("SISkillID","400051012")
        # Terminal.SetCheckBox("Auto Attack", False)
        
        # Terminal.SetSpinBox("SkillInjection",100)
        # Terminal.SetCheckBox("Melee No Delay",False)
        # Terminal.SetCheckBox("Skill Injection", True)
        
    elif job == 2512: #Shade 4th
        print("Setting up Settings for Shade")
        Terminal.SetLineEdit("SISkillID","25120003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        
    elif job == 1212: #BW 4th
        print("Setting up Settings for Blaze Wizard")
        Terminal.SetCheckBox("Full Map Attack",False)
        #attackAuto(12001020,True)
        setSIND("32120055;12121055",65,True)
    elif job == 572: #Jett 4th
        print("Setting up Settings for Jett")
        
        Terminal.SetLineEdit("SISkillID","5710020")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Melee No Delay",True)
    elif job == ThunderBreakerJobs[3]:
        attackSemiNDMagic(32120055,32120055,0.45,True)
        # attackSI(400051007,True,100,"SIRadioMagic")
        # Terminal.SetCheckBox("General FMA",True)
        # Terminal.SetCheckBox("Kami Vac",False)
    elif job == WildHunterJobs[3]:
        attackSI(400031033,True,100,"SIRadioShoot")
        
    elif job == 434: #dual blade
        attackSIND(400040006,True,16)
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)
        if job not in AngelicBusterJobs and job not in BlasterJobs:
            Terminal.SetCheckBox("General FMA",False)
        #if job not in LuminousJobs:
        #    Terminal.SetCheckBox("Full Map Attack",False)

#Key.Set(0x4C, 1, 2321054)
#ToggleBuffs(2321054)