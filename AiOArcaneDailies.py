import Character,Field,Inventory,Key,Npc,Packet,Quest,Terminal,time,GameState,sys,os,Party,json,Login,datetime

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")

try:
    import SunCat, SCHotkey, SCLib
except:
    print("Couldn't find SunCat module")

#SunCat's All-in-one Dailies

#Change these
#--------------------------------------------------
dailyVJ = True
dailyChuChu = True
dailyDD = False
dailySS = True

SCLib.StartVars()
###persist variables
if SCLib.GetVar("ToggleAttack") is None:
    SCLib.PersistVar("ToggleAttack", False)

if GameState.IsInGame():
    if Quest.GetQuestState(34120) != 2:
        #print("You havn't completed VJ storyline quests yet. Disable VJ daily")
        dailyVJ = False
    if Quest.GetQuestState(34218) != 2:
        #print("You havn't completed ChuChu storyline quests yet. Disable Chuchu daily")
        dailyChuChu = False
    if Quest.GetQuestState(34330) != 2:
        #print("You havn't completed Lachelein storyline quests yet. Disable Dream Defender daily")
        dailyDD = False
    if Quest.GetQuestState(34479) != 2:
        #print("You havn't completed Arcana storyline quests yet. Disable Sirit Savior daily")
        dailySS = False

kamiOffsetX = -100
kamiOffsetY = -50

#ChuChu
chuChuHardMode = True

#Dream Defender
ddLevelSelect = 30 #This is the stage you will enter
ddExitLevel = 31 #This is the stage you will exit

#Spirit Savior
npcChatKey = 0x20 #NPC chat key (default spacebar)
killTime = 1.2 #How long it takes you to kill the mob (can be set to a fraction)
waitTime = 0.5 #How long to wait after killing before picking up (for lag reasons)
roundWaitTime = 0.5 #How long to wait when handing in spirits
roundsPerRun = 15 #How many times you want to collect 5 spirits per run
totalRuns = 1 #How many times you want to enter spirit savior

#--------------------------------------------------

#Don't touch anything below this
#--------------------------------------------------

symbolMaxTries = 20

#Vanishing Journey
vjQuests = []

vjMap = 450001000
vjNPC = 3003104

#ChuChu
ccStartingMap = 450002023
ccExitMap     = 450002024
ccNpc         = 3003166
hungryMutoMaps = [921170050, 921170100, 921170101, 921170102, 921170103, 921170104, 921170105]
allIngredients = []
allRecipes = []
currentRecipe = None

#Dream Defender
ddStartingMap = 450004000
ddMap = 921171000
ddMapEnd = 921171099
ddExitMap = 921171100
ddNpc = 9010100
ddPurpleBoxes = [9833080, 9833081, 9833082, 9833083, 9833084]
#ddYellowBox = 9833072
#ddFilterMobs = [9833090, 9833091]
ddRestX = 3400
ddRestY = -650

#Spirit Savior
ssStartingMap = 450005000
ssExitMap = 921172400
ssMapStart = 921172300
ssMapEnd = 921172399
ssMobArray = [8644101, 8644102, 8644103, 8644104, 8644105, 8644106, 8644107, 8644108, 8644109, 8644110, 8644111, 8644112]
ssBaseX = -175
ssBaseY = -491
ssNpc = 3003381
enemyMobs = [8644201, 8644301, 8644302, 8644303, 8644304, 8644305]

#Gollux
secondMap = [863010400]
thirdMap = [863010410]
fourthMap = [863010420]
heartMap = [863010500]
headMap = [863010600]
###Jobs, Jobs[0] = 1st job, Jobs[1] = 2nd job etc###
KannaJobs = [4200, 4210, 4211, 4212]
LuminousJobs = [2700, 2710, 2711, 2712]
ArkJobs = [15500, 15510, 15511, 15512]
BlasterJobs = [3700, 3710, 3711, 3712]
DemonAvengerJobs = [3101, 3120, 3121, 3122]
DemonSlayerJobs = [3100, 3110, 3111, 3112]
AranJobs = [2000,2100, 2110, 2111, 2112]
MercedesJobs = [2300, 2310, 2311, 2312]
HayatoJobs = [4100, 4110, 4111, 4112]
BattleMageJobs = [3200, 3210, 3211, 3212]
WildHunterJobs = [3300, 3310, 3311, 3312]
KaiserJobs = [6100, 6110, 6111, 6112]
MihileJobs = [5100, 5110, 5111, 5112]
AngelicBusterJobs = [6500, 6510, 6511, 6512]
XenonJobs = [3600, 3610, 3611, 3612]
PhantomJobs = [2400, 2410, 2411, 2412]
EvanJobs = [2200, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218]
IlliumJobs = [15200,15210,15211,15212]
CadenaJobs = [6400,6410,6411,6412]
job = Character.GetJob()
HotKey = 0x79
try:
    SCHotkey.StartHotkeys(100)
except:
    SCHotkey.StopHotkeys()
def KillPersistVarThred():
    print("Restarting SCLib variables")
    SCLib.StopVars()
    time.sleep(1)
SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F10

def startupCheck(accountId):
    split_id = accountId.split("@")[0]
    if os.path.exists('info/{}.json'.format(split_id)):
        #print("Loading")
        with open('info/{}.json'.format(split_id)) as f:
            return json.load(f)
    else:
        print("Creating")
        with open('info/{}.json'.format(split_id), "w+") as db_file:
            db_file.write(json.dumps({}))
            return {}

def handleReady(data):
    if 'daily_start' not in data:
        data['daily_start'] = 1
    if 'daily_end' not in data:
        data['daily_end'] = 1
    if 'cur_pos' not in data:
        data['cur_pos'] = Terminal.GetLineEdit("LoginChar")
    if 'changing_mule' not in data:
        data['changing_mule'] = False
    if 'date' not in data:
        data['date'] = str(datetime.datetime.utcnow().date())
    if 'daily_done' not in data:
        data['daily_done'] = False
    if 'done_char' not in data:
        data['done_char'] = []
    if 'training_done' not in data:
        data['training_done'] = False
    if 'training_char' not in data:
        data['training_char'] = 7
def writeJson(data,accountId):
    split_id = accountId.split("@")[0]
    with open('info/{}.json'.format(split_id), 'w') as outfile:
        parsed = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(parsed)
        outfile.close()

accountId = Terminal.GetLineEdit("LoginID")
accountData = startupCheck(accountId)
handleReady(accountData)
writeJson(accountData,accountId)

current_date = str(datetime.datetime.utcnow().date())
#check if date changed
if current_date != accountData['date']:
    accountData['date'] = current_date
    accountData['daily_done'] = False
    accountData['done_char'][:] = []
    writeJson(accountData,accountId)
    print("It's a new day!")
    KillPersistVarThred()

#check if done doing dailies on all characters
if len(accountData['done_char']) == accountData['daily_end'] - accountData['daily_start'] + 1 and not accountData['daily_done']:
    accountData['daily_done'] = True
    Terminal.SetLineEdit("LoginChar",str(accountData['training_char']))
    writeJson(accountData,accountId)
    print("Finished dailies on every char")

#change character to next char
if accountData["cur_pos"] in accountData['done_char'] and not accountData['daily_done']:
    print("Logging out to move to next char")
    Terminal.Logout()
#return to farming char
if accountData['cur_pos'] != str(accountData['training_char']) and accountData['daily_done'] and GameState.IsInGame():
    print("Loggin out ot return to farming char")
    Terminal.Logout()

def initAttack():
    print("Initializing attack settings for this character")
    attack_key = 0x44
    pgup_key = 0x21
    Terminal.SetComboBox("Familiar0",1)
    Terminal.SetCheckBox("Mob Falldown",False)
    if job == 3712:
        
        Terminal.SetLineEdit("SISkillID","37121003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job ==4212: #4th
        print("Setting up Settings for Kanna")
        Terminal.SetSpinBox("MonkeySpiritsNDcheck",40)
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",True)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",True)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetCheckBox("Auto Attack",True)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Key.Set(0x47,1,42111003)
    elif job == 2712: #lumi fourth job
        print("Setting up Settings for Luminous")
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        if Character.HasBuff(2,20040216): #Light Mode
            Key.Set(attack_key,1,27121100)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            Key.Set(attack_key,1,27111303)
        else:                              #Dark Mode
            Key.Set(attack_key,1,27121202)
        Terminal.SetCheckBox("Skill Injection", False)
        
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3122: #DA fourth job
        print("Setting up Settings for DA")
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31211000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3112: #DS fourth job
        print("Setting up Settings for DS")
        Terminal.SetLineEdit("SISkillID","31121010")
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2312: #Mercedes 4th
        print("Setting up Settings for Mercedes")
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,23111000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4112: #Hayato 4th 41121011
        print("Setting up Settings for Hayato")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","41121011")
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3612:#Xenon 4th 36121000
        print("Setting up Settings for Xenon")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","36121000")
        Terminal.SetSpinBox("SkillInjection",80)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2412: #Phantom 4th 24121000
        print("Setting up Settings for Phantom")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","24121000")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetSpinBox("SkillInjection",110)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 15212: #Illium 4th
        print("Setting up Settings for Illium")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",True)
        Terminal.SetCheckBox("bot/illium/summon_control",True)
        Terminal.SetCheckBox("General FMA",True)
    elif job == 6412: # Cadena 4th job
        print("Setting up Settings for Cadena")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","64001006")
        Terminal.SetSpinBox("SkillInjection",150)
        
        Terminal.SetRadioButton("si_cadena",True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 15512: #Ark 4th 155121007 @50
        print("Setting up Settings for Ark")
        Terminal.SetLineEdit("SISkillID", "155001100")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetSpinBox("SkillInjection",700)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2217: #Evan 4th 22170061 SI/ND
        print("Setting up Settings for Evan")
        Terminal.SetLineEdit("SISkillID", "22170061")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",True)
        
        Terminal.SetSpinBox("SkillInjection",80)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetCheckBox("dragon_kami",False)
    elif job == 2112: #Aran 4th 21000007
        print("Setting up Settings for Aran")
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
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
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 14212: # Kinesis 4th 142111002
        print("Setting up Settings for Kinesis")
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,142111002)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 6512: #AB 4th
        print("Setting up Settings for AB")
        Terminal.SetLineEdit("SISkillID","65121100")
        Terminal.SetCheckBox("Auto Attack", False)
        
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("General FMA",True)
    elif job == 3512: #mechanic 4th 400051012
        #mech_att(on)
        print("Setting up Settings for Mechanic")
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetLineEdit("SISkillID","400051012")
        Terminal.SetCheckBox("Auto Attack", False)
        
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2512: #Shade 4th
        print("Setting up Settings for Shade")
        Terminal.SetLineEdit("SISkillID","25120003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 1212: #BW 4th
        print("Setting up Settings for Blaze Wizard")
        Terminal.SetLineEdit("SISkillID","12121055")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 572: #Jett 4th
        print("Setting up Settings for Jett")
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetLineEdit("SISkillID","5710020")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Melee No Delay",True)
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)

def initAttackDone():
    print("Initializing done attack settings for this character")
    attack_key = 0x44
    pgup_key = 0x21
    Terminal.SetComboBox("Familiar0",5)
    Terminal.SetCheckBox("Rush By Level",True)
    if job == 3712:
        print("Setting up settings for Blaster")
        Terminal.SetLineEdit("SISkillID","37121003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",1)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job ==4212: #4th
        print("Setting up Settings for Kanna")
        Terminal.SetSpinBox("MonkeySpiritsNDcheck",40)
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",True)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",True)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetCheckBox("Auto Attack",True)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Key.Set(0x47,1,42111003)
    elif job == 2712: #lumi fourth job
        print("Setting up Settings for Luminous")
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        if Character.HasBuff(2,20040216): #Light Mode
            Key.Set(attack_key,1,27121100)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            Key.Set(attack_key,1,27111303)
        else:                              #Dark Mode
            Key.Set(attack_key,1,27121202)
        Terminal.SetCheckBox("Skill Injection", False)
        
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3122: #DA fourth job
        print("Setting up Settings for DA")
        Key.Set(pgup_key, 1, 31011001)
        Key.Set(attack_key,1,31211000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3112: #DS fourth job
        print("Setting up Settings for DS")
        Terminal.SetLineEdit("SISkillID","31121010")
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2312: #Mercedes 4th
        print("Setting up Settings for Mercedes")
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,23111000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4112: #Hayato 4th 41121011
        print("Setting up Settings for Hayato")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","41121011")
        Terminal.SetSpinBox("SkillInjection",150)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3612:#Xenon 4th 36121000
        print("Setting up Settings for Xenon")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","36121000")
        Terminal.SetSpinBox("SkillInjection",80)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2412: #Phantom 4th 24121000
        print("Setting up Settings for Phantom")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","24121000")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetSpinBox("SkillInjection",110)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 15212: #Illium 4th
        print("Setting up Settings for Illium")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",True)
        Terminal.SetCheckBox("bot/illium/summon_control",True)
        Terminal.SetCheckBox("General FMA",True)
    elif job == 6412: # Cadena 4th job
        print("Setting up Settings for Cadena")
        Key.Set(pgup_key, 2, 2001582)
        Terminal.SetLineEdit("SISkillID","64001006")
        Terminal.SetSpinBox("SkillInjection",150)
        
        Terminal.SetRadioButton("si_cadena",True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 15512: #Ark 4th 155121007 @50
        print("Setting up Settings for Ark")
        Terminal.SetLineEdit("SISkillID", "155001100")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetSpinBox("SkillInjection",700)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
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
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
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
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 14212: # Kinesis 4th 142111002
        print("Setting up Settings for Kinesis")
        Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,142111002)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 6512: #AB 4th
        print("Setting up Settings for AB")
        Terminal.SetLineEdit("SISkillID","65121100")
        Terminal.SetCheckBox("Auto Attack", False)
        
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("General FMA",True)
    elif job == 3512: #mechanic 4th 400051012
        #mech_att(on)
        print("Setting up Settings for Mechanic")
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetLineEdit("SISkillID","400051012")
        Terminal.SetCheckBox("Auto Attack", False)
        
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2512: #Shade 4th
        print("Setting up Settings for Shade")
        Terminal.SetLineEdit("SISkillID","25120003")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 1212: #BW 4th
        print("Setting up Settings for Blaze Wizard")
        Terminal.SetLineEdit("SISkillID","12121055")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 572: #Jett 4th
        print("Setting up Settings for Jett")
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetLineEdit("SISkillID","5710020")
        Terminal.SetCheckBox("Auto Attack", False)
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Melee No Delay",True)
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)

if not GameState.IsInGame() and not GameState.IsInCashShop() and not SCLib.GetVar("ToggleAttack"):
    SCLib.UpdateVar("ToggleAttack",True)
    print("Enabling TogglaAttack Flag")

if GameState.IsInGame() and accountData['daily_done'] and SCLib.GetVar("ToggleAttack"):
    initAttackDone()
    SCLib.UpdateVar("ToggleAttack",False)
if GameState.IsInGame() and not accountData['daily_done'] and SCLib.GetVar("ToggleAttack"):
    initAttack()
    SCLib.UpdateVar("ToggleAttack",False)

def initVars():
    SCLib.PersistVar("StartingMap", Field.GetID())
    SCLib.PersistVar("UsingKami", Terminal.GetCheckBox("Kami Vac"))
    SCLib.PersistVar("UsingSI", Terminal.GetCheckBox("Skill Injection"))
    SCLib.PersistVar("UsingFMA", Terminal.GetCheckBox("Full Map Attack"))
    SCLib.PersistVar("UsingGFMA", Terminal.GetCheckBox("General FMA"))
    SCLib.PersistVar("UsingWhitelist", Terminal.GetPushButton("Whitelist"))
    SCLib.PersistVar("UsingAutoBuff", Terminal.GetCheckBox("Auto Buff"))
    SCLib.PersistVar("CurDaily", "VJ")
    SCLib.PersistVar("CurQuest", None)
    SCLib.PersistVar("SymbolCount", 0)
    SCLib.PersistVar("CurSSRuns", 0)
    
    SCLib.PersistVar("CurStep", "StartingVJ")

    SCLib.PersistVar("RetryCount", 0)

    SCLib.StartVars()

def useSymbol(symbol):
    if symbol.valid and SCLib.GetVar("SymbolCount") < symbolMaxTries:
        oPacket = Packet.COutPacket(SCLib.PacketHeader["Symbols"])
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(symbol.pos) #inv slot
        oPacket.Encode4(0xFFFFF9BB) #???
        Packet.SendPacket(oPacket)
        SCLib.UpdateVar("SymbolCount", SCLib.GetVar("SymbolCount") + 1)
        return True
    else:
        SCLib.UpdateVar("SymbolCount", 0)
        return False

class VJQuest:
    quest = None
    killmap = None
    completemap = None
    npc = None
    npcx = None
    npcy = None
    
    def __init__(self, q, km, cm=vjMap, n=vjNPC, snx=-2233, sny=60):
        self.quest = q
        self.killmap = km
        self.completemap = cm
        self.npc = n
        self.npcx = snx
        self.npcy = sny
        
    def IsActive(self):
        if Quest.GetQuestState(self.quest) == 1:
            return True
        return False
    
    def DoQuest(self):        
        if Quest.GetQuestState(self.quest) == 1:
            curMap = Field.GetID()
            SCLib.UpdateVar("CurQuest", self.quest)
            if Quest.CheckCompleteDemand(self.quest, self.npc):
                if curMap != self.killmap:
                    Terminal.Rush(self.killmap)
            else:
                if curMap != self.completemap:
                    Terminal.Rush(self.completemap)
                else:
                    if Terminal.GetCheckBox("Kami Vac"):
                        Terminal.SetCheckBox("Kami Vac", False)
                    
                    if Character.GetPos().x != self.npcx:
                        SunCat.Teleport(self.npcx, self.npcy)
                    time.sleep(1)
                    Quest.CompleteQuest(self.quest, self.npc)
                    time.sleep(2)
                    if SCLib.GetVar("UsingKami"):
                        Terminal.SetCheckBox("Kami Vac", True)
                    
                    SCLib.UpdateVar("CurQuest", None)
                    
def initVJ():
    vjQuests.append(VJQuest(34130, 450001010))
    vjQuests.append(VJQuest(34131, 450001012))
    vjQuests.append(VJQuest(34132, 450001014))
    vjQuests.append(VJQuest(34133, 450001016))
    vjQuests.append(VJQuest(34134, 450001110))
    vjQuests.append(VJQuest(34135, 450001112))
    vjQuests.append(VJQuest(34136, 450001114))
    vjQuests.append(VJQuest(34137, 450001210))
    vjQuests.append(VJQuest(34138, 450001210))
    vjQuests.append(VJQuest(34139, 450001010))
    vjQuests.append(VJQuest(34140, 450001012))
    vjQuests.append(VJQuest(34141, 450001014))
    vjQuests.append(VJQuest(34142, 450001016))
    vjQuests.append(VJQuest(34143, 450001110))
    vjQuests.append(VJQuest(34144, 450001112))
    vjQuests.append(VJQuest(34145, 450001114))
    vjQuests.append(VJQuest(34146, 450001210))
    vjQuests.append(VJQuest(34147, 450001210))
    vjQuests.append(VJQuest(34148, 450001013, 450001013, 3003107, 991, -898))
    vjQuests.append(VJQuest(34149, 450001112, 450001112, 3003108, 74, -710))
    vjQuests.append(VJQuest(34150, 450001216, 450001216, 3003109, -1079, -149))

def acceptVJ():
    curMap = Field.GetID()
    if curMap != vjMap:
        Terminal.Rush(vjMap)
        return

    if Terminal.GetCheckBox("Kami Vac"):
        Terminal.SetCheckBox("Kami Vac", False)
    
    Terminal.SetCheckBox("Auto NPC", True)
    if Character.GetPos().x != -2233:
        SunCat.Teleport(-2233, 60)
    time.sleep(0.1)
    if Quest.GetQuestState(34128) != 2:
        Quest.StartQuest(34128,vjNPC)
        time.sleep(1.5)
        Quest.CompleteQuest(34128,vjNPC)
    #Quest.StartQuest(34128, vjNPC)
    
    Npc.ClearSelection()
    #Npc.RegisterSelection("[Daily Quest] Vanishing Journey")
    Npc.RegisterSelection("Those are all")
    time.sleep(3)
    Quest.StartQuest(34129, vjNPC)
    time.sleep(3)
    #Character.TalkToNpc(vjNPC)
    #time.sleep(1)
    
    if SCLib.GetVar("UsingKami"):
        Terminal.SetCheckBox("Kami Vac", True)
        
    SCLib.UpdateVar("CurStep", "DoingVJ")
    
def doVJ():
    if dailyVJ:
        initVJ()
        
        counter = -1
        
        if SCLib.GetVar("CurStep") == "StartingVJ":
            print("Starting Vanishing Journey")
            acceptVJ()
        elif SCLib.GetVar("CurStep") == "DoingVJ":
            counter = 0
            for q in vjQuests:
                if q.IsActive():
                    counter += 1
                
                if SCLib.GetVar("CurQuest") == None or SCLib.GetVar("CurQuest") == q.quest:
                    q.DoQuest()
            if counter == 0:
                SCLib.UpdateVar("CurStep", "FinishedVJ")
        elif SCLib.GetVar("CurStep") == "FinishedVJ":
            print("Finishing VJ")
            if not Quest.CheckCompleteDemand(34129, vjNPC):
                Quest.CompleteQuest(34129, vjNPC)

            vjSymbol = Inventory.FindItemByID(1712001)
            if not useSymbol(vjSymbol):
                print("Finished VJ")
                SCLib.UpdateVar("CurDaily", "ChuChu")
                SCLib.UpdateVar("CurStep", "InitChuChu")
        
    else:
        print("Skipping VJ")
        SCLib.UpdateVar("CurDaily", "ChuChu")
        SCLib.UpdateVar("CurStep", "InitChuChu")
        
#ChuChu
class Ingredient:
    name = ""
    mobID = 0
    itemID = 0
    
    def __init__(self, nm, mid, iid):
        self.name = nm
        if chuChuHardMode:
            self.mobID = mid
        else:
            self.mobID = mid - 20
        self.itemID = iid
    
    def GetMob(self):
        mobCheck = Field.FindMob(self.mobID)
        if mobCheck.valid:
            return mobCheck
        
        return None
    
    def GetDrop(self):
        dropCheck = Field.FindItem(self.itemID)
        if dropCheck.valid:
            return dropCheck
            
        return None
    
    def HandIn(self):
        hiPacket = Packet.COutPacket(SCLib.PacketHeader["ChuChu"])
        hiPacket.Encode1(0x02)
        hiPacket.EncodeString("pt_mutoHotPot")
        hiPacket.EncodeBuffer("0592 0093")
        Packet.SendPacket(hiPacket)
        time.sleep(2)
    
    def GetIngredient(self, amount):
        curAmount = 0
        firstAmount = SunCat.GetChuChu()
        
        while curAmount < amount:
            if Field.GetID() not in hungryMutoMaps or GameState.IsInGame() == False:
                break
            curAmount = SunCat.GetChuChu()
            if curAmount == firstAmount:
                curAmount = 0
            
            curDrop = self.GetDrop()
            if curDrop is not None:
                if self.name == "Slurpy Fruit":
                    while self.GetDrop() is not None:
                        if Field.GetID() not in hungryMutoMaps or GameState.IsInGame() == False:
                            break
                        SunCat.KamiTP(curDrop.x, curDrop.y)
                        Character.LootItem()
                        time.sleep(0.1)
                else:
                    SunCat.KamiTP(curDrop.x, curDrop.y)
                    Character.LootItem()
            else:
                curMob = self.GetMob()
                if curMob is not None:
                    SunCat.KamiTP(curMob.x + kamiOffsetX, curMob.y + kamiOffsetY)
            
            time.sleep(0.1)
        
        self.HandIn()

class Recipe:
    name = ""
    ingredients = []
    amounts = []
    
    def __init__(self, nm, igs, amts):
        self.name = nm
        self.ingredients = igs
        self.amounts = amts

def InitIngredients():
    allIngredients.append(Ingredient("Savory Fin", 9833054, 2435864))
    allIngredients.append(Ingredient("Tart Fins", 9833062, 2435865))
    allIngredients.append(Ingredient("Fresh Mane", 9833052, 2435860))
    allIngredients.append(Ingredient("Zesty Mane", 9833060, 2435861))
    allIngredients.append(Ingredient("Sweet Hoof", 9833050, 2435856))
    allIngredients.append(Ingredient("Spicy Hoof", 9833058, 2435857))
    allIngredients.append(Ingredient("Slimy Feather", 9833056, 2435868))
    allIngredients.append(Ingredient("Sticky Feather", 9833064, 2435869))
    allIngredients.append(Ingredient("Unpleasant Talon", 9833057, 2435870))
    allIngredients.append(Ingredient("Chewy Talon", 9833065, 2435871))
    allIngredients.append(Ingredient("Greasy Peel", 9833051, 2435858))
    allIngredients.append(Ingredient("Sour Peel", 9833059, 2435859))
    allIngredients.append(Ingredient("Crunchy Shell", 9833055, 2435866))
    allIngredients.append(Ingredient("Soft Shell", 9833063, 2435867))
    allIngredients.append(Ingredient("Soft Sole", 9833053, 2435862))
    allIngredients.append(Ingredient("Chewy Sole", 9833061, 2435863))
    allIngredients.append(Ingredient("Slurpy Fruit", 9833066, 2435872))
        
def InitRecipes():
    InitIngredients()
    
    #Easy Mobs
    allRecipes.append(Recipe("Fried Treat", [allIngredients[4], allIngredients[2]], [5, 10]))
    allRecipes.append(Recipe("Savory Stir Fry", [allIngredients[10], allIngredients[14]], [5, 10]))
    allRecipes.append(Recipe("Nummy Noodles", [allIngredients[4], allIngredients[2], allIngredients[0]], [5, 5, 10]))
    allRecipes.append(Recipe("Steamy Surprise", [allIngredients[10], allIngredients[14], allIngredients[12]], [5, 5, 10]))
    allRecipes.append(Recipe("Weird Wrap", [allIngredients[2], allIngredients[0], allIngredients[6]], [5, 5, 10]))
    allRecipes.append(Recipe("Gamey Soup", [allIngredients[0], allIngredients[12], allIngredients[8]], [5, 5, 10]))
    allRecipes.append(Recipe("Mystery Roast", [allIngredients[10], allIngredients[14], allIngredients[6], allIngredients[16]], [5, 5, 10, 1]))
    allRecipes.append(Recipe("Mystery Roast", [allIngredients[2], allIngredients[12], allIngredients[8], allIngredients[16]], [5, 5, 10, 1]))
    
    #Hard Mobs
    allRecipes.append(Recipe("Fried Squish", [allIngredients[5], allIngredients[3]], [5, 10]))
    allRecipes.append(Recipe("Dumpling Delights", [allIngredients[11], allIngredients[15]], [5, 10]))
    allRecipes.append(Recipe("Funky Pizza", [allIngredients[5], allIngredients[3], allIngredients[1]], [5, 5, 10]))
    allRecipes.append(Recipe("Juicy Buns", [allIngredients[11], allIngredients[15], allIngredients[13]], [5, 5, 10]))
    allRecipes.append(Recipe("Yucky Pickles", [allIngredients[3], allIngredients[1], allIngredients[7]], [5, 5, 10]))
    allRecipes.append(Recipe("Chewy Porridge", [allIngredients[1], allIngredients[13], allIngredients[9]], [5, 5, 10]))
    allRecipes.append(Recipe("Fruit Salad", [allIngredients[11], allIngredients[15], allIngredients[7], allIngredients[16]], [5, 5, 10, 1]))
    allRecipes.append(Recipe("Spicy Sausage", [allIngredients[3], allIngredients[13], allIngredients[9], allIngredients[16]], [5, 5, 10, 1]))
    
def changeChannel():
    print("Changing channel, please wait...")
    curChannel = GameState.GetChannel()
    
    while curChannel == GameState.GetChannel():
        Terminal.ChangeChannel(0)
        time.sleep(8)

def createParty():
    cpPacket = Packet.COutPacket(SCLib.PacketHeader["Party"])
    cpPacket.EncodeBuffer("01 00 10 00 42 65 73 74 20 70 61 72 74 79 20 65 76 65 72 21")
    Packet.SendPacket(cpPacket)

def leaveParty():
    lpPacket = Packet.COutPacket(SCLib.PacketHeader["Party"])
    lpPacket.EncodeBuffer("02 00")
    Packet.SendPacket(lpPacket)
    
def initChuChu():
    if Field.GetID() != ccStartingMap:
        Terminal.Rush(ccStartingMap)
    else:
        SunCat.HookChuChu()
        
        Terminal.SetCheckBox("Auto NPC", True)
        Terminal.SetCheckBox("Kami Vac", False)
        Terminal.SetCheckBox("Full Map Attack", False)
        Terminal.SetCheckBox("General FMA", False)
        Terminal.SetPushButton("Whitelist", False)
        
        changeChannel()
        
        SCLib.UpdateVar("CurStep", "StartingChuChu")

def startChuChu():
    if Field.GetID() != ccStartingMap:
        SCLib.UpdateVar("CurStep", "InitChuChu")
    else:
        retryCount = SCLib.GetVar("RetryCount")
        
        if retryCount > 3:
            SCLib.UpdateVar("RetryCount", 0)
            print("Finished ChuChu")
            SCLib.UpdateVar("CurStep", "FinishedChuChu")
            SunCat.UnhookChuChu()
        else:
            Npc.ClearSelection()
            Npc.RegisterSelection("Enter <Hungry Muto>")
            if chuChuHardMode:
                Npc.RegisterSelection("Hard")
            else:
                Npc.RegisterSelection("Normal")
            Character.TalkToNpc(ccNpc)
            time.sleep(5)
            
            if Field.GetID() == ccStartingMap:
                print("Failed to enter ChuChu, creating a new party...")
                leaveParty()
                createParty()
                SCLib.UpdateVar("RetryCount", retryCount + 1)
                time.sleep(1)
            elif Field.GetID() in hungryMutoMaps:
                print("Starting ChuChuPQ!")
                SCLib.UpdateVar("CurStep", "DoingChuChu")
                time.sleep(14)

def doingChuChu():
    if Field.GetID() != ccExitMap:
        currentRecipe = allRecipes[SunCat.GetRecipe()]
        for i in range(len(currentRecipe.ingredients)):
            print("Getting " + str(currentRecipe.amounts[i]) + "x " + currentRecipe.ingredients[i].name)
            currentRecipe.ingredients[i].GetIngredient(currentRecipe.amounts[i])
        
    else:
        time.sleep(0.5)
        SunCat.KamiTP(528, 138)
        time.sleep(0.5)
        SunCat.StopTP()
        SunCat.UnhookChuChu()
        time.sleep(1)
        Npc.ClearSelection()
        Npc.RegisterSelection("Claim ")
        time.sleep(0.1)
        Character.TalkToNpc(3003166)
        time.sleep(1)
        print("Done! Sleeping for a few seconds to check for another run...")
        SCLib.UpdateVar("CurStep", "InitChuChu")
        time.sleep(5)

def finishChuChu():
    chuchuSymbol = Inventory.FindItemByID(1712002)
    if not useSymbol(chuchuSymbol):
        if SCLib.GetVar("UsingWhitelist"):
            Terminal.SetPushButton("Whitelist", True)
        SCLib.UpdateVar("CurDaily", "DD")
        SCLib.UpdateVar("CurStep", "StartingDD")
        
def doChuChu():
    if dailyChuChu:
        InitRecipes()
        
        if SCLib.GetVar("CurStep") == "InitChuChu":
            initChuChu()
        elif SCLib.GetVar("CurStep") == "StartingChuChu":
            startChuChu()
        elif SCLib.GetVar("CurStep") == "DoingChuChu":
            doingChuChu()
        elif SCLib.GetVar("CurStep") == "FinishedChuChu":
            finishChuChu()
    else:
        SCLib.UpdateVar("CurDaily", "DD")
        SCLib.UpdateVar("CurStep", "InitDD")
        
#Dream Defender
def initDD():
    if Field.GetID() != ddStartingMap:
        Terminal.Rush(ddStartingMap)
    else:        
        leaveParty()
        
        SunCat.HookDD()
        
        Terminal.SetCheckBox("Auto NPC", True)
        Terminal.SetCheckBox("Kami Vac", False)
        Terminal.SetCheckBox("Full Map Attack", False)
        Terminal.SetCheckBox("General FMA", False)
        Terminal.SetCheckBox("Grenade Kami",False)
        Terminal.SetCheckBox("Legit Vac",False)
        Terminal.SetCheckBox("dragon_kami",False)
        Terminal.SetCheckBox("Mob Falldown",False)
        Terminal.SetCheckBox("Kami Loot",False)
        Terminal.SetCheckBox("Kami Collision Items",False)
        
        #for mob in ddFilterMobs:
            #SunCat.FilterMob(mob)
            
        #SunCat.FilterMob(ddYellowBox)
        
        Npc.ClearSelection()
        Npc.RegisterSelection("Attempt")
        Npc.RegisterSelection(str(ddLevelSelect))
        time.sleep(2)
        Character.TalkToNpc(ddNpc)
        time.sleep(3)
        
        SCLib.UpdateVar("CurStep", "StartingDD")

def retreatDD():
    rPacket = Packet.COutPacket(SCLib.PacketHeader["RetreatDD"])
    rPacket.EncodeBuffer("[01000000]")
    Packet.SendPacket(rPacket)
        
def startDD():
    if Field.GetID() >= ddMap and Field.GetID() <= ddMapEnd:
        curStage = SunCat.GetDDStage()
        if curStage >= ddExitLevel:
            SunCat.StopTP()
            retreatDD()
            time.sleep(4)
        else:
            boxFound = False
            for box in ddPurpleBoxes:
                curBox = Field.FindMob(box)
                if curBox.valid:
                    boxFound = True
                    if SCLib.GetVar("UsingSI"):
                        Terminal.SetCheckBox("Skill Injection", True)
                    SunCat.KamiTP(curBox.x + kamiOffsetX, curBox.y + kamiOffsetY)
                    break
        if boxFound == False:
            Terminal.SetCheckBox("Skill Injection", False)
            SunCat.KamiTP(ddRestX, ddRestY)
    elif Field.GetID() == ddExitMap:
        SunCat.StopTP()
        #SunCat.UnfilterMobs()
        Character.TalkToNpc(ddNpc)
    else:
        if SCLib.GetVar("RetryCount") < 3:
            print("Failed to enter DD... Retrying")
            SCLib.UpdateVar("RetryCount", SCLib.GetVar("RetryCount") + 1)
            SCLib.UpdateVar("CurStep", "InitDD")
        else:
            print("Finished DD")
            SunCat.UnhookDD()
            SCLib.UpdateVar("CurStep", "InitSS")
            SCLib.UpdateVar("CurDaily", "SS")
            SCLib.UpdateVar("RetryCount", 0)

def doDD():
    if dailyDD:
        if SCLib.GetVar("CurStep") == "InitDD":
            initDD()
        elif SCLib.GetVar("CurStep") == "StartingDD":
            startDD()
    else:
        SCLib.UpdateVar("CurDaily", "SS")
        SCLib.UpdateVar("CurStep", "InitSS")
    
#Spirit Savior
def inSS():
    return Field.GetID() >= ssMapStart and Field.GetID() <= ssMapEnd
    
def initSS():
    if Field.GetID() != ssStartingMap:
        Terminal.Rush(ssStartingMap)
    else:
        SunCat.Teleport(0, 139)
        
        leaveParty()
        
        Terminal.SetCheckBox("Auto NPC", True)
        Terminal.SetCheckBox("Kami Vac", False)
        Terminal.SetCheckBox("Full Map Attack", False)
        Terminal.SetCheckBox("General FMA", False)
        Terminal.SetCheckBox("Auto Buff", False)
        
        for mob in enemyMobs:
            SunCat.FilterMob(mob)
        
        Npc.ClearSelection()
        Npc.RegisterSelection("Attempt")
        Character.TalkToNpc(ssNpc)
        time.sleep(3)
        
        SCLib.UpdateVar("CurStep", "StartingSS")

def runSS():
    for i in range(roundsPerRun):
        killCount = 0
        
        mobsKilled = []
        
        while killCount < 5:
            if not GameState.IsInGame() or not inSS():
                print("Not in SS!")
                break

            curMob = None
            
            for mobID in ssMobArray:
                mob = Field.FindMob(mobID)
                if mob.valid and mob not in mobsKilled:
                    curMob = mob
                    mobsKilled.append(mob)
                    break
            
            if curMob is not None:
                SunCat.KamiTP(curMob.x, curMob.y)
                time.sleep(killTime)
                Key.Press(npcChatKey)
                time.sleep(0.2)
                Key.Press(npcChatKey)
                time.sleep(waitTime)
                killCount += 1
            else:
                print("No mobs left!")
                time.sleep(3) #Wait for mobs to respawn - this should never be hit
        
        SunCat.KamiTP(ssBaseX, ssBaseY)
        time.sleep(roundWaitTime)
        
    SCLib.UpdateVar("CurSSRuns", SCLib.GetVar("CurSSRuns") + 1)
    SCLib.UpdateVar("CurStep", "FinishingSS")

def finishSS():
    if Field.GetID() == ssExitMap:
        Character.TalkToNpc(ssNpc)
        
        SunCat.StopTP()
        SunCat.UnfilterMobs()
        SCLib.UpdateVar("CurStep", "InitSS")
        time.sleep(5)

    
def startSS():
    if inSS():
        SCLib.UpdateVar("CurStep", "RunSS")
    else:
        if SCLib.GetVar("RetryCount") < 3 and SCLib.GetVar("CurSSRuns") < totalRuns:
            print("Failed to enter SS... Retrying")
            SCLib.UpdateVar("RetryCount", SCLib.GetVar("RetryCount") + 1)
            SCLib.UpdateVar("CurStep", "InitSS")
        else:
            print("Finished SS")
            SCLib.UpdateVar("CurDaily", "Return")
            SCLib.UpdateVar("RetryCount", 0)
    
def doSS():
    if dailySS:
        if SCLib.GetVar("CurStep") == "InitSS":
            initSS()
        elif SCLib.GetVar("CurStep") == "StartingSS":
            startSS()
        elif SCLib.GetVar("CurStep") == "RunSS":
            runSS()
        elif SCLib.GetVar("CurStep") == "FinishingSS":
            finishSS()
    else:
        SCLib.UpdateVar("CurDaily", "Return")
        SCLib.UpdateVar("RetryCount", 0)

if GameState.IsInGame() and accountData['changing_mule'] and not accountData['daily_done']:
    initAttack()
    accountData['changing_mule'] = False
    writeJson(accountData,accountId)

if not Terminal.IsRushing() and not accountData['daily_done'] and not accountData['changing_mule'] and not SCLib.GetVar("ToggleAttack"): #only need to do this if daily is not done
    if SCLib.CheckVersion(22):
        if SCLib.GetVar("CurDaily") is None:
            initAttack()
        initVars()
        curDaily = SCLib.GetVar("CurDaily")
        if GameState.IsInGame():
            if curDaily == "VJ":
                Terminal.SetCheckBox("Rush By Level",False)
                doVJ()
            elif curDaily == "ChuChu":
                Terminal.SetCheckBox("Rush By Level",False)
                doChuChu()
            elif curDaily == "DD":
                Terminal.SetCheckBox("Rush By Level",False)
                doDD()
            elif curDaily == "SS":
                Terminal.SetCheckBox("Rush By Level",False)
                doSS()
            elif curDaily == "Return":
                SCLib.UpdateVar("CurDaily", None)
                SCLib.UpdateVar("CurStep", "StartingVJ")
                print("Done! Back to botting...")
                if SCLib.GetVar("UsingKami"):
                    Terminal.SetCheckBox("Kami Vac", True)
                if SCLib.GetVar("UsingSI"):
                    Terminal.SetCheckBox("Skill Injection", True)
                if SCLib.GetVar("UsingFMA"):
                    Terminal.SetCheckBox("Full Map Attack", True)
                if SCLib.GetVar("UsingGFMA"):
                    Terminal.SetCheckBox("General FMA", True)
                if SCLib.GetVar("UsingAutoBuff"):
                    Terminal.SetCheckBox("Auto Buff", True)
                Terminal.SetCheckBox("Rush By Level",True)
                accountData['done_char'].append(Terminal.GetLineEdit("LoginChar"))
                accountData['changing_mule'] = True
                writeJson(accountData,accountId)
                Terminal.Logout()
            else:
                SCLib.StartVars()
        else:
            #Handle all d/c's
            if SCLib.GetVar("CurStep") == "DoingChuChu":
                if Field.GetID() == ccExitMap:
                    Character.TalkToNpc(3003166)
                    time.sleep(5)
                    SCLib.SetVar("CurStep", "InitChuChu")

#always make sure doing cur_pos character
if job == -1 and not accountData['changing_mule'] and GameState.GetLoginStep() == 1:
    print("Not logged in yet")
    Terminal.SetLineEdit("LoginChar",accountData["cur_pos"])
    time.sleep(5)

if accountData['changing_mule'] and GameState.GetLoginStep() == 2 and not accountData['daily_done']:
    Terminal.SetCheckBox("Auto Login",False)
    Terminal.SetLineEdit("LoginChar",str(int(accountData["cur_pos"]) + 1)) #update cur pos to next
    Terminal.SetCheckBox("Auto Login",True)
    time.sleep(1)
    accountData["cur_pos"] = Terminal.GetLineEdit("LoginChar") #update cur pos
    accountData['changing_mule'] = False
    writeJson(accountData,accountId)
    KillPersistVarThred() #restart persisten variables

if accountData['daily_done'] and GameState.GetLoginStep() == 2: #returning to farming char
    Terminal.SetCheckBox("Auto Login",False)
    Terminal.SetLineEdit("LoginChar",str(accountData['training_char']))
    Terminal.SetCheckBox("Auto Login",True)
    time.sleep(1)
    accountData["cur_pos"] = Terminal.GetLineEdit("LoginChar")
    accountData['changing_mule'] = True
    writeJson(accountData,accountId)
    print("returning to farming character")

if accountData['daily_done'] and GameState.IsInGame() and accountData['changing_mule'] and job != 0 and job != 1: #set
    initAttackDone()
    accountData['changing_mule'] = False
    writeJson(accountData,accountId)

if Field.GetID() == ccExitMap:
    Character.TalkToNpc(3003166)
    time.sleep(1)