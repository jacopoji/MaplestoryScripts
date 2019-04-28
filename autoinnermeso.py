import Terminal
import Character
import time
import GameState
import Packet
import Inventory

innerid = 70000050

# require update on header change
InnerAccept = 0x0113
InnerSend = 0x0111
InnerRecv = 0x0140



############ do not touch below #############

miracleid = 5062800

acceptPacket = Packet.COutPacket(InnerAccept)
acceptPacket.Encode4(int(time.monotonic() * 1000))
acceptPacket.Encode2(1)


def RollAbility(miracle):
    sendPacket = Packet.COutPacket(InnerSend)
    sendPacket.Encode4(int(time.monotonic() * 1000))
    sendPacket.Encode2(miracle.pos)
    sendPacket.Encode4(miracleid)
    Packet.SendPacket(sendPacket)


def FindInner(op1, op1scale, op2, op2scale, op3, op3scale):
    if (op1 == innerid and op1scale == 40) or \
            (op2 == innerid and op2scale == 40) or \
            (op3 == innerid and op3scale == 40):
        print("Found it")
        Terminal.SetProperty(Character.GetName() + str(innerid), True)
        return True
    elif (op1 == innerid and op1scale == 20) or \
            (op2 == innerid and op2scale == 20) or \
            (op3 == innerid and op3scale == 20):
        print("Found 15% inner ability")
        return True
    else:
        return False


def TierUpgrade(tier):
    if tier > Terminal.GetProperty("tier", 0):
        print("Upgrade tier")
        Terminal.SetProperty("tier", tier)
        return True
    else:
        return False


if GameState.IsInGame():
    Terminal.SetCheckBox("special/IAReset", False)

    miracle = Inventory.FindItemByID(miracleid)

    Packet.BlockRecvHeader(InnerRecv)
    while miracle.valid and not Terminal.GetProperty(Character.GetName() + str(innerid), False):
        RollAbility(miracle)
        innerResult = Packet.WaitForRecv(InnerRecv, 5000)
        if innerResult.GetRemaining() > 0:
            void = innerResult.ReadLong(4)
            op1 = innerResult.ReadLong(4)
            op1scale = innerResult.ReadLong(1)
            op1pos = innerResult.ReadLong(1)
            op1tier = innerResult.ReadLong(1)
            op2 = innerResult.ReadLong(4)
            op2scale = innerResult.ReadLong(1)
            op2pos = innerResult.ReadLong(1)
            op2tier = innerResult.ReadLong(1)
            op3 = innerResult.ReadLong(4)
            op3scale = innerResult.ReadLong(1)
            op3pos = innerResult.ReadLong(1)
            op3tier = innerResult.ReadLong(1)

            if TierUpgrade(op1tier):
                Packet.SendPacket(acceptPacket)
            elif FindInner(op1, op1scale, op2, op2scale, op3, op3scale):
                Packet.SendPacket(acceptPacket)
            else:
                time.sleep(1)
        else:
            print("Failed to roll inner ability. Check header")
            break

        miracle = Inventory.FindItemByID(miracleid)

    Packet.UnBlockRecvHeader(InnerRecv)