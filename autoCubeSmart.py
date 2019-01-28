import DataType, Character, Field, Inventory, Packet, Terminal, time, GameState, functools, operator
#Ultimate Auto Cube v2.0
#10/29/18 GMS 194.4
#Author: Comicals   #Credit: Qybah
#########################################################
#Headers
revealHeader    = 0x013E
stampHeader     = 0x0132

#Cube ID's
RED     = 5062009
BLACK   = 5062010
OCCULT  = 2711000
MASTER  = 2710002
MEISTER = 2710003
#########################################################

# Auto Reveal & Stamp
autoReveal  = True
autoStamp   = True

#Change to cube ID you wanna use
cubeid      = 5062009
smartCube   = False                  # Use optimal cubes while ranking up from rare to Legendary
useOccult   = False                 # option for smart cube.

#Slot of item to cube
startSlot   = 1
endSlot     = 9

#Stat threshold
statThreshold           = 21
stopAtStatThreshold     = True
autoStat                = True      # Automatically set whichever highest stat you have
isLvl160                = 0

#For drop&meso rate
dropStatThreshold       = 15        # Work only with Single Meso or Drop rate
stopAtMesoRate          = True
stopAtDropRate          = True
stopAtDoubleMesoRate    = True
stopAtDoubleDropRate    = True
stopAtMesoAndDropRate   = True

#For your glove
critStatThreshold       = 12         # Work only with single crit ilne
stopAtCritDamage        = True
stopAtDoubleCritDamage  = True

#For Weapons
#Currenlty supports only "ATT" "MATT" "IED" "BOSS"
stopAtAtkThreshold      = True
atkThreshold            = 18
wepPotentialLines       = 3         # Set 0 if you are not going to use it
wepPotentialOptions     = [["ATT","ATT","BOSS"],["ATT","BOSS","BOSS"],["ATT","IED","BOSS"],["ATT","ATT","ATT"],["ATT","ATT","IED"],["ATT","IED","IED"]]      # Always keep end squre bracket

#Change delay if you want (seconds)
delay = 0.3

#Only if autoStat is False, adjust these
STRcheck    = False
DEXcheck    = False
INTcheck    = False
LUKcheck    = False
ALLcheck    = False
ATTcheck    = False
MATTcheck   = False
HPcheck     = True


# Change order if you want other smart cube order (Case sensitive)
epic_optimal        = [OCCULT, MASTER, RED, BLACK, MEISTER]
unique_optimal      = [MASTER, RED, BLACK, MEISTER]
legendary_optimal   = [BLACK, RED, MEISTER]
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################

optSTRr = {10041:(3,4),12041:(2,3),12047:(3,4),20041:(6,7),22041:(4,5),22057:(6,7),30041:(9,10),30047:(9,9),32041:(5,6),32059:(9,10),40041:(12,13),42041:(7,8),42063:(12,13),60060:(9,9),60068:(6,6),70027:(2,3),70065:(2,2)}
optDEXr = {10042:(3,4),12042:(2,3),12048:(3,4),20042:(6,7),22042:(4,5),22058:(6,7),30042:(9,10),32042:(5,6),32060:(9,10),40042:(12,13),40047:(12,12),42042:(7,8),42064:(12,13),60061:(9,9),60069:(6,6),70073:(2,2),70093:(2,3)}
optINTr = {10043:(3,4),12043:(2,3),12049:(3,4),20043:(6,7),22043:(4,5),22059:(6,7),30043:(9,10),30048:(9,9),32043:(5,6),32061:(9,10),40043:(12,13),42043:(7,8),42065:(12,13),60062:(9,9),60070:(6,6),70063:(2,2),70106:(2,3)}
optLUKr = {10044:(3,4),12044:(2,3),12050:(3,4),20044:(6,7),22044:(4,5),22060:(6,7),30044:(9,10),32044:(5,6),32062:(9,10),40044:(12,13),40048:(12,12),42044:(7,8),42066:(12,13),60063:(9,9),60071:(6,6),70023:(2,3),70067:(2,2)}
optHPr = {10045:(3,4),12045:(2,3),20045:(6,7),20047:(6,7),22045:(4,5),22047:(4,5),30045:(9,10),32045:(5,6),32047:(5,6),40045:(12,13),42045:(7,8),42047:(7,8),60006:(9,9),60007:(6,6),60059:(2,3),70066:(2,2)}
optALLr = {20086:(3,4),22086:(2,3),22087:(3,4),22802:(2,2),30086:(6,7),32086:(4,5),32087:(6,7),32801:(6,6),40086:(9,10),42086:(5,6),42087:(9,10),60002:(20,20),60004:(5,5),60005:(10,10),60038:(3,3),60067:(6,6),60073:(3,3),70029:(2,4),70049:(2,3)}
optATTr = {20051:(6,7),22051:(6,7),30051:(9,10),32051:(9,10),40051:(12,13),42051:(12,13),60025:(12,12),60034:(4,4)}
optMATTr = {20052:(6,7),22052:(6,7),30052:(9,10),32053:(9,10),40052:(12,13),42053:(12,13),60026:(12,12),60035:(4,4)}
ATT     = [30051, 32051, 40051, 42051, 60025, 60034]
MATT    = [30052, 32052, 40052, 42052, 60026, 60035]
IED     = [20291, 30291, 40291, 40292, 60010, 60027]
BOSS    = [30601, 30602, 40601, 40602, 40603, 42601, 42602, 42603, 60003, 60011, 60057]

stat    = {"STR", "DEX", "INT", "LUK", "ALL","HP"}
atkstat = {"ATT", "MATT"}

def FindHighestStat():
    demonA = [3122,3121,3120]
    if Character.GetJob() in demonA:
        return "HP"
    else:
        stats = {"STR":Character.GetStr(), "DEX":Character.GetDex(), "INT":Character.GetInt(), "LUK":Character.GetLuk()}
        return sorted(stats, key=stats.get, reverse=True)[0]
 
if autoStat:
    ALLcheck = True
    if FindHighestStat() == "STR":
        STRcheck, DEXcheck, INTcheck, LUKcheck,HPcheck = True, False, False, False,False
        ATTcheck    = True
        MATTcheck   = False
    elif FindHighestStat() == "HP":
        STRcheck, DEXcheck, INTcheck, LUKcheck,HPcheck = False, False, False, False,True
        ALLcheck = False
        ATTcheck    = True
        MATTcheck   = False
    elif FindHighestStat() == "DEX":
        STRcheck, DEXcheck, INTcheck, LUKcheck,HPcheck = False, True, False, False,False
        ATTcheck    = True
        MATTcheck   = False
    elif FindHighestStat() == "INT":
        STRcheck, DEXcheck, INTcheck, LUKcheck,HPcheck = False, False, True, False,False
        ATTcheck    = False
        MATTcheck   = True
    elif FindHighestStat() == "LUK":
        STRcheck, DEXcheck, INTcheck, LUKcheck,HPcheck = False, False, False, True,False
        ATTcheck    = True
        MATTcheck   = False

def getStats(stat, option):
    if stat == "STR":
        value = optSTRr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    elif stat == "DEX":
        value = optDEXr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    elif stat == "INT":
        value = optINTr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    elif stat == "LUK":
        value = optLUKr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    elif stat == "ALL":
        value = optALLr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    elif stat == "ATT":
        value = optATTr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    elif stat == "MATT":
        value = optMATTr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    elif stat == "HP":
        value = optHPr.get(option)
        if value != None:
            return value[isLvl160]
        else:
            return 0
    else:
        return 0
 
 
def getHighestPotential(item):
    statcalc = {'STR':0, 'DEX':0, 'INT':0, 'LUK':0, 'ALL':0,'HP':0}
    #print(item.id)
    #print("\t"+ str(item.option1) + "\n\t" + str(item.option2) + "\n\t" + str(item.option3))
    for x in stat:
        if x == 'STR' and STRcheck == False:
            continue
        elif x == 'DEX' and DEXcheck == False:
            continue
        elif x == 'INT' and INTcheck == False:
            continue
        elif x == 'LUK' and LUKcheck == False:
            continue
        elif x == 'ALL' and ALLcheck == False:
            continue
        elif x == 'HP' and HPcheck == False:
            continue
        else:
            perc = statcalc.get(x)
            perc += getStats(x, item.option1)
            perc += getStats(x, item.option2)
            perc += getStats(x, item.option3)
            statcalc[x] = perc
            if x == 'ALL':
                statcalc['STR'] = statcalc.get('STR') + perc
                statcalc['DEX'] = statcalc.get('DEX') + perc
                statcalc['INT'] = statcalc.get('INT') + perc
                statcalc['LUK'] = statcalc.get('LUK') + perc
    #for key,value in statcalc.items():
        #print(key + " => " + str(value))
    maximum = max(statcalc.values())
    #print(str(maximum))
    return maximum
 
def getHighestAtk(item):
    statcalc = {'ATT':0, 'MATT':0}
    for x in atkstat:
        if x == 'ATT' and ATTcheck == False:
            continue
        elif x == 'MATT' and MATTcheck == False:
            continue
        else:
            perc = statcalc.get(x)
            perc += getStats(x, item.option1)
            perc += getStats(x, item.option2)
            perc += getStats(x, item.option3)
            statcalc[x] = perc
        #for key,value in statcalc.items():
            #print(key + " => " + str(value))
        maximum = max(statcalc.values())
        #print(str(maximum))
        return maximum
 
def containsWepPotLines(item, totalLines):
    line = 0
    if totalLines == 0:
        return False
 
    WepPots = IED + BOSS
    if ATTcheck:
        WepPots = WepPots + ATT
    elif MATTcheck:
        WepPots = WepPots + MATT
 
    if item.option1 in WepPots:
        line += 1
    if item.option2 in WepPots:
        line += 1
    if item.option3 in WepPots:
        line += 1
 
    if line >= totalLines:
        return True
    else:
        return False
 
def containsWepPotOptions(item, wepPotentialOptions):
    for potentials in wepPotentialOptions:
        options     = [item.option1, item.option2, item.option3]
        index       = 0
        currLines   = 0
        totalLines  = len(potentials)
 
        for pot in potentials:
            if pot == "ATT" and bool(set(options)&set(ATT)):
                option = (set(options) & set(ATT)).pop()
                options.pop(options.index(option))
                currLines+=1
   
            elif pot == "MATT" and bool(set(options)&set(MATT)):
                option = (set(options) & set(MATT)).pop()
                options.pop(options.index(option))
                currLines+=1
   
            elif pot == "IED" and bool(set(options)&set(IED)):
                option = (set(options) & set(IED)).pop()
                options.pop(options.index(option))
                currLines+=1
   
            elif pot == "BOSS" and bool(set(options)&set(BOSS)):
                option = (set(options) & set(BOSS)).pop()
                options.pop(options.index(option))
                currLines+=1
        #print(potentials, totalLines, currLines)
        if currLines == totalLines:
            #print("Found it")
            return True
    return False
 
 
 
def containMesosObtained(item):
    return item.option1 == 40650 or item.option2 == 40650 or item.option3 == 40650

def containDoubleMesoObtained(item):
    count = 0
    if item.option1 == 40650:
        count += 1
    if item.option2 == 40650:
        count += 1
    if item.option3 == 40650:
        count += 1
    return count >= 2

def containItemDropRate(item):
    return item.option1 == 40656 or item.option2 == 40656 or item.option3 == 40656

def containDoubleDropRate(item):
    count = 0
    if item.option1 == 40656:
        count += 1
    if item.option2 == 40656:
        count += 1
    if item.option3 == 40656:
        count += 1
    return count >= 2

def containOneMesoOneDropRate(item):
    meso = 0
    drop = 0
    if item.option1 == 40650 or item.option2 == 40650 or item.option3 == 40650:
        meso += 1
    if item.option1 == 40656 or item.option2 == 40656 or item.option3 == 40656:
        drop += 1
    return (meso and drop)

def containsCritDamage(item):
    return item.option1 in [40056, 40057] or item.option2 in [40056, 40057] or item.option3 in [40056, 40057]
 
def containDoubleCritDamage(item):
    count = 0
    if item.option1 == 40056 or item.option1 == 40057:
        count += 1
    if item.option2 == 40056 or item.option2 == 40057:
        count += 1
    if item.option3 == 40056 or item.option3 == 40057:
        count += 1
    return count >= 2

def successRoll(slot, flag):
    print("Slot {0} item successfully found target potential". format(slot))
    time.sleep(delay)

def UseCube(cubeid, slot):
    if smartCube:
        if item.grade < 2 and useOccult:
            for cube in epic_optimal:
                if Inventory.FindItemByID(cube).valid:
                    Inventory.UseCube(cube, slot)
                    break
        elif item.grade < 3:
            for cube in unique_optimal:
                if Inventory.FindItemByID(cube).valid:
                    Inventory.UseCube(cube, slot)
                    break
        elif item.grade < 4:
            for cube in legendary_optimal:
                if Inventory.FindItemByID(cube).valid:
                    Inventory.UseCube(cube, slot)
                    break
        else:
            Inventory.UseCube(cubeid, slot)
    else:
        Inventory.UseCube(cubeid, slot)
 
 
def Reveal(slot):
    item = Inventory.GetItem(1, slot)
    if item.grade > 0 and item.option1 == 0 and GameState.IsInGame():
        oPacket = Packet.COutPacket(revealHeader)
        oPacket.Encode4(int(time.monotonic()*1000)) #time
        oPacket.Encode2(0x007F)
        oPacket.Encode2(item.pos)
        Packet.SendPacket(oPacket)
        time.sleep(1)
   
def Stamp(slot):
    silverStamp = 2049501
    item = Inventory.GetItem(1, slot)
    stamp = Inventory.FindItemByID(silverStamp)
 
    while item.grade > 0 and item.option1 > 0  and item.option3==0 \
    and stamp.valid and GameState.IsInGame():
        oPacket = Packet.COutPacket(stampHeader)
        oPacket.Encode4(int(time.monotonic()*1000)) #time
        oPacket.Encode2(stamp.pos)
        oPacket.Encode2(slot)
        Packet.SendPacket(oPacket)
        time.sleep(1)
 
        item    = Inventory.GetItem(1, slot)
        stamp   = Inventory.FindItemByID(silverStamp)
 
   

if GameState.IsInGame():
 
    for i in range(startSlot, endSlot+1):
        if autoReveal:
            Reveal(i)
        if autoStamp:
            Stamp(i)
        item = Inventory.GetItem(1, i)
        if item.valid and item.grade > 0 and item.option1 > 0:
            if not item.valid:
                pass
            elif stopAtStatThreshold == True and getHighestPotential(item) >= statThreshold:
                pass
            elif stopAtMesoRate == True and getHighestPotential(item) >= dropStatThreshold and containMesosObtained(item):
                pass
            elif stopAtDropRate == True and getHighestPotential(item) >= dropStatThreshold and containItemDropRate(item):
                pass
            elif stopAtDoubleMesoRate == True and containDoubleMesoObtained(item):
                pass
            elif stopAtDoubleDropRate == True and containDoubleDropRate(item):
                pass
            elif stopAtMesoAndDropRate == True and containOneMesoOneDropRate(item):
                pass
            elif stopAtCritDamage == True and containsCritDamage(item) and getHighestPotential(item) >= critStatThreshold:
                pass
            elif stopAtDoubleCritDamage == True and containDoubleCritDamage(item):
                pass
            elif stopAtAtkThreshold  == True and getHighestAtk(item) >= atkThreshold:
                pass
            elif containsWepPotOptions(item, wepPotentialOptions):
                pass
            elif containsWepPotLines(item, wepPotentialLines):
                pass
            else:
                UseCube(cubeid, i)
                time.sleep(delay)
                break