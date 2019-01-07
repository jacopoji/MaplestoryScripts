import DataType
import Character
import Field
import Inventory
import Packet
import Terminal
import time
import GameState

#Cube ID's
#RED		5062009
#BLACK		5062010
#MASTER 	2710002
#MEISTER	2710003

#Change to cube ID you wanna use
cubeid = 5062009

#Slot of item to cube
slot = 1

#Stop at meso, droprate, threshold?
stopAtMeso = False
stopAtDropRate = False
stopAtDoubleDropRate = True
stopAtOneMesoOneDropRate = True
stopAtDoubleCritDamage = False
stopAtThreshold = True

#Change to minimum %age of same stat it should stop on
threshold = 21

#Allowed stats above threshold, change to False if need to ignore it
STRcheck = False
DEXcheck = False
INTcheck = False
LUKcheck = True
ALLcheck = True
ATTcheck = True
MATTcheck = False

#Change delay if you want (seconds)
delay = 1

#Level 160: higher or lower? 0 is lower, 1 is 160 or higher
isLvl160 = 0



####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################
####################DO NOT TOUCH BELOW##################

optSTRr = {10041:(3,4),12041:(2,3),12047:(3,4),20041:(6,7),22041:(4,5),22057:(6,7),30041:(9,10),30047:(9,9),32041:(5,6),32059:(9,10),40041:(12,13),42041:(7,8),42063:(12,13),60060:(9,9),60068:(6,6),70027:(2,3),70065:(2,2)}
optDEXr = {10042:(3,4),12042:(2,3),12048:(3,4),20042:(6,7),22042:(4,5),22058:(6,7),30042:(9,10),32042:(5,6),32060:(9,10),40042:(12,13),40047:(12,12),42042:(7,8),42064:(12,13),60061:(9,9),60069:(6,6),70073:(2,2),70093:(2,3)}
optINTr = {10043:(3,4),12043:(2,3),12049:(3,4),20043:(6,7),22043:(4,5),22059:(6,7),30043:(9,10),30048:(9,9),32043:(5,6),32061:(9,10),40043:(12,13),42043:(7,8),42065:(12,13),60062:(9,9),60070:(6,6),70063:(2,2),70106:(2,3)}
optLUKr = {10044:(3,4),12044:(2,3),12050:(3,4),20044:(6,7),22044:(4,5),22060:(6,7),30044:(9,10),32044:(5,6),32062:(9,10),40044:(12,13),40048:(12,12),42044:(7,8),42066:(12,13),60063:(9,9),60071:(6,6),70023:(2,3),70067:(2,2)}
optALLr = {20086:(3,4),22086:(2,3),22087:(3,4),22802:(2,2),30086:(6,7),32086:(4,5),32087:(6,7),32801:(6,6),40086:(9,10),42086:(5,6),42087:(9,10),60002:(20,20),60004:(5,5),60005:(10,10),60038:(3,3),60067:(6,6),60073:(3,3),70029:(2,4),70049:(2,3)}
optATTr = {20051:(6,7),22051:(6,7),30051:(9,10),32051:(9,10),40051:(12,13),42051:(12,13),60025:(12,12),60034:(4,4)}
optMATTr = {20052:(6,7),22052:(6,7),30052:(9,10),32053:(9,10),40052:(12,13),42053:(12,13),60026:(12,12),60035:(4,4)}
stat = {"STR", "DEX", "INT", "LUK", "ALL", "ATT", "MATT"}

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
	else:
		return 0

def getHighestPotential(item):
	statcalc = {'STR':0, 'DEX':0, 'INT':0, 'LUK':0, 'ALL':0, 'ATT':0, 'MATT':0}
	print(item.id)
	print("\t"+ str(item.option1) + "\n\t" + str(item.option2) + "\n\t" + str(item.option3))
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
		elif x == 'ATT' and ATTcheck == False:
			continue
		elif x == 'MATT' and MATTcheck == False:
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
	for key,value in statcalc.items():
		print(key + " => " + str(value))
	maximum = max(statcalc.values())
	print(str(maximum))
	return maximum

def containMesosObtained(item):
	return item.option1 == 40650 or item.option2 == 40650 or item.option3 == 40650
	
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

def containDoubleCritDamage(item):
	count = 0
	if item.option1 == 40056 or item.option1 == 40057:
		count += 1
	if item.option2 == 40056 or item.option2 == 40057:
		count += 1
	if item.option3 == 40056 or item.option3 == 40057:
		count += 1
	return count >= 2
	

if GameState.IsInGame():
	item = Inventory.GetItem(1, slot)
	if stopAtMeso == True and containMesosObtained(item):
		time.sleep(30)
	elif stopAtDropRate == True and containItemDropRate(item):
		time.sleep(30)
	elif stopAtDoubleDropRate == True and containDoubleDropRate(item):
		time.sleep(30)
	elif stopAtOneMesoOneDropRate == True and containOneMesoOneDropRate(item):
		time.sleep(30)
	elif stopAtDoubleCritDamage == True and containDoubleCritDamage(item):
		time.sleep(30)
	elif stopAtThreshold == True and getHighestPotential(item) >= threshold:
		time.sleep(30)
	else:
		Inventory.UseCube(cubeid, slot)
		time.sleep(delay)