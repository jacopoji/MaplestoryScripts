import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal, Context, Inventory, Key, Quest, Party
#Auto Lotus Act4
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
    portal = Field.FindPortal(portal)
    if portal.valid:
        flag = False
        if Terminal.GetCheckBox("Kami Vac"):
            flag = True
            CheckBox("Kami Vac", False)
            time.sleep(1)
          
        if not (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5):
            Character.Teleport(portal.x, portal.y-20)
            time.sleep(1)
            if enter:
                Character.EnterPortal()
                time.sleep(1)
        elif enter:
            time.sleep(1)
            Character.EnterPortal()
          
        if flag:
            time.sleep(1)
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
            time.sleep(1)
            CheckBox("Kami Vac", True)
          
      
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
      
      
    Gate            = 350040000
    Gate2           = 350040002
    UnholyPath      = 350040020
    UnholyPath2      = 350040030
    HighPathStandby = 350040041
    HighPath      = 350040050
  
    ShipDeck0       = 350042720
    ShipDeck        = 350042700
    DeadEnd         = 350043000
    SecretEnterance = 350044000
    SecretPath      = 350044001
    Refuge          = 350040100
    NearRefuge      = 350040130
    NearRefuge2      = 350040150
    RefugeWait      = 350040161
    RefugeAttack    = 350040170
    AndroidMemory   =350040190
    CentralTower1    = 350040200
    CentralTower2    = 350040220
    CentralTower3    = 350040240
    Transmit        = 350040260
  
    Inspection      = 350042000
    Inspection2      = 350042050
  
    BehindStation   = 350042002
    ShipDeck1       = 350042100
    ShipDeck3       = 350042200
    ShipDeck6       = 350042350
    ShipDeck7       = 350042400
    ShipDeck8       = 350042450
    ShipDeck9       = 350042500
    Flare           = 350042603
  
  
    if currentMap == Gate:
        ToPortal("pt_event1")
  
    elif currentMap == Gate2:
        ToPortal("pt_next")
      
    elif MapRange(UnholyPath):
        ToPortal("pt_out")
      
    elif MapRange(UnholyPath2):
        ToPortal("pt_out")
  
    elif currentMap==HighPathStandby:
        Npc.ClearSelection()
        Npc.RegisterSelection("I'm")
        time.sleep(1)
        Character.TalkToNpc(1540502)
      
      
    elif MapRange(HighPath):
        if MobExists():
            SetAttack()
        else:
            SetAttack(False)
  
    elif MapRange(350040100):
        if HasQuest(33202):
            if InProgress(33202, 1540665):
                SetAttack(False)
                ToPortal("pt_left")
            else:
                ToNPC(1540665)
                CompleteQuest(33202, 1540665)
        elif DoQuest(33203):
            if NeedQuest(33203):
                StartQuest(33203, 1540665)
            elif HasQuest(33203):
                if InProgress(33203, 1540665):
                    SetAttack(False)
                    ToPortal("pt_right")
                else:
                    ToNPC(1540665)
                    CompleteQuest(33203, 1540665)
        elif NeedQuest(33204):
            StartQuest(33204, 1540664)
              
          
    elif MapRange(NearRefuge):
        if InProgress(33202, 1540665):
            SetAttack(True)
        else:
            SetAttack(False)
            Npc.ClearSelection()
            Npc.RegisterSelection("Yeah,")
            time.sleep(1)
            ToPortal("pt_out")
          
    elif MapRange(NearRefuge2):
        if InProgress(33203, 1540665):
            SetAttack(True)
        else:
            SetAttack(False)
            Npc.ClearSelection()
            Npc.RegisterSelection("Yeah,")
            time.sleep(1)
            ToPortal("pt_out")
  
    elif MapRange(RefugeAttack):
        SetAttack(True)
      
    elif MapRange(AndroidMemory):
        SetAttack(False)
        if NeedQuest(33206):
            StartQuest(33206, 1540662)
        elif HasQuest(33206):
            CompleteQuest(33206, 1540650)
  
    elif MapRange(CentralTower1):
        ToPortal("pt_up")
  
    elif MapRange(CentralTower2):
        ToPortal("pt_next")  
  
    elif MapRange(CentralTower3):
        ToPortal("pt_next")
  
    elif MapRange(Transmit):
        SetAttack(False)
        Teleport(-420,52)
        time.sleep(3)
        '''
        if UsePacket:
            #bPacket = lPacket = aPacket = cPacket = Packet.COutPacket(gateSend)
            #B,L,A,C in order
            print("sending packet")
            buffers = ["07CAF4A2 00000002 0000", "07CAF4A2 00000001 0000", "07CAF4A2 00000003 0000", "07CAF4A2 00000004 0000"]
            for buffer in buffers:
                print(buffer)
                gatePacket = Packet.COutPacket(gateSend)
                gatePacket.EncodeBuffer(buffer)
                wait = Packet.WaitForRecv(gateRecv, 10000)
                Packet.SendPacket(gatePacket)
        '''
          
        Key.Press(0x20)
        #time.sleep(2)
        #Key.Press
      
        #press space
        #press blac
  
    elif MapRange(Inspection):
        SpamKey("alt")
        LeftRight()
      
    elif currentMap == BehindStation:
        ToPortal("east00")
      
    elif MapRange(Inspection2):
        if MobExists():
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("next00")
  
    elif MapRange(ShipDeck1):
        if MobExists():
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("next00")
  
    elif MapRange(ShipDeck3):
        if MobExists():
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("next00")
          
    elif MapRange(ShipDeck6):
        if MobExists():
            SetAttack()
        else:
            SetAttack(False)
            ToPortal("next00")
    elif MapRange(ShipDeck7):
        if MobExists():
            SetAttack()
        else:
            SetAttack(False)
            ToNPC(1540679)
            Key.Press(npckey)
  
    elif MapRange(ShipDeck8):
        if MobExists(4):
            RobotAttack()
        else:
            RobotAttack(False)
            ToPortal("next00")
      
      
    elif MapRange(ShipDeck9):
        if MobExists(8):
            RobotAttack()
        else:
            RobotAttack(False)
            ToPortal("next00")
  
    elif currentMap == Flare:
        SpamKey("up")
      
    elif currentMap == ShipDeck0:
        ToPortal("pt_run")
  
    elif currentMap == ShipDeck:
        CheckBox("30 Sec God Mode", True)
        Teleport(-771,155)
      
    elif currentMap == DeadEnd:
        SpamKey("down")
      
    elif currentMap == SecretEnterance:
        ToPortal("out00")
  
    elif currentMap == SecretPath:
        ToPortal("out00")