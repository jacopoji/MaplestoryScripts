import Character, GameState, Context, DataType, Field, Inventory, Key, Npc, Packet, Quest, Terminal, time, random
#Script is written by Retard (https://www.gamekiller.net/members/retard.942916/)

def toPortal(portal):                        # Credit to Rain for this function
    tPortal = Field.FindPortal(portal)
    if tPortal.valid:
        while tPortal.x != Character.GetPos().x:
            Character.Teleport(tPortal.x, tPortal.y)
            time.sleep(1)
            if tPortal.x == Character.GetPos().x:
                break
        Character.EnterPortal()
        time.sleep(2)

if GameState.IsInGame() and Character.GetLevel() >= 140:
    if Field.GetID() != 271041000 and not Character.HasBuff(2, 2311003):
        oPacket = Packet.COutPacket(0x02C2)
        oPacket.Encode4(0x0000000F)
        oPacket.Encode4(0x00000000)
        oPacket.Encode4(0x1027C1E8)
        Packet.SendPacket(oPacket)
        time.sleep(3)
    elif Field.GetID() == 271041000 and Character.HasBuff(2, 2311003):
        toPortal("out00")
else:
    print("Not level 140 or above")