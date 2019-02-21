import Character, GameState, Inventory, Key, Packet, Terminal, time

# These will need updating each version
CashItemRequestOpcode = 1337
CashItemResultOpcode = 1739
BuyByMesoRequest = 85
LoadLockerDoneResult = 2
MoveLToSRequest = 15

class CashItemInfo:
    def __init__(self):
        self.liSN = 0
        self.nItemID = 0
        # None of the other vars are useful for this specific script

def GetCashItemInfo():
    return CashItemInfo()

pCashItemInfo = GetCashItemInfo()

def BuyByMeso():
    Packet.BlockSendHeader(CashItemResultOpcode)
    oPacket = Packet.COutPacket(CashItemRequestOpcode)
    oPacket.Encode1(BuyByMesoRequest)
    nMeso = Character.GetMeso()
    nPrice = 0
    if nMeso >= 25000000:
        nCommoditySN = 87000027
        nPrice = 25000000
    elif nMeso >= 13000000:
        nCommoditySN = 87000026
        nPrice = 13000000
    elif nMeso >= 5200000:
        nCommoditySN = 87000025
        nPrice = 5200000
    oPacket.Encode4(nCommoditySN)
    oPacket.Encode4(nPrice)
    Packet.SendPacket(oPacket)
    time.sleep(3)
    Packet.UnBlockSendHeader(CashItemResultOpcode)

def MoveLToS(liSN, nEmptySlotPOS):
    oPacket = Packet.COutPacket(CashItemRequestOpcode)
    oPacket.Encode1(MoveLToSRequest)
    oPacket.Encode8(liSN)
    oPacket.Encode1(5) # nTI
    oPacket.Encode2(nEmptySlotPOS)
    Packet.SendPacket(oPacket)

def CashItemResLoadLockerDone():
    iPacket = Packet.WaitForRecv(CashItemResultOpcode, 10000)
    if iPacket.GetRemaining() > 0:
        nRes = iPacket.ReadLong(1)
        if nRes == LoadLockerDoneResult:
            bItemLockerFull = iPacket.ReadLong(1)
            if bItemLockerFull == 1:
                nOverItemCount = iPacket.ReadLong(4)
            nCashItemCount = iPacket.ReadLong(2)
            if nCashItemCount >= 0:
                bFound = False
                for i in range(0, nCashItemCount):
                    CashItemInfoDecode(iPacket)
                    if pCashItemInfo.nItemID == 5040004:
                        bFound = True
                        break
                if bFound:
                    time.sleep(1)
                    MoveLToS(pCashItemInfo.liSN, nEmptySlotPOS)
                else:
                    BuyByMeso()
            time.sleep(2)
            Terminal.LeaveCashShop()
    else:
        Terminal.LeaveCashShop()

def CashItemInfoDecode(iPacket):
    pCashItemInfo.liSN = iPacket.ReadLong(8)
    dwAccountID = iPacket.ReadLong(4)
    dwCharacterID = iPacket.ReadLong(4)
    pCashItemInfo.nItemID = iPacket.ReadLong(4)
    nCommodityID = iPacket.ReadLong(4)
    nNumber = iPacket.ReadLong(2)
    sBuyCharacterID = iPacket.ReadLong(13)
    ftDateExpire = iPacket.ReadLong(8) # FileTime(4, 4)
    nPaybackRate = iPacket.ReadLong(4)
    dDiscountRate = iPacket.ReadLong(8)
    dwOrderNo = iPacket.ReadLong(4)
    dwProductNo = iPacket.ReadLong(4)
    bRefundable = iPacket.ReadLong(1)
    nSourceFlag = iPacket.ReadLong(1)
    nStorageBank = iPacket.ReadLong(1)
    # CashItemOption Decode
    liCashItemSN = iPacket.ReadLong(8)
    ftExpireDate = iPacket.ReadLong(8) # FileTime(4, 4)
    nGrade = iPacket.ReadLong(4)
    iPacket.ReadLong(4) # aOption[0]
    iPacket.ReadLong(4) # aOption[1]
    iPacket.ReadLong(4) # aOption[2]

if GameState.IsInGame():
    if Inventory.GetItemCount(5040004) == 0 and Inventory.GetEmptySlotCount(5) > 0 and Character.GetMeso() >= 5200000:
        nEmptySlotPOS = 0
        for i in range(1, Inventory.GetItemSlotCount(5)):
            pItem = Inventory.GetItem(5, i)
            if not pItem.valid:
                nEmptySlotPOS = i
                break
        Terminal.EnterCashShop()
        CashItemResLoadLockerDone()