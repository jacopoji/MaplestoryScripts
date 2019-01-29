import Character, Context, os, sys, Inventory, Packet, Terminal, time, GameState
flameid = [2048745, 2048744, 2048724, 2048716]

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "\SunCat")

try:
    import SunCat, SCHotkey, SCLib
except:
    print("Couldn't find SunCat module")

def Flame():
    if (GameState.IsInGame()):
        for item in flameid:
            flame = Inventory.FindItemByID(item)
            if (flame.valid):
                #send packet for flame, which timestamp and item pos.
                oPacket = Packet.COutPacket(0x12B)
                oPacket.Encode4(int(time.monotonic()*1000))
                oPacket.Encode2(flame.pos)
                oPacket.Encode2(0x001)
                oPacket.EncodeBuffer("00")
                Packet.SendPacket(oPacket)
                SCHotkey.StopHotkeys()
                break
if SCLib.CheckVersion(20):
    SCHotkey.RegisterKeyEvent(0x7B, Flame) # CHANGE FIRST PARAMETER WITH VIRTUAL KEYCODE (F12 BY DEFAULT)
    SCHotkey.StartHotkeys()