import Character,Field,Inventory,Key,Npc,Packet,Quest,Terminal,time,GameState,sys,os,Party,json,Login,datetime

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")

try:
    import SunCat, SCHotkey, SCLib
except:
    print("Couldn't find SunCat module")

#if not SCLib.CheckVersion():
#    print("Need to update SCLib")
#SunCat's All-in-one Dailies

#Change these
#--------------------------------------------------
dailyVJ = True
dailyChuChu = True
dailyDD = True
dailySS = True

SCLib.StartVars()
###persist variables
if SCLib.GetVar("ToggleAttack") is None:
    SCLib.PersistVar("ToggleAttack", False)
if SCLib.GetVar("SpiritCoin") is None:
    SCLib.PersistVar("SpiritCoin", Inventory.GetItemCount(4310235))
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

#updated for v203
CashItemRequestOpcode = 0x0546
CashItemResultOpcode = 0x06E2
BuyByMesoRequest = 85
LoadLockerDoneResult = 2
MoveLToSRequest = 15

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
job = Character.GetJob()
level = Character.GetLevel()
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
    if 'arcane_daily_date' not in data:
        data['arcane_daily_date'] = str(datetime.datetime.utcnow().date())
    if 'arcane_daily_done' not in data:
        data['arcane_daily_done'] = False
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
if current_date != accountData['arcane_daily_date']:
    accountData['arcane_daily_date'] = current_date
    accountData['arcane_daily_done'] = False
    accountData['done_char'][:] = []
    accountData['cur_pos'] = str(accountData['daily_start'])
    writeJson(accountData,accountId)
    print("It's a new day!")
    KillPersistVarThred()
    if GameState.IsInGame():
        Terminal.Logout()

#check if done doing dailies on all characters
if len(accountData['done_char']) == accountData['daily_end'] - accountData['daily_start'] + 1 and not accountData['arcane_daily_done']:
    accountData['arcane_daily_done'] = True
    Terminal.SetLineEdit("LoginChar",str(accountData['training_char']))
    writeJson(accountData,accountId)
    print("Finished dailies on every char")

#change character to next char
if accountData["cur_pos"] in accountData['done_char'] and not accountData['arcane_daily_done']:
    if GameState.IsInGame():
        print("Logging out to move to next char")
        accountData['changing_mule'] = True
        Terminal.Logout()
        writeJson(accountData,accountId)
        
#return to farming char
if accountData['cur_pos'] != str(accountData['training_char']) and accountData['arcane_daily_done'] and GameState.IsInGame():
    if GameState.IsInGame():
        print("Loggin out ot return to farming char")
        Terminal.Logout()

def toggle_rush_by_level(indicator):
    Terminal.SetCheckBox("Rush By Level",indicator)
    Terminal.SetRushByLevel(indicator)

def VJprequest():
    toggle_rush_by_level(False)
    #print("Doing VJ prequest")
    jobid = Character.GetJob()
    level = Character.GetLevel()

    fieldid = Field.GetID()
    quest1 = Quest.GetQuestState(1466)
    quest2 = Quest.GetQuestState(34100)
    quest3 = Quest.GetQuestState(34101)
    quest4 = Quest.GetQuestState(34102)
    quest5 = Quest.GetQuestState(34103)
    quest6 = Quest.GetQuestState(34104)
    quest7 = Quest.GetQuestState(34105)
    quest8 = Quest.GetQuestState(34106)
    quest9 = Quest.GetQuestState(34107)
    quest10 = Quest.GetQuestState(34108)
    quest11 = Quest.GetQuestState(34109)
    quest12 = Quest.GetQuestState(34110)
    quest13 = Quest.GetQuestState(34111)
    quest14 = Quest.GetQuestState(34112)
    quest15 = Quest.GetQuestState(34113)
    quest16 = Quest.GetQuestState(34114)
    quest17 = Quest.GetQuestState(34115)
    quest18 = Quest.GetQuestState(34116)
    quest19 = Quest.GetQuestState(34117)
    quest20 = Quest.GetQuestState(34118)
    quest21 = Quest.GetQuestState(34119)
    quest22 = Quest.GetQuestState(34120)
    # Fakesymbol, enter at correct place and replace FAKESYMBOLID with item ID
    fakesymbol = Inventory.FindItemByID(1712000)  # enter ID
    if fakesymbol.valid:
        Inventory.SendChangeSlotPositionRequest(1, fakesymbol.pos, -1600, -1)
    # RealSymbol, enter at correct place and replace REALSYMBOLID with item ID
    realsymbol = Inventory.FindItemByID(1712001)  # enter ID
    if realsymbol.valid:
        Inventory.SendChangeSlotPositionRequest(1, realsymbol.pos, -1600, -1)
    if fieldid == 450001000:
        time.sleep(1)
        if Character.GetPos().x != -338:
            Character.Teleport(-338, -3)
    if fieldid == 450001340:
        time.sleep(1)
        if Character.GetPos().x != 563:
            Character.Teleport(563, 177)
    if fieldid == 450001350:
        time.sleep(1)
        if Character.GetPos().x != 1200:
            Character.Teleport(1200, 177)
    if quest1 != 2:
        if quest1 == 0:
            if fieldid != 270010111:
                Terminal.Rush(270010111)
            else:
                Quest.StartQuest(1466, 2140001)
        elif quest1 == 1:
            if Quest.CheckCompleteDemand(1466, 2140001) == 0:
                if fieldid != 270010111:
                    Terminal.Rush(270010111)
                else:
                    Quest.CompleteQuest(1466, 2140001)
                    time.sleep(3)
                    oPacket = Packet.COutPacket(0x00F4)
                    oPacket.Encode4(0x291000E6)
                    oPacket.Encode1(0x01)
                    oPacket.Encode2(0x0001)
                    oPacket.Encode2(0xF9C0)
                    oPacket.Encode2(0xFFFF)
                    Packet.SendPacket(oPacket)
                    time.sleep(3)

            else:
                if fieldid != 450001010:
                    Terminal.Rush(450001010)
    elif quest2 != 2:
        if fieldid != 450001000:
            Terminal.Rush(450001000)
        else:
            if quest2 == 0:
                Quest.StartQuest(34100, 3003131)
            elif quest2 == 1:
                Quest.CompleteQuest(34100, 3003131)
    elif quest3 != 2:
        if fieldid != 450001000:
            Terminal.Rush(450001000)
        else:
            if quest3 == 0:
                Quest.StartQuest(34101, 3003131)
            elif quest3 == 1:
                Quest.CompleteQuest(34101, 3003111)
    elif quest4 != 2:
        if quest4 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34102, 3003111)
        elif quest4 == 1:
            if Quest.CheckCompleteDemand(34102, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34102, 3003111)

            else:
                if fieldid != 450001010:
                    Terminal.Rush(450001010)
    elif quest5 != 2:
        if quest5 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34103, 3003111)
        elif quest5 == 1:
            if Quest.CheckCompleteDemand(34103, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34103, 3003111)
            else:
                if fieldid != 450001012:
                    Terminal.Rush(450001012)
    elif quest6 != 2:
        if quest6 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34104, 3003111)
        elif quest6 == 1:
            if Quest.CheckCompleteDemand(34104, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34104, 3003111)
            else:
                if fieldid != 450001014:
                    Terminal.Rush(450001014)
    elif quest7 != 2:
        #print("7")
        if quest7 == 0:
            if fieldid != 450001000:
                Terminal.Rush(450001000)
            else:
                Quest.StartQuest(34105, 3003111)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(34105, 3003111) == 0:
                if fieldid != 450001000:
                    Terminal.Rush(450001000)
                else:
                    Quest.CompleteQuest(34105, 3003111)
            else:
                if fieldid != 450001016:
                    Terminal.Rush(450001016)
    elif quest8 != 2:
        if fieldid != 450001000:
            Terminal.Rush(450001000)
        else:
            if quest8 == 0:
                Quest.StartQuest(34106, 3003111)
            elif quest8 == 1:
                Quest.CompleteQuest(34106, 3003131)
    elif quest9 != 2:
        if fieldid != 450001005:
            Terminal.Rush(450001005)
        else:
            Quest.StartQuest(34107, 3003110)
    elif quest10 != 2:
        if fieldid != 450001105:
            Terminal.Rush(450001105)
        else:
            Quest.StartQuest(34108, 3003133)
    elif quest11 != 2:
        if fieldid != 450001100:
            Terminal.Rush(450001100)
        else:
            Quest.StartQuest(34109, 3003125)
    elif quest12 != 2:
        if fieldid != 450001100:
            Terminal.Rush(450001100)
        else:
            if quest12 == 0:
                Quest.StartQuest(34110, 3003134)
            elif quest12 == 1:
                Quest.CompleteQuest(34110, 3003125)
    elif quest13 != 2:
        if quest13 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34111, 3003125)
        elif quest13 == 1:
            if Quest.CheckCompleteDemand(34111, 3003125) == 0:
                if fieldid != 450001100:
                    Terminal.Rush(450001100)
                else:
                    Quest.CompleteQuest(34111, 3003125)
            else:
                if fieldid != 450001110:
                    Terminal.Rush(450001110)
    elif quest14 != 2:
        if quest14 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34112, 3003125)
        elif quest14 == 1:
            if Quest.CheckCompleteDemand(34112, 3003125) == 0:
                if fieldid != 450001100:
                    Terminal.Rush(450001100)
                else:
                    Quest.CompleteQuest(34112, 3003125)
            else:
                if fieldid != 450001112:
                    Terminal.Rush(450001112)
    elif quest15 != 2:
        if quest15 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34113, 00000000)
        elif quest15 == 1:
            if Quest.CheckCompleteDemand(34113, 0000000) == 0:
                if fieldid != 450001100:
                    Terminal.Rush(450001100)
                else:
                    Quest.CompleteQuest(34113, 0000000)
            else:
                if fieldid != 450001114:
                    Terminal.Rush(450001114)
    elif quest16 != 2:
        if quest16 == 0:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.StartQuest(34114, 3003135)
        elif quest16 == 1:
            if fieldid != 450001100:
                Terminal.Rush(450001100)
            else:
                Quest.CompleteQuest(34114, 3003126)
    elif quest17 != 2:
        if quest17 == 0:
            Quest.StartQuest(34115, 3003127)
            time.sleep(10)
        elif quest == 1:
            time.sleep(5)
    elif quest18 != 2:
        if quest18 == 0:
            if fieldid != 450001210:
                Terminal.Rush(450001210)
            else:
                Quest.StartQuest(34116, 3003128)
        elif quest18 == 1:
            if Quest.CheckCompleteDemand(34116, 3003114) == 0:
                if fieldid == 450001210:
                    Character.Teleport(1125, -29)
                    time.sleep(1)
                    Quest.CompleteQuest(34116, 3003114)
                elif fieldid != 450001210:
                    Terminal.Rush(450001210)
                else:
                    Quest.CompleteQuest(34116, 3003114)
            else:
                if fieldid != 450001210:
                    Terminal.Rush(450001210)

    elif quest19 != 2:
        if quest19 == 0:
            if fieldid != 450001215:
                Terminal.Rush(450001215)
            else:
                Quest.StartQuest(34117, 3003129)
        elif quest19 == 1:
            if Quest.CheckCompleteDemand(34117, 3003115) == 0:
                if fieldid == 450001215:
                    Character.Teleport(1460, -35)
                    time.sleep(1)
                    Quest.CompleteQuest(34117, 3003115)
                elif fieldid != 450001215:
                    Terminal.Rush(450001215)
            else:
                if fieldid != 450001215:
                    Terminal.Rush(450001215)

    elif quest20 != 2:
        if quest20 == 0:
            if fieldid == 450001219:
                time.sleep(5)
                if Character.GetPos().x != 607:
                    Terminal.SetCheckBox("Kami Vac",False)
                    Character.Teleport(607,177)
                else:
                    Party.LeaveParty()
                    Character.EnterPortal()
            if fieldid != 450001218:
                Terminal.Rush(450001218)
            else:
                Quest.StartQuest(34118, 3003130)
        elif quest20 == 1:
            if Quest.CheckCompleteDemand(34118, 3003116) == 0:
                if fieldid == 450001218:
                    Character.Teleport(1441, 177)
                    time.sleep(1)
                    Quest.CompleteQuest(34118, 3003116)
                elif fieldid != 450001218:
                    Terminal.Rush(450001218)
            else:
                if fieldid != 450001218:
                    Terminal.Rush(450001218)
    elif quest21 != 2:
        if quest21 == 0:
            Terminal.Rush(450001219)
            time.sleep(5)
            if fieldid == 450001219:
                time.sleep(5)
                if Character.GetPos().x != 607:
                    Terminal.SetCheckBox("Kami Vac",False)
                    Character.Teleport(607,177)
                else:
                    Party.LeaveParty()
                    Character.EnterPortal()
        if quest21 == 1:
            if Quest.CheckCompleteDemand(34119, 3003140) == 0:
                if fieldid != 450001219:
                    Terminal.Rush(450001219)
                    Quest.CompleteQuest(34119, 3003140)
                else:
                    Quest.CompleteQuest(34119, 3003140)
            else:
                if fieldid == 450001219:
                    if Character.GetPos().x != 607:
                        Terminal.SetCheckBox("Kami Vac",False)
                        Character.Teleport(607,177)
                    else:
                        Party.LeaveParty()
                        Character.EnterPortal()
    elif quest22 != 2:
        if quest22 == 0:
            Terminal.Rush(450001250)
            Quest.StartQuest(34120, 3003143)
            time.sleep(10)
            oPacket = Packet.COutPacket(0x00F4)
            oPacket.Encode4(0x2951FDBD)
            oPacket.Encode1(0x01)
            oPacket.Encode2(0x0001)
            oPacket.Encode2(0xF9C0)
            oPacket.Encode2(0xFFFF)
            time.sleep(5)
    elif fieldid != 450001000:
        print("Rushing")
        Terminal.Rush(450001000)
        time.sleep(2)
        toggle_rush_by_level(True)

def Chuchuprequest():
    toggle_rush_by_level(False)
    if GameState.IsInGame():
        time.sleep(1)
        jobid = Character.GetJob()
        level = Character.GetLevel()
        if Terminal.IsRushing():
            time.sleep(3)

        fieldid = Field.GetID()
        quest1 = Quest.GetQuestState(34200)
        quest2 = Quest.GetQuestState(34201)
        quest3 = Quest.GetQuestState(34202)
        quest4 = Quest.GetQuestState(34203)
        quest5 = Quest.GetQuestState(34204)
        quest6 = Quest.GetQuestState(34205)
        quest7 = Quest.GetQuestState(34206)
        quest8 = Quest.GetQuestState(34207)
        quest9 = Quest.GetQuestState(34208)
        quest10 = Quest.GetQuestState(34209)
        quest11 = Quest.GetQuestState(34210)
        quest12 = Quest.GetQuestState(34211)
        quest13 = Quest.GetQuestState(34212)
        quest14 = Quest.GetQuestState(34213)
        quest15 = Quest.GetQuestState(34214)
        quest16 = Quest.GetQuestState(34215)
        quest17 = Quest.GetQuestState(34216)
        quest18 = Quest.GetQuestState(34217)
        quest19 = Quest.GetQuestState(34218)

        if fieldid == 450002000:
            if Character.GetPos().x != 1084:
                Character.Teleport(1084, 138)
                time.sleep(2)

        if fieldid == 450002010:
            Character.Teleport(667, -588)
            time.sleep(3)
            Key.Press(0x26)
            time.sleep(1)



        fakesymbol = Inventory.FindItemByID(1712002)  # enter ID
        if fakesymbol.valid:
            Inventory.SendChangeSlotPositionRequest(1, fakesymbol.pos, -1601, -1)

        if quest8 == 0 and quest7 == 2 and quest9 != 2:
            time.sleep(1)
            Npc.RegisterSelection("Delicious")
            time.sleep(1)
            Npc.RegisterSelection("Beefy")
            time.sleep(1)
            Npc.RegisterSelection("Bite of Heaven")

        if quest1 != 2:
            if quest1 == 0:
                Terminal.Rush(450002000)
                time.sleep(5)
                if fieldid != 450002201:
                    Terminal.Rush(450002201)
                elif fieldid == 450002201:
                    Quest.StartQuest(34200, 3003156)

        elif quest2 != 2:
            if quest2 == 0:
                if fieldid != 450002000:
                    Terminal.Rush(450002000)
                elif fieldid == 450002000:
                    Quest.StartQuest(34201, 3003150)

        elif quest3 != 2:
            if quest3 == 0:
                if fieldid != 450002000:
                    Terminal.Rush(450002000)
                elif fieldid == 450002000:
                    Quest.StartQuest(34202, 3003152)
        elif quest4 != 2:
            if quest4 == 0:
                if fieldid != 450002000:
                    Terminal.Rush(450002000)
                elif fieldid == 450002000:
                    Quest.StartQuest(34203, 3003152)
            elif quest4 == 1:
                if Quest.CheckCompleteDemand(34203, 3003152) == 0:
                    if fieldid != 450002000:
                        Terminal.Rush(450002000)
                    else:
                        Quest.CompleteQuest(34203, 3003152)
                else:
                    if fieldid != 450002001:
                        Terminal.Rush(450002001)

        elif quest5 != 2:
            if quest5 == 0:
                if fieldid != 450002000:
                    Terminal.Rush(450002000)
                elif fieldid == 450002000:
                    Quest.StartQuest(34204, 3003152)

        elif quest6 != 2:
            if quest6 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34205, 0000000)
            elif quest6 == 1:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.CompleteQuest(34205, 3003151)

        elif quest7 != 2:
            if quest7 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34206, 3003151)

        elif quest8 != 2:
            if quest8 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34207, 3003151)
            if quest8 == 1:
                if Quest.CheckCompleteDemand(34207, 3003151) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34207, 3003151)
                else:
                    if fieldid != 450002002:
                        Terminal.Rush(450002002)
        elif quest9 != 2:
            if quest9 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34208, 3003151)
            if quest9 == 1:
                if Quest.CheckCompleteDemand(34208, 3003151) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34208, 3003151)
                else:
                    if fieldid != 450002004:
                        Terminal.Rush(450002004)

        elif quest10 != 2:
            if quest10 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34209, 3003153)
            if quest10 == 1:
                if Quest.CheckCompleteDemand(34209, 3003153) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34209, 3003153)
                else:
                    if fieldid != 450002009:
                        Terminal.Rush(450002009)

        elif quest11 != 2:
            if quest11 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34210, 3003153)
            if quest11 == 1:
                if Quest.CheckCompleteDemand(34210, 3003153) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34210, 3003153)
                else:
                    if fieldid != 450002007:
                        Terminal.Rush(450002007)

        elif quest12 != 2:
            if quest12 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34211, 3003154)
            if quest12 == 1:
                if Quest.CheckCompleteDemand(34211, 3003154) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34211, 3003154)
                else:
                    if fieldid != 450002012:
                        Terminal.Rush(450002012)

        elif quest13 != 2:
            if quest13 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34212, 3003154)
            if quest13 == 1:
                if Quest.CheckCompleteDemand(34212, 3003154) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34212, 3003154)
                else:
                    if fieldid != 450002014:
                        Terminal.Rush(450002014)

        elif quest14 != 2:
            if quest14 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34213, 3003155)
            if quest14 == 1:
                if Quest.CheckCompleteDemand(34213, 3003155) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34213, 3003155)
                else:
                    if fieldid != 450002017:
                        Terminal.Rush(450002017)


        elif quest15 != 2:
            if quest15 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                elif fieldid == 450002023:
                    Quest.StartQuest(34214, 3003155)
            if quest15 == 1:
                if Quest.CheckCompleteDemand(34214, 3003155) == 0:
                    if fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34214, 3003155)
                else:
                    if fieldid != 450002019:
                        Terminal.Rush(450002019)


        elif quest16 != 2:
            print("q16")
            if quest16 == 0:
                if fieldid != 450002023:
                    Terminal.Rush(450002023)
                else:
                    Quest.StartQuest(34215, 3003151)
            if quest16 == 1:
                if Quest.CheckCompleteDemand(34215, 3003151) == 0:
                    if fieldid == 450002251 or fieldid == 450002250 and Quest.CheckCompleteDemand(34215, 3003151) == 0:
                        Terminal.SetCheckBox("Kami Vac",False)
                        Character.Teleport(11, 138)
                        time.sleep(1)
                        Character.EnterPortal()
                        time.sleep(1)
                        Terminal.SetCheckBox("Kami Vac",True)
                    elif fieldid != 450002023:
                        Terminal.Rush(450002023)
                    else:
                        Quest.CompleteQuest(34215, 3003151)
                else:
                    if fieldid != 450002251 and fieldid != 450002250:
                        Terminal.Rush(450002010)
                    elif fieldid == 450002251 or fieldid == 450002250:
                        Terminal.StopRush()

        elif quest17 != 2:
            print("q17")
            if quest17 == 0:
                if fieldid != 450002000:
                    Terminal.Rush(450002000)
                elif fieldid == 450002000:
                    Quest.StartQuest(34216, 3003150)

        elif quest18 != 2:
            print("q18")
            if quest18 == 0:
                if fieldid != 450002021:
                    Terminal.Rush(450002021)
                elif fieldid == 450002021:
                    Quest.StartQuest(34217, 3003156)

        elif quest19 != 2:
            if quest19 == 0:
                if fieldid != 450002021:
                    Terminal.Rush(450002021)
                elif fieldid == 450002021:
                    Quest.StartQuest(34218, 3003156)

def event_quests():
    #StartQuest(52516, 9330195)
    #StartQuest(52517, 9330195)
    #StartQuest(52518, 9330196)
    #StartQuest(52519, 9330197)
    #StartQuest(52520, 9330198)
    quest1 = Quest.GetQuestState(52516)
    #print(quest1)
    if quest1 != 1:
        Quest.StartQuest(52516, 9330195)
    elif quest1 ==1:
        doQuest(52516,9330195)
        doQuest(52517,9330195)
        doQuest(52518,9330196)
        doQuest(52519,9330197)
        doQuest(52520,9330198)
        if Quest.GetQuestState(52520) == 1 and not Inventory.FindItemByID(3994619).valid:
            forfeit_quest(52520)
            print("Forfeiting quest because dced")

def forfeit_quest(questid):
    oPacket = Packet.COutPacket(0x0166)
    tohex = hex(questid)[2:].zfill(4)
    oPacket.EncodeBuffer("03 {} {} 00 00".format(tohex[2:4],tohex[0:2])) #0166 [0328CD0000]
    Packet.SendPacket(oPacket)

def doQuest(questid,questnpc_start,questnpc_end=0):
    if questnpc_end == 0:
        questnpc_end = questnpc_start
    quest_state = Quest.GetQuestState(questid)
    if quest_state != 1:
        Quest.StartQuest(questid,questnpc_start)
    elif quest_state == 1:
        if Quest.CheckCompleteDemand(questid,questnpc_end) == 0:
            Quest.CompleteQuest(questid,questnpc_end)

class CashItemInfo:
    def __init__(self):
        self.liSN = 0
        self.nItemID = 0
        # None of the other vars are useful for this specific script
 
def GetCashItemInfo():
    return CashItemInfo()
 
pCashItemInfo = GetCashItemInfo()
 
def BuyByMeso():
    Packet.BlockSendHeader(CashItemResultOpcode)
    oPacket = Packet.COutPacket(CashItemRequestOpcode)
    oPacket.Encode1(BuyByMesoRequest)
    nMeso = Character.GetMeso()
    nPrice = 0
    if nMeso >= 25000000:
        nCommoditySN = 87000027
        nPrice = 25000000
    elif nMeso >= 13000000:
        nCommoditySN = 87000026
        nPrice = 13000000
    elif nMeso >= 5200000:
        nCommoditySN = 87000025
        nPrice = 5200000
    oPacket.Encode4(nCommoditySN)
    oPacket.Encode4(nPrice)
    Packet.SendPacket(oPacket)
    time.sleep(3)
    Packet.UnBlockSendHeader(CashItemResultOpcode)
 
def MoveLToS(liSN, nEmptySlotPOS):
    oPacket = Packet.COutPacket(CashItemRequestOpcode)
    oPacket.Encode1(MoveLToSRequest)
    print(liSN, flush=True)
    oPacket.Encode8(liSN)
    oPacket.Encode4(5040004)
    oPacket.Encode1(5) # nTI
    oPacket.Encode2(nEmptySlotPOS)
    Packet.SendPacket(oPacket)
 
def CashItemResLoadLockerDone():
    iPacket = Packet.WaitForRecv(CashItemResultOpcode, 10000)
    if iPacket.GetRemaining() > 0:
        nRes = iPacket.ReadLong(1)
        if nRes == LoadLockerDoneResult:
            bItemLockerFull = iPacket.ReadLong(1)
            if bItemLockerFull == 1:
                nOverItemCount = iPacket.ReadLong(4)
            nCashItemCount = iPacket.ReadLong(2)
            if nCashItemCount >= 0:
                bFound = False
                for i in range(0, nCashItemCount):
                    CashItemInfoDecode(iPacket)
                    if pCashItemInfo.nItemID == 5040004:
                        bFound = True
                        Terminal.SetProperty("liSN", pCashItemInfo.liSN)
                        break
                if bFound:
                    time.sleep(1)
                    CashItemInfoDecode(iPacket)
                    print("Moving", flush=True)
                    MoveLToS(Terminal.GetProperty("liSN", -1), nEmptySlotPOS)
                else:
                    BuyByMeso()
            time.sleep(2)
            Terminal.LeaveCashShop()
    else:
        Terminal.LeaveCashShop()
 
def CashItemInfoDecode(iPacket):
    pCashItemInfo.liSN = iPacket.ReadLong(8)
    dwAccountID = iPacket.ReadLong(4)
    dwCharacterID = iPacket.ReadLong(4)
    pCashItemInfo.nItemID = iPacket.ReadLong(4)
    nCommodityID = iPacket.ReadLong(4)
    nNumber = iPacket.ReadLong(2)
    sBuyCharacterID = iPacket.ReadLong(13)
    ftDateExpire = iPacket.ReadLong(8) # FileTime(4, 4)
    nPaybackRate = iPacket.ReadLong(4)
    dDiscountRate = iPacket.ReadLong(8)
    dwOrderNo = iPacket.ReadLong(4)
    dwProductNo = iPacket.ReadLong(4)
    bRefundable = iPacket.ReadLong(1)
    nSourceFlag = iPacket.ReadLong(1)
    nStorageBank = iPacket.ReadLong(1)
    # CashItemOption Decode
    liCashItemSN = iPacket.ReadLong(8)
    ftExpireDate = iPacket.ReadLong(8) # FileTime(4, 4)
    nGrade = iPacket.ReadLong(4)
    iPacket.ReadLong(4) # aOption[0]
    iPacket.ReadLong(4) # aOption[1]
    iPacket.ReadLong(4) # aOption[2]
def toggle_skill():
    if job in WildHunterJobs and level > 11:
        #Rige Jaguar
        buff = 33001001
        toggle_buffs(buff,buff,True)
    elif job in MechanicJobs:
        #Mount Mechanic machine
        buff = 35001002
        toggle_buffs(buff,buff,True)
    elif job in FPMageJobs or job in ILMageJobs or job in BishopJobs:
        #magic guard
        buff = 2001002
        toggle_buffs(buff)
        if job == BishopJobs[3]:
            summon_dragon = 2321003
            toggle_buffs(summon_dragon)
    elif job in EvanJobs:
        #magic guard
        buff = 22001012
        toggle_buffs(buff)
    elif job == DawnWarriorJobs[3]:
        buff = 11121005
        toggle_buffs(buff)
    elif job == ThunderBreakerJobs[3]:
        buff = 15121004
        toggle_buffs(buff)
    elif job in WindArcherJobs and job != WindArcherJobs[0]:
        buff = 13101022
        toggle_buffs(buff)
    elif job in BattleMageJobs:
        if job == BattleMageJobs[0]:
            buff = 32001016 #hasty aura
            toggle_buffs(buff)
        elif job == BattleMageJobs[1]:
            buff = 32101009 #yellow aura
            toggle_buffs(buff)
        elif job == BattleMageJobs[2]:
            buff = 32111012 #blue aura
            toggle_buffs(buff)
        elif job == BattleMageJobs[3]:
            buff = 32121017 #dark aura
            toggle_buffs(buff)
    elif job == AngelicBusterJobs[3]:
        buff = 65121011
        toggle_buffs(buff)
    elif job in DarkknightJobs and job != DarkknightJobs[0]:
        buff = 1301013
        toggle_buffs(buff)
    elif job in HeroJobs and job != HeroJobs[0]:
        buff = 1101013
        toggle_buffs(buff)
    elif job in ShadeJobs and job >=2510:
        buff = 25101009
        toggle_buffs(buff)
    elif job == 531: #Cannon Trooper 5311005
        buff = 5311005
        timeout_buffs(buff)
        buff3 = 5311004
        timeout_buffs(buff3)
    elif job == 532: #Cannoneer
        buff = 5321004
        timeout_buffs(buff)
        buff2 = 5320007
        skill2= 5311005
        timeout_buffs(buff2,skill2)
        buff3 = 5311004
        timeout_buffs(buff3)
    elif job == CorsairJobs[2]: #or job == CorsairJobs[3]:
        buff = 5211014
        timeout_buffs(buff)
    elif job == CorsairJobs[3]: #5220014
        buff = 5220014
        skill = 5211007
        timeout_buffs(buff,skill)
    elif job == BuccaneerJobs[2]: #or job == CorsairJobs[3]:
        buff = 5111007
        timeout_buffs(buff)
    elif job == BuccaneerJobs[3]: #5220014
        buff = 5120012
        skill = 5111007
        timeout_buffs(buff,skill)

        buff2 = 5121013
        timeout_buffs(buff2,buff2,30,True,True)
    elif job in IlliumJobs and job != IlliumJobs[0]:
        buff = 152101000
        skill = 152101003
        toggle_buffs(buff,skill)
    elif job in HayatoJobs:
        buff = 40011289
        timeout_buffs(buff)
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
        buff = 142121004
        timeout_buffs(buff)
    elif job == ShadowerJobs[3] and level >= 140:
        buff = 4221054
        timeout_buffs(buff)
        #buffs = Character.GetBuffs()
        #for buffa in buffs:
        #    print("Current Buff Id: {}; Remaining Time: {}".format(buff.id,buff.timeLeft))
    elif job in NightlordJobs and job != NightlordJobs[0]:
        buff = 4101011
        toggle_buffs(buff)
        if job == NightlordJobs[3] and level >= 140:
            buff = 4121054
            timeout_buffs(buff,buff,30,False)
    elif job in KaiserJobs:
        buff = 60001217
        toggle_buffs(buff)
        if job == KaiserJobs[2] or job == KaiserJobs[3]:
            buff = 61111002
            toggle_buffs(buff)
    elif job in PhantomJobs:
        buff = 20031210
        toggle_buffs(buff)
    elif job in BowmasterJobs:
        if job == BowmasterJobs[2]:
            buff = 3111011
            toggle_buffs(buff)
        elif job == BowmasterJobs[3]:
            buff = 3111011
            toggle_buffs(buff)
            buff2=3121054
            timeout_buffs(buff2,buff2,30,False)
    elif job in DemonSlayerJobs:
        if job == DemonSlayerJobs[3]:
            buff = 31121054
            timeout_buffs(buff,timer=10)
    elif job in DemonAvengerJobs:
        if job == DemonAvengerJobs[3]:
            if level >= 140:
                buff = 31221054
                timeout_buffs(buff,buff,30,False)
            if level >= 200:
                buff = 31221053
                timeout_buffs(buff,buff,30,False)
    elif job in MercedesJobs:
        if level >= 140:
            buff = 23121054
            timeout_buffs(buff)
def toggle_buffs(buffid,skillid = None,toggleKami = False):
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
                toggle_kami(False)
            time.sleep(short_sleep)
            Character.UseSkill(skillid)
            #time.sleep(short_sleep)
            if job in BattleMageJobs:
                time.sleep(short_sleep)
                Character.UseSkill(32001014)
                #time.sleep(short_sleep)
            if Character.HasBuff(2, buffid) == True:
                if toggleKami:
                    toggle_kami(True)
            Terminal.SetCheckBox("Auto Attack",autoAttack)
            Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
            Terminal.SetCheckBox("Skill Injection",skillInject)
    
def timeout_buffs(buffid,skillid = None,timer = 30,need_sleep = True,injectSkill = False):
    if need_sleep:
        short_sleep = 0.75
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
                print("Skill {}: Continued".format(buffid))
                autoAttack = Terminal.GetCheckBox("Auto Attack")
                skillInject = Terminal.GetCheckBox("Skill Injection")
                javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
                Terminal.SetCheckBox("Auto Attack",False)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                if not injectSkill:
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

def initAttack():
    print("Initializing attack settings for this character")
    attack_key = 0x44
    pgup_key = 0x21
    Terminal.SetComboBox("Familiar0",1)
    Terminal.SetCheckBox("Mob Falldown",False)
    Terminal.SetCheckBox("eliteCC",True)
    toggle_rush_by_level(False)
    if Character.IsOwnFamiliar(9960098):
        Terminal.SetSlider("sliderMP", 100)
        Terminal.SetComboBox("MPKey",4)
    else:
        Terminal.SetSlider("sliderMP", 10)
        Terminal.SetComboBox("MPKey",6)
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
        Terminal.SetSpinBox("MonkeySpiritsNDdelay",0)
        Terminal.SetCheckBox("Grenade Kami",True)
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",True)
        Terminal.SetCheckBox("Kami Vac",False)
        Terminal.SetCheckBox("Auto Attack",True)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Key.Set(0x47,1,42111003)
    elif job == 2712: #lumi fourth job
        print("Setting up Settings for Luminous")
        '''
        if Character.HasBuff(2,20040216): #Light Mode
            Key.Set(attack_key,1,27121100)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            Key.Set(attack_key,1,27111303)
        else:                              #Dark Mode
            Key.Set(attack_key,1,27121202)
        '''
        Key.Set(attack_key,1,27121100)
        Terminal.SetCheckBox("Skill Injection", False)
        
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetCheckBox("Full Map Attack",False)
    elif job == 3122: #DA fourth job
        print("Setting up Settings for DA")
        Key.Set(attack_key,1,31211000)
        Terminal.SetCheckBox("Skill Injection", False)
        #Terminal.SetSpinBox("SkillInjection",100)
        
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",50)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3112: #DS fourth job
        print("Setting up Settings for DS")
        Terminal.SetLineEdit("SISkillID","400011018")
        Terminal.SetSpinBox("SkillInjection",50)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2312: #Mercedes 4th 400031024
        print("Setting up Settings for Mercedes")
        Terminal.SetLineEdit("SISkillID","400031024")
        Terminal.SetSpinBox("SkillInjection",110)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 4112: #Hayato 4th 41121011
        print("Setting up Settings for Hayato")
        
        Terminal.SetLineEdit("SISkillID","41121011")
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3612:#Xenon 4th 36121000
        print("Setting up Settings for Xenon")
        Terminal.SetLineEdit("SISkillID","36121000")
        Terminal.SetSpinBox("SkillInjection",80)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2412: #Phantom 4th 24121000
        print("Setting up Settings for Phantom")
        Terminal.SetLineEdit("SISkillID","24121000")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetSpinBox("SkillInjection",110)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 15212: #Illium 4th
        print("Setting up Settings for Illium")
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",True)
        Terminal.SetCheckBox("bot/illium/summon_control",True)
        Terminal.SetCheckBox("General FMA",True)
        Terminal.SetCheckBox("Kami Vac",False)
    elif job == 6412: # Cadena 4th job
        print("Setting up Settings for Cadena")
        attackSIND(64001001,True,160,"si_cadena")
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
        Terminal.SetLineEdit("SISkillID","400051011")
        Terminal.SetCheckBox("Auto Attack", False)
        
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("General FMA",True)
        Terminal.SetCheckBox("Kami Vac",False)
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
        Terminal.SetSpinBox("SkillInjection",31)
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
    elif job == ThunderBreakerJobs[3]:
        attackSI(400051007,True,100,"SIRadioMagic")
        Terminal.SetCheckBox("General FMA",True)
        Terminal.SetCheckBox("Kami Vac",False)
    elif job == WildHunterJobs[3]:
        attackSI(400031033,True,100,"SIRadioShoot")
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 434: #dual blade
        attackSIND(400040006,True,16)
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)
        if job not in AngelicBusterJobs and job not in ThunderBreakerJobs:
            Terminal.SetCheckBox("General FMA",False)
        #if job not in LuminousJobs:
        #    Terminal.SetCheckBox("Full Map Attack",False)

def initAttackDone():
    print("Initializing done attack settings for this character")
    attack_key = 0x44
    pgup_key = 0x21
    if job == 1212:
        Terminal.SetComboBox("Familiar0",1)
    else:
        Terminal.SetComboBox("Familiar0",5)
    toggle_rush_by_level(True)
    Terminal.SetCheckBox("Kami Vac",False)
    Terminal.SetSlider("sliderMP", 10)
    Terminal.SetComboBox("MPKey",6)
    Terminal.SetCheckBox("eliteCC",False)
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
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("Auto SP",True)
        Terminal.SetCheckBox("charm_fma",True)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetCheckBox("Auto Attack",True)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Key.Set(0x47,1,42111003)
    elif job == 2712: #lumi fourth job
        print("Setting up Settings for Luminous")
         #Assign an Item, reboot potion, to Page up(0x21)
        Key.Set(attack_key,1,27121100)
        Terminal.SetCheckBox("Skill Injection", False)
        
        #Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        #Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Auto Attack", True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetCheckBox("Full Map Attack",False)
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
         #Assign an Item, reboot potion, to Page up(0x21)
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
        
        Terminal.SetLineEdit("SISkillID","41121011")
        Terminal.SetSpinBox("SkillInjection",100)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 3612:#Xenon 4th 36121000
        print("Setting up Settings for Xenon")
        
        Terminal.SetLineEdit("SISkillID","36121000")
        Terminal.SetSpinBox("SkillInjection",80)
        Terminal.SetCheckBox("Melee No Delay",False)
        
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 2412: #Phantom 4th 24121000
        print("Setting up Settings for Phantom")
        
        Terminal.SetLineEdit("SISkillID","24121000")
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMelee",True)
        
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetSpinBox("SkillInjection",110)
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 15212: #Illium 4th
        print("Setting up Settings for Illium")
        
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",True)
        Terminal.SetCheckBox("bot/illium/summon_control",True)
        Terminal.SetCheckBox("General FMA",True)
        Terminal.SetCheckBox("Kami Vac",False)
    elif job == 6412: # Cadena 4th job
        print("Setting up Settings for Cadena")
        attackSIND(64001001,True,160,"si_cadena")
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
        Terminal.SetCheckBox("Kami Vac",True)
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
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 6512: #AB 4th
        print("Setting up Settings for AB")
        Terminal.SetLineEdit("SISkillID","400051011")
        Terminal.SetCheckBox("Auto Attack", False)
        
        Terminal.SetSpinBox("SkillInjection",0)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetRadioButton("SIRadioMagic",True)
        Terminal.SetCheckBox("Skill Injection", True)
        Terminal.SetCheckBox("General FMA",True)
        Terminal.SetCheckBox("Kami Vac",False)
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
        Terminal.SetSpinBox("SkillInjection",31)
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
    elif job == ThunderBreakerJobs[3]:
        attackSI(400051007,True,100,"SIRadioMagic")
        Terminal.SetCheckBox("General FMA",True)
        Terminal.SetCheckBox("Kami Vac",False)
    elif job == WildHunterJobs[3]:
        attackSI(400031033,True,100,"SIRadioShoot")
        Terminal.SetCheckBox("Kami Vac",True)
    elif job == 434: #dual blade
        attackSIND(400040006,True,16)
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)
        if job not in AngelicBusterJobs:
            Terminal.SetCheckBox("General FMA",False)
        #if job not in LuminousJobs:
        #    Terminal.SetCheckBox("Full Map Attack",False)

if not GameState.IsInGame() and not GameState.IsInCashShop() and not SCLib.GetVar("ToggleAttack"):
    SCLib.UpdateVar("ToggleAttack",True)
    print("Enabling TogglaAttack Flag")

if GameState.IsInGame() and accountData['arcane_daily_done'] and SCLib.GetVar("ToggleAttack") and job != -1:
    initAttackDone()
    SCLib.UpdateVar("ToggleAttack",False)
if GameState.IsInGame() and not accountData['arcane_daily_done'] and SCLib.GetVar("ToggleAttack") and job != -1:
    initAttack()
    SCLib.UpdateVar("ToggleAttack",False)

def initVars():
    SCLib.PersistVar("StartingMap", Field.GetID())
    SCLib.PersistVar("UsingKami", Terminal.GetCheckBox("Kami Vac"))
    SCLib.PersistVar("UsingSI", Terminal.GetCheckBox("Skill Injection"))
    SCLib.PersistVar("UsingAA", Terminal.GetCheckBox("Auto Attack"))
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
    #print("Initializing Dailies")
    #print(SCLib.GetVar("CurDaily"))
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
    vjQuests.append(VJQuest(34150, 450001216, 450001216, 3003109, 1299, -28))

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
            
            toggle_skill()
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
        if Field.GetID() == ccExitMap:
            Character.TalkToNpc(ccNpc)
        else:
            Terminal.Rush(ccStartingMap)
    else:
        SunCat.HookChuChu()
        
        Terminal.SetCheckBox("Auto NPC", True)
        Terminal.SetCheckBox("Kami Vac", False)
        Terminal.SetCheckBox("Full Map Attack", False)
        Terminal.SetCheckBox("General FMA", False)
        Terminal.SetCheckBox("Grenade Kami", False)
        Terminal.SetPushButton("Whitelist", False)
        
        changeChannel()
        
        SCLib.UpdateVar("CurStep", "StartingChuChu")
        

def startChuChu():
    if Field.GetID() != ccStartingMap:
        SCLib.UpdateVar("CurStep", "InitChuChu")
    elif Field.GetID() == ccExitMap:
        Character.TalkToNpc(ccNpc)
    else:
        retryCount = SCLib.GetVar("RetryCount")
        
        if retryCount > 3:
            SCLib.UpdateVar("RetryCount", 0)
            print("Finished ChuChu")
            SCLib.UpdateVar("CurStep", "FinishedChuChu")
            SunCat.UnhookChuChu()
        else:
            Terminal.StopRush()
            print("Talking to enter")
            Npc.ClearSelection()
            Npc.RegisterSelection("Enter")
            Npc.RegisterSelection("Hard")
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
                time.sleep(8)
                

def doingChuChu():
    if Field.GetID() != ccExitMap and Field.GetID() != ccStartingMap:
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
        Npc.RegisterSelection("Claim")
        Character.TalkToNpc(3003166)
        time.sleep(1)
        print("Done! Sleeping for a few seconds to check for another run...")
        SCLib.UpdateVar("CurStep", "InitChuChu")
        time.sleep(5)
#print(SCLib.GetVar("CurStep"))
def finishChuChu():
    chuchuSymbol = Inventory.FindItemByID(1712002)
    if not useSymbol(chuchuSymbol):
        if SCLib.GetVar("UsingWhitelist"):
            Terminal.SetPushButton("Whitelist", True)
        SCLib.UpdateVar("CurDaily", "DD")
        SCLib.UpdateVar("CurStep", "InitDD")
        
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

##########################
##########################
# Dream Defender Daily
##########################
##########################


NIGHTMARE_BOX = [9833080, 9833081, 9833082, 9833083, 9833084]
DD_MAP = [921171000, 921171001, 921171002, 921171003, 921171004, 921171005]
DD_CLOCKMAP = 450003540
DD_ENTERMAP = 450004000
DD_EXITMAP = 921171100
SLEEP_TIME = 0.5

CoinNpc = [9010101, 9010102, 9010103, 9010104, 9010105]
Lache_Town = 450003000


def toggle_attack(flag):
    if SCLib.GetVar("UsingAA"):
        Terminal.SetCheckBox("Auto Attack", flag)
    if SCLib.GetVar("UsingSI"):
        Terminal.SetCheckBox("Skill Injection", flag)
    if job in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay", flag)
    if job in KannaJobs: #MonkeySpiritsNDcheck
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", flag)

def is_in_center(x, y):
    ptgo_up = Field.FindPortal('ptgo_up')
    ptgo_down = Field.FindPortal('ptgo_down')
    ptgo_left = Field.FindPortal('ptgo_left')
    ptgo_right = Field.FindPortal('ptgo_right')
    ptback_up = Field.FindPortal('ptback_up')
    ptback_down = Field.FindPortal('ptback_down')
    ptback_left = Field.FindPortal('ptback_left')
    ptback_right = Field.FindPortal('ptback_right')
    return x >= ptgo_left.x - 50 and x <= ptgo_right.x + 50 and y >= ptgo_up.y - 50 and y <= ptgo_down.y + 50

def is_in_left(x, y):
    ptgo_up = Field.FindPortal('ptgo_up')
    ptgo_down = Field.FindPortal('ptgo_down')
    ptgo_left = Field.FindPortal('ptgo_left')
    ptgo_right = Field.FindPortal('ptgo_right')
    ptback_up = Field.FindPortal('ptback_up')
    ptback_down = Field.FindPortal('ptback_down')
    ptback_left = Field.FindPortal('ptback_left')
    ptback_right = Field.FindPortal('ptback_right')
    return x >= ptback_left.x - 450 and x <= ptback_left.x + 450 and y >= ptback_left.y - 250 and y <= ptback_left.y + 250

def is_in_right(x, y):
    ptgo_up = Field.FindPortal('ptgo_up')
    ptgo_down = Field.FindPortal('ptgo_down')
    ptgo_left = Field.FindPortal('ptgo_left')
    ptgo_right = Field.FindPortal('ptgo_right')
    ptback_up = Field.FindPortal('ptback_up')
    ptback_down = Field.FindPortal('ptback_down')
    ptback_left = Field.FindPortal('ptback_left')
    ptback_right = Field.FindPortal('ptback_right')
    return x >= ptback_right.x - 450 and x <= ptback_right.x + 450 and y >= ptback_right.y - 250 and y <= ptback_right.y + 250

def is_in_up(x, y):
    ptgo_up = Field.FindPortal('ptgo_up')
    ptgo_down = Field.FindPortal('ptgo_down')
    ptgo_left = Field.FindPortal('ptgo_left')
    ptgo_right = Field.FindPortal('ptgo_right')
    ptback_up = Field.FindPortal('ptback_up')
    ptback_down = Field.FindPortal('ptback_down')
    ptback_left = Field.FindPortal('ptback_left')
    ptback_right = Field.FindPortal('ptback_right')
    return x >= ptback_up.x - 450 and x <= ptback_up.x + 450 and y >= ptback_up.y - 250 and y <= ptback_up.y + 250

def is_in_down(x, y):
    ptgo_up = Field.FindPortal('ptgo_up')
    ptgo_down = Field.FindPortal('ptgo_down')
    ptgo_left = Field.FindPortal('ptgo_left')
    ptgo_right = Field.FindPortal('ptgo_right')
    ptback_up = Field.FindPortal('ptback_up')
    ptback_down = Field.FindPortal('ptback_down')
    ptback_left = Field.FindPortal('ptback_left')
    ptback_right = Field.FindPortal('ptback_right')
    return x >= ptback_down.x - 450 and x <= ptback_down.x + 450 and y >= ptback_down.y - 250 and y <= ptback_down.y + 250

def room_of(x, y):
    if is_in_center(x, y):
        return 'center'
    elif is_in_up(x, y):
        return 'up'
    elif is_in_down(x, y):
        return 'down'
    elif is_in_left(x, y):
        return 'left'
    elif is_in_right(x, y):
        return 'right'
    else:
        return None

def find_one_box():
    print("Searching a Box")
    flag = False
    for box_id in NIGHTMARE_BOX:
        mob = Field.FindMob(box_id)
        if mob.valid:
            print("Found Mob", mob, box_id)
            flag = True
            return mob
    print("Found None")
    return None

def close_enough(x1, y1, x2, y2, distance):
    if (x1 - x2)**2 + (y1 - y2)**2 < distance**2:
        return True
    else:
        return False

def safe_teleport(x, y):
    toggle_attack(False)
    pos = Character.GetPos()
    if not close_enough(pos.x, pos.y, x, y, 1000):
        print('TOO FAR. NOT SAFE TO TELEPORT!!!')
        time.sleep(SLEEP_TIME)
        return
    Character.Teleport(x, y - 5)
    time.sleep(SLEEP_TIME)

def safe_enter_portal():
    start = Character.GetPos()
    Character.EnterPortal()
    time.sleep(SLEEP_TIME)
    end = Character.GetPos()
    if close_enough(start.x, start.y, end.x, end.y, 10):
        Character.EnterPortal()

def moving_to_room(from_room, to_room):
    ptgo_up = Field.FindPortal('ptgo_up')
    ptgo_down = Field.FindPortal('ptgo_down')
    ptgo_left = Field.FindPortal('ptgo_left')
    ptgo_right = Field.FindPortal('ptgo_right')
    ptback_up = Field.FindPortal('ptback_up')
    ptback_down = Field.FindPortal('ptback_down')
    ptback_left = Field.FindPortal('ptback_left')
    ptback_right = Field.FindPortal('ptback_right')
    if from_room is None or to_room is None or from_room == to_room:
        return

    print('Moving from %s to %s.' % (from_room, to_room))
    if from_room == 'center':
        if to_room == 'up' and ptgo_up.valid:
            safe_teleport(ptgo_up.x, ptgo_up.y)
        elif to_room == 'down' and ptgo_down.valid:
            safe_teleport(ptgo_down.x, ptgo_down.y)
        elif to_room == 'left' and ptgo_left.valid:
            safe_teleport(ptgo_left.x, ptgo_left.y)
        elif to_room == 'right' and ptgo_right.valid:
            safe_teleport(ptgo_right.x, ptgo_right.y)
        safe_enter_portal()
    elif to_room == 'center':
        if from_room == 'up' and ptback_up.valid:
            safe_teleport(ptback_up.x, ptback_up.y)
        elif from_room == 'down' and ptback_down.valid:
            safe_teleport(ptback_down.x, ptback_down.y)
        elif from_room == 'left' and ptback_left.valid:
            safe_teleport(ptback_left.x, ptback_left.y)
        elif from_room == 'right' and ptback_right.valid:
            safe_teleport(ptback_right.x, ptback_right.y)
        safe_enter_portal()
    else:
        moving_to_room(from_room, 'center')

def start_DD():
    print("Attempting to join Dream Defender")
    Party.LeaveParty()
    Disabler()
    if Terminal.GetCheckBox("Skill Injection"):
        Terminal.SetCheckBox("Skill Injection", False)
    Npc.ClearSelection()
    Npc.RegisterSelection("Dream")
    Npc.RegisterSelection("Stage")
    Character.TalkToNpc(9010100)
    time.sleep(3)

def leave_DD():
    print("Get reward and leave")
    Character.TalkToNpc(9010100)    
    time.sleep(3)

def GetCoin(npc):
    print("Receiving coins from", npc)
    retry=0
    while SCLib.GetVar("DDCoin") == Inventory.GetItemCount(4310227) and retry<3:
        Character.TalkToNpc(npc)
        time.sleep(3)
        retry+=1

def Disabler():
    if Terminal.GetCheckBox("General FMA"):
        Terminal.SetCheckBox("General FMA", False)
    if Terminal.GetCheckBox("Full Map Attack"):
        Terminal.SetCheckBox("Full Map Attack", False)
    if Terminal.GetCheckBox("Grenade Kami"):
        Terminal.SetCheckBox("Grenade Kami", False)
    if Terminal.GetCheckBox("Mob Falldown"):
        Terminal.SetCheckBox("Mob Falldown", False)
    if Terminal.GetCheckBox("Kami Vac"):
        Terminal.SetCheckBox("Kami Vac", False)
    if Terminal.GetCheckBox("bot/kanna_kami"):
        Terminal.SetCheckBox("bot/kanna_kami", False)
    
    if not (Terminal.GetCheckBox("General FMA") or Terminal.GetCheckBox("Full Map Attack") or Terminal.GetCheckBox("Grenade Kami") or Terminal.GetCheckBox("Mob Falldown") or Terminal.GetCheckBox("bot/kanna_kami") or Terminal.GetCheckBox("Kami Vac")):
        return True
    else:
        return False


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

def Rush(mapid):
    if Terminal.IsRushing():
        time.sleep(1)
    elif Field.GetID() != mapid:
        time.sleep(1)
        Terminal.Rush(mapid)

def ToPortal(portal, enter=True):
    portal = Field.FindPortal(portal)
    if portal.valid:
        if not (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5):
            SunCat.Teleport(portal.x, portal.y-5)
            time.sleep(1)
            if enter:
                Character.EnterPortal()
                time.sleep(1)
        elif enter:
            time.sleep(1)
            Character.EnterPortal()

options = ['General FMA', 'Full Map Attack', 'Grenade Kami', 'Mob Falldown', 'Kami Vac', 'bot/kanna_kami', 'bot/si_no_wait', 'Skill Injection', 'Auto Attack']
for option in options:
    if SCLib.GetVar(option) is None:
        SCLib.PersistVar(option, Terminal.GetCheckBox(option))
    else:
        SCLib.UpdateVar(option, Terminal.GetCheckBox(option))

def RestoreSetting():
    print("restore terminal setting")
    for option in options:
        Terminal.SetCheckBox(option, SCLib.GetVar(option))

def doDreamDefenderLevels():
    while SCLib.GetVar("CurStep") == "InitDD":
        if Field.GetID() not in DD_MAP+[DD_CLOCKMAP, DD_ENTERMAP, DD_EXITMAP]:
            Rush(DD_CLOCKMAP)
        if Field.GetID() == DD_CLOCKMAP:
            ToPortal("top00")
            time.sleep(2)
            
        retryCount = 0
        while retryCount < 3 and Field.GetID() == DD_ENTERMAP:
            start_DD()
            retryCount += 1
            
        if retryCount == 3:
            print("Finished Dream Defender daily")
            SCLib.UpdateVar("CurStep", "StartingDD")
            break
        
        flag = True
        startStage = 0
        
        while GameState.IsInGame() and Field.GetID() in DD_MAP and Disabler():
            ptgo_up = Field.FindPortal('ptgo_up')
            ptgo_down = Field.FindPortal('ptgo_down')
            ptgo_left = Field.FindPortal('ptgo_left')
            ptgo_right = Field.FindPortal('ptgo_right')
            ptback_up = Field.FindPortal('ptback_up')
            ptback_down = Field.FindPortal('ptback_down')
            ptback_left = Field.FindPortal('ptback_left')
            ptback_right = Field.FindPortal('ptback_right')    
            print(ptgo_up.valid)
            if flag:
                startStage = SunCat.GetDDStage()
                flag = False
            
            if startStage != SunCat.GetDDStage():
                retreatDD()
            
            box = find_one_box()
            if box is None:
                print('Can not find any nightmare box. Wait.')
                toggle_attack(False)
                time.sleep(SLEEP_TIME*2)
            else:
                room_of_box = room_of(box.x, box.y)
                print(box.x, box.y)
                print('Found box in room: %s' % room_of_box)

                pos = Character.GetPos()
                room_of_char = room_of(pos.x, pos.y)
                print(pos.x, pos.y)
                print('The character is in room: %s' % room_of_char)

                if room_of_box == room_of_char:
                    if close_enough(pos.x, pos.y, box.x, box.y, 50):
                        print('Close enough. Toggle AA. Wait.')
                        toggle_attack(True)
                        time.sleep(SLEEP_TIME)
                    else:
                        print('Not close enough. Teleport to box.')
                        safe_teleport(box.x, box.y)
                        time.sleep(SLEEP_TIME)
                else:
                    moving_to_room(room_of_char, room_of_box)
            time.sleep(SLEEP_TIME)
        '''
        while Field.GetID() in DD_MAP:
            Disabler()
            print("Cleared the starting floor, wait and fail on purpose to leave the map")
            time.sleep(3)
        '''
        if Field.GetID() == DD_EXITMAP:
            RestoreSetting()
            leave_DD()

def doDreamDefenderCoins():
    while SCLib.GetVar("CurStep") == "StartingDD":
        print("Returning to Lachelein Main street")
        if Field.GetID() == DD_ENTERMAP:
            exitpt = Field.FindPortal("out00")
            Character.MoveX(exitpt.x+30, 4000)
            time.sleep(1)
            Character.EnterPortal()
            time.sleep(2)
        elif Field.GetID() != Lache_Town:
            Rush(Lache_Town)
            time.sleep(5)
        elif Field.GetID() == Lache_Town:
            print("Receiving coins from npcs")
            for npc in CoinNpc:
                SCLib.UpdateVar("DDCoin", Inventory.GetItemCount(4310227))
                GetCoin(npc)
            SCLib.UpdateVar("CurDaily", "SS")
            SCLib.UpdateVar("CurStep", "InitSS")
            print("Finished getting extra coins")

def doDD():
    if dailyDD:
        if SCLib.GetVar("CurStep") == "InitDD":
            doDreamDefenderLevels()
        elif SCLib.GetVar("CurStep") == "StartingDD":
            doDreamDefenderCoins()
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
        toggle_attack(True)
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
        time.sleep(1)
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
        if Inventory.GetItemCount(4310235) == (SCLib.GetVar("SpiritCoin")+30):
            SCLib.UpdateVar("CurDaily", "Return")
            SCLib.UpdateVar("RetryCount", 0)
            print("You earned daily cap for spirit coin")
            print("Finished Spirit Savior Daily")
            return
        elif SCLib.GetVar("RetryCount") < 3 and SCLib.GetVar("CurSSRuns") < totalRuns:
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

def dungeonTeleport():
    prefield = Field.GetID()
    Terminal.SetCheckBox("Kami Vac",False)
    time.sleep(1)
    Key.Press(0x08)
    time.sleep(1)
    Character.EnterPortal()
    time.sleep(1)
    newfield = Field.GetID()
    if newfield != prefield:
        print("Successfully entered portal")
        Terminal.SetCheckBox("Kami Vac",True)
    else:
        print("Failed to enter portal")

if GameState.IsInGame() and accountData['changing_mule'] and not accountData['arcane_daily_done']:
    initAttack()
    accountData['changing_mule'] = False
    writeJson(accountData,accountId)

if GameState.IsInGame() and not accountData['arcane_daily_done'] and not accountData['changing_mule'] and not SCLib.GetVar("ToggleAttack"): #only need to do this if daily is not done
    if GameState.IsInGame() and Inventory.GetItemCount(5040004) == 0 and Inventory.GetEmptySlotCount(5) > 0 and Character.GetMeso() >= 5200000:
        print("Need to buy a hyper teleport rock")
        autoAttack = Terminal.GetCheckBox("Auto Attack")
        skillInject = Terminal.GetCheckBox("Skill Injection")
        javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
        toggle_rush_by_level(False)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Skill Injection",False)
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        time.sleep(5)
        if Inventory.GetItemCount(5040004) == 0 and Inventory.GetEmptySlotCount(5) > 0 and Character.GetMeso() >= 5200000:
            nEmptySlotPOS = 0
            for i in range(1, Inventory.GetItemSlotCount(5)):
                pItem = Inventory.GetItem(5, i)
                if not pItem.valid:
                    nEmptySlotPOS = i
                    break
            if Terminal.IsRushing():
                Terminal.StopRush()
            time.sleep(1)
            Terminal.EnterCashShop()
            CashItemResLoadLockerDone()
            time.sleep(1)
        Terminal.SetCheckBox("Auto Attack",autoAttack)
        Terminal.SetCheckBox("Skill Injection",skillInject)
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
    elif Quest.GetQuestState(34120) != 2 and level >= 200:
        VJprequest()
    elif Quest.GetQuestState(34218) != 2 and level >= 210:
        Chuchuprequest()
    else:
        if Field.GetID() in [450002021,450001250,450001240]:
            dungeonTeleport()
        if SCLib.GetVar("CurDaily") is None:
            initAttack()
            print("Cur daily is none")
            time.sleep(2)
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
                print("Done with this character...")
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
                if GameState.IsInGame():
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
    Terminal.SetCheckBox("Auto Login",True)
    time.sleep(5)

if accountData['changing_mule'] and GameState.GetLoginStep() == 2 and not accountData['arcane_daily_done']:
    Terminal.SetCheckBox("Auto Login",False)
    Terminal.SetLineEdit("LoginChar",str(int(accountData["cur_pos"]) + 1)) #update cur pos to next
    Terminal.SetCheckBox("Auto Login",True)
    time.sleep(1)
    accountData["cur_pos"] = Terminal.GetLineEdit("LoginChar") #update cur pos
    accountData['changing_mule'] = False
    writeJson(accountData,accountId)
    KillPersistVarThred() #restart persisten variables

if accountData['arcane_daily_done'] and GameState.GetLoginStep() == 2: #returning to farming char
    Terminal.SetCheckBox("Auto Login",False)
    Terminal.SetLineEdit("LoginChar",str(accountData['training_char']))
    Terminal.SetCheckBox("Auto Login",True)
    time.sleep(1)
    accountData["cur_pos"] = Terminal.GetLineEdit("LoginChar")
    accountData['changing_mule'] = True
    writeJson(accountData,accountId)
    print("returning to farming character")

if accountData['arcane_daily_done'] and GameState.IsInGame() and accountData['changing_mule'] and job != 0 and job != 1: #set
    initAttackDone()
    accountData['changing_mule'] = False
    writeJson(accountData,accountId)


if Field.GetID() == ccExitMap and SCLib.GetVar("CurDaily") != "ChuChu":
    print("Leaving chuchu exit map")
    time.sleep(1)
    Npc.ClearSelection()
    Npc.RegisterSelection("Claim")
    Character.TalkToNpc(3003166)
    time.sleep(1)
    Npc.ClearSelection()


if Field.GetID() == ssExitMap and SCLib.GetVar("CurDaily") != "SS":
    Character.TalkToNpc(ssNpc)
elif Field.GetID() == ssExitMap and SCLib.GetVar("CurDaily") == "SS":
    finishSS()
if job == 2712 and not SCLib.GetVar("ToggleAttack"): #lumi fourth job kill switch
    attack_key = 0x44
    if Character.HasBuff(2,20040216): #Light Mode
        Key.Set(attack_key,1,27121100)
    elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
        Key.Set(attack_key,1,27111303)
    else:                              #Dark Mode
        Key.Set(attack_key,1,27121202)

#event_quests()
if GameState.IsInGame():
    toggle_skill()
print(SCLib.GetVar("CurDaily"))
#print(SCLib.GetVar("CurStep"))