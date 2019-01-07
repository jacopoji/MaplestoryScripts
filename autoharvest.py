import Character, GameState, Context, DataType, Field, Inventory, Key, Npc, Packet, Quest, Terminal, time, random

silvervein = 200000
magentavein = 200001
bluevein = 200002
brownvein = 200003
emeraldvein = 200004
goldvein = 200005
aquamarinevein = 200006
redvein = 200007
blackvein = 200008
purplevein = 200009
#-----#
silverherb = 100000
magentaherb = 100001
blueherb = 100002
brownherb = 100003
emeraldherb = 100004
goldherb = 100005
aquamarineherb = 100006
redherb = 100007
blackherb = 100008
purpleherb = 100009




toMine = [silverherb,magentaherb,blueherb,brownherb,emeraldherb,goldherb,aquamarineherb,redherb,blackherb,purpleherb] #Enter which vein/herb you want to mine/harvest.




####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################



class Platform(object):
    def __init__(self, y):
        self.y = y


class Rope(object):
    def __init__(self, x, y, plat):
        self.x = x
        self.y = y
        self.platform = plat
        
    def toRope(self):
        pos = Character.GetPos()
        while pos.x not in range(self.x-75,self.x+75):
            Character.AMoveX(self.x)
            pos = Character.GetPos()
        storedY = pos.y
        Character.StopMove()
        time.sleep(0.4)
        Character.AMoveX(self.x)
        Character.Jump()
        time.sleep(0.1) #NOT SURE IF NEEDED
        while pos.y > self.platform.y:
            Character.StopMove()
            Character.AMoveY(self.platform.y)
            pos = Character.GetPos()
            if pos.y == storedY:
                self.toRope()
                return
        Character.StopMove()

def Mine(vein):
    pos = Character.GetPos()
    while pos.x < (vein.x - 50) or pos.x > (vein.x + 50):
        Character.AMoveX(vein.x)
        pos = Character.GetPos()
    Character.StopMove()
    print("Pressing mining key")
    time.sleep(.25)
    Key.Press(0x20)
    time.sleep(.1)
    Key.Press(0x20)
    time.sleep(.1)
    Key.Press(0x20)
    time.sleep(4)

harvestMap = [910001011, 910001012, 910001013, 910001014]
Npc.ClearSelection()
Npc.RegisterSelection("Level")

ground = Platform(510)
firstPlat = Platform(210)
secondPlat = Platform(-30)
thirdPlat = Platform(-270)
fourthPlat = Platform(-510)
lastPlat = Platform(-750)
#-----#
firstRope = Rope(1180, 510, firstPlat)
secondRope = Rope(1060, 210, secondPlat)
thirdRope = Rope(450, -30, thirdPlat)
fourthRope = Rope(1340, -270, fourthPlat)
lastRope = Rope(538, -510, lastPlat)

if GameState.IsInGame():
    if Field.GetID() in harvestMap:
        reactors_temp = Field.GetReactors()
        reactors = []
        for items in reactors_temp:
            if items.y+1 in [510,210,-30,-270,-510,-750]:
                reactors.append(items)
        print("find reactor")
        pos = Character.GetPos()
        for reactor in reactors:
            if reactor.id in toMine:
                break
        #reactor = Field.FindReactor(random.choice(toMine))
        if reactor.valid:
            print("found valid reactor at x={},y={}".format(reactor.x,reactor.y))
            if reactor.y + 1 == ground.y:
                while pos.y < ground.y:
                    Character.JumpDown()
                    time.sleep(0.4)
                    pos = Character.GetPos()
                    if pos.y == ground.y:
                        break
                if pos.y == ground.y:
                    Mine(reactor)
            elif reactor.y + 1 == firstPlat.y:
                while pos.y < firstPlat.y:
                    Character.JumpDown()
                    time.sleep(0.4)
                    pos = Character.GetPos()
                    if pos.y == firstPlat.y:
                        break
                while pos.y > firstPlat.y:
                    if pos.y == ground.y:
                        Rope.toRope(firstRope)
                        pos = Character.GetPos()
                        break
                if pos.y == firstPlat.y:
                    Mine(reactor)
            elif reactor.y + 1 == secondPlat.y:
                while pos.y < secondPlat.y:
                    Character.JumpDown()
                    time.sleep(0.4)
                    pos = Character.GetPos()
                    if pos.y == secondPlat.y:
                        break
                while pos.y > secondPlat.y:
                    if pos.y == ground.y:
                        Rope.toRope(firstRope)
                        Rope.toRope(secondRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == firstPlat.y:
                        Rope.toRope(secondRope)
                        pos = Character.GetPos()
                        break
                if pos.y == secondPlat.y:
                    Mine(reactor)
            elif reactor.y + 1 == thirdPlat.y:
                while pos.y < thirdPlat.y:
                    Character.JumpDown()
                    time.sleep(0.4)
                    pos = Character.GetPos()
                    if pos.y == thirdPlat.y:
                        break
                while pos.y > thirdPlat.y:
                    if pos.y == ground.y:
                        Rope.toRope(firstRope)
                        Rope.toRope(secondRope)
                        Rope.toRope(thirdRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == firstPlat.y:
                        Rope.toRope(secondRope)
                        Rope.toRope(thirdRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == secondPlat.y:
                        Rope.toRope(thirdRope)
                        pos = Character.GetPos()
                        break
                if pos.y == thirdPlat.y:
                    Mine(reactor)
            elif reactor.y + 1 == fourthPlat.y:
                while pos.y < fourthPlat.y:
                    Character.JumpDown()
                    time.sleep(0.4)
                    pos = Character.GetPos()
                    if pos.y == fourthPlat.y:
                        break
                while pos.y > fourthPlat.y:
                    if pos.y == ground.y:
                        Rope.toRope(firstRope)
                        Rope.toRope(secondRope)
                        Rope.toRope(thirdRope)
                        Rope.toRope(fourthRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == firstPlat.y:
                        Rope.toRope(secondRope)
                        Rope.toRope(thirdRope)
                        Rope.toRope(fourthRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == secondPlat.y:
                        Rope.toRope(thirdRope)
                        Rope.toRope(fourthRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == thirdPlat.y:
                        Rope.toRope(fourthRope)
                        pos = Character.GetPos()
                        break
                if pos.y == fourthPlat.y:
                    Mine(reactor)
            elif reactor.y + 1 == lastPlat.y:
                while pos.y > lastPlat.y:
                    if pos.y == ground.y:
                        Rope.toRope(firstRope)
                        Rope.toRope(secondRope)
                        Rope.toRope(thirdRope)
                        Rope.toRope(fourthRope)
                        Rope.toRope(lastRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == firstPlat.y:
                        Rope.toRope(secondRope)
                        Rope.toRope(thirdRope)
                        Rope.toRope(fourthRope)
                        Rope.toRope(lastRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == secondPlat.y:
                        Rope.toRope(thirdRope)
                        Rope.toRope(fourthRope)
                        Rope.toRope(lastRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == thirdPlat.y:
                        Rope.toRope(fourthRope)
                        Rope.toRope(lastRope)
                        pos = Character.GetPos()
                        break
                    elif pos.y == fourthPlat.y:
                        Rope.toRope(lastRope)
                        pos = Character.GetPos()
                        break
                if pos.y == lastPlat.y:
                    Mine(reactor)