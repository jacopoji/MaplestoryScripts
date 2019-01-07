import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal, Context, Inventory, Key, Quest, Party
#Auto Lotus Act3
#Author: Comicals
#v1.0 10/18/18

############################################
# False for Auto Attack
UseSI       = False
UseKami     = True

#If you d/c too much at hallway room, set it True and do it manually
Manual      = False
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

def WaitSpawn(timer, map):
    count = 0
    while count < timer and Field.GetID() == map and GameState.IsInGame():
        time.sleep(1)
        count+=1
        if MobExists():
            return False
    return True

if GameState.IsInGame():
    #debugging()
    currentMap = Field.GetID()
    if currentMap == 913050010:
        Party.LeaveParty()

    #act3
 
    Conference  = 350031003
    Deck        = 350031004
    WaistDeck   = 350031005
    HallWay     = 350031006
    Bedroom1    = 350031007
    HallWay2    = 350031200
    Bedroom2    = 350031300
    Bedroom3    = 350031400
    Prison      = 350031500
    Pilothouse  = 350031600
 
    DeckCorner  = 350032400
    AboveDeck1  = 350032100
    AboveDeck2  = 350032200
    AboveDeck3  = 350032300
    UnknownSky  = 350032500
 
    DeckOut     = 350033100
    NightSky    = 350033203
 
    if currentMap == Conference:
        ToPortal("out00")
 
    elif currentMap == Deck:
        if NeedQuest(33181):
            StartQuest(33181, 1540625)
        else:
            ToPortal("goHall")
 
    elif currentMap == WaistDeck:
        Npc.ClearSelection()
        Npc.RegisterSelection("We")
        ToPortal("out00")
   
    elif currentMap == HallWay:   
        if Field.FindNpc(1540618).valid:
            ToPortal("army1_1")
            for i in range(2):
                SpamKey("ctrl")
            LeftRight()
            time.sleep(3)
        elif Field.FindNpc(1540619).valid:
            ToPortal("army2_1")
            SpamSpace()
            time.sleep(3)
        else:
            ToPortal("inRoom1")
       
    elif currentMap == Bedroom1:
        if Field.FindNpc(1540634).valid:
            ToPortal("army9_1")
            SpamKey("ctrl")
            time.sleep(4)
            ToPortal("out00")
       
    elif MapRange(HallWay2):
        p1=p2=p3=p4=p5=True
        mobFlag = True
        while GameState.IsInGame() and Field.GetID()!=WaistDeck and p5:
            print(p1, p2, p3, p4, p5)
            time.sleep(3)
            if MapRange(HallWay2):
                if MobExists() and not Manual:
                    SetAttack()
                else:
                    if WaitSpawn(8):
                        mobFlag = False
                        if p1:
                            p1 = False
                        elif not p2 and p3:
                            p3 = False
                        elif not p4 and p5:
                            p5 = False
               
                    if not p1 and p3 and not mobFlag:
                        ToPortal("inRoom2")
                    elif not p3 and p5 and not mobFlag:
                        ToPortal("inRoom3")
                    elif not p5 and not mobFlag:
                        Npc.ClearSelection()
                        Npc.RegisterSelection("We")
                        ToPortal("inRoom4")
                        break
       
            elif MapRange(Bedroom2):
                mobFlag = True
                print("bed2")
                ToPortal("Army3_1")
                time.sleep(2)
                SpamKey("ctrl")
           
                time.sleep(3)
                ToPortal("Army4_1")
                time.sleep(2)
                SpamSpace()
           
                time.sleep(3)
                ToPortal("Army5_1")
                time.sleep(2)
                LeftRight()
           
                time.sleep(3)
                ToPortal("Army6_1")
                time.sleep(2)
                SpamSpace()
           
                time.sleep(3)
                ToPortal("out00")
                p2 = False
       
            elif MapRange(Bedroom3):
                mobFlag = True
                ToPortal("Army7_1")
                SpamSpace()
           
                time.sleep(4)
                ToPortal("Army8_1")
                LeftRight()
           
                time.sleep(4)
                ToPortal("out00")
                p4 = False
       
           
           
    elif MapRange(Pilothouse):
        if MobExists():
            SetAttack()
        else:
            SetAttack(False)
            LeftRight()
   
    elif MapRange(DeckCorner):
        SetAttack(False)
        if Field.FindNpc(1540610).valid:
            ToPortal("east00")
        else:
            Npc.ClearSelection()
            Npc.RegisterSelection("I will")
            time.sleep(1)
            ToPortal("mid00")
            time.sleep(5)
   
    elif MapRange(AboveDeck1):
        if Inventory.FindItem(4034229).count < 30:
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("west00")
       
   
    elif MapRange(AboveDeck2):
        if Inventory.FindItem(4034230).count < 30:
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("west00")
       
    elif MapRange(AboveDeck3):
        if Inventory.FindItem(4034231).count < 30:
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("west00")
       
    elif MapRange(UnknownSky):
        print("auto failing")
        CheckBox("30 Sec God Mode", False)
        CheckBox("Full God Mode", False)
        for i in range(5):
            Character.TakeDamage(1)
            time.sleep(1)
 
    elif MapRange(DeckOut):
        Npc.ClearSelection()
        Npc.RegisterSelection("Yes")
        Npc.RegisterSelection("Even")
        Npc.RegisterSelection("I had")
        Npc.RegisterSelection("I missed")
        Npc.RegisterSelection("Admit")
        ToPortal("west00")
        time.sleep(10)
   
    elif currentMap==NightSky:
        Npc.ClearSelection()
        Npc.RegisterSelection("(I would")
        Npc.RegisterSelection("Hit")
        time.sleep(5)
        SpamKey("down")