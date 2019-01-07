import Field, GameState, Terminal, time, Character, Npc, Quest, Packet, os, sys, DataType, Key

# raigeki_scripts
# gollux prequest + maze teleporter v197.4
# utilizes SunCat Lib: https://www.gamekiller.net/threads/suncat-library-hotkeys-more.3265846/

# tp packet
header = 0x0327

# using kami?
# no = 0  (gfma/fma)
# yes = 1
kami = 0

# using auto attack?
# no = 0  (skill injection)
# yes = 1
auto = 0

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")

try:
    import SunCat, SCHotkey, SCLib
except:
    pr("Couldn't find SunCat module")


def pr(string):  # in anticipation for SunCat's future fix on his SunPrint override function to implement the use of flush
    return print(string)

def mapID(id):
    if type(id) is int:
        return Field.GetID() == id
    else:
        return Field.GetID() in id

def rush(mapid):
    if not Terminal.IsRushing():
        pr("Rushing to map ID: {0}".format(mapid))
        Terminal.Rush(mapid)
        time.sleep(1)
    else:
        time.sleep(1)

def tele(x, y):
    pr("Teleporting to {0}, {1}".format(x, y))
    Character.Teleport(x, y - 10)
    time.sleep(1)

def goThru(x, y):
    tele(x, y - 10)
    pr("Going thru portal.")
    Character.EnterPortal()
    time.sleep(.5)
    Character.EnterPortal()
    time.sleep(1)

def mazeMove(x, y):
    global here
    Character.Teleport(x, y - 10)
    time.sleep(.5)
    pr("Teleporting to maze portal.")
    while Field.GetID() != here:
        pr("Current map is {0} and here variable map is {1}".format(Field.GetID(), here))
        here = Field.GetID()
    if Field.GetID() == here:
        attempts = 4
        pr("You are still in initial map {0}, trying to go to next map.".format(here))
        for x in range(attempts):
            pr("Running attempt #" + str(x + 1))
            if Field.GetID() != here:
                break
            Character.EnterPortal()
            time.sleep(.2)

def setAttack(bool):
    if Character.GetJob() == 4212:  # kanna settings
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", bool)
        Terminal.SetCheckBox("bot/kanna_kami", bool)
        Terminal.SetCheckBox("Summon Kishin", bool)
        Terminal.SetCheckBox("bot/kishin_fma", bool)
        Terminal.SetCheckBox("Grenade Kami", bool)
    elif Character.GetJob() == 3712:  # blaster settings
        if Terminal.GetLineEdit("SISkillID") != "37121003":
            Terminal.SetLineEdit("SISkillID", "37121003")
        if Terminal.GetRadioButton("SkillInjection2") is False:
            Terminal.SetRadioButton("SkillInjection2", True)
        if Terminal.GetCheckBox("Melee No Delay") is True:
            Terminal.SetCheckBox("Melee No Delay", False)
        if Terminal.GetCheckBox("General FMA") is False:
            Terminal.SetCheckBox("General FMA", True)
        Terminal.SetCheckBox("Skill Injection", bool)
    elif Character.GetJob() == 15512:  # ark settings
        if Terminal.GetLineEdit("SISkillID") != "155121007":
            Terminal.SetLineEdit("SISkillID", "155121007")
        if Terminal.GetRadioButton("SkillInjection2") is False:
            Terminal.SetRadioButton("SkillInjection2", True)
        if Terminal.GetSpinBox("SkillInjection") != 200:
            Terminal.SetSpinBox("SkillInjection", 200)
        if Terminal.GetCheckBox("Melee No Delay") is False:
            Terminal.SetCheckBox("Melee No Delay", True)
        if Terminal.GetCheckBox("General FMA") is False:
            Terminal.SetCheckBox("General FMA", True)
        Terminal.SetCheckBox("Skill Injection", bool)
    else:
        if kami == 1 and Terminal.GetCheckBox("Kami Vac") != bool:
            Terminal.SetCheckBox("Kami Vac", bool)
        if auto == 1 and Terminal.GetCheckBox("Auto Attack") != bool:
            Terminal.SetCheckBox("Auto Attack", bool)
        elif auto == 0 and Terminal.GetCheckBox("Skill Injection") != bool:
            Terminal.SetCheckBox("Skill Injection", bool)

def startQuest(quest, npc):
    pr("Starting quest {0} from npc {1}".format(quest, npc))
    Quest.StartQuest(quest, npc)
    time.sleep(1)

def completeQuest(quest, npc):
    pr("Completing quest {0} from npc {1}".format(quest, npc))
    Quest.StartQuest(quest, npc)
    time.sleep(1)

def chatQuest(quest, nStart, nEnd=None):
    if nEnd is None:
        nEnd = nStart
    if needQuest(quest):
        startQuest(quest, nStart)
    elif hasQuest(quest):
        completeQuest(quest, nEnd)

def needQuest(id):  # quest hasn't been accepted
    return Quest.GetQuestState(id) == 0

def hasQuest(id):  # quest is active
    return Quest.GetQuestState(id) == 1

def doQuest(id):  # quest isn't complete/turned in
    return Quest.GetQuestState(id) != 2

def questDone(quest, npc):
    return Quest.CheckCompleteDemand(quest, npc) == 0

def mazeKey(dKey):
    global here
    key = ['up', 'down', 'left', 'right']
    portalName = []
    if mapID(863000015):
        portalName = ["up00", "down00", "west00", "Out00"]
    elif mapID(range(863000000, 863000015)):
        portalName = ["up00", "down00", "west00", "east00"]

    for num in range(4):
        if key[num] == dKey:
            here = Field.GetID()
            portal = Field.FindPortal(portalName[num])
            mazeMove(portal.x, portal.y)

def wait(delay, quest, npc):
    for s in range(delay):
        if GameState.IsInGame() and not questDone(quest, npc):
            time.sleep(1)
        else:
            break


if SCLib.CheckVersion(21):
    if GameState.IsInGame():
        # settings
        Terminal.SetRushByLevel(False)
        Terminal.SetCheckBox("Rush By Level", False)
        Terminal.SetCheckBox("map/maprusher/hypertelerock", False)
        Terminal.SetCheckBox("Auto NPC", True)
        Terminal.SetCheckBox("Auto Rune", True)
        Terminal.SetSpinBox("KamiOffsetX", -75)
        Terminal.SetSpinBox("KamiOffsetY", -50)
        here = []
        was = []

        # main script
        if doQuest(31260):
            # quest id's
            q0 = 31240
            q1 = q0 + 1
            q2 = q1 + 1
            q3 = q2 + 1
            q4 = q3 + 1
            q5 = q4 + 1
            q6 = q5 + 1
            q7 = q6 + 1
            q9 = q7 + 2
            q10 = q9 + 1
            q12 = q10 + 2
            q13 = q12 + 1
            q15 = q13 + 2
            q16 = q15 + 1
            q17 = q16 + 1
            q18 = q17 + 1
            q19 = q18 + 1
            q20 = q19 + 1

            # npc id's
            nGrendel = 1032001
            nPepper = 2134009
            nRidley = 2134012

            # map id's
            mCitadel = 301000000

            if doQuest(q0):
                chatQuest(q0, nGrendel)

            elif doQuest(q1):
                if needQuest(q1):
                    startQuest(q1, nGrendel)

            elif doQuest(q2):
                if needQuest(q2):
                    startQuest(q2, nGrendel)
                elif hasQuest(q2):
                    if mapID(mCitadel):
                        completeQuest(q2, nPepper)
                    else:
                        warp = Packet.COutPacket(header)
                        warp.EncodeBuffer("0692AD4E 00000005")
                        Packet.SendPacket(warp)

            elif doQuest(q3):
                chatQuest(q3, nPepper, nRidley)

            elif doQuest(q4):
                chatQuest(q4, nRidley, nPepper)

            elif doQuest(q5):
                chatQuest(q5, 0, nRidley)

            elif doQuest(q6):
                if needQuest(q6):
                    startQuest(q6, nRidley)
                elif hasQuest(q6):
                    if questDone(q6, nRidley):
                        if mapID(mCitadel):
                            completeQuest(q6, nRidley)
                        else:
                            rush(mCitadel)
                    else:
                        setAttack(True)
                        rush(301010000)  # hall of storms 1
                        wait(30, q6, nRidley)
                        rush(301010100)  # hall of storms 2
                        wait(30, q6, nRidley)

            elif doQuest(q7):
                chatQuest(q7, nPepper)

            elif doQuest(q9):
                if needQuest(q9):
                    startQuest(q9, nRidley)
                elif hasQuest(q9):
                    if questDone(q9, nRidley):
                        if mapID(mCitadel):
                            completeQuest(q9, nRidley)
                        else:
                            rush(mCitadel)
                    else:
                        rush(301020000)  # hall of magic 1
                        wait(30, q9, nRidley)
                        rush(301020100)  # hall of magic 2
                        wait(30, q9, nRidley)

            elif doQuest(q10):
                chatQuest(q10, nPepper)

            elif doQuest(q12):
                if needQuest(q12):
                    startQuest(q12, nRidley)
                elif hasQuest(q12):
                    if questDone(q12, nRidley):
                        if mapID(mCitadel):
                            completeQuest(q12, nRidley)
                        else:
                            rush(mCitadel)
                    else:
                        rush(301030000)  # hall of gales 1
                        wait(30, q12, nRidley)
                        rush(301030100)  # hall of gales 2
                        wait(30, q12, nRidley)

            elif doQuest(q13):
                chatQuest(q13, nPepper)

            elif doQuest(q15):
                if needQuest(q15):
                    lv = Terminal.GetCheckBox("Legit Vac")
                    startQuest(q15, nRidley)
                elif hasQuest(q15):
                    if questDone(q15, nRidley):
                        Terminal.SetCheckBox("Legit Vac", lv)
                        if mapID(mCitadel):
                            completeQuest(q15, nRidley)
                        else:
                            rush(mCitadel)
                    else:
                        rush(301040000)  # hall of the night 1
                        Terminal.SetCheckBox("Legit Vac", False)  # legit vac with flying mobs doesn't work and will cause dc's
                        wait(30, q15, nRidley)
                        rush(301040100)  # hall of the night 2
                        Terminal.SetCheckBox("Legit Vac", True)
                        wait(30, q15, nRidley)

            elif doQuest(q16):
                chatQuest(q16, nPepper)

            elif doQuest(q17):
                if needQuest(q17):
                    startQuest(q17, nRidley)

            elif doQuest(q18):
                if needQuest(q18):
                    startQuest(q18, 0)
                elif hasQuest(q18):
                    if questDone(q18, 0):
                        time.sleep(5)
                        completeQuest(q18, 0)
                    else:
                        rush(301070010)  # path to the altar (boss)
                        time.sleep(2)

            elif doQuest(q19):
                if needQuest(q19):
                    pr("Requirements: 2 empty USE slots and 1 empty EQUIP slot")
                    startQuest(q19, 0)  # 2 use slots, 1 equip slot free

            elif doQuest(q20):
                if needQuest(q20):
                    rush(mCitadel)
                    startQuest(q20, nRidley)
                elif hasQuest(q20):
                    if questDone(q20, nRidley):
                        setAttack(False)
                        if mapID(mCitadel):
                            completeQuest(q20, nRidley)
                        else:
                            rush(mCitadel)
                    else:
                        if mapID(301060000):  # guardsman crossway
                            setAttack(True)
                            time.sleep(2)
                        else:
                            rush(301060000)

        if doQuest(17523):
            # quest id's
            q0 = 17500
            q1 = q0 + 1
            q2 = q1 + 1
            q3 = q2 + 1
            q4 = q3 + 1
            q5 = q4 + 1
            q6 = q5 + 1
            q7 = q6 + 1
            q8 = q7 + 1
            q9 = q8 + 1
            q10 = q9 + 1
            q11 = q10 + 1
            q12 = q11 + 1
            q13 = q12 + 1
            q14 = q13 + 1
            q15 = q14 + 1
            q16 = q15 + 1
            q17 = q16 + 1
            q18 = q17 + 1
            q19 = q18 + 1
            q20 = q19 + 1
            q21 = q20 + 1
            q22 = q21 + 1
            q23 = q22 + 1

            # npc id's
            nPepper = 9390112
            nChermini = 9390113
            nJayJay = 9390114
            nHologram = 9390101
            nDevice = 9390102
            nHilla = 9390100
            nGuardian = 9390120

            # map id's
            mRefuge = 863100000
            mMaze = range(863000000, 863000016)

            # maze hotkeys
            SCHotkey.RegisterKeyEvent(0x26, mazeKey, 'up')
            SCHotkey.RegisterKeyEvent(0x28, mazeKey, 'down')
            SCHotkey.RegisterKeyEvent(0x25, mazeKey, 'left')
            SCHotkey.RegisterKeyEvent(0x27, mazeKey, 'right')

            if mapID(mRefuge):
                setAttack(False)
                time.sleep(2)

            if mapID(mMaze):  # if you're in the maze
                SCHotkey.StartHotkeys(10)
                Terminal.SetComboBox("eva_cmb", 0)  # no reaction
                time.sleep(2)

            elif not mapID(mMaze):  # if you're not in the maze
                Terminal.SetComboBox("eva_cmb", 3)  # next map cc
                time.sleep(2)

            if doQuest(q0):
                if needQuest(q0):
                    setAttack(False)
                    startQuest(q0, nPepper)
                elif hasQuest(q0):
                    if mapID(301000000) and Quest.GetQuestState(31260) == 2:
                        goThru(1360, 323)
                    elif mapID(301070000):  # path to the altar
                        goThru(682, 323)
                    elif mapID(863100008):  # crimsonheart ruins exterior
                        goThru(128, 118)
                    elif mapID(863100001):  # shadow veil forest 1
                        goThru(538, 118)
                    elif mapID(mRefuge):
                        tele(820, 58)
                        completeQuest(q0, nPepper)

            elif doQuest(q1):
                chatQuest(q1, nPepper)

            elif doQuest(q2):
                if needQuest(q2):
                    startQuest(q2, nPepper)
                if hasQuest(q2):
                    if questDone(q2, nPepper):
                        rush(mRefuge)
                        tele(820, 58)
                        completeQuest(q2, nPepper)
                    else:
                        if not mapID(863100002):
                            rush(863100002)  # shadow veil forest 2
                        setAttack(True)
                        time.sleep(2)

            elif doQuest(q3):
                if needQuest(q3):
                    startQuest(q3, nPepper)
                elif hasQuest(q3):
                    if questDone(q3, nPepper):
                        rush(mRefuge)
                        tele(820, 58)
                        completeQuest(q3, nPepper)
                    else:
                        if not mapID(863100003):
                            rush(863100003)  # shadow veil forest 3
                        setAttack(True)
                        time.sleep(2)

            elif doQuest(q4):
                if needQuest(q4):
                    startQuest(q4, nPepper)
                elif hasQuest(q4):
                    if questDone(q4, nPepper):
                        rush(mRefuge)
                        tele(820, 58)
                        completeQuest(q4, nPepper)
                    else:
                        if not mapID(863100004):
                            rush(863100004)  # shadow veil forest 4
                        setAttack(True)
                        time.sleep(2)

            elif doQuest(q5):
                if needQuest(q5):
                    startQuest(q5, nChermini)
                elif hasQuest(q5):
                    rush(863100005)  # shadow veil forest 5
                    completeQuest(q5, nJayJay)

            elif doQuest(q6):
                chatQuest(q6, nJayJay)

            elif doQuest(q7):
                chatQuest(q7, nJayJay)

            elif doQuest(q8):
                if needQuest(q8):
                    setAttack(False)
                    startQuest(q8, nJayJay)
                elif hasQuest(q8):
                    if not questDone(q8, nJayJay):
                        if mapID(863100005):
                            goThru(152, -2)
                        elif mapID(863000017):
                            goThru(270, 118)
                        elif mapID(863000000):
                            setAttack(True)
                            time.sleep(2)

            elif doQuest(q9):
                if needQuest(q9):
                    pr(">>>>>>>>>>>>>>>>>>>>>>>>>> Go to Labyrinth 2")
                    time.sleep(2)
                    if mapID(863000001):
                        startQuest(q9, 0)
                    else:
                        setAttack(False)
                        time.sleep(2)
                elif hasQuest(q9):
                    if questDone(q9, 0):
                        setAttack(False)
                        completeQuest(q9, 0)
                    else:
                        if mapID(863000001):
                            setAttack(True)
                            time.sleep(2)
                        else:
                            setAttack(False)
                            time.sleep(2)

            elif doQuest(q10):
                if needQuest(q10):
                    pr(">>>>>>>>>>>>>>>>>>>>>>>>>> Go to Labyrinth 3")
                    time.sleep(2)
                    if mapID(863000002):
                        startQuest(q10, 0)
                elif hasQuest(q10):
                    if questDone(q10, 0):
                        setAttack(False)
                        completeQuest(q10, 0)
                    else:
                        if mapID(863000002):
                            setAttack(True)
                            time.sleep(2)
                        else:
                            setAttack(False)
                            time.sleep(2)

            elif doQuest(q11):
                if needQuest(q11):
                    pr(">>>>>>>>>>>>>>>>>>>>>>>>>> Go to Labyrinth 5")
                    time.sleep(2)
                    if mapID(863000004):
                        startQuest(q11, 0)
                elif hasQuest(q11):
                    if questDone(q11, 0):
                        setAttack(False)
                        completeQuest(q11, 0)
                    else:
                        if mapID(863000004):
                            setAttack(True)
                            time.sleep(2)
                        else:
                            setAttack(False)
                            time.sleep(2)

            elif doQuest(q12):
                if needQuest(q12):
                    pr(">>>>>>>>>>>>>>>>>>>>>>>>>> Go to Labyrinth's End")
                    time.sleep(2)
                    if mapID(863000016):
                        startQuest(q12, nHologram)
                elif hasQuest(q12):
                    completeQuest(q12, nHologram)

            elif doQuest(q13):
                chatQuest(q13, 0, nJayJay)

            elif doQuest(q14):
                if needQuest(q14):
                    startQuest(q14, nJayJay)
                elif hasQuest(q14):
                    if mapID(mRefuge):
                        completeQuest(q14, nChermini)
                    else:
                        rush(mRefuge)

            elif doQuest(q15):
                if needQuest(q15):
                    nJayJay = 9390111
                    startQuest(q15, nJayJay)
                elif hasQuest(q15):
                    if mapID(863100006):
                        completeQuest(q15, nJayJay)
                    else:
                        rush(863100006)

            elif doQuest(q16) and Quest.GetQuestState(q15) == 2:
                if Quest.GetQuestState(q16) <= 0:
                    if mapID(863100100):
                        startQuest(q16, nDevice)
                    else:
                        rush(863100100)
                elif hasQuest(q16):
                    completeQuest(q16, nDevice)

            elif doQuest(q17) and Quest.GetQuestState(q16) == 2:
                if Quest.GetQuestState(q17) <= 0:
                    if mapID(863100103):
                        startQuest(q17, 0)
                    else:
                        rush(863100103)
                elif hasQuest(q17):
                    completeQuest(q17, 0)

            elif doQuest(q18):
                if needQuest(q18):
                    if mapID(863100104):
                        startQuest(q18, nHilla)
                    else:
                        rush(863100104)
                elif hasQuest(q18):
                    if questDone(q18, nHilla):
                        setAttack(False)
                        if mapID(863100104):
                            completeQuest(q18, nHilla)
                        else:
                            rush(863100104)
                    else:
                        if mapID(863100105):
                            setAttack(True)
                            time.sleep(2)
                        else:
                            setAttack(False)
                            time.sleep(2)

            elif doQuest(q19):
                if needQuest(q19):
                    startQuest(q19, 0)
                elif hasQuest(q19):
                    if mapID(mRefuge):
                        completeQuest(q19, nPepper)
                    else:
                        rush(mRefuge)

            elif doQuest(q20):
                chatQuest(q20, nPepper)

            elif doQuest(q21):
                if needQuest(q21):
                    startQuest(q21, 0)
                elif hasQuest(q21):
                    if mapID(mRefuge):
                        rush(863100005)
                    elif mapID(863100005):
                        goThru(152, -2)
                    elif mapID(863000017):
                        goThru(270, 118)
                    elif mapID(863000016):
                        completeQuest(q21, nHologram)
                    pr(">>>>>>>>>>>>>>>>>>>>>>>>>> Go to Labyrinth's End")
                    time.sleep(2)

            elif doQuest(q22):
                if needQuest(q22):
                    startQuest(q22, nHologram)
                elif hasQuest(q22):
                    if questDone(q22, nHologram):
                        if mapID(863000016):
                            completeQuest(q22, nHologram)
                        else:
                            if mapID(863000015):
                                setAttack(False)
                                goThru(305, -362)
                            else:
                                pr(">>>>>>>>>>>>>>>>>>>>>>>>>> Go to Labyrinth's End")
                                time.sleep(2)
                    else:
                        if mapID(863000016):
                            goThru(-1277, 118)
                        elif mapID(863000015):
                            setAttack(True)
                            time.sleep(2)
                        else:
                            setAttack(False)
                            time.sleep(2)

            elif doQuest(q23):
                if needQuest(q23):
                    goThru(285, 118)
                    startQuest(q23, nGuardian)
                elif hasQuest(q23):
                    if questDone(q23, nGuardian):
                        setAttack(False)
                        if mapID(863000100):
                            completeQuest(q23, nGuardian)
                        else:
                            if mapID(863000015):
                                goThru(305, -362)
                            elif mapID(863000016):
                                goThru(285, 118)
                    else:
                        if mapID(863000100):
                            goThru(-1201, 118)
                        elif mapID(863000016):
                            goThru(-1279, 118)
                        elif mapID(863000015):
                            setAttack(True)
                            time.sleep(2)
                        else:
                            time.sleep(3)
            else:
                pr("No tasks.")
        else:
            pr("Nothing to do.")