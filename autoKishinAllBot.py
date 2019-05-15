import os, sys, Terminal, time, GameState, Field, Character, Context, Key,Inventory,Packet
sys.path.append('C:/Users/Jacopo/Desktop/Scripts')
import headers
#KannaForEveryBot.py
#Author: Comicals
#10/22/18 v1.2

#--- Filter BOT---
# 0 every bot
# 1 bots only in whitelist
# 2 bots except in blacklist
idFilter        = 0
idWhiteList     = [10,11,13,53,102,103,115,116,114,207,228,227,226,225,224]
idBlackList     = []


#--- Filter MAP --- 
# 0 Follow bots in any map
# 1 Follow bots only in whitelisted maps
# 2 Follow bots except in blacklisted maps
# 3 Follow bots only in current map
goldenBeachMaps = [120040100,120040100,120040300,120041000,120041100,120041200,120041300,120041400,120041500,120041600,120041700,120041800]
mapFilter       = 1
mapWhiteList    = [310070470,224000142,102030100,102030200,273040300,273020300,271030540,801030000,240090700,240040521,251010500,240030101,220070100,220070300,240010600,120041100,105020400,200010301,260010300,260020400,240010900,102040500,866000130,100020400,101030500,120040100,120040100,120040300,120041000,120041100,120041200,120041300,120041400,120041500,120041600,120041700,120041800,103030000,102030000,105010301,211040200,260020500,261020300,240010700,224000100,251010100,103041115,221030400,221030620,271030540,273020000,240010600,260020700]
mapBlackList    = []

# Maximum time spent on each bot. 
# Set True  if you like to have your kanna stay for given time period in the map
# Set False if you like to move to next bot right after finishing kishin.
timeout         = 15
wait            = False
train_to_200    = True

CP_UserHyperSkillUpRequest = 513 # 0x0201
LP_ChangeSkillRecordResult = 97 # 0x0061
CashItemRequestOpcode = headers.cash_item_header
CashItemResultOpcode = headers.cash_recv_header
BuyByMesoRequest = 85
LoadLockerDoneResult = 2
MoveLToSRequest = 15
#########################
# Dont Touch below
#########################
visited     = []
kishinPump  = 5

def Kishin(pump=3):
    safe = True
    for player in Field.GetCharacters():
        if not Terminal.IsLocalUser(player.id):
            safe = False
    if safe:
        for i in range(pump):
            Character.UseSkill(42111003)
            time.sleep(1)
       
       
def WaitForFollow(user, startTime):
    timer = 0
    time.sleep(3)
    while (Field.GetID() != user.mapid or GameState.GetChannel() != user.channel) \
        and time.time() - startTime < timeout:
        time.sleep(1)
        timer+=1
    if Terminal.IsRushing():
        #print(Field.GetID(), user.mapid, GameState.GetChannel(), user.channel)
        if Field.GetID() != user.mapid or GameState.GetChannel() != user.channel:
            print("Failed in chasing {0} at {1} Ch{2}".format(user.charname, user.mapid, user.channel), flush=True)
        Terminal.StopRush()
   
   
def CheckIdFilter(user):
    if idFilter == 0:
        return True
    elif idFilter == 1 and user.clientid in idWhiteList:
        return True
    elif idFilter == 2 and user.clientid not in idBlackList:
        return True
    else:
        return False
   
   
def CheckMapFilter(user):
    if mapFilter == 0:
        return True
    elif mapFilter == 1 and user.mapid in mapWhiteList:
        return True
    elif mapFilter == 2 and user.mapid not in mapBlackList:
        return True
    elif mapFilter == 3 and user.mapid == Field.GetID():
        return True
    else:
        return False

def CheckKanna(user):
    if avoidKanna and user.jobid in [4211, 4212]:
        return False
    else:
        return True
def attackAuto(skillid,on):
    attack_key = 0x44
    Key.Set(attack_key,1,skillid)
    Terminal.SetCheckBox("Skill Injection", False)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack", on)
    Terminal.SetComboBox("AttackKey",33)
    Terminal.SetSpinBox("autoattack_spin",100)

def SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    count = 0
    if siSkill != 32120055:
        delay = 30*math.ceil(delay*1000 * (10+attackSpeed)/480)/1000
    print("The delay for skill {} is {}, starting si".format(siSkill,delay))
    if siSkill not in [25101000,25121000]:
        sleepTime = 0.231
    else:
        sleepTime = 0.101
    while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetLineEdit("SISkillID",str(siSkill))
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",17)
        time.sleep(sleepTime)
        #Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetLineEdit("SISkillID",str(dummySkill))
        time.sleep(0.043)
        Terminal.SetCheckBox("Skill Injection",False)
        time.sleep(delay+0.05)
        #if Terminal.IsRushing():
        #    break
        if count >= 30:
            break
        if siSkill == 27111303 and not(Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219)):
            break
        count += 1
    print("Si ended due to break options")
def attackSemiNDMagic(siSkill,dummySkill,delay,on,attackSpeed = 4):
    try:
        SCLib.ThreadedFunction(SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed))
    except:
        x = 1


def bind_skill(skill):
   oPacket = Packet.COutPacket(CP_UserHyperSkillUpRequest)
   oPacket.Encode4(int(time.monotonic() * 1000))
   oPacket.Encode4(skill)
   Packet.SendPacket(oPacket)

   Packet.WaitForRecv(LP_ChangeSkillRecordResult, 10000)
   print("Received {}.".format(skill))

   Key.Set(0xDD, 1, skill)


class CashItemInfo:
    def __init__(self):
        self.liSN = 0
        self.nItemID = 0
        # None of the other vars are useful for this specific script
 
def GetCashItemInfo():
    return CashItemInfo()
pCashItemInfo = GetCashItemInfo()

def has_htr():
    return Inventory.GetItemCount(5040004) >= 1

def BuyByMeso():
    Packet.BlockSendHeader(CashItemResultOpcode)
    oPacket = Packet.COutPacket(CashItemRequestOpcode)
    oPacket.Encode1(BuyByMesoRequest)
    nMeso = Character.GetMeso()
    nPrice = 0
    if nMeso >= 13000000:
        nCommoditySN = 87000026
        nPrice = 13000000
    elif nMeso >= 5200000:
        nCommoditySN = 87000025
        nPrice = 5200000
    elif nMeso >= 25000000:
        nCommoditySN = 87000027
        nPrice = 25000000
    oPacket.Encode4(nCommoditySN)
    oPacket.Encode4(nPrice)
    Packet.SendPacket(oPacket)
    time.sleep(3)
    Packet.UnBlockSendHeader(CashItemResultOpcode)
 
def MoveLToS(liSN, nEmptySlotPOS):
    oPacket = Packet.COutPacket(CashItemRequestOpcode)
    oPacket.Encode1(MoveLToSRequest)
    print(liSN, flush=True)
    oPacket.Encode8(liSN)
    oPacket.Encode4(5040004)
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
                        Terminal.SetProperty("liSN", pCashItemInfo.liSN)
                        break
                if bFound:
                    time.sleep(1)
                    CashItemInfoDecode(iPacket)
                    print("Moving", flush=True)
                    MoveLToS(Terminal.GetProperty("liSN", -1), nEmptySlotPOS)
                else:
                    BuyByMeso()
            time.sleep(2)
            Terminal.LeaveCashShop()
    else:
        Terminal.LeaveCashShop()
        toggle_rush_by_level(True)
        Terminal.StopRush()
 
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

job = Character.GetJob() 
level = Character.GetLevel()
if GameState.IsInGame() and job in [4211, 4212]:
    if Inventory.GetItemCount(5040004) == 0 and Inventory.GetEmptySlotCount(5) > 0 and Character.GetMeso() >= 5200000:
            print("Need to buy hyper teleport rock")
            #toggle_rush_by_level(False)
            Terminal.SetCheckBox("Auto Attack",False)
            Terminal.SetCheckBox("Skill Injection",False)
            Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
            time.sleep(5)
            if Inventory.GetItemCount(5040004) == 0 and Inventory.GetEmptySlotCount(5) > 0 and Character.GetMeso() >= 5200000:
                nEmptySlotPOS = 0
                for i in range(1, Inventory.GetItemSlotCount(5)):
                    pItem = Inventory.GetItem(5, i)
                    if not pItem.valid:
                        nEmptySlotPOS = i
                        break
                if Terminal.IsRushing():
                    Terminal.StopRush()
                time.sleep(1)
                Terminal.EnterCashShop()
                CashItemResLoadLockerDone()
                time.sleep(1)
    if Character.GetLevel() < 200 and train_to_200:
        
        Terminal.SetCheckBox("Rush By Level", True)
        Terminal.SetCheckBox("Kami Vac",True)
        if job == 4200: #kanna first job
            attackAuto(42001000,True)
        elif job in KannaJobs and field_id in curbrockhideout:
            attackAuto(42001000,True)
        elif job == 4210: #kanna 2nd
            Terminal.SetCheckBox("Auto Attack",False)
            Terminal.SetSpinBox("charm_delay",100)
            Terminal.SetCheckBox("charm_fma",True)
            Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
            Terminal.SetSpinBox("SkillInjection", 100)
            Terminal.SetLineEdit("SISkillID","42001006")
            Terminal.SetCheckBox("Skill Injection",True)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",100)
        elif job == 4211:#kanna 3rd
            Terminal.SetSpinBox("charm_delay",100)
            Terminal.SetCheckBox("charm_fma",True)
            Terminal.SetCheckBox("Summon Kishin",False)
            Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
            Terminal.SetCheckBox("Auto Attack",True)
            Terminal.SetSpinBox("autoattack_spin",7500)
            Terminal.SetComboBox("AttackKey",36)
            Terminal.SetCheckBox("Skill Injection",False)
            Key.Set(0x47,1,42111003) #kishin
        elif job == 4212: #kanna 4th 
            if level >= 160 and Character.GetSkillLevel(32121052) == 1 and useHyperExploit:
                Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
                attackSemiNDMagic(32120055,32120055,0.45,True)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                bind_skill(32121052)
            else:
                Terminal.SetSpinBox("MonkeySpiritsNDdelay",100)
                Terminal.SetCheckBox("Grenade Kami",True)
                Terminal.SetCheckBox("charm_fma",False)
                Terminal.SetCheckBox("Summon Kishin",False)
                Terminal.SetCheckBox("MonkeySpiritsNDcheck",True)
                Terminal.SetCheckBox("Skill Injection",False)
            Terminal.SetCheckBox("Auto Attack",True)
            Terminal.SetSpinBox("autoattack_spin",7500)
            Terminal.SetComboBox("AttackKey",36)
            Key.Set(0x47,1,42111003) #kishin
    else:
        Terminal.SetCheckBox("Kami Vac",False)
        Terminal.SetCheckBox("Rush By Level",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        #Terminal.SetCheckBox("Mob Falldown",False)
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Auto Rune",False)
        if Inventory.GetItemCount(5040004) != 0:
            for user in Terminal.GetLocalUsers():
                user = Terminal.GetLocalUser(user.clientid) # dynamic update
                if CheckIdFilter(user) and CheckMapFilter(user) and user.channel > 0:
                    location = (user.mapid, user.channel)
                    startTime = time.time()
                    if location not in visited:
                        visited.append(location)
                        print("Kishin for {0} at {1} Ch{2}".format(user.charname, user.mapid, user.channel), flush=True)
                        Terminal.SetFollowID(user.clientid)
                        WaitForFollow(user, startTime)
                        Kishin(kishinPump)
                        while time.time() - startTime < timeout and wait:
                            time.sleep(1)