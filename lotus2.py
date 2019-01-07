import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal, Context, Inventory, Key, Quest, Party
#Auto Lotus Act2
#v1.0 10/16/18

############################################

UseKami = True
UseSI = True  # False for Auto Attack

############################################


def SetAttack(toggle=True):
    if toggle:
        if UseKami:
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
    CheckBox("Kami Vac", False)
    time.sleep(1)
    portal = Field.FindPortal(portal)
    if portal.valid:
        if not (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5):
            Character.Teleport(portal.x, portal.y-20)
            time.sleep(1)
            if enter:
                Character.EnterPortal()
                time.sleep(1)
        elif enter:
            time.sleep(1)
            Character.EnterPortal()
          
def Teleport(x, y):
    CheckBox("Kami Vac", False)
    time.sleep(1)
    if not (Character.GetPos().x < x+5 and Character.GetPos().x > x-5):
        Character.Teleport(x, y-5)
      
def ToNPC(npc):
    CheckBox("Kami Vac", False)
    time.sleep(1)
    npc = Field.FindNpc(npc)
    if npc.valid:
        if not (Character.GetPos().x < npc.x+5 and Character.GetPos().x > npc.x-5):
            Character.Teleport(npc.x, npc.y-10)
    time.sleep(1)

def ToReactor(react):
    CheckBox("Kami Vac", False)
    time.sleep(1)
    react = Field.FindReactor(react)
    if react.valid:
        SunCat.KamiTP(react.x-20, react.y+20)
    time.sleep(1)
  
def Attacks(number):
    for i in range(number):
        Character.BasicAttack()
        time.sleep(1.5)
    SunCat.StopTP()
      
def Rush(mapid):
    if Terminal.IsRushing():
        time.sleep(1)
    elif Field.GetID() != mapid:
        time.sleep(1)
        Terminal.Rush(mapid)
      
def DoQuest(id):
    if Quest.GetQuestState(id) != 2:
        #print("havn't finished quest "+str(id)+" yet")
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
        print("Currently doing quest "+str(id))
        return True
    else:
        return False

def StartQuest(id, npc):
    print("Getting quest "+str(id))
    Quest.StartQuest(id, npc)
    time.sleep(2)
  
def CompleteQuest(id, npc):
    print("Completing quest "+str(id))
    Quest.CompleteQuest(id, npc)
    time.sleep(2)

def CheckBox(set, value):
    if Terminal.GetCheckBox(set) != value:
        Terminal.SetCheckBox(set, value)
  
def CheckMap(map):
    if Field.GetID()==map:
        return True
    else:
        return False
      
def MapRange(map):
    if Field.GetID() >= map and Field.GetID() < map+10:
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

if GameState.IsInGame():
    #debugging()
    currentMap = Field.GetID()
    if currentMap == 913050010:
        Party.LeaveParty()
      
    #act2
    Boarding        = 350020023
    Deck            = 350020100
    CentralDeck     = 350020110
    Sparrow         = 350020300
    MainDeck        = 350020120
    WaistDeck       = 350020400
    Conference      = 350020700
    HallWay         = 350020800
    Storage         = 350021300
    StorageEscape   = 350022000
    Storage2        = 350022010
    Attack1         = 350022100
    Attack2         = 350022200
    Attack3         = 350022300
    WaistDeck2      = 350022400
    Attack5         = 350022500
    Attack6         = 350022600
    Attack7         = 350022700
  
    MainDeck3       = 350023000
    Deck1           = 350023100
    Deck2           = 350023200
    Deck3           = 350023300
    Deck4           = 350023400
    Deck5           = 350023500
    Deck6           = 350023600
    Deck7           = 350023700
  
    Conference2     = 350024100
    WaistDeck3      = 350024200
    HallWay2        = 350024300
    Quarter1        = 350024400
    Quarter2        = 350024500
    Quarter3        = 350024600
    Quarter4        = 350024400
  
  
    if currentMap == Boarding:
        SetAttack(False)
        ToPortal("west00")
    elif currentMap == Deck:
        SetAttack(False)
        if not HasQuest(33164):
            Npc.ClearSelection()
            Npc.RegisterSelection("We can")
            time.sleep(1)
            Character.TalkToNpc(1540550)
        else:
            Teleport(-955,-118)
            time.sleep(3)
            SpamKey("ctrl")
      
        if DoQuest(33165):
            if NeedQuest(33165):
                StartQuest(33165, 1540551)
            if HasQuest(33165):
                ToPortal("west00")
    elif currentMap == CentralDeck:
        SetAttack(False)
        if HasQuest(33165):
            Npc.ClearSelection()
            Npc.RegisterSelection("It")
            time.sleep(1)
            Character.TalkToNpc(1540554)
          
        if DoQuest(33166):
            if NeedQuest(33166):
                StartQuest(33166, 1540554)
            if HasQuest(33166):
                ToPortal("west00")
    elif MapRange(Sparrow):
        if InProgress(33166, 1540555):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("west00")
          
    elif MapRange(MainDeck):
        if HasQuest(33166):
            CompleteQuest(33166, 1540555)
        elif NeedQuest(33167):
            StartQuest(33167, 1540555)
        elif HasQuest(33167):
            ToPortal("west00")
          
    elif MapRange(WaistDeck):
        if HasQuest(33167):
            ToPortal("left")
        else:
            ToPortal("right")
      
    elif MapRange(Conference):
        if HasQuest(33167):
            CompleteQuest(33167, 1540556)
        else:
            ToPortal("out00")
  
    elif MapRange(HallWay):
        print("Not automated")
        print("Choose Right and You cannot hit her")
        Npc.ClearSelection()
        Npc.RegisterSelection("right")
        Npc.RegisterSelection("You cannot")
        time.sleep(2)
        ToPortal("in00")
        time.sleep(3)
  
    elif MapRange(Storage):
        if MobExists:
            SetAttack(True)
        else:
            SetAttack(False)
            Npc.ClearSelection()
            Npc.RegisterSelection("right")
            Npc.RegisterSelection("You cannot")
            time.sleep(5)
    elif MapRange(StorageEscape):
        SetAttack(False)
        SpamSpace()
  
    elif MapRange(Storage2):
        SetAttack(False)
        ToPortal("out00")
      
    elif MapRange(Attack1):
        if MobExists(0):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("next00")
          
    elif MapRange(Attack2):
        if MobExists(1):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("next00")
  
    elif MapRange(Attack3):
        if MobExists(0):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("next00")
      
    elif MapRange(Attack5):
        if MobExists(0):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("next00")
          
    elif MapRange(Attack6):
        if MobExists(0):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("next00")
          
    elif MapRange(Attack7):
        if MobExists(0):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("next00")
    elif MapRange(WaistDeck2):
        ToPortal("center")
      
    elif MapRange(MainDeck3):
        ToPortal("east00")
      
    elif MapRange(Deck1):
        if MobExists():
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
          
    elif MapRange(Deck2):
        if MobExists(1):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
          
    elif MapRange(Deck3):
        if MobExists(1):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
          
    elif MapRange(Deck4):
        if MobExists():
            SetAttack(True)
        else:
            SetAttack(False)
            SpamKey("alt")
            ToPortal("east00")
          
    elif MapRange(Deck5):
        if MobExists(1):
            SetAttack(True)
        else:
            SetAttack(False)
            SpamKey("down")
            ToPortal("east00")
  
    elif MapRange(Deck6):
        if MobExists(1):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
  
    elif MapRange(Deck7):
        if MobExists(1):
            SetAttack(True)
        else:
            SetAttack(False)
            ToPortal("east00")
  
    elif MapRange(Conference2):
        ToPortal("out00")
  
    elif MapRange(WaistDeck3):
        ToPortal("right")
      
    elif MapRange(HallWay2):
        p1=p2=p3=p4=True      
        while GameState.IsInGame() and (p3 or p4) and Field.GetID() != 913050010:
            print("Logout or stop script to break out loop if this shit is looping poorly, and do it manually")
            if MapRange(HallWay2) and p3:
                SetAttack(False)
          
                ToPortal("in01")
          
                ToPortal("in02")
              
                ToPortal("in03")
              
            if not p3:
                ToPortal("out00")
                p4=False
          
            if MapRange(Quarter1):
                if MobExists():
                    SetAttack()
                else:
                    SetAttack(False)
                    ToPortal("out00")
                    p1 = False
          
            elif MapRange(Quarter2):
                if MobExists():
                    SetAttack()
                else:
                    SetAttack(False)
                    ToPortal("out00")
                    p2 = False
          
            elif MapRange(Quarter3):
                if MobExists():
                    SetAttack()
                else:
                    SetAttack(False)
                    ToPortal("out00")
                    p3 = False
          
            time.sleep(3)