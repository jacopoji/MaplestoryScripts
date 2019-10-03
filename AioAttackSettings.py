import Field, Character, Terminal, time, GameState,sys,os,Key
import math
if not any("SunCat" in s for s in sys.path):
	sys.path.append(os.getcwd() + "\SunCat")

try:
	import SCLib
except:
	print("Couldn't find SunCat module")

from JobConstants import *

def AttackAuto(skillid,on):
    attack_key = 0x44
    Key.Set(attack_key,1,skillid)
    Terminal.SetCheckBox("Skill Injection", False)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack", on)
    Terminal.SetComboBox("AttackKey",33)
    Terminal.SetSpinBox("autoattack_spin",100)

def AttackSI(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)
    Terminal.SetRadioButton(siOption,True)

def AttackSIND(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetRadioButton(siOption,True)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)

def SemiNDAA(siSkill,dummySkill,delay,on):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection",False)
    Terminal.SetCheckBox("Melee No Delay",True)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    #count = 0
    while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        for x in range(8):
            Character.UseSkill(siSkill)
            time.sleep(0.015)
        Character.UseSkill(dummySkill)
        time.sleep(delay)
        if Terminal.IsRushing():
            break

def AttackSemiND(siSkill,dummySkill,delay,on):
    try:
        SCLib.ThreadedFunction(SemiNDAA(siSkill,dummySkill,delay,on))
    except:
        x = 1

def SetSIND(siSkill,delay,on):
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetLineEdit("SISkillID",siSkill)
    Terminal.SetCheckBox("Skill Injection",on)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetSpinBox("SkillInjection",delay)

def ToggleSkill():
    if job in WildHunterJobs and level > 11:
        #Rige Jaguar
        buff = 33001001
        ToggleBuffs(buff,buff,True)
        if level >= 140:
            buff = 33121054
            TimeoutBuffs(buff)
        hunter = 33111013
        TimeoutBuffs(hunter)
    elif job in MechanicJobs:
        #Mount Mechanic machine
        if level < 160:
            buff = 35001002
            ToggleBuffs(buff,buff,True)
            bots = 35121009
            TimeoutBuffs(bots)
        if job == MechanicJobs[1]:
            roboLauncher = 35101012
            ToggleBuffs(roboLauncher)
        elif job == MechanicJobs[2]:
            buff = 35111013
            TimeoutBuffs(buff)
            roboLauncher = 35101012
            ToggleBuffs(roboLauncher)
            support = 35111008
            ToggleBuffs(support)
        elif job == MechanicJobs[3]:
            buff = 35120014
            skill = 35111013
            TimeoutBuffs(buff,skill)
            if level < 160:
                roboLauncher = 35101012
                ToggleBuffs(roboLauncher)
                support = 35111008
                ToggleBuffs(support)
    elif job in FPMageJobs or job in ILMageJobs or job in BishopJobs:
        #magic guard
        buff = 2001002
        ToggleBuffs(buff)
        if job == BishopJobs[3]:
            summon_dragon = 2321003
            ToggleBuffs(summon_dragon)
    elif job in EvanJobs:
        #magic guard
        buff = 22001012
        ToggleBuffs(buff)
    elif job in DawnWarriorJobs:
        if job == DawnWarriorJobs[1]:
            buff = 11101022 #moon 
            ToggleBuffs(buff)
        elif job == DawnWarriorJobs[2]:
            #buff = 11111022 #sun
            buff = 11101022 #moon 
            ToggleBuffs(buff)
        elif job == DawnWarriorJobs[3]:
            #if level < 180:
            #    buff = 11111022 
            #else:
            #    buff = 11121005#equinox
            buff = 11111022
            ToggleBuffs(buff)
    elif job == ThunderBreakerJobs[3]:
        buff = 15121004
        ToggleBuffs(buff)
    elif job == NightWalkerJobs[3]:
        buff = 14121003
        TimeoutBuffs(buff,timer=10)
    elif job in WindArcherJobs and job != WindArcherJobs[0]:
        if job == WindArcherJobs[1]:
            buff = 13101022
            ToggleBuffs(buff)
        elif job == WindArcherJobs[2]:
            buff = 13110022
            skill = 13101022
            ToggleBuffs(buff,skill)
        elif job == WindArcherJobs[3]:
            buff = 13120003
            skill = 13101022
            ToggleBuffs(buff,skill)
    elif job in BattleMageJobs:
        if job == BattleMageJobs[0]:
            buff = 32001016 #hasty aura
            ToggleBuffs(buff)
        elif job == BattleMageJobs[1]:
            buff = 32101009 #yellow aura
            ToggleBuffs(buff)
        elif job == BattleMageJobs[2]:
            buff = 32111012 #blue aura
            ToggleBuffs(buff)
        elif job == BattleMageJobs[3]:
            buff = 32121017 #dark aura
            ToggleBuffs(buff)
    elif job == AngelicBusterJobs[3]:
        buff = 65121011
        ToggleBuffs(buff)
    elif job in DarkknightJobs and job != DarkknightJobs[0]:
        buff = 1301013
        ToggleBuffs(buff)
        if level >= 140:
            buff = 1321054
            TimeoutBuffs(buff)
    elif job in HeroJobs and job != HeroJobs[0]:
        buff = 1101013
        ToggleBuffs(buff)
    elif job in ShadeJobs and job >=2510:
        buff = 25101009
        ToggleBuffs(buff)
        if job == ShadeJobs[4] and level >= 140:
            buff2 = 25121131
            TimeoutBuffs(buff2)
    elif job == 531: #Cannon Trooper 5311005
        buff = 5311005
        TimeoutBuffs(buff)
        buff3 = 5311004
        TimeoutBuffs(buff3)
    elif job == 532: #Cannoneer
        buff = 5321004
        TimeoutBuffs(buff)
        buff2 = 5320007
        skill2= 5311005
        TimeoutBuffs(buff2,skill2)
        buff3 = 5311004
        TimeoutBuffs(buff3)
        buff4 = 5321052
        TimeoutBuffs(buff4,timer = 30)
    elif job == CorsairJobs[2]: #or job == CorsairJobs[3]:
        buff = 5211014
        TimeoutBuffs(buff)
    elif job == CorsairJobs[3]: #5220014
        buff = 5220014
        skill = 5211007
        TimeoutBuffs(buff,skill)
    elif job == BuccaneerJobs[2]: #or job == CorsairJobs[3]:
        buff = 5111007
        TimeoutBuffs(buff)
    elif job == BuccaneerJobs[3]: #5220014
        buff = 5120012
        skill = 5111007
        TimeoutBuffs(buff,skill)

        buff2 = 5121013
        TimeoutBuffs(buff2,buff2,30,True,True)
    elif job in IlliumJobs and job != IlliumJobs[0]:
        buff = 152101000
        skill = 152101003
        ToggleBuffs(buff,skill)
    elif job in HayatoJobs:
        buff = 40011289
        TimeoutBuffs(buff)
        if level >= 140:
            buff = 41121054
            TimeoutBuffs(buff)
        '''
        if Character.HasBuff(2,buff) == False:
            timeout = time.time() + 30
            if not Terminal.GetProperty("skill_timeout",False):
                Terminal.SetProperty("skill_timeout",timeout)
                print("Summer rain: Initialize")
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                Character.UseSkill(buff)
                time.sleep(short_sleep)
                Terminal.SetCheckBox("Skill Injection",True)
            elif time.time() > Terminal.GetProperty("skill_timeout",False):
                Terminal.SetProperty("skill_timeout",timeout)
                print("Summer rain: Continued")
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                Character.UseSkill(buff)
                time.sleep(short_sleep)
        '''
    elif job in KinesisJobs:
        if job == KinesisJobs[3]:
            buff = 142121004
            TimeoutBuffs(buff)
            
    elif job == ShadowerJobs[3] and level >= 140:
        buff = 1
        skill = 4221054 #coin
        TimeoutBuffs(buff,skill,timer = 40)
        if level < 180:
            buff2 = 4221052 #shadow veil
            TimeoutBuffs(buff2,timer=15)
        #buffs = Character.GetBuffs()
        #for buffa in buffs:
        #    print("Current Buff Id: {}; Remaining Time: {}".format(buff.id,buff.timeLeft))
    elif job in NightlordJobs and job != NightlordJobs[0]:
        buff = 4101011
        ToggleBuffs(buff)
        buff2 = 4111007
        TimeoutBuffs(buff2,timer = 60)
        if job == NightlordJobs[3] and level >= 140:
            buff = 4121054
            TimeoutBuffs(buff,buff,30)
    elif job in KaiserJobs:
        buff = 60001217
        ToggleBuffs(buff)
        if job == KaiserJobs[2] or job == KaiserJobs[3]:
            buff = 61111002
            ToggleBuffs(buff)
        if level >= 140:
            buff = 61121054
            TimeoutBuffs(buff)
    elif job in PhantomJobs:
        buff = 20031210
        ToggleBuffs(buff)
    elif job in BowmasterJobs:
        if job == BowmasterJobs[2]:
            buff = 3111011
            ToggleBuffs(buff)
        elif job == BowmasterJobs[3]:
            buff = 3111011
            ToggleBuffs(buff)
            buff2=3121054
            TimeoutBuffs(buff2,buff2,30,False)
    elif job in MarksmanJobs:
        if job == MarksmanJobs[2]:
            buff = 3211012
            ToggleBuffs(buff)
        elif job == MarksmanJobs[3]:
            buff = 3211012
            ToggleBuffs(buff)
            buff2 = 3221054
            TimeoutBuffs(buff2,need_sleep = True)
    elif job in DemonSlayerJobs:
        if job == DemonSlayerJobs[3]:
            buff = 31121054
            TimeoutBuffs(buff)
    elif job in DemonAvengerJobs:
        if job == DemonAvengerJobs[3]:
            if level >= 140:
                buff = 31221054
                TimeoutBuffs(buff,buff,30,False)
            if level >= 200:
                buff = 31221053
                TimeoutBuffs(buff,buff,30,False)
    elif job in MercedesJobs:
        if level >= 140:
            buff = 23121054
            TimeoutBuffs(buff)
    elif job in DualbladeJobs:
        #if job == DualbladeJobs[-1]:
            #buff = 4341002
            #TimeoutBuffs(buff)
            #buff2= 4341011
            #TimeoutBuffs(buff2,timer=50)
        if level >= 140:
            buff = 4341054
            TimeoutBuffs(buff)
    elif job in XenonJobs:
        buff = 36001005
        ToggleBuffs(buff)
        if job == XenonJobs[3]:
            buff = 36121002
            TimeoutBuffs(buff)
            buff2= 36121003
            TimeoutBuffs(buff2)
    elif job in ArkJobs[1:]:
        buff = 155101008
        ToggleBuffs(buff)
            
def ToggleBuffs(buffid,skillid = None,ToggleKami = False):
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
            if ToggleKami:
                toggleKami(False)
            time.sleep(short_sleep)
            Character.UseSkill(skillid)
            #time.sleep(short_sleep)
            if job in BattleMageJobs:
                time.sleep(short_sleep)
                Character.UseSkill(32001014)
                #time.sleep(short_sleep)
            if Character.HasBuff(2, buffid) == True:
                if ToggleKami:
                    toggleKami(True)
            Terminal.SetCheckBox("Auto Attack",autoAttack)
            Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
            Terminal.SetCheckBox("Skill Injection",skillInject)
    
def TimeoutBuffs(buffid,skillid = None,timer = 30,need_sleep = True,injectSkill = False):
    if need_sleep:
        short_sleep = 0.85
    else:
        short_sleep = 0.05
    if skillid is None:
        skillid = buffid
    if Character.GetSkillLevel(skillid) > 0:
        if Character.HasBuff(2,buffid) == False and len(Field.GetMobs()) > 0:
            timeout = time.time() + timer
            if not Terminal.GetProperty("skill_timeout{}".format(str(buffid)),False):
                Terminal.SetProperty("skill_timeout{}".format(str(buffid)),timeout)
                print("Skill {}: Initialize".format(buffid))
                autoAttack = Terminal.GetCheckBox("Auto Attack")
                skillInject = Terminal.GetCheckBox("Skill Injection")
                javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
                Terminal.SetCheckBox("Auto Attack",False)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                if not injectSkill:
                    if skillid == 4341002:
                        Key.Set(0x44, 1, skillid)
                        Character.UseSkill(skillid)
                        time.sleep(0.01)
                        Key.Down(0x44)
                        time.sleep(0.7)
                        Key.Up(0x44)
                    else:
                        Character.UseSkill(skillid)
                        time.sleep(0.01)
                        Character.UseSkill(skillid)
                        time.sleep(0.01)
                        Character.UseSkill(skillid)
                else:
                    Terminal.SetLineEdit("SISkillID",str(skillid))
                    Terminal.SetSpinBox("SkillInjection",300)
                    Terminal.SetCheckBox("Skill Injection",True)
                    time.sleep(short_sleep*2)
                    Terminal.SetCheckBox("Skill Injection",False)
                #time.sleep(short_sleep)
                Terminal.SetCheckBox("Auto Attack",autoAttack)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
                Terminal.SetCheckBox("Skill Injection",skillInject)
            elif time.time() > Terminal.GetProperty("skill_timeout{}".format(str(buffid)),False):
                Terminal.SetProperty("skill_timeout{}".format(str(buffid)),timeout)
                #print("Skill {}: Continued".format(buffid))
                autoAttack = Terminal.GetCheckBox("Auto Attack")
                skillInject = Terminal.GetCheckBox("Skill Injection")
                javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
                Terminal.SetCheckBox("Auto Attack",False)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                if not injectSkill:
                    Character.UseSkill(skillid)
                    time.sleep(0.01)
                    Character.UseSkill(skillid)
                    time.sleep(0.01)
                    Character.UseSkill(skillid)
                else:
                    Terminal.SetLineEdit("SISkillID",str(skillid))
                    Terminal.SetSpinBox("SkillInjection",300)
                    Terminal.SetCheckBox("Skill Injection",True)
                    time.sleep(short_sleep*2)
                    Terminal.SetCheckBox("Skill Injection",False)
                if job == KinesisJobs[3]:
                    time.sleep(short_sleep*2)
                    Character.UseSkill(142121005)
                #time.sleep(short_sleep)
                Terminal.SetCheckBox("Auto Attack",autoAttack)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
                Terminal.SetCheckBox("Skill Injection",skillInject)

def AttackSemiNDOnce(siSkill,dummySkill,delay,on):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    if Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetLineEdit("SISkillID",str(siSkill))
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",15)
        time.sleep(0.24)
        Terminal.SetCheckBox("Skill Injection",False)
        time.sleep(0.02)
        Character.UseSkill(dummySkill)
        time.sleep(delay)

def SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    Terminal.SetCheckBox("Speedy Gonzales",True)
    count = 0
    if siSkill != 32120055:
        delay = 30*math.ceil(delay*1000 * (10+attackSpeed)/480)/1000
    #print("The delay for skill {} is {}, starting si".format(siSkill,delay))
    if siSkill in [5311000,5301000]:
        sleepTime = 0.161
    elif siSkill not in [25101000,25121000]:
        sleepTime = 0.231
    else:
        sleepTime = 0.101
    while Field.GetCharacterCount()<=1 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
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
        if count >= 20:
            break
        if siSkill == 27111303 and not(Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219)):
            break
        count += 1
    #print("Si ended due to break options")
    #Terminal.SetProperty("IssueThread",True)
def AttackSemiNDMagic(siSkill,dummySkill,delay,on,attackSpeed = 4):
    try:
        SCLib.ThreadedFunction(SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed))
    except Exception as e:
        print(e)
        

def ToggleAttack(on):
    attack_key = 0x44
    pgup_key = 0x21
    job = Character.GetJob()
    level = Character.GetLevel()
    useHyperExploit = True
    if job == 4200: #kanna first job
        AttackSI(42001006,on)
    elif job == 4210: #kanna 2nd
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",on)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetSpinBox("SkillInjection", 100)
        Terminal.SetLineEdit("SISkillID","42001006")
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4211:#kanna 3rd
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",on)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 4212: #kanna 4th 
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetCheckBox("Summon Kishin",False)
            Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
            Terminal.SetSpinBox("autoattack_spin",7500)
            Terminal.SetComboBox("AttackKey",36)
            AttackSIND(42120026,on,100)
            #AttackSemiNDMagic(42111000,42001006,0.70,on)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 2700: #lumi first job
        # 20040217 Dark Mode Buff
        # 20040216 Light Mode
        # 20040220 20040219 Equi Mode
        AttackSemiNDMagic(27001201,27001201,0.98,on)
    elif job == 2710: #lumi second job
        if Character.HasBuff(2,20040217): #use dark magic
            #AttackAuto(27001201,on)
            AttackSI(27101202,on,200)
        else:
            #AttackSemiNDMagic(27101100,27101100,0.5,on)
            AttackAuto(27101100,on)
    elif job == 2711: #lumi third job
        if Character.HasBuff(2,20040216): #Light Mode
            AttackAuto(27101100,on)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            AttackSemiNDMagic(27111303,27111303,1.77,on)
        else:                              #Dark Mode
            #AttackAuto(27111202,on)
            AttackSI(27101202,on,200)
    elif job == 2712: #lumi fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,20040216): #Light Mode
                AttackAuto(27121100,on)
            elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
                AttackSemiNDMagic(27111303,27111303,1.77,on)
                #AttackAuto(27111303,on)
            else:                              #Dark Mode
                #AttackSemiNDOnce(27121202,27001201,0.96,on)
                AttackSI(27101202,on,200)
    elif job == 3101: #DA first job
        AttackAuto(31011000,on)
    elif job == 3120: #DA 2nd
        #AttackSemiNDMagic(31201010,31201010,0.66,on)
        AttackSIND(31201010,on,100)
        #AttackAuto(31011000,on)
    elif job == 3121 or job == 3122: #DA third job and fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(31211010,31211010,0.78,on)
    elif job == 3100 or job == 3110 or job == 3111: #DS first - third job
        #Key.Set(attack_key,1,31000004)31001008
        if SCLib.GetVar("DoingJobAdv"):
            AttackSI(31001008,100,on)
        else:
            AttackSemiNDMagic(31001008,31001008,0.55,on)
    elif job == 3112: #DS fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSI(31121010,on,16)
            AttackSemiNDMagic(31121010,31121010,0.66,on)
    elif job == 2300: #Mercedes 1st 
        AttackAuto(23001000,on)
    elif job ==2310: #Mercedes 2nd
        AttackAuto(23101000,on)
        #AttackSIND(23101007,on,250)
        #AttackSIND(23100004,on,300)
    elif job ==2311: #Mercedes 3rd
        #AttackAuto(23111000,on)
        '''
        attack_key = 0x44
        Key.Set(attack_key,1,23111000)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetLineEdit("SISkillID",str(23111002))
        Terminal.SetSpinBox("SkillInjection",200)
        Terminal.SetCheckBox("Melee No Delay",on)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetCheckBox("Skill Injection", on)
        '''
        AttackSemiNDMagic(23111000,23111002,0.54,on)
        #AttackSIND(23111000,on,250)
    elif job == 2312: #Mercedes 4th
        #AttackAuto(23111000)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            '''
            attack_key = 0x44
            Key.Set(attack_key,1,23111000)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",100)
            Terminal.SetLineEdit("SISkillID",str(23111002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
            '''
            #AttackAuto(23111000,on)
            #AttackSIND(23120013,on,150)
            AttackSemiNDMagic(23120013,23111002,0.54,on)
    elif job == 4100: #Hayato 1st 41001004
        AttackSI(41001004,on,100)
    elif job == 4110: #Hayato 2nd 41101000
        AttackSemiNDMagic(41101000,41101000,0.45,on)
    elif job == 4111: #Hayato 3rd 41111011
        AttackSemiNDMagic(41111011,41111011,0.45,on)
    elif job == 4112: #Hayato 4th 41121011
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(41121011,41121011,0.45,on)
    elif job == 3600:#Xenon 1st 36001000
        AttackSemiNDMagic(36001000,36001000,1.08,on)
    elif job == 3610:#Xenon 2nd 36101000
        AttackSemiNDMagic(36101000,36101000,0.99,on)
    elif job == 3611:#Xenon 3rd 36111000
        #AttackSemiNDMagic(36111000,36111000,1.8,on)
        AttackSemiNDMagic(36111009,36111009,0.81,on)
        #AttackSemiNDMagic(36111010,36111010,0.72,on)
    elif job == 3612:#Xenon 4th 36121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(36121001) >= 1:
                AttackSemiNDMagic(36121011,36121011,1.38,on)
            else:
                AttackSI(36121000,on,110)
    elif job == 2400: #Phantom 1st 24001000
        AttackSemiNDMagic(24001000,24001000,0.81,on)
    elif job == 2410: #Phantom 2nd 24101000
        AttackSemiNDMagic(24101000,24101000,0.99,on)
    elif job == 2411: #Phantom 3rd 24111000
        AttackSemiNDMagic(24111000,24111000,0.99,on)
    elif job == 2412: #Phantom 4th 24121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(24121010) >= 1 and Character.GetSkillLevel(24121000) >= 1:
                AttackSemiNDMagic(24121010,24121010,1.08,on)
                #SetSIND("24121010;24121000",140,on)
            elif Character.GetSkillLevel(24121010) >= 1:
                AttackSemiNDMagic(24121010,24121010,1.08,on)
            else:
                AttackSI(24121000,on,150)
    elif job == 15000: #Illium Pre 1st
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job in IlliumJobs: #Illium 1st+2nd+3rd+4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSIND(32120055,32120055,0.45,on)
        #AttackSIND("32120055;64001001",on,100)
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        else:
            Terminal.SetCheckBox("Skill Injection", False)
            Terminal.SetCheckBox("Melee No Delay",False)
            Terminal.SetCheckBox("Auto Attack",False)
            
            Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",on)
            Terminal.SetCheckBox("bot/illium/summon_control",on)
            Terminal.SetCheckBox("General FMA",on)
    elif job in CadenaJobs: #Cadena 1st + 2nd + 3rd 64001006 or 64001001
        if job != CadenaJobs[-1]:
            AttackSIND("64001001;64001006",on,100)
        else:
            if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
                #AttackSIND(32120055,32120055,0.45,on)
                #AttackSIND("32120055;64001001",on,100)
                #AttackSemiNDMagic(32120055,32120055,0.45,on) 
                AttackSI(32120055,on)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                BindSkill(32121052)
            else:
                AttackSIND("64120000;64001001",on,100)
    elif job in ArkJobs: #Ark 1st + 2nd + 3rd 155001100
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(155001100,155001100,0.85,on)
    elif job == 2001: #Evan pre 1st job
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 2200: #Evan 1st 22001010 AA
        AttackAuto(22001010,on)
    elif job == 2211: #Evan 2nd 22110010 SI/ND
        AttackSIND(22110010,on,100)
        
    elif job == 2214: #Evan 3rd 22140010 SI/ND
        AttackSIND(22140010,on,100)
        
    elif job == 2217: #Evan 4th 22170061 SI/ND
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(22170061,on,100)
        
    elif job == 0:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 100: #Swordman
        AttackAuto(1001005,on)
    elif job == 110: #fighter 1101011
        AttackAuto(1101011,on)
    elif job == 111: #crusader 1111010
        AttackSIND(1111010,on,450)
    elif job == 112: #Hero 1120017
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(1120017,on,100)
            #AttackSemiNDMagic(1120017,1120017,0.6,on)
    elif job == 120: #Page 1201011
        AttackSI(1201011,on)
    elif job == 121: #White knight 1211008
        #AttackAuto(1211008,on)
        AttackSI(1201011,on)
    elif job == 122: #Paladin 1211008
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1221004,1221004,0.81,on)
            '''
            while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame():
                for x in range(1,8,1):
                    Character.UseSkill(1221004)
                    time.sleep(0.02)
                time.sleep(0.02)
                Character.UseSkill(1221004)
                time.sleep(0.80)
            '''
    elif job == 130: #Spearman 1301011
        AttackSemiND(1301011,1301011,0.81,on)
        
    elif job == 131: #Berserker
        AttackSemiND(1301011,1301011,0.81,on)
        
    elif job == 132: #Dark Knight
        #AttackAuto(1321012,on)
        #AttackSIND(1321012,on,450)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1321012,1321012,0.84,on)
    elif job == 200: #Mage
        AttackAuto(2001008,on)
        
    elif job == 220: #IL wizard
        AttackAuto(2201005,on)
        
    elif job == 221: #IL mage
        AttackAuto(2211002,on)
        
    elif job == 222: #IL archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2221006,on)

        
    elif job == 210: #FP wizard
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 211: #FP mage
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 212: #FP archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2121006,on)
        
    elif job == 230: #cleric
        AttackAuto(2301005,on)
    elif job == 231: #priest
        AttackAuto(2311004,on)
    elif job == 232: #Bishop
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackSI(2321007,on,100,"SIRadioMagic")
    elif job == 300: #Archer
        AttackAuto(3001004,on)
        
    elif job == 310: #Hunter
        AttackAuto(3101005,on)
        
    elif job == 311: #Ranger
        AttackAuto(3111003,on)
        #AttackSIND(3111003,on,300)
        
    elif job == 312: #Bowmaster
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(3121015,on,100)
        
    elif job == 320: #Crossbowman
        AttackAuto(3201005,on)
    elif job == 321: #Sniper
        AttackAuto(3211009,on)
        #AttackSIND(3211009,on,400)
    elif job == 322: #Marksman
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(3221007,on)
    elif job == 400: #Thief
        
        if SCLib.GetVar("DualBlade"):
            if Character.GetSkillLevel(4001013) == 0:
                LevelSkill(4001013)
            AttackAuto(4001013,on)
        else:
            AttackAuto(4001334,on)
        if Character.GetSkillLevel(4001013) >= 1:
            SCLib.UpdateVar("DualBlade",True)
        else:
            SCLib.UpdateVar("DualBlade",False)
        
    elif job == 410: #Assassin
        AttackSI(4101008,on)
        
    elif job == 411: #Hermit
        AttackSI(4111015,on)
        
    elif job == 412: #nightlord
        #print(Character.GetSkillLevel(32121052))
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetSpinBox("KamiOffsetX", -85)
            AttackAuto(4121013,on)
        
    elif job == 420: #Bandit
        AttackSI(4201012,on)
        
    elif job == 421: #Chief Bandit
        AttackSI(4211002,on)
        
    elif job == 422: #Shadower
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(4221007,on)
            #AttackSemiNDMagic(4221007,4221007,1.1,on)
        
    elif job == 430: #dualblade
        if Character.GetSkillLevel(4001013) == 0:
            LevelSkill(4001013)
        elif Character.GetSkillLevel(4000012) < 10:
            LevelSkill(4000012)
        elif Character.GetSkillLevel(4001011) < 5:
            LevelSkill(4001011)
        elif Character.GetSkillLevel(4001003) < 10:
            LevelSkill(4001003)
        elif Character.GetSkillLevel(4001013) < 10:
            LevelSkill(4001013)
        AttackAuto(4001013,on)
    elif job == 431: #dualblade
        AttackAuto(4001013,on)
    elif job == 432:
        AttackSIND(4321004,on,450)
    elif job == 433:
        #AttackAuto(4321004,on)
        AttackSIND(4321004,on,450)
    elif job == 434: #dual blade 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(4341004,4341004,0.74,on)
    elif job == 500: #Pirate
        AttackAuto(5001002,on)
    elif job == 501: #Cannoneer Pirate
        #AttackAuto(5011000,on)
        AttackSIND(5011002,on,200)
    elif job == 510: #Brawler
        AttackAuto(5101012,on)
    elif job == 511: #Marauder
        AttackAuto(5111002,on)
    elif job == 512: #Buccaneer
        #AttackAuto(5121007,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5121017,5121007,1.25,on)
            #AttackSI(5121017,on,100)
    elif job == 520: #Gunslinger
        AttackAuto(5201001,on)
    elif job == 521: #Outlaw
        AttackAuto(5211008,on)
    elif job == 522: #Corsair
        #if level < 160:
        #    AttackSIND(5221017,on,350)
        #else:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5221017,5221017,0.85,on)
    elif job == 530: #Cannoneer
        #AttackAuto(5301001,on)
        #AttackSIND(5011002,on,200)
        if Character.GetSkillLevel(5301000) >= 1:
            AttackSIND("5301000;5011002",on,300)
            #AttackSemiNDMagic(5301000,5301000,0.90,on)
        else:
            attack_key = 0x44
            Key.Set(attack_key,1,5301001)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",400)
            Terminal.SetLineEdit("SISkillID",str(5011002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
    elif job == 531: #Cannon Trooper
        '''
        if Terminal.GetCheckBox("Mob Falldown"):
            AttackAuto(5311000,on)
        else:
            AttackAuto(5301001,on)
            Terminal.SetCheckBox("Speedy Gonzales",True)
        '''
        if Character.GetSkillLevel(5311000) >= 1:
            #AttackSemiNDMagic(5311000,5311000,0.96,on)
            AttackSIND("5311000;5011002",on,250)
        else:
            attack_key = 0x44
            Key.Set(attack_key,1,5301001)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",400)
            Terminal.SetLineEdit("SISkillID",str(5011002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
    elif job == 532: #Cannon Master
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND("5321000;5011002",on,250)
            #AttackSemiNDMagic(5321000,5321000,0.95,on)
    elif job == 508: #Jett 1sts
        AttackAuto(5081020,on)
    elif job == 570: #Jett 2nd
        #AttackAuto(5081020,on)
        if Character.GetSkillLevel(5701011) >= 1:
            #AttackSemiNDMagic(5701011,5701011,0.2,on,attackSpeed=4)
            AttackSIND(5701011,on,150)
        else:
            AttackAuto(5701010,on)
    elif job == 571: #Jett 3rd
        if Character.GetSkillLevel(5710020) >= 1:
            #AttackSemiNDMagic(5710020,5710020,0.9,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
        else:
            AttackSIND(5701011,on,150)
    elif job == 572: #Jett 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSemiNDMagic(5710020,5710020,0.4,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
    elif job == 1100: #Dawn warrior 1st
        AttackSI(11001020,on)
    elif job == 1110: #Dawn Warrior 2nd
        #AttackAuto(11101120,on)
        AttackSIND(11101120,on,600)
    elif job == 1111: #Dawn Warrior 3rd
        AttackSI(11111120,on)
        #AttackAuto(11111220,on)
    elif job == 1112: #Dawn Warrior 4th
        dummySkill = 11001020
        dummyDelay = 0.81
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,11111022):
                AttackSemiNDMagic(11121203,dummySkill,dummyDelay,on)
    elif job == 1200: #BW 1st
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
        ToggleLoot(False)
        Terminal.SetCheckBox("Full Map Attack",False)
    elif job == 1210: #BW 2nd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1211: #BW 3rd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1212: #BW 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:           
            #if level < 140:
            Terminal.SetCheckBox("Full Map Attack",True)
            AttackAuto(12001020,on)
                
            #elif level >= 140:
            #    Terminal.SetCheckBox("Full Map Attack",False)
            #    AttackSIND(12121055,on,31)
            
    elif job == 1300: #Wind Archer 1st
        AttackAuto(13001020,on)
    elif job == 1310: #Wind Archer 2nd
        if Character.GetSkillLevel(13101020) >= 1:
            AttackSI(13101020,on)
        else:
            AttackAuto(13001020,on)
    elif job == 1311: #Wind Archer 3rd
        #AttackAuto(13111020,on)
        AttackSI(13101020,on)
    elif job == 1312: #Wind Archer 4th
        #AttackAuto(13121002,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(13121002,on,siOption = "SIRadioShoot")
    elif job == 1400: #Night Walker 1st
        AttackAuto(14001020,on)
    elif job == 1410: #Night Walker 2nd
        AttackSI(14101020,on)
    elif job == 1411: #Night Walker 3rd
        AttackAuto(14111022,on)
    elif job == 1412: #Night Walker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(14111022,on)
    elif job == 1500: #Thunder breaker 1st
        #AttackAuto(15001020,on)
        if Character.GetSkillLevel(15001021) >= 1:
            #AttackSIND(15001021,on,600)
            AttackSemiNDMagic(15001021,15001021,0.8,on)
        else:
            AttackAuto(15001020,on)
    elif job == 1510: #Thunder breaker 2nd
        #AttackAuto(15101020,on)
        AttackSemiNDMagic(15101020,15101020,0.72,on)
    elif job == 1511: #Thunder breaker 3rd
        #AttackAuto(15111020,on)
        AttackSemiNDMagic(15111020,15111020,0.9,on)
    elif job == 1512: #Thunder breaker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(15121002,15121002,1.08,on)
            #30 * math.ceil(BaseDelay * (14)/480)
            #AttackSIND(15121002,on,500)
        #AttackSIND(15111020,on,300)
        #AttackAuto(15121001,on)
    elif job == 3300: #Wild Hunter 1st
        AttackAuto(33001105,on)
    elif job == 3310: #Wild Hunter 2nd
        #AttackAuto(33101113,on)
        AttackSI(33101215,on)
    elif job == 3311: #Wild Hunter 3rd
        AttackAuto(33111112,on)
        #AttackSI(33111010,on,100,"SIRadioMagic")
    elif job == 3312: #Wild Hunter 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(33111112,on)
    elif job == 3200: #Battle Mage 1st
        AttackSI(32001014,on)
    elif job == 3210: #Battle Mage 2nd
        #AttackSI(32100010,on)
        AttackSIND(32101001,on,250)
    elif job == 3211: #Batlle Mage 3rd
        #AttackSI(32110017,on)
        AttackSIND(32101001,on,250)
    elif job == 3212: #Battle Mage 4th
        if level >= 160:
            if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
                #AttackSemiNDMagic(32120055,32120055,0.45,on) 
                AttackSI(32120055,on)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            if SCLib.GetVar("DoingZakum"):
                #AttackAuto(32121002,on)
                AttackSIND(32101001,on,250)
            else:
                #AttackSI(32120019,on)
                AttackSIND(32101001,on,250)
    elif job == 3700: #Blaster 1st
        Terminal.SetCheckBox("General FMA",False)
        AttackAuto(37001000,on)
    elif job == 3710: #Blaster 2nd
        #Terminal.SetCheckBox("General FMA",on)
        Terminal.SetCheckBox("General FMA",False)
        AttackAuto(37001000,on)
    elif job == 3711: #Blaster 3rd
        #AttackAuto(37001000,on)
        AttackSI(37110006,on,80)
        Terminal.SetCheckBox("General FMA",on)
        #Terminal.SetCheckBox("General FMA",on)
    elif job == 3712: #Blaster 4th
        #AttackAuto(37001000,on)
        Terminal.SetCheckBox("General FMA",False)
        #vulcan()
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(37121000,on,80)
    elif job == 3500: #Mechanic 1st
        AttackAuto(35001004,on)
    elif job == 3510: #Mechanic 2nd
        AttackAuto(35101001,on)
    elif job == 3511: #Mechanic 3rd
        AttackAuto(35111006,on)
    elif job == 3512: #Mechanic 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(35111015,35111015,0.84,on)
            #AttackSI(35121015,on,250)
        #AttackAuto(35111006,on)
    elif job == 11212: #Beast Tamer
        #if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
        #    #AttackSemiNDMagic(32120055,32120055,0.45,on) 
        #AttackSI(32120055,on)
        #elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
        #    BindSkill(32121052)
        #else:
        if Character.HasBuff(2,110001501):
            if Character.GetSkillLevel(112000003) >= 1:
                #AttackSIND(112000003,on,450)
                AttackSemiNDMagic(112000003,112001008,0.38,on)
            else:
                if level <= 17:
                    AttackAuto(112000000,on)
                    
                elif level >= 17 and (not useExploit or SCLib.GetVar("DoingZakum")):
                    Terminal.SetCheckBox("Auto Attack", False)
                    Terminal.SetCheckBox("Skill Injection", False)
                    Terminal.SetCheckBox("Melee No Delay",False)
                    count = 0
                    if on and not Terminal.IsRushing():
                        while count < 100 and len(Field.GetMobs())>0: #constantly presses control to simulate human actions
                            Key.Down(0x11)
                            time.sleep(0.1)
                            Key.Up(0x11)
                            time.sleep(0.1)
                            count += 1
                            if len(Field.GetMobs())==0:
                                break
    elif job == 2000:#Aran pre
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
        
    elif job == 2100 or job == 2110: #Aran 1st 21000007
        AttackSI(21000006,on,80)
        #AttackSemiNDMagic(21000006,21000006,0.4,on)
            

    elif job == 2111 or job == 2112: #Aran 3rd
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSemiNDMagic(21111021,21111021,0.81,on)
            SetSIND("21110028;21100018",100,True)
            #if Character.HasBuff(2,21110016):
            #    AttackSIND(21111021,on,450)
            #else:
            #    AttackSIND(21111021,on,400)
            #AttackSemiNDMagic(21111021,21111021,0.65,on)
            #Terminal.SetCheckBox("Speedy Gonzales",True)
            '''
            elif job == 2110 or job == 2111 or job == 2112: #Aran 2nd+3rd+4th 21000007
                Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
                Key.Set(attack_key,1,21001010)
                Terminal.SetLineEdit("SISkillID","21100018")
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetSpinBox("SkillInjection",30)
                Terminal.SetCheckBox("Auto SP",True)
                Terminal.SetCheckBox("Melee No Delay",on)
                #Terminal.SetRadioButton("SIRadioMagic",True)
                Terminal.SetCheckBox("Auto Attack", False)
                Terminal.SetComboBox("AttackKey",33)
                Terminal.SetSpinBox("autoattack_spin",100)
            '''
    elif job == 14200:# Kinesis 1st
        AttackSemiNDMagic(142001001,142001001,0.63,on,attackSpeed = 5)
    elif job == 14210: #Kinesis 2nd 142101002
        AttackSemiNDMagic(142101002,142101002,0.79,on,attackSpeed = 5)
        #AttackAuto(142101002,on)
    elif job == 14211 or job == 14212: #Kinesis 3rd + 4th 142111002
        #
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if job == 14211:
                Terminal.SetCheckBox("Instant Final Smash",True)
            else:
                Terminal.SetCheckBox("Instant Final Smash",False)
            AttackAuto(142111002,on)
            #AttackSemiNDMagic(142101002,142101002,0.79,on,attackSpeed = 5)
        
    elif job == 6500: #AB 1st
        AttackSemiNDMagic(60011216,60011216,0.6,on)
    elif job == 6510: #AB 2nd
        AttackSemiNDMagic(65001100,65001100,0.57,on)
    elif job == 6511: #AB 3rd
        #AttackSI(65111002,on,100,"SIRadioMagic")
        AttackSemiNDMagic(65111002,65111002,1.2,on)
    elif job == 6512: #AB 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if SCLib.GetVar("DoingZakum"):
                AttackSI(65121008,on)
            else:
                AttackSemiNDMagic(65121100,65111002,1.2,on)
    elif job in KaiserJobs and job != KaiserJobs[3]: #Kaiser 1st 2nd 3rd 4th
        AttackSemiNDMagic(61001005,61001005,0.36,on)
    elif job == KaiserJobs[3]:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(61001005,61001005,0.36,on)
    elif job == 2500: #Shade 1st
        AttackAuto(25001000,on)
    elif job == 2510: #Shade 2nd
        AttackSemiNDMagic(25101000,25101000,1.19,on)
    elif job == 2511: #Shade 3rd
        AttackSIND(25110001,on,300)
        #AttackSemiNDMagic(25110001,2511001,0.99,on)
        #AttackSIND(25111000,on,800)
    elif job == 2512: #Shade 4th
        #AttackSI(25120003,on,100)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(25121000) >= 1:
                AttackSemiNDMagic(25121000,25121000,0.63,on)
            else:
                AttackSIND(25110001,on,300)
    elif job == 5100: #Mihile 1st
        AttackAuto(51001004,on)
        #AttackSemiNDMagic(51001004,51001004,0.96,on)
    elif job == 5110: #Mihile 2nd
        #AttackSIND(51101005,on,800)
        AttackSemiNDMagic(51101005,51001004,0.96,on)
    elif job == 5111: #Mihile 3rd
        AttackSemiNDMagic(51111006,51111006,0.84,on)
        #AttackSIND(51111006,on,600)
    elif job == 5112: #Mihile 4th
        delay = 0.84
        if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
            #AttackSemiNDMagic(32120055,32120055,0.45,on) 
            AttackSI(32120055,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(51121009,51111006,0.84,on)
            #AttackSIND(51121009,on,400)
    elif job == 330 or job == 331 or job == 332:
        AttackSIND("3301003",on,1,siOption = "si_cadena")
    else:
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Skill Injection", False)
        #print("Not any of the listed jobs, not going to attack for safety")
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)