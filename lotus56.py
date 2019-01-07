import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal, Context, Inventory, Key, Quest, Party
if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")
try:
    import SunCat, SCLib
except:
    print("Couldn't find SunCat module")
#Auto Lotus Act5+6
#Author: Comicals
#v1.1 10/23/18 
############################################
# False for Auto Attack
UseSI       = False
UseKami     = True 

# if you use different npc interaction key, change corresponding virtual key.
# 0x20(space) is default
npckey      = 0x20

############################################
def SetAttack(toggle=True, kami=True):
    if toggle:
        if UseKami and kami:
            CheckBox("Kami Vac", True)
        else:
            CheckBox("Kami Vac", False)
        if UseSI:
            if Character.GetJob() == 4212:
                CheckBox("Skill Injection", False)
                CheckBox("MonkeySpiritsNDcheck", True)
            else:
                CheckBox("Skill Injection", True)
                CheckBox("MonkeySpiritsNDcheck", False)
        else:
            CheckBox("Skill Injection", False)
            CheckBox("MonkeySpiritsNDcheck", False)
            CheckBox("Auto Attack", True)
    else:
        CheckBox("Kami Vac", False)
        CheckBox("Auto Attack", False)
        CheckBox("Skill Injection", False)
        CheckBox("MonkeySpiritsNDcheck", False)

def ToPortal(portal, enter=True):
    map=Field.GetID()
    portal = Field.FindPortal(portal)
    if portal.valid:
        AAFlag      = False
        kamiFlag    = False
        if Terminal.GetCheckBox("Auto Attack"):
            AAFlag = True
            CheckBox("Auto Attack", False)
        if Terminal.GetCheckBox("Kami Vac"):
            kamiFlag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
           
        if not (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5):
            Character.Teleport(portal.x, portal.y-20)
            time.sleep(1)
           
        attempt = 0
        while enter and Field.GetID() == map and attempt<3:
            attempt+=1
            Character.EnterPortal()
            time.sleep(1)
           
        if AAFlag:
            CheckBox("Auto Attack", True)
        if kamiFlag:
            CheckBox("Kami Vac", True)

           
def Teleport(x, y):
    CheckBox("Kami Vac", False)
    time.sleep(1)
    if not (Character.GetPos().x < x+5 and Character.GetPos().x > x-5):
        Character.Teleport(x, y-5)
       
   
def ToNPC(npc, talk=False):
    npc = Field.FindNpc(npc)
    if npc.valid:
        flag = False
        if Terminal.GetCheckBox("Kami Vac"):
            flag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
           
        if not (Character.GetPos().x < npc.x+5 and Character.GetPos().x > npc.x-5):
            Character.Teleport(npc.x, npc.y-10)
            time.sleep(1)
            if talk:
                Character.TalkToNpc(npc)
       
        if flag:
            CheckBox("Kami Vac", True)
           
def DoQuest(id):
    if Quest.GetQuestState(id) != 2:
        return True
    else:
        return False

def NeedQuest(id):
    if Quest.GetQuestState(id) == 0:
        return True
    else:
        return False

def HasQuest(id):
    if Quest.GetQuestState(id) == 1:
        return True
    else:
        return False

def DoneQuest(id):
    if Quest.GetQuestState(id) == 2:
        return True
    else:
        return False
       
def InProgress(id, npc):
    if Quest.CheckCompleteDemand(id, npc) != 0:
        return True
    else:
        return False

def StartQuest(id, npc, tp=False):
    flag = False
    if Field.FindNpc(npc).valid and tp:
        if Terminal.GetCheckBox("Kami Vac"):
            flag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
        Character.Teleport(npc.x, npc.y-10)
       
    print("Getting quest "+str(id))
    Quest.StartQuest(id, npc)
    time.sleep(1)
   
    if flag:
        CheckBox("Kami Vac", True)
   
def CompleteQuest(id, npc, tp=False):
    flag = False
    if Field.FindNpc(npc).valid and tp:
        if Terminal.GetCheckBox("Kami Vac"):
            flag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
        Character.Teleport(npc.x, npc.y-10)
       
    print("Completing quest "+str(id))
    Quest.CompleteQuest(id, npc)
    time.sleep(1)

def CheckBox(set, value):
    if Terminal.GetCheckBox(set) != value:
        Terminal.SetCheckBox(set, value)
   
def CheckMap(map):
    if Field.GetID()==map:
        return True
    else:
        return False
       
def MapRange(map):
    if Field.GetID() >= map and Field.GetID() <= map+1:
        return True
    else:
        return False

def MobExists(count=0):
    if len(Field.GetMobs())>count:
        return True
    else:
        return False   
   
def SpamKey(key):
    if key == "down":
        key = 0x28
    elif key == "alt":
        key = 0x12
    elif key == "ctrl":
        key = 0x11
    elif key == "up":
        key = 0x26
    delay = 0
   
    for i in range(5):
        delay += 0.2
        time.sleep(delay)
        Key.Down(key)
        time.sleep(0.1)
        Key.Up(key)

def SpamSpace():
    for i in range(20):
        Key.Down(0x20)
        time.sleep(0.05)
        Key.Up(0x20)
   

def LeftRight():
    for i in range(50):
        Key.Down(0x25)
        time.sleep(0.02)
        Key.Up(0x25)
        time.sleep(0.02)
        Key.Down(0x27)
        time.sleep(0.02)
        Key.Up(0x27)

       
def debugging():
    print("", flush=False)
    print(Field.GetID(), flush=False)
    onpt = False
    ptname = ""
    for i in Field.GetPortals():
        if i.x < Character.GetPos().x+10 and i.x > Character.GetPos().x-10:
            onpt = True
            ptname = i.name
        print(i.name, end='     ', flush=False)
    print("", flush=False)
    if onpt:
        print("currently on",ptname, flush=False)
    print(len(Field.GetMobs()), flush=False)
   
def RobotAttack(atk=True):
    if atk:
        #CheckBox("General FMA", False)
        CheckBox("Melee No Delay", False)
        CheckBox("Skill Injection", False)
        CheckBox("Auto Attack", True)
        CheckBox("Kami Vac", True)
    else:
        CheckBox("Auto Attack", False)
        CheckBox("Kami Vac", False)
       

if GameState.IsInGame():
    currentMap = Field.GetID()
    if currentMap == 913050010:
        Party.LeaveParty()

    Gate            = 350050000
    EntryPath1      = 350050100
    EntryPath2      = 350050200
    BlackHD1        = 350051000
    BlackHD1050     = 350051050
    BlackHD1100     = 350051100
    BlackHD1150     = 350051150
    BlackHD1200     = 350051200
    BlackHD1250     = 350051250
    BlackHD1300     = 350051300
    BlackHD1250     = 350051250
    BlackHD1300     = 350051300
    BlackHD1350     = 350051350
    BlackHD1400     = 350051400
    BlackHD1450     = 350051450
   
    BlackHD2        = 350052000
    BlackHD2050     = 350052050
    BlackHD2100     = 350052100
    BlackHD2150     = 350052150
    BlackHD2200     = 350052200
    BlackHD2250     = 350052250
    BlackHD2300     = 350052300
    BlackHD2350     = 350052350
    BlackHD2400     = 350052400
    BlackHD2450     = 350052450
    BlackHD2500     = 350052500
    BlackHD2550     = 350052550
    BlackHD2600     = 350052600
    BlackHD2650     = 350052650
    BlackHD2700     = 350052700
    BlackHD2750     = 350052750   
    BlackHD2800     = 350052800
    BlackHD2900     = 350052900
   
    DeepHold        = 350053920
    DeepHold_path1  = 350053004
    DeepHold_path2  = 350053005
    DeepHold_path3  = 350053006
    DeepHold_path4  = 350053007
   
    DeepHold1       = 350053100
    DeepHold2       = 350053200
    DeepHold3       = 350053300
    DeepHold4       = 350053400
    DeepHold4_5       = 350053450
    DeepHold5       = 350053500
    DeepHold5_5       = 350053550
    DeepHold7       = 350053700
    DeepHold7_5     = 350053750
    DeepHold8       = 350053800
    DeepHold8_5     = 350053850
   
    BlackHD4        = 350054000
    BlackHD4100     = 350054100
    BlackHD4200     = 350054200
    BlackHD4300     = 350054300
    BlackHD4400     = 350054400
   
   
    BlackHD5        = 350055000
    BlackHD5100     = 350055100
    BlackHD5200     = 350055200
    BlackHD5300     = 350055300
    BlackHD5400     = 350055400
   
   
    BlackHD6        = 350056000
    BlackHD6100     = 350056100
    BlackHD6200     = 350056200
    BlackHD6300     = 350056300
    BlackHD6400     = 350056400
    BlackHD6500     = 350056500
   
   
    BlackHD8        = 350058000
    BlackHD8050     = 350058050
    BlackHD8100     = 350058100
    BlackHD8150     = 350058150
    BlackHD8200     = 350058200
    BlackHD8250     = 350058250
    BlackHD8300     = 350058300
   
    GasCollider     = 350058500
    GasLab          = 350058600
    ElevatorDeck    = 350058700
    Elevator        = 350058800
    Elevator2        = 350058850
   
   
    CoreEnterance   = 350060000
    Core            = 350060160
   
    Lotus1          = 350060220
    Lotus2          = 350060240
    Lotus3          = 350060260
   
   
    BHCorrider      = 350062000
    BHCorrider1      = 350062110
    BHCorrider2      = 350062120
    BHCorrider3      = 350062130
    BHCorrider4      = 350062150
   
   
    Quater          = 350062400
    Gelimer         = 350062410
    Gelimer2        = 350062500
    Escape1         = 350063000
    Escape2         = 350063001
    Escape3         = 350063002
    Escape4         = 350063003
    Escape5         = 350063004
   
   
    if currentMap == Gate:
        if DoQuest(33223):
            if NeedQuest(33223):
                Npc.ClearSelection()
                Npc.RegisterSelection("Trust")
                time.sleep(1)
                StartQuest(33223, 1540729)
        else:
            ToPortal("in00")
    elif currentMap in range(EntryPath1, EntryPath1+10):
        ToPortal("out00")
    elif currentMap == EntryPath2:
        ToNPC(1540710)
    elif currentMap == BlackHD1:
        ToPortal("goto_1050")
    elif currentMap in range(BlackHD1050, BlackHD1050+10):
        ToPortal("goto_1100")
    elif currentMap in range(BlackHD1100, BlackHD1100+10):
        if HasQuest(33225):
            if InProgress(33225, 1540732):
                SetAttack(True)
            else:
                CompleteQuest(33225, 1540732)
        else:
            SetAttack(False)
            ToPortal("goto_1200")
    elif currentMap in range(BlackHD1200, BlackHD1200+10):
        if HasQuest(33226):
            if InProgress(33226, 1540732):
                SetAttack(True)
            else:
                CompleteQuest(33226, 1540732)
        else:
            SetAttack(False)
            ToPortal("goto_1250")
    elif currentMap in range(BlackHD1250, BlackHD1250+10):
        ToPortal("goto_1300")
   
    elif currentMap in range(BlackHD1300, BlackHD1300+10):
        if not Inventory.FindItem(4009324).valid:
            ToPortal("goto_1350")
        else:
            ToPortal("goto_1500")
       
    elif currentMap in range(BlackHD1350, BlackHD1350+10):
        Character.MoveX(500, 5000)
       
    elif currentMap in range(BlackHD1400, BlackHD1400+10):
        if not Inventory.FindItem(4009324).valid:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("goto_1450")
           
    elif currentMap in range(BlackHD1450, BlackHD1450+10):
        ToPortal("goto_1300")
       
    elif currentMap == BlackHD2:
        ToPortal("goto_2050")
       
    elif currentMap in range(BlackHD2050, BlackHD2050+10):
        ToPortal("goto_2100")
       
    elif currentMap in range(BlackHD2100, BlackHD2100+10):
        ToPortal("goto_2200")
   
    #elif currentMap == range(BlackHD2150, BlackHD2150+10):
   
   
   
    elif currentMap in range(BlackHD2200, BlackHD2200+10):
        ToPortal("goto_2250")
       
    elif currentMap in range(BlackHD2250, BlackHD2250+10):
        ToPortal("goto_2350")
   
    #elif currentMap in range(BlackHD2300, BlackHD2300+10):
       
    elif currentMap in range(BlackHD2350, BlackHD2350+10):
        ToPortal("goto_2400")
       
    elif currentMap in range(BlackHD2400, BlackHD2400+10):
        ToPortal("goto_2450")
       
    elif currentMap in range(BlackHD2450, BlackHD2450+10):
        if HasQuest(33227):
            if InProgress(33227, 1540732):
                SetAttack(True)
            else:
                SetAttack(False)
                CompleteQuest(33227, 1540732)
        elif DoQuest(33228):
            SetAttack(False)
            if NeedQuest(33228):
                StartQuest(33228, 1540732)
            if HasQuest(33228):
                ToPortal("goto_2500")
            else:
                ToPortal("goto_2500")
               
       
   
    elif currentMap in range(BlackHD2500, BlackHD2500+10):
        if HasQuest(33228):
            ToNPC(1540757)
            Key.Press(npckey)
        else:
            ToPortal("goto_2550")
       
    elif currentMap in range(BlackHD2550, BlackHD2550+10):
        ToPortal("goto_2400")
       
    elif currentMap in range(BlackHD2800, BlackHD2800+10):
        ToPortal("goto_2600")
   
    elif currentMap in range(BlackHD2600, BlackHD2600+10):
        ToPortal("goto_2650")
       
   
    elif currentMap in range(BlackHD2650, BlackHD2650+10):
        if not Inventory.FindItem(4009324).valid:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("goto_2700")
   
    elif currentMap in range(BlackHD2700, BlackHD2700+10):
        ToPortal("goto_2900")
       
    elif currentMap in range(BlackHD2900, BlackHD2900+10):
        Npc.ClearSelection()
        Npc.RegisterSelection("Defeat")
        time.sleep(2)
       
    elif currentMap in range( DeepHold, DeepHold+10):
        if NeedQuest(33233):
            StartQuest(33233, 1540703)

    elif currentMap in range(DeepHold_path1, DeepHold_path1+4):
        SunCat.StopTP()
        ToPortal("endportal")
   
           
   
    elif MapRange(DeepHold1):
        if DoQuest(33234):
            Npc.ClearSelection()
            Npc.RegisterSelection("(Console ")
            ToPortal("mapTwoOne")
            time.sleep(5)
           
   
    elif currentMap in range( DeepHold2, DeepHold2+10):
        #ToPortal("mapTwoOne")
        if InProgress(33234, 1540709):
            SetAttack(True)
        else:
            SetAttack(False)
            CompleteQuest(33234, 1540709)
       
    elif currentMap in range( DeepHold3, DeepHold3+10):
        SetAttack(False)
        count = 0
       
       
        SunCat.KamiTP(303, -511)
        Character.BasicAttack()
        time.sleep(5)
        if Quest.GetQuestState(33236) != -1:
            SunCat.StopTP()
            StartQuest(33236, 1540703)
       
       
        SunCat.KamiTP(863, -511)
        Character.BasicAttack()
        if Quest.GetQuestState(33236) != -1:
            SunCat.StopTP()
            StartQuest(33236, 1540703)
        time.sleep(5)
           
           
    elif currentMap in range(DeepHold4, DeepHold4+10):
        ToPortal("mapTwoOne")
       
    elif currentMap in range(DeepHold4_5, DeepHold4_5+10):
        if InProgress(33237, 1540709):
            SetAttack(True)
        else:
            SetAttack(False)
            CompleteQuest(33237, 1540709)
   
    elif currentMap in range(DeepHold5_5, DeepHold5_5+10):
        SetAttack(False)
        print("Hit Left Top and Left Bottom")
        count=0
        pipe1 = [221, -940]
        pipe2 = [-165 -540]
       
        SunCat.KamiTP(221, -910)
        Character.BasicAttack()
        time.sleep(4)
        if Quest.GetQuestState(33239) != -1:
            SunCat.StopTP()
            StartQuest(33239, 1540703)
           
       
        SunCat.KamiTP(-165, -510)
        Character.BasicAttack()
        if Quest.GetQuestState(33239) != -1:
            SunCat.StopTP()
            StartQuest(33239, 1540703)
        time.sleep(4)
           
       
           
       
       
   
    elif currentMap in range(DeepHold7, DeepHold7+10):
        SetAttack(True)
   
    elif currentMap in range(DeepHold7_5, DeepHold7_5+10):
        SetAttack(False)
        LeftRight()
       
    elif currentMap in range(DeepHold8, DeepHold8+10):
        SetAttack(True)
       
    elif currentMap in range(DeepHold8_5, DeepHold8_5+10):
        SetAttack(False)
        LeftRight()
       
    if currentMap == 350053007:
        ToPortal("mapPT")
       
   
    elif currentMap == BlackHD4:
        ToPortal("in00")
       
   
    elif currentMap in range (BlackHD4100, BlackHD4100+10):
        if Field.FindPortal("hid00").valid:
            ToPortal("hid00")
            time.sleep(5)
        Teleport(-3800, 1360)
        time.sleep(5)
       
    #elif currentMap in range (BlackHD4100, BlackHD4100+10):
   
    elif currentMap in range (BlackHD4300, BlackHD4300+10):
        if len(Field.GetMobs())>1:
            SetAttack(True)
        else:
            SetAttack(False)
           
            for i in range(1):
                for i in Field.GetNpcs():
                    print(i.x, i.y)
                    Character.Teleport(i.x, i.y-100)
                    Key.Press(npckey)
                    time.sleep(2)
           
            ToPortal("next00")
   
   
    if currentMap == BlackHD5:
        ToPortal("in00")
       
    elif currentMap in range(BlackHD5100, BlackHD5100+10):
        ToPortal("out00")
   
    elif currentMap in range(BlackHD5200, BlackHD5200+10):
        if not Inventory.FindItem(4009324).valid:
            ToPortal("outup")
        else:
            ToPortal("outdown")
   
    elif currentMap in range(BlackHD5300, BlackHD5300+10):
        mob = Field.FindMob(8240085)
        while mob.valid:
            SunCat.KamiTP(mob.x-50, mob.y)
       
        if not Inventory.FindItem(4009324).valid:
            SetAttack(True, False)
        else:
            SunCat.StopTP()
            SetAttack(False)
            ToPortal("next00")
           
    elif currentMap in range(BlackHD5400, BlackHD5400+10):
        ToPortal("out00")
        #Teleport(3052,687)
        #Character.EnterPortal()
       
    if currentMap ==  BlackHD6:
        ToPortal("in00")
       
   
   
    elif currentMap in range(BlackHD6100, BlackHD6100+10):
        if len(Field.GetMobs())>1:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("out00")
           
    elif currentMap in range(BlackHD6200, BlackHD6200+10):
        if len(Field.GetMobs())>1:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("out00")
           
    elif currentMap in range(BlackHD6300, BlackHD6300+10):
        if len(Field.GetMobs())>1:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("out00")
   
   
    elif currentMap in range(BlackHD6400, BlackHD6400+10): 
        Teleport(-4174,777)
        Key.Press(npckey)
   
   
    elif currentMap in range(BlackHD6500, BlackHD6500+10):
        if len(Field.GetMobs())>1:
            RobotAttack()
        else:
            RobotAttack(False)
            ToPortal("out00")
   
    if currentMap == BlackHD8:
        ToPortal("in00")
   
    elif currentMap in range(BlackHD8050, BlackHD8050+10):
        if len(Field.GetMobs())>0:
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("pt_next")
           
   
    elif currentMap in range(BlackHD8100, BlackHD8100+10):
        ToPortal("pt_next")
   
    elif currentMap in range(BlackHD8150, BlackHD8150+10):
        if len(Field.GetMobs())>0:
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("pt_next")
           
    elif currentMap in range(BlackHD8200, BlackHD8200+10):
        ToPortal("pt_next")
   
    elif currentMap in range(BlackHD8150, BlackHD8150+10):
        if len(Field.GetMobs())>0:
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("pt_next")
   
    elif currentMap in range(BlackHD8250, BlackHD8250+10):
        Teleport(3000, -1000)
   
    elif currentMap in range(BlackHD8300, BlackHD8300+10):
        if len(Field.GetMobs())>0:
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("pt_next")
            time.sleep(3)
            if NeedQuest(33250):
                StartQuest(33250, 1540723)
   
   
    if currentMap == GasCollider:
        ToPortal("pt_next")
   
    elif currentMap == GasLab:
        if DoQuest(33251):
            StartQuest(33251, 1540724)
        elif DoQuest(33252):
            StartQuest(33252, 1540725)
        elif DoQuest(33253):
            StartQuest(33253, 1540726)
        elif DoQuest(33254):
            StartQuest(33254, 1540727)
        elif DoQuest(33255):
            StartQuest(33255, 1540728)
   
    elif currentMap == ElevatorDeck:
        ToPortal("pt_350058700")
       
    elif currentMap == Elevator:
        CheckBox("30 Sec God Mode", True)
        #Character.Teleport(-193,-600)
       
    elif currentMap == Elevator2:
        ToPortal("in00")
       
    if currentMap==CoreEnterance:
        SetAttack(False)
        ToPortal("bossIn00")
       
    if currentMap in range(Core, Core+10):
        SetAttack(True)
   
    if MapRange(Lotus1) or MapRange(Lotus2) or MapRange(Lotus3):
        SetAttack()
   
   
    if currentMap == BHCorrider:
        SetAttack(False)
        ToPortal("In00")
   
    elif currentMap in range(BHCorrider1, BHCorrider1+10):
        if len(Field.GetMobs())>0:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
   
    elif currentMap in range(BHCorrider3, BHCorrider3+10):
        if len(Field.GetMobs())>0:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
           
    elif currentMap in range(BHCorrider4, BHCorrider4+10):
        if len(Field.GetMobs())>0:
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
           
    if currentMap == Quater:
        SetAttack(False)
        ToPortal("pt00")
        Character.TalkToNpc()
   
    elif currentMap == Gelimer:
        Npc.ClearSelection()
        Npc.RegisterSelection("Please")
        time.sleep(2)
        SpamSpace()
       
    elif currentMap == Gelimer2:
        Character.MoveX(Field.FindPortal("pt00").x, 8000)
        #ToPortal("pt00")
        SpamSpace()
       
    elif currentMap == 350062900:
        ToPortal("out00")
   
    elif currentMap == Escape1:
        Character.MoveX(0, 5000)
       
    elif currentMap == Escape2:
        ToPortal("wet00")
       
    elif currentMap == Escape3:
        ToPortal("west00")
       
    elif currentMap == Escape4:
        time.sleep(2)
        ToPortal("pt00")
       
    elif currentMap == Escape5:
        time.sleep(2)
        ToPortal("pt00")
        SpamKey("alt")
       
else:
    SetAttack(False)
    SunCat.StopTP()