import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal, Context, Inventory, Key, Quest, Party
if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")
try:
    import SunCat, SCLib
except:
    print("Couldn't find SunCat module")

#Auto Lotus Act1
#v1.2 10/16/18 v1.2 (GMS 199.3)

############################################

UseKami = True
UseSI = True  # False for Auto Attack


UsePacket = True
q1Header = 0x032C
elevatorRequestHeader = 0x00EE
elevatorResultHeader = 0x00EC

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
            Character.Teleport(portal.x, portal.y-15)
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
    if Quest.CheckCompleteDemand(id, npc) == 1:
        #print("Currently doing quest "+str(id))
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
if GameState.IsInGame():
    q1 = 31900
    q2 = 31901
    q3 = 33150
 
    AirShip = 350011010
    NightSky = 350011020
    BlackWingDen1 = 350011100
    BlackWingDen2 = 350011200
    BlackWingDen3 = 350011300
    BlackWingDen4 = 350011800
    BlackWingDen5 = 350011900
    WireRoute1 = 350011400
    WireRoute2 = 350011410
    RailWay = 350011420
    Silo1 = 350011430
    Silo2 = 350011500
    PathEmpress = 350012010
    Hospital = 350013000
    Mindscape1 = range(350013100, 350013100+10)
    Mindscape2 = range(350013200, 350013200+10)
    Mindscape3 = range(350013300, 350013300+10)
    Mindscape4 = range(350013500, 350013500+10)
 
 
 
    currentMap = Field.GetID()
    #act1
    if DoQuest(q1):
        SetAttack(False)
        if NeedQuest(q1):
            if currentMap == 913050010:
                StartQuest(q1, 1105001)
            else:
                if UsePacket:
                    if currentMap != 100000000:
                        Rush(100000000)
                    else:
                        q1Packet = Packet.COutPacket(q1Header)
                        q1Packet.EncodeBuffer("01399E27 00000001")
                        Packet.SendPacket(q1Packet)
        elif HasQuest(q1):
            if currentMap == 913050010:
                CompleteQuest(q1, 1105001)
             
 
    elif DoQuest(q2):
        if NeedQuest(q2):
            if currentMap == 913050010:
                SetAttack(False)
                StartQuest(q2, 1105001)
        elif HasQuest(q2):
            if currentMap == 913050010:
                SetAttack(False)
                print("Enter scenario")
                Party.LeaveParty()
             
            elif currentMap == AirShip:
                SetAttack(False)
                if NeedQuest(q3):
                    StartQuest(33150, 1540503)
                if DoneQuest(q3):
                    Character.MoveX(1000, 5000)
                 
            elif currentMap == NightSky:
                SetAttack(False)
                Npc.ClearSelection()
                Npc.RegisterSelection("Let's go")
                time.sleep(2)
                ToPortal("pt_BHpark1")
             
            elif currentMap in [BlackWingDen1, BlackWingDen2, BlackWingDen3, BlackWingDen4, BlackWingDen5]:
                if not (Field.FindMob(8240021).valid or Field.FindMob(8240022).valid or Field.FindMob(8240048).valid):
                    SetAttack(False)
                    ToPortal("pt_Next")
                    ToPortal("pt_next")
                    ToPortal("pt_done")
                else:
                    SetAttack(True)
                 
            elif currentMap == WireRoute1:
                SetAttack(False)
                print("Password 0196")
                #CheckBox("Auto NPC", False)
                ToNPC(1540501)
                '''
                if UsePacket:
                    Character.TalkToNpc(1540501)
                    time.sleep(2)
                    Packet.BlockSendHeader(elevatorResultHeader)
                    elePacket = Packet.COutPacket(elevatorRequestHeader)
                    elePacket.EncodeBuffer("00 37 01 04 00 30 31 39 36")
                    Packet.SendPacket(elePacket)
                    time.sleep(3)
                    Packet.UnBlockSendHeader(elevatorResultHeader)
                '''
            elif currentMap == WireRoute2:
                SetAttack(False)
                #CheckBox("Auto NPC", True)
                Character.Teleport(1979, -500)
                time.sleep(3)
         
            elif currentMap == RailWay:
                SetAttack(False)
                Character.Teleport(-11, -8500)
                time.sleep(3)
             
            elif currentMap == Silo1:
                SetAttack(False)
                Teleport(1528,-145)
                Attacks(8)
            elif currentMap == Silo2:
                SetAttack(False)
                time.sleep(1)
             
            elif currentMap == PathEmpress:
                SetAttack(False)
                Npc.ClearSelection()
                Npc.RegisterSelection("I'm")
                Teleport(-500,88)
                Character.MoveX(-1500, 5000)
             
            elif currentMap == Hospital:
                SetAttack(False)
                if DoQuest(33157):
                    Npc.ClearSelection()
                    Npc.RegisterSelection("The Empress")
                    time.sleep(2)
                    Character.TalkToNpc(1540511)
             
                elif DoQuest(33158):
                    if NeedQuest(33158):
                        StartQuest(33158, 1540514)
                    else:
                        #print("enter")
                        Character.TalkToNpc(1540510)
         
            elif currentMap in Mindscape1:
                p1 = p2 = True
                while CheckMap(currentMap) and GameState.IsInGame():
                    SetAttack(False)
                 
                    while p1 and CheckMap(currentMap):
                        Character.MoveX(Field.FindReactor(3500001).x, 10000)
                        p1 = False
                 
                    while p2 and CheckMap(currentMap):
                        Reactors = range(3500001, 3500006)
                        for i in Reactors:
                            ToReactor(i)
                            Attacks(5)
                            SunCat.StopTP()
                         
                        if Field.GetID() != currentMap:
                            p2 = False
                 
                    if p1 == p2 == False and CheckMap(currentMap):
                        Character.MoveX(1600, 10000)
             
            elif currentMap in Mindscape2:
                p1 = p2 = p3 = p4 = True
                while CheckMap(currentMap) and GameState.IsInGame():
                    while p1:
                        SetAttack(False)
                        time.sleep(2)
                        Teleport(-580,148)
                        p1 = False
                        time.sleep(3)
                     
                    while p2:
                        while(Inventory.FindItem(4000890).count < 20) and CheckMap(currentMap):
                            SetAttack(True)
                        p2 = False
                        time.sleep(3)
                 
                    while p3:
                        SetAttack(False)
                        time.sleep(2)
                        ToPortal("in01")
                        p3 = False
                        time.sleep(3)
                     
                    while p4:
                        while(Inventory.FindItem(4000890).count < 30) and CheckMap(currentMap):
                            SetAttack(True)
                        else:
                            SetAttack(False)
                            ToPortal("in02")
                            time.sleep(3)
                            p4 = False
                         
                    if p1 == p2 == p3 == p4:
                        SetAttack(False)
                        ToReactor(3500006)
                        Character.BasicAttack()
                        SunCat.StopTP()
                        time.sleep(5)
         
            elif currentMap in Mindscape3:
                p1 = p2 = p3 = p4 = p5 = True
                reactors = [3500007, 3500008, 3500009, 3500010]
                mobs = [8240032, 8240023, 8240025, 8240024]
                while CheckMap(currentMap) and GameState.IsInGame():
                    while p1 and CheckMap(currentMap):
                        while Field.FindMob(mobs[0]).valid:
                            SetAttack(True)
                            time.sleep(1)

                        SetAttack(False)
                        Teleport(180, -208)
                        ToReactor(reactors[0])
                        Attacks(3)
                     
                        Teleport(1525, 69)
                        if Field.FindMob(mobs[1]).valid:
                            p1 = False
                            print("p2")
                                     
                    Teleport(1525, 69)
                    while p2 and CheckMap(currentMap):
                        while Field.FindMob(mobs[1]).valid:
                            SetAttack(True)
                     
                        SetAttack(False)
                        Teleport(1525, 69)
                        ToReactor(reactors[1])
                        Attacks(3)
                        if Field.FindMob(mobs[2]).valid:
                            p2 = False
                            print("p3")
                 
                    while p3 and CheckMap(currentMap):
                        while Field.FindMob(mobs[2]).valid:
                            SetAttack(True)
                            time.sleep(1)
                     
                        SetAttack(False)
                        Teleport(1525, 69)                     
                        ToReactor(reactors[2])
                        Attacks(3)
                        if Field.FindMob(mobs[3]).valid:
                            p3 = False
                            print("p4")

                    while p4 and CheckMap(currentMap):
                        while Field.FindMob(mobs[3]).valid:
                            SetAttack(True)
                            if Field.GetMobCount() < 3:
                                SunCat.KamiTP(180, -208)
                                time.sleep(5)
                                SunCat.StopTP()
                        p4 = False
                        time.sleep(3)
                    Teleport(1525, 69)
                    time.sleep(2)
                    ToReactor(reactors[3])
                    Attacks(3)
                    print("done")
         
            elif currentMap in Mindscape4:
                time.sleep(5)
                while CheckMap(currentMap) and GameState.IsInGame():
                    p1=p2=p3=p4=True
                 
                 
                    while p1 and CheckMap(currentMap):
                        Teleport(-692,-200)
                        p1=False
                        print("done p1")
                        time.sleep(3)
                     
                    while p2 and CheckMap(currentMap):
                        while(Inventory.FindItem(4000890).count < 30) and CheckMap(currentMap):
                            SetAttack(True)
                        p2 = False
                        print("done p2")
                        time.sleep(3)
                     
                    while p3 and CheckMap(currentMap):
                        SetAttack(False)
                        time.sleep(2)
                        Teleport(0,-200)
                        time.sleep(3)
                        ToPortal("in01")
                        p3 = False
                        print("done p3")
                        time.sleep(3)
                     
                    p4flag=True
                    while p4 and CheckMap(currentMap):
                        if p4flag:
                            Character.MoveX(1200, 4000)
                            p4flag=False
                            time.sleep(3)
                        reacts = [3500011, 3500012, 3500013, 3500014, 3500015, 3500016, 3500017]
                        for i in reacts:
                            if not CheckMap(currentMap):
                                break
                            ToReactor(i)
                            Attacks(5)
                            SunCat.StopTP()
                         
                        if CheckMap(currentMap):
                            time.sleep(10)
                     
else:
    SetAttack(False)
    SunCat.StopTP()