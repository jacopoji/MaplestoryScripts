curbrockhideout = [600050000,600050010,600050020]
useExploit = False
useHyperExploit = True
doEvent = False
#do Monster park how many times?
do_MP = True
do_MP_count = 2
buy_tickets = 1

#Starforce items or not
star_force = True
star_force_level = 10
safeguard = True
whitelist = []

#Zakum
DoZakumDaily=True

getSpider = False

DoBlackGate = False
doSleepyWood = False
doBeach = False
get_pensalir = False
#Key to restart pers. variables
HotKey = 0x7A

#headers that might need to be updated every game update
#headers updated for v203
import sys
sys.path.append('C:/Users/Jacopo/Desktop/Scripts')
import headers
from JobConstants import *
store_header = headers.bank_header
block_header = headers.bank_block_header
buy_ticket_header = headers.cash_item_header
recv = headers.cash_recv_header
SF_header = headers.SF_header
StarForceRecv = headers.SF_recv_header
collide_header = headers.collide_header
potential_header = headers.potential_header
potential_recv = headers.potential_recv_header
BlockBuyHeader = headers.buy_block_header
BuyItemHeader = headers.buy_header
useExpansionHeader = headers.use_expansion_header
level_skill_header = headers.level_skill_header 
dialogue_header = headers.dialogue_header
quest_header = headers.quest_header
#updated for v203
CashItemRequestOpcode = headers.cash_item_header
CashItemResultOpcode = headers.cash_recv_header
BuyByMesoRequest = 85
LoadLockerDoneResult = 2
MoveLToSRequest = 15

CP_UserHyperSkillUpRequest = 515 # 0x0203
LP_ChangeSkillRecordResult = 99 # 0x0063

#equip slot numbers
helmet_slot = -1
top_slot = -5
shoe_slot = -7
glove_slot = -8
cape_slot = -9
weapon_slot = -11
eye_slot = -3
face_slot = -2
earring_slot = -4
ring1_slot = -12
ring2_slot = -13
ring3_slot = -15
ring4_slot = -16
necklace_slot = -17
emblem_slot = -61

#accessories
aquatic_letter_eye = 1022231
condensed_power_crystal = 1012478
half_earrings = 1032022
rose_earrings = 1032017
horntail_ring = 1113149
horntail_earrings = 1032241
horntail_necklace = 1122000
chaos_horntail_necklace = 1122076
kanna_ring = 1113155
greed_pendant = 1122219
blackgate_mask = 1012535
blackgate_necklace = 1122312
blackgate_ring = 1113185

#lists
equip_slot_list = [helmet_slot,top_slot,shoe_slot,glove_slot,cape_slot,weapon_slot]
accessory_list = [aquatic_letter_eye,condensed_power_crystal,half_earrings,horntail_ring,horntail_necklace,chaos_horntail_necklace,kanna_ring,greed_pendant,blackgate_mask,blackgate_necklace,blackgate_ring]
accessory_slot_list = [eye_slot,face_slot,earring_slot,ring1_slot,ring2_slot,ring3_slot,ring4_slot,necklace_slot]
ring_list = [kanna_ring,blackgate_ring,horntail_ring]
face_list = [condensed_power_crystal,blackgate_mask]
eye_list = [aquatic_letter_eye]
earring_list = [half_earrings,rose_earrings,horntail_earrings]
necklace_list = [greed_pendant,blackgate_necklace,chaos_horntail_necklace,horntail_necklace]
blackgate_eqp = [1004549, 1012535, 1052952, 1082658, 1102840, 1113185, 1122312, 1132289, 1152191]

MP_Coin = 4310020

mobFalldownBlacklist = [105010301]#101030500
SpeedyGonzalesList = ["51121009","5011002","23100004","24001000","24101000"]
import Character,Field,Inventory,Key,Npc,Packet,Quest,Terminal,time,GameState,sys,os,Party,json,Login,datetime,math

if not any("SunCat" in s for s in sys.path):
    sys.path.append(os.getcwd() + "/SunCat")

try:
    import SunCat,SCLib, SCHotkey
except:
    print("Couldn't find SunCat module")
#if not SCLib.CheckVersion(): #This would cause crash, disable when not needed
#    print("Need to update SCLib")
SCLib.StartVars()
###persist variables
persistVariables = ["DoingSleepy","DoingBeach","MPDone","DoingMP","retry_count","zakum_retry_count","KillZakumDaily","HasSpawned","NowLockedVar","DoingZakum","DoingBG","DoingCurbrock","BuyExpansion","EvanLogout","ExploitCount","DoingJobAdv","GettingBoogie","Cannoneer","DualBlade"]
if SCLib.GetVar("MPDone") is None:
    SCLib.PersistVar("MPDone", False)
if SCLib.GetVar("DoingMP") is None:
    SCLib.PersistVar("DoingMP",False)
if SCLib.GetVar("retry_count") is None:
    SCLib.PersistVar("retry_count",0)
if SCLib.GetVar("KillZakumDaily") is None:
    SCLib.PersistVar("KillZakumDaily", DoZakumDaily)
if SCLib.GetVar("HasSpawned") is None:
    SCLib.PersistVar("HasSpawned", False)
if SCLib.GetVar("NowLockedVar") is None:
    SCLib.PersistVar("NowLockedVar", False)
if SCLib.GetVar("DoingZakum") is None:
    SCLib.PersistVar("DoingZakum",False)
if SCLib.GetVar("zakum_retry_count") is None:
    SCLib.PersistVar("zakum_retry_count",0)
if SCLib.GetVar("DoingBG") is None:
    SCLib.PersistVar("DoingBG",False)
if SCLib.GetVar("DoingCurbrock") is None:
    SCLib.PersistVar("DoingCurbrock",False)
if SCLib.GetVar("BuyExpansion") is None:
    SCLib.PersistVar("BuyExpansion",False)
if SCLib.GetVar("EvanLogout") is None:
    SCLib.PersistVar("EvanLogout",False)
if SCLib.GetVar("ExploitCount") is None:
    SCLib.PersistVar("ExploitCount",0)
if SCLib.GetVar("DoingJobAdv") is None:
    SCLib.PersistVar("DoingJobAdv",False)
if SCLib.GetVar("GettingBoogie") is None:
    SCLib.PersistVar("GettingBoogie",False)
if SCLib.GetVar("Cannoneer") is None:
    SCLib.PersistVar("Cannoneer",False)
if SCLib.GetVar("DualBlade") is None:
    SCLib.PersistVar("DualBlade",False)
if doBeach == False:
    SCLib.PersistVar("DoingBeach",False)
else:
    if SCLib.GetVar("DoingBeach") is None:
        SCLib.PersistVar("DoingBeach",False)
if doSleepyWood == False:
    SCLib.PersistVar("DoingSleepy",False)
else:
    if SCLib.GetVar("DoingSleepy") is None:
        SCLib.PersistVar("DoingSleepy",False)
HasSpawned = SCLib.GetVar("HasSpawned")
NowLockedVar = SCLib.GetVar("NowLockedVar")
KillZakumDaily = SCLib.GetVar("KillZakumDaily")
job = Character.GetJob()
level = Character.GetLevel()
field_id = Field.GetID()
pos = Character.GetPos()
DualbladeJobs = [400,430,431,432,433,434]




#DEFINE MP DUNGEON OPTIONS
mapSleep = 2.0 #Delay in between entering and exiting map
shortSleep = 0.2 #Increase if lagging
mossy_tree_forest = "Mossy Tree Forest (Lv.115-124)"
sky_forest = "Sky Forest Training Center (Lv.120-129)"
secret_pirate = "Secret Pirate Hideout (Lv.125-134)"
other_world = "Otherworld Battleground (Lv.135-144)"
dangerous_forest = "Dangerously Isolated Forest (Lv.140-149)"
forbidden_time = "Forbidden Time (Lv.145-154)"
clandestine_ruins = "Clandestine Ruins (Lv.150-159)"
leopard_portal = (493,92)
tiger_portal = (661,92)

#map ids
CheifsResidence = 211000001
TheDoorToZakum = 211042300
EntranceToZakumAlter = 211042400
ZakumsAltar = [280030100,280030101,280030102,280030103,280030104]
TheCaveOfTrials3Zakum = 211042200
blackgate_maps = [610050000,610051300, 610051400, 610051500, 610051600, 610051700, 610051800, 610051900, 610052000, 610050100, 610050200, 610050600, 610050700, 610050800, 610051200, 610050300, 610050400, 610050500, 610050900, 610051000, 610051100]
henesys = 100000000



NpcTylusWarriorInstructor = 2020008
NpcRobeiraMagicianInstructor = 2020009
NpcReneBowmanInstructor = 2020010
NpcArecThiefInstructor = 2020011
NpcPedroPirateInstructor = 2020013
EncryptedSlateOfTheSquad = 2083000

#mob ids
NormalZakum = 8800002
NormalZakumv1 = 8800000
NormalZakumv2 = 8800001    
blackgate_boss = [9480235, 9480236, 9480237, 9480238, 9480239]

padding = 20
map1 = 101050010
map2 = 910150100
try:
    SCHotkey.StartHotkeys(100)
except:
    SCHotkey.StopHotkeys()
def KillPersistVarThred():
    print("Restarting SCLib variables")
    SCLib.StopVars()
    time.sleep(1)

SCHotkey.RegisterKeyEvent(HotKey, KillPersistVarThred) #F11
if Terminal.GetCheckBox("Instant Enchantment Scroll"):
    SCLib.StopVars()
    time.sleep(1)
    print("Killing SCLib variables")
    Terminal.SetCheckBox("Instant Enchantment Scroll",False)

def AlishanRushing():
    if level > 32:
        if field_id != 749080900:
            Quest.StartQuest(55234,9330458)
        else:
            TeleportEnter(-822,-537)
            ToggleRushByLevel(True)
            print("Resume rush by level; alishan")

def DungeonTeleport():
    prefield = field_id
    ToggleKami(False)
    ToggleAttackQuest(False)
    time.sleep(1)
    Key.Press(0x08)
    time.sleep(1)
    Character.EnterPortal()
    time.sleep(1)
    newfield = Field.GetID()
    if newfield != prefield:
        print("Successfully entered portal")
        ToggleKami(True)
        ToggleAttackQuest(True)
    else:
        print("Failed to enter portal")
def ToggleRushByLevel(indicator):
    Terminal.SetCheckBox("Rush By Level",indicator)
    Terminal.SetRushByLevel(indicator)

def ToggleKami(indicator):
    if job == 11212 and level > 17 and level < 104:
        Terminal.SetCheckBox("Kami Vac",False)
    else:
        Terminal.SetCheckBox("Kami Vac",indicator)

def ToggleLoot(indicator):
    Terminal.SetCheckBox("Kami Loot",indicator)
    #Terminal.SetCheckBox("Auto Loot",indicator)
#print(Character.GetMP())

def BindSkill(skill):
   oPacket = Packet.COutPacket(CP_UserHyperSkillUpRequest)
   oPacket.Encode4(int(time.monotonic() * 1000))
   oPacket.Encode4(skill)
   Packet.SendPacket(oPacket)

   Packet.WaitForRecv(LP_ChangeSkillRecordResult, 10000)
   print("Received {}.".format(skill))

   Key.Set(0xDD, 1, skill)
def ToggleSkill():
    if job in WildHunterJobs and level > 11:
        #Rige Jaguar
        buff = 33001001
        ToggleBuffs(buff,buff,True)
        if level >= 140:
            buff = 33121054
            TimeoutBuffs(buff)
        hunter = 33111013
        TimeoutBuffs(hunter)
    elif job in MechanicJobs:
        #Mount Mechanic machine
        if level < 160:
            buff = 35001002
            ToggleBuffs(buff,buff,True)
            bots = 35121009
            TimeoutBuffs(bots)
        if job == MechanicJobs[1]:
            roboLauncher = 35101012
            ToggleBuffs(roboLauncher)
        elif job == MechanicJobs[2]:
            buff = 35111013
            TimeoutBuffs(buff)
            roboLauncher = 35101012
            ToggleBuffs(roboLauncher)
            support = 35111008
            ToggleBuffs(support)
        elif job == MechanicJobs[3]:
            buff = 35120014
            skill = 35111013
            TimeoutBuffs(buff,skill)
            if level < 160:
                roboLauncher = 35101012
                ToggleBuffs(roboLauncher)
                support = 35111008
                ToggleBuffs(support)
    elif job in FPMageJobs or job in ILMageJobs or job in BishopJobs:
        #magic guard
        buff = 2001002
        ToggleBuffs(buff)
        if job == BishopJobs[3]:
            summon_dragon = 2321003
            ToggleBuffs(summon_dragon)
    elif job in EvanJobs:
        #magic guard
        buff = 22001012
        ToggleBuffs(buff)
    elif job in DawnWarriorJobs:
        if job == DawnWarriorJobs[1]:
            buff = 11101022 #moon 
            ToggleBuffs(buff)
        elif job == DawnWarriorJobs[2]:
            #buff = 11111022 #sun
            buff = 11101022 #moon 
            ToggleBuffs(buff)
        elif job == DawnWarriorJobs[3]:
            #if level < 180:
            #    buff = 11111022 
            #else:
            #    buff = 11121005#equinox
            buff = 11111022
            ToggleBuffs(buff)
    elif job == ThunderBreakerJobs[3]:
        buff = 15121004
        ToggleBuffs(buff)
    elif job == NightWalkerJobs[3]:
        buff = 14121003
        TimeoutBuffs(buff,timer=10)
    elif job in WindArcherJobs and job != WindArcherJobs[0]:
        if job == WindArcherJobs[1]:
            buff = 13101022
            ToggleBuffs(buff)
        elif job == WindArcherJobs[2]:
            buff = 13110022
            skill = 13101022
            ToggleBuffs(buff,skill)
        elif job == WindArcherJobs[3]:
            buff = 13120003
            skill = 13101022
            ToggleBuffs(buff,skill)
    elif job in BattleMageJobs:
        if job == BattleMageJobs[0]:
            buff = 32001016 #hasty aura
            ToggleBuffs(buff)
        elif job == BattleMageJobs[1]:
            buff = 32101009 #yellow aura
            ToggleBuffs(buff)
        elif job == BattleMageJobs[2]:
            buff = 32111012 #blue aura
            ToggleBuffs(buff)
        elif job == BattleMageJobs[3]:
            buff = 32121017 #dark aura
            ToggleBuffs(buff)
    elif job == AngelicBusterJobs[3]:
        buff = 65121011
        ToggleBuffs(buff)
    elif job in DarkknightJobs and job != DarkknightJobs[0]:
        buff = 1301013
        ToggleBuffs(buff)
        if level >= 140:
            buff = 1321054
            TimeoutBuffs(buff)
    elif job in HeroJobs and job != HeroJobs[0]:
        buff = 1101013
        ToggleBuffs(buff)
    elif job in ShadeJobs and job >=2510:
        buff = 25101009
        ToggleBuffs(buff)
        if job == ShadeJobs[4] and level >= 140:
            buff2 = 25121131
            TimeoutBuffs(buff2)
    elif job == 531: #Cannon Trooper 5311005
        buff = 5311005
        TimeoutBuffs(buff)
        buff3 = 5311004
        TimeoutBuffs(buff3)
    elif job == 532: #Cannoneer
        buff = 5321004
        TimeoutBuffs(buff)
        buff2 = 5320007
        skill2= 5311005
        TimeoutBuffs(buff2,skill2)
        buff3 = 5311004
        TimeoutBuffs(buff3)
        buff4 = 5321052
        TimeoutBuffs(buff4,timer = 30)
    elif job == CorsairJobs[2]: #or job == CorsairJobs[3]:
        buff = 5211014
        TimeoutBuffs(buff)
    elif job == CorsairJobs[3]: #5220014
        buff = 5220014
        skill = 5211007
        TimeoutBuffs(buff,skill)
    elif job == BuccaneerJobs[2]: #or job == CorsairJobs[3]:
        buff = 5111007
        TimeoutBuffs(buff)
    elif job == BuccaneerJobs[3]: #5220014
        buff = 5120012
        skill = 5111007
        TimeoutBuffs(buff,skill)

        buff2 = 5121013
        TimeoutBuffs(buff2,buff2,30,True,True)
    elif job in IlliumJobs and job != IlliumJobs[0]:
        buff = 152101000
        skill = 152101003
        ToggleBuffs(buff,skill)
    elif job in HayatoJobs:
        buff = 40011289
        TimeoutBuffs(buff)
        if level >= 140:
            buff = 41121054
            TimeoutBuffs(buff)
        '''
        if Character.HasBuff(2,buff) == False:
            timeout = time.time() + 30
            if not Terminal.GetProperty("skill_timeout",False):
                Terminal.SetProperty("skill_timeout",timeout)
                print("Summer rain: Initialize")
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                Character.UseSkill(buff)
                time.sleep(short_sleep)
                Terminal.SetCheckBox("Skill Injection",True)
            elif time.time() > Terminal.GetProperty("skill_timeout",False):
                Terminal.SetProperty("skill_timeout",timeout)
                print("Summer rain: Continued")
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                Character.UseSkill(buff)
                time.sleep(short_sleep)
        '''
    elif job in KinesisJobs:
        if job == KinesisJobs[3]:
            buff = 142121004
            TimeoutBuffs(buff)
            
    elif job == ShadowerJobs[3] and level >= 140:
        buff = 1
        skill = 4221054 #coin
        TimeoutBuffs(buff,skill,timer = 40)
        if level < 180:
            buff2 = 4221052 #shadow veil
            TimeoutBuffs(buff2,timer=15)
        #buffs = Character.GetBuffs()
        #for buffa in buffs:
        #    print("Current Buff Id: {}; Remaining Time: {}".format(buff.id,buff.timeLeft))
    elif job in NightlordJobs and job != NightlordJobs[0]:
        buff = 4101011
        ToggleBuffs(buff)
        buff2 = 4111007
        TimeoutBuffs(buff2,timer = 60)
        if job == NightlordJobs[3] and level >= 140:
            buff = 4121054
            TimeoutBuffs(buff,buff,30)
    elif job in KaiserJobs:
        buff = 60001217
        ToggleBuffs(buff)
        if job == KaiserJobs[2] or job == KaiserJobs[3]:
            buff = 61111002
            ToggleBuffs(buff)
        if level >= 140:
            buff = 61121054
            TimeoutBuffs(buff)
    elif job in PhantomJobs:
        buff = 20031210
        ToggleBuffs(buff)
    elif job in BowmasterJobs:
        if job == BowmasterJobs[2]:
            buff = 3111011
            ToggleBuffs(buff)
        elif job == BowmasterJobs[3]:
            buff = 3111011
            ToggleBuffs(buff)
            buff2=3121054
            TimeoutBuffs(buff2,buff2,30,False)
    elif job in MarksmanJobs:
        if job == MarksmanJobs[2]:
            buff = 3211012
            ToggleBuffs(buff)
        elif job == MarksmanJobs[3]:
            buff = 3211012
            ToggleBuffs(buff)
            buff2 = 3221054
            TimeoutBuffs(buff2,need_sleep = True)
    elif job in DemonSlayerJobs:
        if job == DemonSlayerJobs[3]:
            buff = 31121054
            TimeoutBuffs(buff)
    elif job in DemonAvengerJobs:
        if job == DemonAvengerJobs[3]:
            if level >= 140:
                buff = 31221054
                TimeoutBuffs(buff,buff,30,False)
            if level >= 200:
                buff = 31221053
                TimeoutBuffs(buff,buff,30,False)
    elif job in MercedesJobs:
        if level >= 140:
            buff = 23121054
            TimeoutBuffs(buff)
    elif job in DualbladeJobs:
        #if job == DualbladeJobs[-1]:
            #buff = 4341002
            #TimeoutBuffs(buff)
            #buff2= 4341011
            #TimeoutBuffs(buff2,timer=50)
        if level >= 140:
            buff = 4341054
            TimeoutBuffs(buff)
    elif job in XenonJobs:
        buff = 36001005
        ToggleBuffs(buff)
        if job == XenonJobs[3]:
            buff = 36121002
            TimeoutBuffs(buff)
            buff2= 36121003
            TimeoutBuffs(buff2)
    elif job in ArkJobs[1:]:
        buff = 155101008
        ToggleBuffs(buff)
            
def ToggleBuffs(buffid,skillid = None,toggleKami = False):
    short_sleep = 0.75
    if skillid is None:
        skillid = buffid
    if Character.GetSkillLevel(buffid) > 0:
        if Character.HasBuff(2, buffid) == False:
            autoAttack = Terminal.GetCheckBox("Auto Attack")
            skillInject = Terminal.GetCheckBox("Skill Injection")
            javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
            Terminal.SetCheckBox("Auto Attack",False)
            Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
            Terminal.SetCheckBox("Skill Injection",False)
            if toggleKami:
                ToggleKami(False)
            time.sleep(short_sleep)
            Character.UseSkill(skillid)
            #time.sleep(short_sleep)
            if job in BattleMageJobs:
                time.sleep(short_sleep)
                Character.UseSkill(32001014)
                #time.sleep(short_sleep)
            if Character.HasBuff(2, buffid) == True:
                if toggleKami:
                    ToggleKami(True)
            Terminal.SetCheckBox("Auto Attack",autoAttack)
            Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
            Terminal.SetCheckBox("Skill Injection",skillInject)
    
def TimeoutBuffs(buffid,skillid = None,timer = 30,need_sleep = True,injectSkill = False):
    if need_sleep:
        short_sleep = 0.85
    else:
        short_sleep = 0.05
    if skillid is None:
        skillid = buffid
    if Character.GetSkillLevel(skillid) > 0:
        if Character.HasBuff(2,buffid) == False and len(Field.GetMobs()) > 0:
            timeout = time.time() + timer
            if not Terminal.GetProperty("skill_timeout{}".format(str(buffid)),False):
                Terminal.SetProperty("skill_timeout{}".format(str(buffid)),timeout)
                print("Skill {}: Initialize".format(buffid))
                autoAttack = Terminal.GetCheckBox("Auto Attack")
                skillInject = Terminal.GetCheckBox("Skill Injection")
                javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
                Terminal.SetCheckBox("Auto Attack",False)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                if not injectSkill:
                    if skillid == 4341002:
                        Key.Set(0x44, 1, skillid)
                        Character.UseSkill(skillid)
                        time.sleep(0.01)
                        Key.Down(0x44)
                        time.sleep(0.7)
                        Key.Up(0x44)
                    else:
                        Character.UseSkill(skillid)
                        time.sleep(0.01)
                        Character.UseSkill(skillid)
                        time.sleep(0.01)
                        Character.UseSkill(skillid)
                else:
                    Terminal.SetLineEdit("SISkillID",str(skillid))
                    Terminal.SetSpinBox("SkillInjection",300)
                    Terminal.SetCheckBox("Skill Injection",True)
                    time.sleep(short_sleep*2)
                    Terminal.SetCheckBox("Skill Injection",False)
                #time.sleep(short_sleep)
                Terminal.SetCheckBox("Auto Attack",autoAttack)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
                Terminal.SetCheckBox("Skill Injection",skillInject)
            elif time.time() > Terminal.GetProperty("skill_timeout{}".format(str(buffid)),False):
                Terminal.SetProperty("skill_timeout{}".format(str(buffid)),timeout)
                #print("Skill {}: Continued".format(buffid))
                autoAttack = Terminal.GetCheckBox("Auto Attack")
                skillInject = Terminal.GetCheckBox("Skill Injection")
                javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
                Terminal.SetCheckBox("Auto Attack",False)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
                Terminal.SetCheckBox("Skill Injection",False)
                time.sleep(short_sleep)
                if not injectSkill:
                    Character.UseSkill(skillid)
                    time.sleep(0.01)
                    Character.UseSkill(skillid)
                    time.sleep(0.01)
                    Character.UseSkill(skillid)
                else:
                    Terminal.SetLineEdit("SISkillID",str(skillid))
                    Terminal.SetSpinBox("SkillInjection",300)
                    Terminal.SetCheckBox("Skill Injection",True)
                    time.sleep(short_sleep*2)
                    Terminal.SetCheckBox("Skill Injection",False)
                if job == KinesisJobs[3]:
                    time.sleep(short_sleep*2)
                    Character.UseSkill(142121005)
                #time.sleep(short_sleep)
                Terminal.SetCheckBox("Auto Attack",autoAttack)
                Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
                Terminal.SetCheckBox("Skill Injection",skillInject)

def TeleportEnter(x,y):
    prefield = field_id
    ToggleKami(False)
    ToggleAttackQuest(False)
    time.sleep(1)
    if Character.GetPos().x != x:
        Character.Teleport(x,y)
    time.sleep(1)
    Character.EnterPortal()
    Character.EnterPortal()
    Character.EnterPortal()
    Character.EnterPortal()
    newfield = Field.GetID()
    if newfield != prefield:
        print("Successfully entered portal")
        ToggleKami(True)
        ToggleAttackQuest(True)
    else:
        print("Failed to enter portal")
    

class CashItemInfo:
    def __init__(self):
        self.liSN = 0
        self.nItemID = 0
        # None of the other vars are useful for this specific script
 
def GetCashItemInfo():
    return CashItemInfo()
pCashItemInfo = GetCashItemInfo()

def HasHtr():
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
        ToggleRushByLevel(True)
        print("Resume rush by level; htr")
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

def ToggleHtr(indicator):
    Terminal.SetCheckBox("map/maprusher/hypertelerock",indicator)

def acceptQuest(quest, startnpc, startmap, currentmap):
    ToggleKami(False)
    print("Accepting quest:{} from NPC:{}".format(quest,startnpc))
    print("Target map:{}  Current map:{}".format(startmap,currentmap))
    if currentmap != startmap:
        field_id = Field.GetID()
        if startmap == 100030300:
            print("Rushing to Farm Center")
            while field_id != 100030300:
                ToggleRushByLevel(False)
                field_id = Field.GetID()
                if field_id == 100030320: #-117 35
                    Terminal.StopRush()
                    ToggleAttackQuest(False)
                    TeleportEnter(-117,35)
                elif field_id == 100030310:
                    Terminal.StopRush()
                    ToggleAttackQuest(False)
                    TeleportEnter(1062,-25)
                else:
                    Terminal.Rush(startmap)
        elif startmap == 100030101:
            print("Rushing to living room")
            while field_id != 100030101:
                ToggleRushByLevel(False)
                Terminal.Rush(100030102)
                time.sleep(2)
                field_id = Field.GetID()
                if pos.x != -1006 and field_id == 100030102:
                    ToggleAttackQuest(False)
                    TeleportEnter(-1006,-32)
                    break
                elif pos.x == -1006:
                    ToggleAttackQuest(False)
                    TeleportEnter(-1006,-32)
                    break
        else:
            Terminal.Rush(startmap)
            time.sleep(1)
    questnpc = Field.FindNpc(startnpc)
    if questnpc.valid:
        if not close_enough(pos.x,pos.y,questnpc.x,questnpc.y):
            time.sleep(0.5)
            Character.Teleport(questnpc.x, questnpc.y)
            time.sleep(0.5)
            Quest.StartQuest(quest, startnpc)
        else:
            Quest.StartQuest(quest, startnpc)
    elif startnpc == 1013000 or startnpc == 0:
        Quest.StartQuest(quest, startnpc)
    else:
        Quest.StartQuest(quest, startnpc)
def completeQuest(quest, endnpc, endmap, grindmap, currentmap):
    print("Completing quest:{} at NPC:{} in map:{}".format(quest,endnpc,endmap))
    if Quest.CheckCompleteDemand(quest, endnpc) ==0:
        if currentmap != endmap:
            field_id = Field.GetID()
            if endmap == 100030101 or grindmap == 100030101:
                print("Rushing to living room")
                while field_id != 100030101:
                    ToggleRushByLevel(False)
                    Terminal.Rush(100030102)
                    time.sleep(2)
                    field_id = Field.GetID()
                    if pos.x != -1006 and field_id == 100030102:
                        ToggleAttackQuest(False)
                        TeleportEnter(-1006,-32)
                        break
                    elif pos.x == -1006:
                        ToggleAttackQuest(False)
                        TeleportEnter(-1006,-32)
                        break
            elif endmap == 100030300:
                print("Rushing to Farm Center")
                while field_id != 100030300:
                    ToggleRushByLevel(False)
                    field_id = Field.GetID()
                    time.sleep(2)
                    if field_id == 100030320: #-117 35
                        Terminal.StopRush()
                        ToggleAttackQuest(False)
                        TeleportEnter(-117,35)
                    elif field_id == 100030310:
                        Terminal.StopRush()
                        ToggleAttackQuest(False)
                        TeleportEnter(1062,-25)
                    elif field_id != 100030300:
                        Terminal.Rush(endmap)
            else:
                ToggleAttackQuest(False)
                Terminal.Rush(endmap)
                time.sleep(1)
        questnpc = Field.FindNpc(endnpc)
        if questnpc.valid:
            if not close_enough(pos.x,pos.y,questnpc.x,questnpc.y):
                ToggleKami(False)
                time.sleep(0.5)
                Character.Teleport(questnpc.x, questnpc.y)
                time.sleep(0.5)
                Quest.CompleteQuest(quest, endnpc)
            else:
                Quest.CompleteQuest(quest, endnpc)
        elif endnpc == 1013000:
            print("Quest npc is Mir")
            Quest.CompleteQuest(quest, endnpc)
    else:
        ToggleKami(True)
        if currentmap != grindmap:
            print("Rushing to grindmap")
            field_id = Field.GetID()
            if grindmap == 100030300:
                print("Rushing to Farm Center")
                while field_id != 100030300:
                    ToggleRushByLevel(False)
                    field_id = Field.GetID()
                    if field_id == 100030320: #-117 35
                        Terminal.StopRush()
                        ToggleAttackQuest(False)
                        TeleportEnter(-117,35)
                    elif field_id == 100030310:
                        Terminal.StopRush()
                        ToggleAttackQuest(False)
                        TeleportEnter(1062,-25)
                    else:
                        Terminal.Rush(grindmap)
            elif grindmap == 100030101:
                print("Rushing to living room")
                while field_id != 100030101:
                    ToggleRushByLevel(False)
                    Terminal.Rush(100030102)
                    time.sleep(2)
                    field_id = Field.GetID()
                    if pos.x != -1006 and field_id == 100030102:
                        ToggleAttackQuest(False)
                        TeleportEnter(-1006,-32)
                        break
                    elif pos.x == -1006:
                        ToggleAttackQuest(False)
                        TeleportEnter(-1006,-32)
                        break
            else:
                Terminal.Rush(grindmap)
                time.sleep(1)

def close_enough(x1, y1, x2, y2, distance=300):
    if (x1 - x2)**2 + (y1 - y2)**2 < distance**2:
        return True
    else:
        return False

def mapID(id):
    if type(id) is int:
        return Field.GetID() == id
    else:
        return Field.GetID() in id

def RushTo(mapid):
    HQ = 331001000
    citycentre = 331000000
    firstfloor = 331002000
    secondfloor=331002100
    ManonForest = 924000200
    GriffeyForest = 924000201
    if mapid == HQ:
        if field_id == secondfloor:
            TeleportEnter(-464,207)
        elif field_id == firstfloor:
            TeleportEnter(-480,207)
        elif field_id == citycentre:
            TeleportEnter(-250,255)
    elif mapid == firstfloor:
        if field_id == HQ:
            TeleportEnter(-93,-209)
        elif field_id == citycentre:
            TeleportEnter(1042,199)
        if field_id == secondfloor:
            TeleportEnter(-464,207)
    elif mapid == ManonForest:
        if field_id != 240020400:
            Terminal.Rush(240020400)
        elif field_id == 240020400:
            TeleportEnter(1040,452)
    elif mapid == GriffeyForest:
        if field_id != 240020100:
            Terminal.Rush(240020100)
        elif field_id == 240020100:
            TeleportEnter(-50,332)
    else:
        if not Terminal.IsRushing():
            print("Rushing to map ID: {0}".format(mapid))
            Terminal.Rush(mapid)
            time.sleep(2)
        else:
            time.sleep(1)

def Exploit1():
    ToggleRushByLevel(False)
    ToggleAttackQuest(False)
    ToggleKami(False)
    ToggleHtr(True)
    expTable = dict()
    expTable[30] = 19112
    expTable[31] = 19112
    expTable[32] = 19112
    expTable[33] = 19112
    expTable[34] = 19112
    expTable[35] = 22934
    expTable[36] = 27520
    expTable[37] = 33024
    expTable[38] = 29628
    expTable[39] = 47553
    expTable[40] = 51357
    expTable[41] = 55465
    expTable[42] = 59902
    expTable[43] = 64694
    expTable[44] = 69869
    expTable[45] = 75458
    expTable[46] = 81494
    expTable[47] = 88013
    expTable[48] = 95054
    expTable[49] = 102658
    expTable[50] = 110870
    expTable[51] = 119739
    expTable[52] = 129318
    expTable[53] = 139663
    expTable[54] = 150836
    expTable[55] = 162902
    expTable[56] = 175934
    expTable[57] = 190008
    expTable[58] = 205208
    expTable[59] = 221624
    expTable[60] = 221624
    expTable[61] = 221624
    expTable[62] = 221624
    expTable[63] = 221624
    expTable[64] = 221624
    expTable[65] = 238245
    expTable[66] = 256113
    expTable[67] = 275321
    expTable[68] = 295970
    expTable[69] = 318167
    expTable[70] = 342029
    expTable[71] = 367681
    expTable[72] = 395257
    expTable[73] = 424901
    expTable[74] = 456768
    expTable[75] = 488741
    expTable[76] = 522952
    expTable[77] = 559558
    expTable[78] = 598727
    expTable[79] = 640637
    expTable[80] = 685481
    expTable[81] = 733464
    if level < 30 or (level <= 81 and Character.GetExp() > (expTable[level] - 5309)):
        if field_id != 866000390:
            RushTo(866000390)
            time.sleep(0.5)
    else:
        if SCLib.GetVar("ExploitCount"):
            time.sleep(2)
            RushTo(224000041)
            SCLib.UpdateVar("ExploitCount",False)
        elif not SCLib.GetVar("ExploitCount"):
            Npc.ClearSelection()
            Npc.RegisterSelection("ghost")
            RushTo(224000040)
            time.sleep(2)
            SCLib.UpdateVar("ExploitCount",True)
        else:
            Npc.ClearSelection()
            Npc.RegisterSelection("ghost")
            RushTo(224000040)
            time.sleep(2)
            SCLib.UpdateVar("ExploitCount",True)
        if field_id == 224000101:
            Terminal.StopRush()

def AssignHyperStats():
    hyperStats = [(80000400,15),(80000401,15),(80000402,15),(80000403,15),(80000404,15),(80000405,15),(80000406,10),(80000409,15),(80000410,15),(80000412,15),(80000413,15),(80000414,15),(80000419,15),(80000420,15)]
    for hyperStat in hyperStats:
        if Character.GetSkillLevel(hyperStat[0]) < hyperStat[1]:
            hyperStatPacket = Packet.COutPacket(headers.level_skill_header)
            hyperStatPacket.EncodeBuffer("** ** ** ** {} FFFFFFFA".format(hex(hyperStat[0])[2:].zfill(8)))
            Packet.SendPacket(hyperStatPacket)
            print("Assigning a skill point to {}".format(hyperStat[0]))

def EventQuests():
    #StartQuest(52516, 9330195)
    #StartQuest(52517, 9330195)
    #StartQuest(52518, 9330196)
    #StartQuest(52519, 9330197)
    #StartQuest(52520, 9330198)
    quest1 = Quest.GetQuestState(52516)
    #print(quest1)
    if quest1 != 1:
        Quest.StartQuest(52516, 9330195)
    elif quest1 ==1:
        doQuest(52516,9330195)
        doQuest(52517,9330195)
        doQuest(52518,9330196)
        doQuest(52519,9330197)
        doQuest(52520,9330198)
        if Quest.GetQuestState(52520) == 1 and not Inventory.FindItemByID(3994619).valid:
            ForfeitQuest(52520)
            print("Forfeiting quest because dced")

def ForfeitQuest(questid):
    oPacket = Packet.COutPacket(quest_header)
    tohex = hex(questid)[2:].zfill(4)
    oPacket.EncodeBuffer("03 {} {} 00 00".format(tohex[2:4],tohex[0:2])) #0166 [0328CD0000]
    print("Packet to forfeit is: 03 {} {} 00 00".format(tohex[2:4],tohex[0:2]))
    Packet.SendPacket(oPacket)

def doQuest(questid,questnpc_start,questnpc_end=0):
    if questnpc_end == 0:
        questnpc_end = questnpc_start
    quest_state = Quest.GetQuestState(questid)
    if quest_state != 1:
        Quest.StartQuest(questid,questnpc_start)
    elif quest_state == 1:
        if Quest.CheckCompleteDemand(questid,questnpc_end) == 0:
            Quest.CompleteQuest(questid,questnpc_end)

def ToHex(val, nbits):
    return ((val + (1 << nbits)) % (1 << nbits))

def EnterPortal(name):
    time.sleep(0.5)
    portal = Field.FindPortal(name)
    pos = Character.GetPos()
    if pos.x != portal.x:
        print("Portal " + str(name) + " found, teleporting...")
        ToggleKami(False)
        Character.Teleport(portal.x, portal.y-20)
        time.sleep(0.5)
        print("Teleported to portal: " + str(name)+"...")
    print("Trying to enter portal...")
    count = 0
    ToggleKami(False)
    while GameState.IsInGame() and Character.GetPos().x == portal.x and count < 5:
        if Field.GetID() == 610050000:
            break

        ToggleKami(False)
        Character.EnterPortal()
        time.sleep(0.5)
        Character.EnterPortal()
        time.sleep(0.5)
        ToggleKami(True)
        count += 1

def KillMano():
    time.sleep(2)
    mob = Field.FindMob(9300815)
    if mob.valid:
        ToggleKami(True)
        ToggleAttackQuest(True)
    elif not mob.valid:
        ToggleKami(False)
        ToggleAttackQuest(False)
        TeleportEnter(68,150)

def GoToGreatSpirit():
    while Field.GetID() != map2:
        if (Field.GetID() != map1) and (Field.GetID() != map2):
            Terminal.Rush(map1)
            time.sleep(1)
        if Field.GetID() == map1:
            Character.TalkToNpc(1033211)
            time.sleep(1)

def StartQuest(quest, npc, map):
    if field_id != map:
        time.sleep(3)
        Terminal.Rush(map)
    else:
        location = Field.FindNpc(npc) #change
        if location.valid:
            if abs(Character.GetPos().x - location.x) > 400:
                ToggleKami(False)
                Character.Teleport(location.x, location.y)
        time.sleep(1)
        Quest.StartQuest(quest, npc)
        time.sleep(1)
        ToggleKami(True)

def CompleteQuest(quest, npc, map):
   if Terminal.IsRushing():
       time.sleep(1)
   elif field_id != map:
       time.sleep(3)
       Terminal.Rush(map)
   else:
       location = Field.FindNpc(npc)
       if location.valid:
           if abs(Character.GetPos().x - location.x) > 400:
               ToggleKami(False)
               Character.Teleport(location.x, location.y)
       time.sleep(1)
       Quest.CompleteQuest(quest, npc)
       time.sleep(1)
       ToggleKami(True)

def KillMobAndLoot(map):
    ToggleLoot(True)
    if Terminal.IsRushing():
        time.sleep(1)
    elif mapID != map:
        Terminal.Rush(map)
        time.sleep(3)
    else:
        Terminal.SetCheckBox("Kami Loot", True)
        Terminal.SetCheckBox("Auto Loot", True)

def BuyExpansionPacket():
    if Character.GetMeso() > 19900000:
        time.sleep(1)
        Character.TalkToNpc(2080001)
        time.sleep(1)
        print("Buying expansion via packet")
        Packet.BlockRecvHeader(BlockBuyHeader)
        time.sleep(0.5)
        BuyKey = Packet.COutPacket(BuyItemHeader)
        BuyKey.EncodeBuffer("00 000D 0023DBB3 0001 00000000 012FA660") #00F4 00 000D 0023DBB3 0001 00000000 01238100
        Packet.SendPacket(BuyKey)
        time.sleep(0.5)
        if Inventory.FindItemByID(2350003).count == 0:
            print("Buying via discount packet")
            BuyKey = Packet.COutPacket(BuyItemHeader)
            BuyKey.EncodeBuffer("00 000D 0023DBB3 0001 00000000 01238100") #00F4 00 000D 0023DBB3 0001 00000000 01238100
            Packet.SendPacket(BuyKey)
            time.sleep(0.5)
        Packet.UnBlockRecvHeader(BlockBuyHeader)
        CloseShop = Packet.COutPacket(BuyItemHeader)
        CloseShop.EncodeBuffer("[03]")
        Packet.SendPacket(CloseShop)
        time.sleep(0.5)
        ToggleRushByLevel(True)
        ToggleKami(True)

def BuySpear():
    ToggleRushByLevel(False)
    ToggleKami(False)
    if field_id != 102000000:
        RushTo(102000000)
    elif field_id == 102000000 and Character.GetPos().x !=836:
        Character.Teleport(836,1287)
    else:
        if Character.GetMeso() > 40000: #00F4 [00] 0033 0015D9C2 0001 00000000 00009C40          1021000
            time.sleep(1)
            Character.TalkToNpc(1021000)
            time.sleep(1)
            print("Buying spear via packet")
            Packet.BlockRecvHeader(BlockBuyHeader)
            time.sleep(0.5)
            BuyKey = Packet.COutPacket(BuyItemHeader)
            BuyKey.EncodeBuffer("00 0033 0015D9C2 0001 00000000 00009C40")
            Packet.SendPacket(BuyKey)
            time.sleep(0.5)
            Packet.UnBlockRecvHeader(BlockBuyHeader)
            CloseShop = Packet.COutPacket(BuyItemHeader)
            CloseShop.EncodeBuffer("[03]")
            Packet.SendPacket(CloseShop)
            time.sleep(0.5)
            ToggleRushByLevel(True)
            ToggleKami(True)

def BuyPotion(): #00F4 [00] 000D 001E8C67 05DC 00000000 00000ED8
    ToggleRushByLevel(False)
    ToggleKami(False)
    while True:
        field_id = Field.GetID()
        if field_id != 600000000:
            if not Terminal.IsRushing():
                Terminal.Rush(600000000)
            else:
                time.sleep(1)
        elif field_id == 600000000 and Character.GetPos().x !=4291:
            Character.Teleport(4291,21)
            time.sleep(2)
        else:
            if Character.GetMeso() > 38000:
                time.sleep(1)
                Character.TalkToNpc(9201060)
                time.sleep(1)
                print("Buying potion via packet")
                Packet.BlockRecvHeader(BlockBuyHeader)
                time.sleep(0.5)
                BuyKey = Packet.COutPacket(BuyItemHeader)
                if Character.GetMeso() > 5700000:
                    BuyKey.EncodeBuffer("00 000D 001E8C67 05DC 00000000 00000ED8") #00F4 00 000D 001E8C67 0001 00000000 00000ED8
                    print("Have enough money to buy 1500 potions")
                else:
                    BuyKey.EncodeBuffer("00 000D 001E8C67 {} 00000000 00000ED8".format(hex(int(Character.GetMeso()/3800))[2:].zfill(4)))
                    print("Only have enough money to buy {} potions".format(int(Character.GetMeso()/3800)))
                Packet.SendPacket(BuyKey)
                time.sleep(0.5)
                if Inventory.FindItemByID(2002023).count == 0:
                    print("Failed to buy, using discount packet")
                    BuyKey = Packet.COutPacket(BuyItemHeader)
                    if Character.GetMeso() > 5700000:
                        BuyKey.EncodeBuffer("00 000D 001E8C67 05DC 00000000 00000E40")
                    else:
                        BuyKey.EncodeBuffer("00 000D 001E8C67 {} 00000000 00000E40".format(hex(int(Character.GetMeso()/3800))[2:].zfill(4)))
                    Packet.SendPacket(BuyKey)
                    time.sleep(0.5)
                if Inventory.FindItemByID(2002023).count == 0:
                    print("Out of potions, cc")
                    Packet.UnBlockRecvHeader(BlockBuyHeader)
                    CloseShop = Packet.COutPacket(BuyItemHeader)
                    CloseShop.EncodeBuffer("[03]")
                    Packet.SendPacket(CloseShop)
                    Terminal.SetPushButton("Leave shop",True)
                    time.sleep(1)
                    Terminal.SetPushButton("Leave shop",False)
                    Terminal.ChangeChannel(0)
                    continue
                Packet.UnBlockRecvHeader(BlockBuyHeader)
                CloseShop = Packet.COutPacket(BuyItemHeader)
                CloseShop.EncodeBuffer("[03]")
                Packet.SendPacket(CloseShop)
                time.sleep(0.5)
                ToggleRushByLevel(True)
                ToggleKami(True)
                break

def BuyCrossbow():
    ToggleRushByLevel(False)
    ToggleKami(False)
    if field_id != 100000101:
        RushTo(100000101)
    else:
        if Character.GetMeso() > 30000: #00F4 [00] 000A 00164EF0 0001 00000000 00007530
            time.sleep(1)
            Character.TalkToNpc(1011000)
            time.sleep(1)
            print("Buying crossbow via packet")
            Packet.BlockRecvHeader(BlockBuyHeader)
            time.sleep(0.5)
            BuyKey = Packet.COutPacket(BuyItemHeader)
            BuyKey.EncodeBuffer("00 000A 00164EF0 0001 00000000 00007530")
            Packet.SendPacket(BuyKey)
            time.sleep(0.5)
            Packet.UnBlockRecvHeader(BlockBuyHeader)
            CloseShop = Packet.COutPacket(BuyItemHeader)
            CloseShop.EncodeBuffer("[03]")
            Packet.SendPacket(CloseShop)
            time.sleep(0.5)
            ToggleRushByLevel(True)
            ToggleKami(True)

def BuyArrow():
    ToggleRushByLevel(False)
    ToggleKami(False)
    if field_id != 100000102:
        RushTo(100000102)
    else:
        if Character.GetMeso() > 1400: #00F4 [00] 0029 001F72C8 0001 00000000 00000578
            time.sleep(1)
            Character.TalkToNpc(1011100)
            time.sleep(1)
            print("Buying crossbow arrow via packet")
            Packet.BlockRecvHeader(BlockBuyHeader)
            time.sleep(0.5)
            BuyKey = Packet.COutPacket(BuyItemHeader)
            BuyKey.EncodeBuffer("00 0029 001F72C8 0001 00000000 00000578")
            Packet.SendPacket(BuyKey)
            time.sleep(0.5)
            Packet.UnBlockRecvHeader(BlockBuyHeader)
            CloseShop = Packet.COutPacket(BuyItemHeader)
            CloseShop.EncodeBuffer("[03]")
            Packet.SendPacket(CloseShop)
            time.sleep(0.5)
            ToggleRushByLevel(True)
            ToggleKami(True)

def BuyStars():
    print("Buying stars")
    count = 0
    if Character.GetMeso() > 10000:
        ToggleRushByLevel(False)
        ToggleKami(False)
        if field_id != 100000102:
            RushTo(100000102)
        else:
            if Character.GetMeso() > 10000: #00F4 [00] 002E 001F95F0 0001 00000000 000001F4
                time.sleep(1)
                Character.TalkToNpc(1011100)
                time.sleep(1)
                print("Buying throwing stars via packet")
                Packet.BlockRecvHeader(BlockBuyHeader)
                time.sleep(0.5)
                BuyKey = Packet.COutPacket(BuyItemHeader)
                BuyKey.EncodeBuffer("00 002E 001F95F0 0001 00000000 000001F4")
                while count < 20:
                    Packet.SendPacket(BuyKey)
                    time.sleep(1)
                    count += 1
                Packet.UnBlockRecvHeader(BlockBuyHeader)
                CloseShop = Packet.COutPacket(BuyItemHeader)
                CloseShop.EncodeBuffer("[03]")
                Packet.SendPacket(CloseShop)
                time.sleep(0.5)
                ToggleRushByLevel(True)
                ToggleKami(True)

def BuyBullets():
    ToggleRushByLevel(False)
    ToggleKami(False)
    print("Buying Bullets")
    count = 0
    if Character.GetMeso() > 12000:
        if field_id != 100000102:
            RushTo(100000102)
        else:
            if Character.GetMeso() > 12000: #00F4 [00] 0035 00238D90 0001 00000000 00000258
                time.sleep(1)
                Character.TalkToNpc(1011100)
                time.sleep(1)
                print("Buying bullets via packet")
                Packet.BlockRecvHeader(BlockBuyHeader)
                time.sleep(0.5)
                BuyKey = Packet.COutPacket(BuyItemHeader)
                BuyKey.EncodeBuffer("00 0035 00238D90 0001 00000000 00000258")
                while count < 20:
                    Packet.SendPacket(BuyKey)
                    time.sleep(1)
                    count += 1
                Packet.UnBlockRecvHeader(BlockBuyHeader)
                CloseShop = Packet.COutPacket(BuyItemHeader)
                CloseShop.EncodeBuffer("[03]")
                Packet.SendPacket(CloseShop)
                time.sleep(0.5)
                ToggleRushByLevel(True)
                ToggleKami(True)

def TeleportToMobs():
    mobs = Field.GetMobs()
    if len(mobs) > 0:
        ToggleKami(False)
    else:
        ToggleKami(True)
    for mob in mobs:
        if (Character.GetPos().x - mob.x) not in range(-100,0):
            time.sleep(1)
            Character.Teleport(mob.x-20,mob.y)
        break

def CatchJaguar():
    print("Catching jaguar")
    jaguar_map = 931000500
    ToggleRushByLevel(False)
    ToggleKami(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    while True:
        jagQuest = Quest.GetQuestState(23015)
        
        # put capture onto a keys
        Key.Set(0x44, 1, 30001061)

        subweapon = Inventory.FindItemByID(1353400)
        medal = Inventory.FindItemByID(1142242)
        weapon = Inventory.FindItemByID(1462092)
        petbox = Inventory.FindItemByID(2434265)
        if subweapon.valid:
            # type, equipslot, newslot(-10 is sub weapon), count(-1 to equip)
            Inventory.SendChangeSlotPositionRequest(1, subweapon.pos, -10, -1)
        elif medal.valid:
            # type, equipslot, newslot(-49 is medal), count(-1 to equip)
            Inventory.SendChangeSlotPositionRequest(1, medal.pos, -49, -1)
        elif petbox.valid:
            Inventory.UseItem(2434265)
        elif weapon.valid:
            Character.Jump()
            # type, equipslot, newslot(-11 is weapon), count(-1 to equip)
            Inventory.SendChangeSlotPositionRequest(1, weapon.pos, -11, -1)
            
        if jagQuest != 2:
            if jagQuest == 0:
                Quest.StartQuest(23015, 2151002)
                time.sleep(1)
                
        elif jagQuest == 2:
            field_id = Field.GetID()
            if field_id != jaguar_map:
                Character.TalkToNpc(2151008)
            else:
                time.sleep(5)
                jag1 = Field.FindMob(9304000)
                jag2 = Field.FindMob(9304001)
                jag3 = Field.FindMob(9304002)
                jag4 = Field.FindMob(9304003)
                jag5 = Field.FindMob(9304004)
                
                # special jaguars
                jag6 = Field.FindMob(9304005)
                jag7 = Field.FindMob(9304006)
                jag8 = Field.FindMob(9304007)
                jag9 = Field.FindMob(9304008)
                
                jag = [jag9, jag8, jag7, jag6, jag5, jag4, jag3, jag2, jag1]
                
                # we are in the jaguar room, so catch it
                # 60 auto attacks should be enough to catch a jaguar

                pos = Character.GetPos()
                i = 0
                for i in range(0, 9):
                    if jag[i].valid:
                        catchable = jag[i]
                            
                j = 0
                while j < 120:
                    pos = Character.GetPos()
                    if pos.y != catchable.y:
                        Character.Teleport(catchable.x, catchable.y)
                        time.sleep(5)
                        
                    elif pos.y < catchable.y+ 20 and pos.y > catchable.y -20:
                        # on the same platform, so move to it and AA
                        Character.AMoveX(jag[i].x)
                        Character.BasicAttack()	
                        time.sleep(0.5)
                        Character.BasicAttack()	
                        time.sleep(0.5)
                        Character.BasicAttack()	
                        time.sleep(0.5)
                        Key.Press(0x44)
                    j = j + 1
                # after catching it, we need to rush out
                Character.Teleport(328, 28)
                time.sleep(5)
                Character.EnterPortal()
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; jaguar")
                Terminal.StopRush()
                time.sleep(10)
                break

def UseExpansionPacket():
    item = Inventory.FindItemByID(2350003)
    if item.valid:
        usePacket = Packet.COutPacket(useExpansionHeader)
        usePacket.EncodeBuffer("[{}00B3DB2300]".format(hex(item.pos).split('x')[1].zfill(2)))
        Packet.SendPacket(usePacket)
        SCLib.UpdateVar("BuyExpansion",False)

def BuyExpansion():
    if Character.GetMeso() > 20000000:
        ToggleRushByLevel(False)
        if Terminal.GetCheckBox("Kami Vac"):
            Terminal.SetCheckBox("Kami Vac",False)
        if not Terminal.IsRushing():
            if field_id != 240000002:
                RushTo(240000002)
            elif field_id == 240000002:
                Terminal.SetPushButton("Use item",False)
                Terminal.SetPushButton("Sell item",False)
                print("Buy item packet")
                BuyExpansionPacket()
                Terminal.SetPushButton("Leave shop",True)
                time.sleep(1)
                UseExpansionPacket()
                Terminal.SetPushButton("Leave shop",False)
                Terminal.SetPushButton("Use item",True)
                Terminal.SetPushButton("Sell item",True)
                if not SCLib.GetVar("BuyExpansion"):
                    ToggleRushByLevel(True)
                    ToggleKami(True)
    if not SCLib.GetVar("BuyExpansion"):
        ToggleRushByLevel(True)
        ToggleKami(True)
        print("Not buying")

def HasPensalir(printInfo = True):
    #pensalir gear
    pensalir_warrior_cape = 1102718
    pensalir_mage_cape = 1102719
    pensalir_bowman_cape = 1102720
    pensalir_thief_cape = 1102721
    pensalir_pirate_cape = 1102722

    pensalir_warrior_helmet = 1004229
    pensalir_mage_helmet = 1004230
    pensalir_bowman_helmet = 1004231
    pensalir_thief_helmet = 1004232
    pensalir_pirate_helmet = 1004233

    pensalir_warrior_gloves = 1082608
    pensalir_mage_gloves = 1082609
    pensalir_bowman_gloves = 1082610
    pensalir_thief_gloves = 1082611
    pensalir_pirate_gloves = 1082612

    pensalir_warrior_shoes = 1072967
    pensalir_mage_shoes = 1072968
    pensalir_bowman_shoes = 1072969
    pensalir_thief_shoes = 1072970
    pensalir_pirate_shoes = 1072971

    pensalir_warrior_overall = 1052799
    pensalir_mage_overall = 1052800
    pensalir_bowman_overall = 1052801
    pensalir_thief_overall = 1052802
    pensalir_pirate_overall = 1052803

    cape_list = [pensalir_mage_cape,pensalir_warrior_cape,pensalir_bowman_cape,pensalir_thief_cape,pensalir_pirate_cape]
    helmet_list = [pensalir_warrior_helmet,pensalir_mage_helmet,pensalir_bowman_helmet,pensalir_thief_helmet,pensalir_pirate_helmet]
    glove_list = [pensalir_warrior_gloves,pensalir_mage_gloves,pensalir_bowman_gloves,pensalir_thief_gloves,pensalir_pirate_gloves]
    shoe_list = [pensalir_warrior_shoes,pensalir_mage_shoes,pensalir_bowman_shoes,pensalir_thief_shoes,pensalir_pirate_shoes]
    overall_list = [pensalir_warrior_overall,pensalir_mage_overall,pensalir_bowman_overall,pensalir_thief_overall,pensalir_pirate_overall]

    #if len(accountData['done_links']) >= 25:
    #    get_pensalir = True
    #else:
    #    get_pensalir = False
    if printInfo:
        print("Has shoe : {}".format(Character.GetEquippedItemIDBySlot(shoe_slot) in shoe_list))
        print("Has cape : {}".format(Character.GetEquippedItemIDBySlot(cape_slot) in cape_list))
        print("Has helmet : {}".format(Character.GetEquippedItemIDBySlot(helmet_slot) in helmet_list))
        print("Has glove : {}".format(Character.GetEquippedItemIDBySlot(glove_slot) in glove_list))
        print("Has overall : {}".format(Character.GetEquippedItemIDBySlot(top_slot) in overall_list))
    if Character.GetEquippedItemIDBySlot(shoe_slot) in shoe_list and Character.GetEquippedItemIDBySlot(cape_slot) in cape_list and Character.GetEquippedItemIDBySlot(helmet_slot) in helmet_list and Character.GetEquippedItemIDBySlot(glove_slot) in glove_list and Character.GetEquippedItemIDBySlot(top_slot) in overall_list:
        if printInfo:
            print("Has pensalir gear now")
        return True
    else:
        if get_pensalir:
            return False
        else:
            return True
    
    utgard_fan = 1552102

def EquipItem(item_pos,equip_slot,throw_old = False):
    print("Equipping item from "+item_pos + "to" + equip_slot)
    target_equip = Inventory.GetItem(1,item_pos).id
    equip_success = False
    Terminal.SetCheckBox("Auto Equip",False)
    autoAttack = Terminal.GetCheckBox("Auto Attack")
    skillInject = Terminal.GetCheckBox("Skill Injection")
    javelin = Terminal.GetCheckBox("bot/illium/radiant_javelin_delay")
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
    Terminal.SetCheckBox("Skill Injection",False)
    Terminal.SetRadioButton("SIRadioDragon",True)
    time.sleep(5)
    Terminal.SetCheckBox("Auto Equip",False)
    while not equip_success:
        Inventory.SendChangeSlotPositionRequest(1,item_pos,equip_slot,-1)
        time.sleep(1)
        if Inventory.GetItem(1,item_pos).id != target_equip:#Equip change request success
            print("Successfully equipped item")
            equip_success = True
            Terminal.SetCheckBox("Auto Equip",True)
    
    if throw_old and equip_success:
        time.sleep(2)
        Terminal.SetCheckBox("Auto Loot",False)
        Inventory.SendChangeSlotPositionRequest(1,item_pos,0,-1) #Dropping weaker item
        time.sleep(1)
        Terminal.SetCheckBox("Auto Loot",True)
        Terminal.SetCheckBox("Auto Equip",True)
    
    Terminal.SetCheckBox("Auto Attack",autoAttack)
    Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",javelin)
    Terminal.SetCheckBox("Skill Injection",skillInject)
    Terminal.SetCheckBox("Auto Equip",True)


def EquipPensalir():
    #pensalir gear
    pensalir_warrior_cape = 1102718
    pensalir_mage_cape = 1102719
    pensalir_bowman_cape = 1102720
    pensalir_thief_cape = 1102721
    pensalir_pirate_cape = 1102722

    pensalir_warrior_helmet = 1004229
    pensalir_mage_helmet = 1004230
    pensalir_bowman_helmet = 1004231
    pensalir_thief_helmet = 1004232
    pensalir_pirate_helmet = 1004233

    pensalir_warrior_gloves = 1082608
    pensalir_mage_gloves = 1082609
    pensalir_bowman_gloves = 1082610
    pensalir_thief_gloves = 1082611
    pensalir_pirate_gloves = 1082612

    pensalir_warrior_shoes = 1072967
    pensalir_mage_shoes = 1072968
    pensalir_bowman_shoes = 1072969
    pensalir_thief_shoes = 1072970
    pensalir_pirate_shoes = 1072971

    pensalir_warrior_overall = 1052799
    pensalir_mage_overall = 1052800
    pensalir_bowman_overall = 1052801
    pensalir_thief_overall = 1052802
    pensalir_pirate_overall = 1052803

    cape_list = [pensalir_mage_cape,pensalir_warrior_cape,pensalir_bowman_cape,pensalir_thief_cape,pensalir_pirate_cape]
    helmet_list = [pensalir_warrior_helmet,pensalir_mage_helmet,pensalir_bowman_helmet,pensalir_thief_helmet,pensalir_pirate_helmet]
    glove_list = [pensalir_warrior_gloves,pensalir_mage_gloves,pensalir_bowman_gloves,pensalir_thief_gloves,pensalir_pirate_gloves]
    shoe_list = [pensalir_warrior_shoes,pensalir_mage_shoes,pensalir_bowman_shoes,pensalir_thief_shoes,pensalir_pirate_shoes]
    overall_list = [pensalir_warrior_overall,pensalir_mage_overall,pensalir_bowman_overall,pensalir_thief_overall,pensalir_pirate_overall]

    items = Inventory.GetItems(1)
    for item in items:
        if item.id in cape_list:
            if Character.GetEquippedItemIDBySlot(cape_slot) not in cape_list:
                EquipItem(item.pos,cape_slot,throw_old = True)
        elif item.id in helmet_list:
            if Character.GetEquippedItemIDBySlot(helmet_slot) not in helmet_list:
                EquipItem(item.pos,helmet_slot,throw_old = True)
        elif item.id in glove_list:
            if Character.GetEquippedItemIDBySlot(glove_slot) not in glove_list:
                EquipItem(item.pos,glove_slot,throw_old = True)
        elif item.id in shoe_list:
            if Character.GetEquippedItemIDBySlot(shoe_slot) not in shoe_list:
                EquipItem(item.pos,shoe_slot,throw_old = True)
        elif item.id in overall_list:
            if Character.GetEquippedItemIDBySlot(top_slot) not in overall_list:
                EquipItem(item.pos,top_slot,throw_old = True)

#########Job specific advancements##########
def KannaFirstJobAdv():
    SCLib.UpdateVar("DoingJobAdv",True)
    if field_id == 807040000:
        if Terminal.IsRushing():
            print("Stopping terminal rush")
            Terminal.StopRush()
        print("Doing First Job")
        Terminal.SetCheckBox("Kami Vac",False)
        ToggleRushByLevel(False)
        quest_state = Quest.GetQuestState(57400)
        quest_state1 = Quest.GetQuestState(57401)
        quest_state2 = Quest.GetQuestState(57402)
        print("Doing quests")
        if quest_state != 2:
            print("Quest 0")
            if quest_state == 0:
                Quest.StartQuest(57400, 000000)
        elif quest_state1 != 2:
            print("Quest 1")
            if quest_state1 == 0:
                Quest.StartQuest(57401, 9130082)
            elif quest_state1 == 1:
                Quest.CompleteQuest(57401, 9130082)
        elif quest_state2 != 2:
            print("Quest 3")
            if quest_state2 == 0:
                Quest.StartQuest(57402, 000000)
            elif quest_state2 ==1:
                portal = Field.FindPortal("east00")
                if portal.valid:
                    print("Found portal at x={} y={}".format(portal.x,portal.y))
                    Character.Teleport(portal.x, portal.y-10)
                    time.sleep(1)
                    Character.EnterPortal()
    elif field_id == 807040100:
        quest = Quest.GetQuestState(57402)
        if quest == 1:
            Quest.CompleteQuest(57402, 9130083)
            print("Returning control to rush by level")
            ToggleRushByLevel(True)
            ToggleKami(True)
            SCLib.UpdateVar("DoingJobAdv",False)
    else:
        time.sleep(1)
        fan = Inventory.FindItemByID(1552000)
        time.sleep(1)
        if fan.valid:
            print("Equipping fan")
            Inventory.SendChangeSlotPositionRequest(1, fan.pos, -11, -1)
            time.sleep(1)
        print("Setting up first job settings")
        Key.Set(0x44, 1, 42001000)
        time.sleep(1)
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)

def LumiFirstJobAdv():
    laniasHome = 101000100
    if field_id != laniasHome:
        Terminal.Rush(laniasHome)
        time.sleep(10)
    else:
        Quest.StartQuest(25530, 1032205)
        time.sleep(4)
        Quest.StartQuest(25531, 0)
        time.sleep(2)
        ToggleRushByLevel(True)
        ToggleKami(True)

def LumiSecondJobAdv():
    Quest.StartQuest(25510, 1032209)

def LumiThirdJobAdv():
    Quest.StartQuest(25511, 1032209)

def LumiFourthJobAdv():
    Quest.StartQuest(25512, 0)

#00F3 [1A0100000000] choose DA
#0098 663E3907 D99F894C 1BE264A4 EE5FB23A 197D999D 00000000 00000000 1574B793
#demonS 00F3 [1A0101000000] 02A0 [458EB8030000]
#demonA 00F3 [1A0100000000] 02A0 [CD5FB9030000]
def ChooseDA():
    oPacket = Packet.COutPacket(dialogue_header)
    oPacket.EncodeBuffer("[1A0100000000]")
    Packet.SendPacket(oPacket)
def ChooseDS():
    oPacket = Packet.COutPacket(dialogue_header)
    oPacket.EncodeBuffer("[1A0101000000]")
    Packet.SendPacket(oPacket)
def DemonFirstJobAdv():
    if "Demon Avenger" not in accountData['done_links']:
        ChooseDA()
        time.sleep(2)
    elif "Demon Slayer" not in accountData['done_links']:
        ChooseDS()
        time.sleep(2)

def DASecondJobAdv():
    Terminal.SetCheckBox("Kami Vac",False)
    ToggleAttackQuest(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    if Quest.GetQuestState(23210) !=2:
        if Quest.GetQuestState(23210) == 0:
            Quest.StartQuest(23210, 2151000)
        elif Quest.CheckCompleteDemand(23210, 2153006) != 0:
            #need to fight the cat
            print("Entering cat fighting map")
            if field_id != 931050100:
                if field_id != 310020100:
                    Terminal.Rush(310020100)
                else:
                    TeleportEnter(515,-14)
            else:
                Terminal.SetCheckBox("Kami Vac",True)
                ToggleAttackQuest(True)
        else:
            print("Done fighting")
            Quest.CompleteQuest(23210, 2153006)
    elif Quest.GetQuestState(23211) !=2:
        print("Second quest")
        if Quest.GetQuestState(23211) == 0:
            Quest.StartQuest(23211, 2153006)
        elif Quest.CheckCompleteDemand(23211, 2153006) == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection("Move ")
            Quest.CompleteQuest(23211, 2153006)
    elif Quest.GetQuestState(23212) !=2:
        print("third quest")
        if Quest.GetQuestState(23212) == 0:
            print("Start third quest")
            Quest.StartQuest(23212, 2151009)
        elif Quest.GetQuestState(23212) == 1:
            if field_id == 931050110:
                TeleportEnter(111,-14)
                print("Rush out of instanced map")
            elif field_id != 310010000:
                Terminal.Rush(310010000)
                print("Rush to hide")
            else:
                ToggleRushByLevel(True)
                Terminal.SetCheckBox("Kami Vac",True)
                SCLib.UpdateVar("DoingJobAdv",False)
                Quest.CompleteQuest(23212, 2151009)
                ToggleRushByLevel(True)
                Terminal.SetCheckBox("Kami Vac",True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; da second jobadv")

def DAThirdJobAdv():
    Terminal.SetCheckBox("Kami Vac",False)
    ToggleAttackQuest(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    if Quest.GetQuestState(23213) !=2:
        print("1")
        if Quest.GetQuestState(23213) == 0:
            Quest.StartQuest(23213, 2151009)
        elif Quest.GetQuestState(23213) == 1:
            if field_id != 931050110:
                if field_id != 310020100:
                    Terminal.Rush(310020100)
                else:
                    TeleportEnter(515,-14)
            else:
                Quest.CompleteQuest(23213, 2153006)
    elif (Quest.GetQuestState(23218) != 2 and job in DemonSlayerJobs) or (Quest.GetQuestState(23214) != 2 and job in DemonAvengerJobs):
        print("2")
        #if job == 3120:
        if Quest.GetQuestState(23214) == 0:
            if field_id != 931050110:
                if field_id != 310020100:
                    Terminal.Rush(310020100)
                else:
                    TeleportEnter(515,-14)
            else:
                Quest.StartQuest(23214, 2153006)
        elif Quest.GetQuestState(23214) == 1:
            if Quest.CheckCompleteDemand(23214,2153006) != 0:
                if len(Field.GetMobs()) > 0:
                    Terminal.StopRush()
                    ToggleAttackQuest(True)
                    ToggleKami(False)
                    time.sleep(5)
                elif field_id == 931050120:
                    ToggleKami(False)
                    TeleportEnter(109,-14)
                else:
                    ForfeitQuest(23214)
            else:
                time.sleep(1)
                Quest.CompleteQuest(23214, 2153006)
                ToggleAttackQuest(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingJobAdv",False)
    #else:
        elif Quest.GetQuestState(23218) == 0:
            if field_id != 931050110:
                if field_id != 310020100:
                    Terminal.Rush(310020100)
                else:
                    TeleportEnter(515,-14)
            else:
                Quest.StartQuest(23218, 2153006)
        elif Quest.GetQuestState(23218) == 1:
            if Quest.CheckCompleteDemand(23218,2153006) != 0:
                if len(Field.GetMobs()) > 0:
                    Terminal.StopRush()
                    ToggleAttackQuest(True)
                    ToggleKami(True)
                    time.sleep(5)
                elif field_id == 931050120:
                    ToggleKami(False)
                    TeleportEnter(109,-14)
            else:
                if field_id != 931050110:
                    if field_id != 310020100:
                        Terminal.Rush(310020100)
                    else:
                        TeleportEnter(515,-14)
                else:
                    time.sleep(1)
                    Quest.CompleteQuest(23218, 2153006)
                    time.sleep(1)
                    ToggleAttackQuest(True)
                    ToggleKami(True)
                    SCLib.UpdateVar("DoingJobAdv",False)
def DAFourthJobAdv():
    CalmBeforeTheStorm = 23221
    quest = Quest.GetQuestState(CalmBeforeTheStorm)
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest != 2:
        if quest == 0:
            #Terminal.SetCheckBox("Auto NPC",False)
            #time.sleep(1)
            Quest.StartQuest(CalmBeforeTheStorm,2151009)
            #time.sleep(1)
            #NoPacket = Packet.COutPacket(0x00F3)
            #NoPacket.EncodeBuffer("[0300]")
            #Terminal.SetCheckBox("Auto NPC",True)
            time.sleep(1)
            #Packet.SendPacket(NoPacket)
        elif quest == 1:
            if Quest.CheckCompleteDemand(CalmBeforeTheStorm,2151009) == 0:
                if field_id != 310010000:
                    Terminal.Rush(310010000)
                    print("Rush to hide")
                else:
                    Quest.CompleteQuest(CalmBeforeTheStorm,2151009)
                    ToggleRushByLevel(True)
                    SCLib.UpdateVar("DoingJobAdv",False)
                    time.sleep(1)
                    print("Resume rush by level; da fourth job adv")
            else:
                ToggleKami(False)
                time.sleep(5)
                TeleportToMobs()
                ToggleAttackQuest(True)

def DSFourthJobAdv():
    TrueAwakening = 23219
    TrueAwakening2 = 23215
    quest = Quest.GetQuestState(TrueAwakening)
    quest2 = Quest.GetQuestState(TrueAwakening2)
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest != 2:
        if quest == 0:
            #Terminal.SetCheckBox("Auto NPC",False)
            #time.sleep(1)
            Quest.StartQuest(TrueAwakening,2151009)
            #time.sleep(1)
            #NoPacket = Packet.COutPacket(0x00F3)
            #NoPacket.EncodeBuffer("[0300]")
            #Terminal.SetCheckBox("Auto NPC",True)
            time.sleep(1)
            #Packet.SendPacket(NoPacket)
        elif quest == 1:
            if Quest.CheckCompleteDemand(TrueAwakening,2151009) == 0:
                if field_id != 310010000:
                    Terminal.Rush(310010000)
                    print("Rush to hide")
                else:
                    Quest.CompleteQuest(TrueAwakening,2151009)
                    ToggleRushByLevel(True)
                    SCLib.UpdateVar("DoingJobAdv",False)
                    time.sleep(1)
                    print("Resume rush by level; ds fourth job adv")
            else:
                if field_id == 220050300:
                    ToggleKami(False)
                    Character.TalkToNpc(2159331)
                else:
                    ToggleKami(False)
                    time.sleep(5)
                    #TeleportToMobs()
                    ToggleAttackQuest(True)
    if quest2 != 2:
        if quest2 == 0:
            #Terminal.SetCheckBox("Auto NPC",False)
            #time.sleep(1)
            Quest.StartQuest(TrueAwakening2,2151009)
            #time.sleep(1)
            #NoPacket = Packet.COutPacket(0x00F3)
            #NoPacket.EncodeBuffer("[0300]")
            #Terminal.SetCheckBox("Auto NPC",True)
            time.sleep(1)
            #Packet.SendPacket(NoPacket)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(TrueAwakening2,2151009) == 0:
                if field_id != 310010000:
                    Terminal.Rush(310010000)
                    print("Rush to hide")
                else:
                    Quest.CompleteQuest(TrueAwakening2,2151009)
                    ToggleRushByLevel(True)
                    SCLib.UpdateVar("DoingJobAdv",False)
                    time.sleep(1)
                    print("Resume rush by level; ds fourth job adv")
            else:
                if field_id == 220050300:
                    ToggleKami(False)
                    Character.TalkToNpc(2159331)
                else:
                    ToggleKami(False)
                    time.sleep(5)
                    #TeleportToMobs()
                    ToggleAttackQuest(True)
def MercedesFirstJobAdv():
    Quest.StartQuest(29952, 1033210)

def MercedesSecondJobAdv():
    map1 = 101050010
    ToggleRushByLevel(False)
    #get an complete the first quest
    quest1 = Quest.GetQuestState(24010)
    #get an complete the second quest
    quest2 = Quest.GetQuestState(24011)
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(24010, 0)
            time.sleep(2)
        elif quest1 == 1:
            if Field.GetID() != map2:
                GoToGreatSpirit()
            else:
                Quest.CompleteQuest(24010, 1033210)
                time.sleep(1)
    elif quest2 != 2:
        if quest2 == 0:
            if Field.GetID() != map2:
                GoToGreatSpirit()
            else:
                Quest.StartQuest(24011, 1033210)
                time.sleep(1)
        elif quest2 == 1:
            if Field.GetID() != map2:
                GoToGreatSpirit()
            else:
                Quest.CompleteQuest(24011, 1033210)
                time.sleep(1)
                SCLib.UpdateVar("DoingJobAdv",False)
def HayatoFirstJobAdv():
    SCLib.UpdateVar("DoingJobAdv",True)
    if field_id == 807040000:
        if Terminal.IsRushing():
            print("Stopping terminal rush")
            Terminal.StopRush()
        print("Doing First Job")
        Terminal.SetCheckBox("Kami Vac",False)
        ToggleRushByLevel(False)
        quest_state = Quest.GetQuestState(57102)
        quest_state1 = Quest.GetQuestState(57103)
        quest_state2 = Quest.GetQuestState(57104)
        print("Doing quests")
        if quest_state != 2:
            print("Quest 0")
            if quest_state == 0:
                Quest.StartQuest(57102, 000000)
            elif quest_state == 1:
                Quest.CompleteQuest(57102, 9130031)
        elif quest_state1 != 2:
            print("Quest 1")
            if quest_state1 == 0:
                Quest.StartQuest(57103, 9130031)
            elif quest_state1 == 1:
                Quest.CompleteQuest(57103, 9130031)
        elif quest_state2 != 2:
            print("Quest 3")
            if quest_state2 == 0:
                Quest.StartQuest(57104, 9130031)
            elif quest_state2 ==1:
                portal = Field.FindPortal("east00")
                if portal.valid:
                    print("Found portal at x={} y={}".format(portal.x,portal.y))
                    Character.Teleport(portal.x, portal.y-10)
                    time.sleep(1)
                    Character.EnterPortal()
    elif field_id == 807040100:
        quest = Quest.GetQuestState(57104)
        if Terminal.IsRushing():
            Terminal.StopRush()
        if Quest.GetQuestState(16880) == 0:
            Quest.StartQuest(16880, 0)
        elif quest == 1:
            Quest.CompleteQuest(57104, 9130024)
            print("Returning control to rush by level")
            ToggleRushByLevel(True)
            ToggleKami(True)
            SCLib.UpdateVar("DoingJobAdv",False)
    else:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Hayato first job done")

def PressControl():
    if GameState.IsInGame():
        oPacket = Packet.COutPacket(dialogue_header)
        oPacket.EncodeBuffer("[35]")
        Packet.SendPacket(oPacket)

def IlliumZero():
    pet = Inventory.FindItemByID(2434265)
    SCLib.UpdateVar("DoingJobAdv",True)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)

    if level == 1 and field_id == 940202009:
        ToggleKami(False)
        Character.Teleport(-3319, 79)
        time.sleep(2)
     
        time.sleep(1)
        Character.EnterPortal()
        time.sleep(4)

    if level == 1 and field_id == 940202011:
        ToggleKami(False)
        Character.Teleport(-3400, 79)
        Character.Teleport(-3000, -500)
     
    if field_id == 940202013 or field_id == 940202014 or field_id == 940202015:
        print('1')
        mob = Field.FindMob(2400418)
        if mob.valid:
            Terminal.SetSpinBox("KamiOffsetX", -45)
            ToggleKami(True)
            Character.BasicAttack()
        else:
            time.sleep(1)
            ToggleKami(False)
            Character.Teleport(832,813)
            time.sleep(1)
            Character.EnterPortal()
            ToggleKami(True)
         
    # some questing begins here
    preparations = Quest.GetQuestState(34800)
    collecting = Quest.GetQuestState(34801)
    if preparations != 2:
        print("2")
        if preparations == 0:
            Quest.StartQuest(34800, 3001330)
            time.sleep(1)

        elif Quest.CheckCompleteDemand(34800, 3001330) != 0:
            Inventory.SendChangeSlotPositionRequest(1, 1, -11, -1)
            time.sleep(1)
            Inventory.UseItem(2000046)
            time.sleep(1)
        else:
            Quest.CompleteQuest(34800, 3001330)

 
    elif collecting != 2:
        print("3")
        if field_id == 940202012:
            TeleportEnter(13,813)
        if collecting == 0:
            Quest.StartQuest(34801, 3001330)
            time.sleep(1)
        elif Quest.CheckCompleteDemand(34801, 3001330) != 0:
            if field_id == 940202012:
                TeleportEnter(13,813)
            if field_id == 940202015:
                mob = Field.FindMob(2400418)
                if mob.valid:
                    Character.Teleport(mob.x, 10000)
                    Character.BasicAttack()
                else:
                    TeleportEnter(832,813)
            if field_id in range(940203000, 940203010) :
                mob = Field.FindMob(2400413)
                if mob.valid:
                    Terminal.SetSpinBox("KamiOffsetX", -45)
                    ToggleKami(True)
                    Character.BasicAttack()
                else:
                    ToggleKami(False)
        else:
            Quest.CompleteQuest(34801, 3001330)
            TeleportEnter(803,813)
    elif field_id == 940202012:
        print("4")
        TeleportEnter(13,813)
    elif field_id in range(940203000, 940203010):
        TeleportEnter(803,813)
        SCLib.UpdateVar("DoingJobAdv",False)
def IlliumFirstJobAdv():
    grossular = Quest.GetQuestState(34802)
    combat = Quest.GetQuestState(34803)
    social = Quest.GetQuestState(34804)
    crystalGate = Quest.GetQuestState(34805)
    specialActivity = Quest.GetQuestState(34806)
    dean = Quest.GetQuestState(34807)
    divine1 = Quest.GetQuestState(34808)
    cries = Quest.GetQuestState(34809)
    gate2 = Quest.GetQuestState(34811)
    aftergate = Quest.GetQuestState(34812)
    verdantFlora = Quest.GetQuestState(34813)
    festival2 = Quest.GetQuestState(34814)
    festival3 = Quest.GetQuestState(34815)
    festival4 = Quest.GetQuestState(34816)
    jobadv = Quest.GetQuestState(34817)
    escape = Quest.GetQuestState(34718)
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    while Terminal.IsRushing():
        if field_id == 402000521 or field_id == 402000524:
            Character.EnterPortal()
            Key.Press(0x26) #up key
            Character.EnterPortal()
            Key.Press(0x26) #up key
    if field_id == 402000526 and specialActivity != 2:
        Quest.StartQuest(34806, 0)
 
    if grossular != 2:
        if grossular == 0:
            DungeonTeleport()
            RushTo(402000526)
            Quest.StartQuest(34802, 3001332)
         
        elif Quest.CheckCompleteDemand(34802, 3001332) != 0:
            if field_id != 402000511:
                RushTo(402000511)
            time.sleep(1)
         
        else:
            RushTo(402000526)
            Quest.CompleteQuest(34802, 3001332)
 
    elif combat != 2:
        if combat == 0:
            if field_id != 402000527:
                RushTo(402000527)
                time.sleep(4)
            else:
                time.sleep(8)
                print("Pressing Control Key")
                PressControl()
                time.sleep(6)
                PressControl()
                time.sleep(6)
                print("Done Pressing")
            Quest.StartQuest(34803, 3001333)
         
        elif Quest.CheckCompleteDemand(34803, 3001333) != 0:
            RushTo(402000531)
            print("Teleport")
            if pos.x not in range(440,470):
                ToggleKami(False)
                Character.Teleport(461, 20000)
     
        else:
            print("rushing")
            RushTo(402000527)
            Quest.CompleteQuest(34803, 3001333)
         
    elif social != 2:
        if social == 0:
            RushTo(402000530)
            Quest.StartQuest(34804, 3001360)
     
        elif Quest.CheckCompleteDemand(34804, 3001360) != 0:
            Character.TalkToNpc(3001314)
            time.sleep(3)
            Character.TalkToNpc(3001315)
            time.sleep(3)
            Character.TalkToNpc(3001316)
            time.sleep(3)
            Character.TalkToNpc(3001317)
            time.sleep(3)
            Character.TalkToNpc(3001318)
         
        else:
            Quest.CompleteQuest(34804, 3001360)
 
    elif crystalGate != 2:
        if crystalGate == 0:
            RushTo(402000530)
            Quest.StartQuest(34805, 3001334)
            time.sleep(2)
         
        elif Quest.CheckCompleteDemand(34805, 3001334) != 0:
            if field_id != 402000517:
                RushTo(402000517)
         
            else:
                time.sleep(1)
                # remove these lines if you're using mob vac
                Character.Teleport(1500, 50000)
             
        else:
            RushTo(402000530)
            while Terminal.IsRushing():
                time.sleep(1)
            Quest.CompleteQuest(34805, 3001334)
            RushTo(402000528)
 
    elif specialActivity != 2:
        if specialActivity == 0:
            Quest.StartQuest(34806, 0)
     
        else:
            RushTo(402000528)
            Quest.CompleteQuest(34806, 3001331)
         
    elif dean != 2:
        if dean == 0:
            RushTo(402000532)
            Quest.StartQuest(34807, 3001337)
            time.sleep(1)
         
        elif Quest.CheckCompleteDemand(34807, 3001337) != 0:
            RushTo(402000534)
            Character.Teleport(500, 10000)
         
        else:
            RushTo(402000532)
            Quest.CompleteQuest(34807, 3001337)
                 
    elif divine1 != 2:
        if divine1 == 0:
            RushTo(402000526)
            Quest.StartQuest(34808, 3001335)
         
        elif Quest.CheckCompleteDemand(34808, 3001335) != 0:
            RushTo(402000514)
            print("Long Sleep")
            time.sleep(30)
            Quest.StartQuest(34809, 0)
            while True:
                if GameState.IsInGame():
                    ToggleKami(True)
                    print("Turning Kami on")
                    RushTo(402000513)
                    cries = Quest.GetQuestState(34809)
                    after = Quest.GetQuestState(34810)
                    if cries != 2:
                        if Quest.CheckCompleteDemand(34809, 3001338) != 0:
                            RushTo(402000513)
                            while Terminal.IsRushing():
                                time.sleep(1)
                        else:
                            Quest.CompleteQuest(34809, 3001338)
                    elif after != 2:
                        if after == 0:
                            time.sleep(1)
                            Npc.ClearSelection()
                            time.sleep(1)
                            Npc.RegisterSelection("Choice 1")
                            time.sleep(1)
                            Quest.StartQuest(34810, 3001338)
                    else:
                        break
                else:
                    break
             
        else:
            RushTo(402000526)
            ToggleKami(False)
            Quest.CompleteQuest(34808, 3001335)
            RushTo(402000530)
 
    elif gate2 != 2:
        if gate2 == 0:
            RushTo(402000530)
         
        elif Quest.CheckCompleteDemand(34811, 3001334) != 0:
            ToggleKami(False)
            Character.Teleport(0, 10000)
            RushTo(402000535)
         
        else:
            RushTo(402000530)
            Quest.CompleteQuest(34811, 3001334)
         
    elif aftergate != 2:
        if aftergate == 0:
            RushTo(402000530)
            Quest.StartQuest(34812, 0)
            time.sleep(5)
     
        elif Quest.CheckCompleteDemand(34812, 3001336) != 0:
            RushTo(402000501)
         
        else:
            Quest.CompleteQuest(34812, 3001336)
         
    elif verdantFlora != 2:
        if verdantFlora == 0:
            RushTo(402000501)
            print("Might get stuck here")
            #E6 00 06 01 00 00 00 00
            Npc.ClearSelection()
            time.sleep(2)
            Npc.RegisterSelection("Of course!")
            time.sleep(1)
            Quest.StartQuest(34813, 3001336)
            time.sleep(1)
            Npc.ClearSelection()
            time.sleep(2)
            Npc.RegisterSelection("Of ")
            time.sleep(2)
         
        elif Quest.CheckCompleteDemand(34813, 3001336) != 0:
            RushTo(402000502)
            ToggleKami(False)
            Character.Teleport(1309, 10000)
         
        else:
            RushTo(402000501)
            while Terminal.IsRushing():
                time.sleep(1)
            Quest.CompleteQuest(34813, 3001336)
            time.sleep(5)
            RushTo(402000529)
         
    elif festival2 != 2:
        if festival2 == 0:
            RushTo(402000529)
            Quest.StartQuest(34814, 3001339)
            ToggleKami(False)
            time.sleep(3)
         
        elif Quest.CheckCompleteDemand(34814, 3001339) != 0:
            RushTo(402000507)
            time.sleep(1)
         
        else:
            RushTo(402000529)
            Quest.CompleteQuest(34814, 3001339)
            time.sleep(1)
         
    elif festival3 != 2:
        if festival3 == 0:
            RushTo(402000529)
            Quest.StartQuest(34815, 3001339)
            time.sleep(3)
     
        elif Quest.CheckCompleteDemand(34815, 3001339) != 0:
            RushTo(402000509)
            time.sleep(1)
         
        else:
            RushTo(402000529)
            Quest.CompleteQuest(34815, 3001339)
            time.sleep(1)
         
    elif festival4 != 2:
        if festival4 == 0:
            RushTo(402000529)
            Quest.StartQuest(34816, 3001339)
            time.sleep(2)
         
        elif Quest.CheckCompleteDemand(34816, 3001339) != 0:
            RushTo(402000504)
            time.sleep(1)
         
        else:
            RushTo(402000529)
            Quest.CompleteQuest(34816, 3001339)
            time.sleep(1)
                 
    elif jobadv != 2:
        if jobadv == 0:
            RushTo(402000529)
            Quest.StartQuest(34817, 3001339)
            time.sleep(2)
     
        elif Quest.CheckCompleteDemand(34817, 3001339) != 0:
            if field_id == 402000529:
                RushTo(402000504)
             
            elif field_id in range(940202100, 940202199):
                mob = Field.FindMob(2400420)
                if mob.valid:
                    time.sleep(20)
                    ToggleKami(False)
                    Character.Teleport(-500, 20000)
                    time.sleep(1)
                else:
                    ToggleKami(False)
                    Character.Teleport(1, -683)
                    time.sleep(2)
                    Character.EnterPortal()
                    Character.EnterPortal()
                    time.sleep(3)
         
            elif field_id in range(940202200, 940202299):
                Character.JumpDown()
                time.sleep(2)
                Character.JumpDown()
                time.sleep(10)
                Character.JumpDown()
                mob = Field.FindMob(2400420)
                mob2 = Field.FindMob(2400421)
                if mob.valid or mob2.valid:
                    time.sleep(1)
                else:
                    ToggleKami(False)
                    Character.Teleport(-583, -31)
                    time.sleep(2)
                    Character.EnterPortal()
                    Character.EnterPortal()
            elif field_id in range(940202300, 940202399):
                ToggleKami(False)
                if pos.x != 35:
                    Character.Teleport(35, -2000)
                Character.JumpDown()
                time.sleep(1)
                mob = Field.FindMob(2400421)
                if mob.valid:
                    time.sleep(1)
                else:
                    ToggleKami(False)
                    Character.Teleport(1,-638)
                    time.sleep(1)
                    Character.EnterPortal()
            elif field_id in range(940202400, 940202499):
                ToggleKami(False)
                Character.Teleport(-1, -638)
                time.sleep(1)
                Character.EnterPortal()
        else:
            time.sleep(1)
    elif escape != 2:
        RushTo(940202032)
        ToggleKami(False)
        Character.Teleport(915, 10000)
        Quest.CompleteQuest(34718, 3001344)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleRushByLevel(True)
        print("Resume rush by level; illium first")
        time.sleep(10)

def IlliumSecondJobAdv():
    escape = Quest.GetQuestState(34818)
    lookback = Quest.GetQuestState(34820)
    SCLib.UpdateVar("DoingJobAdv",True)
    ToggleRushByLevel(False)
    if escape != 2:
        print("Escape")
        RushTo(940202032)
        ToggleKami(False)
        Character.Teleport(332, 10000)
        Quest.CompleteQuest(34818, 3001344)
        ToggleKami(True)
        time.sleep(10)
     
    elif field_id == 940202032 and escape == 2:
        print("2")
        ToggleKami(False)
        Quest.StartQuest(34860, 0)
        time.sleep(1)
        Key.Press(0x08)
        time.sleep(1)
        Character.EnterPortal()

    elif field_id in range(940202500, 940202599):
        print("3")
        ToggleKami(False)
        Key.Press(0x08)
        time.sleep(1)
        Character.EnterPortal()

    elif field_id in range(940202600, 940202699): 
        ToggleKami(False)
        print("4")
        Key.Press(0x08)
        time.sleep(1)
        Character.EnterPortal()
         
    elif field_id in range(940202700, 940202799):
        print("5")
        ToggleKami(False)
        Key.Press(0x08)
        time.sleep(1)
        Character.EnterPortal()
     
    elif field_id == 940202036:
        print("6")
        ToggleKami(False)
        Character.Teleport(-739, 813)
 
    elif field_id == 940202037:
        ToggleKami(False)
        time.sleep(4)
        Character.Teleport(803,813)
        time.sleep(1)
        Character.EnterPortal()
     
    elif lookback != 2:
        if lookback == 0:
            RushTo(940202040)
            Quest.StartQuest(34820, 3001343)
         
        elif Quest.CheckCompleteDemand(34820, 3000002) == 0:
            RushTo(400000000)
            Quest.CompleteQuest(34820, 3000002)
        elif Quest.GetQuestState(34820) == 2:
            ToggleRushByLevel(True)
            print("Completed all Illium Quests and now returning control to rush by level")
            SCLib.UpdateVar("DoingJobAdv",False)
            time.sleep(1)
            
def IlliumThirdJobAdv():
    GirlWhoSaved = 34831
    HelpingShuang = 34832
    SanctuaryDiscovered1= 34834
    Board1 = 2838
    quest1 = Quest.GetQuestState(34831)
    quest2 = Quest.GetQuestState(34832)
    quest2_1 = Quest.GetQuestState(2838)
    quest3 = Quest.GetQuestState(34834)
    RelicExcavationCamp = 102040200
    ExcavationCompletionArea = 102040100
    InitialExcavationArea = 102040000
    shuang = 9040000
    board1npc = 1022111
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest1 != 2:
        if quest1 == 0:
            acceptQuest(GirlWhoSaved,0,0,0)
        elif quest1 == 1:
            completeQuest(GirlWhoSaved,shuang,RelicExcavationCamp,RelicExcavationCamp,field_id)
    elif quest2 != 2:
        if quest2 == 0:
            acceptQuest(HelpingShuang,shuang,RelicExcavationCamp,field_id)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(HelpingShuang,shuang) != 0:
                if quest2_1 !=2:
                    if quest2_1 == 0:
                        acceptQuest(Board1,board1npc,ExcavationCompletionArea,field_id)
                    elif quest2_1 == 1:
                        if Quest.CheckCompleteDemand(Board1,board1npc) != 0:
                            RushTo(InitialExcavationArea)
                            time.sleep(30)
                            RushTo(ExcavationCompletionArea)
                            time.sleep(30)
                        else:
                            completeQuest(Board1,board1npc,ExcavationCompletionArea,ExcavationCompletionArea,field_id)
            else:
                completeQuest(HelpingShuang,shuang,RelicExcavationCamp,RelicExcavationCamp,field_id)
    elif quest3 != 2:
        if quest3 == 0:
            acceptQuest(SanctuaryDiscovered1,shuang,RelicExcavationCamp,field_id)
            ToggleRushByLevel(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            print("Resume rush by level; illium third job adv")

def IlliumFourthJobAdv():
    DiscoveryoftheSanctuary2 = 34842
    quest1 = Quest.GetQuestState(34842)
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest1 != 2:
        if quest1 == 0:
            acceptQuest(DiscoveryoftheSanctuary2,0,0,0)
            SCLib.UpdateVar("DoingJobAdv",False)
def CadenaFirstJobAdv():
    quest1 = Quest.GetQuestState(34600)
    quest2 = Quest.GetQuestState(34601)
    quest3 = Quest.GetQuestState(34602)
    quest4 = Quest.GetQuestState(34603)
    quest5 = Quest.GetQuestState(34656)
    quest6 = Quest.GetQuestState(34604)
    quest7 = Quest.GetQuestState(34605)
    quest8 = Quest.GetQuestState(34606)
    quest9 = Quest.GetQuestState(34607)
    quest10 = Quest.GetQuestState(34608)
    quest11 = Quest.GetQuestState(34609)
    quest12 = Quest.GetQuestState(34610)
    quest13 = Quest.GetQuestState(34611)
    quest14 = Quest.GetQuestState(34612)
    quest15 = Quest.GetQuestState(34613)
    quest16 = Quest.GetQuestState(34614)
    quest17 = Quest.GetQuestState(34615)
    quest18 = Quest.GetQuestState(34616)
    quest19 = Quest.GetQuestState(34617)
    quest20 = Quest.GetQuestState(34618)
    quest21 = Quest.GetQuestState(34619)
    quest22 = Quest.GetQuestState(34620)
    quest23 = Quest.GetQuestState(34621)
    quest24 = Quest.GetQuestState(34622)
    quest25 = Quest.GetQuestState(34623)
    quest26 = Quest.GetQuestState(34624)
    quest27 = Quest.GetQuestState(34625)
    ToggleRushByLevel(False)
    pet = Inventory.FindItemByID(2434265)
    SCLib.UpdateVar("DoingJobAdv",True)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)
    if quest1 != 2:
        Terminal.SetCheckBox("Auto SP",False)
        if quest1 == 0:
            Quest.StartQuest(34600, 0)
            time.sleep(10)
        elif field_id == 940200500:
            EnterPortal("west00")
        elif field_id == 940200501:
            EnterPortal("up00")
    if quest2 != 2:
        if quest2 == 0:
            if field_id == 940200502:
                Quest.StartQuest(34601, 3001221)
            elif field_id == 940200600 or 940200601:
                Key.Press(0x11)
                time.sleep(1)
        elif quest2 == 1:
            Quest.CompleteQuest(34601, 3001221)
    elif quest3 != 2:
        if field_id == 402000002:
            if quest3 == 0:
                Quest.StartQuest(34602, 3001202)
                time.sleep(10)
            elif quest3 == 1:
                Npc.ClearSelection()
                Npc.RegisterSelection("remain")
                Npc.RegisterSelection("Never")
                Quest.CompleteQuest(34602, 3001202)
                time.sleep(8)
        else:
            Terminal.Rush(402000002)
    elif quest4 != 2:
        if field_id == 402000002:
            if quest4 == 0:
                Quest.StartQuest(34603, 3001202)
            elif quest4 == 1:
                if Quest.CheckCompleteDemand(34603, 3001202) == 0:
                    Quest.CompleteQuest(34603, 3001202)
                else:
                    Inventory.UseItem(2437264)
        else:
            Terminal.Rush(402000002)
    elif quest5 != 2:
        if field_id != 402000001:
            Terminal.Rush(402000001)
        else:
            if quest5 == 0:
                Quest.StartQuest(34656, 3001200)
    elif quest6 != 2:
        if field_id != 402000001:
            Terminal.Rush(402000001)
        else:
            if quest6 == 0:
                Quest.StartQuest(34604, 3001200)
            elif quest6 == 1:
                pos = Character.GetPos()
                if pos.x != -308:
                    ToggleKami(False)
                    Character.Teleport(-308, 304)
                else:
                    Quest.CompleteQuest(34604, 3001210)
                    ToggleKami(True)
    elif quest7 != 2:
        if quest7 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34605, 3001210)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(34605, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34605, 3001210)
            else:
                if field_id != 402000110:
                    Terminal.Rush(402000110)
    elif quest8 != 2:
        if quest8 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34606, 3001210)
        elif quest8 == 1:
            if Quest.CheckCompleteDemand(34606, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34606, 3001210)
            else:
                if field_id != 402000111:
                    Terminal.Rush(402000111)
    elif quest9 != 2:
        if quest9 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34607, 3001210)
        elif quest9 == 1:
            if Quest.CheckCompleteDemand(34607, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34607, 3001210)
            elif field_id != 402000112:
                Terminal.Rush(402000112)
    elif quest10 != 2:
        if quest10 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                pos = Character.GetPos()
                if pos.x != -308:
                    ToggleKami(False)
                    Character.Teleport(-308, 304)
                else:
                    Quest.StartQuest(34608, 3001210)
                    ToggleKami(True)
        if quest10 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.CompleteQuest(34608, 3001203)
    elif quest11 != 2:
        if quest11 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34609, 3001210)
        elif quest11 == 1:
            if Quest.CheckCompleteDemand(34609, 3001210) == 0:
                if field_id != 402000001:
                    Terminal.Rush(402000001)
                else:
                    Quest.CompleteQuest(34609, 3001210)
            else:
                if field_id != 402000220:
                    Terminal.Rush(402000220)
    elif quest12 != 2:
        if quest12 == 0:
            if field_id != 402000200:
                Terminal.Rush(402000200)
            else:
                Quest.StartQuest(34610, 3001218)
        elif quest12 == 1:
            Quest.CompleteQuest(34610, 3001218)
            Terminal.Sleep(3)
    elif quest13 != 2:
        print("13")
        print(quest13)
        if quest13 == 0:
            print("quest unstarted")
            pos = Character.GetPos()
            if pos.x != -506:
                ToggleKami(False)
                Character.Teleport(-506, 45)
                time.sleep(2)
            else:
                Quest.StartQuest(34611, 3001218)
                ToggleKami(True)
        elif quest13 == 1:
            print("quest ongoing")
            if field_id == 940200900:
                EnterPortal("next00")
                time.sleep(5)
            if field_id == 402000210:
                Quest.CompleteQuest(34611, 3001214)
            else:
                RushTo(402000210)
        if field_id == 940200700:
            print("first field")
            if len(Field.GetMobs()) == 0:
                DungeonTeleport()
            else:
                ToggleKami(True)
        elif field_id == 940200800:
            if len(Field.GetMobs()) == 0:
                DungeonTeleport()
            else:
                ToggleKami(True)
        elif field_id == 940200900:
            if len(Field.GetMobs()) == 0:
                DungeonTeleport()
            else:
                ToggleKami(True)
    elif quest14 != 2:
        if quest14 == 0:
            Quest.StartQuest(34612, 3001214)
        elif quest14 == 1:
            Quest.CompleteQuest(34612, 3001214)
            time.sleep(2)
    elif quest15 != 2:
        if quest15 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                time.sleep(3)
                Quest.StartQuest(34613, 0)
        elif quest15 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.CompleteQuest(34613, 3001210)
                time.sleep(2)
    elif quest16 != 2:
        if quest16 == 0:
            Quest.StartQuest(34614, 0)
        elif quest16 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                pos = Character.GetPos()
                if pos.x != -98:
                    ToggleKami(False)
                    Character.Teleport(-98, 304)
                else:
                    Quest.CompleteQuest(34614, 3001226)
                    ToggleKami(True)
    elif quest17 != 2:
        if quest17 == 0:
            Quest.StartQuest(34615, 0)
            time.sleep(3)
        elif quest17 == 1:
            # Talk to Gusto
            Terminal.Rush(402000200)
            while Terminal.IsRushing():
                time.sleep(5)
            Character.TalkToNpc(3001218)
            time.sleep(3)

            # Talk to Corbo
            Terminal.Rush(402000100)
            while Terminal.IsRushing():
                time.sleep(5)
            Character.TalkToNpc(3001219)
            time.sleep(3)

            # Talk to Antuin
            Terminal.Rush(402000000)
            while Terminal.IsRushing():
                time.sleep(5)
            pos = Character.GetPos()
            if pos.x != -1639:
                ToggleKami(False)
                Character.Teleport(-1639, 35-20)
                time.sleep(3)
            Character.TalkToNpc(3001212)
            time.sleep(8)
            ToggleKami(True)
    elif quest18 != 2:
        if quest18 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34616, 0)
        elif quest18 == 1:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.CompleteQuest(34616, 3001204)
    elif quest19 != 2:
        if quest19 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34617, 3001204)
        elif quest19 == 1:
            if Quest.CheckCompleteDemand(34617, 3001204) == 0:
                if field_id != 402000000:
                    Terminal.Rush(402000000)
                else:
                    pos = Character.GetPos()
                    if pos.x != -1639:
                        ToggleKami(False)
                        Character.Teleport(-1639, 35 - 20)
                    else:
                        Quest.CompleteQuest(34617, 3001204)
                        ToggleKami(True)
            else:
                if field_id != 402000120:
                    Terminal.Rush(402000120)
    elif quest20 != 2:
        if quest20 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34618, 3001204)
        elif quest20 == 1:
            if Quest.CheckCompleteDemand(34618, 3001204) == 0:
                if field_id != 402000000:
                    Terminal.Rush(402000000)
                else:
                    pos = Character.GetPos()
                    if pos.x != -1650:
                        ToggleKami(False)
                        Character.Teleport(-1650, 35 - 20)
                    else:
                        Quest.CompleteQuest(34618, 3001204)
                        ToggleKami(True)
            else:
                if field_id != 402000121:
                    Terminal.Rush(402000121)
    elif quest21 != 2:
        print("21 "+str(quest21))
        if quest21 == 0:
            while Field.GetID() == 940200507:
                Key.Press(0x20)
                Key.Up(0x20)
                time.sleep(0.1)
            else:
                pos = Character.GetPos()
                if pos.x != -1701:
                    ToggleKami(False)
                    Character.Teleport(-1701, 27 - 20)
                    time.sleep(3)
                if field_id != 402000000:
                    Terminal.Rush(402000000)
                else:
                    Quest.StartQuest(34619, 3001204)
                    ToggleKami(True)
        elif quest21 == 1:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.CompleteQuest(34619, 3001204)
    elif quest22 != 2:
        print("22")
        if quest22 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34620, 3001212)
        elif quest22 == 1:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.CompleteQuest(34620, 3001212)
    elif quest23 != 2:
        print("23")
        if quest23 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34621, 0)
        elif quest23 == 1:
            if Quest.CheckCompleteDemand(34621, 3001228) == 0:
                if field_id != 402000000:
                    Terminal.Rush(402000000)
                else:
                    Quest.CompleteQuest(34621, 3001228)
            else:
                if field_id != 402000122:
                    Terminal.Rush(402000122)
    elif quest24 != 2:
        print("24")
        if quest24 == 0:
            if field_id != 402000000:
                Terminal.Rush(402000000)
            else:
                Quest.StartQuest(34622, 0)
        elif quest24 == 1:
            if field_id != 402000301:
                Terminal.Rush(402000301)
            else:
                Quest.CompleteQuest(34622, 3001220)
    elif quest25 != 2:
        print("25")
        if quest25 == 0:
            if field_id == 940201000:
                time.sleep(1)
            elif field_id != 402000301:
                Terminal.Rush(402000301)
            else:
                Quest.StartQuest(34623, 3001223)
        elif quest25 == 1:
            if field_id == 402000301:
                Quest.CompleteQuest(34623, 3001211)
    elif quest26 != 2:
        print("26")
        if quest26 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34624, 3001200)
        elif quest26 == 1:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.CompleteQuest(34624, 3001200)
    elif quest27 != 2:
        print("27")
        if quest27 == 0:
            if field_id != 402000001:
                Terminal.Rush(402000001)
            else:
                Quest.StartQuest(34625, 3001200)
        elif quest27 == 1:
            if field_id != 402000400:
                Terminal.Rush(402000400)
            else:
                Quest.CompleteQuest(34625, 3001205)
                time.sleep(5)
                ToggleKami(True)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; cadena")
                
    if job == 6400 and level >= 30:
        Quest.StartQuest(34657, 3001250)
        ToggleKami(True)
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; cadena")

def CadenaThirdJobAdv():
    Quest.StartQuest(34658, 3001250)

def CadenaFourthJobAdv():
    Quest.StartQuest(34659,0)

def ArkFirstJobAdv():
    SCLib.UpdateVar("DoingJobAdv",True)
    quest1 = Quest.GetQuestState(34915)
    quest2 = Quest.GetQuestState(34916)
    quest3 = Quest.GetQuestState(34917)
    quest4 = Quest.GetQuestState(34918)
    quest5 = Quest.GetQuestState(34919)
    quest6 = Quest.GetQuestState(34920)
    quest7 = Quest.GetQuestState(34921)
    quest8 = Quest.GetQuestState(34922)
    quest9 = Quest.GetQuestState(34923)
    quest10 = Quest.GetQuestState(34924)
    quest11 = Quest.GetQuestState(34925)
    quest12 = Quest.GetQuestState(34926)
    quest13 = Quest.GetQuestState(34927)
    quest14 = Quest.GetQuestState(34928)
    quest15 = Quest.GetQuestState(34929)
    quest16 = Quest.GetQuestState(34930)
    quest17 = Quest.GetQuestState(34931)
    quest18 = Quest.GetQuestState(34932)
    quest19 = Quest.GetQuestState(34933)
    quest20 = Quest.GetQuestState(34934)
    quest21 = Quest.GetQuestState(34935)
    quest22 = Quest.GetQuestState(34936)
    quest23 = Quest.GetQuestState(34937)
    quest24 = Quest.GetQuestState(34938)
    quest25 = Quest.GetQuestState(34902)
    if quest1 != 2:
        print("1")
        ToggleRushByLevel(False)
        if quest1 == 0:
            print("Starting quest")
            StartQuest(34915, 3001406, 402000615)
        if field_id == 940205000:
            ToggleKami(True)
    elif quest2 != 2:   
        print("2")
        if quest2 == 0:
            ToggleKami(False)
            StartQuest(34916, 3001400, 402000600)
        elif quest2 == 1:
            ToggleKami(False)
            CompleteQuest(34916, 3001400, 402000600)
    elif quest3 != 2:
        print("3")
        if quest3 == 0:
            print("3.0")
            ToggleKami(False)
            StartQuest(34917, 3001400, 402000600)
        elif quest3 == 1:
            print("3.1")
            if Quest.CheckCompleteDemand(34917, 3001400) == 0:
                ToggleKami(False)
                CompleteQuest(34917, 3001400, 402000600)
            else:
                KillMobAndLoot(402000610)
    elif quest4 != 2:
        print("4")
        if quest4 == 0:
            ToggleKami(False)
            StartQuest(34918, 3001400, 402000600)
        elif quest4 == 1:
            ToggleKami(False)
            CompleteQuest(34918, 3001401, 402000600)
    elif quest5 != 2:
        print("5")
        if quest5 == 0:
            ToggleKami(False)
            StartQuest(34919, 3001401, 402000600)
        elif quest5 == 1:
            if Quest.CheckCompleteDemand(34919, 3001401)!= 0:
                KillMobAndLoot(402000611)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34919, 3001401, 402000600)
    elif quest6 != 2:
        print("6")
        if quest6 == 0:
            ToggleKami(False)
            StartQuest(34920, 3001401, 402000600)
        elif quest6 == 1:
            CompleteQuest(34920, 3001402, 402000600)
    elif quest7 != 2:
        print("7")
        if quest7 == 0:
            ToggleKami(False)
            StartQuest(34921, 3001402, 402000600)
        elif quest7 == 1:
            if Quest.CheckCompleteDemand(34921, 3001402):
                KillMobAndLoot(402000612)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34921, 3001402, 402000600)
    elif quest8 != 2:
        print("8")
        if quest8 == 0:
            ToggleKami(False)
            StartQuest(34922, 3001402, 402000600)
        elif quest8 == 1:
            ToggleKami(False)
            CompleteQuest(34922, 3001403, 402000600)
    elif quest9 != 2:
        print("9")
        if quest9 == 0:
            ToggleKami(False)
            StartQuest(34923, 3001404, 402000613)
        elif quest9 == 1:
            if Quest.CheckCompleteDemand(34923, 3001404):
                KillMobAndLoot(402000613)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34923, 3001404, 402000613)
    elif quest10 != 2:
        print("10")
        if quest10 == 0:
            ToggleKami(False)
            StartQuest(34924, 3001400, 402000600)
        elif quest10 == 1:
            ToggleKami(False)
            CompleteQuest(34924, 3001405, 402000614)
    elif quest11 != 2:
        print("11")
        if quest11 == 0:
            ToggleKami(False)
            StartQuest(34925, 3001405, 402000614)
        elif quest11 == 1:
            ToggleKami(False)
            CompleteQuest(34925, 3001400, 402000600)
    elif quest12 != 2:
        print("12")
        if quest12 == 0:
            ToggleKami(False)
            StartQuest(34926, 3001402, 402000600)
        elif quest12 == 1:
            if Quest.CheckCompleteDemand(34926, 3001402):
                KillMobAndLoot(402000616)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34926, 3001402, 402000600)
    elif quest13 != 2:
        print("13")
        if quest13 == 0:
            ToggleKami(False)
            StartQuest(34927, 3001401, 402000600)
        elif quest13 == 1:
            if Quest.CheckCompleteDemand(34927, 3001401):
                KillMobAndLoot(402000617)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34927, 3001401, 402000600)
    elif quest14 != 2:
        print("14")
        if quest14 == 0:
            ToggleKami(False)
            StartQuest(34928, 3001400, 402000600)
        elif quest14 == 1:
            ToggleKami(False)
            CompleteQuest(34928, 3001407, 402000615)
    elif quest15 != 2:
        print("15")
        if quest15 == 0:
            ToggleKami(False)
            StartQuest(34929, 3001400, 402000600)       
        elif quest15 == 1:
            ToggleKami(False)
            CompleteQuest(34929, 3001408, 402000620)
    elif quest16 != 2:
        print("16")
        if quest16 == 0:
            ToggleKami(False)
            StartQuest(34930, 3001409, 402000621)
        elif quest16 == 1:
            if Quest.CheckCompleteDemand(34930, 3001409):
                KillMobAndLoot(402000621)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34930, 3001409, 402000621)
    elif quest17 != 2:
        print("17")
        if quest17 == 0:
            ToggleKami(False)
            StartQuest(34931, 3001410, 402000622)
        elif quest17 == 1:
            if Quest.CheckCompleteDemand(34931, 3001410):
                KillMobAndLoot(402000622)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34931, 3001410, 402000622)
    elif quest18 != 2:
        print("18")
        if quest18 == 0:
            ToggleKami(False)
            StartQuest(34932, 3001411, 402000630)
        elif quest18 == 1:
            ToggleKami(False)
            CompleteQuest(34932, 3001412, 402000631)
    elif quest19 != 2:
        print("19")
        if quest19 == 0:
            ToggleKami(False)
            StartQuest(34933, 3001412, 402000631)
        elif quest19 == 1:
            if Quest.CheckCompleteDemand(34933, 3001412):
                KillMobAndLoot(402000631)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34933, 3001412, 402000631)
    elif quest20 != 2:
        print("20")
        if quest20 == 0:
            ToggleKami(False)
            StartQuest(34934, 3001413, 402000633)
        elif quest20 == 1:
            if Quest.CheckCompleteDemand(34934, 3001413):
                KillMobAndLoot(402000633)
                time.sleep(5)
            else:
                ToggleKami(False)
                CompleteQuest(34934, 3001413, 402000633)
    elif quest21 != 2:
        print("21")
        if quest21 == 0:
            ToggleKami(False)
            StartQuest(34935, 3001414, 402000635)
        elif quest21 == 1:
            ToggleKami(False)
            CompleteQuest(34935, 3001416, 402000648)
    elif quest22 != 2:
        print("22")
        if quest22 == 0:
            ToggleKami(False)
            StartQuest(34936, 3001415, 402000648)
            time.sleep(2)
            while Field.GetID() == 402090006:
                Key.Press(0x20)
                Key.Press(0x88)
                print("press")
    elif quest23 != 2:
        print("23")
        if quest23 == 0:
            ToggleKami(False)
            StartQuest(34937, 3001417, 402000644)
        elif quest23 == 1:
            ToggleKami(False)
            CompleteQuest(34937, 3001417, 402000644)
    elif quest24 != 2:
        print("24")
        if quest24 == 0:
            if Field.GetID() == 402000644:
                ToggleKami(False)
                StartQuest(34938, 3001423, 402000644)
            elif Field.GetID() == 940205100:
                ToggleKami(True)
                time.sleep(3)
                print("{} Mobs remaining".format(len(Field.GetMobs())))
                if len(Field.GetMobs()) == 0:
                    EnterPortal("next00")
            elif Field.GetID() == 940205200:
                ToggleKami(True)
                time.sleep(3)
                print("{} Mobs remaining".format(len(Field.GetMobs())))
                if len(Field.GetMobs()) == 0:
                    EnterPortal("next00")
                
            elif Field.GetID() == 940205300:
                ToggleKami(True)
                time.sleep(3)
                print("{} Mobs remaining".format(len(Field.GetMobs())))
                if len(Field.GetMobs()) == 0:
                    EnterPortal("next00")
            elif field_id != 402000644:
                RushTo(402000644)
                    
    elif quest25 != 2:
        print("25")
        if quest25 == 0:
            ToggleKami(False)
            StartQuest(34902, 0, 402000640)
            #SCLib.UpdateVar("DoingJobAdv",False)

def ArkSecondJobAdv():
    quest1 = Quest.GetQuestState(34939)
    quest2 = Quest.GetQuestState(34940)
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest1 != 2:
        if quest1 == 0:
            ToggleKami(False)
            StartQuest(34939, 0, 402000640)
        elif quest1 == 1:
            ToggleKami(False)
            CompleteQuest(34939, 0, 402000640)
    elif quest2 != 2:
        if quest2 == 0:
            if Field.GetID() == 402000640:
                ToggleKami(False)
                StartQuest(34940, 0, 402000640)
        elif Field.GetID() == 940205400:
            ToggleKami(True)
            time.sleep(3)
            print("{} Mobs remaining".format(len(Field.GetMobs())))
            if len(Field.GetMobs()) == 0:
                EnterPortal("next00")
        elif Field.GetID() == 940205500:
            ToggleKami(True)
            time.sleep(3)
            print("{} Mobs remaining".format(len(Field.GetMobs())))
            if len(Field.GetMobs()) == 0:
                EnterPortal("next00")
        elif Field.GetID() == 940205600:
            ToggleKami(True)
            time.sleep(3)
            print("{} Mobs remaining".format(len(Field.GetMobs())))
            if len(Field.GetMobs()) == 0:
                EnterPortal("next00")
        elif Field.GetID() == 940205900:
            ToggleKami(True)
            time.sleep(3)
    elif quest2 == 2:
        ToggleRushByLevel(True)
        ToggleKami(True)
        print("Ark done")
        SCLib.UpdateVar("DoingJobAdv",False)
    if level >= 60:
        jobQuest = Quest.GetQuestState(34903)
        print("Completing Ark Third Job Adv")
        if jobQuest != 2:
            if jobQuest == 0:
                Quest.StartQuest(34903, 0)
                time.sleep(5)
            elif jobQuest == 1:
                Quest.CompleteQuest(34903, 0)
                time.sleep(5)
                SCLib.UpdateVar("DoingJobAdv",False)

def ArkFourthJobAdv():
    jobQuest = Quest.GetQuestState(34904)
    if jobQuest != 2:
        if jobQuest == 0:
            Quest.StartQuest(34904, 0)
            time.sleep(5)
        elif jobQuest == 1:
            Quest.CompleteQuest(34904, 0)
            time.sleep(5)
            SCLib.UpdateVar("DoingJobAdv",False)

def EvanFirstJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    StrangeDream = 22000
    FeedingBullDog = 22001
    SandwichForBreakfast = 22002
    DeliveringTheLunchBox = 22003
    FixingTheFence = 22004
    RescuingThePiglet = 22005
    ReturningTheEmptyLunchBox = 22006
    CollectingEggs = 22007
    ChasingAwayTheFoxes = 22008
    VerifyingTheFarmSituation = 22009
    StrangeFarm = 22010
    BabyDragonAwakens = 22500
    HungryBabyDragon = 22501
    ABiteOfHay = 22502
    ABiteOfPork = 22503
    TastyMilk1 = 22504
    TastyMilk2 = 22505
    TastyMilk3 = 22506
    WhatIsADragonMaster = 22507
    StrangePigs1 = 22508
    StrangePigs2 = 22509
    LetterDelivery = 22510
    DragonMaster1stJobAdvancement = 22100
    quest1 = Quest.GetQuestState(StrangeDream)
    quest2 = Quest.GetQuestState(FeedingBullDog)
    quest3 = Quest.GetQuestState(SandwichForBreakfast)
    quest4 = Quest.GetQuestState(DeliveringTheLunchBox)
    quest5 = Quest.GetQuestState(FixingTheFence)
    quest6 = Quest.GetQuestState(RescuingThePiglet)
    quest7 = Quest.GetQuestState(ReturningTheEmptyLunchBox)
    quest8 = Quest.GetQuestState(CollectingEggs)
    quest9 = Quest.GetQuestState(ChasingAwayTheFoxes)
    quest10= Quest.GetQuestState(VerifyingTheFarmSituation)
    quest11= Quest.GetQuestState(StrangeFarm)
    quest12= Quest.GetQuestState(BabyDragonAwakens)
    quest13= Quest.GetQuestState(HungryBabyDragon)
    quest14= Quest.GetQuestState(ABiteOfHay)
    quest15= Quest.GetQuestState(ABiteOfPork)
    quest16= Quest.GetQuestState(TastyMilk1)
    quest17= Quest.GetQuestState(TastyMilk2)
    quest18= Quest.GetQuestState(TastyMilk3)
    quest19= Quest.GetQuestState(WhatIsADragonMaster)
    quest20= Quest.GetQuestState(StrangePigs1)
    quest21= Quest.GetQuestState(StrangePigs2)
    quest22= Quest.GetQuestState(LetterDelivery)
    DragonNest = 1013002
    Mir = 1013000
    Mom = 1013100
    Utah = 1013101
    BullDog = 1013102
    Dad = 1013103
    Hen = 1013104
    DairyCow = 1013105
    ChiefStan= 1012003
    livingroom = 100030101
    frontyard = 100030102
    backyard = 100030103
    farmcentre = 100030300
    largeforesttrail = 100030310
    largeforesttrail2= 100030320
    lushforest = 900020100
    lostforest = 900020220
    pet = Inventory.FindItemByID(2434265)
    Terminal.SetCheckBox("settings/loginwait",False)
    if pet.valid and quest5 == 2:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)
    if field_id == 900010000:
        print("1")
        ToggleKami(False)
        Key.Press(0x08)
        time.sleep(1)
        Character.EnterPortal()
        time.sleep(2)
    elif field_id == 900010100:
        print("2")
        ToggleKami(False)
        Key.Press(0x08)
        time.sleep(1)
        Character.EnterPortal()
        time.sleep(10)
    elif field_id == 900010200:
        print("3")
        ToggleKami(False)
        Character.Teleport(-455,35)
        time.sleep(1)
        Character.TalkToNpc(1013001)
        time.sleep(2)
    elif quest1 != 2:
        print("4")
        Terminal.SetCheckBox("settings/loginwait",False)
        if quest1 == 0:
            ToggleKami(False)
            acceptQuest(StrangeDream,Mom,livingroom,field_id)
            SCLib.UpdateVar("EvanLogout",True)
        elif quest1 == 1:
            Terminal.SetCheckBox("settings/explogout",True)
            Terminal.SetSpinBox("settings/explogout",1)
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            completeQuest(StrangeDream,Utah,frontyard,frontyard,field_id) # leaving living room once completing the quest at Utah once
            time.sleep(1)
            if Quest.GetQuestState(StrangeDream) == 2:
                SCLib.UpdateVar("EvanLogout",True)
    elif quest2 != 2:
        print("2")
        Terminal.SetCheckBox("settings/loginwait",False)
        if quest2 == 0:
            ToggleKami(False)
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            acceptQuest(FeedingBullDog,Utah,frontyard,field_id) #once before accepting quest
            time.sleep(1)
            if Quest.GetQuestState(FeedingBullDog) != 1:
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
        elif quest2 == 1:
            completeQuest(FeedingBullDog,BullDog,frontyard,frontyard,field_id)
    elif quest3 != 2:
        print("3")
        Terminal.SetCheckBox("settings/loginwait",False)
        if quest3 == 0:
            SCLib.UpdateVar("EvanLogout",True)
            acceptQuest(SandwichForBreakfast,Utah,frontyard,field_id) #Accepting the quest once
        elif quest3 == 1:
            sandwich = Inventory.FindItemByID(2022620)
            if SCLib.GetVar("EvanLogout") and sandwich.valid:
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            if sandwich.valid:
                time.sleep(1)
                Inventory.UseItem(2022620)
                time.sleep(1)
            print("Doing sandwich quest")
            completeQuest(SandwichForBreakfast,Mom,livingroom,livingroom,field_id) #completing quest once
            if Quest.GetQuestState(SandwichForBreakfast) == 2:
                SCLib.UpdateVar("EvanLogout",True)
                time.sleep(2)
    elif quest4 != 2:
        Terminal.SetCheckBox("settings/loginwait",False)
        if quest4 == 0:
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            acceptQuest(DeliveringTheLunchBox,Mom,livingroom,field_id) #lunch box once
            time.sleep(1)
            if Quest.GetQuestState(DeliveringTheLunchBox) == 1:
                SCLib.UpdateVar("EvanLogout",True)
            else:
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
        elif quest4 == 1:
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            completeQuest(DeliveringTheLunchBox,Dad,farmcentre,farmcentre,field_id)
    elif quest5 != 2:
        Terminal.SetCheckBox("settings/loginwait",False)
        if quest5 == 0:
            SCLib.UpdateVar("EvanLogout",True)
            acceptQuest(FixingTheFence,Dad,farmcentre,field_id) #attaking once
        elif quest5 == 1:
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            completeQuest(FixingTheFence,Dad,farmcentre,farmcentre,field_id)
            ToggleLoot(True)
    elif quest6 != 2:
        print("6")
        Terminal.SetCheckBox("settings/loginwait",False)
        ToggleLoot(False)
        if quest6 == 0:
            print("Toggling logout var")
            SCLib.UpdateVar("EvanLogout",True)
            acceptQuest(RescuingThePiglet,Dad,farmcentre,field_id) #sitting chair once
        elif quest6 == 1:
            if Quest.CheckCompleteDemand(RescuingThePiglet,Dad) != 0:
                if SCLib.GetVar("EvanLogout"):
                    SCLib.UpdateVar("EvanLogout",False)
                    if GameState.IsInGame():
                        Terminal.Logout()
                if field_id == lushforest:
                    piglet = Field.FindNpc(1013200)
                    if piglet.valid:
                        ToggleKami(False)
                        Character.Teleport(piglet.x,piglet.y)
                        time.sleep(1)
                        Character.TalkToNpc(1013200)
                        time.sleep(1)
                        Character.Teleport(piglet.x - 200,piglet.y + 200)
                elif field_id == farmcentre:
                    #Terminal.Rush(lushforest)
                    TeleportEnter(181,-865)
                    print("This part needs to be changed") #
            if field_id == lostforest:
                dragnest = Field.FindNpc(DragonNest)
                if dragnest.valid:
                    ToggleKami(False)
                    Character.Teleport(dragnest.x,dragnest.y)
                    time.sleep(1)
                    Character.TalkToNpc(DragonNest)
            elif field_id == 900020200 or field_id == 900020210:
                ToggleKami(False)
                Key.Press(0x08)
                time.sleep(1)
                Character.EnterPortal()
                SCLib.UpdateVar("EvanLogout",True)
            elif field_id == lushforest or field_id == 900020110: #dragon egg once
                if SCLib.GetVar("EvanLogout"):
                    if GameState.IsInGame():
                        Terminal.Logout()
                    SCLib.UpdateVar("EvanLogout",False)
                ToggleKami(False)
                Key.Press(0x08)
                time.sleep(1)
                Character.EnterPortal()
            if Quest.CheckCompleteDemand(RescuingThePiglet,Dad) == 0:
                if field_id ==farmcentre:
                    completeQuest(RescuingThePiglet,Dad,farmcentre,farmcentre,field_id)
    elif quest7 != 2:
        print("7")
        if quest7 == 0:
            acceptQuest(ReturningTheEmptyLunchBox,Dad,farmcentre,field_id)
        elif quest7 == 1:
            completeQuest(ReturningTheEmptyLunchBox,Mom,livingroom,livingroom,field_id)
    elif quest8 != 2:
        if quest8 == 0:
            acceptQuest(CollectingEggs,Utah,frontyard,field_id)
        elif quest8 == 1:
            if field_id != frontyard:
                Terminal.Rush(frontyard)
            elif field_id == frontyard:
                npc_hen = Field.FindNpc(Hen)
                if npc_hen.valid and Quest.CheckCompleteDemand(CollectingEggs,Utah) != 0:
                    ToggleKami(False)
                    Character.Teleport(npc_hen.x,npc_hen.y)
                    time.sleep(1)
                    Character.TalkToNpc(Hen)
            completeQuest(CollectingEggs,Utah,frontyard,frontyard,field_id)
            SCLib.UpdateVar("EvanLogout",True)
    elif quest9 != 2:
        if quest9 == 0: #incubator once
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            acceptQuest(ChasingAwayTheFoxes,Utah,frontyard,field_id)
            time.sleep(1)
            if Quest.GetQuestState(ChasingAwayTheFoxes) == 1:
                SCLib.UpdateVar("EvanLogout",True)
        elif quest9 == 1: #setting up hot key once
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            completeQuest(ChasingAwayTheFoxes,Utah,frontyard,backyard,field_id)
            time.sleep(1)
            if Quest.GetQuestState(ChasingAwayTheFoxes) == 2:
                SCLib.UpdateVar("EvanLogout",True)
    elif quest10 != 2:
        if quest10 == 0:
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            acceptQuest(VerifyingTheFarmSituation,Utah,frontyard,field_id)
        elif quest10 == 1:
            completeQuest(VerifyingTheFarmSituation,Dad,farmcentre,farmcentre,field_id)
    elif quest11 != 2:
        if quest11 == 0:
            acceptQuest(StrangeFarm,Dad,farmcentre,field_id)
            SCLib.UpdateVar("EvanLogout",True)
        elif quest11 == 1: #dragon out once
            completeQuest(StrangeFarm,Dad,farmcentre,largeforesttrail,field_id)
            time.sleep(2)
            if SCLib.GetVar("EvanLogout") and level == 10 or Character.GetPos().x == 196:
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
    elif quest12 != 2:
        if quest12 == 0: #not sure with npc here 2411021
            acceptQuest(BabyDragonAwakens,Mir,farmcentre,field_id)
            SCLib.UpdateVar("EvanLogout",True)
        elif quest12 == 1: #stat window
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            completeQuest(BabyDragonAwakens,Mir,farmcentre,largeforesttrail,field_id)
    elif quest13 != 2:
        if quest13 == 0:
            acceptQuest(HungryBabyDragon,Mir,field_id,field_id)
        elif quest13 == 1:
            completeQuest(HungryBabyDragon,Dad,farmcentre,farmcentre,field_id)
    elif quest14 != 2:
        if quest14 == 0:
            acceptQuest(ABiteOfHay,Dad,farmcentre,field_id)
        elif quest14 == 1:
            ToggleKami(False)
            ToggleLoot(False)
            if field_id == farmcentre:
                haystacks = Field.GetReactors()
                for haystack in haystacks:
                    pos = Character.GetPos()
                    if Quest.CheckCompleteDemand(ABiteOfHay,Mir) == 0:
                        break
                    else:
                        ToggleLoot(True)
                        if pos.x != haystack.x:
                            Character.Teleport(haystack.x,haystack.y)
                            ToggleAttackQuest(False)
                            time.sleep(2)
                            Character.BasicAttack()
                            time.sleep(2)
                            Character.BasicAttack()
                            time.sleep(2)
                            Character.BasicAttack()
                            time.sleep(2)
                            Character.BasicAttack()
                        else:
                            time.sleep(2)
                            Character.BasicAttack()
                            time.sleep(2)
                            Character.BasicAttack()
                            time.sleep(2)
                            Character.BasicAttack()
                            time.sleep(2)
                            Character.BasicAttack()
            completeQuest(ABiteOfHay,Mir,farmcentre,farmcentre,field_id)
            ToggleLoot(False)
            time.sleep(1)
            if Quest.GetQuestState(ABiteOfHay) == 2:
                SCLib.UpdateVar("EvanLogout",True)
    elif quest15 != 2:
        if quest15 == 0: #destroying object once
            if SCLib.GetVar("EvanLogout"):
                if GameState.IsInGame():
                    Terminal.Logout()
                SCLib.UpdateVar("EvanLogout",False)
            acceptQuest(ABiteOfPork,Mir,farmcentre,field_id)
        elif quest15 ==1:
            completeQuest(ABiteOfPork,Mir,largeforesttrail,largeforesttrail,field_id)
    elif quest16 != 2:
        if quest16 == 0:
            acceptQuest(TastyMilk1,Mir,farmcentre,field_id)
        elif quest16 == 1:
            completeQuest(TastyMilk1,Dad,farmcentre,farmcentre,field_id)
    elif quest17 != 2:
        if quest17 == 0:
            acceptQuest(TastyMilk2,Dad,farmcentre,field_id)
        elif quest17 == 1:
            completeQuest(TastyMilk2,DairyCow,largeforesttrail,largeforesttrail,field_id)
    elif quest18 != 2:
        if quest18 == 0:
            acceptQuest(TastyMilk3,DairyCow,largeforesttrail,field_id)
        elif quest18 == 1:
            completeQuest(TastyMilk3,Mir,largeforesttrail,largeforesttrail,field_id)
    elif quest19 != 2:
        Quest.StartQuest(WhatIsADragonMaster,Mir)
    elif quest20 != 2:
        if quest20 == 0:
            acceptQuest(StrangePigs1,Dad,farmcentre,field_id)
        elif quest20 == 1:
            completeQuest(StrangePigs1,Mir,farmcentre,farmcentre,field_id)
    elif quest21 != 2:
        if quest21 == 0:
            acceptQuest(StrangePigs2,Mir,farmcentre,field_id)
        elif quest21 == 1:
            completeQuest(StrangePigs2,Mir,largeforesttrail2,largeforesttrail2,field_id)
    elif quest22 != 2:
        if quest22 == 0:
            acceptQuest(LetterDelivery,Dad,farmcentre,field_id)
            SCLib.UpdateVar("EvanLogout",True)
        elif quest22 == 1:#world map once
            completeQuest(LetterDelivery,ChiefStan,henesys,henesys,field_id)
            if SCLib.GetVar("EvanLogout"):
                SCLib.UpdateVar("EvanLogout",False)
                if GameState.IsInGame():
                    Terminal.Logout()
            if field_id == henesys:
                ToggleKami(False)
                Character.Teleport(3350,124)
                time.sleep(1)
        if Quest.GetQuestState(LetterDelivery) == 2:
            ToggleRushByLevel(True)
            ToggleKami(True)
            print("Evan first job done")
    magicwand = Inventory.FindItemByID(1372043)
    if magicwand.valid:
        Inventory.SendChangeSlotPositionRequest(1,magicwand.pos,weapon_slot,-1)
        Terminal.SetCheckBox("settings/loginwait",True)
        SCLib.UpdateVar("EvanLogout",False)
    if Quest.GetQuestState(LetterDelivery) == 2:
        ToggleRushByLevel(True)
        ToggleKami(True)
        ToggleLoot(False)
        SCLib.UpdateVar("DoingJobAdv",False)
        SCLib.UpdateVar("EvanLogout",False)
        Terminal.SetCheckBox("settings/loginwait",True)
        Terminal.SetCheckBox("settings/explogout",False)
        print("Resume rush by level; evan")

def XenonSecondJobAdv():
    #print("Needs to be implemented")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    SecretInstructions = 23610
    VeritasFinest = 23611
    quest1 = Quest.GetQuestState(SecretInstructions)
    quest2 = Quest.GetQuestState(VeritasFinest)
    profDreamboat = 2300001
    veritas = 230050000
    pet = Inventory.FindItemByID(2434265)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)
    if quest1 != 2:
        if quest1 == 0:
            print("Starting quest1")
            Quest.StartQuest(SecretInstructions, 0)
    elif quest2 != 2:
        if quest2 == 0:
            print("Starting quest2")
            Quest.StartQuest(VeritasFinest, 0)
        elif quest2 == 1:
            completeQuest(VeritasFinest,profDreamboat,veritas,veritas,field_id)
            if Quest.GetQuestState(VeritasFinest) == 2:
                ToggleRushByLevel(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; xenon second")
    if Quest.GetQuestState(VeritasFinest) == 2:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; xenon second")
    
def XenonThirdJobAdv():
    ToggleRushByLevel(False)
    ToggleKami(False)
    OnlyTheBrave = 23612
    BlackWingsHat1 = 23613
    BlackWingsHat2 = 23614
    GettingCaught = 23615
    quest1 = Quest.GetQuestState(OnlyTheBrave)
    quest2 = Quest.GetQuestState(BlackWingsHat1)
    quest3 = Quest.GetQuestState(BlackWingsHat2)
    quest4 = Quest.GetQuestState(GettingCaught)
    roadtothemine1 = 310040000
    instancedmine1 = 931060030
    veritas = 230050000

    stephan = 2159421
    promathus = 2300002
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest1 != 2 :
        if quest1 == 0:
            print("Starting quest1")
            Quest.StartQuest(OnlyTheBrave,0)
        elif quest1 == 1:
            print("Doing quest1")
            if quest2 != 2:
                print("quest2")
                if field_id != roadtothemine1:
                    RushTo(roadtothemine1)
                if quest2 == 0:
                    acceptQuest(BlackWingsHat1,stephan,roadtothemine1,field_id)
                elif quest2 == 1:
                    completeQuest(BlackWingsHat1,stephan,roadtothemine1,roadtothemine1,field_id)
            elif quest3 != 2:
                print("quest3")
                acceptQuest(BlackWingsHat2,stephan,roadtothemine1,field_id)
            elif quest4 != 2:
                print("Quest4")
                if quest4 == 0:
                    if field_id != roadtothemine1:
                        RushTo(roadtothemine1)
                    else:
                        Quest.StartQuest(GettingCaught,stephan)
                        time.sleep(1)
                elif quest4 == 1:
                    if Quest.CheckCompleteDemand(23615,2159421) == 0:
                        ToggleKami(False)
                        ToggleAttackQuest(False)
                        time.sleep(5)
                        Quest.CompleteQuest(23615, 2159421)
                        time.sleep(1)
                        DungeonTeleport()
                        time.sleep(1)
                        DungeonTeleport()
                    else:
                        if len(Field.GetMobs()) >= 1 and field_id == 931060030:
                            ToggleKami(True)
                            Character.UseSkill(36101000)
                        else:
                            ForfeitQuest(23615)
            else:
                print("else")
                completeQuest(OnlyTheBrave,promathus,veritas,roadtothemine1,field_id)
                if Quest.GetQuestState(OnlyTheBrave) == 2:
                    SCLib.UpdateVar("DoingJobAdv",False)
            
def XenonFourthJobAdv():
    ToggleRushByLevel(False)
    ToggleKami(False)
    IdentiyCrisis = 23616
    rooD = 2300000
    veritas = 230050000
    quest1 = Quest.GetQuestState(IdentiyCrisis)
    SCLib.UpdateVar("DoingJobAdv",True)
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(IdentiyCrisis,0)
        elif quest1 == 1:
            completeQuest(IdentiyCrisis,rooD,veritas,veritas,field_id)
            if Quest.GetQuestState(IdentiyCrisis) == 2:
                SCLib.UpdateVar("DoingJobAdv",False)

def PhantomFirstJobAdv():
    #print("Needs to be implemented")
    SCLib.UpdateVar("DoingJobAdv",True)
    time.sleep(1)
    AProperIntroduction = 25000
    quest1 = Quest.GetQuestState(AProperIntroduction)
    ToggleRushByLevel(False)
    Forecastle = 915000000
    WaistDeck = 915000100
    Outside = 915000200
    KnightsChamberPre = 915000300
    KnightsChamberPost = 915000301
    Ereve = 915000400
    gaston = 1402000
    Kidan = 1402001
    if level == 1 and field_id == Forecastle:
        DungeonTeleport()
    if quest1 != 2:
        if quest1 == 0:
            acceptQuest(AProperIntroduction,gaston,WaistDeck,field_id)
        elif quest1 == 1:
            if field_id == WaistDeck:
                DungeonTeleport()
            elif field_id == Outside:
                TeleportEnter(-600,-672)
            elif field_id == KnightsChamberPre:
                if pos.x != -2447 and pos.y != 40:
                    ToggleKami(False)
                    Character.Teleport(-2447,40)
                EnterPortal("in00")
            elif field_id == KnightsChamberPost:
                #Character.TalkToNpc(Kidan)
                TeleportEnter(-1707,61)
            elif field_id == Ereve:
                DungeonTeleport()
                time.sleep(2)
                ToggleRushByLevel(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; phantom first")
    
def PhantomSecondJobAdv():
    #print("Needs to be implemented")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    TheErstWhileVault = 25100
    ThatsSoRaven = 25101
    quest1 = Quest.GetQuestState(TheErstWhileVault)
    quest2 = Quest.GetQuestState(ThatsSoRaven)
    cloudpark2 = 200020000
    smallpark = 200020001
    TreasureVaultEntrance = 915010000
    TreasureVault = 915010001

    smallcabinet = 1403000
    print(quest1)
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(TheErstWhileVault,0)
        elif quest1 == 1:
            #print("needs imple")
            if field_id != TreasureVaultEntrance:
                if field_id != smallpark:
                    if field_id != cloudpark2:
                        RushTo(cloudpark2)
                        time.sleep(1)
                    elif field_id == cloudpark2:
                        TeleportEnter(1116,-637)
                        time.sleep(2)
                elif field_id == smallpark:
                    TeleportEnter(263,83)
                    time.sleep(2)
            if Quest.CheckCompleteDemand(TheErstWhileVault,0) == 0:
                Quest.CompleteQuest(TheErstWhileVault,0)
    elif quest2 != 2:
        if quest2 == 0:
            Quest.StartQuest(ThatsSoRaven,0)
    if field_id != TreasureVaultEntrance:
        print("Second")
        if field_id != smallpark:
            if field_id != cloudpark2:
                RushTo(cloudpark2)
            elif field_id == cloudpark2:
                TeleportEnter(1116,-637)
        elif field_id == smallpark:
            TeleportEnter(263,83)
        if Quest.CheckCompleteDemand(ThatsSoRaven,0) == 0:
            Quest.CompleteQuest(ThatsSoRaven,0)
    if field_id == TreasureVaultEntrance and len(Field.GetMobs()) > 0:
        print("Break lock")
        ToggleKami(True)
        ToggleAttackQuest(True)
    elif field_id == TreasureVaultEntrance and len(Field.GetMobs()) == 0:
        ToggleKami(False)
        ToggleAttackQuest(False)
        TeleportEnter(163,182)
    if field_id == TreasureVault:
        Character.TalkToNpc(smallcabinet)
        time.sleep(1)
        Character.TalkToNpc(smallcabinet)
        time.sleep(1)
        Character.TalkToNpc(smallcabinet)
        time.sleep(1)
        ToggleKami(False)
        ToggleAttackQuest(False)
        DungeonTeleport()

def PhantomThirdJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    ThePoorTheRich = 25110
    TheLowdown = 25111
    quest1 = Quest.GetQuestState(ThePoorTheRich)
    quest2 = Quest.GetQuestState(TheLowdown)

    overlookedarea=260010601
    arianttreasure = 915010100
    arianttreasurevault = 915010101
    TreasureChest = 1403001
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(ThePoorTheRich,0)
            print("1.0")
        elif quest1 == 1:
            print("1.1")
            if Quest.CheckCompleteDemand(ThePoorTheRich,0) == 0:
                Quest.CompleteQuest(ThePoorTheRich,0)
    elif quest2 != 2:
        if quest2 == 0:
            print("2.0")
            Quest.StartQuest(TheLowdown,0)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(TheLowdown,0) == 0:
                Quest.CompleteQuest(TheLowdown,0)
                print("complete q2")
            elif field_id == overlookedarea:
                TeleportEnter(866,275)
            elif field_id == arianttreasure:
                mobs = Field.GetMobs()
                print("Killing mobs")
                '''
                for mob in mobs:
                    mobs = Field.GetMobs()
                    if mob.valid:
                        Character.Teleport(mob.x-20,mob.y)
                        Character.UseSkill(24001000)
                        time.sleep(1)
                        Character.UseSkill(24001000)
                        time.sleep(1)
                        Character.UseSkill(24001000)
                        time.sleep(1)
                        Character.UseSkill(24001000)
                        time.sleep(1)
                        Character.UseSkill(24001000)
                        time.sleep(1)
                        Character.UseSkill(24001000)
                        time.sleep(1)
                '''
                if len(mobs) == 0:
                    TeleportEnter(166,182)
                else:
                    ToggleKami(True)
            elif field_id == arianttreasurevault:
                Character.TalkToNpc(TreasureChest)
            elif field_id != 260010600:
                RushTo(260010600)
            elif field_id == 260010600:
                TeleportEnter(134,275)

def PhantomFourthJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    WhatsInAPhantom = 25120
    AnExpensiveAcquisition = 25121
    TheEmpressAndTheThief = 25122
    quest1 = Quest.GetQuestState(WhatsInAPhantom)
    quest2 = Quest.GetQuestState(AnExpensiveAcquisition)
    quest3 = Quest.GetQuestState(TheEmpressAndTheThief)
    lushforest = 240010102
    leafretreasurevaultentrance = 915010200
    leafretreasurevault = 915010201

    portrait = 1403003
    if quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(WhatsInAPhantom,0)
        elif quest1 == 1:
            if Quest.CheckCompleteDemand(WhatsInAPhantom,0) == 0:
                Quest.CompleteQuest(WhatsInAPhantom,0)
    elif quest2 != 2:
        if quest2 == 0:
            Quest.StartQuest(AnExpensiveAcquisition,0)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(AnExpensiveAcquisition,0) == 0:
                Quest.CompleteQuest(AnExpensiveAcquisition,0)
                print("complete q2")
            elif field_id == lushforest:
                TeleportEnter(476,332)
            elif field_id == leafretreasurevaultentrance:
                mobs = Field.GetMobs()
                if len(mobs) == 0:
                    TeleportEnter(165,182)
                else:
                    ToggleKami(True)
    elif quest3 != 2:
        if quest3 == 0:
            Quest.StartQuest(TheEmpressAndTheThief,0)
        elif quest3 ==1:
            if field_id == leafretreasurevaultentrance:
                mobs = Field.GetMobs()
                if len(mobs) == 0:
                    TeleportEnter(165,182)
                else:
                    ToggleKami(True)
            elif field_id == leafretreasurevault:
                Character.TalkToNpc(portrait)

def BeastTamerFirstJobAdv():
    SCLib.UpdateVar("DoingJobAdv",True)
    ReadingMap = 59019
    ToStumpTown = 59020
    TheBoyWhoCried = 59036
    BluffingTom = 59037
    TheKoboldThreat1 = 59038
    TheKoboldThreat2 = 59039
    TheKoboldThreat3 = 59040
    SavingTheTownsPeople1 = 59041
    SavingTheTownsPeople2 = 59042
    SavingTheTownsPeople3 = 59043
    DiscoveringTheDen = 59044
    quest1 = Quest.GetQuestState(ReadingMap)
    quest2 = Quest.GetQuestState(ToStumpTown)
    quest3 = Quest.GetQuestState(TheBoyWhoCried)
    quest4 = Quest.GetQuestState(BluffingTom)
    quest5 = Quest.GetQuestState(TheKoboldThreat1)
    quest6 = Quest.GetQuestState(TheKoboldThreat2)
    quest7 = Quest.GetQuestState(TheKoboldThreat3)
    quest8 = Quest.GetQuestState(SavingTheTownsPeople1)
    quest9 = Quest.GetQuestState(SavingTheTownsPeople2)
    quest10= Quest.GetQuestState(SavingTheTownsPeople3)
    quest11= Quest.GetQuestState(DiscoveringTheDen)
    StumpTown = 866000000
    DarkForestRoad1 = 866000100
    DarkForestRoad2 = 866000105
    CreepyForestPath1 = 866000110
    CreepyForestPath2 = 866000115
    GloomyForestPath = 866000120
    KoboldPit1 = 866000130
    woodrock = 9390312
    bluffingtomnpc = 9390313
    grandmatom = 9390451
    papatom = 9390450
    bluffingtomnpc2 = 9390314
    pet = Inventory.FindItemByID(2434265)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)
    if quest1 != 2:
        print("1")
        if quest1 == 0:
            Quest.StartQuest(ReadingMap,0)
        elif quest1 == 1:
            Quest.CompleteQuest(ReadingMap,0)
    elif quest2 != 2:
        print("2")
        if quest2 == 0:
            acceptQuest(ToStumpTown,0,field_id,field_id)
        elif quest2 == 1:
            completeQuest(ToStumpTown,woodrock,StumpTown,StumpTown,field_id)
    elif quest3 != 2:
        print("3")
        if quest3 == 0:
            acceptQuest(TheBoyWhoCried,woodrock,StumpTown,field_id)
        elif quest3 == 1:
            completeQuest(TheBoyWhoCried,woodrock,StumpTown,DarkForestRoad1,field_id)
    elif quest4 != 2:
        print("4")
        if quest4 == 0:
            acceptQuest(BluffingTom,bluffingtomnpc,StumpTown,field_id)
        elif quest4 == 1:
            completeQuest(BluffingTom,bluffingtomnpc,StumpTown,DarkForestRoad2,field_id)
    elif quest5 != 2:
        print("5")
        if quest5 == 0:
            acceptQuest(TheKoboldThreat1,bluffingtomnpc,StumpTown,field_id)
        elif quest5 == 1:
            completeQuest(TheKoboldThreat1,bluffingtomnpc,StumpTown,CreepyForestPath1,field_id)
    elif quest6 != 2:
        print("6")
        if quest6 == 0:
            acceptQuest(TheKoboldThreat2,woodrock,StumpTown,field_id)
        elif quest6 == 1:
            completeQuest(TheKoboldThreat2,woodrock,StumpTown,CreepyForestPath2,field_id)
    elif quest7 != 2:
        print("7")
        if quest7 == 0:
            acceptQuest(TheKoboldThreat3,bluffingtomnpc,StumpTown,field_id)
        elif quest7 == 1:
            completeQuest(TheKoboldThreat3,bluffingtomnpc,StumpTown,GloomyForestPath,field_id)
    elif quest8 != 2:
        print("8")
        if quest8 == 0:
            acceptQuest(SavingTheTownsPeople1,woodrock,StumpTown,field_id)
        elif quest8 == 1:
            completeQuest(SavingTheTownsPeople1,grandmatom,DarkForestRoad2,DarkForestRoad2,field_id)
    elif quest9 != 2:
        print("9")
        if quest9 == 0:
            acceptQuest(SavingTheTownsPeople2,grandmatom,DarkForestRoad2,field_id)
        elif quest9 == 1:
            completeQuest(SavingTheTownsPeople2,papatom,CreepyForestPath2,CreepyForestPath2,field_id)
    elif quest10 != 2:
        print("10")
        if quest10 == 0:
            acceptQuest(SavingTheTownsPeople3,papatom,CreepyForestPath2,field_id)
        elif quest10 == 1:
            completeQuest(SavingTheTownsPeople3,bluffingtomnpc2,GloomyForestPath,GloomyForestPath,field_id)
    elif quest11 != 2:
        print("11")
        if quest11 == 0:
            acceptQuest(DiscoveringTheDen,bluffingtomnpc,StumpTown,field_id)
        elif quest11 == 1:
            completeQuest(DiscoveringTheDen,woodrock,StumpTown,StumpTown,field_id)
    elif quest11 == 2 and level < 33:
        RushTo(KoboldPit1)
        ToggleKami(False)
    elif quest11 == 2 and level >= 33:
        AlishanRushing()
        SCLib.UpdateVar("DoingJobAdv",False)
    
def AranFirstJobAdv():
    def TeleportToNPC(npc, delay):
        fnpc = Field.FindNpc(npc)           
        if fnpc.valid:
            time.sleep(delay)                        
            ToggleKami(False)
            Character.Teleport(fnpc.x, fnpc.y)
            time.sleep(delay)         

    def Autism():
        time.sleep(1)
        #Key.Press(0x11)
        Character.BasicAttack()
        time.sleep(3)
        #Key.Press(0x11)
        Character.BasicAttack()
        time.sleep(3)
        #Key.Press(0x11)
        Character.BasicAttack()
        time.sleep(3)
        Character.BasicAttack()
        #Key.Press(0x11)
    # Map
    black_road                = 914000000
    snow_island               = 140090000
    rien                      = 140000000
    snowcoveredfield1         = 140020000
    snowcoveredfield2         = 140020100
    snowcoveredfield3         = 140020200
    dangerousforest           = 140010200
    # Quest
    find_the_lost_kid         = 21000
    return_of_the_hero        = 21010
    the_missing_weapon        = 21011
    abilities_lost            = 21012
    gift_for_the_hero         = 21013
    lilins_account            = 21014
    basic_fitness_training_1  = 21015
    basic_fitness_training_2  = 21016
    basic_fitness_training_3  = 21017
    basic_fitness_test        = 21018
    the_five_heroes           = 21100
    thePolearmWieldingHero    = 21101
    newBegginings             = 21700
    quest7 = Quest.GetQuestState(basic_fitness_training_1)
    quest8 = Quest.GetQuestState(basic_fitness_training_2)
    quest9 = Quest.GetQuestState(basic_fitness_training_3)
    quest10= Quest.GetQuestState(basic_fitness_test)
    quest11= Quest.GetQuestState(the_five_heroes)
    quest12= Quest.GetQuestState(thePolearmWieldingHero)
    quest13= Quest.GetQuestState(newBegginings)
    # NPC
    athena_id                 = 1209000
    lost_kid_id               = athena_id + 6
    lilin_id                  = 1202000
    lilin_town_id             = 1201000
    puka_id                   = lilin_id + 1
    puen_id                   = lilin_id + 2
    puir_id                   = lilin_id + 3
    purun_id                  = lilin_id + 4
    putzki_id                 = lilin_id + 5
    polearm_id                = 1201001

    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    pet = Inventory.FindItemByID(2434265)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)
    if field_id == black_road:

        Terminal.Rush(field_id + 100)
        time.sleep(1)

    elif field_id == black_road + 100:
        ToggleKami(False)
        TeleportToNPC(athena_id, 1)
        Character.TalkToNpc(athena_id)
        time.sleep(1)
        Quest.StartQuest(find_the_lost_kid, athena_id)
        time.sleep(1)
        ToggleKami(True)
        Terminal.Rush(field_id + 200)

    elif field_id == black_road + 300:

        Quest.StartQuest(find_the_lost_kid, lost_kid_id)
        time.sleep(1)

    elif field_id == black_road + 500:
        ToggleKami(False)
        TeleportToNPC(athena_id + 7, 1)
        Quest.CompleteQuest(find_the_lost_kid + 1, athena_id + 7)
        ToggleKami(True)

    elif field_id == snow_island:
        ToggleKami(False)
        TeleportToNPC(lilin_id, 1)
        Character.TalkToNpc(lilin_id)
        ToggleKami(True)

    elif field_id == snow_island + 100:
        Quest.StartQuest(return_of_the_hero, puka_id)
        if Quest.CheckCompleteDemand(return_of_the_hero, puka_id) != 0:
            Inventory.UseItem(2000022)
            time.sleep(2)
            Quest.CompleteQuest(return_of_the_hero, puka_id)
            time.sleep(2)
            Terminal.Rush(field_id + 100)

    elif field_id == snow_island + 200:
        Quest.StartQuest(the_missing_weapon, puen_id)
        time.sleep(1)
        if Quest.CheckCompleteDemand(the_missing_weapon, puir_id) == 0:
            Quest.CompleteQuest(the_missing_weapon, puir_id)
            time.sleep(1)
            Terminal.Rush(field_id + 100)

    elif field_id == snow_island + 300:
        Quest.StartQuest(abilities_lost, purun_id)
        time.sleep(1)
        Inventory.SendChangeSlotPositionRequest(1, 1, -11, -1)
        if Quest.GetQuestState(abilities_lost) != 2:
            mob = Field.FindMob(9300383)
            if mob.valid:
                ToggleKami(True)
            else:
                ToggleKami(False)

        elif Quest.GetQuestState(abilities_lost) == 2:
            time.sleep(1)
            Terminal.Rush(field_id + 100)

    elif field_id == snow_island + 400:
        if Quest.GetQuestState(gift_for_the_hero) == 0:
            putzki = Field.FindNpc(putzki_id)
            time.sleep(1)
            if pos.x != putzki.x:
                ToggleKami(False)
                Character.Teleport(putzki.x, putzki.y)
            time.sleep(1)
            Quest.StartQuest(gift_for_the_hero, putzki_id)

        else:
            box = Field.FindReactor(1402000)
            ToggleKami(False)
            if box.valid and Quest.CheckCompleteDemand(gift_for_the_hero, putzki_id) != 0:
                time.sleep(1)
                if pos.x != box.x:
                    Character.Teleport(box.x, box.y)
                time.sleep(1)
                Autism()
                bamboo = Field.FindItem(4032309)
                wood   = Field.FindItem(4032310)
                if bamboo.valid or wood.valid:
                    Character.Teleport(bamboo.x, bamboo.y)
                    time.sleep(2)            
                    Character.LootItem()    
                    time.sleep(2)            
                    Character.Teleport(wood.x, wood.y)    
                    time.sleep(2)
                    Character.LootItem()

            if Quest.CheckCompleteDemand(gift_for_the_hero, putzki_id) == 0:
                putzki = Field.FindNpc(putzki_id)
                time.sleep(1)
                if pos.x != putzki.x:
                    Character.Teleport(putzki.x, putzki.y)
                time.sleep(1)
                Quest.CompleteQuest(gift_for_the_hero, putzki_id)
                time.sleep(1)
                Terminal.Rush(snow_island - 90000)
    elif field_id == 140090500:
        DungeonTeleport()
    elif field_id == 140010000:
        TeleportEnter(-101,86)

    elif field_id == snow_island - 90000:
        #if pos.x != -208:
        #    ToggleKami(False)
        #    Character.Teleport(-208, 86)
        if Quest.GetQuestState(lilins_account) == 0:
            time.sleep(1)          
            Quest.StartQuest(lilins_account, lilin_town_id)
        if Quest.GetQuestState(lilins_account) == 1:
            time.sleep(1)
            Npc.ClearSelection()
            time.sleep(1)
            Npc.RegisterSelection("Black Mage")
            time.sleep(1)
            Npc.RegisterSelection("Sealed away the Black Mage")
            time.sleep(1)
            Quest.CompleteQuest(lilins_account, lilin_town_id)
    if quest7 != 2:
        if quest7 == 0:
            acceptQuest(basic_fitness_training_1,lilin_town_id,rien,field_id)
        elif quest7 == 1:
            completeQuest(basic_fitness_training_1,lilin_town_id,rien,snowcoveredfield1,field_id)
    elif quest8 != 2:
        if quest8 == 0:
            acceptQuest(basic_fitness_training_2,lilin_town_id,rien,field_id)
        elif quest8 == 1:
            completeQuest(basic_fitness_training_2,lilin_town_id,rien,snowcoveredfield2,field_id)
    elif quest9 != 2:
        print("9")
        if quest9 == 0:
            acceptQuest(basic_fitness_training_3, lilin_town_id, rien, field_id)
        elif quest9 == 1:
            completeQuest(basic_fitness_training_3, lilin_town_id, rien,snowcoveredfield3,field_id)
    elif quest10 != 2:
        print("10")
        if quest10 == 0:
            acceptQuest(basic_fitness_test, lilin_town_id, rien, field_id)
        elif quest10 == 1:
            completeQuest(basic_fitness_test, lilin_town_id, rien,dangerousforest,field_id)
    elif quest11 != 2:
        if quest11 == 0:
            acceptQuest(the_five_heroes,lilin_town_id,rien,field_id)
    elif quest12 != 2:
        if quest12 == 0:
            acceptQuest(thePolearmWieldingHero,polearm_id,rien,field_id)
    elif quest13 != 2:
        if quest13 == 0:
            acceptQuest(newBegginings,lilin_town_id,rien,field_id)
    
def AranSecondJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    InSearchOfIts = 21200
    MirrorOfDesire = 21201
    BlackSmith = 21202
    Lilin   = 1201000
    polearm = 1201001
    Maha = 1201002
    sirBlackSmith = 1203000
    quest1 = Quest.GetQuestState(InSearchOfIts)
    quest2 = Quest.GetQuestState(MirrorOfDesire)
    quest3 = Quest.GetQuestState(BlackSmith)
    Rien = 140000000
    mirrorcave = 140030000
    headblacksmithshop = 914021000
    outside = 914021010
    if quest1 != 2:
        if quest1 == 0:
            acceptQuest(InSearchOfIts,Lilin,Rien,field_id)
        elif quest1 == 1:
            completeQuest(InSearchOfIts,Maha,Rien,Rien,field_id)
    elif quest2 !=2:
        if quest2 == 0:
            acceptQuest(MirrorOfDesire,Lilin,Rien,field_id)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(MirrorOfDesire,Maha) != 0:
                if field_id != mirrorcave and field_id != headblacksmithshop and field_id != outside:
                    RushTo(mirrorcave)
                elif field_id == mirrorcave:
                    TeleportEnter(-7,122)
                elif quest3 != 2:
                    if quest3 == 0:
                        acceptQuest(BlackSmith,sirBlackSmith,headblacksmithshop,field_id)
                    elif quest3 ==1:
                        if Quest.CheckCompleteDemand(BlackSmith,sirBlackSmith) != 0:
                            if field_id == headblacksmithshop:
                                TeleportEnter(-1301,363)
                            else:
                                ToggleKami(True)
                                ToggleAttackQuest(True)
                        elif Quest.CheckCompleteDemand(BlackSmith,sirBlackSmith) == 0:
                            if field_id != headblacksmithshop:
                                DungeonTeleport()
                            else:
                                completeQuest(BlackSmith,sirBlackSmith,headblacksmithshop,headblacksmithshop,field_id)
            elif Quest.CheckCompleteDemand(MirrorOfDesire,Maha) == 0:
                if field_id in range(headblacksmithshop,headblacksmithshop+10):
                    TeleportEnter(839,543)
                else:
                    completeQuest(MirrorOfDesire,Maha,Rien,Rien,field_id)

def AranThirdJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    WeaponNeverLeavesItsOwner = 21300
    CatchThatThief = 21301
    MakingRedJade = 21302
    FriendshipWithYeti = 21303

    Lilin   = 1201000
    polearm = 1201001
    Maha = 1201002
    sirBlackSmith = 1203000
    Tititi = 1203001

    quest1 = Quest.GetQuestState(WeaponNeverLeavesItsOwner)
    quest2 = Quest.GetQuestState(CatchThatThief)
    quest3 = Quest.GetQuestState(MakingRedJade)
    quest4 = Quest.GetQuestState(FriendshipWithYeti)
    Rien = 140000000
    PenguinPort = 140020300
    crowmap = 914022000
    mirrorcave = 140030000
    razorsharpcliff = 914022100
    headblacksmithshop = 914021000
    outside = 914022200
    if quest1 != 2:
        if quest1 == 0:
            acceptQuest(WeaponNeverLeavesItsOwner,Lilin,Rien,field_id)
        elif quest1 == 1:
            completeQuest(WeaponNeverLeavesItsOwner,Maha,Rien,Rien,field_id)
    elif quest2 != 2:
        if quest2 == 0:
            acceptQuest(CatchThatThief,Maha,Rien,field_id)
        elif quest2 == 1:
            ToggleHtr(False)
            completeQuest(CatchThatThief,Maha,Rien,PenguinPort,field_id)
            if field_id == crowmap and len(Field.GetMobs()) == 0:
                DungeonTeleport()
                ToggleHtr(True)
    elif quest3 != 2:
        if quest3 == 0:
            acceptQuest(MakingRedJade,Lilin,Rien,field_id)
        elif quest3 == 1:
            if Quest.CheckCompleteDemand(MakingRedJade,Maha) != 0:
                if field_id != mirrorcave and field_id != razorsharpcliff and field_id != outside:
                    RushTo(mirrorcave)
                elif field_id == mirrorcave:
                    TeleportEnter(-7,122)
                elif quest4 != 2:
                    print("4")
                    if quest4 == 0:
                        print("accept")
                        acceptQuest(FriendshipWithYeti,Tititi,razorsharpcliff,field_id)
                    elif quest4 ==1:
                        print("Do")
                        if Quest.CheckCompleteDemand(FriendshipWithYeti,Tititi) != 0:
                            if field_id == razorsharpcliff:
                                TeleportEnter(-211,454)
                            else:
                                ToggleKami(True)
                                ToggleAttackQuest(True)
                                ToggleLoot(True)
                        elif Quest.CheckCompleteDemand(FriendshipWithYeti,Tititi) == 0:
                            if field_id != razorsharpcliff:
                                DungeonTeleport()
                                ToggleLoot(False)
                            else:
                                completeQuest(FriendshipWithYeti,Tititi,razorsharpcliff,razorsharpcliff,field_id)
            elif Quest.CheckCompleteDemand(MakingRedJade,Maha) == 0:
                print("Done")
                if field_id in range(razorsharpcliff,razorsharpcliff+10):
                    TeleportEnter(-271,-197)
                else:
                    completeQuest(MakingRedJade,Maha,Rien,Rien,field_id)

def AranFourthJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    AWeaponFightsOwner = 21400
    TrainingThePolearm = 21401
    Lilin   = 1201000
    polearm = 1201001
    Maha = 1201002
    sirBlackSmith = 1203000
    Tititi = 1203001

    quest1 = Quest.GetQuestState(AWeaponFightsOwner)
    quest2 = Quest.GetQuestState(TrainingThePolearm)

    Rien = 140000000
    PenguinPort = 140020300
    crowmap = 914022000
    mirrorcave = 140030000
    
    if quest1 != 2:
        print("1")
        if quest1 == 0:
            acceptQuest(AWeaponFightsOwner,Lilin,Rien,field_id)
        elif quest1 == 1:
            completeQuest(AWeaponFightsOwner,Maha,Rien,Rien,field_id)
    elif quest2 !=2:
        print('2')
        if quest2 == 0:
            acceptQuest(TrainingThePolearm,Maha,Rien,field_id)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(TrainingThePolearm,Maha) == 0:
                if field_id != Rien:
                    DungeonTeleport()
                else:
                    completeQuest(TrainingThePolearm,Maha,Rien,Rien,field_id)
            else:
                if len(Field.GetMobs())>0 or field_id == 914020000:
                    ToggleKami(True)
        if quest2 == 1 and field_id != 914020000 and Quest.CheckCompleteDemand(TrainingThePolearm,Maha) != 0:
            ForfeitQuest(TrainingThePolearm)
            time.sleep(2)

def ExplorerFirstJobAdv():
    print("Doing explorer job adv")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    pet = Inventory.FindItemByID(2434265)
    if pet.valid and not SCLib.GetVar("Cannoneer"):
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)
    if SCLib.GetVar("Cannoneer"):
        CannoneerFirstJobAdv()
    elif SCLib.GetVar("DualBlade"):
        DualbladeFirstJobAdv()
    else:
        if Field.GetID() == 4000011:
            ToggleKami(False)
            ToggleAttackQuest(False)
            TeleportEnter(1106,545)
        if Field.GetID() == 4000012:
            Npc.ClearSelection()
            Npc.RegisterSelection("I don't need you, Mai! (Skip tutorial and teleport straight to town.)")
            Character.TalkToNpc(10301)
            time.sleep(5)
            
        if Character.GetLevel() == 2:
            ToggleKami(False)
            if Field.GetID() == 4000020:
                Character.Teleport(1614 ,154)
                time.sleep(5)
                Character.TalkToNpc(10304)
                time.sleep(3)
                Character.TalkToNpc(10304)
        if Character.GetLevel() == 3:
            ToggleKami(False)
            if Field.GetID() == 4000020:
                TeleportEnter(2197,274)
        if Field.GetID() == 4000021:
            ToggleKami(False)
            TeleportEnter(683,215)
        if Field.GetID() == 4000026:
            ToggleKami(False)
            TeleportEnter(765,215)
        if Character.GetLevel() ==3:
            ToggleKami(False)
            if Field.GetID() == 4000030:
                TeleportEnter(2506,287)     
        if Field.GetID() == 4000031:
            ToggleKami(False)
            if Character.GetLevel() ==3:
                Character.Teleport(1962, 407)
                time.sleep(5)
                Quest.CompleteQuest(32211, 10305)
        if Character.GetLevel() ==4:
            ToggleKami(False)
            Quest.StartQuest(32212, 10305)
            time.sleep(5)
            Quest.CompleteQuest(32212, 10306)
        if Character.GetLevel() ==5:
            ToggleKami(False)
            Quest.StartQuest(32213, 10306)
            if Quest.GetQuestState(32213) == 1:
                if Field.GetID() == 4000031:
                    TeleportEnter(34,527)
            if Field.GetID() == 4000030:
                if not Inventory.FindItemByID(4033914).valid:
                    if pos.x != 1895:
                        Character.Teleport(1895 ,407)
                    time.sleep(2)
                    Character.BasicAttack()
                    item = Field.FindItem(4033914)
                    if item.valid:
                        Character.Teleport(item.x, item.y)
                        Terminal.SetCheckBox("Auto Loot", True)
                if Inventory.FindItemByID(4033914).valid:
                    if Field.GetID() == 4000030:
                        Terminal.SetCheckBox("Auto Loot", False)
                        TeleportEnter(2506,287)  
                        Terminal.SetCheckBox("Auto Loot", True)
            
        if Character.GetLevel() == 6:
            if Field.GetID() == 4000030:
                TeleportEnter(2506,282)
            if Field.GetID() == 4000031:
                Character.Teleport(1835, 407)
                time.sleep(5)
                Quest.StartQuest(32214, 10305)
                if Quest.GetQuestState(32214) ==1:
                    Character.EnterPortal()
                
            KillMano()
        if Character.GetLevel() == 7:
            Warrior = 0
            Magician = 1
            Bowman = 2
            Thief = 3
            Pirate = 4
            if "Shadower" not in accountData['done_links'] or "Night Lord" not in accountData['done_links']:
                desired_job = Thief
            elif "Hero" not in accountData['done_links'] or "Dark Knight" not in accountData['done_links'] or "Paladin" not in accountData['done_links']:
                desired_job = Warrior
            elif "Ice/Lightning Archmage" not in accountData['done_links'] or "Fire/Poison Archmage" not in accountData['done_links'] or "Bishop" not in accountData['done_links']:
                desired_job = Magician
            elif "Marksman" not in accountData['done_links'] or "Bowmaster" not in accountData['done_links']:
                desired_job = Bowman
            elif "Corsair" not in accountData['done_links'] or "Buccaneer" not in accountData['done_links']:
                desired_job = Pirate

            if desired_job == 0:
                desired_job_text = "powerful"
            elif desired_job == 1:
                desired_job_text = "intelligent"
            elif desired_job == 2:
                desired_job_text = "long-ranged"
            elif desired_job == 3:
                desired_job_text = "speedy"
            elif desired_job == 4:
                desired_job_text = "fancy"
            Npc.ClearSelection()
            Npc.RegisterSelection(desired_job_text)
            Character.TalkToNpc(10307)
            time.sleep(5)
            Quest.StartQuest(32216, 10306)
            time.sleep(5)
        if Character.GetLevel() == 10:
            if Field.GetID() == 120000101:
                Quest.StartQuest(1405, 1090000)
                SCLib.UpdateVar("DoingJobAdv",False)
            if Field.GetID() == 100000201:
                Quest.StartQuest(1403, 1012100)
                SCLib.UpdateVar("DoingJobAdv",False)
            if Field.GetID() == 102000003:
                Quest.StartQuest(1401, 1022000)
                SCLib.UpdateVar("DoingJobAdv",False)
            if Field.GetID() == 103000003:
                Quest.StartQuest(1404, 1052001)
                SCLib.UpdateVar("DoingJobAdv",False)
            if Field.GetID() == 101000003:
                Quest.StartQuest(1402, 1032001)
                SCLib.UpdateVar("DoingJobAdv",False)
            time.sleep(3)
            if Character.GetJob() !=0:
                ToggleRushByLevel(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleLoot(False)
                print("Resume rush by level; explorer first")

def ExplorerSecondJobAdv():
    print("Explorer 2")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    Terminal.SetCheckBox("Auto Loot",True)
    thiefQuest = 1421
    warriorQuest = 1410
    fighterQuest = 1411
    pageQuest = 1412
    spearmanQuest = 1413
    mageQuest = 1414
    ILwizardQuest = 1416
    FPwizardQuest = 1415
    clericQuest = 1417
    archerQuest = 1418
    pirateQuest = 1424
    brawlerQuest = 1425
    gunslingerQuest = 1426
    cannoneerQuest = 1427
    cannoneerQuest2 = 1428
    hunterQuest = 1419
    crossbowmanQuest = 1420
    assassinQuest = 1422
    banditQuest = 1423

    thiefInstructor = 1052001
    warriorInstructor = 1022000
    mageInstructor = 1032001
    archerInstructor = 1012100
    pirateInstructor = 1090000
    cannoneerInstructor = 1096006
    thiefMap = 103000003
    warriorMap = 102000003
    mageMap = 101000003
    archerMap = 100000201
    pirateMap = 120000101
    thiefMap2= 910370000 #103050310
    warriorMap2 = 910230000
    mageMap2 = 910140000
    archerMap2 = 910070000
    pirateMap2 = 912040000
    hunting_maps = [thiefMap2,warriorMap2,mageMap2,archerMap2,pirateMap2]

    done_list = accountData['done_links']
    if job == ShadowerJobs[0]:
        if "Shadower" not in done_list:
            targetJob = banditQuest
        elif "Night Lord":
            targetJob = assassinQuest
        Instructor = thiefInstructor
        toGoMap = thiefMap
        toDoQuest = thiefQuest
    elif job == HeroJobs[0]:
        if "Hero" not in done_list:
            targetJob = fighterQuest
        elif "Paladin" not in done_list:
            targetJob = pageQuest
        elif "Dark Knight" not in done_list:
            targetJob = spearmanQuest
        Instructor = warriorInstructor
        toGoMap = warriorMap
        toDoQuest = warriorQuest
    elif job == ILMageJobs[0]:
        if "Ice/Lightning Archmage" not in done_list:
            targetJob = ILwizardQuest
        elif "Fire/Poison Archmage" not in done_list:
            targetJob = FPwizardQuest
        elif "Bishop" not in done_list:
            targetJob = clericQuest
        Instructor = mageInstructor
        toGoMap = mageMap
        toDoQuest = mageQuest
    elif job == BowmasterJobs[0]:
        if "Bowmaster" not in done_list:
            targetJob = hunterQuest
        elif "Marksman" not in done_list:
            targetJob = crossbowmanQuest
        Instructor = archerInstructor
        toGoMap = archerMap
        toDoQuest = archerQuest
    elif job == CorsairJobs[0]:
        if "Corsair" not in done_list:
            targetJob = gunslingerQuest
        elif "Buccaneer" not in done_list:
            targetJob = brawlerQuest
        Instructor = pirateInstructor
        toGoMap = pirateMap
        toDoQuest = pirateQuest
    elif job == CannoneerJobs[0]:
        targetJob = pirateQuest
        Instructor = pirateInstructor
        toGoMap = pirateMap
        toDoQuest = cannoneerQuest
    quest = Quest.GetQuestState(toDoQuest)
    quest2= Quest.GetQuestState(targetJob)

    pet = Inventory.FindItemByID(2434265)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)

    if job == 501:
        quest2 = Quest.GetQuestState(cannoneerQuest2)
        if quest != 2:
            if quest == 0:
                acceptQuest(toDoQuest,cannoneerInstructor,toGoMap,field_id)
            elif quest == 1:
                completeQuest(toDoQuest,Instructor,toGoMap,toGoMap,field_id)
        elif quest2 !=2:
            #print("2")
            if quest2 == 0:
                acceptQuest(cannoneerQuest2,Instructor,toGoMap,field_id)
                time.sleep(2)
            elif quest2 == 1:
                print(Inventory.FindItemByID(4031013).count)
                if Quest.CheckCompleteDemand(cannoneerQuest2,Instructor) == 0 or Inventory.FindItemByID(4031013).count >= 30:
                    print("Done")
                    if field_id != toGoMap:
                        print("Need to teleport")
                        ToggleKami(False)
                        DungeonTeleport()
                        time.sleep(1)
                        completeQuest(cannoneerQuest2,Instructor,toGoMap,toGoMap,field_id)
                    elif field_id == toGoMap:
                        completeQuest(cannoneerQuest2,Instructor,toGoMap,toGoMap,field_id)
                        SCLib.UpdateVar("DoingJobAdv",False)
                        ToggleRushByLevel(True)
                        print("Resume rush by level; cannoneer first")
                else:
                    if len(Field.GetMobs()) > 0:
                        ToggleKami(True)
                        print("not done")
                    elif field_id != pirateMap2:
                        ForfeitQuest(cannoneerQuest2)
                        print("Not in map, need to forfeit quest")
    if job in explorerFirstJobs:
        if quest != 2:
            if quest == 0:
                acceptQuest(toDoQuest,Instructor,toGoMap,field_id)
            elif quest == 1:
                completeQuest(toDoQuest,Instructor,toGoMap,toGoMap,field_id)
        elif quest2 !=2:
            #print("2")
            if quest2 == 0:
                acceptQuest(targetJob,Instructor,toGoMap,field_id)
                time.sleep(2)
            elif quest2 == 1:
                print(Inventory.FindItemByID(4031013).count)
                if Quest.CheckCompleteDemand(targetJob,Instructor) == 0 or Inventory.FindItemByID(4031013).count >= 30:
                    print("Done")
                    if field_id != toGoMap:
                        print("Need to teleport")
                        ToggleKami(False)
                        DungeonTeleport()
                        time.sleep(1)
                        completeQuest(targetJob,Instructor,toGoMap,toGoMap,field_id)
                    elif field_id == toGoMap:
                        completeQuest(targetJob,Instructor,toGoMap,toGoMap,field_id)
                        SCLib.UpdateVar("DoingJobAdv",False)
                        ToggleRushByLevel(True)
                        print("Resume rush by level; explorer second -> first")
                        ToggleLoot(False)
                else:
                    if len(Field.GetMobs()) > 0:
                        ToggleKami(True)
                        print("not done")
                    elif field_id not in hunting_maps:
                        ForfeitQuest(targetJob)
                        print("Not in map, need to forfeit quest")

def ExplorerThirdJobAdv():
    print("Explorer 3")
    SCLib.UpdateVar("DoingJobAdv",True)
    ToggleRushByLevel(False)
    CheifsResidence = 211000001
    WarriorChief = 2020008
    MagicianChief = 2020009
    BowmanChief = 2020010
    ThiefChief = 2020011
    PirateChief = 2020013

    warriorQuest = 1430
    fighterQuest = 1431
    pageQuest = 1432
    spearmanQuest = 1433
    mageQuest = 1434
    ILwizardQuest = 1436
    FPwizardQuest = 1435
    clericQuest = 1437
    archerQuest = 1438
    hunterQuest = 1439
    crossbowmanQuest = 1440
    thiefQuest = 1441
    assassinQuest= 1442
    banditQuest = 1443
    pirateQuest = 1444
    gunslingerQuest = 1446
    brawlerQuest = 1445
    dualbladeQuest = 1447
    cannoneerQuest = 1448


    thiefInstructor = 1052001
    warriorInstructor = 1022000
    mageInstructor = 1032001
    archerInstructor = 1012100
    pirateInstructor = 1090000
    thiefMap = 103000003
    warriorMap = 102000003
    mageMap = 101000003
    archerMap = 100000201
    pirateMap = 120000101

    el_nath_map = 211040401
    HolyStone = 2030006
    SparklingCrystal = 1061010
    RadiantCrystalPassageway = 910540000
    DimensionalWorld = [x for x in range(910540000,910540600)]
    

    if job in NightlordJobs:
        toDoQuest = thiefQuest
        toDoQuest2 = assassinQuest
        Instructor = thiefInstructor
        Chief = ThiefChief
        toGoMap = thiefMap
    elif job in ShadowerJobs:
        toDoQuest = thiefQuest
        toDoQuest2 = banditQuest
        Instructor = thiefInstructor
        Chief = ThiefChief
        toGoMap = thiefMap
    elif job in HeroJobs:
        toDoQuest = warriorQuest
        toDoQuest2 = fighterQuest
        Instructor = warriorInstructor
        Chief = WarriorChief
        toGoMap = warriorMap
    elif job in PaladinJobs:
        toDoQuest = warriorQuest
        toDoQuest2 = pageQuest
        Instructor = warriorInstructor
        Chief = WarriorChief
        toGoMap = warriorMap
    elif job in DarkknightJobs:
        toDoQuest = warriorQuest
        toDoQuest2 = spearmanQuest
        Instructor = warriorInstructor
        Chief = WarriorChief
        toGoMap = warriorMap
    elif job in ILMageJobs:
        toDoQuest = mageQuest
        toDoQuest2 = ILwizardQuest
        Instructor = mageInstructor
        Chief = MagicianChief
        toGoMap = mageMap
    elif job in FPMageJobs:
        toDoQuest = mageQuest
        toDoQuest2 = FPwizardQuest
        Instructor = mageInstructor
        Chief = MagicianChief
        toGoMap = mageMap
    elif job in BishopJobs:
        toDoQuest = mageQuest
        toDoQuest2 = clericQuest
        Instructor = mageInstructor
        Chief = MagicianChief
        toGoMap = mageMap
    elif job in BowmasterJobs:
        toDoQuest = archerQuest
        toDoQuest2 = hunterQuest
        Instructor = archerInstructor
        Chief = BowmanChief
        toGoMap = archerMap
    elif job in MarksmanJobs:
        toDoQuest = archerQuest
        toDoQuest2 = crossbowmanQuest
        Instructor = archerInstructor
        Chief = BowmanChief
        toGoMap = archerMap
    elif job in BuccaneerJobs:
        toDoQuest = pirateQuest
        toDoQuest2 = brawlerQuest
        Instructor = pirateInstructor
        Chief = PirateChief
        toGoMap = pirateMap
    elif job in CorsairJobs:
        toDoQuest = pirateQuest
        toDoQuest2 = gunslingerQuest
        Instructor = pirateInstructor
        Chief = PirateChief
        toGoMap = pirateMap
    elif job in CannoneerJobs:
        toDoQuest = pirateQuest
        toDoQuest2 = cannoneerQuest
        Instructor = pirateInstructor
        Chief = PirateChief
        toGoMap = pirateMap
    elif job in DualbladeJobs:
        toDoQuest = thiefQuest
        toDoQuest2 = dualbladeQuest
        Instructor = thiefInstructor
        Chief = ThiefChief
        toGoMap = thiefMap
    quest = Quest.GetQuestState(toDoQuest)
    quest2= Quest.GetQuestState(toDoQuest2)
    if quest != 2:
        print("1")
        if quest == 0:
            acceptQuest(toDoQuest,Instructor,toGoMap,field_id)
        elif quest == 1:
            completeQuest(toDoQuest,Chief,CheifsResidence,CheifsResidence,field_id)
    elif quest2 != 2:
        print("2")
        if quest2 == 0:
            acceptQuest(toDoQuest2,Chief,CheifsResidence,field_id)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(toDoQuest2,Chief) == 0:
                if field_id in DimensionalWorld:
                    mobs = Field.GetMobs()
                    print("Still in dimensional world")
                    if len(mobs) == 0:
                        Character.TalkToNpc(SparklingCrystal)
                        ToggleLoot(False)
                else:
                    print("Completing quest")
                    completeQuest(toDoQuest2,Chief,CheifsResidence,CheifsResidence,field_id)
                    time.sleep(3)
                    if Quest.GetQuestState(toDoQuest2) == 2:
                        SCLib.UpdateVar("DoingJobAdv",False)
                        ToggleRushByLevel(True)
                        print("Resume rush by level; explorer third")
            elif field_id == el_nath_map:
                print("talk to holy stone")
                if pos.x != 27 and pos.y != 454:
                    ToggleKami(False)
                    Character.Teleport(27, 454)
                    time.sleep(3)
                Character.TalkToNpc(HolyStone)
            elif field_id == RadiantCrystalPassageway:
                print("In passage way")
                DungeonTeleport()
                DungeonTeleport()
                DungeonTeleport()
            elif field_id in DimensionalWorld:
                print("In demensional world")
                mobs = Field.GetMobs()
                ToggleAttackQuest(True)
                ToggleLoot(True)
                if len(mobs) == 0:
                    if pos.x != 692:
                        ToggleKami(False)
                        Character.Teleport(692,-456)
                        ToggleLoot(False)
                    else:
                        Character.TalkToNpc(SparklingCrystal)
                        ToggleLoot(False)
                else:
                    ToggleKami(True)
                    ToggleAttackQuest(True)
            elif field_id != 211040300:
                print("Rushing there")
                RushTo(211040300)
                time.sleep(3)
            elif field_id == 211040300:
                ToggleAttackQuest(False)
                TeleportEnter(31,454)
                time.sleep(1)
                TeleportEnter(31,454)
                TeleportEnter(31,454)
    
    if Quest.GetQuestState(toDoQuest2) == 2:
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleRushByLevel(True)
        print("Explorer third job done")

def ExplorerFourthJobAdv():
    print("Explorer 4")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    #3rd job instructors
    warriorInstructor = 2020008
    mageInstructor = 2020009
    archerInstructor = 2020010
    thiefInstructor = 2020011
    pirateInstructor = 2020013

    #4th job instructors
    thiefChief = 2081400
    warriorChief = 2081100
    mageChief = 2081200
    archerChief = 2081300
    pirateChief = 2081500
    
    #quests
    warriorQuest = 1450
    warriorQuest2 = 1451
    mageQuest = 1452
    mageQuest2 = 1453
    archerQuest = 1454
    archerQuest2 = 1455
    thiefQuest = 1456
    thiefQuest2 = 1457
    pirateQuest = 1458
    pirateQuest2 = 1459

    #maps
    ForestOfThePriest = 240010501
    ManonForest = 924000200
    GriffeyForest = 924000201
    if job in NightlordJobs or job in ShadowerJobs or job in DualbladeJobs:
        toDoQuest = thiefQuest
        toDoQuest2 = thiefQuest2
        Instructor = thiefInstructor
        Chief = thiefChief
    elif job in HeroJobs or job in PaladinJobs or job in DarkknightJobs:
        toDoQuest = warriorQuest
        toDoQuest2 = warriorQuest2
        Instructor = warriorInstructor
        Chief = warriorChief
    elif job in ILMageJobs or job in FPMageJobs or job in BishopJobs:
        toDoQuest = mageQuest
        toDoQuest2 = mageQuest2
        Instructor = mageInstructor
        Chief = mageChief
    elif job in BowmasterJobs or job in MarksmanJobs:
        toDoQuest = archerQuest
        toDoQuest2 = archerQuest2
        Instructor = archerInstructor
        Chief = archerChief
    elif job in CorsairJobs or job in BuccaneerJobs or job in CannoneerJobs:
        toDoQuest = pirateQuest
        toDoQuest2 = pirateQuest2
        Instructor = pirateInstructor
        Chief = pirateChief

    quest = Quest.GetQuestState(toDoQuest)
    quest2 = Quest.GetQuestState(toDoQuest2)

    star = 4031344
    star2 = 4031512
    pentagon= 4031343
    pentagon2 = 4031511
    pentagon3 = 4031514
    pentagon4 = 4031517
    pentagon5 = 4031860
    pentagon_loot = 4031517
    star_loot = 4031518
    if Terminal.GetCheckBox("filter_etc"):
        Terminal.SetCheckBox("filter_etc",False)
    if Terminal.GetCheckBox("filter_use"):
        Terminal.SetCheckBox("filter_use",False)
    if quest != 2:
        if quest == 0:
            acceptQuest(toDoQuest,Instructor,field_id,field_id)
        elif quest == 1:
            completeQuest(toDoQuest,Chief,ForestOfThePriest,ForestOfThePriest,field_id)
    elif quest2 != 2:
        if quest2 == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection("Manon")
            acceptQuest(toDoQuest2,Chief,ForestOfThePriest,field_id)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(toDoQuest2,Chief) == 0:
                print("Done")
                ToggleLoot(False)
                if field_id == ManonForest or field_id == GriffeyForest:
                    DungeonTeleport()
                else:
                    ToggleHtr(True)
                    completeQuest(toDoQuest2,Chief,ForestOfThePriest,ForestOfThePriest,field_id)
                time.sleep(3)
                if Character.GetJob() in explorerFourthJobs:
                    SCLib.UpdateVar("DoingJobAdv",False)
                    ToggleRushByLevel(True)
                    print("Resume rush by level; explorer fourth")
            elif not (Inventory.FindItemByID(pentagon).count >= 1 or Inventory.FindItemByID(pentagon2).count >= 1 or Inventory.FindItemByID(pentagon3).count >= 1 or Inventory.FindItemByID(pentagon4).count >= 1 or Inventory.FindItemByID(pentagon5).count >= 1):
                print("Hunt for pentagon")
                if field_id == GriffeyForest:
                    DungeonTeleport()
                if field_id != ManonForest:
                    ToggleHtr(False)
                    RushTo(ManonForest)
                    time.sleep(1)
                else:
                    ToggleLoot(True)
                    loot = Field.FindItem(pentagon_loot)
                    time.sleep(2)
                    if not loot.valid:
                        time.sleep(5)
                        ToggleAttackQuest(True)
                        ToggleKami(True)
                        mobs = Field.GetMobs()
                        if len(mobs) == 0 and not Field.FindItem(pentagon_loot).valid:
                            Terminal.SetCheckBox("timedCCCheck",True)
                            time.sleep(1)
                            Terminal.SetCheckBox("timedCCCheck",False)
                    else:
                        ToggleLoot(True)
                        ToggleKami(False)
                        pos = Character.GetPos()
                        if pos.x != loot.x:
                            Character.Teleport(loot.x,loot.y)
                            time.sleep(5)
            elif not (Inventory.FindItemByID(star).count >= 1 or Inventory.FindItemByID(star2).count >= 1):
                print("Hunt for star")
                if field_id == ManonForest:
                    DungeonTeleport()
                if field_id != GriffeyForest:
                    ToggleHtr(False)
                    RushTo(GriffeyForest)
                    time.sleep(1)
                else:
                    time.sleep(2)
                    loot = Field.FindItem(star_loot)
                    ToggleLoot(True)
                    if not loot.valid:
                        time.sleep(5)
                        ToggleAttackQuest(True)
                        ToggleKami(True)
                        mobs = Field.GetMobs()
                        if len(mobs) == 0 and not Field.FindItem(star_loot).valid:
                            Terminal.SetCheckBox("timedCCCheck",True)
                            time.sleep(1)
                            Terminal.SetCheckBox("timedCCCheck",False)
                    else:
                        ToggleLoot(True)
                        ToggleKami(False)
                        pos = Character.GetPos()
                        if pos.x != loot.x:
                            Character.Teleport(loot.x,loot.y)
                            time.sleep(5)

def CygnusFirstJobAdv():
    #map 1
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    ToggleKami(False)

    if field_id == 130030000:
        quest_state = Quest.GetQuestState(20820)
        if quest_state == 0:
            Quest.StartQuest(20820, 1102101)
    #map 2
    elif field_id == 130030100:
        quest1 = Quest.GetQuestState(20821)
        quest2 = Quest.GetQuestState(20822)
        if quest1 != 2:
            if quest1 == 0:
                Quest.StartQuest(20821, 1102101)
            elif quest1 == 1:
                Quest.CompleteQuest(20821, 1102100)
        else:
            if quest2 == 0:
                Quest.StartQuest(20822, 1102100)
            elif quest2 == 1:
                Quest.CompleteQuest(20822, 1102101)
    #map 3
    elif field_id == 130030101:
        quest1 = Quest.GetQuestState(20823)
        quest2 = Quest.GetQuestState(20824)
        quest3 = Quest.GetQuestState(20825)
        quest4 = Quest.GetQuestState(20826)
        quest5 = Quest.GetQuestState(20827)
        if quest1 != 2:
            if quest1 == 0:
                Quest.StartQuest(20823, 1102101)
            elif quest1 == 1:
                Quest.CompleteQuest(20823, 1102101)
        elif quest2 != 2:
            if quest2 == 0:
                Quest.StartQuest(20824, 1102101)
            elif quest2 == 1:
                equip = Inventory.FindItemByID(1003769)
                if equip.valid:
                    Inventory.SendChangeSlotPositionRequest(1, equip.pos, -1, -1)
                elif Character.GetEquippedItemIDBySlot(-1) == 1003769:
                    Quest.CompleteQuest(20824, 1102101)
        elif quest3 != 2:
            if quest3 == 0:
                Quest.StartQuest(20825, 1102103)
            elif quest3 == 1:
                Quest.CompleteQuest(20825, 1102103)
        elif quest4 != 2:
            if quest4 == 0:
                Quest.StartQuest(20826, 1102103)
            elif quest4 == 1:
                Quest.CompleteQuest(20826, 1102112)
        elif quest5 != 2:
            if quest5 == 0:
                Quest.StartQuest(20827, 1102101)
            elif quest5 == 1:
                portal = Field.FindPortal("next00")
                if portal.valid:
                    Character.Teleport(portal.x, portal.y)
                    time.sleep(1)
                    Character.EnterPortal()
                    time.sleep(1)
    #map 4
    elif field_id == 130030102:
        quest1 = Quest.GetQuestState(20827)
        quest2 = Quest.GetQuestState(20828)
        if quest1 != 2:
            Quest.CompleteQuest(20827, 1102114)
        elif quest2 == 0:
            Quest.StartQuest(20828, 1102114)
        elif quest2 == 1:
            Character.Teleport(-2524, -173)
            time.sleep(1)
            Quest.CompleteQuest(20828, 1102101)
    #map 5
    elif field_id == 130030103:
        quest1 = Quest.GetQuestState(20829)
        quest2 = Quest.GetQuestState(20830)
        quest3 = Quest.GetQuestState(20831)
        quest4 = Quest.GetQuestState(20832)
        quest5 = Quest.GetQuestState(20833)
        if quest1 != 2:
            if quest1 == 0:
                Quest.StartQuest(20829, 1102102)
            if quest1 == 1:
                if Quest.CheckCompleteDemand(20829, 1102102) == 0:
                    Quest.CompleteQuest(20829, 1102102)
                else:
                    # kill mobs
                    pos = Character.GetPos()
                    if pos.y >= 29:
                        # move up
                        if pos.x < -430:
                            # move right
                            Character.AMoveX(-430)
                        elif pos.x > -280:
                            # move left
                            Character.AMoveX(-280)
                        else:
                            Character.Jump()
                    else:
                        # move and attack
                        mob = Field.FindMob(9300730)
                        if mob.valid:
                            if pos.x < mob.x:
                                if pos.x < mob.x - 100:
                                    # move right
                                    Character.MoveX(mob.x - 100, 10000)
                                else:
                                    # face right
                                    Character.AMoveX(pos.x + 1)
                            else:
                                if pos.x > mob.x + 100:
                                    # move left
                                    Character.MoveX(mob.x + 100, 10000)
                                else:
                                    # face left
                                    Character.AMoveX(pos.x - 1)
                            Character.BasicAttack()
        elif quest2 != 2:
            if quest2 == 0:
                Quest.StartQuest(20830, 1102101)
            elif quest2 == 1:
                Inventory.UseItem(2001555)
                time.sleep(1)
                Quest.CompleteQuest(20830, 1102101)
        elif quest3 != 2:
            if quest3 == 0:
                Quest.StartQuest(20831, 1102102)
            elif quest3 == 1:
                if Quest.CheckCompleteDemand(20831, 1102102) == 0:
                    Quest.CompleteQuest(20831, 1102102)
                else:
                    pos = Character.GetPos()
                    if pos.y >= 29:
                        # move up
                        if pos.x < -430:
                            # move right
                            Character.AMoveX(-430)
                        elif pos.x > -280:
                            # move left
                            Character.AMoveX(-280)
                        else:
                            Character.Jump()
                    else:
                        # move and attack and pickup
                        dropitem = Field.FindItem(4000489)
                        if dropitem.valid:
                            if pos.x < dropitem.x - 25:
                                # move right
                                Character.MoveX(dropitem.x - 25, 10000)
                            elif pos.x > dropitem.x + 25:
                                # move left
                                Character.MoveX(dropitem.x + 25, 10000)
                            Character.LootItem()
                        else:
                            mob = Field.FindMob(9300730)
                            if mob.valid:
                                if pos.x < mob.x:
                                    if pos.x < mob.x - 100:
                                        # move right
                                        Character.MoveX(mob.x - 100, 10000)
                                    else:
                                        # face right
                                        Character.AMoveX(pos.x + 1)
                                else:
                                    if pos.x > mob.x + 100:
                                        # move left
                                        Character.MoveX(mob.x + 100, 10000)
                                    else:
                                        # face left
                                        Character.AMoveX(pos.x - 1)
                                Character.BasicAttack()
        elif quest4 != 2:
            Quest.StartQuest(20832, 1102102)
        elif quest5 != 2:
            Quest.StartQuest(20833, 1102113)
    elif field_id == 130030104:
        quest1 = Quest.GetQuestState(20833)
        quest2 = Quest.GetQuestState(20834)
        quest3 = Quest.GetQuestState(20835)
        if quest1 != 2:
            Quest.CompleteQuest(20833, 1102113)
        else:
            if quest2 != 2:
                if quest2 == 0:
                    Quest.StartQuest(20834, 1102106)
                elif quest2 == 1:
                    Quest.CompleteQuest(20834, 1102107)
            elif quest3 == 0: 
                Quest.StartQuest(20835, 1102107)
            elif quest3 == 1:
                Quest.CompleteQuest(20835, 1102112)
            elif quest3 == 2:
                Quest.StartQuest(20836, 1102102)
    elif field_id == 130030105:
        quest1 = Quest.GetQuestState(20836)
        quest2 = Quest.GetQuestState(20837)
        if quest1 != 2:
            Quest.CompleteQuest(20836, 1102102)
        elif quest2 == 0:
            Key.Set(0x43, 1, 10001244) # 'C'
            time.sleep(1)
            Quest.StartQuest(20837, 1102102)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(20837, 1102102) == 0:
                Quest.CompleteQuest(20837, 1102102)
            else:
                # kill mobs
                pos = Character.GetPos()
                if pos.y >= 30:
                    # move up
                    if pos.x < -430:
                        # move right
                        Character.AMoveX(-430)
                    elif pos.x > -280:
                        # move left
                        Character.AMoveX(-280)
                    else:
                        Character.Jump()
                else:
                    # move and attack
                    mob = Field.FindMob(9300731)
                    if mob.valid:
                        Character.AMoveX(mob.x)
                        Key.Press(0x43) # 'C'
    elif field_id == 130030106:
        quest1 = Quest.GetQuestState(20838)
        quest2 = Quest.GetQuestState(20839)
        if quest1 == 0:
            Quest.StartQuest(20838, 1102104)
        elif quest1 == 1:
            if Quest.CheckCompleteDemand(20838, 1102104) == 0:
                Quest.CompleteQuest(20838, 1102104)
            else:
                rope_x = 2201
                rope_y = -152
                reactor_x = 1861
                reactor_y = -212
                pos = Character.GetPos()
                if pos.y > rope_y:
                    if pos.x < rope_x:
                        Character.MoveX(rope_x - 50, 10000)
                        Character.Jump()
                        Character.MoveY(rope_y, 2000)
                    elif pos.x > rope_x:
                        Character.MoveX(rope_x + 50, 10000)
                        Character.Jump()
                        Character.MoveY(rope_y, 2000)
                    else:
                        Character.MoveY(rope_y, 10000)
                elif pos.y == rope_y:
                    Character.MoveX(2160, 10000)
                    Character.Jump()
                elif pos.y == reactor_y:
                    if pos.x < reactor_x - 10:
                        Character.MoveX(reactor_x - 10, 10000)
                    elif pos.x > reactor_x + 10:
                        Character.MoveX(reactor_x + 10, 10000)
                    dropitem = Field.FindItem(4033670)
                    if dropitem.valid:
                        if pos.x < dropitem.x - 25:
                            Character.MoveX(dropitem.x - 25, 10000)
                        elif pos.x > dropitem.x + 25:
                            Character.MoveX(dropitem.x + 25, 10000)
                        Character.LootItem()
                    else:
                        Character.BasicAttack()
                else:
                    # ??? reset pls ???
                    Character.MoveX(2600, 20000)
        elif quest2 == 0:
            Quest.StartQuest(20839, 1102100)
        else:
            portal = Field.FindPortal("next00")
            if portal.valid:
                Character.Teleport(portal.x, portal.y)
                time.sleep(1)
                Character.EnterPortal()
                time.sleep(1)
    elif field_id == 130030006:
        portal = Field.FindPortal("west00")
        if portal.valid:
            Character.Teleport(portal.x, portal.y)
            time.sleep(1)
            Character.EnterPortal()
            time.sleep(1)

    elif field_id == 130000000:
        quest1 = Quest.GetQuestState(20839)
        quest2 = Quest.GetQuestState(20860)

        done_list = accountData['done_links']
        
        if "Thunder Breaker" not in done_list:
            targetJobQuest = 20865
            Instructor = 1101007
        elif "Night Walker" not in done_list:
            targetJobQuest = 20864
            Instructor = 1101006
        elif "Blaze Wizard" not in done_list:
            targetJobQuest =  20862
            Instructor = 1101004
        elif "Dawn Warrior" not in done_list:
            targetJobQuest = 20861
            Instructor = 1101003
        elif "Wind Archer" not in done_list:
            targetJobQuest = 20863
            Instructor = 1101005
        quest3 = Quest.GetQuestState(targetJobQuest)
        if quest1 == 1:
            Character.Teleport(189, 88)
            time.sleep(1)
            Quest.CompleteQuest(20839, 1101000)
        elif quest1 == 2:
            if quest2 == 0:
                Quest.StartQuest(20860, 1101002)
            elif quest2 == 1:
                Quest.CompleteQuest(20860, 1101002)

            elif quest2 == 2:
                if quest3 == 0:
                    if Character.GetPos().x != -870:
                        Character.Teleport(-870, 88)
                    time.sleep(1)
                    Quest.StartQuest(targetJobQuest, Instructor)
                elif quest3 == 1:
                    Quest.CompleteQuest(targetJobQuest, Instructor)
                    ToggleRushByLevel(True)
                    SCLib.UpdateVar("DoingJobAdv",False)
                    ToggleKami(True)
                    print("Resume rush by level; cygnus first")

def CygnusSecondJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)

    if job in BlazeWizardJobs:
        targetJobQuest =  20872
        Instructor = 1101004
    elif job in DawnWarriorJobs:
        targetJobQuest = 20871
        Instructor = 1101003
    elif job in WindArcherJobs:
        targetJobQuest = 20873
        Instructor = 1101005
    elif job in NightWalkerJobs:
        targetJobQuest = 20874
        Instructor = 1101006
    elif job in ThunderBreakerJobs:
        targetJobQuest = 20875
        Instructor = 1101007
    quest1 = Quest.GetQuestState(20870)

    quest2 = Quest.GetQuestState(targetJobQuest)
    if quest1 == 0:
        Quest.StartQuest(20870, 1101002)
    elif quest1 == 1:
        if field_id != 130000000:
            Terminal.Rush(130000000)
        else:
            if Character.GetPos().x != -870:
                Character.Teleport(-870, 88)
                time.sleep(1)
            Quest.CompleteQuest(20870, 1101002)
    elif quest2 == 0:
        if field_id != 130000000:
            Terminal.Rush(130000000)
        else:
            if Character.GetPos().x != -870:
                Character.Teleport(-870, 88)
                time.sleep(1)
            Quest.StartQuest(targetJobQuest, Instructor)
    elif quest2 == 1:
        print("2")
        if field_id == 913001000 or field_id == 913001001 or field_id == 913001002:
            if Quest.CheckCompleteDemand(targetJobQuest, Instructor) == 0:
                # leave that map
                Character.TalkToNpc(1102001)
            else:
                # bot should be attacking now and killing mobs cause of the settings inside terminal (fma, flame orb hack auto att, blabla)
                ToggleKami(True)
                time.sleep(1)
        elif field_id == 130020000:
            if Quest.CheckCompleteDemand(targetJobQuest, Instructor) == 0:
                Terminal.Rush(130000000)
            else:
                portal = Field.FindPortal("in01")
                if portal.valid:
                    ToggleKami(False)
                    Character.Teleport(portal.x, portal.y - 20)
                    time.sleep(1)
                    Character.EnterPortal()
        elif field_id == 130000000:
            if Quest.CheckCompleteDemand(targetJobQuest, Instructor) == 0:
                if Character.GetPos().x != -870:
                    ToggleKami(False)
                    Character.Teleport(-870, 88)
                    time.sleep(1)
                Quest.CompleteQuest(targetJobQuest, Instructor)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleKami(True)
                print("Resume rush by level; cygnus second")
            else:
                Terminal.Rush(130020000)
        else:
            if Quest.CheckCompleteDemand(targetJobQuest, Instructor) == 0:
                Terminal.Rush(130000000)
            else:
                Terminal.Rush(130020000)

def CygnusThirdJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    quest1 = Quest.GetQuestState(20880)
    quest2 = Quest.GetQuestState(20881)
    quest3 = Quest.GetQuestState(20882)
    quest4 = Quest.GetQuestState(20883)
    if quest1 != 2:
        print("1")
        if quest1 == 0:
            Quest.StartQuest(20880, 1101002)
        elif quest1 == 1:
            if field_id == 222020100:
                portal = Field.FindPortal("in01")
                if portal.valid:
                    ToggleKami(False)
                    Character.Teleport(portal.x, portal.y-20)
                    time.sleep(1)
                    Character.EnterPortal()
            elif field_id == 222020000:
                Quest.CompleteQuest(20880, 2040052)
            else:
                Terminal.Rush(222020000)
    elif quest2 != 2:
        print("2")
        if quest2 == 0:
            if field_id == 222020000:
                Quest.StartQuest(20881, 2040052)
            else:
                Terminal.Rush(222020000)
        elif quest2 == 1:
            if field_id == 222020000:
                portal = Field.FindPortal("in00")
                if portal.valid:
                    ToggleKami(False)
                    Character.Teleport(portal.x, portal.y-20)
                    time.sleep(1)
                    Character.EnterPortal()
            elif field_id == 922030400:
                Quest.CompleteQuest(20881, 1104302)
            else:
                Terminal.Rush(222020000)
    elif quest3 != 2:
        print("3")
        if quest3 == 0:
            if field_id in range(922030400,922030400+20):
                Quest.StartQuest(20882, 1104302)
            elif field_id == 222020000:
                portal = Field.FindPortal("in00")
                if portal.valid:
                    ToggleKami(False)
                    Character.Teleport(portal.x, portal.y-20)
                    time.sleep(1)
                    Character.EnterPortal()
            else:
                Terminal.Rush(222020000)
        elif quest3 == 1:
            print("doing 3")
            if field_id in range(922030400,922030400+20):
                if Quest.CheckCompleteDemand(20882, 1104303) == 0:
                    Quest.CompleteQuest(20882, 1104303)
                    print("Turn on kill settings")
                    ToggleKami(True)
                else:
                    time.sleep(1) #bot should kill mobs cause of terminal settings
                    ToggleKami(True)
            elif field_id not in range(922030400,922030400+20):
                RushTo(222020000)
                time.sleep(3)
                TeleportEnter(372,-435)
                time.sleep(1)
                ToggleKami(True)
    elif quest4 != 2:
        print("4")
        if quest4 == 0:
            if field_id == 922030400:
                Quest.StartQuest(20883, 1104303)
            elif field_id != 922030400:
                RushTo(922030400)
        elif quest4 == 1:
            if field_id == 130000000:
                Quest.CompleteQuest(20883, 1101002)
            else:
                Terminal.Rush(130000000)

def CygnusFourthJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    quest1 = Quest.GetQuestState(20890)
    quest2 = Quest.GetQuestState(20891)
    quest3 = Quest.GetQuestState(20892)
    quest4 = Quest.GetQuestState(20893)
    quest5 = Quest.GetQuestState(20894)
    if quest1 != 2:
        print('1')
        if quest1 == 0:
            Quest.StartQuest(20890, 1101002)
        elif quest1 == 1:
            if field_id == 913031003:
                Quest.CompleteQuest(20890, 1104300)
    elif quest2 != 2:
        print("2")
        if quest2 == 0:
            ToggleKami(False)
            if Character.GetPos().x != 553:
                Character.Teleport(553,1310)
            time.sleep(1)
            Quest.StartQuest(20891, 1104300)
        elif quest2 == 1:
            if field_id == 913031003:
                Quest.CompleteQuest(20891, 1102112)
    elif quest3 != 2:
        print("3")
        if field_id == 130000000:
            if quest3 == 0:
                Quest.StartQuest(20892, 1101002)
            elif quest3 == 1:
                Quest.CompleteQuest(20892, 1101000)
        else:
            Terminal.Rush(130000000)
    elif quest4 != 2: #913031002
        print("4")
        if quest4 == 0:
            time.sleep(1)
            Quest.StartQuest(20893, 1101000)
        elif quest4 == 1:
            if field_id == 913031002:
                ToggleKami(True)
                print("Waiting for it to be killed")
                Terminal.StopRush()
                time.sleep(3) #let bot kill cygnus boss
            elif field_id == 130000000:
                Quest.CompleteQuest(20893, 1101000)
            elif field_id != 130000000:
                RushTo(130000000)
            else:
                time.sleep(1)
    elif quest5 != 2:
        print("5")
        if quest5 == 0:
            if field_id == 130000000:
                Quest.StartQuest(20894, 1101000)
        elif quest5 == 1:
            Quest.CompleteQuest(20894,1101000)
            time.sleep(1)
            ToggleRushByLevel(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            ToggleKami(True)
            print("Resume rush by level; cygnus fourth")

def ResistanceFirstJobAdv():
    print("Resistance 1")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    if job == 3000:
        if Terminal.IsRushing():
            time.sleep(1)
        if field_id == 931000000:
            # the beginning map
            ToggleKami(False)
            Character.AMoveX(-96)
            time.sleep(1)
        elif field_id == 931000001:
            # move to the portal
            if Character.GetPos().x != 1440:
                Character.Teleport(1440,28)
            Character.EnterPortal()
            
        # and now we are in the room with vita
        elif field_id == 931000010:
            Character.TalkToNpc(2159006)
            time.sleep(5)
            
            
        elif field_id == 931000012:
            Character.TalkToNpc(2159006)
            
        elif field_id == 931000013:
            Character.TalkToNpc(2159007)
            time.sleep(5)
            
        elif field_id == 931000020:
            time.sleep(2)
            if Character.GetPos().x != 0:
                Character.Teleport(0,28)
            
            
        elif field_id == 931000030:
            time.sleep(1)
            if Character.GetPos().x != 342:
                Character.Teleport(342,28)
            Key.Press(0x20)
        
        else:
            # so we finished the beginner stuff
            # now we are in edelstein. 
            spillIt = Quest.GetQuestState(23000)
            kindergarten = Quest.GetQuestState(23001)
            police = Quest.GetQuestState(23002)
            doctor = Quest.GetQuestState(23003)
            streetsweeper = Quest.GetQuestState(23004)
            mascot = Quest.GetQuestState(23005)
            mysteriousInvitation = Quest.GetQuestState(23010)
            done_list = accountData['done_links']
            
            if "Blaster" not in done_list:
                targetJobQuest = 23160
                Instructor = 2151000
            elif "Wild Hunter" not in done_list:
                targetJobQuest = 23012
                Instructor = 2151002
            elif "Battle Mage" not in done_list:
                targetJobQuest = 23011
                Instructor = 2151001
            elif "Mechanic" not in done_list:
                targetJobQuest = 23013
                Instructor = 2151004
                
            targetJob = Quest.GetQuestState(targetJobQuest)
            
            if spillIt != 2:
                if field_id != 310000000 and spillIt == 0:
                    Terminal.Rush(310000000)
                    time.sleep(1)
                
                if field_id == 310000000:
                    pos = Character.GetPos()
                    if pos.x != -1297 and pos.y != -14:
                        ToggleKami(False)
                        Character.Teleport(-1297, -14)
                        
                if spillIt == 0:
                    ToggleKami(False)
                    Character.Teleport(-1297, -14)
                    # we need to accept the quest.
                    Quest.StartQuest(23000, 2152000)
                    time.sleep(1)
                    
                
                elif Quest.CheckCompleteDemand(23000, 2152000) != 0:
                    if kindergarten != 2:
                        if kindergarten == 0:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                            Quest.StartQuest(23001, 2152001)
                            
                        
                        elif Quest.CheckCompleteDemand(23001, 2152001) != 0:
                            if field_id != 310020000:
                                Terminal.Rush(310020000)
                                time.sleep(1)
                            
                            # and now we need to kill + loot 5 of the things
                            pos = Character.GetPos()
                            mob = Field.FindMob(150000)
                            potDrop = Field.FindItem(4000595)	
                            # to face right
                            
                            if potDrop.valid:
                                if pos.y < potDrop.y + 75 and pos.y > potDrop.y -75:
                                    # on the same platform, so attack
                                    Character.AMoveX(potDrop.x)
                                    Character.LootItem()
                                    
                                else:
                                    # bottom platform
                                    Character.Teleport(potDrop.x, potDrop.y)
                            
                            elif mob.valid:
                                if mob.y == pos.y:
                                    # on the same platform, so attack
                                    Character.AMoveX(mob.x)
                                    Character.BasicAttack()
                                    
                                else:
                                    ToggleKami(False)
                                    # bottom platform
                                    Character.Teleport(mob.x, mob.y)
                                    
                        else:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                            time.sleep(1)
                            pos = Character.GetPos()
                            if pos.x != -1297 and pos.y != -14:
                                ToggleKami(False)
                                Character.Teleport(-1297, -14)
                            time.sleep(1)
                            Npc.ClearSelection()
                            Npc.RegisterSelection("Peace")
                            
                            Quest.CompleteQuest(23001, 2152001)
                            
                    
                    elif police != 2:
                        if police == 0:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                            Quest.StartQuest(23002, 2152003)
                            
                        elif Quest.CheckCompleteDemand(23002,2152003) != 0:
                            # in progress. 
                            if field_id != 310020100:
                                Terminal.Rush(310020100)
                                
                            pos = Character.GetPos()
                            mob = Field.FindMob(150001)	

                            if mob.valid:
                                # the mob exists. Find it, move to it, kill it
                                if mob.y == pos.y:
                                    # on the same platform, so attack
                                    Character.AMoveX(mob.x)
                                    Character.BasicAttack()
                                
                                else:
                                    ToggleKami(False)
                                    Character.Teleport(mob.x, mob.y)
                                    
                        
                        else: 
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                            time.sleep(1)
                            Npc.ClearSelection()
                            Npc.RegisterSelection("How safe it is")
                            
                            Quest.CompleteQuest(23002, 2152003)
                            
                    
                    elif doctor != 2:
                        if doctor == 0:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                            Quest.StartQuest(23003, 2152004)
                    
                        elif Quest.CheckCompleteDemand(23003,2152004) != 0:
                            if field_id != 310020000:
                                Terminal.Rush(310020000)
                                
                            pos = Character.GetPos()
                            item = Field.FindItem(4034738)
                            
                            if item.valid and (pos.y < item.y + 75 and pos.y > item.y -75):
                                ToggleLoot(False)
                                ToggleKami(False)
                                if pos.x < item.x -15 or pos.x > item.x + 15:
                                    Character.AMoveX(item.x)
                                    Character.LootItem()
                                Character.LootItem()
                                
                            else:
                                ToggleLoot(False)
                                ToggleKami(False)
                                if pos.x < 588 or pos.x > 628 or pos.y > item.y - 75:
                                    Character.Teleport(608, -260)
                                Character.BasicAttack()
                                
                        else:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                            time.sleep(1)
                            Npc.ClearSelection()
                            Npc.RegisterSelection("Surround themselves in an environment that")
                            
                            Quest.CompleteQuest(23003, 2152004)
                            
                    elif streetsweeper != 2:
                        if streetsweeper == 0:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                            Quest.StartQuest(23004, 2152002)
                            
                        elif Quest.CheckCompleteDemand(23004, 2152002) != 0:
                            if field_id != 310020200:
                                Terminal.Rush(310020200)
                                time.sleep(1)
                            
                            # and now we need to kill + loot 5 of the things
                            pos = Character.GetPos()
                            mob = Field.FindMob(150002)
                            item = Field.FindItem(4000597)
                            
                            if item.valid:
                                ToggleLoot(False)
                                if item.y > -100:
                                    # bottom platform
                                    if pos.y < -100:
                                        Character.JumpDown()
                                    Character.AMoveX(item.x)
                                    Character.LootItem()
                                    
                                elif (pos.y < item.y + 75 and pos.y > item.y -75):
                                    Character.AMoveX(item.x)
                                    Character.LootItem()
                                    
                                else:
                                    Character.Teleport(item.x, item.y)
                                        
                            
                            elif mob.valid:
                                if mob.y > -100:
                                    # bottom platform
                                    if pos.y < -100:
                                        Character.JumpDown()
                                    Character.AMoveX(mob.x)
                                    Character.BasicAttack()
                                    
                                elif mob.y == pos.y:
                                    Character.AMoveX(mob.x)
                                    Character.BasicAttack()
                                    
                                else:	
                                    Character.Teleport(mob.x, mob.y)
                        
                        else:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                                time.sleep(1)
                            Character.Teleport(-800, -14)
                            time.sleep(1)
                            Npc.ClearSelection()
                            Npc.RegisterSelection("Restriction on our freedom")
                            Quest.CompleteQuest(23004, 2152002)
                    
                    elif mascot != 2:
                        if mascot == 0:
                            if field_id != 310000000:
                                Terminal.Rush(310000000)
                                time.sleep(1)
                            Character.Teleport(-376, -14)
                            time.sleep(0.5)
                            Quest.StartQuest(23005, 2152005)
                        
                        elif Quest.CheckCompleteDemand(23005, 2152005) != 0:
                            Character.Teleport(1020, -14)
                            time.sleep(0.5)
                            Character.TalkToNpc(2152019)
                            time.sleep(1)

                        else:
                            Character.Teleport(-376, -14)
                            time.sleep(0.5)
                            Npc.ClearSelection()
                            Npc.RegisterSelection("You'd live life as a puppet without even realizing")
                            Quest.CompleteQuest(23005, 2152005)
                            time.sleep(1)
                    
                elif Quest.CheckCompleteDemand(23000, 2152000) == 0:
                    # if its done, rush back to the map
                    if field_id != 310000000:
                        Terminal.Rush(310000000)
                    Npc.ClearSelection()
                    Npc.RegisterSelection("It's such a rush to help people!")
                    Quest.CompleteQuest(23000, 2152000)
                    time.sleep(1)  

            elif spillIt == 2:
                # we finished the preliminary quests. Now do mysteriuos invitation
                if mysteriousInvitation != 2:
                    if mysteriousInvitation == 0:
                        Quest.StartQuest(23010, 2152000)
                        time.sleep(1)
                    elif mysteriousInvitation == 1:
                        Inventory.UseItem(2031010)
                        time.sleep(1)
                        Quest.CompleteQuest(23010, 2151003)
                        time.sleep(1)
                        
                elif targetJob != 2:
                    if targetJob == 0:
                        Quest.StartQuest(targetJobQuest, Instructor)
                        time.sleep(1)
                    elif targetJob == 1:
                        Quest.CompleteQuest(targetJobQuest, Instructor)
                        time.sleep(3)
    if job == 3300:
        CatchJaguar()
    elif job != 3300 and job != 3000 and job != -1:
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleKami(True)
        print("Resume rush by level; resistance first")

def ResistanceSecondJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    if job in WildHunterJobs:
        toDoQuest = 23021
        toDoQuest2 = 23024
        Instructor = 2151002
    elif job in BlasterJobs:
        toDoQuest = 23161
        toDoQuest2= 23162
        Instructor = 2151000
    elif job in BattleMageJobs:
        toDoQuest = 23020
        toDoQuest2 =23023
        Instructor = 2151001
    elif job in MechanicJobs:
        toDoQuest = 23022
        toDoQuest2 =23025
        Instructor = 2151004
    jobAdvance = Quest.GetQuestState(toDoQuest)
    vengeance = Quest.GetQuestState(toDoQuest2)
    if jobAdvance != 2:
        # if the quest is done and we aren't in the correct field_id, rush to it
        if field_id != 310010000:
            Terminal.Rush(310010000)
            time.sleep(1)
            
        if jobAdvance == 0:
            Quest.StartQuest(toDoQuest, 2152000) # accept it from old man
            time.sleep(1)
            
        elif jobAdvance == 1:
            # if complete, hand it in 
            Quest.CompleteQuest(toDoQuest, Instructor)
            time.sleep(1)
    
    elif vengeance != 2:
        pos = Character.GetPos()
        
        if vengeance == 0 and field_id != 310010000:
            Terminal.Rush(310010000)
            time.sleep(1)
            
        if vengeance == 0:
            Quest.StartQuest(toDoQuest2, Instructor)
            time.sleep(1)
            
        elif Quest.CheckCompleteDemand(toDoQuest2, Instructor) != 0:
            if field_id != 310000000 and field_id != 931000100:
                Terminal.Rush(310000000)
                time.sleep(1)
                
            elif field_id == 310000000:
                ToggleKami(False)
                Character.Teleport(1864, -14)
                time.sleep(0.5)
                Character.EnterPortal()
                time.sleep(1)
            
            else:
                # we are in the field_id
                Character.TalkToNpc(2159100)	# talk to him to activate scene
                item = Field.FindItem(4034787)	# look for the item
                
                if item.valid:
                    ToggleKami(False)
                    if pos.x < item.x -15 or pos.x > item.x + 15:
                        Character.AMoveX(item.x)
                    Character.LootItem()
                else:
                    ToggleKami(True)
                time.sleep(1)
                ToggleLoot(True)
            
        elif Quest.CheckCompleteDemand(toDoQuest2, Instructor) == 0:
            if field_id != 310010000 and field_id != 310000000:
                ToggleKami(False)
                Character.Teleport(-374, -14)
                time.sleep(1)
                Character.EnterPortal()
                time.sleep(1)
            elif field_id == 310010000:
                Quest.CompleteQuest(toDoQuest2, Instructor)
                time.sleep(1)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleKami(True)
                ToggleLoot(False)
                print("Resume rush by level; resistance second")
            else:
                Terminal.Rush(310010000)
                time.sleep(1)

def ResistanceThirdJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    Terminal.SetCheckBox("Auto Equip",False)
    if job in WildHunterJobs:
        toDoQuest = 23031
        toDoQuest2 = 23034
        Instructor = 2151002
    elif job in BlasterJobs:
        toDoQuest = 23163
        toDoQuest2= 23164
        Instructor = 2151000
    elif job in BattleMageJobs:
        toDoQuest = 23030
        toDoQuest2 =23033
        Instructor = 2151001
    elif job in MechanicJobs:
        toDoQuest = 23032
        toDoQuest2 =23035
        Instructor = 2151004
    fieldTrip = Quest.GetQuestState(toDoQuest)
    energyDevice = Quest.GetQuestState(toDoQuest2)
    
    if fieldTrip != 2:
        if fieldTrip == 0:
            if field_id != 310010000:
                Terminal.Rush(310010000)
                time.sleep(1)
            Quest.StartQuest(toDoQuest, 2152000)
            
        elif fieldTrip == 1:
            if field_id == 310010000:
                Quest.CompleteQuest(toDoQuest, Instructor)
            else:
                Terminal.Rush(310010000)
                
    elif energyDevice != 2:
        if energyDevice == 0:
            if field_id == 310010000:
                Quest.StartQuest(toDoQuest2, Instructor)
                time.sleep(1)
            else:
                Terminal.Rush(310010000)
                
        elif Quest.CheckCompleteDemand(toDoQuest2, Instructor) != 0:
            # need to kill generator thing
            if Character.GetEquippedItemIDBySlot(-1) == 1003134 or Inventory.GetItemCount(5040004) != 0:
                # if you're wearing the hat, then we can just proceed with quest
                if field_id == 931000200 or field_id == 931000201:
                    ToggleKami(True)
                else:
                    if field_id != 310050100:
                        Terminal.Rush(310050100)
                    TeleportEnter(793,18)
                    
            else:
                # we need the hat
                # check if you have it in your inventory
                hat = Inventory.FindItemByID(1003134)
                if hat.valid:
                    # wear the hat
                    ToggleAttackQuest(False)
                    time.sleep(5)
                    Inventory.SendChangeSlotPositionRequest(1, hat.pos, -1, -1)
                    time.sleep(1) # sleep 1 second
                    
                else:
                    # don't have the hat, so lets do the quest to get it
                    hatQuest = Quest.GetQuestState(23946)
                    if hatQuest != 2:
                        if hatQuest == 0:
                            if field_id != 310040000:
                                Terminal.Rush(310040000)
                                
                            else:
                                Character.Teleport(1614, -812)
                                time.sleep(1)
                                Quest.StartQuest(23946, 2153000)
                                
                        elif Quest.CheckCompleteDemand(23946, 2153000) == 0:
                            Quest.CompleteQuest(23946, 2153000)
                            
                        else:
                            if field_id != 310040000:
                                Terminal.Rush(310040000)
                                
                            else:
                                if pos.x != 1614:
                                    Character.Teleport(1614, -812)
                                    time.sleep(1)
                        
                    else:
                        buyHat = Quest.GetQuestState(23947)
                        if buyHat == 0:
                            Quest.StartQuest(23947, 2153000)
                        elif buyHat == 1:
                            Quest.CompleteQuest(23947, 2153000)
                        else:
                            print("Not enough money")
        
        elif Quest.CheckCompleteDemand(toDoQuest2, Instructor) == 0:
            # if we are done, then rush back to hand it in
            if field_id == 931000200:
                TeleportEnter(140,18)
            
            elif field_id == 310010000:
                Quest.CompleteQuest(toDoQuest2, Instructor)
                time.sleep(1)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleKami(True)
                Terminal.SetCheckBox("Auto Equip",True)
                print("Resume rush by level; resistance third")
            else:
                Terminal.Rush(310010000)

def ResistanceFourthJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    Terminal.SetCheckBox("Auto Equip",False)
    if job in WildHunterJobs:
        toDoQuest = 23041
        toDoQuest2 = 23044
        toDoQuest3 = 23047
        toDoQuest4 = 23050
        toDoQuest5 = 23053
        Instructor = 2151002
        missingInstructor = 2159111
    elif job in BlasterJobs:
        toDoQuest = 23165
        toDoQuest2 =23166
        toDoQuest3 = 23167
        toDoQuest4 = 23168
        toDoQuest5 = 23169
        Instructor = 2151000
        missingInstructor = 2159488
    elif job in BattleMageJobs:
        toDoQuest = 23040
        toDoQuest2 =23043
        toDoQuest3 = 23046
        toDoQuest4 = 23049
        toDoQuest5 = 23052
        Instructor = 2151001
        missingInstructor = 2159110
    elif job in MechanicJobs:
        toDoQuest = 23042
        toDoQuest2 =23045
        toDoQuest3 = 23048
        toDoQuest4 = 23051
        toDoQuest5 = 23054
        Instructor = 2151004
        missingInstructor = 2159112

    drill = Quest.GetQuestState(toDoQuest)
    missing = Quest.GetQuestState(toDoQuest2)
    mad = Quest.GetQuestState(toDoQuest3)
    weapon = Quest.GetQuestState(toDoQuest4)
    master = Quest.GetQuestState(toDoQuest5)

    if drill != 2:
        if field_id != 310010000:
            Terminal.Rush(310010000)
            time.sleep(1)
            
        if drill == 0:
            Quest.StartQuest(toDoQuest, 2152000)
            time.sleep(1)
            
        elif drill == 1:
            # complete it
            Quest.CompleteQuest(toDoQuest, 2151003)

    elif missing != 2:
        if missing == 0:
            if field_id != 310010000:
                Terminal.Rush(310010000)
                time.sleep(1)
            else:
                Quest.StartQuest(toDoQuest2, 2151003)
            
        elif missing == 1:
            if Character.GetEquippedItemIDBySlot(-1) == 1003134:
                # gelimer's keycard
                keyCard = Inventory.FindItemByID(4032743)
                if not keyCard.valid and field_id != 310060000:
                    # if we don't have the keycard and we aren't in 
                    # Gelimer's field_id, then rush to it
                    Terminal.Rush(310060000)
                    
                elif not keyCard.valid and field_id == 310060000:
                    # if we don't have the keycard and we are in 
                    # Gelimer's field_id, then do his quest
                    if mad == 0:
                        Npc.ClearSelection()
                        Npc.RegisterSelection("I'm a new member of the Black Wings")
                        Npc.RegisterSelection("I was patrolling")
                        Npc.RegisterSelection("An intruder?! You need to beef up security")
                        Npc.RegisterSelection("Then allow me to patrol for you")
                        Npc.RegisterSelection("I just offered out of loyalty")
                        Quest.StartQuest(toDoQuest3, 2154009)
                    
                    elif mad == 1:
                        Quest.CompleteQuest(toDoQuest3, 2154009)
                        time.sleep(1)
                    
                elif keyCard.valid and field_id == 310060221:
                    # enter the field_id that requires a keycard
                    TeleportEnter(953,16)
                    
                elif keyCard.valid and field_id >= 931000300 and field_id <= 931000303:
                    portal = Field.FindPortal("out00")
                    if portal.valid:
                        ToggleKami(False)
                        Character.Teleport(portal.x, portal.y - 10)
                        time.sleep(1) # sleep 1 second
                        
                elif keyCard.valid and (field_id <931000300 or field_id > 931000300) and (field_id < 931000310 or field_id > 931000313):
                    # rush to the hidden field_id
                    Terminal.Rush(310060220)
                    time.sleep(1)
                    time.sleep(3)
                    TeleportEnter(1613,-284)
                    
                else:
                    # field_id with the job instructor
                    Quest.CompleteQuest(toDoQuest2, missingInstructor)
                    time.sleep(1) # sleep 1 second
            
            else:
                # wear your hat or get a new one
                hat = Inventory.FindItemByID(1003134)
                if hat.valid:
                    # wear the hat
                    Inventory.SendChangeSlotPositionRequest(1, hat.pos, -1, -1)
                    time.sleep(1) # sleep 1 second
                    
                else:
                     # don't have the hat, so lets do the quest to get it
                    hatQuest = Quest.GetQuestState(23946)
                    if hatQuest != 2:
                        if hatQuest == 0:
                            if field_id != 310040000:
                                Terminal.Rush(310040000)
                                
                            else:
                                Character.Teleport(1614, -812)
                                time.sleep(1)
                                Quest.StartQuest(23946, 2153000)
                                
                        elif Quest.CheckCompleteDemand(23946, 2153000) == 0:
                            Quest.CompleteQuest(23946, 2153000)
                            
                        else:
                            if field_id != 310040000:
                                Terminal.Rush(310040000)
                                
                            else:
                                if pos.x != 1614:
                                    Character.Teleport(1614, -812)
                                    time.sleep(1)
                        
                    else:
                        buyHat = Quest.GetQuestState(23947)
                        if buyHat == 0:
                            Quest.StartQuest(23947, 2153000)
                        elif buyHat == 1:
                            Quest.CompleteQuest(23947, 2153000)
                        else:
                            print("Not enough money")
            
    elif weapon !=2:
        # need to kill the machine thing
        if weapon == 0:
            Quest.StartQuest(toDoQuest4, missingInstructor)
            time.sleep(1) # sleep 1 second
        
        elif Quest.CheckCompleteDemand(toDoQuest4, missingInstructor) != 0:
            # if not done, rush to the mob and kill
            
            if field_id >= 931000310 and field_id <= 931000313:
                portal = Field.FindPortal("west00")
                if portal.valid:
                    TeleportEnter(portal.x, portal.y-10)
            elif field_id >= 931000300 and field_id <= 931000303:
                portal = Field.FindPortal("out00")
                if portal.valid:
                    ToggleKami(False)
                    Character.Teleport(portal.x, portal.y - 10)
                    time.sleep(1) # sleep 1 second
            elif field_id == 310060221:
                TeleportEnter(953,16)
            elif field_id == 310060220:
                # enter the field_id that requires a keycard
                TeleportEnter(1613,-284)
            elif not (field_id >= 931000320 and field_id <= 931000323):
                # if we don't have the keycard and we aren't in 
                # Gelimer's field_id, then rush to it
                Terminal.Rush(310060220)
            else:
                print("Find mob")
                Terminal.StopRush()
                TeleportToMobs()
                #ToggleKami(True)
        
        else:
            # quest is completed
            if field_id >= 931000320 and field_id <= 931000323 :
                portal = Field.FindPortal("east00")
                if portal.valid:
                    TeleportEnter(portal.x, portal.y - 10)
            else:
                Quest.CompleteQuest(toDoQuest4, missingInstructor)
                
    elif master != 2:
        if master == 0:
            if field_id != 310010000:
                RushTo(310010000)
            else:
                Quest.StartQuest(toDoQuest5, Instructor)
                time.sleep(1)
                time.sleep(1)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleKami(True)
                Terminal.SetCheckBox("Auto Equip",True)
                print("Resume rush by level; resistance fourth")

def ABSecondJobAdv():
    toDoQuest = 25825
    quest = Quest.GetQuestState(toDoQuest)
    if quest != 2:
        if quest == 0:
            Quest.StartQuest(toDoQuest,3000018)

def ABThirdJobAdv():
    toDoQuest = 25826
    quest = Quest.GetQuestState(toDoQuest)
    if quest != 2:
        if quest == 0:
            Quest.StartQuest(toDoQuest,3000018)

def ABFourthJobAdv():
    toDoQuest = 25827
    quest = Quest.GetQuestState(toDoQuest)
    if quest != 2:
        if quest == 0:
            Quest.StartQuest(toDoQuest,3000018)

def KaiserSecondJobAdv():
    toDoQuest = 25710
    quest = Quest.GetQuestState(toDoQuest)
    if quest != 2:
        if quest == 0:
            Quest.StartQuest(toDoQuest,0)

def KaiserThirdJobAdv():
    toDoQuest = 25711
    quest = Quest.GetQuestState(toDoQuest)
    if quest != 2:
        if quest == 0:
            Quest.StartQuest(toDoQuest,0)

def KaiserFourthJobAdv():
    toDoQuest = 25712
    quest = Quest.GetQuestState(toDoQuest)
    if quest != 2:
        if quest == 0:
            Quest.StartQuest(toDoQuest,3000011)

def JettSecondJobAdv():
    print("Jett Second")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    toDoQuest = 53236
    toDoQuest2 = 53237
    toDoQuest3 = 53238
    pirateInstructor = 1090000
    thunderhammer = 9270091
    toGoMap = 552000071
    quest = Quest.GetQuestState(toDoQuest)
    quest2 = Quest.GetQuestState(toDoQuest2)
    quest3 = Quest.GetQuestState(toDoQuest3)

    pet = Inventory.FindItemByID(2434265)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)

    if quest != 2:
        if quest == 0:
            acceptQuest(toDoQuest,pirateInstructor,field_id,field_id)
        elif quest == 1:
            completeQuest(toDoQuest,thunderhammer,toGoMap,toGoMap,field_id)
    elif quest2 != 2:
        if quest2 == 0:
            acceptQuest(toDoQuest2,thunderhammer,toGoMap,field_id)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(toDoQuest2,thunderhammer) == 0:
                if field_id == 552000072:
                    DungeonTeleport()
                else:
                    completeQuest(toDoQuest2,thunderhammer,toGoMap,toGoMap,field_id)
            else:
                mobs = Field.GetMobs()
                if len(mobs) != 0:
                    ToggleKami(True)
    elif quest3 != 2:
        if quest3 == 0:
            acceptQuest(toDoQuest3,thunderhammer,toGoMap,field_id)
            ToggleRushByLevel(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            print("Resume rush by level; jett second")

def JettThirdJobAdv():
    print("Jett Third")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    toDoQuest = 53239
    pirateInstructor = 1090000
    thunderhammer = 9270091
    toGoMap = 552000071
    quest = Quest.GetQuestState(toDoQuest)

    if quest != 2:
        if quest == 0:
            if field_id == 552000071:
                DungeonTeleport()
            else:
                acceptQuest(toDoQuest,thunderhammer,field_id,field_id)
                time.sleep(2)

        elif quest == 1:
            if Quest.CheckCompleteDemand(toDoQuest,thunderhammer) == 0:
                if field_id != toGoMap:
                    DungeonTeleport()
                else:
                    completeQuest(toDoQuest,thunderhammer,toGoMap,toGoMap,field_id)
            else:
                mobs = Field.GetMobs()
                if len(mobs) != 0:
                    ToggleKami(True)
                elif field_id == 552000071:
                    ForfeitQuest(toDoQuest)
                    DungeonTeleport()

def JettFourthJobAdv():
    print("Jett Fourth")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    toDoQuest = 53242
    toDoQuest2 = 53243
    toDoQuest3 = 53244
    toDoQuest4 = 53249
    toDoQuest5 = 53251
    toDoQuest6 = 53252
    toDoQuest7 = 53253

    broker = 2111007
    bedin = 2111008
    bart = 1094000
    eurek = 2040050
    baroq = 9270090

    quest = Quest.GetQuestState(toDoQuest)
    quest2 = Quest.GetQuestState(toDoQuest2)
    quest3 = Quest.GetQuestState(toDoQuest3)
    quest4 = Quest.GetQuestState(toDoQuest4)
    quest5 = Quest.GetQuestState(toDoQuest5)
    quest7 = Quest.GetQuestState(toDoQuest7)

    magatia = 261000000
    labhallway = 261010000
    desertofdreams = 260020620
    steephill = 240010300
    if quest != 2:
        if quest == 0:
            acceptQuest(toDoQuest,broker,field_id,field_id)
        elif quest == 1:
            if Quest.CheckCompleteDemand(toDoQuest,broker) == 0:
                completeQuest(toDoQuest,broker,magatia,magatia,field_id)
            else:
                pieceOfSteel = 4000357
                hardenedPieceOfSteel = 4000358
                wires = 4000364
                if Inventory.FindItemByID(pieceOfSteel).count < 50:
                    RushTo(261020600)
                elif Inventory.FindItemByID(hardenedPieceOfSteel).count < 50:
                    RushTo(261020700)
                else:
                    RushTo(261020400)
                ToggleKami(True)
                ToggleAttackQuest(True)
    elif quest2 != 2:
        if quest2 == 0:
            acceptQuest(toDoQuest2,broker,magatia,field_id)
        elif quest2 == 1:
            completeQuest(toDoQuest2,bedin,labhallway,labhallway,field_id)
    elif quest3 != 2:
        if quest3 == 0:
            acceptQuest(toDoQuest3,broker,magatia,field_id)
        elif quest3 == 1:
            if Quest.CheckCompleteDemand(toDoQuest3,broker) == 0:
                completeQuest(toDoQuest3,broker,magatia,magatia,field_id)
            elif field_id != desertofdreams:
                RushTo(desertofdreams)
            elif field_id == desertofdreams:
                TeleportEnter(-935,455)
                time.sleep(5)
    elif quest4 != 2:
        if quest4 == 0:
            acceptQuest(toDoQuest4,bart,field_id,field_id)
        elif quest4 == 1:
            message = 2430752
            if Quest.CheckCompleteDemand(toDoQuest4,bart) == 0:
                Quest.CompleteQuest(toDoQuest4,bart)
            if Inventory.FindItemByID(message).valid:
                Inventory.UseItem(message)
    elif quest5 != 2:
        if quest5 == 0:
            acceptQuest(toDoQuest5,eurek,field_id,field_id)
        elif quest5 == 1:
            if Quest.CheckCompleteDemand(toDoQuest6,baroq) == 0:
                Quest.CompleteQuest(toDoQuest6,baroq)
            else:
                ToggleKami(True)
    elif quest7 != 2:
        if quest7 == 1:
            if field_id != steephill:
                RushTo(steephill)
            else:
                TeleportEnter(441,332)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; jett fourth")

def CannoneerFirstJobAdv():
    def Autism():
        time.sleep(1)
        #Key.Press(0x11)
        Character.BasicAttack()
        time.sleep(3)
        #Key.Press(0x11)
        Character.BasicAttack()
        time.sleep(3)
        #Key.Press(0x11)
        Character.BasicAttack()
        time.sleep(3)
        Character.BasicAttack()
        #Key.Press(0x11)


    Quest1 = Quest.GetQuestState(2573)
    Quest2 = Quest.GetQuestState(2561)
    Quest3 = Quest.GetQuestState(2560)
    Quest4 = Quest.GetQuestState(2562)
    Quest5 = Quest.GetQuestState(2563)
    Quest6 = Quest.GetQuestState(2564)
    Quest7 = Quest.GetQuestState(2565)
    Quest8 = Quest.GetQuestState(2566)
    Quest9 = Quest.GetQuestState(2567)
    Quest10 = Quest.GetQuestState(2574)
    Quest11 = Quest.GetQuestState(2568)
    Quest12 = Quest.GetQuestState(2569)
    Quest13 = Quest.GetQuestState(2570)

    JobAdv1 = Quest.GetQuestState(1427)
    JobAdv2 = Quest.GetQuestState(1428)
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    Terminal.SetCheckBox("Pet Item Teleport",False)
    if field_id == 3000600 and Quest1 == 0:
        Quest.StartQuest(2573, 1096000)
        time.sleep(30)
    elif Quest2 != 2:
        if field_id == 3000100 and Quest2 != 2:
            if Quest2 == 0:
                Quest.StartQuest(2561, 1096003)
                time.sleep(2)
            elif Quest2 == 1:
                Cat = Inventory.FindItemByID(2010000)
                if Cat.valid:
                    Inventory.UseItem(2010000)
                    time.sleep(2)
                    Quest.CompleteQuest(2561, 1096003)
                else:
                    print('this mean yo dum ass dropped the apple, gonna forfeit quest')
                    oPacket = Packet.COutPacket(quest_header)
                    oPacket.EncodeBuffer("03 01 0A 00 00")
                    Packet.SendPacket(oPacket)
    elif Quest3 != 2:
        if field_id == 3000100 and Quest3 != 2:
            if Quest3 == 0:
                Quest.StartQuest(2560, 1096003)
                time.sleep(2)
            elif Quest3 == 1:
                Quest.CompleteQuest(2560, 1096003)
    elif Quest4 != 2:
        if field_id == 3000100 and Quest4 != 2:
            if Quest4 == 0:
                Npc.ClearSelection()
                Npc.RegisterSelection('''Is there someone else there?''')
                Quest.StartQuest(2562, 1096003)
                time.sleep(3)
            elif Quest4 == 1:
                if field_id == 3000100:
                    ToggleKami(False)
                    Character.Teleport(847, 118)
                    time.sleep(1)
                    Key.Press(0x26)
                    time.sleep(1)
                    Character.Teleport(-257, 164)
                    Quest.CompleteQuest(2562, 1096005)
                elif field_id == 3000200:
                    ToggleKami(False)
                    Character.Teleport(-257, 164)
                    Quest.CompleteQuest(2562, 1096005)
    elif Quest5 != 2:
        if field_id == 3000200 and Quest5 != 2:
            if Quest5 == 0:
                Quest.StartQuest(2563, 1096005)
                time.sleep(1)
            elif Quest5 == 1:
                Quest.CompleteQuest(2563, 1096005)
    elif Quest6 != 2:
        if field_id == 3000200 and Quest6 != 1:
            if Quest6 == 0:
                Quest.StartQuest(2564, 1096005)
                time.sleep(1)
        elif Quest6 == 1 and Quest.CheckCompleteDemand(2564, 1096005) != 0:
            if field_id != 3000300:
                ToggleKami(False)
                Character.Teleport(382, 164)
                time.sleep(1)
                Key.Press(0x26)
            elif field_id == 3000300:
                ToggleAttackQuest(True)
                ToggleKami(True)
                ToggleLoot(True)
        elif Quest.CheckCompleteDemand(2564, 1096005) == 0:
            ToggleAttackQuest(False)
            ToggleKami(False)
            if field_id == 3000200:
                Quest.CompleteQuest(2564, 1096005)
            elif field_id != 3000200:
                Character.Teleport(-742, 168)
                time.sleep(1)
                Key.Press(0x26)
                time.sleep(1)
    elif Quest7 != 2:
        print("q7")
        ToggleAttackQuest(False)
        if field_id == 3000200 and Quest7 == 0:
            Quest.StartQuest(2565, 1096005)
        elif Quest7 == 1 and Quest.CheckCompleteDemand(2565, 1096005) != 0:
            if field_id == 3000400:
                box = Field.FindReactor(1209001)
                ToggleLoot(True)
                if Character.GetPos().x != box.x-10:
                    ToggleKami(False)
                    Character.Teleport(box.x-10,box.y)
                    Autism()
                    time.sleep(2)
            elif field_id != 3000400:
                ToggleKami(False)
                Character.Teleport(150, -175)
                time.sleep(1)
                Key.Press(0x26)
        elif Quest.CheckCompleteDemand(2565, 1096005) == 0:
            ToggleLoot(False)
            if field_id == 3000200:
                Quest.CompleteQuest(2565, 1096005)
            elif field_id != 3000200:
                ToggleKami(False)
                Character.Teleport(-1764, 168)
                time.sleep(1)
                Key.Press(0x26)
    elif Quest8 != 2:
        if field_id == 3000200 and Quest8 == 0:
            Quest.StartQuest(2566, 1096005)
        elif Quest8 == 1:
            if field_id == 3000200 and Quest.CheckCompleteDemand(2566, 1096005) != 0:
                Character.Teleport(150, -175)
                time.sleep(1)
                Key.Press(0x26)
                time.sleep(1)
            if field_id == 3000400 and Quest.CheckCompleteDemand(2566, 1096005) != 0:
                Character.Teleport(2308, 121)
                time.sleep(3)
                Key.Press(0x26)
            elif field_id == 3000500 and Quest.CheckCompleteDemand(2566, 1096005) != 0:
                Character.Teleport(-567, 165)
                time.sleep(1)
                Character.TalkToNpc(1096010)
            elif field_id == 3000500 and Quest.CheckCompleteDemand(2566, 1096005) == 0:
                Character.Teleport(-1120, 165)
                time.sleep(1)
                Key.Press(0x26)
            elif field_id == 3000400 and Quest.CheckCompleteDemand(2566, 1096005) == 0:
                Character.Teleport(-1764, 168)
                time.sleep(1.5)
                Key.Press(0x26)
            elif field_id == 3000200 and Quest.CheckCompleteDemand(2566, 1096005) == 0:
                Quest.CompleteQuest(2566, 1096005)
    elif Quest9 != 2:
        if field_id == 3000200 and Quest9 == 0:
            Quest.StartQuest(2567, 1096005)
        elif field_id == 3000400 and Quest9 == 0:
            Character.Teleport(-1764, 168)
            time.sleep(1)
            Key.Press(0x26)
            time.sleep(1)
        elif field_id == 3000200 and Quest9 == 1:
            Character.Teleport(-1377, 164)
            time.sleep(1)
            Key.Press(0x26)
        elif field_id == 3000100 and Quest9 == 1:
            Character.Teleport(-484, 260)
            time.sleep(2)
            Quest.CompleteQuest(2567, 1096003)
    elif Quest10 != 2:
        if field_id == 3000100 and Quest10 == 0:
            Quest.StartQuest(2574, 1096003)
        elif field_id != 3000100 and Quest10 == 0:
            Terminal.Rush(3000100)
        elif field_id == 3000100 and Quest10 == 1:
            Character.Teleport(847, 118)
            time.sleep(1)
            Key.Press(0x26)
        elif field_id == 3000200 and Quest10 == 1:
            Character.Teleport(-274, 164)
            time.sleep(1)
            Quest.CompleteQuest(2574, 1096005)
    elif Quest11 != 2:
        if field_id == 3000200 and Quest11 == 0:
            Quest.StartQuest(2568, 1096005)
        elif field_id == 912060500 and Quest11 == 1:
            Quest.CompleteQuest(2568, 1096006)
    elif Quest12 != 2:
        if field_id == 912060500 and Quest12 == 0:
            Quest.StartQuest(2569, 1096006)
        elif field_id != 912060500 and Quest12 == 0:
            Terminal.Rush(912060500)
        elif field_id == 912060500 and Quest12 == 1:
            Quest.CompleteQuest(2569, 1096004)
    elif Quest13 != 2:
        if field_id == 912060500 and Quest13 == 0:
            Quest.StartQuest(2570, 1096006)
        elif field_id != 912060500 and Quest13 == 0:
            Terminal.Rush(912060500)
        elif Quest13 == 1:
            if field_id != 120000101:
                Character.Teleport(420, 18)
                time.sleep(1)
                Key.Press(0x26)
            elif field_id == 120000101 and Quest.CheckCompleteDemand(2570, 1090000) == 0:
                Quest.CompleteQuest(2570, 1090000)
                ToggleKami(True)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                Terminal.SetCheckBox("Pet Item Teleport",True)
                print("Resume rush by level; cannoneer first")

def LevelSkill(id):
    qPacket = Packet.COutPacket(level_skill_header)
    skillid = hex(id)[2:].zfill(8)
    qPacket.EncodeBuffer("8D 47 8D 00 {0} {1} {2} {3} 01 00 00 00".format(skillid[6:8],skillid[4:6],skillid[2:4],skillid[0:2]))
    Packet.SendPacket(qPacket)

def ShadeFirstJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    Terminal.SetCheckBox("Mob Falldown",False)
    moonbeam = 3002000
    chieffox = 3002005
    compass = 3002006
    timber = 3002007
    brook = 3002008
    patience = 3002009
    moonbeam2= 3002101

    FoxPointPath = 940200060
    FoxPointVillage = 410000000
    ShadeHouse = 410000001
    FoxTree = 410000002
    EclipseHill1 = 410000010

    quest = 38000
    quest2= 38001
    quest3= 38002
    quest4= 38003
    quest5= 38004
    quest6= 38996
    quest7= 38997
    quest8= 38998
    quest9= 38005
    q1 = Quest.GetQuestState(quest)
    q2 = Quest.GetQuestState(quest2)
    q3 = Quest.GetQuestState(quest3)
    q4 = Quest.GetQuestState(quest4)
    q5 = Quest.GetQuestState(quest5)
    q6 = Quest.GetQuestState(quest6)
    q7 = Quest.GetQuestState(quest7)
    q8 = Quest.GetQuestState(quest8)
    q9 = Quest.GetQuestState(quest9)
    q10 = Quest.GetQuestState(38006)
    q11 = Quest.GetQuestState(38007)
    q12 = Quest.GetQuestState(38008)
    q13 = Quest.GetQuestState(38009)
    q14 = Quest.GetQuestState(38010)
    q15 = Quest.GetQuestState(38011)
    q16 = Quest.GetQuestState(38012)
    q17 = Quest.GetQuestState(38013)
    q18 = Quest.GetQuestState(38014)
    q19 = Quest.GetQuestState(38015)
    q20 = Quest.GetQuestState(38016)
    q21 = Quest.GetQuestState(38017)
    q22 = Quest.GetQuestState(38018)
    q23 = Quest.GetQuestState(38019)
    q24 = Quest.GetQuestState(38020)
    q25 = Quest.GetQuestState(38021)
    q26 = Quest.GetQuestState(38022)
    q27 = Quest.GetQuestState(38023)
    q28 = Quest.GetQuestState(38024)
    q29 = Quest.GetQuestState(38025)
    q30 = Quest.GetQuestState(38026)
    q31 = Quest.GetQuestState(38027)
    q32 = Quest.GetQuestState(38028)
    q33 = Quest.GetQuestState(38029)
    q34 = Quest.GetQuestState(38030)

    def EnterPortalInMap(field_id, pos, x, y):
        if Field.GetID() == field_id:
            if pos.x == x:
                Character.EnterPortal()
            else:
                Character.Teleport(x, y - 10)
            
    def ToggleKillSettings(switch, iSwitch):
        Terminal.SetSpinBox("KamiOffsetX", -45)
        Terminal.SetSpinBox("KamiOffsetY", -10)
        Terminal.SetSpinBox("KamiLoot", 0)
        Terminal.SetSpinBox("autoattack_spin", 50)
        Terminal.SetComboBox("AttackKey", 1)
        Terminal.SetCheckBox("Kami Loot", iSwitch)
        Terminal.SetCheckBox("Auto Loot", iSwitch)
        Terminal.SetCheckBox("Kami Vac", switch)
        Terminal.SetCheckBox("Auto Attack", switch)
    
    def TeleportTo(x, y):
        if Character.GetPos().x != x:
            Terminal.SetCheckBox("Kami Vac",False)
            Character.Teleport(x, y - 10)
    
    
    def RushTo(id):
        eastMaps = [410000030,410000031,410000040,410000041,410000050,410000051]
        if Field.GetID() != id:
            if id == 410000002:
                if Field.GetID() != 410000000:
                    RushTo(410000000)
                else:
                    EnterPortalInMap(410000000,Character.GetPos(),15,39)
            elif id == 410000000:
                if Field.GetID() in eastMaps:
                    EnterPortal("west00")
                elif Field.GetID() in [410000000,410000001,410000002,410000003]:
                    EnterPortal("out00")
                else:
                    EnterPortal("east00")
            elif id == 410000001:
                if Field.GetID() != 410000000:
                    RushTo(410000000)
                else:
                    EnterPortalInMap(410000000,Character.GetPos(),-767,-107)
            
            else:
                if Field.GetID() < id:
                    EnterPortal("east00")
                else:
                    EnterPortal("west00")
            Terminal.Rush(id)
            
    '''
    if field_id == FoxPointPath:
        DungeonTeleport()

    if q1 == 1:
        completeQuest(quest,moonbeam,FoxPointVillage,FoxPointVillage,field_id)
    elif q2 != 2:
        if q2 == 0:
            acceptQuest(quest2,moonbeam,FoxPointVillage,field_id)
        elif q2 == 1:
            completeQuest(quest2,chieffox,FoxPointVillage,FoxPointVillage,field_id)
    elif q3 != 2:
        if q3 == 0:
            acceptQuest(quest3,chieffox,FoxPointVillage,field_id)
        elif q3 == 1:
            if Quest.CheckCompleteDemand(quest3,chieffox) == 0:
                acceptQuest(quest3,chieffox,FoxPointVillage,field_id)
            else:
                if field_id == FoxPointVillage:
                    TeleportEnter(-765,-107)
                elif field_id == ShadeHouse:
                    if pos.x != -3:
                        Character.Teleport(-3,13)
                    Character.TalkToNpc(3002013)
    elif q4 != 2:
        if q4 == 0:
            acceptQuest(quest4,chieffox,FoxPointVillage,field_id)
        elif q4 ==1:
            if Quest.CheckCompleteDemand(quest4,chieffox) != 0:
                Character.Teleport(-765,-107)
                time.sleep(2)
                Character.TalkToNpc(timber)
                time.sleep(1)
                Character.TalkToNpc(compass)
                time.sleep(1)
                Character.TalkToNpc(patience)
                time.sleep(1)
                Character.Teleport(687,-53)
                time.sleep(1)
                Character.TalkToNpc(brook)
            else:
                completeQuest(quest4,chieffox,FoxPointVillage,FoxPointVillage,field_id)
    elif q5 != 2:
        if q5 == 0:
            acceptQuest(quest5,chieffox,FoxPointVillage,field_id)
        elif q5 == 1:
            RushTo(FoxTree)
    elif q6 != 2:
        if q6 == 0:
            acceptQuest(quest6,moonbeam2,FoxTree,field_id)
    elif q7 != 2:
        if q7 == 0:
            acceptQuest(quest7,moonbeam2,FoxTree,field_id)
        elif q7 ==1:
            if Quest.CheckCompleteDemand(quest7,moonbeam2) == 0:
                completeQuest(quest7,moonbeam2,FoxTree,FoxTree,field_id)
            else:
                Character.UseSkill(20051284)
    elif q8 != 2:
        print("8")
        if q8 == 0:
            acceptQuest(quest8,moonbeam2,FoxTree,field_id)
        elif q8 == 1:
            if Quest.CheckCompleteDemand(quest8,moonbeam2) == 0:
                completeQuest(quest8,moonbeam2,FoxTree,FoxTree,field_id)
            else:
                if pos.x != -267:
                    Character.Teleport(-267,-410)
                Character.UseSkill(25001000)
    elif field_id == 410000002:
        DungeonTeleport()
    elif q9 != 2:
        print("9")
        if q9 == 0:
            acceptQuest(quest9,moonbeam,FoxPointVillage,field_id)
        elif q9 == 1:
            #if Quest.CheckCompleteDemand(quest9,moonbeam) == 0:
            completeQuest(quest9,moonbeam,FoxPointVillage,EclipseHill1,field_id)
    '''
    if q15 == 2: 
        Key.Set(0x11, 1, 25001002)
        print("Settings skill to ctrl")
        Terminal.SetCheckBox("Auto SP",True)
    else:
        SkillLevel = Character.GetSkillLevel(25001000)
        if SkillLevel < 1:
            print("Skill level is {},continue".format(SkillLevel))
            LevelSkill(25001000)
        Key.Set(0x11, 1, 25001000)
        print("Settings skill to ctrl")
        Terminal.SetCheckBox("Auto SP",False)
        
      
    if q1 != 2:
        EnterPortalInMap(940200060, pos, 1100, -161)
        if field_id == 410000000:
            Quest.CompleteQuest(38000, 3002000)
  
    elif q2 == 0:
        Quest.StartQuest(38001, 3002000)
    elif q2 == 1:
        Quest.CompleteQuest(38001, 3002005)
    elif q3 == 0:
        Quest.StartQuest(38002, 3002005)
    elif q3 == 1:
        if Quest.CheckCompleteDemand(38002, 3002005):
            RushTo(410000001)
        else:
            RushTo(410000000)
            Quest.CompleteQuest(38002, 3002005)
    elif q4 == 0:
        Quest.CompleteQuest(38003, 3002005)
    elif q4 == 1:
        RushTo(410000000)
        if pos.x != 2:
            Character.Teleport(2, 30)
        Character.TalkToNpc(3002007)
        time.sleep(1)
        Character.TalkToNpc(3002006)
        time.sleep(1)
        Character.TalkToNpc(3002009)
        time.sleep(1)
        Character.TalkToNpc(3002008)
        time.sleep(1)
        Quest.CompleteQuest(38003, 3002005)
    elif q5 == 0:
        Quest.StartQuest(38004, 3002005)
    elif q5 == 1:
        EnterPortalInMap(410000000, pos, 2, 42)
    elif q6 == 0:
        Quest.StartQuest(38996, 3002101)
    elif q7 == 0:
        Quest.StartQuest(38997, 3002101)
    elif q7 == 1:
        Key.Set(0x42, 1, 20051284)
        Key.Press(0x42)
        Quest.CompleteQuest(38997, 3002101)
    elif q8 == 0:
        Quest.StartQuest(38998, 3002101)
    elif q8 == 1:
        if Quest.CheckCompleteDemand(38998, 3002101):
            mob = Field.FindMob(9300877)
            if mob.valid:
                TeleportToMobs()
                Terminal.SetSpinBox("KamiOffsetX", -30)
                Terminal.SetSpinBox("KamiOffsetY", -10)
                Character.BasicAttack()
        else:
            Terminal.SetCheckBox("Kami Vac", False)
            Quest.CompleteQuest(38998, 3002101)
    elif q9 == 0:
        RushTo(410000000)
        Quest.StartQuest(38005, 3002000)
    elif q9 == 1:
        if Quest.CheckCompleteDemand(38005, 3002000):
            RushTo(410000010)
            ToggleKillSettings(True, True)
        else:
            ToggleKillSettings(False, False)
            RushTo(410000000)
            TeleportTo(881, -20)
            Quest.CompleteQuest(38005, 3002000)
    elif q10 == 0:
        Quest.StartQuest(38006, 3002000)
    elif q10 == 1:
        if Quest.CheckCompleteDemand(38006, 3002000):
            RushTo(410000012)
            ToggleKillSettings(True, True)
        else:
            ToggleKillSettings(False, False)
            RushTo(410000000)
            TeleportTo(881, -20)
            Quest.CompleteQuest(38006, 3002000)
    elif q11 == 0:
        Quest.StartQuest(38007, 3002000)
    elif q11 == 1:
        if Quest.CheckCompleteDemand(38007, 3002000):
            RushTo(410000020)
            ToggleKillSettings(True, True)
        else:
            ToggleKillSettings(False, False)
            RushTo(410000000)
            TeleportTo(881, -20)
            Quest.CompleteQuest(38007, 3002000)
    elif q12 == 0:
        Quest.StartQuest(38008, 3002000)
    elif q12 == 1:
        RushTo(410000001)
        EnterPortalInMap(410000001, pos, -3, 13)
        Character.TalkToNpc(3002013)
    elif q13 == 0:
        Quest.StartQuest(38009, 0)
    elif q13 == 1:
        RushTo(410000000)
        Character.TalkToNpc(3002007)
        time.sleep(1)
        Character.TalkToNpc(3002006)
        time.sleep(1)
        Character.TalkToNpc(3002009)
        time.sleep(1)
        Character.TalkToNpc(3002008)
        Quest.CompleteQuest(38009, 3002005)
    elif q14 == 0:
        if field_id != 410000000:
            RushTo(410000000)
        Quest.StartQuest(38010, 3002005)
    elif q14 == 1:
        if Quest.CheckCompleteDemand(38010, 3002005):
            RushTo(410000022)
            ToggleKillSettings(True, True)
        else:
            ToggleKillSettings(False, False)
            RushTo(410000000)
            TeleportTo(881, -20)
            Quest.CompleteQuest(38010, 3002005)
    elif q15 == 0:
        acceptQuest(38011,moonbeam,FoxPointVillage,field_id)
    elif q15 == 1:
        RushTo(410000002)
    elif q16 == 0:
        RushTo(410000000)
        Quest.StartQuest(38012, 3002005)
    elif q16 == 1:
        Terminal.SetCheckBox("Auto SP", False)
        if Quest.CheckCompleteDemand(38012, 3002005):
            if q17 == 0:
                RushTo(410000000)
                Quest.StartQuest(38013, 3002007)
            elif q17 == 1:
                print("17")
                if Quest.CheckCompleteDemand(38013, 3002007):
                    RushTo(410000030)
                    ToggleKillSettings(True, False)
                    time.sleep(20)
                    ToggleKillSettings(False, False)
                    RushTo(410000031)
                    ToggleKillSettings(True, False)
                    time.sleep(20)
                else:
                    ToggleKillSettings(False, False)
                    RushTo(410000000)
                    TeleportTo(-767, -107)
                    Quest.CompleteQuest(38013, 3002007)
            elif q18 == 0:
                RushTo(410000000)
                TeleportTo(-767, -107)
                Npc.ClearSelection()
                Npc.RegisterSelection("Raw Liver")
                Npc.RegisterSelection("Fox God")
                Npc.RegisterSelection("Power to handle spirits")
                Quest.StartQuest(38014, 3002006)
            elif q19 == 0:
                RushTo(410000000)
                Quest.StartQuest(38015, 3002009)
            elif q19 == 1:
                if Quest.CheckCompleteDemand(38015, 3002009):
                    RushTo(410000040)
                    ToggleKillSettings(True, False)
                else:
                    ToggleKillSettings(False, False)
                    RushTo(410000000)
                    TeleportTo(-767, -107)
                    Quest.CompleteQuest(38015, 3002009)
            elif q20 == 0:
                RushTo(410000000)
                TeleportTo(562, 186)
                Quest.StartQuest(38016, 3002008)
            elif q20 == 1:
                if Quest.CheckCompleteDemand(38016, 3002008):
                    RushTo(410000041)
                    ToggleKillSettings(True, False)
                else:
                    ToggleKillSettings(False, False)
                    RushTo(410000000)
                    TeleportTo(582, 186)
                    Quest.CompleteQuest(38016, 3002008)
            elif q21 == 0:
                RushTo(410000000)
                Quest.StartQuest(38017, 3002000)
            elif q21 == 1:
                Quest.CompleteQuest(38017, 3002000)
        else:
            Quest.CompleteQuest(38012, 3002005)
    elif q22 == 0:
        Quest.StartQuest(38018, 3002005)
    elif q22 == 1:
        if Quest.CheckCompleteDemand(38018, 3002005):
            RushTo(410000001)
            EnterPortalInMap(410000001, pos, -3, 13)
            Character.TalkToNpc(3002013)
    elif q23 == 1:
        RushTo(410000000)
        Quest.CompleteQuest(38019, 3002005)
    elif q24 == 0:
        Quest.StartQuest(38020, 3002005)
    elif q24 == 1:
        if Quest.CheckCompleteDemand(38020, 3002005):
            RushTo(410000002)
            Quest.CompleteQuest(38020, 3002014)
          
    elif q25 == 1:
        if (Field.GetMobCount() > 0):
            ToggleKillSettings(True, False)
        else:
            ToggleKillSettings(False, False)
            Quest.CompleteQuest(38021, 0)
    elif q26 == -1:
        EnterPortalInMap(940200040, pos, 808, 25)
    elif q26 == 1:
        if (Field.GetMobCount() > 0):
            ToggleKillSettings(True, False)
        else:
            ToggleKillSettings(False, False)
            Quest.CompleteQuest(38022, 3002103)
    elif q27 == 0:
        RushTo(410000000)
        TeleportTo(54, 40)
        Quest.StartQuest(38023, 3002005)
    elif q27 == 1:
        RushTo(410000001)
        EnterPortalInMap(410000001, pos, -3, 13)
        Character.TalkToNpc(3002013)
    elif q28 == 0:
        RushTo(410000000)
        TeleportTo(54, 40)
        Quest.StartQuest(38024, 3002000)
    elif q28 == 1:
        Character.TalkToNpc(3002007)
        time.sleep(1)
        Character.TalkToNpc(3002009)
        time.sleep(1)
        Character.TalkToNpc(3002008)
        time.sleep(1)
        Character.TalkToNpc(3002001)
        time.sleep(1)
        Quest.CompleteQuest(38024, 3002005)
    elif q29 == 0:
        Quest.StartQuest(38025, 3002005)
    elif q29 == 1:
        Quest.CompleteQuest(38025, 3002010)
    elif q30 == 0:
        Quest.StartQuest(38026, 0)
    elif q30 == 1:
        print("30")
        if Quest.CheckCompleteDemand(38026, 3002101):
            ToggleKillSettings(False, False)
            RushTo(410000050)
            ToggleKillSettings(True, True)
            time.sleep(30)
            ToggleKillSettings(False, False)
            RushTo(410000051)
            ToggleKillSettings(True, False)
            time.sleep(30)
        else:
            ToggleKillSettings(False, False)
            RushTo(410000002)
            Quest.CompleteQuest(38026, 3002101)
    elif q31 == 0:
        print(q31)
        if field_id != 410000002:
            RushTo(410000002)
        Quest.StartQuest(38027, 3002101)
    elif q32 == 0:
        print("q32 0")
        RushTo(410000000)
        Quest.StartQuest(38028, 3002010)
    elif q32 == 1:
        Inventory.UseItem(2432316)
    elif q33 == 0:
        Quest.StartQuest(38029, 0)
    elif q33 == 1:
        Quest.CompleteQuest(38029, 3000000)
    elif q34 == 0:
        Quest.StartQuest(38030, 3000000)
    elif q34 == 1:
        RushTo(400000000)
        time.sleep(10)
        RushTo(100000000)
        Quest.CompleteQuest(38030, 3000000)
        time.sleep(10)
        if Quest.GetQuestState(38030) == 2:
            ToggleRushByLevel(True)
            ToggleKami(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            print("Resume rush by level; shade first")

def ShadeThirdJobAdv():
    ToggleRushByLevel(False)
    ToggleKami(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    quest = Quest.GetQuestState(38074)
    quest2 = Quest.GetQuestState(38075)
    quest3 = Quest.GetQuestState(38076)
    if quest == 0:
        Quest.StartQuest(38074, 0)
    elif quest != 2:
        if field_id == 211060000:
            TeleportEnter(895,-326)
        elif field_id == 921110300:
            TeleportEnter(437,-448)
        else:
            Terminal.Rush(211060000)
    elif quest2 != 2:
        if field_id == 211060000:
            TeleportEnter(895,-326)
        elif field_id == 921110300:
            TeleportEnter(437,-448)
        elif field_id == 921110301:
            r = Field.FindReactor(2119007)

            if r.valid:
                pos = Character.GetPos()
                if pos.x != r.x-50 and pos.y != r.y:
                    Character.Teleport(r.x-50, r.y)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
        else:
            Terminal.Rush(211060000)
    elif quest3 == 0:
        Quest.StartQuest(38076,0)
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; shade third")

def ShadeFourthJobAdv():
    ToggleRushByLevel(False)
    ToggleKami(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    quest = Quest.GetQuestState(38072)
    quest2 = Quest.GetQuestState(38073)
    if quest == 0:
        Quest.StartQuest(38072,0)
    elif quest == 1:
        if field_id != 302000000:
            Terminal.Rush(302000000)
        else:
            Quest.CompleteQuest(38072,2500002)
    elif quest2 == 0:
        Quest.StartQuest(38073, 2500002)
    elif quest2 == 1:
        if field_id != 302000000:
            Terminal.Rush(302000000)
        else:
            Quest.CompleteQuest(38073,2500002)
            ToggleRushByLevel(True)
            ToggleKami(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            print("Resume rush by level; shade fourth")

def MihileSecondJobAdv():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    
    quest = Quest.GetQuestState(20806)
    quest2 = Quest.GetQuestState(20807)
    quest3 = Quest.GetQuestState(20808)
    quest4 = Quest.GetQuestState(20809)
    quest5 = Quest.GetQuestState(20810)
    field_id = Field.GetID()
    if quest != 2:
        print("1")
        Quest.StartQuest(20806, 1101002)
    elif quest2 != 2:
        print("2,1")
        if quest2 == 0:
            print("2,0")
            Quest.StartQuest(20807, 1102000)
        elif quest2 == 1:
            if Quest.CheckCompleteDemand(20807,1102000) == 0:
                if field_id in range(913070800,913070800+20):
                    DungeonTeleport()
                elif field_id ==103000000:
                    Quest.CompleteQuest(20807,1102000)
            else:
                if field_id ==103000000:
                    npc = Field.FindNpc(1103002)
                    if close_enough(pos.x,pos.y,npc.x,npc.y):
                        Character.TalkToNpc(1103002)
                    else:
                        Character.Teleport(npc.x,npc.y)
                elif field_id in range(913070800,913070800+20):
                    if pos.x != -3298:
                        print("teleporting to enemy")
                        Character.Teleport(-3298,88)
                    ToggleAttackQuest(True)
                else:
                    Terminal.Rush(103000000)
    elif quest3 != 2: #101030300
        print("3,1")
        pet = Inventory.FindItemByID(2434265)
        if pet.valid:
            Key.Set(0x41, 2, 2001582)
            time.sleep(2)
            Inventory.UseItem(2434265)
            time.sleep(2)
        if quest3 == 0:
            print("3")
            Quest.StartQuest(20808, 1102000)
        else:
            if Quest.CheckCompleteDemand(20808,1102000) == 0:
                ToggleLoot(False)
                Quest.CompleteQuest(20808,1102000)
            else:
                if field_id ==101030300:
                    print("Enabling attack settings")
                    ToggleKami(True)
                    ToggleLoot(True)
                    ToggleAttackQuest(True)
                else:
                    Terminal.Rush(101030300)
    elif quest4 != 2:
        print("4,1")
        if quest4 == 0:
            print("4")
            Quest.StartQuest(20809, 1102000)
        else:
            if Quest.CheckCompleteDemand(20809,1102000) == 0:
                Quest.CompleteQuest(20809,1102000)
            else:
                if field_id == 102020500:
                    print("Enable attack settings")
                    stumpy = Field.FindMob(3220000)
                    if stumpy.valid:
                        if Character.GetPos().x not in range(stumpy.x-200,stumpy.x):
                            ToggleKami(False)
                            Character.Teleport(stumpy.x-100,stumpy.y)
                        ToggleAttackQuest(True)
                    else:
                        Terminal.ChangeChannel(0)
                else:
                    Terminal.Rush(102020500)
    elif quest5 != 2:
        print("5")
        Quest.StartQuest(20810, 1101000)
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; mihile second")

def MihileThirdJobAdv():
    ToggleRushByLevel(False)
    ToggleKami(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    quest = Quest.GetQuestState(20320)
    quest2 = Quest.GetQuestState(20321)
    if quest == 0:
        Quest.StartQuest(20320, 1101002)
    elif quest == 1:
        if Quest.CheckCompleteDemand(20320,1101002) == 0:
            if field_id == 913070200:
                DungeonTeleport()
            elif field_id == 130000000:
                Quest.CompleteQuest(20320, 1101002)
                ToggleRushByLevel(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; mihile third")
        else:
            if field_id != 913070200:
                if field_id == 130000000:
                    Quest.StartQuest(20321, 1101002)
                else:
                    Terminal.Rush(130000000)
            else:
                ToggleKami(True)
                ToggleAttackQuest(True)

def MihileFourthJobAdv():
    ToggleRushByLevel(False)
    ToggleKami(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    quest = Quest.GetQuestState(20410)
    quest2 = Quest.GetQuestState(20411)
    if quest != 2:
        Quest.StartQuest(20410, 1101002)
    elif quest2 != 2:
        if quest2 == 0:
            Quest.StartQuest(20411, 1101002)
        else:
            if Quest.CheckCompleteDemand(20411,1101002) == 0:
                if field_id == 913070100:
                    DungeonTeleport()
                elif field_id == 130000000:
                    Quest.CompleteQuest(20411, 1101002)
                    ToggleRushByLevel(True)
                    ToggleKami(True)
                    SCLib.UpdateVar("DoingJobAdv",False)
                    print("Resume rush by level; mihile fourth")
                else:
                    Terminal.Rush(130000000)
            else:
                if field_id != 913070100:
                    if field_id == 130000000:
                        Quest.StartQuest(20412, 1101002)
                    else:
                        Terminal.Rush(130000000)
                else:
                    ToggleKami(True)
                    ToggleAttackQuest(True)

def DualbladeFirstJobAdv():
    print("Check1")
    time.sleep(1)

    fieldID = Field.GetID()
    pos = Character.GetPos()
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    #NPCid to NPC Name
    RydenSP = (1057001)
    ShibaBTGE = (1057000)
    RydenBTGE = (1057001)
    LadySyl = (1056000)
    PlayHouse = (9300521)
    Suri = (1058000)
    DarkLord = (1052001)

    #Change FieldID to name for ease of use
    StartingPlace = (103050900)
    BeginnerTrainingGroundEntrance = (103050910)
    TrainingSpot1 = (103050911)
    TrainingSpot2 = (103050912)
    TrainingSpot3 = (103050913)
    LadySylsRoom = (103050101)
    SecretPracticePlaceEntrance = (103050500)
    TheSecretGarden2ndFloor = (103050100)
    PracticePlace1 = (103050510)
    PracticePlace2 = (103050520)
    PracticePlace3 = (103050530)
    Hideout = (103000003)

    #Change QuestID to QUest Name
    EmbarkingOnTheDualBladePath = (2600)
    BasicTraining1 = (2601)
    BasicTraining2 = (2602)
    BasicTraining3 = (2603)
    CalmAndCollected = (2604)
    IntoTheDarkness = (2605)
    SpyTraning1 = (2606)
    SpyTraning2 = (2607)
    SpyTraning3 = (2608)
    SpyTraningComplete = (2609)
    TheRuse = (2610)

    #Get queststate for quests
    quest1 = Quest.GetQuestState (EmbarkingOnTheDualBladePath)
    quest2 = Quest.GetQuestState (BasicTraining1)
    quest3 = Quest.GetQuestState (BasicTraining2)
    quest4 = Quest.GetQuestState (BasicTraining3)
    quest5 = Quest.GetQuestState (CalmAndCollected)
    quest6 = Quest.GetQuestState (IntoTheDarkness)
    quest7 = Quest.GetQuestState (SpyTraning1)
    quest8 = Quest.GetQuestState (SpyTraning2)
    quest9 = Quest.GetQuestState (SpyTraning3)
    quest10 = Quest.GetQuestState (SpyTraningComplete)
    quest11 = Quest.GetQuestState (TheRuse)


    #Complete quest1 (EmbarkingOnTheDualBladePath)
    if quest1 != 2:
        if quest1 ==0:
            Quest.StartQuest (EmbarkingOnTheDualBladePath, RydenSP)
        elif quest1 ==1:
            if fieldID != BeginnerTrainingGroundEntrance:
                if fieldID != StartingPlace:
                    Terminal.Rush(StartingPlace)
                if pos.x != 1060:
                    time.sleep(15)
                    Character.Teleport(1063, 152)
                    time.sleep(1)
                if pos.x == 1063:
                    Character.EnterPortal()
            else:
                Quest.CompleteQuest (EmbarkingOnTheDualBladePath, ShibaBTGE)
    #Complete quest2 (BasicTraining1)
    elif quest2 != 2:
        if quest2 ==0:
            if fieldID != BeginnerTrainingGroundEntrance:
                Terminal.Rush(BeginnerTrainingGroundEntrance)
            else:
                Quest.StartQuest (BasicTraining1, ShibaBTGE)
        elif quest2 ==1:
            if Quest.CheckCompleteDemand (BasicTraining1, ShibaBTGE) ==0:
                ToggleKami(False)
                Terminal.SetCheckBox("Auto Attack", False)
                if fieldID != BeginnerTrainingGroundEntrance:
                    Terminal.Rush (BeginnerTrainingGroundEntrance)
                else:
                    Quest.CompleteQuest (BasicTraining1, ShibaBTGE)
            else:
                if fieldID != TrainingSpot1:
                    Terminal.Rush(TrainingSpot1)
                    Terminal.SetCheckBox("Auto Attack", True)
                    ToggleKami(True)
                else:
                    snail = Field.FindMob(100000)
                    if snail.valid:
                        Character.Teleport(snail.x,snail.y)
                        time.sleep(1)
    #Complete quest3 (BasicTraining2)
    elif quest3 != 2:
        if quest3 ==0:
            if fieldID != BeginnerTrainingGroundEntrance:
                Terminal.Rush(BeginnerTrainingGroundEntrance)
            else:
                Quest.StartQuest (BasicTraining2, ShibaBTGE)
        elif quest3 ==1:
            if Quest.CheckCompleteDemand (BasicTraining2, ShibaBTGE) ==0:
                ToggleKami(False)
                Terminal.SetCheckBox("Auto Attack", False)
                if fieldID != BeginnerTrainingGroundEntrance:
                    Terminal.Rush (BeginnerTrainingGroundEntrance)
                else:
                    Quest.CompleteQuest (BasicTraining2, ShibaBTGE)
            else:
                if fieldID != TrainingSpot2:
                    Terminal.Rush(TrainingSpot2)
                if fieldID == TrainingSpot2:
                    Terminal.SetCheckBox("Auto Attack", True)
                    ToggleKami(True)
                    snail = Field.FindMob(100001)
                    if snail.valid:
                        Character.Teleport(snail.x,snail.y)
                        time.sleep(1)
    #Complete quest4 (BasicTraining3)
    elif quest4 != 2:
        if quest4 ==0:
            if fieldID != BeginnerTrainingGroundEntrance:
                Terminal.Rush(BeginnerTrainingGroundEntrance)
            else:
                Quest.StartQuest (BasicTraining3, ShibaBTGE)
        elif quest4 ==1:
            if Quest.CheckCompleteDemand (BasicTraining3, ShibaBTGE) ==0:
                ToggleKami(False)
                Terminal.SetCheckBox("Auto Attack", False)
                if fieldID != BeginnerTrainingGroundEntrance:
                    Terminal.Rush (BeginnerTrainingGroundEntrance)
                else:
                    Quest.CompleteQuest (BasicTraining3, ShibaBTGE)
            else:
                if fieldID != TrainingSpot3:
                    Terminal.Rush(TrainingSpot3)
                if fieldID == TrainingSpot3:
                    Terminal.SetCheckBox("Auto Attack", True)
                    snail = Field.FindMob(100002)
                    if snail.valid:
                        Character.Teleport(snail.x,snail.y)
                        time.sleep(1)
    #Complete quest5 (CalmAndCollected)
    elif quest5 != 2:
        if quest5 ==0:
            if fieldID != BeginnerTrainingGroundEntrance:
                Terminal.Rush(BeginnerTrainingGroundEntrance)
            else:
                Quest.StartQuest (CalmAndCollected, RydenBTGE)
        elif quest5 ==1:
            if fieldID != LadySylsRoom:
                Terminal.Rush (LadySylsRoom)
            else:
                Quest.CompleteQuest (CalmAndCollected, LadySyl)
    #Comlete quest6 (IntoTheDarkness)
    elif quest6 != 2:
        if quest6 ==0:
            if fieldID != LadySylsRoom:
                Terminal.Rush(LadySylsRoom)
            else:
                Quest.StartQuest (IntoTheDarkness, LadySyl)
        elif quest6 ==1:
            if fieldID != SecretPracticePlaceEntrance:
                if fieldID != TheSecretGarden2ndFloor:
                    Terminal.Rush (TheSecretGarden2ndFloor)
                if pos.x != 82:
                    Character.Teleport(82, 152)
                    time.sleep(1)
                if pos.x == 82:
                    Character.EnterPortal()
            else:
                Quest.CompleteQuest (IntoTheDarkness, RydenBTGE)
    #Complete quest7 (SpyTraning1)
    elif quest7 != 2:
        if quest7 ==0:
            if fieldID != SecretPracticePlaceEntrance:
                if fieldID != TheSecretGarden2ndFloor:
                    Terminal.Rush (TheSecretGarden2ndFloor)
                if pos.x != 82:
                    Character.Teleport(82, 152)
                    time.sleep(1)
                if pos.x == 82:
                    Character.EnterPortal()
            else:
                Quest.StartQuest (SpyTraning1, RydenBTGE)
        elif quest7 ==1:
            if Quest.CheckCompleteDemand (SpyTraning1, RydenBTGE) ==0:
                Terminal.SetCheckBox("Auto Attack", False)
                if fieldID != SecretPracticePlaceEntrance:
                    if fieldID != TheSecretGarden2ndFloor:
                        Terminal.Rush (TheSecretGarden2ndFloor)
                    if pos.x != 82:
                        Character.Teleport(82, 152)
                        time.sleep(1)
                    if pos.x == 82:
                        Character.EnterPortal()
                else:
                    Quest.CompleteQuest (SpyTraning1, RydenBTGE)
            else:
                if fieldID != PracticePlace1:
                    Terminal.Rush(PracticePlace1)
                if fieldID == PracticePlace1:
                    mob = Field.FindMob(PlayHouse)
                    if mob.valid:
                        Character.Teleport(mob.x, mob.y)
                        Terminal.SetCheckBox("Auto Attack", True)
    #Complete quest8 (SpyTraning2)
    elif quest8 != 2:
        if quest8 ==0:
            if fieldID != SecretPracticePlaceEntrance:
                if fieldID != TheSecretGarden2ndFloor:
                    Terminal.Rush (TheSecretGarden2ndFloor)
                if pos.x != 82:
                    Character.Teleport(82, 152)
                    time.sleep(1)
                if pos.x == 82:
                    Character.EnterPortal()
            else:
                Quest.StartQuest (SpyTraning2, RydenBTGE)
        elif quest8 ==1:
            if Quest.CheckCompleteDemand (SpyTraning2, RydenBTGE) ==0:
                Terminal.SetCheckBox("Auto Attack", False)
                if fieldID != SecretPracticePlaceEntrance:
                    if fieldID != TheSecretGarden2ndFloor:
                        Terminal.Rush (TheSecretGarden2ndFloor)
                    if pos.x != 82:
                        Character.Teleport(82, 152)
                        time.sleep(1)
                    if pos.x == 82:
                        Character.EnterPortal()
                else:
                    Quest.CompleteQuest (SpyTraning2, RydenBTGE)
            else:
                if fieldID != PracticePlace2:
                    Terminal.Rush(PracticePlace2)
                if pos.x != -1173:
                    Character.Teleport(-1173, -222)
                else:
                    Character.TalkToNpc(Suri)
    #complete quest9 (SpyTraning3)
    elif quest9 != 2:
        Terminal.SetCheckBox("Rush By Level", 0)
        if quest9 ==0:
            if fieldID != SecretPracticePlaceEntrance:
                if fieldID != TheSecretGarden2ndFloor:
                    Terminal.Rush (TheSecretGarden2ndFloor)
                if pos.x != 82:
                    Character.Teleport(82, 152)
                    time.sleep(1)
                if pos.x == 82:
                    Character.EnterPortal()
            else:
                Quest.StartQuest (SpyTraning3, RydenBTGE)
        elif quest9 ==1:
            if Quest.CheckCompleteDemand (SpyTraning3, RydenBTGE) ==0:
                Terminal.SetCheckBox("Auto Attack", False)
                ToggleKami(False)
                if fieldID != SecretPracticePlaceEntrance:
                    if fieldID != TheSecretGarden2ndFloor:
                        Terminal.Rush (TheSecretGarden2ndFloor)
                    if pos.x != 82:
                        Character.Teleport(82, 152)
                        time.sleep(1)
                    if pos.x == 82:
                        Character.EnterPortal()
                else:
                    Quest.CompleteQuest (SpyTraning3, RydenBTGE)
            else:
                if fieldID != PracticePlace3:
                    Terminal.Rush(PracticePlace3)
                if fieldID == PracticePlace3:
                    Terminal.SetCheckBox("Auto Attack", True)
                    ToggleKami(True)
                    snail = Field.FindMob(9300523)
                    if snail.valid:
                        Character.Teleport(snail.x,snail.y)
                        time.sleep(1)
    #Complete quest10 (SpyTraningComplete)
    elif quest10 != 2:
        Terminal.SetCheckBox("Rush By Level", 0)
        print("Toggle rush by level false db")
        if quest10 ==0:
            if fieldID != SecretPracticePlaceEntrance:
                if fieldID != TheSecretGarden2ndFloor:
                    Terminal.Rush (TheSecretGarden2ndFloor)
                if pos.x != 82:
                    Character.Teleport(82, 152)
                    time.sleep(1)
                if pos.x == 82:
                    Character.EnterPortal()
            else:
                Quest.StartQuest (SpyTraningComplete, RydenBTGE)
        elif quest10 ==1:
            Terminal.SetCheckBox("Auto Attack", False)
            ToggleKami(False)
            if fieldID != LadySylsRoom:
                Terminal.Rush(LadySylsRoom)
            else:
                Quest.CompleteQuest (SpyTraningComplete, LadySyl)
    #Complete quest11 (TheRuse)
    elif quest11 != 2:
        if quest11 ==0:
            if fieldID != LadySylsRoom:
                Terminal.Rush (LadySylsRoom)
            else:
                Quest.StartQuest(TheRuse, RydenBTGE)
        elif quest11 ==1:
            if fieldID != Hideout:
                Terminal.Rush(Hideout)
            if pos.x != -893:
                Character.Teleport(-893, 60)
            else:
                Quest.CompleteQuest(TheRuse, DarkLord)
                time.sleep(1)
                print("All Done, starting maprusher")
                Terminal.SetCheckBox("Kami Vac", 1)
                Terminal.SetCheckBox("Auto Attack", 1)
                Inventory.SendChangeSlotPositionRequest(1, 1, -11, -1)
                time.sleep(5)
                Terminal.SetCheckBox("Rush By Level", 1)
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)

def DualbladeSecondJobAdv():
    ToggleRushByLevel(False)
    ToggleKami(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    #time.sleep(1)
    quest0 = Quest.GetQuestState(2622)
    quest1 = Quest.GetQuestState(2623)

    if quest0 != 2:
        Quest.StartQuest(2622, 1056000)
        time.sleep(2)
        if field_id == 103050101:
            Quest.CompleteQuest(2622, 1056000)
        else:
            Terminal.Rush(103050101)

    elif quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(2623, 1056000)

        elif Quest.CheckCompleteDemand(2623, 1056000) != 0:
            Inventory.UseItem(20430071)
            r = Field.FindReactor(1032001)
            i = Field.FindItem(2430071)

            if i.valid:
                Character.Teleport(i.x, i.y)
                time.sleep(1)
                Character.LootItem()
                time.sleep(1)
                Inventory.UseItem(2430071)

            elif r.valid:
                pos = Character.GetPos()
                if pos.x != r.x and pos.y != r.y:
                    Character.Teleport(r.x, r.y)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                time.sleep(2)
                Character.BasicAttack()
                Inventory.UseItem(2430071)



        else:
            if field_id == 910350000:
                Character.Teleport(2487, 152)
                time.sleep(1)
                Character.EnterPortal()

            if field_id == 103050101:
                Quest.CompleteQuest(2623, 1056000)
                time.sleep(5)
                ToggleRushByLevel(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleLoot(False)
                print("Resume rush by level; db second")

def DualBladeThirdJobAdv():
    item = Inventory.GetItemCount(4031013)
    ToggleRushByLevel(False)
    #time.sleep(1)
    quest0 = Quest.GetQuestState(2637)
    quest1 = Quest.GetQuestState(2638)
    SCLib.UpdateVar("DoingJobAdv",True)
    Terminal.SetCheckBox("filter_etc", False)
    Terminal.SetCheckBox("Auto Loot", True)
    Key.Set(0x11, 1, 4001013)
    print("Settings skill to ctrl")
    if quest0 != 2:
        Quest.StartQuest(2637, 1056000)
        time.sleep(2)
        if field_id == 103050101:
            Quest.CompleteQuest(2637, 1056000)
        else:
            Terminal.Rush(103050101)

    elif quest1 != 2:
        if quest1 == 0:
            Quest.StartQuest(2638, 1056000)

        else:
            if field_id == 103050101:
                Quest.CompleteQuest(2638, 1056000)
                ToggleRushByLevel(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("Resume rush by level; db third")
            elif item >= 30:
                Character.Teleport(503, 152)
                ToggleKami(False)
                Terminal.SetCheckBox("Auto Attack", False)
                time.sleep(3)
                Character.EnterPortal()
                time.sleep(1)
                Terminal.SetCheckBox("Auto Attack", True)
                ToggleKami(True)
            else:
                Terminal.SetCheckBox("Auto Attack", True)
                ToggleKami(True)

def DualBladeFourthJobAdv():
    def TP_Syl():
        if  field_id != 103050000 and field_id != 103050200 and field_id != 103050100 and field_id != 103050101:
            Terminal.Rush(103000000)
            Character.Teleport(363, -144)
            time.sleep(1)
            Character.EnterPortal()
            time.sleep(1)
        if field_id == 103050000:
            Character.Teleport(218, 156)
            time.sleep(1)
            Character.EnterPortal()
        elif field_id == 103050200:
            Character.Teleport(299, 152)
            time.sleep(1)
            Character.EnterPortal()
        elif field_id == 103050100:
            Character.Teleport(1882, 152)
            time.sleep(1)
            Character.EnterPortal()

    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    time.sleep(1)
    print("Check4")
    quest0 = Quest.GetQuestState(2641)
    quest1 = Quest.GetQuestState(2642)


    if quest0 != 2:
        print("Check1")
        Quest.StartQuest(2641, 1056000)
        time.sleep(2)
        if field_id == 103050101:
            Quest.CompleteQuest(2641, 1056000)
        else:
            TP_Syl()

    elif quest1 != 2:
        print("Check2")
        if quest1 == 0:
            Quest.StartQuest(2642, 1056000)

        elif Quest.CheckCompleteDemand(2642, 1056000) != 0:
            Terminal.Rush(103030200)
            while Terminal.IsRushing():
                time.sleep(1)

        else:
            if field_id == 103050101:
                Quest.CompleteQuest(2642, 1056000)
                time.sleep(5)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleRushByLevel(True)
                print("Resume rush by level; db fourth")
            else:
                TP_Syl()
                while Terminal.IsRushing():
                    time.sleep(1)

def DualBladeFifth():
    print("Start Advancement")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    #time.sleep(1)
    quest0 = Quest.GetQuestState(1441)
    quest1 = Quest.GetQuestState(1447)

    Terminal.SetCheckBox("filter_etc", False)

    if quest0 != 2:
        ToggleKami(False)
        Quest.StartQuest(1441, 1052001)
        time.sleep(2)
        if field_id == 211000001:
            Quest.CompleteQuest(1441, 2020011)
        else:
            Terminal.Rush(211000001)

    elif quest1 != 2:
        ToggleKami(False)
        if quest1 == 0:
            Quest.StartQuest(1447, 2020011)
            time.sleep(1)

        elif Quest.CheckCompleteDemand(1447, 2020011) != 0:
            ToggleKami(False)
            if field_id == 211040401:
                pos = Character.GetPos()
                if pos.x != 27 and pos.y != 454:
                    Character.Teleport(27, 454)
                    time.sleep(3)
                Character.TalkToNpc(2030006)
            if field_id == 910540000:
                Character.Teleport(2696, 200)
                Character.EnterPortal()

            if field_id == 910540400:
                ToggleKami(True)
                i = Field.FindItem(4031059)
                m = Field.FindMob(9001003)
                if i.valid:
                    Character.Teleport(i.x, i.y)
                    time.sleep(1)
                    Character.LootItem()

                elif m.valid:
                    Character.Teleport(m.x, m.y)


        else:
            if field_id == 910540400:
                Character.TalkToNpc(1061010)
            elif field_id != 211000001:
                Terminal.Rush(211000001)

            else:
                Quest.CompleteQuest(1447, 2020011)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleRushByLevel(True)
                ToggleKami(True)
                print("Resume rush by level; db fifth")

def DualBladeSixth():
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    time.sleep(1)
    quest0 = Quest.GetQuestState(1456)
    quest1 = Quest.GetQuestState(1457)

    Terminal.SetCheckBox("filter_etc", False)
    #Key.Set(0x11, 1, 4331011)

    if quest0 != 2:
        Quest.StartQuest(1456, 2020011)
        time.sleep(2)
        if field_id == 240010501:
            Quest.CompleteQuest(1456, 2081400)
        else:
            Terminal.Rush(240010501)

    elif quest1 != 2:
        ToggleKami(False)
        if quest1 == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection("Please send me to Manon Forest")
            Quest.StartQuest(1457, 2081400)

        elif Quest.CheckCompleteDemand(1457, 2081400) != 0:
            if field_id == 924000200:
                i = Field.FindItem(4031517)
                m = Field.FindMob(9001043)
                if i.valid:
                    Character.Teleport(i.x, i.y)
                    Character.LootItem()
                    time.sleep(1)

                elif m.valid:
                    pos = Character.GetPos()
                    if pos != (-374, 452):
                        Character.Teleport(-374, 452)

                else:
                    ToggleKami(False)
                    Character.Teleport(-12, 452)
                    time.sleep(1)
                    Character.EnterPortal()
            if Inventory.FindItemByID(4031517).valid and field_id != 924000201:
                Terminal.Rush(240020100)
            if field_id == 240020100:
                ToggleKami(False)
                Terminal.SetCheckBox("Auto Attack", False)
                Character.Teleport(-50, 332)
                time.sleep(1)
                Character.EnterPortal()
                time.sleep(1)
                Terminal.SetCheckBox("Auto Attack", True)
            if field_id == 924000201:
                i = Field.FindItem(4031518)
                m = Field.FindMob(9001044)

                if i.valid:
                    Character.Teleport(i.x, i.y)
                    Character.LootItem()
                    time.sleep(1)

                if m.valid:
                    pos = Character.GetPos()
                    if pos != (-21, 452):
                        Character.Teleport(-21, 452)

        else:
            if field_id == 924000201:
                Character.Teleport(-10, 452)
                time.sleep(1)
                Character.EnterPortal()

            elif field_id != 240010501:
                Terminal.Rush(240010501)

            else:
                Quest.CompleteQuest(1457, 2081400)
                time.sleep(1)
                SCLib.UpdateVar("DoingJobAdv",False)
                ToggleRushByLevel(True)
                ToggleKami(True)
                print("Resume rush by level; db sixth")

def KinesisFirstJobAdv():

    CheckYourself = 22712
    JaysGripe = 22720
    VicePresidents = 22721
    petition1 = 22722
    petition2 = 22723
    petition3 = 22724
    JaysOnTheCase = 22725
    CodeBreakerJay1=22726
    HeroOnTheScene =22727
    GatheringEvidence = 22728
    AreBlackCatsUnlucky=22729
    CodeBreakerJay2=22730
    AherosDuty1 = 22731
    AherosDuty2 = 22732
    APaleThreat = 22733
    quest1 = Quest.GetQuestState(CheckYourself)
    quest2 = Quest.GetQuestState(JaysGripe)
    quest3 = Quest.GetQuestState(VicePresidents)
    quest4 = Quest.GetQuestState(petition1)
    quest5 = Quest.GetQuestState(petition2)
    quest6 = Quest.GetQuestState(petition3)
    quest7 = Quest.GetQuestState(JaysOnTheCase)
    quest8 = Quest.GetQuestState(CodeBreakerJay1)
    quest9 = Quest.GetQuestState(HeroOnTheScene)
    quest10= Quest.GetQuestState(GatheringEvidence)
    quest11= Quest.GetQuestState(AreBlackCatsUnlucky)
    quest12 = Quest.GetQuestState(CodeBreakerJay2)
    quest13 = Quest.GetQuestState(AherosDuty1)
    quest14 = Quest.GetQuestState(AherosDuty2)
    quest15 = Quest.GetQuestState(APaleThreat)
    Jay = 1531007
    Yuna = 1531008
    Jin = 1531061
    Young = 1531046
    Joon = 1531047
    Min = 1531042
    Hyuk = 1531043
    Nero = 1531010
    BlueShirtGuy = 1531064
    BlondeLady = 1531065
    TshirtBoy = 1531066
    StraightHairGirl = 1531067
    trainingroom1 = 331001110
    trainingroom2 = 331001120
    trainingroom3 = 331001130
    HQ = 331001000
    citycentre = 331000000
    firstfloor = 331002000
    secondfloor=331002100
    classroom1 =331002300
    classroom2 = 331002500
    subwaycar1 =331003000
    pet = Inventory.FindItemByID(2434265)
    SCLib.UpdateVar("DoingJobAdv",True)
    if pet.valid:
        Key.Set(0x41, 2, 2001582)
        time.sleep(2)
        Inventory.UseItem(2434265)
        time.sleep(2)

    if field_id in range(trainingroom1,trainingroom1+10):
        print("1")
        DungeonTeleport()
    elif field_id in range(trainingroom2,trainingroom2+10):
        print("2")
        TeleportEnter(-285,63)
    elif field_id in range(trainingroom3,trainingroom3+10):
        mobs = Field.GetMobs()
        if len(mobs) == 0:
            DungeonTeleport()
        else:
            ToggleKami(True)
            Character.MoveX(600,5)
            print("Moving")
            time.sleep(2)
    elif quest1 != 2:
        if quest1 == 0:
            acceptQuest(CheckYourself,Jay,HQ,field_id)
        elif quest1 == 1:
            SkillLevel = Character.GetSkillLevel(140000291)
            drink = Inventory.FindItemByID(2000040)
            if drink.valid:
                Inventory.UseItem(2000040)
            if SkillLevel < 6:
                print("Skill level is {},continue".format(SkillLevel))
                qPacket = Packet.COutPacket(level_skill_header)
                qPacket.EncodeBuffer("8D 47 8D 00 23 3C 58 08 01 00 00 00")
                Packet.SendPacket(qPacket)
                time.sleep(1)
            completeQuest(CheckYourself,Jay,HQ,HQ,field_id)
    elif quest2 != 2:
        if quest2 == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection(" ")
            acceptQuest(JaysGripe,Jay,HQ,field_id)
        elif quest2 == 1:
            if field_id != firstfloor:
                RushTo(firstfloor)
            elif field_id == firstfloor:
                completeQuest(JaysGripe,Yuna,firstfloor,firstfloor,field_id)
    elif quest3 != 2:
        ToggleKami(False)
        if quest3 == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection(" ")
            acceptQuest(VicePresidents,Yuna,firstfloor,field_id)
        elif quest3 == 1:
            if Quest.CheckCompleteDemand(VicePresidents,Yuna) != 0:
                if quest4 != 2:
                    acceptQuest(petition1,Jin,firstfloor,field_id)
                elif quest5 != 2:
                    acceptQuest(petition2,Young,firstfloor,field_id)
                elif quest6 != 2:
                    acceptQuest(petition3,Joon,firstfloor,field_id)
            else:
                Npc.ClearSelection()
                Npc.RegisterSelection(" ")
                completeQuest(VicePresidents,Yuna,firstfloor,firstfloor,field_id)
    elif quest7 != 2:
        if quest7 == 0:
            acceptQuest(JaysOnTheCase,Jay,HQ,field_id)
        elif quest7 == 1:
            if field_id != HQ:
                RushTo(HQ)
            else:
                completeQuest(JaysOnTheCase,Jay,HQ,HQ,field_id)
    elif quest8 != 2:
        if quest8 == 0:
            Npc.ClearSelection()
            Npc.RegisterSelection(" ")
            if field_id != HQ:
                RushTo(HQ)
            acceptQuest(CodeBreakerJay1,Jay,HQ,field_id)
        elif quest8 == 1:
            if field_id != firstfloor:
                RushTo(firstfloor)
            else:
                completeQuest(CodeBreakerJay1,Min,firstfloor,firstfloor,field_id)
    elif quest9 != 2:
        if quest9 == 0:
            acceptQuest(HeroOnTheScene,Min,firstfloor,field_id)
        elif quest9 == 1:
            if field_id == firstfloor:
                TeleportEnter(122,207)
            elif field_id in range(331002300,331002310) and len(Field.GetMobs()) > 0:
                ToggleKami(True)
            else:
                completeQuest(HeroOnTheScene,Hyuk,classroom1,classroom1,field_id)
    elif quest10 != 2:
        if quest10 == 0:
            acceptQuest(GatheringEvidence,0,classroom1,classroom1)
        elif quest10 == 1:
            if Quest.CheckCompleteDemand(GatheringEvidence,0) != 0:
                if field_id in range(331002300,331002310):
                    DungeonTeleport()
                elif field_id == firstfloor:
                    EnterPortal("up_floor2")
                elif field_id == secondfloor:
                    EnterPortal("into_classroom")
                elif field_id in range(331002400,331002410) and len(Field.GetMobs()) > 0:
                    ToggleKami(True)
            elif Quest.CheckCompleteDemand(GatheringEvidence,0) == 0:
                Quest.CompleteQuest(GatheringEvidence,0)
    elif quest11 != 2:
        print('11')
        if field_id == classroom2:
            DungeonTeleport()
        elif quest11 == 0:
            print("0")
            if field_id != citycentre:
                RushTo(firstfloor)
                if field_id == firstfloor:
                    TeleportEnter(-475,207)
            else:
                acceptQuest(AreBlackCatsUnlucky,Nero,citycentre,field_id)
        elif quest11 == 1:
            if field_id != HQ:
                RushTo(HQ)
            else:
                completeQuest(AreBlackCatsUnlucky,Jay,HQ,HQ,field_id)
    elif quest12 != 2:
        print("12")
        if quest12 == 0:
            if field_id != HQ:
                RushTo(HQ)
            else:
                Npc.ClearSelection()
                Npc.RegisterSelection(" ")
                acceptQuest(CodeBreakerJay2,Jay,HQ,field_id)
        elif quest12 == 1:
            if field_id == citycentre:
                TeleportEnter(-753,413)
            elif field_id == HQ:
                TeleportEnter(-94,-209)
            else:
                completeQuest(CodeBreakerJay2,BlueShirtGuy,subwaycar1,subwaycar1,field_id)
    elif quest13 != 2:
        print("13")
        if quest13 ==0:
            acceptQuest(AherosDuty1,BlueShirtGuy,subwaycar1,field_id)
        elif quest13 ==1:
            if field_id == citycentre:
                TeleportEnter(-753,413)
            if Quest.CheckCompleteDemand(AherosDuty1,BlueShirtGuy) != 0:
                if field_id == subwaycar1:
                    TeleportEnter(813,57)
                elif len(Field.GetMobs()) > 0:
                    ToggleKami(True)
                else:
                    npcs = Field.GetNpcs()
                    for npc in npcs:
                        if npc.valid:
                            Character.TalkToNpc(npc.id)
                            time.sleep(2)
    elif quest14 != 2:
        print("14")
        if quest14 ==0:
            acceptQuest(AherosDuty2,TshirtBoy,field_id,field_id)
        elif quest14 ==1:
            if field_id == citycentre:
                TeleportEnter(-753,413)
            if Quest.CheckCompleteDemand(AherosDuty2,StraightHairGirl) != 0:
                if len(Field.GetMobs()) == 0:
                    DungeonTeleport()
                elif len(Field.GetMobs()) > 0:
                    ToggleKami(True)
                else:
                    npcs = Field.GetNpcs()
                    for npc in npcs:
                        if npc.valid:
                            Character.TalkToNpc(npc.id)
                            time.sleep(2)
            elif Quest.CheckCompleteDemand(AherosDuty2,StraightHairGirl) == 0:
                npcs = Field.GetNpcs()
                for npc in npcs:
                    if npc.valid:
                        Character.TalkToNpc(npc.id)
                        time.sleep(2)
    elif quest15 != 2:
        print("15")
        if quest15 ==0:
            acceptQuest(APaleThreat,StraightHairGirl,field_id,field_id)
        elif quest15 ==1:
            if field_id == citycentre:
                TeleportEnter(-753,413)
            if Quest.CheckCompleteDemand(APaleThreat,StraightHairGirl) != 0:
                if len(Field.GetMobs()) == 0:
                    DungeonTeleport()
                elif len(Field.GetMobs()) > 0:
                    ToggleKami(True)
                else:
                    npcs = Field.GetNpcs()
                    for npc in npcs:
                        if npc.valid:
                            Character.TalkToNpc(npc.id)
                            time.sleep(2)
            elif Quest.CheckCompleteDemand(APaleThreat,StraightHairGirl) == 0:
                npcs = Field.GetNpcs()
                for npc in npcs:
                    if npc.valid:
                        Character.TalkToNpc(npc.id)
                        time.sleep(2)

def KinesisSecondJobAdv():
    TypeNDataUpgrade = 22770
    SCLib.UpdateVar("DoingJobAdv",True)
    quest1 = Quest.GetQuestState(TypeNDataUpgrade)

    Jay = 1531007
    Yuna = 1531008
    Jin = 1531061
    Young = 1531046
    Joon = 1531047
    Min = 1531042
    Hyuk = 1531043
    Nero = 1531010
    BlueShirtGuy = 1531064
    BlondeLady = 1531065
    TshirtBoy = 1531066
    StraightHairGirl = 1531067
    trainingroom1 = 331001110
    trainingroom2 = 331001122
    trainingroom3 = 331001130
    HQ = 331001000
    citycentre = 331000000
    firstfloor = 331002000
    secondfloor=331002100
    classroom1 =331002300
    classroom2 = 331002500
    subwaycar1 =331003000
    if quest1 !=2 :
        print("1")
        if quest1 == 0:
            Quest.StartQuest(TypeNDataUpgrade,Jay)
            SCLib.UpdateVar("DoingJobAdv",False)

def KinesisThirdJobAdv():
    TypeEDataUpgrade = 22800
    Jay = 1531007
    quest1 = Quest.GetQuestState(TypeEDataUpgrade)
    
    if quest1 !=2 :
        print("1")
        if quest1 == 0:
            Quest.StartQuest(TypeEDataUpgrade,Jay)

def KinesisFourthJobAdv():
    TypeDDataUpgrade = 22850
    Jay = 1531007
    quest1 = Quest.GetQuestState(TypeDDataUpgrade)

    if quest1 !=2 :
        print("1")
        if quest1 == 0:
            Quest.StartQuest(TypeDDataUpgrade,Jay)
################################################################
def Id2Str(jobid):
    if jobid in LuminousJobs:
        return "Luminous"
    elif jobid in DemonAvengerJobs:
        return "Demon Avenger"
    elif jobid in DemonSlayerJobs:
        return "Demon Slayer"
    elif jobid in MercedesJobs:
        return "Mercedes"
    elif jobid in HayatoJobs:
        return "Hayato"
    elif jobid in XenonJobs:
        return "Xenon"
    elif jobid in PhantomJobs:
        return "Phantom"
    elif jobid in ArkJobs:
        return "Ark"
    elif jobid in EvanJobs:
        return "Evan"
    elif jobid in IlliumJobs:
        return "Illium"
    elif jobid in CadenaJobs:
        return "Cadena"
    elif jobid == 11212:
        return "Beast Tamer"
    elif jobid in AranJobs:
        return "Aran"
    elif jobid in KinesisJobs:
        return "Kinesis"
    elif jobid in BlazeWizardJobs:
        return "Blaze Wizard"
    elif jobid in KannaJobs:
        return "Kanna"
    elif jobid in BlasterJobs:
        return "Blaster"
    elif jobid in ShadowerJobs:
        return "Shadower"
    elif jobid in NightlordJobs:
        return "Night Lord"
    elif jobid in DualbladeJobs:
        return "Dual Blade"
    elif jobid in HeroJobs:
        return "Hero"
    elif jobid in PaladinJobs:
        return "Paladin"
    elif jobid in DarkknightJobs:
        return "Dark Knight"
    elif jobid in ILMageJobs:
        return "Ice/Lightning Archmage"
    elif jobid in FPMageJobs:
        return "Fire/Poison Archmage"
    elif jobid in BishopJobs:
        return "Bishop"
    elif jobid in MarksmanJobs:
        return "Marksman"
    elif jobid in BowmasterJobs:
        return "Bowmaster"
    elif jobid in CorsairJobs:
        return "Corsair"
    elif jobid in BuccaneerJobs:
        return "Buccaneer"
    elif jobid in CannoneerJobs:
        return "Cannoneer"
    elif jobid in JettJobs:
        return "Jett"
    elif jobid in DawnWarriorJobs:
        return "Dawn Warrior"
    elif jobid in NightWalkerJobs:
        return "Night Walker"
    elif jobid in WindArcherJobs:
        return "Wind Archer"
    elif jobid in ThunderBreakerJobs:
        return "Thunder Breaker"
    elif jobid in WildHunterJobs:
        return "Wild Hunter"
    elif jobid in BattleMageJobs:
        return "Battle Mage"
    elif jobid in MechanicJobs:
        return "Mechanic"
    elif jobid in AngelicBusterJobs:
        return "Angelic Buster"
    elif jobid in KaiserJobs:
        return "Kaiser"
    elif jobid in MihileJobs:
        return "Mihile"
    elif jobid in ShadeJobs:
        return "Shade"
    else:
        return "Unkown Job jobid ="+str(jobid)


def StarItem(pos, currStar, itemMaxStar, userMaxStar, itemid):
   with open('starforceCosts.txt', 'a+') as sfCosts:
       #print('{0} {1}'.format("Position: ".ljust(padding), str(pos)))
       sfCosts.write('{0} {1}\n'.format("Position: ".ljust(padding), str(pos)))
       slotStartingMeso = Character.GetMeso()
       slotStartingStar = currStar
     
       if itemid in whitelist:
           return
       while currStar < userMaxStar and currStar < itemMaxStar and Inventory.GetItem(1, pos).valid:     
           if GameState.IsInGame():
               print("#-----------------------Star-----------------------#")
               print('{0} {1}'.format("Starring From: ".ljust(padding), str(currStar)))
               print('{0} {1}'.format("User Max stars: ".ljust(padding), str(userMaxStar)))
               print('{0} {1}'.format("Item max stars: ".ljust(padding), str(itemMaxStar)))
               print('{0} {1}'.format("Item ID: ".ljust(padding), str(itemid)))
             
               sfCosts.write("\t#-----------------------Star-----------------------#\n")
               sfCosts.write('\t{0} {1}\n'.format("Starring From: ".ljust(padding), str(currStar)))
               sfCosts.write('\t{0} {1}\n'.format("User Max stars: ".ljust(padding), str(userMaxStar)))
               sfCosts.write('\t{0} {1}\n'.format("Item max stars: ".ljust(padding), str(itemMaxStar)))
               sfCosts.write('\t{0} {1}\n'.format("Item ID: ".ljust(padding), str(itemid)))
             
               beforeMeso = Character.GetMeso()
             
               # star the item
               oPacket = Packet.COutPacket(SF_header)
               oPacket.Encode1(0x01)
               oPacket.EncodeBuffer("** ** ** **")
               oPacket.Encode2(ToHex(pos, 16))
               oPacket.Encode1(0x00)
               oPacket.Encode4(0x00000001)
               oPacket.Encode4(0xFFFFFFFF)
               if safeguard and currStar in range(12, 17):
                   oPacket.Encode2(0x0101)
                   print("SAFEGUARDING")
                   sfCosts.write('\tSAFEGUARDING\n')
               else:
                   oPacket.Encode2(0x0100)
               Packet.SendPacket(oPacket)
           
               # wait for recv
               iPacket = Packet.WaitForRecv(StarForceRecv, 10000)
           
               if iPacket.GetRemaining() < 140:
                   print("Recv length too short (was: " + str(iPacket.GetRemaining()) + ")")
                   sfCosts.write("\tRecv length too short (was: " + str(iPacket.GetRemaining()) + ")\n")
                   break
                 
               afterMeso = Character.GetMeso()
               iCosted = beforeMeso - afterMeso
               print('{0} {1:,}'.format("Meso Cost of Star: ".ljust(padding), iCosted))
               print('{0} {1}'.format("iPacket remaining: ".ljust(padding), iPacket.GetRemaining()))
             
               sfCosts.write('\t{0} {1:,}\n'.format("Meso Cost of Star: ".ljust(padding), iCosted))
               sfCosts.write('\t{0} {1}\n'.format("iPacket remaining: ".ljust(padding), iPacket.GetRemaining()))

               # remove this line if you want faster stars
               # note: this is used as a delay (for safety, etc), so remove at your own risk
               Packet.WaitForRecv(StarForceRecv, 1000)
             
             
               # update current star counter
               currStar = Inventory.GetItem(1, pos).currentStar

               # get max star again in case item blew up
               # item blown up means itemMaxStar = 0
               itemMaxStar = Inventory.GetItem(1, pos).maxStar
             
       slotEndingMeso = Character.GetMeso()
       slotEndingStar = currStar
       slotTotalCost = slotStartingMeso - slotEndingMeso
       if (slotStartingMeso - slotEndingMeso) != 0:
           print('{0} {1:,} meso from star {2} to {3}\n'.format("Total Cost: ".ljust(padding), slotTotalCost, str(slotStartingStar), str(slotEndingStar)))
           sfCosts.write('{0} {1:,} meso from star {2} to {3}\n\n'.format("Total Cost: ".ljust(padding), slotTotalCost, str(slotStartingStar), str(slotEndingStar)))
       
################# MONSTER PARK
################# MONSTER PARK
################# MONSTER PARK
#57.19% -> 91.23%
def DungeonSelector():
    #charLvl = Character.GetLevel()
    if level in range(115,125):
        return (leopard_portal,mossy_tree_forest)
    elif level in range(125,135):
        return (leopard_portal,secret_pirate)
    elif level in range(135,145):
        return (leopard_portal,other_world)
    elif level in range(145,155):
        return (leopard_portal,forbidden_time)
    elif level in range(155,160):
        return (leopard_portal,clandestine_ruins)
    #return (leopard_portal,mossy_tree_forest)
def RushToMP():
    #field_id = Field.GetID()
    rushToMPFlag = True
    while rushToMPFlag:
        field_id_check = Field.GetID()
        if field_id_check == 100000000:
            Character.Teleport(3133,334)
            Character.TalkToNpc(9071003)
            time.sleep(1)
        else:
            Terminal.Rush(100000000)
            time.sleep(1)
        if field_id_check == 951000000:
            print("Complete rushToMP")
            rushToMPFlag = False

def EnterDungeon():
    #field_id = Field.GetID()
    enterDungeonFlag = True
    try_count = 0
    while enterDungeonFlag and try_count < 6:
        try_count += 1
        field_id_check = Field.GetID()
        token = DungeonSelector()
        print("Entering dungeon {}".format(token[1]))
        pos = Character.GetPos()
        if pos.x not in range(token[0][0]-5,token[0][0]+5):
            Character.Teleport(token[0][0],token[0][1])
        time.sleep(1)
        Npc.ClearSelection()
        Character.EnterPortal()
        Npc.RegisterSelection(token[1])
        time.sleep(1)
        if field_id_check != 951000000:
            print("Complete enterDungeon")
            enterDungeonFlag = False
#2
def ReturnMonsterParkMaps():
    return Field.GetID() >= 952000000 and Field.GetID() <= 954070599

def RushOutMP():
    rush_out_flag = True
    while rush_out_flag:
        rush_out_field = Field.GetID()
        if rush_out_field == 951000000:
            Character.TalkToNpc(9071003)
        if rush_out_field != 951000000 and not ReturnMonsterParkMaps():
            rush_out_flag = False
        time.sleep(1)

#Zakum
def ResetNowLockedFunction():
    if NowLockedVar:
        print("Resetting NowLockedVar back to False")
        SCLib.UpdateVar("NowLockedVar", False)
def NowLockedFunction():
    if not NowLockedVar:
        print("Boss Attempt started, Now locked for this boss")
        SCLib.UpdateVar("NowLockedVar", True)
def DidSpawn():
    if not HasSpawned:
        print("Updating HasSpawned to True")
        SCLib.UpdateVar("HasSpawned", True)
def ResetSpawn():
    if HasSpawned:
        print("Resetting HasSpawned back to False")
        SCLib.UpdateVar("HasSpawned", False)
def GetToTheDoorToZakum():
    print("Going to Zakum")
    if field_id != CheifsResidence:
        Terminal.Rush(CheifsResidence)
    else:
        #Ark, Angelic Buster, Cannoneer, Jett, Mechanic, Shade, Thunder Breaker
        Pirates = [511,512,521,522,15500, 15510, 15511, 15512, 6500, 6510, 6511, 6512, 530, 531, 532, 508, 570, 571, 572, 3500, 3510, 3511, 3512, 2500, 2510, 2511, 2512, 1500, 1510, 1511, 1512]
        #Wild Hunter, Wind Archer, Mercedes
        Bowman = [331,332,311,312,321,322,3300, 3310, 3311, 3312, 1300, 1310, 1311, 1312, 2300, 2310, 2311, 2312]
        #Phantom, Xenon, Dual Blade
        Thief = [2400, 2410, 2411, 2412, 3600, 3610, 3611, 3612, 400, 430, 431, 432, 433, 434,6411,6412,6410,422,421,411,412,1412,1411]
        #Kanna, Battle Mage, Beast Tamer, Blaze Wizard, Evan, Luminous
        Magician = [211,212,221,222,231,232,14211,14212,15211,15212,4200, 4210, 4211, 4212, 3200, 3210, 3211, 3212, 11000, 11200, 11210, 11211, 11212, 1200, 1210, 1211, 1212, 2200, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2700, 2710, 2711, 2712, ]
        #Aran, Blaster, Demon Avenger, Demon Slayer, Hayato, Kaiser, Mihile, Zero, Dawn Warrior
        Warrior = [111,112,121,122,131,132,3700, 3710, 3711, 3712, 2100, 2110, 2111, 2112, 3101, 3120, 1321, 3122,3121, 3100, 3110, 3111, 3112, 4100, 4110, 4111, 4112, 6100, 6110, 6111, 6112, 5100, 5110, 5111, 5112, 10100, 10110, 10111, 10112, 1100, 1110, 1111, 1112]
        if job in Bowman:
            TalkNPC = NpcReneBowmanInstructor
        elif job in Thief:
            TalkNPC = NpcArecThiefInstructor
        elif job in Magician:
            TalkNPC = NpcRobeiraMagicianInstructor
        elif job in Warrior:
            TalkNPC = NpcTylusWarriorInstructor
        elif job in Pirates:
            TalkNPC = NpcPedroPirateInstructor
        zakjob = [6995, 6996, 6997, 6998, 6999]
        questToDo = 6995
        for i in zakjob:
            questToDo = i
            ZakumCheck = Quest.GetQuestState(i)
            if ZakumCheck == 2:
                ZakumQuest = True
                break
            elif ZakumCheck == 0 or ZakumCheck == 1:
                ZakumQuest = False
                break
        if ZakumQuest:
            Npc.ClearSelection()
            Npc.RegisterSelection("I want to ")
            time.sleep(1)
            Character.TalkToNpc(TalkNPC)
            time.sleep(3)
        else:
            Quest.StartQuest(questToDo,TalkNPC)
            time.sleep(4)
            Quest.CompleteQuest(questToDo,TalkNPC)
            Npc.ClearSelection()
            Npc.RegisterSelection("I want to ")
            time.sleep(3)
            Character.TalkToNpc(TalkNPC)
            time.sleep(1)

def StartupCheck(accountId):
    split_id = accountId.split("@")[0]
    if os.path.exists('C:/Users/Jacopo/Desktop/TerminalManager/info/{}.json'.format(split_id)):
        #print("Loading")
        #print(split_id)
        with open('C:/Users/Jacopo/Desktop/TerminalManager/info/{}.json'.format(split_id)) as f:
            return json.load(f)
    else:
        print("Creating")
        with open('C:/Users/Jacopo/Desktop/TerminalManager/info/{}.json'.format(split_id), "w+") as db_file:
            db_file.write(json.dumps({}))
            return {}

def HandleReady(data):
    if 'link_start' not in data:
        if 'storage_number' in data:
            data['link_start'] = data['storage_number']+1
        else:
            data['link_start'] = 0
    if 'link_end' not in data:
        data['link_end'] = 11
    if 'storing_meso' not in data:
        data['storing_meso'] = False
    if 'storage_number' not in data:
        data['storage_number'] = 0
    if 'cur_link_pos' not in data:
        if 'link_start' in data:
            data['cur_link_pos'] = str(data['link_start'])
    if 'changing_mule' not in data:
        data['changing_mule'] = False
    if 'date' not in data:
        data['date'] = str(datetime.datetime.utcnow().date())
    if 'zakum_date' not in data:
        data['zakum_date'] = str(datetime.datetime.utcnow().date())
    if 'daily_done' not in data:
        data['daily_done'] = False
    if 'phase_one' not in data:
        data['phase_one'] = False
    if 'done_links' not in data:
        data['done_links'] = []
    if 'done_zakum' not in data:
        data['done_zakum'] = []
    if 'training_done' not in data:
        data['training_done'] = False
    if 'total_slots' not in data:
        data['total_slots'] = 1
    if 'used_slots' not in data:
        data['used_slots'] = 0
def WriteJson(data,accountId):
    split_id = accountId.split("@")[0]
    with open('C:/Users/Jacopo/Desktop/TerminalManager/info/{}.json'.format(split_id), 'w') as outfile:
        parsed = json.dumps(data, indent=4, sort_keys=True)
        outfile.write(parsed)
        outfile.close()

accountId = Terminal.GetLineEdit("LoginID")
accountData = StartupCheck(accountId)
HandleReady(accountData)
WriteJson(accountData,accountId)

if field_id in range(3000000,3000700):
    SCLib.UpdateVar("Cannoneer",True)
    SCLib.UpdateVar("DualBlade",False)
    print("Doing Cannoneer job adv")
elif field_id in range(103050900,103050900+100) or job in DualbladeJobs[1::]:
    SCLib.UpdateVar("Cannoneer",False)
    SCLib.UpdateVar("DualBlade",True)

current_date = str(datetime.datetime.utcnow().date())
if current_date != accountData['date']:
    accountData['date'] = current_date
    accountData['zakum_date'] = current_date
    accountData['daily_done'] = False
    WriteJson(accountData,accountId)

#7

def RevealItemPotential(itemPos):
    if Character.GetMeso() > 500000:
        oPacket = Packet.COutPacket(potential_header)
        oPacket.EncodeBuffer("** ** ** 00 7F 00")
        oPacket.Encode2(itemPos)
        Packet.SendPacket(oPacket)
        rPacket = Packet.WaitForRecv(potential_recv,5000)
        print(rPacket)

def RevealAllPotential():
    print("revealing potentials")
    item_list = Inventory.GetItems(1)
    for item in item_list:
        if item.grade > 0 and item.option1 == 0 and GameState.IsInGame():
            #if item.sn not in accountData['equips']:
            #    accountData['equips'].append(item.sn)
            RevealItemPotential(item.pos)
            time.sleep(0.5)


######Black gate
def BossCheck():
    print("Waiting for boss to spawn...")
    time.sleep(10)
    for mob in blackgate_boss:
        print("Checking for boss: " + str(mob) + "...")
        while Field.FindMob(mob).valid and GameState.IsInGame():
            print("Boss found: " + str(mob) + ", killing boss...")
            time.sleep(6)
    for item in blackgate_eqp:
        print("Checking for item: " + str(item) + "...")
        while Field.FindItem(item).valid and GameState.IsInGame():
            Terminal.SetCheckBox("Kami Vac",False)
            print("item found with id:" + str(item) + ", waiting until item looted")
            time.sleep(9)
    for mob in blackgate_boss:
        print("Checking for boss: " + str(mob) + "...")
        while Field.FindMob(mob).valid and GameState.IsInGame():
            print("Boss found: " + str(mob) + ", killing boss...")
            time.sleep(6)
    for item in blackgate_eqp:
        print("Checking for item: " + str(item) + "...")
        while Field.FindItem(item).valid and GameState.IsInGame():
            Terminal.SetCheckBox("Kami Vac",False)
            print("item found with id:" + str(item) + ", waiting until item looted")
            time.sleep(9)
    for mob in blackgate_boss:    
        print("Checking for boss: " + str(mob) + "...")
        while Field.FindMob(mob).valid and GameState.IsInGame():
            print("Boss found: " + str(mob) + ", killing boss...")
            time.sleep(6)
    for item in blackgate_eqp:
        print("Checking for item: " + str(item) + "...")
        while Field.FindItem(item).valid and GameState.IsInGame():
            Terminal.SetCheckBox("Kami Vac",False)
            print("item found with id:" + str(item) + ", waiting until item looted")
            time.sleep(9)
    print("no boss found or boss killed")
    time.sleep(2)


if job == -1 and not accountData['changing_mule'] and GameState.GetLoginStep() == 1:
    #print("Not logged in yet")
    Terminal.SetLineEdit("LoginChar",accountData["cur_link_pos"])
    Terminal.SetCheckBox("Auto Login",True)
    time.sleep(10)

if accountData['changing_mule'] and GameState.GetLoginStep() == 2:
    Terminal.SetCheckBox("Auto Login",False)
    Terminal.SetLineEdit("LoginChar",str(int(accountData["cur_link_pos"]) + 1))
    chars = Login.GetChars()
    for char in chars:
        if char.level >= 140:
            if Id2Str(char.jobid) not in accountData["done_links"]:
                accountData["done_links"].append(Id2Str(char.jobid))
                print("Updating done char list")
    Terminal.SetCheckBox("Auto Login",True)
    accountData["changing_mule"] = False
    time.sleep(1)
    accountData["cur_link_pos"] = Terminal.GetLineEdit("LoginChar")
    WriteJson(accountData,accountId)
    KillPersistVarThred()

def PrintInfo(chars):
    directory = "C:/Users/Jacopo/Pictures/MapleStoryMerch/ready_to_sell/{}".format(Terminal.GetLineEdit("LoginID"))
    level_count = 0
    link_count = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Creating folder")
    else:
        filelist = [ f for f in os.listdir(directory) if f.endswith(".txt") ]
        if len(filelist) > 1:
            for f in filelist:
                os.remove(os.path.join(directory, f))
        print("Writing to file")
        with open('C:/Users/Jacopo/Pictures/MapleStoryMerch/ready_to_sell/{0}/{0}.txt'.format(Terminal.GetLineEdit("LoginID")),'w') as f:
            f.write("Comes with the following:\n")
            for char in chars:
                if char.level > 100:
                    level_count += char.level
                    link_count += 1
                    f.write("{} {}\n".format(Id2Str(char.jobid),char.level))
            f.write("Total Legion: {}\n".format(level_count))
            f.write("Total Links Skill Characters: {}\n".format(link_count-1))
            f.write("Reboot Box Stage 1 (untouched)")
            f.write(
	'''\nOriginal Email that was used to create this account
Please do not hesitate to message me if you have any questions, I will be as responsive as possible. 
Will provide all information that was used to create the accounts including the original email.
I'm in the EST time zone.
	''')
        f.close()

if accountData['training_done'] and GameState.GetLoginStep() == 2:
    Terminal.SetCheckBox("Auto Login",False)
    chars = Login.GetChars()
    count = 0
    if not Terminal.GetProperty("OutputInfo",False):
        PrintInfo(chars)
        with open('C:/Users/Jacopo/Desktop/TerminalManager/info/output/links_{}.txt'.format(Terminal.GetLineEdit("LoginID")),'w') as charInfo:
            for char in chars:
                if char.level > 100:
                    count += char.level
                    charInfo.write("{} {}\n".format(Id2Str(char.jobid),char.level))
            charInfo.write("Total Legion: {}".format(count))
            charInfo.close()
        Terminal.ChangeStatus("#################Training Done##############")
        print("Detected that training is done")
        Terminal.SetProperty("OutputInfo",True)
        Terminal.SetCheckBox("settings/expcrash",False)

if not accountData['changing_mule'] and GameState.GetLoginStep() == 2:
    accountData['total_slots'] = Login.GetCharSlot()
    accountData['used_slots'] = Login.GetCharCount()
    total_links = 20
    WriteJson(accountData,accountId)
    chars = Login.GetChars()
    for char in chars:
        if char.level >= 140:
            if Id2Str(char.jobid) not in accountData["done_links"]:
                accountData["done_links"].append(Id2Str(char.jobid))
                print("Updating done char list")
    if accountData['total_slots'] <  (1 + total_links + accountData['storage_number']):
        SCLib.UpdateVar("BuyExpansion",True)
        print("Need to buy more expansion")
    WriteJson(accountData,accountId)
    Terminal.SetLineEdit("LoginChar",accountData["cur_link_pos"])
    Terminal.SetCheckBox("Auto Login",True)
if len(accountData["done_links"]) >= 43 and not accountData['phase_one']:
    accountData['phase_one'] = True
    print("Completed {} links".format(len(accountData["done_links"])))
    WriteJson(accountData,accountId)
    if GameState.IsInGame():
        Terminal.Logout()
        time.sleep(2)
elif len(accountData["done_links"]) == 20 and not accountData['training_done']:
    accountData['training_done'] = True
    print("Completed {} links".format(len(accountData["done_links"])))
    WriteJson(accountData,accountId)
    Terminal.ChangeStatus("#################Training Done##############")


def SafetySetting():
    #Turn off dangerous settings
    dangerous_settings = ["Auto Aggro","MonkeySpiritsNDcheck","General FMA","Full Map Attack","Mob Vac","Vellum Freeze","main/boss_freeze","Full God Mode","Guard God Mode"]
    for settings in dangerous_settings:
        if settings == "General FMA":
            if job not in IlliumJobs and job not in BlasterJobs and job not in [330,331,332]:
                Terminal.SetCheckBox(settings, False)
        elif settings == "Full Map Attack":
            if job not in BlazeWizardJobs:
                Terminal.SetCheckBox(settings, False)
        else:
            Terminal.SetCheckBox(settings, False)

def SetPotion():
    pgup_key = 0x21
    if job not in DemonAvengerJobs:
        if Inventory.FindItemByID(2001582).valid:
            hpSlider = int((Character.GetMaxHP()-1000)/Character.GetMaxHP()*100)
            if hpSlider <= 50:
                hpSlider = 50
            Terminal.SetSlider("sliderHP", hpSlider)
            Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
        elif Inventory.FindItemByID(2001506).valid:
            Key.Set(pgup_key, 2, 2001506) #Mana elixir
        else:
            Terminal.SetSlider("sliderHP",60)
            Key.Set(pgup_key, 2, 2002023)
    else:
        Key.Set(pgup_key, 1, 31011001)

def ShowStatus():
    if GameState.IsInGame():
        timerSecond = 40
        statusString = ""
        if Terminal.GetProperty("timeOut",0) == 0:
            Terminal.SetProperty("timeOut",time.time())
        elif time.time()-Terminal.GetProperty("timeOut",0) >= timerSecond: #timerSecond seconds passed
            
            #Show exp status
            if Terminal.GetProperty("currentExp",0) == 0:
                Terminal.SetProperty("currentExp",Character.GetExp())
            else:
                expPerSecond = int((Character.GetExp()-Terminal.GetProperty("currentExp",0))/timerSecond)
                if expPerSecond < 0:
                    statusString = "Leveled Up!!"
                else:
                    statusString = "{} exp/s".format(expPerSecond)
                Terminal.SetProperty("currentExp",Character.GetExp())
                if expPerSecond == 0:
                    Terminal.StopRush()
                    if not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("GettingBoogie"):
                        ToggleRushByLevel(True)
                

            #Show meso status
            if Terminal.GetProperty("currentMeso",0) == 0:
                Terminal.SetProperty("currentMeso",Character.GetMeso())
            else:
                mesoPerSecond = int((Character.GetMeso()-Terminal.GetProperty("currentMeso",0))/timerSecond)
                statusString += ", {} meso/min".format(mesoPerSecond * 60)
                Terminal.SetProperty("currentMeso",Character.GetMeso())
            Terminal.ChangeStatus(statusString)
            Terminal.SetProperty("timeOut",time.time())
    else:
        if accountData['training_done']:
            Terminal.ChangeStatus("#################Training Done##############")
        else:
            Terminal.ChangeStatus("Not logged in")

def vulcan():
    if GameState.IsInGame() and ((int(time.time())%8==0) or (Character.HasBuff(2, 37110009)==False and Character.HasBuff(2, 37120012)==False)):
        Vulcan = Packet.COutPacket(0x033E)
        Vulcan.Encode4(0x023640F1)
        Vulcan.EncodeBuffer("00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        Packet.SendPacket(Vulcan)
    return

def AttackAuto(skillid,on):
    attack_key = 0x44
    Key.Set(attack_key,1,skillid)
    Terminal.SetCheckBox("Skill Injection", False)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack", on)
    Terminal.SetComboBox("AttackKey",33)
    Terminal.SetSpinBox("autoattack_spin",100)

def AttackSI(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",False)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)
    Terminal.SetRadioButton(siOption,True)

def AttackSIND(skillid,on,delay=100,siOption = "SIRadioMelee"):
    Terminal.SetLineEdit("SISkillID",str(skillid))
    Terminal.SetSpinBox("SkillInjection",delay)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetRadioButton(siOption,True)
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection", on)

def SemiNDAA(siSkill,dummySkill,delay,on):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("Skill Injection",False)
    Terminal.SetCheckBox("Melee No Delay",True)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    #count = 0
    while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        for x in range(8):
            Character.UseSkill(siSkill)
            time.sleep(0.015)
        Character.UseSkill(dummySkill)
        time.sleep(delay)
        if Terminal.IsRushing():
            break

def AttackSemiND(siSkill,dummySkill,delay,on):
    try:
        SCLib.ThreadedFunction(SemiNDAA(siSkill,dummySkill,delay,on))
    except:
        x = 1

def SetSIND(siSkill,delay,on):
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetLineEdit("SISkillID",siSkill)
    Terminal.SetCheckBox("Skill Injection",on)
    Terminal.SetCheckBox("Melee No Delay",on)
    Terminal.SetSpinBox("SkillInjection",delay)

def AttackSemiNDOnce(siSkill,dummySkill,delay,on):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    if Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame() and not Terminal.GetRadioButton("SIRadioDragon") and on:
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetLineEdit("SISkillID",str(siSkill))
        Terminal.SetCheckBox("Melee No Delay",True)
        Terminal.SetSpinBox("SkillInjection",15)
        time.sleep(0.24)
        Terminal.SetCheckBox("Skill Injection",False)
        time.sleep(0.02)
        Character.UseSkill(dummySkill)
        time.sleep(delay)

def SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed):
    Terminal.SetCheckBox("Auto Attack",False)
    Terminal.SetRadioButton("SIRadioMelee",True)
    Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
    Terminal.SetCheckBox("Speedy Gonzales",True)
    count = 0
    if siSkill != 32120055:
        delay = 30*math.ceil(delay*1000 * (10+attackSpeed)/480)/1000
    #print("The delay for skill {} is {}, starting si".format(siSkill,delay))
    if siSkill in [5311000,5301000]:
        sleepTime = 0.161
    elif siSkill not in [25101000,25121000]:
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
    #print("Si ended due to break options")
    #Terminal.SetProperty("IssueThread",True)
def AttackSemiNDMagic(siSkill,dummySkill,delay,on,attackSpeed = 4):
    try:
        #if Terminal.GetProperty("IssueThread",True):
        SCLib.ThreadedFunction(SemiNDSi(siSkill,dummySkill,delay,on,attackSpeed))
        #    Terminal.SetProperty("IssueThread",False)
    except:
        pass
        

def ToggleAttack(on):
    attack_key = 0x44
    pgup_key = 0x21
    exploit_map = 224000102
    if field_id == exploit_map:# Do not need to attack in exploit map
        return
    if Character.IsOwnFamiliar(9960098) and level > 15 and job not in KinesisJobs:
        Terminal.SetSlider("sliderMP", 90) #use boogie to regen mana
        Terminal.SetComboBox("MPKey",4)
    else:
        Terminal.SetSlider("sliderMP", 20) #use potion to regen mana
        Terminal.SetComboBox("MPKey",6)

    if not SCLib.GetVar("DoingZakum") or not getSpider: #Ocassionaly use big spider (in zakum)
        Terminal.SetComboBox("Familiar0",1)

    if job in XenonJobs: #Solve Xenon Auto Ability point issues
        if Character.GetAP() < 70: 
            if Terminal.GetCheckBox("Auto AP"):
                Terminal.SetCheckBox("Auto AP",False)
        else:
            if not Terminal.GetCheckBox("Auto AP"):
                Terminal.SetCheckBox("Auto AP",True)
    else:
        if not Terminal.GetCheckBox("Auto AP"):
            Terminal.SetCheckBox("Auto AP",True)

    if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"): # kami control interupt by job adv script and zakum script
        noKami = [271030540,273020300,273040300]
        if field_id not in noKami:
            ToggleKami(on)
        elif field_id in noKami:
            ToggleKami(False)
    #print(SCLib.GetVar("DoingJobAdv"))
    if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum"):
        if Terminal.GetCheckBox("Legit Vac") and field_id not in mobFalldownBlacklist:# and not Terminal.GetCheckBox("Melee No Delay"):
            Terminal.SetCheckBox("Mob Falldown",on)
        else:
            if Terminal.GetCheckBox("Mob Falldown"):
                Terminal.SetCheckBox("Mob Falldown",False)
    else:
        Terminal.SetCheckBox("Mob Falldown",False)
    if Terminal.GetLineEdit("SISkillID") in SpeedyGonzalesList and Terminal.GetCheckBox("Skill Injection") and Terminal.GetCheckBox("Melee No Delay"):
        #print("In list")
        if not Terminal.GetCheckBox("Speedy Gonzales"):
            Terminal.SetCheckBox("Speedy Gonzales",True)
        if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("GettingBoogie") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"):
            if not Terminal.GetCheckBox("filter_etc"):
                Terminal.SetCheckBox("filter_etc",True)
            if not Terminal.GetCheckBox("filter_use"):
                Terminal.SetCheckBox("filter_use",True)
        else:
            if Terminal.GetCheckBox("filter_etc"):
                Terminal.SetCheckBox("filter_etc",False)
            if Terminal.GetCheckBox("filter_use"):
                Terminal.SetCheckBox("filter_use",False)
        #Terminal.SetSpinBox("FilterMeso",0)
        if level < 140:
            ToggleLoot(False)
    elif Terminal.GetLineEdit("SISkillID") in SpeedyGonzalesList:
        Terminal.SetCheckBox("Speedy Gonzales",True)
    elif job == BuccaneerJobs[1]:
        if not Terminal.GetCheckBox("Speedy Gonzales"):
            Terminal.SetCheckBox("Speedy Gonzales",True) 
    else:
        #if Terminal.GetCheckBox("Speedy Gonzales"):
        #    Terminal.SetCheckBox("Speedy Gonzales",False)
        if Terminal.GetCheckBox("filter_etc"):
            Terminal.SetCheckBox("filter_etc",False)
        if Terminal.GetCheckBox("filter_use"):
            Terminal.SetCheckBox("filter_use",False)
        if level < 140:
            Terminal.SetSpinBox("FilterMeso",0)
            
    #elif job == NightWalkerJobs[2] or job == NightWalkerJobs[3]:
    #    if not Terminal.GetCheckBox("Speedy Gonzales"):
    #        Terminal.SetCheckBox("Speedy Gonzales",True)
    if level > 60 and level < 120 and not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"):
        Terminal.SetCheckBox("Kami Loot",False)
        Terminal.SetCheckBox("Auto Loot",True)
    if job == 4200: #kanna first job
        AttackSI(42001006,on)
    elif job in KannaJobs and field_id in curbrockhideout:
        AttackSI(42001006,on)
    elif job == 4210: #kanna 2nd
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetSpinBox("SkillInjection", 100)
        Terminal.SetLineEdit("SISkillID","42001006")
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4211:#kanna 3rd
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 4212: #kanna 4th 
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetSpinBox("charm_delay",100)
            Terminal.SetCheckBox("charm_fma",False)
            Terminal.SetCheckBox("Summon Kishin",False)
            Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
            Terminal.SetSpinBox("autoattack_spin",7500)
            Terminal.SetComboBox("AttackKey",36)
            #Terminal.SetCheckBox("Skill Injection",False) #42111011
            AttackSemiNDMagic(42111000,42001006,0.70,on)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 2700: #lumi first job
        # 20040217 Dark Mode Buff
        # 20040216 Light Mode
        # 20040220 20040219 Equi Mode
        AttackSI(27001100,on,100,"SIRadioMagic")
    elif job in LuminousJobs and field_id in curbrockhideout:
        AttackAuto(27001201,on)
    elif job == 2710: #lumi second job
        if Character.HasBuff(2,20040217): #use dark magic
            #AttackAuto(27001201,on)
            AttackSI(27101202,on,200)
        else:
            #AttackSemiNDMagic(27101100,27101100,0.5,on)
            AttackAuto(27101100,on)
    elif job == 2711: #lumi third job
        if Character.HasBuff(2,20040216): #Light Mode
            AttackAuto(27101100,on)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            AttackSemiNDMagic(27111303,27111303,1.77,on)
        else:                              #Dark Mode
            #AttackAuto(27111202,on)
            AttackSI(27101202,on,200)
    elif job == 2712: #lumi fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,20040216): #Light Mode
                AttackAuto(27121100,on)
            elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
                AttackSemiNDMagic(27111303,27111303,1.77,on)
                #AttackAuto(27111303,on)
            else:                              #Dark Mode
                #AttackSemiNDOnce(27121202,27001201,0.96,on)
                AttackSI(27101202,on,200)
    elif job == 3101: #DA first job
        AttackAuto(31011000,on)
    elif job in DemonAvengerJobs and field_id in curbrockhideout:
        AttackAuto(31011000,on)
    elif job == 3120: #DA 2nd
        #AttackSemiNDMagic(31201010,31201010,0.66,on)
        AttackSIND(31201010,on,100)
        #AttackAuto(31011000,on)
    elif job == 3121 or job == 3122: #DA third job and fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(31211010,31211010,0.78,on)
    elif job == 3100 or job == 3110 or job == 3111: #DS first - third job
        #Key.Set(attack_key,1,31000004)31001008
        if SCLib.GetVar("DoingJobAdv"):
            AttackSI(31001008,100,on)
        else:
            AttackSemiNDMagic(31001008,31001008,0.55,on)
    elif job == 3112: #DS fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSI(31121010,on,16)
            AttackSemiNDMagic(31121010,31121010,0.66,on)
    elif job == 2300: #Mercedes 1st 
        AttackAuto(23001000,on)
    elif job in MercedesJobs and field_id in curbrockhideout:
        AttackAuto(23001000,on)
    elif job ==2310: #Mercedes 2nd
        AttackAuto(23101000,on)
        #AttackSIND(23101007,on,250)
        #AttackSIND(23100004,on,300)
    elif job ==2311: #Mercedes 3rd
        #AttackAuto(23111000,on)
        '''
        attack_key = 0x44
        Key.Set(attack_key,1,23111000)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetLineEdit("SISkillID",str(23111002))
        Terminal.SetSpinBox("SkillInjection",200)
        Terminal.SetCheckBox("Melee No Delay",on)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetCheckBox("Skill Injection", on)
        '''
        AttackSemiNDMagic(23111000,23111002,0.54,on)
        #AttackSIND(23111000,on,250)
    elif job == 2312: #Mercedes 4th
        #AttackAuto(23111000)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            '''
            attack_key = 0x44
            Key.Set(attack_key,1,23111000)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",100)
            Terminal.SetLineEdit("SISkillID",str(23111002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
            '''
            #AttackAuto(23111000,on)
            #AttackSIND(23120013,on,150)
            AttackSemiNDMagic(23120013,23111002,0.54,on)
    elif job == 4100: #Hayato 1st 41001004
        AttackSI(41001004,on,100)
    elif job in HayatoJobs and field_id in curbrockhideout:
        AttackSI(41001004,on,100)
    elif job == 4110: #Hayato 2nd 41101000
        AttackSemiNDMagic(41101000,41101000,0.45,on)
    elif job == 4111: #Hayato 3rd 41111011
        AttackSemiNDMagic(41111011,41111011,0.45,on)
    elif job == 4112: #Hayato 4th 41121011
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(41121011,41121011,0.45,on)
    elif job == 3600:#Xenon 1st 36001000
        AttackSemiNDMagic(36001000,36001000,1.08,on)
    elif job in XenonJobs and field_id in curbrockhideout:
        AttackSI(36001000,on,150)
    elif job == 3610:#Xenon 2nd 36101000
        AttackSemiNDMagic(36101000,36101000,0.99,on)
    elif job == 3611:#Xenon 3rd 36111000
        #AttackSemiNDMagic(36111000,36111000,1.8,on)
        AttackSemiNDMagic(36111009,36111009,0.81,on)
        #AttackSemiNDMagic(36111010,36111010,0.72,on)
    elif job == 3612:#Xenon 4th 36121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(36121001) >= 1:
                #AttackSemiNDMagic(36121011,36121011,1.38,on)
                SetSIND("36121011;36121000",150,on)
            else:
                AttackSI(36121000,on,110)
    elif job == 2400: #Phantom 1st 24001000
        AttackSemiNDMagic(24001000,24001000,0.81,on)
    elif job in PhantomJobs and field_id in curbrockhideout:
        AttackAuto(24001000,on)
    elif job == 2410: #Phantom 2nd 24101000
        AttackSemiNDMagic(24101000,24101000,0.99,on)
    elif job == 2411: #Phantom 3rd 24111000
        AttackSemiNDMagic(24111000,24111000,0.99,on)
    elif job == 2412: #Phantom 4th 24121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(24121010) >= 1 and Character.GetSkillLevel(24121000) >= 1:
                AttackSemiNDMagic(24121010,24121010,1.08,on)
                #SetSIND("24121010;24121000",140,on)
            elif Character.GetSkillLevel(24121010) >= 1:
                AttackSemiNDMagic(24121010,24121010,1.08,on)
            else:
                AttackSI(24121000,on,150)
    elif job == 15000: #Illium Pre 1st
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job in IlliumJobs: #Illium 1st+2nd+3rd+4th
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",on)
        Terminal.SetCheckBox("bot/illium/summon_control",on)
        Terminal.SetCheckBox("General FMA",on)
    elif job in CadenaJobs: #Cadena 1st + 2nd + 3rd 64001006 or 64001001
        if job != CadenaJobs[-1]:
            AttackSIND("64001001;64001006",on,100)
        else:
            if level >= 160 and Character.GetSkillLevel(32121052) == 1:
                #AttackSIND(32120055,32120055,0.45,on)
                #AttackSIND("32120055;64001001",on,100)
                AttackSemiNDMagic(32120055,32120055,0.45,on)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                BindSkill(32121052)
            else:
                AttackSIND("64120000;64001001",on,100)
    elif job in ArkJobs: #Ark 1st + 2nd + 3rd 155001100
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(155001100,155001100,0.85,on)
    elif job == 2001: #Evan pre 1st job
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 2200: #Evan 1st 22001010 AA
        AttackAuto(22001010,on)
    elif job in EvanJobs and field_id in curbrockhideout:
        if field_id == 600050020:
            AttackSIND(22110010,on,100)
        else:
            AttackAuto(22001010,on)
            Key.Set(attack_key,1,22001010)
    elif job == 2211: #Evan 2nd 22110010 SI/ND
        AttackSIND(22110010,on,100)
        
    elif job == 2214: #Evan 3rd 22140010 SI/ND
        AttackSIND(22140010,on,100)
        
    elif job == 2217: #Evan 4th 22170061 SI/ND
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(22170061,on,100)
        
    elif job == 0:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 100: #Swordman
        AttackAuto(1001005,on)
    elif job == 110: #fighter 1101011
        AttackAuto(1101011,on)
    elif job in HeroJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 111: #crusader 1111010
        #AttackSIND(1111010,on,450)
        AttackSemiNDMagic(1111010,1111010,0.85,on)
    elif job == 112: #Hero 1120017
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSIND(1120017,on,400)
            AttackSemiNDMagic(1120017,1120017,0.6,on)
    elif job == 120: #Page 1201011
        AttackSI(1201011,on)
    elif job in PaladinJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 121: #White knight 1211008
        #AttackAuto(1211008,on)
        AttackSI(1201011,on)
    elif job == 122: #Paladin 1211008
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1221004,1221004,0.81,on)
            '''
            while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame():
                for x in range(1,8,1):
                    Character.UseSkill(1221004)
                    time.sleep(0.02)
                time.sleep(0.02)
                Character.UseSkill(1221004)
                time.sleep(0.80)
            '''
    elif job == 130: #Spearman 1301011
        AttackSemiND(1301011,1301011,0.81,on)
        
    elif job in DarkknightJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 131: #Berserker
        AttackSemiND(1301011,1301011,0.81,on)
        
    elif job == 132: #Dark Knight
        #AttackAuto(1321012,on)
        #AttackSIND(1321012,on,450)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1321012,1321012,0.84,on)
    elif job == 200: #Mage
        AttackAuto(2001008,on)
        
    elif job in ILMageJobs and field_id in curbrockhideout: #1001005
        AttackAuto(2001008,on)
    elif job == 220: #IL wizard
        AttackAuto(2201005,on)
        
    elif job == 221: #IL mage
        AttackAuto(2211002,on)
        
    elif job == 222: #IL archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2221006,on)

        
    elif job in FPMageJobs and field_id in curbrockhideout: #1001005
        AttackSI(2101004,on,100,"SIRadioMagic") 
    elif job == 210: #FP wizard
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 211: #FP mage
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 212: #FP archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2121006,on)
        
    elif job in BishopJobs and field_id in curbrockhideout: #1001005
        AttackAuto(2001008,on)
    elif job == 230: #cleric
        AttackAuto(2301005,on)
    elif job == 231: #priest
        AttackAuto(2311004,on)
    elif job == 232: #Bishop
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackSI(2321007,on,100,"SIRadioMagic")
    elif job == 300: #Archer
        AttackAuto(3001004,on)
        
    elif (job in BowmasterJobs or job in MarksmanJobs) and field_id in curbrockhideout: #1001005
        AttackAuto(3001004,on)
    elif job == 310: #Hunter
        AttackAuto(3101005,on)
        
    elif job == 311: #Ranger
        AttackAuto(3111003,on)
        #AttackSIND(3111003,on,300)
        
    elif job == 312: #Bowmaster
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(3121015,on,600)
        
    elif job == 320: #Crossbowman
        AttackAuto(3201005,on)
    elif job == 321: #Sniper
        AttackAuto(3211009,on)
        #AttackSIND(3211009,on,400)
    elif job == 322: #Marksman
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(3221017,on)
    elif job == 400: #Thief
        
        if SCLib.GetVar("DualBlade"):
            if Character.GetSkillLevel(4001013) == 0:
                LevelSkill(4001013)
            AttackAuto(4001013,on)
        else:
            AttackAuto(4001334,on)
        if Character.GetSkillLevel(4001013) >= 1:
            SCLib.UpdateVar("DualBlade",True)
        else:
            SCLib.UpdateVar("DualBlade",False)
        
    elif job == 410: #Assassin
        AttackSI(4101008,on)
        
    elif job in NightlordJobs and field_id in curbrockhideout: #1001005
        AttackAuto(4101008,on)
    elif job == 411: #Hermit
        AttackSI(4111015,on)
        
    elif job == 412: #nightlord
        #print(Character.GetSkillLevel(32121052))
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetSpinBox("KamiOffsetX", -85)
            if Character.GetSkillLevel(4121017) >= 1:
                AttackSemiNDMagic(4121017,4121017,1.0,on)
            else:
                AttackSI(4111015,on)
        
    elif job == 420: #Bandit
        AttackSI(4201012,on)
        
    elif job in ShadowerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(4001334,on)
    elif job == 421: #Chief Bandit
        AttackSI(4211002,on)
        
    elif job == 422: #Shadower
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(4221007,on)
            #AttackSemiNDMagic(4221007,4221007,1.1,on)
        
    elif job == 430: #dualblade
        if Character.GetSkillLevel(4001013) == 0:
            LevelSkill(4001013)
        elif Character.GetSkillLevel(4000012) < 10:
            LevelSkill(4000012)
        elif Character.GetSkillLevel(4001011) < 5:
            LevelSkill(4001011)
        elif Character.GetSkillLevel(4001003) < 10:
            LevelSkill(4001003)
        elif Character.GetSkillLevel(4001013) < 10:
            LevelSkill(4001013)
        AttackAuto(4001013,on)
    elif job == 431: #dualblade
        AttackAuto(4001013,on)
    elif job == 432:
        AttackSIND(4321004,on,450)
    elif job == 433:
        #AttackAuto(4321004,on)
        AttackSIND(4321004,on,450)
    elif job == 434: #dual blade 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(4341004,4341004,0.74,on)
    elif job == 500: #Pirate
        AttackAuto(5001002,on)
    elif job == 501: #Cannoneer Pirate
        #AttackAuto(5011000,on)
        AttackSIND(5011002,on,200)
    elif job in BuccaneerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5101012,on)
    elif job in CorsairJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5201001,on)
    elif job == 510: #Brawler
        AttackAuto(5101012,on)
    elif job == 511: #Marauder
        AttackAuto(5111002,on)
    elif job == 512: #Buccaneer
        #AttackAuto(5121007,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5121017,5121007,1.25,on)
    elif job == 520: #Gunslinger
        AttackAuto(5201001,on)
    elif job == 521: #Outlaw
        AttackAuto(5211008,on)
    elif job == 522: #Corsair
        #if level < 160:
        #    AttackSIND(5221017,on,350)
        #else:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5221017,5221017,0.85,on)
    elif job == 530: #Cannoneer
        #AttackAuto(5301001,on)
        #AttackSIND(5011002,on,200)
        if Character.GetSkillLevel(5301000) >= 1:
            AttackSIND("5301000;5011002",on,300)
            #AttackSemiNDMagic(5301000,5301000,0.90,on)
        else:
            attack_key = 0x44
            Key.Set(attack_key,1,5301001)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",400)
            Terminal.SetLineEdit("SISkillID",str(5011002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
    elif job in CannoneerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5301001,on)
    elif job == 531: #Cannon Trooper
        '''
        if Terminal.GetCheckBox("Mob Falldown"):
            AttackAuto(5311000,on)
        else:
            AttackAuto(5301001,on)
            Terminal.SetCheckBox("Speedy Gonzales",True)
        '''
        if Character.GetSkillLevel(5311000) >= 1:
            #AttackSemiNDMagic(5311000,5311000,0.96,on)
            AttackSIND("5311000;5011002",on,250)
        else:
            attack_key = 0x44
            Key.Set(attack_key,1,5301001)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",400)
            Terminal.SetLineEdit("SISkillID",str(5011002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
    elif job == 532: #Cannon Master
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND("5321000;5011002",on,250)
            #AttackSemiNDMagic(5321000,5321000,0.95,on)
    elif job == 508: #Jett 1sts
        AttackAuto(5081020,on)
    elif job in JettJobs and field_id in curbrockhideout:
        AttackAuto(5081020,on)
    elif job == 570: #Jett 2nd
        #AttackAuto(5081020,on)
        if Character.GetSkillLevel(5701011) >= 1:
            #AttackSemiNDMagic(5701011,5701011,0.2,on,attackSpeed=4)
            AttackSIND(5701011,on,150)
        else:
            AttackAuto(5701010,on)
    elif job == 571: #Jett 3rd
        if Character.GetSkillLevel(5710020) >= 1:
            #AttackSemiNDMagic(5710020,5710020,0.9,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
        else:
            AttackSIND(5701011,on,150)
    elif job == 572: #Jett 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSemiNDMagic(5710020,5710020,0.4,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
    elif job == 1100: #Dawn warrior 1st
        AttackSI(11001020,on)
    elif job in DawnWarriorJobs and field_id in curbrockhideout: #1001005
        AttackAuto(11001020,on)
    elif job == 1110: #Dawn Warrior 2nd
        #AttackAuto(11101120,on)
        AttackSIND(11101120,on,600)
    elif job == 1111: #Dawn Warrior 3rd
        AttackSI(11111120,on)
        #AttackAuto(11111220,on)
    elif job == 1112: #Dawn Warrior 4th
        dummySkill = 11001020
        dummyDelay = 0.81
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,11111022):
                AttackSemiNDMagic(11121203,dummySkill,dummyDelay,on)
    elif job == 1200: #BW 1st
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
        ToggleLoot(False)
    elif job in BlazeWizardJobs and field_id in curbrockhideout: #1001005
        AttackAuto(12001021,on)
        Terminal.SetCheckBox("Full Map Attack",False)
    elif job == 1210: #BW 2nd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1211: #BW 3rd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1212: #BW 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:           
            #if level < 140:
            Terminal.SetCheckBox("Full Map Attack",True)
            AttackAuto(12001020,on)
                
            #elif level >= 140:
            #    Terminal.SetCheckBox("Full Map Attack",False)
            #    AttackSIND(12121055,on,31)
            
    elif job == 1300: #Wind Archer 1st
        AttackAuto(13001020,on)
    elif job in WindArcherJobs and field_id in curbrockhideout: #1001005
        AttackAuto(13001020,on)
    elif job == 1310: #Wind Archer 2nd
        if Character.GetSkillLevel(13101020) >= 1:
            AttackSI(13101020,on)
        else:
            AttackAuto(13001020,on)
    elif job == 1311: #Wind Archer 3rd
        #AttackAuto(13111020,on)
        AttackSI(13101020,on)
    elif job == 1312: #Wind Archer 4th
        #AttackAuto(13121002,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(13121002,on,siOption = "SIRadioShoot")
    elif job == 1400: #Night Walker 1st
        AttackAuto(14001020,on)
    elif job in NightWalkerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(14001020,on)
    elif job == 1410: #Night Walker 2nd
        AttackSI(14101020,on)
    elif job == 1411: #Night Walker 3rd
        AttackAuto(14111022,on)
    elif job == 1412: #Night Walker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(14111022,on)
    elif job == 1500: #Thunder breaker 1st
        #AttackAuto(15001020,on)
        if Character.GetSkillLevel(15001021) >= 1:
            #AttackSIND(15001021,on,600)
            AttackSemiNDMagic(15001021,15001021,0.8,on)
        else:
            AttackAuto(15001020,on)
    elif job in ThunderBreakerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(15001020,on)
    elif job == 1510: #Thunder breaker 2nd
        #AttackAuto(15101020,on)
        AttackSemiNDMagic(15101020,15101020,0.72,on)
    elif job == 1511: #Thunder breaker 3rd
        #AttackAuto(15111020,on)
        AttackSemiNDMagic(15111020,15111020,0.9,on)
    elif job == 1512: #Thunder breaker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(15121002,15121002,1.08,on)
            #30 * math.ceil(BaseDelay * (14)/480)
            #AttackSIND(15121002,on,500)
        #AttackSIND(15111020,on,300)
        #AttackAuto(15121001,on)
    elif job == 3300: #Wild Hunter 1st
        AttackAuto(33001105,on)
    elif job in WildHunterJobs and field_id in curbrockhideout: #1001005
        AttackAuto(33001105,on)
    elif job == 3310: #Wild Hunter 2nd
        #AttackAuto(33101113,on)
        AttackSI(33101215,on)
    elif job == 3311: #Wild Hunter 3rd
        AttackAuto(33111112,on)
        #AttackSI(33111010,on,100,"SIRadioMagic")
    elif job == 3312: #Wild Hunter 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(33111112,on) 
            #AttackSemiNDMagic(33121016,33121016,1.1,on)
    elif job == 3200: #Battle Mage 1st
        AttackSI(32001014,on)
    elif job in BattleMageJobs and field_id in curbrockhideout: #1001005
        AttackSI(32001014,on)
    elif job == 3210: #Battle Mage 2nd
        #AttackSI(32100010,on)
        AttackSIND(32101001,on,250)
    elif job == 3211: #Batlle Mage 3rd
        #AttackSI(32110017,on)
        AttackSIND(32101001,on,250)
    elif job == 3212: #Battle Mage 4th
        if level >= 160:
            if level >= 160 and Character.GetSkillLevel(32121052) == 1:
                AttackSemiNDMagic(32120055,32120055,0.45,on)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            if SCLib.GetVar("DoingZakum"):
                #AttackAuto(32121002,on)
                AttackSIND(32101001,on,250)
            else:
                #AttackSI(32120019,on)
                AttackSIND(32101001,on,250)
    elif job == 3700: #Blaster 1st
        Terminal.SetCheckBox("General FMA",False)
        if Character.GetSkillLevel(37001004) >= 1:
            AttackSIND(37001004,on,80)
        else:
            AttackAuto(37001000,on)
    elif job in BlasterJobs and field_id in curbrockhideout: #1001005
        #Terminal.SetCheckBox("General FMA",on)
        Terminal.SetCheckBox("General FMA",False)
        if Character.GetSkillLevel(37001004) >= 1:
            AttackSIND(37001004,on,80)
        else:
            AttackAuto(37001000,on)
    elif job == 3710: #Blaster 2nd
        #Terminal.SetCheckBox("General FMA",on)
        Terminal.SetCheckBox("General FMA",False)
        if Character.GetSkillLevel(37001004) >= 1:
            AttackSIND(37001004,on,80)
        else:
            AttackAuto(37001000,on)
    elif job == 3711: #Blaster 3rd
        #AttackAuto(37001000,on)
        AttackSI(37110006,on,80)
        Terminal.SetCheckBox("General FMA",on)
        #Terminal.SetCheckBox("General FMA",on)
    elif job == 3712: #Blaster 4th
        #AttackAuto(37001000,on)
        Terminal.SetCheckBox("General FMA",False)
        vulcan()
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(37121000,on,80)
    elif job == 3500: #Mechanic 1st
        AttackAuto(35001004,on)
    elif job in MechanicJobs and field_id in curbrockhideout: #1001005
        AttackAuto(35001004,on)
    elif job == 3510: #Mechanic 2nd
        AttackAuto(35101001,on)
    elif job == 3511: #Mechanic 3rd
        AttackAuto(35111006,on)
    elif job == 3512: #Mechanic 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2, 35001002):
                AttackSemiNDMagic(35111015,35111015,0.84,on)
            #AttackSI(35121015,on,250)
        #AttackAuto(35111006,on)
    elif job == 11212: #Beast Tamer
        #if level >= 160 and Character.GetSkillLevel(32121052) == 1:
        #    AttackSemiNDMagic(32120055,32120055,0.45,on)
        #elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
        #    BindSkill(32121052)
        #else:
        if Character.HasBuff(2,110001501):
            if Character.GetSkillLevel(112000003) >= 1:
                #AttackSIND(112000003,on,450)
                AttackSemiNDMagic(112000003,112001008,0.38,on)
            else:
                if level <= 17:
                    AttackAuto(112000000,on)
                    
                elif level >= 17 and (not useExploit or SCLib.GetVar("DoingZakum")):
                    Terminal.SetCheckBox("Auto Attack", False)
                    Terminal.SetCheckBox("Skill Injection", False)
                    Terminal.SetCheckBox("Melee No Delay",False)
                    count = 0
                    if on and not Terminal.IsRushing():
                        while count < 100 and len(Field.GetMobs())>0: #constantly presses control to simulate human actions
                            Key.Down(0x11)
                            time.sleep(0.1)
                            Key.Up(0x11)
                            time.sleep(0.1)
                            count += 1
                            if len(Field.GetMobs())==0:
                                break
    elif job == 2000:#Aran pre
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
        
    elif job == 2100:# or job == 2110: #Aran 1st 21000007
        AttackSI(21000006,on,80)
        #AttackSemiNDMagic(21000006,21000006,0.4,on)

    elif job == 2110:
        SetSIND("21000007;21100018",100,on)

    elif job == 2111 or job == 2112: #Aran 3rd
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSemiNDMagic(21111021,21111021,0.81,on)
            SetSIND("21110028;21100018",100,on)

            #if Character.HasBuff(2,21110016):
            #    AttackSIND(21111021,on,450)
            #else:
            #    AttackSIND(21111021,on,400)
            #AttackSemiNDMagic(21111021,21111021,0.65,on)
            #Terminal.SetCheckBox("Speedy Gonzales",True)
            '''
            elif job == 2110 or job == 2111 or job == 2112: #Aran 2nd+3rd+4th 21000007
                Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
                Key.Set(attack_key,1,21001010)
                Terminal.SetLineEdit("SISkillID","21100018")
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetSpinBox("SkillInjection",30)
                Terminal.SetCheckBox("Auto SP",True)
                Terminal.SetCheckBox("Melee No Delay",on)
                #Terminal.SetRadioButton("SIRadioMagic",True)
                Terminal.SetCheckBox("Auto Attack", False)
                Terminal.SetComboBox("AttackKey",33)
                Terminal.SetSpinBox("autoattack_spin",100)
            '''
    elif job == 14200:# Kinesis 1st
        AttackSemiNDMagic(142001001,142001001,0.63,on,attackSpeed = 5)
    elif job in KinesisJobs and field_id in curbrockhideout:
        AttackAuto(142001001,on)
    elif job == 14210: #Kinesis 2nd 142101002
        AttackSemiNDMagic(142101002,142101002,0.79,on,attackSpeed = 5)
        #AttackAuto(142101002,on)
    elif job == 14211 or job == 14212: #Kinesis 3rd + 4th 142111002
        #
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if job == 14211:
                Terminal.SetCheckBox("Instant Final Smash",True)
            else:
                Terminal.SetCheckBox("Instant Final Smash",False)
            AttackAuto(142111002,on)
            #AttackSemiNDMagic(142101002,142101002,0.79,on,attackSpeed = 5)
        
    elif job == 6500: #AB 1st
        AttackSemiNDMagic(60011216,60011216,0.6,on)
    elif job == 6510: #AB 2nd
        AttackSemiNDMagic(65001100,65001100,0.57,on)
    elif job == 6511: #AB 3rd
        #AttackSI(65111002,on,100,"SIRadioMagic")
        AttackSemiNDMagic(65111002,65111002,1.2,on)
    elif job == 6512: #AB 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if SCLib.GetVar("DoingZakum"):
                AttackSI(65121008,on)
            else:
                AttackSemiNDMagic(65121100,65111002,1.2,on)
    elif job in KaiserJobs and job != KaiserJobs[3]: #Kaiser 1st 2nd 3rd 4th
        AttackSemiNDMagic(61001005,61001005,0.36,on)
    elif job == KaiserJobs[3]:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(61001005,61001005,0.36,on)
    elif job == 2500: #Shade 1st
        AttackAuto(25001000,on)
    elif job == 2510: #Shade 2nd
        AttackSemiNDMagic(25101000,25101000,0.75,on)
    elif job == 2511: #Shade 3rd
        AttackSIND(25110001,on,300)
        #AttackSemiNDMagic(25110001,2511001,0.99,on)
        #AttackSIND(25111000,on,800)
    elif job == 2512: #Shade 4th
        #AttackSI(25120003,on,100)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(25121000) >= 1:
                AttackSemiNDMagic(25121000,25121000,0.63,on)
            else:
                AttackSIND(25110001,on,300)
    elif job == 5100: #Mihile 1st
        AttackAuto(51001004,on)
        #AttackSemiNDMagic(51001004,51001004,0.96,on)
    elif job in MihileJobs and field_id in curbrockhideout:
        AttackAuto(51001004,on)
    elif job == 5110: #Mihile 2nd
        #AttackSIND(51101005,on,800)
        AttackSemiNDMagic(51101005,51001004,0.96,on)
    elif job == 5111: #Mihile 3rd
        AttackSemiNDMagic(51111006,51111006,0.84,on)
        #AttackSIND(51111006,on,600)
    elif job == 5112: #Mihile 4th
        delay = 0.84
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(51121009,51111006,0.84,on)
            #AttackSIND(51121009,on,400)
    elif job == 301:
        AttackSIND(3011004,on,1,siOption = "bot/si_cadena")
    elif job == 330 or job == 331 or job == 332:
        AttackSIND(3301003,on,1,siOption = "bot/si_cadena")
        Terminal.SetCheckBox("General FMA",on)
    else:
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Skill Injection", False)
        #print("Not any of the listed jobs, not going to attack for safety")
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)

def ToggleAttackQuest(on):
    attack_key = 0x44
    pgup_key = 0x21
    exploit_map = 224000102
    if field_id == exploit_map:# Do not need to attack in exploit map
        return
    if Character.IsOwnFamiliar(9960098) and level > 15 and job not in KinesisJobs:
        Terminal.SetSlider("sliderMP", 90) #use boogie to regen mana
        Terminal.SetComboBox("MPKey",4)
    else:
        Terminal.SetSlider("sliderMP", 20) #use potion to regen mana
        Terminal.SetComboBox("MPKey",6)

    if not SCLib.GetVar("DoingZakum") or not getSpider: #Ocassionaly use big spider (in zakum)
        Terminal.SetComboBox("Familiar0",1)

    if job in XenonJobs: #Solve Xenon Auto Ability point issues
        if Character.GetAP() < 70: 
            if Terminal.GetCheckBox("Auto AP"):
                Terminal.SetCheckBox("Auto AP",False)
        else:
            if not Terminal.GetCheckBox("Auto AP"):
                Terminal.SetCheckBox("Auto AP",True)
    else:
        if not Terminal.GetCheckBox("Auto AP"):
            Terminal.SetCheckBox("Auto AP",True)

    if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"): # kami control interupt by job adv script and zakum script
        ToggleKami(on)
    #print(SCLib.GetVar("DoingJobAdv"))
    if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum"):
        if Terminal.GetCheckBox("Legit Vac") and Terminal.GetCheckBox("Kami Vac") and field_id not in mobFalldownBlacklist:# and not Terminal.GetCheckBox("Melee No Delay"):
            Terminal.SetCheckBox("Mob Falldown",on)
        else:
            if Terminal.GetCheckBox("Mob Falldown"):
                Terminal.SetCheckBox("Mob Falldown",False)
    else:
        Terminal.SetCheckBox("Mob Falldown",False)
    if Terminal.GetLineEdit("SISkillID") in SpeedyGonzalesList and Terminal.GetCheckBox("Skill Injection") and Terminal.GetCheckBox("Melee No Delay"):
        #print("In list")
        if not Terminal.GetCheckBox("Speedy Gonzales"):
            Terminal.SetCheckBox("Speedy Gonzales",True)
        if not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("GettingBoogie") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"):
            if not Terminal.GetCheckBox("filter_etc"):
                Terminal.SetCheckBox("filter_etc",True)
            if not Terminal.GetCheckBox("filter_use"):
                Terminal.SetCheckBox("filter_use",True)
        else:
            if Terminal.GetCheckBox("filter_etc"):
                Terminal.SetCheckBox("filter_etc",False)
            if Terminal.GetCheckBox("filter_use"):
                Terminal.SetCheckBox("filter_use",False)
        #Terminal.SetSpinBox("FilterMeso",50000)
    elif Terminal.GetLineEdit("SISkillID") in SpeedyGonzalesList:
        Terminal.SetCheckBox("Speedy Gonzales",True)
    elif job == BuccaneerJobs[1]:
        if not Terminal.GetCheckBox("Speedy Gonzales"):
            Terminal.SetCheckBox("Speedy Gonzales",True) 
    else:
        if Terminal.GetCheckBox("Speedy Gonzales"):
            Terminal.SetCheckBox("Speedy Gonzales",False)
        if Terminal.GetCheckBox("filter_etc"):
            Terminal.SetCheckBox("filter_etc",False)
        if Terminal.GetCheckBox("filter_use"):
            Terminal.SetCheckBox("filter_use",False)
        if level < 140:
            Terminal.SetSpinBox("FilterMeso",0)
            
    #elif job == NightWalkerJobs[2] or job == NightWalkerJobs[3]:
    #    if not Terminal.GetCheckBox("Speedy Gonzales"):
    #        Terminal.SetCheckBox("Speedy Gonzales",True)
    if level > 60 and level < 120 and not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingBeach") and not SCLib.GetVar("DoingSleepy"):
        Terminal.SetCheckBox("Kami Loot",False)
        Terminal.SetCheckBox("Auto Loot",True)
    if job == 4200: #kanna first job
        AttackSI(42001006,on)
    elif job in KannaJobs and field_id in curbrockhideout:
        AttackSI(42001006,on)
    elif job == 4210: #kanna 2nd
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetSpinBox("SkillInjection", 100)
        Terminal.SetLineEdit("SISkillID","42001006")
        Terminal.SetCheckBox("Skill Injection",True)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 4211:#kanna 3rd
        Terminal.SetSpinBox("charm_delay",100)
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("Skill Injection",False)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 4212: #kanna 4th 
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetSpinBox("charm_delay",100)
            Terminal.SetCheckBox("charm_fma",False)
            Terminal.SetCheckBox("Summon Kishin",False)
            Terminal.SetCheckBox("MonkeySpiritsNDcheck",False)
            Terminal.SetSpinBox("autoattack_spin",7500)
            Terminal.SetComboBox("AttackKey",36)
            Terminal.SetCheckBox("Skill Injection",False) #42111011
            #AttackSemiNDMagic(42111000,42001006,0.70,on)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetSpinBox("autoattack_spin",7500)
        Terminal.SetComboBox("AttackKey",36)
        Terminal.SetCheckBox("bot/summon_kami",False)
        Key.Set(0x47,1,42111003) #kishin
    elif job == 2700: #lumi first job
        # 20040217 Dark Mode Buff
        # 20040216 Light Mode
        # 20040220 20040219 Equi Mode
        AttackSI(27001100,on,100,"SIRadioMagic")
    elif job in LuminousJobs and field_id in curbrockhideout:
        AttackAuto(27001201,on)
    elif job == 2710: #lumi second job
        if Character.HasBuff(2,20040217): #use dark magic
            #AttackAuto(27001201,on)
            AttackSI(27101202,on,200)
        else:
            #AttackSemiNDMagic(27101100,27101100,0.5,on)
            AttackAuto(27101100,on)
    elif job == 2711: #lumi third job
        if Character.HasBuff(2,20040216): #Light Mode
            AttackAuto(27101100,on)
        elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
            AttackSemiNDMagic(27111303,27111303,1.77,on)
        else:                              #Dark Mode
            #AttackAuto(27111202,on)
            AttackSI(27101202,on,200)
    elif job == 2712: #lumi fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,20040216): #Light Mode
                AttackAuto(27121100,on)
            elif Character.HasBuff(2,20040220) or Character.HasBuff(2,20040219): #Equi Mode
                AttackSemiNDMagic(27111303,27111303,1.77,on)
                #AttackAuto(27111303,on)
            else:                              #Dark Mode
                #AttackSemiNDOnce(27121202,27001201,0.96,on)
                AttackSI(27101202,on,200)
    elif job == 3101: #DA first job
        AttackAuto(31011000,on)
    elif job in DemonAvengerJobs and field_id in curbrockhideout:
        AttackAuto(31011000,on)
    elif job == 3120: #DA 2nd
        #AttackSemiNDMagic(31201010,31201010,0.66,on)
        AttackSIND(31201010,on,100)
        #AttackAuto(31011000,on)
    elif job == 3121 or job == 3122: #DA third job and fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(31211010,on)
    elif job == 3100 or job == 3110 or job == 3111: #DS first - third job
        #Key.Set(attack_key,1,31000004)31001008
        if SCLib.GetVar("DoingJobAdv"):
            AttackSI(31001008,100,on)
        else:
            AttackSI(31001008,on)
    elif job == 3112: #DS fourth job
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSI(31121010,on,16)
            AttackSemiNDMagic(31121010,31121010,0.66,on)
    elif job == 2300: #Mercedes 1st 
        AttackAuto(23001000,on)
    elif job in MercedesJobs and field_id in curbrockhideout:
        AttackAuto(23001000,on)
    elif job ==2310: #Mercedes 2nd
        AttackAuto(23101000,on)
        #AttackSIND(23101007,on,250)
        #AttackSIND(23100004,on,300)
    elif job ==2311: #Mercedes 3rd
        #AttackAuto(23111000,on)
        '''
        attack_key = 0x44
        Key.Set(attack_key,1,23111000)
        Terminal.SetComboBox("AttackKey",33)
        Terminal.SetSpinBox("autoattack_spin",100)
        Terminal.SetLineEdit("SISkillID",str(23111002))
        Terminal.SetSpinBox("SkillInjection",200)
        Terminal.SetCheckBox("Melee No Delay",on)
        Terminal.SetRadioButton("SIRadioMelee",True)
        Terminal.SetCheckBox("Auto Attack",on)
        Terminal.SetCheckBox("Skill Injection", on)
        '''
        AttackAuto(23111000,on)
        #AttackSemiNDMagic(23111000,23111002,0.54,on)
        #AttackSIND(23111000,on,250)
    elif job == 2312: #Mercedes 4th
        #AttackAuto(23111000)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            '''
            attack_key = 0x44
            Key.Set(attack_key,1,23111000)
            Terminal.SetComboBox("AttackKey",33)
            Terminal.SetSpinBox("autoattack_spin",100)
            Terminal.SetLineEdit("SISkillID",str(23111002))
            Terminal.SetSpinBox("SkillInjection",200)
            Terminal.SetCheckBox("Melee No Delay",on)
            Terminal.SetRadioButton("SIRadioMelee",True)
            Terminal.SetCheckBox("Auto Attack",on)
            Terminal.SetCheckBox("Skill Injection", on)
            '''
            #AttackAuto(23111000,on)
            #AttackSIND(23120013,on,150)
            AttackSemiNDMagic(23120013,23111002,0.54,on)
    elif job == 4100: #Hayato 1st 41001004
        AttackSI(41001004,on,100)
    elif job in HayatoJobs and field_id in curbrockhideout:
        AttackSI(41001004,on,100)
    elif job == 4110: #Hayato 2nd 41101000
        AttackSI(41101000,on,100)
    elif job == 4111: #Hayato 3rd 41111011
        AttackSI(41111011,on,100)
    elif job == 4112: #Hayato 4th 41121011
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(41121011,41121011,0.45,on)
    elif job == 3600:#Xenon 1st 36001000
        AttackSI(36001000,on)
    elif job in XenonJobs and field_id in curbrockhideout:
        AttackSI(36001000,on,150)
    elif job == 3610:#Xenon 2nd 36101000
        AttackSI(36101000,on)
    elif job == 3611:#Xenon 3rd 36111000
        #AttackSemiNDMagic(36111000,36111000,1.8,on)
        AttackSI(36111009,on)
        #AttackSemiNDMagic(36111010,36111010,0.72,on)
    elif job == 3612:#Xenon 4th 36121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(36121001) >= 1:
                #AttackSemiNDMagic(36121011,36121011,1.38,on)
                SetSIND("36121011;36121000",150,on)
            else:
                AttackSI(36121000,on,110)
    elif job == 2400: #Phantom 1st 24001000
        AttackSI(24001000,on)
    elif job in PhantomJobs and field_id in curbrockhideout:
        AttackAuto(24001000,on)
    elif job == 2410: #Phantom 2nd 24101000
        AttackSI(24101000,on)
    elif job == 2411: #Phantom 3rd 24111000
        AttackSI(24111000,on)
    elif job == 2412: #Phantom 4th 24121000
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(24121010) >= 1 and Character.GetSkillLevel(24121000) >= 1:
                #AttackSemiNDMagic(24121010,24121010,1.08,on)
                SetSIND("24121010;24121000",150,on)
            elif Character.GetSkillLevel(24121010) >= 1:
                AttackSemiNDMagic(24121010,24121010,1.08,on)
            else:
                AttackSI(24121000,on,150)
    elif job == 15000: #Illium Pre 1st
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job in IlliumJobs: #Illium 1st+2nd+3rd+4th
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack",False)
        
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",on)
        Terminal.SetCheckBox("bot/illium/summon_control",on)
        Terminal.SetCheckBox("General FMA",on)
    elif job in CadenaJobs: #Cadena 1st + 2nd + 3rd 64001006 or 64001001
        if job != CadenaJobs[-1]:
            AttackSIND("64001001;64001006",on,100)
        else:
            AttackSIND("64120000;64001001",on,100)
    elif job in ArkJobs: #Ark 1st + 2nd + 3rd 155001100
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(155001100,on)
    elif job == 2001: #Evan pre 1st job
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 2200: #Evan 1st 22001010 AA
        AttackAuto(22001010,on)
    elif job in EvanJobs and field_id in curbrockhideout:
        if field_id == 600050020:
            AttackSIND(22110010,on,100)
        else:
            AttackAuto(22001010,on)
            Key.Set(attack_key,1,22001010)
    elif job == 2211: #Evan 2nd 22110010 SI/ND
        AttackSIND(22110010,on,100)
        
    elif job == 2214: #Evan 3rd 22140010 SI/ND
        AttackSIND(22140010,on,100)
        
    elif job == 2217: #Evan 4th 22170061 SI/ND
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(22170061,on,100)
        
    elif job == 0:
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
    elif job == 100: #Swordman
        AttackAuto(1001005,on)
    elif job == 110: #fighter 1101011
        AttackAuto(1101011,on)
    elif job in HeroJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 111: #crusader 1111010
        AttackSIND(1111010,on,450)
    elif job == 112: #Hero 1120017
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(1120017,on,400)
            #AttackSemiNDMagic(1120017,1120017,0.4,on)
    elif job == 120: #Page 1201011
        AttackSI(1201011,on)
    elif job in PaladinJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 121: #White knight 1211008
        #AttackAuto(1211008,on)
        AttackSI(1201011,on)
    elif job == 122: #Paladin 1211008
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1221004,1221004,0.81,on)
            '''
            while Field.GetCharacterCount()<=1 and Field.GetEliteState() !=2 and len(Field.GetMobs())>0 and not Terminal.IsRushing() and GameState.IsInGame():
                for x in range(1,8,1):
                    Character.UseSkill(1221004)
                    time.sleep(0.02)
                time.sleep(0.02)
                Character.UseSkill(1221004)
                time.sleep(0.80)
            '''
    elif job == 130: #Spearman 1301011
        AttackSI(1301011,on)
        
    elif job in DarkknightJobs and field_id in curbrockhideout: #1001005
        AttackAuto(1001005,on)
    elif job == 131: #Berserker
        AttackSI(1301011,on)
        
    elif job == 132: #Dark Knight
        #AttackAuto(1321012,on)
        #AttackSIND(1321012,on,450)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(1321012,1321012,0.84,on)
    elif job == 200: #Mage
        AttackAuto(2001008,on)
        
    elif job in ILMageJobs and field_id in curbrockhideout: #1001005
        AttackAuto(2001008,on)
    elif job == 220: #IL wizard
        AttackAuto(2201005,on)
        
    elif job == 221: #IL mage
        AttackAuto(2211002,on)
        
    elif job == 222: #IL archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2221006,on)

        
    elif job in FPMageJobs and field_id in curbrockhideout: #1001005
        AttackSI(2101004,on,100,"SIRadioMagic") 
    elif job == 210: #FP wizard
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 211: #FP mage
        AttackSI(2101004,on,100,"SIRadioMagic") 
        
    elif job == 212: #FP archmage
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackAuto(2121006,on)
        
    elif job in BishopJobs and field_id in curbrockhideout: #1001005
        AttackAuto(2001008,on)
    elif job == 230: #cleric
        AttackAuto(2301005,on)
    elif job == 231: #priest
        AttackAuto(2311004,on)
    elif job == 232: #Bishop
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            AttackSI(2321007,on,100,"SIRadioMagic")
    elif job == 300: #Archer
        AttackAuto(3001004,on)
        
    elif (job in BowmasterJobs or job in MarksmanJobs) and field_id in curbrockhideout: #1001005
        AttackAuto(3001004,on)
    elif job == 310: #Hunter
        AttackAuto(3101005,on)
        
    elif job == 311: #Ranger
        AttackAuto(3111003,on)
        #AttackSIND(3111003,on,300)
        
    elif job == 312: #Bowmaster
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(3121015,on,600)
        
    elif job == 320: #Crossbowman
        AttackAuto(3201005,on)
    elif job == 321: #Sniper
        AttackAuto(3211009,on)
        #AttackSIND(3211009,on,400)
    elif job == 322: #Marksman
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(3221017,on)
    elif job == 400: #Thief
        
        if SCLib.GetVar("DualBlade"):
            if Character.GetSkillLevel(4001013) == 0:
                LevelSkill(4001013)
            AttackAuto(4001013,on)
        else:
            AttackAuto(4001334,on)
        if Character.GetSkillLevel(4001013) >= 1:
            SCLib.UpdateVar("DualBlade",True)
        else:
            SCLib.UpdateVar("DualBlade",False)
        
    elif job == 410: #Assassin
        AttackSI(4101008,on)
        
    elif job in NightlordJobs and field_id in curbrockhideout: #1001005
        AttackAuto(4101008,on)
    elif job == 411: #Hermit
        AttackSI(4111015,on)
        
    elif job == 412: #nightlord
        #print(Character.GetSkillLevel(32121052))
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            Terminal.SetSpinBox("KamiOffsetX", -85)
            if Character.GetSkillLevel(4121017) >= 1:
                AttackSI(4121017,on)
            else:
                AttackSI(4111015,on)
        
    elif job == 420: #Bandit
        AttackSI(4201012,on)
        
    elif job in ShadowerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(4001334,on)
    elif job == 421: #Chief Bandit
        AttackSI(4211002,on)
        
    elif job == 422: #Shadower
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(4221007,on)
        
    elif job == 430: #dualblade
        if Character.GetSkillLevel(4001013) == 0:
            LevelSkill(4001013)
        elif Character.GetSkillLevel(4000012) < 10:
            LevelSkill(4000012)
        elif Character.GetSkillLevel(4001011) < 5:
            LevelSkill(4001011)
        elif Character.GetSkillLevel(4001003) < 10:
            LevelSkill(4001003)
        elif Character.GetSkillLevel(4001013) < 10:
            LevelSkill(4001013)
        AttackAuto(4001013,on)
    elif job == 431: #dualblade
        AttackAuto(4001013,on)
    elif job == 432:
        AttackSIND(4321004,on,450)
    elif job == 433:
        #AttackAuto(4321004,on)
        AttackSIND(4321004,on,450)
    elif job == 434: #dual blade 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiND(4341004,4341004,0.74,on)
    elif job == 500: #Pirate
        AttackAuto(5001002,on)
    elif job == 501: #Cannoneer Pirate
        #AttackAuto(5011000,on)
        AttackSIND(5011002,on,200)
    elif job in BuccaneerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5101012,on)
    elif job in CorsairJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5201001,on)
    elif job == 510: #Brawler
        AttackAuto(5101012,on)
    elif job == 511: #Marauder
        AttackAuto(5111002,on)
    elif job == 512: #Buccaneer
        #AttackAuto(5121007,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5121017,5121007,1.25,on)
    elif job == 520: #Gunslinger
        AttackAuto(5201001,on)
    elif job == 521: #Outlaw
        AttackAuto(5211008,on)
    elif job == 522: #Corsair
        #if level < 160:
        #    AttackSIND(5221017,on,350)
        #else:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(5221017,5221017,0.85,on)
    elif job == 530: #Cannoneer
        #AttackAuto(5301001,on)
        #AttackSIND(5011002,on,200)
        #if Character.GetSkillLevel(5301000) >= 1:
        #    AttackAuto(5301001,on)
            #AttackSemiNDMagic(5301000,5301000,0.84,on)
        #else:
        AttackSIND("5301000;5011002",on,300)
    elif job in CannoneerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(5301001,on)
    elif job == 531: #Cannon Trooper
        '''
        if Terminal.GetCheckBox("Mob Falldown"):
            AttackAuto(5311000,on)
        else:
            AttackAuto(5301001,on)
            Terminal.SetCheckBox("Speedy Gonzales",True)
        '''
        #if Character.GetSkillLevel(5311000) >= 1:
        #    AttackSemiNDMagic(5311000,5311000,0.96,on)
        #else:
        AttackSIND("5311000;5011002",on,250)
    elif job == 532: #Cannon Master
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND("5321000;5011002",on,250)
            #AttackSemiNDMagic(5321000,5321000,0.95,on)
    elif job == 508: #Jett 1sts
        AttackAuto(5081020,on)
    elif job in JettJobs and field_id in curbrockhideout:
        AttackAuto(5081020,on)
    elif job == 570: #Jett 2nd
        #AttackAuto(5081020,on)
        if Character.GetSkillLevel(5701011) >= 1:
            AttackSIND(5701011,on,150)
        else:
            AttackAuto(5701010,on)
    elif job == 571: #Jett 3rd
        if Character.GetSkillLevel(5710020) >= 1:
            #AttackSemiNDMagic(5710020,5710020,0.9,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
        else:
            AttackSIND(5701011,on,150)
    elif job == 572: #Jett 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSemiNDMagic(5710020,5710020,0.4,on,attackSpeed=4)
            AttackSIND(5710020,on,150)
    elif job == 1100: #Dawn warrior 1st
        AttackSI(11001020,on)
    elif job in DawnWarriorJobs and field_id in curbrockhideout: #1001005
        AttackAuto(11001020,on)
    elif job == 1110: #Dawn Warrior 2nd
        #AttackAuto(11101120,on)
        AttackSIND(11101120,on,600)
    elif job == 1111: #Dawn Warrior 3rd
        AttackSI(11111120,on)
        #AttackAuto(11111220,on)
    elif job == 1112: #Dawn Warrior 4th
        dummySkill = 11001020
        dummyDelay = 0.81
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.HasBuff(2,11111022):
                AttackSemiNDMagic(11121203,dummySkill,dummyDelay,on)
    elif job == 1200: #BW 1st
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
        ToggleLoot(False)
    elif job in BlazeWizardJobs and field_id in curbrockhideout: #1001005
        AttackAuto(12001021,on)
        Terminal.SetCheckBox("Full Map Attack",False)
    elif job == 1210: #BW 2nd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1211: #BW 3rd
        Terminal.SetCheckBox("Full Map Attack",True)
        AttackAuto(12001020,on)
        
    elif job == 1212: #BW 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:           
            #if level < 140:
            Terminal.SetCheckBox("Full Map Attack",True)
            AttackAuto(12001020,on)
                
            #elif level >= 140:
            #    Terminal.SetCheckBox("Full Map Attack",False)
            #    AttackSIND(12121055,on,31)
            
    elif job == 1300: #Wind Archer 1st
        AttackAuto(13001020,on)
    elif job in WindArcherJobs and field_id in curbrockhideout: #1001005
        AttackAuto(13001020,on)
    elif job == 1310: #Wind Archer 2nd
        if Character.GetSkillLevel(13101020) >= 1:
            AttackSI(13101020,on)
        else:
            AttackAuto(13001020,on)
    elif job == 1311: #Wind Archer 3rd
        #AttackAuto(13111020,on)
        AttackSI(13101020,on)
    elif job == 1312: #Wind Archer 4th
        #AttackAuto(13121002,on)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSI(13121002,on,siOption = "SIRadioShoot")
    elif job == 1400: #Night Walker 1st
        AttackAuto(14001020,on)
    elif job in NightWalkerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(14001020,on)
    elif job == 1410: #Night Walker 2nd
        AttackSI(14101020,on)
    elif job == 1411: #Night Walker 3rd
        AttackAuto(14111022,on)
    elif job == 1412: #Night Walker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(14111022,on)
    elif job == 1500: #Thunder breaker 1st
        #AttackAuto(15001020,on)
        if Character.GetSkillLevel(15001021) >= 1:
            AttackSIND(15001021,on,600)
            #AttackSemiNDMagic(15001021,15001021,0.8,on)
        else:
            AttackAuto(15001020,on)
    elif job in ThunderBreakerJobs and field_id in curbrockhideout: #1001005
        AttackAuto(15001020,on)
    elif job == 1510: #Thunder breaker 2nd
        AttackAuto(15101020,on)
        #AttackSemiNDMagic(15101020,15101020,0.72,on)
    elif job == 1511: #Thunder breaker 3rd
        AttackAuto(15111020,on)
        #AttackSemiNDMagic(15111020,15111020,0.9,on)
    elif job == 1512: #Thunder breaker 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(15121002,15121002,1.08,on)
            #30 * math.ceil(BaseDelay * (14)/480)
            #AttackSIND(15121002,on,500)
        #AttackSIND(15111020,on,300)
        #AttackAuto(15121001,on)
    elif job == 3300: #Wild Hunter 1st
        AttackAuto(33001105,on)
    elif job in WildHunterJobs and field_id in curbrockhideout: #1001005
        AttackAuto(33001105,on)
    elif job == 3310: #Wild Hunter 2nd
        #AttackAuto(33101113,on)
        AttackSI(33101215,on)
    elif job == 3311: #Wild Hunter 3rd
        AttackAuto(33111112,on)
        #AttackSI(33111010,on,100,"SIRadioMagic")
    elif job == 3312: #Wild Hunter 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackAuto(33111112,on)
    elif job == 3200: #Battle Mage 1st
        AttackSI(32001014,on)
    elif job in BattleMageJobs and field_id in curbrockhideout: #1001005
        AttackSI(32001014,on)
    elif job == 3210: #Battle Mage 2nd
        #AttackSI(32100010,on)
        AttackSIND(32101001,on,250)
    elif job == 3211: #Batlle Mage 3rd
        #AttackSI(32110017,on)
        AttackSIND(32101001,on,250)
    elif job == 3212: #Battle Mage 4th
        if level >= 160:
            if level >= 160 and Character.GetSkillLevel(32121052) == 1:
                AttackSemiNDMagic(32120055,32120055,0.45,on)
            elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
                BindSkill(32121052)
        #elif level >= 140:
        #    if level >= 140 and Character.GetSkillLevel(12121054) == 1:
        #        AttackSIND(12121055,16)
        #    elif level >= 140 and Character.GetSkillLevel(12121054) == 0:
        #        BindSkill(12121054)
        else:
            if SCLib.GetVar("DoingZakum"):
                #AttackAuto(32121002,on)
                AttackSIND(32101001,on,250)
            else:
                #AttackSI(32120019,on)
                AttackSIND(32101001,on,250)
    elif job == 3700: #Blaster 1st
        Terminal.SetCheckBox("General FMA",False)
        if Character.GetSkillLevel(37001004) >= 1:
            AttackSIND(37001004,on,80)
        else:
            AttackAuto(37001000,on)
    elif job in BlasterJobs and field_id in curbrockhideout: #1001005
        #Terminal.SetCheckBox("General FMA",on)
        Terminal.SetCheckBox("General FMA",False)
        if Character.GetSkillLevel(37001004) >= 1:
            AttackSIND(37001004,on,80)
        else:
            AttackAuto(37001000,on)
    elif job == 3710: #Blaster 2nd
        #Terminal.SetCheckBox("General FMA",on)
        Terminal.SetCheckBox("General FMA",False)
        if Character.GetSkillLevel(37001004) >= 1:
            AttackSIND(37001004,on,80)
        else:
            AttackAuto(37001000,on)
    elif job == 3711: #Blaster 3rd
        #AttackAuto(37001000,on)
        AttackSI(37110006,on,80)
        Terminal.SetCheckBox("General FMA",on)
        #Terminal.SetCheckBox("General FMA",on)
    elif job == 3712: #Blaster 4th
        #AttackAuto(37001000,on)
        Terminal.SetCheckBox("General FMA",False)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSIND(37121000,on,80)
    elif job == 3500: #Mechanic 1st
        AttackAuto(35001004,on)
    elif job in MechanicJobs and field_id in curbrockhideout: #1001005
        AttackAuto(35001004,on)
    elif job == 3510: #Mechanic 2nd
        AttackAuto(35101001,on)
    elif job == 3511: #Mechanic 3rd
        AttackAuto(35111006,on)
    elif job == 3512: #Mechanic 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(35111015,35111015,0.84,on)
            #AttackSI(35121015,on,250)
        #AttackAuto(35111006,on)
    elif job == 11212: #Beast Tamer
        #if level >= 160 and Character.GetSkillLevel(32121052) == 1:
        #    AttackSemiNDMagic(32120055,32120055,0.45,on)
        #elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
        #    BindSkill(32121052)
        #else:
        if Character.HasBuff(2,110001501):
            if Character.GetSkillLevel(112000003) >= 1:
                #AttackSIND(112000003,on,450)
                AttackSemiNDMagic(112000003,112001008,0.38,on)
            else:
                if level <= 17:
                    AttackAuto(112000000,on)
                    
                elif level >= 17 and (not useExploit or SCLib.GetVar("DoingZakum")):
                    Terminal.SetCheckBox("Auto Attack", False)
                    Terminal.SetCheckBox("Skill Injection", False)
                    Terminal.SetCheckBox("Melee No Delay",False)
                    count = 0
                    if on and not Terminal.IsRushing():
                        while count < 100 and len(Field.GetMobs())>0: #constantly presses control to simulate human actions
                            Key.Down(0x11)
                            time.sleep(0.1)
                            Key.Up(0x11)
                            time.sleep(0.1)
                            count += 1
                            if len(Field.GetMobs())==0:
                                break
    elif job == 2000:#Aran pre
        Terminal.SetCheckBox("Skill Injection", False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Auto Attack", on)
        Terminal.SetComboBox("AttackKey",1)
        Terminal.SetSpinBox("autoattack_spin",100)
        
    elif job == 2100:# or job == 2110: #Aran 1st 21000007
        AttackSI(21000006,on,80)
        #AttackSemiNDMagic(21000006,21000006,0.4,on)

    elif job == 2110:
        SetSIND("21000007;21100018",100,on)   

    elif job == 2111 or job == 2112: #Aran 3rd
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            #AttackSI(21000006,on,80)
            SetSIND("21110028;21100018",100,on)
            #AttackSemiNDMagic(21111021,21111021,0.81,on)
            #if Character.HasBuff(2,21110016):
            #    AttackSIND(21111021,on,450)
            #else:
            #    AttackSIND(21111021,on,400)
            #AttackSemiNDMagic(21111021,21111021,0.65,on)
            #Terminal.SetCheckBox("Speedy Gonzales",True)
            '''
            elif job == 2110 or job == 2111 or job == 2112: #Aran 2nd+3rd+4th 21000007
                Key.Set(pgup_key, 2, 2001582) #Assign an Item, reboot potion, to Page up(0x21)
                Key.Set(attack_key,1,21001010)
                Terminal.SetLineEdit("SISkillID","21100018")
                Terminal.SetCheckBox("Skill Injection", on)
                Terminal.SetSpinBox("SkillInjection",30)
                Terminal.SetCheckBox("Auto SP",True)
                Terminal.SetCheckBox("Melee No Delay",on)
                #Terminal.SetRadioButton("SIRadioMagic",True)
                Terminal.SetCheckBox("Auto Attack", False)
                Terminal.SetComboBox("AttackKey",33)
                Terminal.SetSpinBox("autoattack_spin",100)
            '''
    elif job == 14200:# Kinesis 1st
        AttackAuto(142001001,on)
        #AttackSemiNDMagic(142001001,142001001,0.63,on,attackSpeed = 5)
    elif job in KinesisJobs and field_id in curbrockhideout:
        AttackAuto(142001001,on)
    elif job == 14210: #Kinesis 2nd 142101002
        #AttackSemiNDMagic(142101002,142101002,0.69,on,attackSpeed = 5)
        AttackAuto(142101002,on)
    elif job == 14211 or job == 14212: #Kinesis 3rd + 4th 142111002
        #
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if job == 14211:
                Terminal.SetCheckBox("Instant Final Smash",True)
            else:
                Terminal.SetCheckBox("Instant Final Smash",False)
            AttackAuto(142111002,on)
        
    elif job == 6500: #AB 1st
        AttackSI(60011216,on)
    elif job == 6510: #AB 2nd
        AttackSI(65001100,on)
    elif job == 6511: #AB 3rd
        AttackSI(65111002,on,100,"SIRadioMagic")
        #AttackSemiNDMagic(65111002,65111002,1.2,on)
    elif job == 6512: #AB 4th
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if SCLib.GetVar("DoingZakum"):
                AttackSI(65121008,on)
            else:
                AttackSemiNDMagic(65121100,65111002,1.2,on)
    elif job in KaiserJobs and job != KaiserJobs[3]: #Kaiser 1st 2nd 3rd 4th
        AttackSI(61001005,on)
    elif job == KaiserJobs[3]:
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(61001005,61001005,0.36,on)
    elif job == 2500: #Shade 1st
        AttackAuto(25001000,on)
    elif job == 2510: #Shade 2nd
        AttackSI(25101000,on)
    elif job == 2511: #Shade 3rd
        AttackSIND(25110001,on,300)
        #AttackSemiNDMagic(25110001,2511001,0.99,on)
        #AttackSIND(25111000,on,800)
    elif job == 2512: #Shade 4th
        #AttackSI(25120003,on,100)
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            if Character.GetSkillLevel(25121000) >= 1:
                AttackSemiNDMagic(25121000,25121000,0.63,on)
            else:
                AttackSIND(25110001,on,300)
    elif job == 5100: #Mihile 1st
        AttackAuto(51001004,on)
        #AttackSemiNDMagic(51001004,51001004,0.96,on)
    elif job in MihileJobs and field_id in curbrockhideout:
        AttackAuto(51001004,on)
    elif job == 5110: #Mihile 2nd
        AttackSIND(51101005,on,800)
        #AttackSemiNDMagic(51101005,51001004,0.96,on)
    elif job == 5111: #Mihile 3rd
        #AttackSemiNDMagic(51111006,51111006,0.84,on)
        AttackSIND(51111006,on,600)
    elif job == 5112: #Mihile 4th
        delay = 0.84
        if level >= 160 and Character.GetSkillLevel(32121052) == 1:
            AttackSemiNDMagic(32120055,32120055,0.45,on)
        elif level >= 160 and Character.GetSkillLevel(32121052) == 0 and useHyperExploit:
            BindSkill(32121052)
        else:
            AttackSemiNDMagic(51121009,51111006,0.84,on)
            #AttackSIND(51121009,on,400)
    else:
        Terminal.SetCheckBox("Auto Attack",False)
        Terminal.SetCheckBox("Melee No Delay",False)
        Terminal.SetCheckBox("Skill Injection", False)
        #print("Not any of the listed jobs, not going to attack for safety")
    if job not in KannaJobs:
        Terminal.SetCheckBox("charm_fma",False)
        Terminal.SetCheckBox("Summon Kishin",False)
        Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
    if job not in IlliumJobs:
        Terminal.SetCheckBox("bot/illium/radiant_javelin_delay",False)
        Terminal.SetCheckBox("bot/illium/summon_control",False)

    

def GetEmblem():
    if job == 2311 and Quest.GetQuestState(24105) !=2: #Mercedes
        print("Getting Silver Emblem")
        Quest.StartQuest(24105, 1033210)
    elif job == 2312 and Quest.GetQuestState(24106) !=2:
        print("Getting Gold Emblem")
        Quest.StartQuest(24106, 1033210)
    elif job == 2711 and Quest.GetQuestState(25675) !=2: #Lumi
        print("Getting Silver Emblem")
        Quest.StartQuest(25675, 1032209)
    elif job == 2712 and Quest.GetQuestState(25676) !=2:
        print("Getting Gold Emblem")
        Quest.StartQuest(25676, 1032209)
    elif job == 2214 and Quest.GetQuestState(22617) !=2: #Evan
        print("Getting Silver Emblem")
        Quest.StartQuest(22617, 1013000)
    elif job == 2217 and Quest.GetQuestState(22618) !=2:
        print("Getting Gold Emblem")
        Quest.StartQuest(22618, 1013000)
    elif job == 4111 and Quest.GetQuestState(62387) !=2: #hayato
        print("Getting Silver Emblem")
        Quest.StartQuest(62387, 9130000)
    elif job == 4112 and Quest.GetQuestState(62388) !=2:
        print("Getting Gold Emblem")
        Quest.StartQuest(62388, 9130000)
    elif job == 4212 and  Quest.GetQuestState(62390) !=2:
        print("Getting Gold Emblem")
        Quest.StartQuest(62390, 9130010)
    elif job == ShadeJobs[3] and Quest.GetQuestState(38080) != 2:
        print("Getting Silver Emblem")
        Quest.StartQuest(38080,0)
def StrongholdPrequest():
    # if character is above level 165, rush to future henesys
    # this will automatically accept Exploring the future
    exploringFuture = Quest.GetQuestState(31103)
    chiefAlex = Quest.GetQuestState(31104)
    henesysInRuins = Quest.GetQuestState(31105)
    fallOfCygnus = Quest.GetQuestState(31106)

    scoutingStronghold = Quest.GetQuestState(31124)
    piercingDefenses = Quest.GetQuestState(31125)
    lostEmblem = Quest.GetQuestState(31126)
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingJobAdv",True)
    if field_id == 271010000:
        if pos.x != -596:
            Character.Teleport(-596, 154)
    
    # if this quest is not completed,
    if exploringFuture != 2:
        if field_id != 271010000:
            Terminal.Rush(271010000)
        # if we are in the map, hand in the quest to alex
        Quest.CompleteQuest(31103, 2142001)
        
    elif chiefAlex != 2:
        # if not in map, rush to it
        if field_id != 271010000:
            Terminal.Rush(271010000)
            
        if chiefAlex == 0:
            Quest.StartQuest(31104, 2142001)
        
        elif Quest.CheckCompleteDemand(31104, 2142001) == 0:
            # answer his quiz
            Npc.ClearSelection()
            Npc.RegisterSelection("Kerning City")
            Npc.RegisterSelection("You were a runaway")
            Npc.RegisterSelection("Stan")
            Npc.RegisterSelection("An old golden watch")
            Quest.CompleteQuest(31104, 2142001)
            
    elif henesysInRuins != 2:
        if field_id != 271010000:
            Terminal.Rush(271010000)
            
        if henesysInRuins == 0:
            Quest.StartQuest(31105, 2142001)
    
        elif Quest.CheckCompleteDemand(31105, 2142002) == 0:
            Quest.CompleteQuest(31105, 2142002)
            
    elif fallOfCygnus != 2:
        if field_id != 271010000:
            Terminal.Rush(271010000)
            
        if fallOfCygnus == 0:
            Quest.StartQuest(31106, 2142002)
            
        elif Quest.CheckCompleteDemand(31106, 2142002) == 0:
            Quest.CompleteQuest(31106, 2142002)
        
        
    elif scoutingStronghold != 2:
        if scoutingStronghold == 0:
            Terminal.Rush(271010000)
            time.sleep(1)
            # and then accept from alex
            Quest.StartQuest(31124, 2142001)
        
        elif Quest.CheckCompleteDemand(31124,2142001) == 0:
            Terminal.Rush(271010000)
            time.sleep(1)
            Quest.CompleteQuest(31124, 2142001)
            Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
            
        else:
            print("in progress")
            # quest is in progress, rush to stronghold entrance
            if field_id == 271030010:
                TeleportEnter(867,148)
            else:
                Terminal.SetCheckBox("map/maprusher/hypertelerock",False)
                Terminal.Rush(271030010)
                time.sleep(10)
    elif piercingDefenses != 2:
        if piercingDefenses == 0:
            Terminal.Rush(271010000)
            time.sleep(1)
            # and then accept from alex
            Quest.StartQuest(31125, 2142001)
            
        elif Quest.CheckCompleteDemand(31125, 2142001) == 0:
            Terminal.Rush(271010000)
            time.sleep(1)
            Quest.CompleteQuest(31125, 2142001)
            Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
            ToggleRushByLevel(True)
            print("Resume rush by level; stronghold")
            
        else:
            # not done yet
            if field_id != 271030010 and field_id != 271030000:
                Terminal.SetCheckBox("map/maprusher/hypertelerock",False)
                Terminal.Rush(271030010)
                time.sleep(8)
                
            else:
                # we are in the map to get the item
                # im assuming you have stable kill settings on
                print("Get")
                ToggleKami(True)
                emblem = Field.FindItem(4032922)
                if emblem.valid:
                    ToggleKami(False)
                    Character.Teleport(emblem.x, emblem.y)
                    time.sleep(2)
                    Terminal.SetCheckBox("Auto Loot",True)

ShowStatus()
if GameState.IsInGame():
    SafetySetting()
    time.sleep(1)
    if Character.GetLevel()>=10:
        AssignHyperStats()
    if not (SCLib.GetVar("DoingJobAdv") and (job == ShadeJobs[0] or job == ShadeJobs[1])) and not Terminal.IsRushing():
        if SCLib.GetVar("DoingJobAdv") or SCLib.GetVar("GettingBoogie"):
            ToggleAttackQuest(True)
        else:
            ToggleAttack(True)
        if Character.GetLevel() >= 10 and job not in [CadenaJobs[0],6002]:
            Terminal.SetCheckBox("Auto SP",True)
            print("On auto sp")
        else:
            Terminal.SetCheckBox("Auto SP",False)
    SetPotion()
    if not Terminal.IsRushing():
        ToggleSkill()
    GetEmblem()
    if level == 60:
        pet = Inventory.FindItemByID(2434265)
        if pet.valid:
            Key.Set(0x41, 2, 2001582)
            time.sleep(2)
            Inventory.UseItem(2434265)
            time.sleep(2)
    if level > 140 and accountData['phase_one'] and not Terminal.IsRushing():
        if Inventory.GetItemCount(5040004) == 0 and Inventory.GetEmptySlotCount(5) > 0 and Character.GetMeso() >= 5200000:
            print("Need to buy hyper teleport rock")
            #ToggleRushByLevel(False)
            Terminal.SetCheckBox("Auto Attack",False)
            Terminal.SetCheckBox("Skill Injection",False)
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
    if level >= 180 and level < 185 and Quest.GetQuestState(31125) != 2 and not HasHtr() and not SCLib.GetVar("DoingZakum"):
        StrongholdPrequest()
        print("Doing stronghold")
    elif (Quest.GetQuestState(31125) == 2 or HasHtr()) and SCLib.GetVar("DoingJobAdv") and level < 200 and level >= 180:
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleRushByLevel(True)
        print("Resume rush by level; stronghold")
    
    if Terminal.GetCheckBox("Skill Injection"):
        if not Terminal.GetCheckBox("Auto Loot"):
            Terminal.SetCheckBox("Auto Loot",True)
    #print("Toggling attack")
############################Job Advancements###############################
    if job == 4200 and level < 13 and field_id != 100020400:
        print("Completing Kanna First job")
        KannaFirstJobAdv()
        
    elif job == 4200 and level < 13 and field_id == 100020400:
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleRushByLevel(True)
        ToggleKami(True)

    elif job == 4200 and level >= 30:
        print("Completing Kanna Second job")
        second_job_quest = Quest.GetQuestState(57458)
        if second_job_quest == 0:
            Quest.StartQuest(57458, 000000)
        ToggleRushByLevel(True)
        ToggleKami(True)

    elif job == 2700 and level == 10:
        print("Completing Lumi first job")
        ToggleRushByLevel(False)
        LumiFirstJobAdv()
        
    elif job == 2700 and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Lumi second job")
        LumiSecondJobAdv()
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif job ==2710 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Lumi third job")
        LumiThirdJobAdv()
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif job == 2711 and level >=100 and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingZakum"):
        print("Completing Lumi fourth job")
        LumiFourthJobAdv()
        ToggleRushByLevel(True)
        ToggleKami(True)
        time.sleep(2)
    elif job == 3001:
        print("Choosing")
        DemonFirstJobAdv()
    elif (job == 3101 or job == 3100) and level == 10:
        ToggleRushByLevel(True)
        ToggleKami(True)
        ToggleLoot(False)
        time.sleep(2)
        print("Resume rush by level; da/ds start")
    elif (job == 3101 or job ==3100) and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Demon Avenger Second job")
        ToggleRushByLevel(False)
        DASecondJobAdv()
    elif (job == 3120 or job == 3110) and level == 30 and field_id == 310010000 and not SCLib.GetVar("DoingCurbrock"):
        TeleportEnter(111,-14)
        ToggleRushByLevel(True)
        ToggleKami(True)
        print("Resume rush by level; da/ds second start training")
    elif (job == 3120 or job == 3110) and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Demon Avenger Third job")
        ToggleRushByLevel(False)
        DAThirdJobAdv()
    elif (job == 3121 or job == 3111) and level < 100 and SCLib.GetVar("DoingJobAdv"):
        print("Done third job and now resetting vars")
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif (job == 3121 or job == 3111) and field_id == 931050110 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        TeleportEnter(111,-14)
        ToggleRushByLevel(True)
        ToggleKami(True)
        print("Resume rush by level; da/ds third start training")
    elif job == 3121 and level >= 100 and not SCLib.GetVar("DoingCurbrock"):
        ToggleRushByLevel(False)
        print("DA fourth job")
        DAFourthJobAdv()
    elif job == 3111 and level >= 100 and not SCLib.GetVar("DoingCurbrock"):
        ToggleRushByLevel(False)
        print("DS fourth job")
        DSFourthJobAdv()
    elif job == 2300 and level <= 13:
        quest = Quest.GetQuestState(29952)
        if quest == 0:
            MercedesFirstJobAdv()
        ToggleRushByLevel(True)
        ToggleKami(True)
        print("Resume rush by level; mercedes start")
    elif job == 2300 and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        ToggleKami(False)
        MercedesSecondJobAdv()
    elif job == 2310 and field_id == 910150100:
        TeleportEnter(9,-250)
        ToggleRushByLevel(True)
        ToggleKami(True)
        print("Resume rush by level; mercedes second start training")
    elif job == 4100 and level <13:
        HayatoFirstJobAdv()
    elif job == 4100 and level >=30 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Hayato Second job")
        second_job_quest = Quest.GetQuestState(57162)
        if second_job_quest == 0:
            Quest.StartQuest(57162, 000000)
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif job == 15000:
        print("Completing Illium Pre-First job")
        IlliumZero()
    elif job == 15200:
        print("Completing Illium First Job")
        IlliumFirstJobAdv()
    elif job == 15210 and Quest.GetQuestState(34820) != 2:
        print("Completing Illium Second Job")
        IlliumSecondJobAdv()
    elif job == 15210 and level < 40 and field_id == 400000001:
        Quest.StartQuest(5500, 1061005)
        SCLib.UpdateVar("DoingCurbrock",True)
    elif job == 15210 and level < 60 and SCLib.GetVar("DoingJobAdv"):
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 15210 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Illium Third Job")
        IlliumThirdJobAdv()
    elif job == 15211 and level < 100:
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleRushByLevel(True)
    elif job == 15211 and level >= 100 and not SCLib.GetVar("DoingZakum"):
        print("Completing Illium Fourth job")
        IlliumFourthJobAdv()
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif job == 15212 and field_id == 940202000:
        TeleportEnter(-2,-20)
        ToggleKami(True)
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; illium fourth start training")
    elif field_id == 102040200 and job == 15211: #Still in relicExcavation Camp
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; relic Excavation camp")
    elif (job == 6400 or job == 6002 or job == 6410) and Quest.GetQuestState(34625) != 2:
        print("Completing Cadena First Job and Second Job")
        SCLib.UpdateVar("DoingJobAdv",True)
        CadenaFirstJobAdv()
    elif job == 6410 and Quest.GetQuestState(34625) == 2 and level <50 and SCLib.GetVar("DoinJobAdv"):
        print("Cadena Job Pre done")
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 6410 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Cadena Third job")
        CadenaThirdJobAdv()
    elif job == 6411 and level >= 100 and not SCLib.GetVar("DoingZakum"):
        print("Completing Cadena Fourth job")
        CadenaFourthJobAdv()
    elif job == 15001:
        if field_id == 402000615:
            Quest.StartQuest(34901, 0)
        print("Starting Ark job")
    elif job in ArkJobs[0:2] and (Quest.GetQuestState(34902) != 2 or Quest.GetQuestState(34938) != 2):
        print("Completing Ark First Job")
        ArkFirstJobAdv()
    elif job == 15510 and Quest.GetQuestState(34940) != 2 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Ark Second Job")
        ArkSecondJobAdv()
    elif job == 15510 and level < 50 and Quest.GetQuestState(34940) == 2 and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("GettingBoogie"):
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; ark second start training")
    elif job == 15510 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Ark Third Job")
        ArkSecondJobAdv()
    elif job == 15511 and level >= 100 and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingZakum"):
        print("Completing Ark Fourth Job")
        ArkFourthJobAdv()
    elif (job == 2001 or job == 2200) and Quest.GetQuestState(22510) != 2:
        print("Completing Evan prequests")
        EvanFirstJobAdv()
    elif job == 2200 and field_id == 100000000:
        print("Enabling rush by level to leave Henesys")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        Terminal.SetCheckBox("settings/loginwait",True)
    elif job == 3600 and level < 30 and field_id == 310010000:
        print("Xenon leave home")
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif job == 3600 and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Xenon Second Job")
        XenonSecondJobAdv()
    elif job == 3610 and level < 60 and field_id == 230050000:
        print("Accepting quest to leave Veritas")
        Quest.StartQuest(32155, 2300001)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif job == 3610 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Completing Xenon Third Job")
        XenonThirdJobAdv()
    elif job == 3611 and level < 100 and field_id == 230050000:
        print("Enabling rush by level to leave Veritas")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 3611 and level >= 100 and not SCLib.GetVar("DoingZakum"):
        print("Completing Xenon Fourth Job")
        XenonFourthJobAdv()
    elif job == 3612 and field_id == 230050000:
        print("Enabling rush by level to leave Veritas")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 2003:
        print("Doing Phantom First job")
        PhantomFirstJobAdv()
    elif job == 2400 and field_id == 150000000:
        print("Finishing Phantom first job, leaving aircraft")
        if Quest.GetQuestState(25000) != 2:
            Quest.CompleteQuest(25000, 1402000)
        SCLib.UpdateVar("DoingJobAdv",False)
        TeleportEnter(-600,-672)
        ToggleRushByLevel(True)
        ToggleKami(True)
    elif job == 2400 and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        print("Doing Phantom Second Job")
        PhantomSecondJobAdv()
    elif job == 2410 and level <= 40:
        smallpark = 200020001
        TreasureVaultEntrance = 915010000
        TreasureVault = 915010001
        cloudpark2 = 200020000
        if Quest.CheckCompleteDemand(25101,0) == 0:
            Quest.CompleteQuest(25101,0)
        if field_id == TreasureVault:
            DungeonTeleport()
        elif field_id == TreasureVaultEntrance:
            DungeonTeleport()
        elif field_id == smallpark:
            DungeonTeleport()
        elif field_id == cloudpark2:
            ToggleRushByLevel(True)
            ToggleKami(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            print("Resume rush by level; cloud park 2")
    elif job == 2410 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Doing Phantom Third Job")
        PhantomThirdJobAdv()
    elif job == 2411 and level < 100:
        if Quest.CheckCompleteDemand(25111,0) == 0:
            Quest.CompleteQuest(25111,0)
        overlookedarea=260010601
        arianttreasure = 915010100
        arianttreasurevault = 915010101
        if field_id == overlookedarea:
            DungeonTeleport()
            ToggleRushByLevel(True)
            ToggleKami(True)
            print("Resume rush by level; over looked area")
        elif field_id == arianttreasure:
            DungeonTeleport()
        elif field_id == arianttreasurevault:
            DungeonTeleport()
            SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 2411 and level >= 100 and not SCLib.GetVar("DoingZakum"):
        print("Doing Phantom Fourth Job")
        PhantomFourthJobAdv()
    elif job == 2412:
        lushforest = 240010102
        leafretreasurevaultentrance = 915010200
        leafretreasurevault = 915010201
        if Quest.CheckCompleteDemand(25122,0) == 0:
            Quest.CompleteQuest(25122,0)
        if field_id == lushforest:
            DungeonTeleport()
            ToggleRushByLevel(True)
            ToggleKami(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            print("Resume rush by level; lush forest")
        elif field_id == leafretreasurevaultentrance:
            DungeonTeleport()
        elif field_id == leafretreasurevault:
            DungeonTeleport()
    elif job == 11212 and Quest.GetQuestState(55234) != 2 and level < 35:
        print("Doing Beast Tamer Prequests")
        BeastTamerFirstJobAdv()
    elif (job == 2000 or job == 2100) and Quest.GetQuestState(21700) != 2 and level < 13:
        print("Doing Aran First Job")
        AranFirstJobAdv()
    elif job == 2100 and field_id == 140000000 and level < 29:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; aran first start training")
    elif job == 2100 and level == 10 and field_id == 140020300 and Character.GetMeso() < 800:
        while True:
            if Character.GetMeso() < 800:
                ToggleRushByLevel(False)
                RushTo(140020200)
                ToggleKami(True)
            else:
                ToggleRushByLevel(True)
                SCLib.UpdateVar("DoingJobAdv",False)
                print("rushing out aran")
                break
    elif job == 2100 and level < 30:
        polearm = Inventory.FindItemByID(1442077)
        if polearm.valid:
            Inventory.SendChangeSlotPositionRequest(1,polearm.pos,weapon_slot,-1)
    elif job == 2100 and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        print("Doing Aran Second Job")
        AranSecondJobAdv()
    elif job == 2110 and field_id == 140000000 and level < 60:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; aran second start training")
    elif job == 2110 and level >=60 and not SCLib.GetVar("DoingCurbrock"):
        print("Doing Aran Third Job")
        AranThirdJobAdv()
    elif job == 2111 and field_id == 140000000 and level < 100:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; aran third start training")
    elif job == 2111 and level >= 100 and not SCLib.GetVar("DoingZakum"):
        print("Doing Aran Fourth Job")
        AranFourthJobAdv()
    elif job == 2112 and field_id == 140000000:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; aran fourth start training")
    elif job == 0 and GameState.IsInGame():
        ExplorerFirstJobAdv()
    elif job == 400 and level < 11:
        ToggleRushByLevel(True)
        ToggleKami(True)
        print("Resume rush by level; db first start training")
        SCLib.UpdateVar("DoingJobAdv",False)
        knife = Inventory.FindItemByID(1332063)
        stars = Inventory.FindItemByID(2070015)
        if knife.valid:
            Inventory.SendChangeSlotPositionRequest(1,knife.pos,weapon_slot,-1)
        if not Terminal.GetProperty("checked", -1):
            if stars.valid:
                SCLib.UpdateVar("DualBlade",False)
            else:
                SCLib.UpdateVar("DualBlade",True)
            if SCLib.GetVar("DualBlade"):
                Terminal.LoadProfile("C:/Users/Jacopo/Desktop/TerminalManager/terminalProfiles/AIOLinksDB.xml")
            else:
                Terminal.LoadProfile("C:/Users/Jacopo/Desktop/TerminalManager/terminalProfiles/AIOLinks.xml")
            Terminal.SetProperty("checked", 1)
        if SCLib.GetVar("DualBlade"):
            Terminal.LoadProfile("C:/Users/Jacopo/Desktop/TerminalManager/terminalProfiles/AIOLinksDB.xml")
        else:
            Terminal.LoadProfile("C:/Users/Jacopo/Desktop/TerminalManager/terminalProfiles/AIOLinks.xml")
    elif (job == 410 or job == 1400) and level < 31 and not Inventory.GetItem(1,weapon_slot).id == 1472061:
        claw = Inventory.FindItemByID(1472061)
        if claw.valid:
            Inventory.SendChangeSlotPositionRequest(1,claw.pos,weapon_slot,-1)
    elif (job in NightlordJobs or job in NightWalkerJobs) and Inventory.FindItemByID(2070000).valid == 0 and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingJobAdv") and Inventory.GetItem(1,weapon_slot).id == 1472061:
        print("Need stars")
        BuyStars()
        Terminal.SetPushButton("Leave shop",True)
        time.sleep(1)
        Terminal.SetPushButton("Leave shop",False)
    elif (job in NightlordJobs or job in NightWalkerJobs) and Inventory.GetItemCount(2070000) < 100  and Inventory.FindItemByID(2070000).valid == 1 and not SCLib.GetVar("DoingJobAdv"):
        print("Recharge stars")
        ToggleRushByLevel(False)
        if field_id != 100000102:
            Terminal.Rush(100000102) # rush to store (Henessys gral store)
            time.sleep(1)
        elif field_id == 100000102:
            time.sleep(0.5)
            Character.TalkToNpc(1011100) #open the store
            time.sleep(10) #Recharge time
            if Inventory.GetItemCount(2070000) >= 100:
                Terminal.SetPushButton("Leave shop",True)
                time.sleep(1)
                Terminal.SetPushButton("Leave shop",False)
                ToggleRushByLevel(True)
    elif (job == 200 or job == BlazeWizardJobs[0]) and level < 11:
        wand = Inventory.FindItemByID(1372043)
        if wand.valid:
            Inventory.SendChangeSlotPositionRequest(1,wand.pos,weapon_slot,-1)
        Terminal.SetCheckBox("Kami Loot",False)
    elif (job == 300 or job == 1300)and level < 11:
        bow = Inventory.FindItemByID(1452051)
        if bow.valid:
            Inventory.SendChangeSlotPositionRequest(1,bow.pos,weapon_slot,-1)
    elif (job == 500 or job in ThunderBreakerJobs) and level < 11:
        knuckle = Inventory.FindItemByID(1482014)
        if knuckle.valid:
            Inventory.SendChangeSlotPositionRequest(1,knuckle.pos,weapon_slot,-1)
    elif job == 501 and level < 15:
        cannon = Inventory.FindItemByID(1532000)
        if cannon.valid:
            Inventory.SendChangeSlotPositionRequest(1,cannon.pos,weapon_slot,-1)
    elif job == 530 and level < 59 and field_id == 120000101:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; cannoneer second start training")
    elif job == CorsairJobs[1] and level < 31:
        pistol = Inventory.FindItemByID(1492014)
        if pistol.valid:
            Inventory.SendChangeSlotPositionRequest(1,pistol.pos,weapon_slot,-1)
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; corsair buy pistol")
    elif job in CorsairJobs and Inventory.FindItemByID(2330000).valid == 0 and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingJobAdv") and not SCLib.GetVar("DoingZakum"):
        print("Need bullets")
        BuyBullets()
        Terminal.SetPushButton("Leave shop",True)
        time.sleep(1)
        Terminal.SetPushButton("Leave shop",False)
    elif job in explorerFirstJobs and level >= 30 and not SCLib.GetVar("DualBlade"):
        print("Doing Explorer Second Job")
        ExplorerSecondJobAdv()
    elif job == 400 and level>=20 and SCLib.GetVar("DualBlade") and not SCLib.GetVar("DoingCurbrock"):
        DualbladeSecondJobAdv()
    elif job == 430 and level>=30 and not SCLib.GetVar("DoingCurbrock"):
        DualBladeThirdJobAdv()
    elif job == 431 and level>=45 and not SCLib.GetVar("DoingCurbrock"):
        DualBladeFourthJobAdv()
    elif job == 432 and level>=60 and not SCLib.GetVar("DoingCurbrock"):
        ExplorerThirdJobAdv()
    elif job == 433 and level >= 100 and not SCLib.GetVar("DoingCurbrock"):
        ExplorerFourthJobAdv()
    elif job == DarkknightJobs[1] and level <32 and Inventory.GetItem(1,weapon_slot).id != 1432002:
        print("Check spear")
        forkspearid = 1432002
        if Inventory.GetItem(1,weapon_slot).id != forkspearid:
            print("Need to buy spear")
            forkspear = Inventory.FindItemByID(forkspearid)
            if forkspear.valid:
                Inventory.SendChangeSlotPositionRequest(1,forkspear.pos,weapon_slot,-1)
            else:
                BuySpear()
                Terminal.SetPushButton("Leave shop",True)
                time.sleep(1)
                Terminal.SetPushButton("Leave shop",False)
    elif job == MarksmanJobs[1] and level <32 and (Inventory.GetItem(1,weapon_slot).id != 1432002 or Inventory.FindItemByID(2061000).count < 1):
        print("Check Crossbow")
        mountainCrossbowid = 1462000
        if Inventory.GetItem(1,weapon_slot).id != mountainCrossbowid:
            print("Need to buy crossbow")
            mountainCrossbow = Inventory.FindItemByID(mountainCrossbowid)
            if mountainCrossbow.valid:
                Inventory.SendChangeSlotPositionRequest(1,mountainCrossbow.pos,weapon_slot,-1)
            else:
                BuyCrossbow()
                Terminal.SetPushButton("Leave shop",True)
                time.sleep(1)
                Terminal.SetPushButton("Leave shop",False)
        elif Inventory.FindItemByID(2061000).count < 1:
            print("Need to buy crossbow arrow")
            BuyArrow()
            Terminal.SetPushButton("Leave shop",True)
            time.sleep(1)
            Terminal.SetPushButton("Leave shop",False)
    elif job in explorerSecondJobs and level == 30 and SCLib.GetVar("DoingJobAdv"):
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; explorer second start training")
    elif job in explorerSecondJobs and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Doing Explorer Third Job")
        ExplorerThirdJobAdv()
    elif job in explorerThirdJobs and level >= 100 and not SCLib.GetVar("DoingCurbrock"):
        print("Doing Explorer Fourth Job")
        ExplorerFourthJobAdv()
    elif job in explorerFourthJobs and field_id == 240010501:
        print("Returning to farming settings")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 508 and level == 10 and field_id == 120000100:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; jett first start training")
    elif job == 508 and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        JettSecondJobAdv()
    elif job == 570 and level < 40 and field_id == 552000071:
        TeleportEnter(53,214)
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; jett second start training")
    elif job == 570 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        JettThirdJobAdv()
    elif job == 571 and level < 70 and field_id == 552000071:
        TeleportEnter(53,214)
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resume rush by level; jett third start training")
    elif job == 571 and level >= 100 and not SCLib.GetVar("DoingCurbrock"):
        JettFourthJobAdv()
    elif job == 572 and level <= 104 and SCLib.GetVar("DoingJobAdv"):
        if field_id == 240010300:
            ToggleRushByLevel(True)
            ToggleKami(True)
            SCLib.UpdateVar("DoingJobAdv",False)
            print("Resume rush by level; jett fourth start training")
    elif job == 1000:
        CygnusFirstJobAdv()
    elif job in cygnusFirstJobs and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        CygnusSecondJobAdv()
    elif job in cygnusSecondJobs and level <60 and field_id == 130000000:
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleKami(True)
        print("Resume rush by level; cygnus second start training")
    elif job in cygnusSecondJobs and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Doing Cygnus Knights Third job")
        CygnusThirdJobAdv()
    elif job in cygnusThirdJobs and level < 100 and field_id == 130000000:
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleKami(True)
        print("Resume rush by level; cygnus third start training")
    elif job in cygnusThirdJobs and level >= 100 and not SCLib.GetVar("DoingCurbrock"):
        CygnusFourthJobAdv()
    elif job in cygnusFourthJobs and field_id == 130000000 and level < 120:
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleKami(True)
        print("Resume rush by level; cygnus fourth start training")
    elif job == 3000:
        print("Resistance first")
        ResistanceFirstJobAdv()
    elif job == WildHunterJobs[0] and level == 10 and field_id == 931000500 and Terminal.GetCheckBox("Rush By Level"):
        print("Leave this jaguar place")
        ToggleKami(False)
        ToggleRushByLevel(False)
        time.sleep(2)
        TeleportEnter(328,25)
        ToggleRushByLevel(True)
        time.sleep(10)
    elif job == WildHunterJobs[0] and level == 10 and Character.GetEquippedItemIDBySlot(weapon_slot) != 1462092:
        crossbow = Inventory.FindItemByID(1462092)
        if crossbow.valid:
            Inventory.SendChangeSlotPositionRequest(1,crossbow.pos,weapon_slot,-1)
    elif job in resistanceFirstJobs and level >= 30:
        ResistanceSecondJobAdv()
    elif job in resistanceSecondJobs and level >= 60:
        ResistanceThirdJobAdv()
    elif job in resistanceThirdJobs and level >= 100:
        ResistanceFourthJobAdv()
    elif job == 3300 and level == 10 and field_id == 310010000:
        CatchJaguar()
    elif job in resistanceFirstJobs and level <= 15 and field_id == 310010000:
        print("Leaving, done job adv")
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleKami(True)
    elif job in MechanicJobs and level < 11:
        pistol = Inventory.FindItemByID(1492014)
        if pistol.valid:
            Inventory.SendChangeSlotPositionRequest(1,pistol.pos,weapon_slot,-1)
    elif job == BlasterJobs[0] and level < 11:
        cannon = Inventory.FindItemByID(1582000)
        if cannon.valid:
            Inventory.SendChangeSlotPositionRequest(1,cannon.pos,weapon_slot,-1)
    elif job == BattleMageJobs[0] and level == 10:
        staff = Inventory.FindItemByID(1382100)
        if staff.valid:
            Inventory.SendChangeSlotPositionRequest(1,staff.pos,weapon_slot,-1)
    elif (job == 14000 or job == 14200) and field_id != 101020400 and Quest.GetQuestState(22733) != 2:
        print("Doing Kinesis First Job")
        KinesisFirstJobAdv()
    elif job == 14200 and field_id == 101020400:
        print("Kinesis prequests done")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 14200 and level >= 30 and not SCLib.GetVar("DoingCurbrock"):
        print("Kinesis Second Job")
        KinesisSecondJobAdv()
    elif job == 14210 and level < 45 and SCLib.GetVar("DoingJobAdv"):
        print("Kinesis Second job adv done")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 14210 and level >= 60 and not SCLib.GetVar("DoingCurbrock"):
        print("Kinesis Third Job")
        KinesisThirdJobAdv()
    elif job == 14211 and level < 80 and SCLib.GetVar("DoingJobAdv"):
        print("Kinesis Third job adv done")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == 14211 and level >= 100 and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock"):
        print("Kinesis Fourth Job")
        KinesisFourthJobAdv()
    elif job == 14212 and level < 110 and SCLib.GetVar("DoingJobAdv"):
        print("Kinesis Fourth job adv done")
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
    elif job == AngelicBusterJobs[0] and level == 10 and field_id == 400000000:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Starting AB training")
    elif job == AngelicBusterJobs[0] and level >= 30:
        ABSecondJobAdv()
    elif job == AngelicBusterJobs[1] and level >= 60:
        ABThirdJobAdv()
    elif job == AngelicBusterJobs[2] and level >= 100:
        ABFourthJobAdv()
    elif job == KaiserJobs[0] and level == 10 and field_id == 400000000:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Starting Kaiser Training")
    elif job == KaiserJobs[0] and level >= 30:
        KaiserSecondJobAdv()
    elif job == KaiserJobs[1] and level >= 60:
        KaiserThirdJobAdv()
    elif job == KaiserJobs[2] and level >= 100:
        KaiserFourthJobAdv()
    elif job == ShadeJobs[0] or job == ShadeJobs[1]:
        print("Doing Shade First job")
        ShadeFirstJobAdv()
    elif job == ShadeJobs[2] and level >= 60:
        print("Doing Shade Third job")
        ShadeThirdJobAdv()
    elif job == ShadeJobs[3] and field_id in [921110301,921110300]:
        DungeonTeleport()
    elif job == ShadeJobs[3] and field_id == 211060000:
        Terminal.StopRush()
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        ToggleKami(True)
        print("Resuming Shade Third Job training")
    elif job == ShadeJobs[3] and level >= 100:
        print("Doing Shade Fourth job")
        ShadeFourthJobAdv()
    elif job == ShadeJobs[4] and field_id == 302000000:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resuming Shade Fourth job training")
    elif job == MihileJobs[0] and field_id == 130000000 and level == 10:
        ToggleRushByLevel(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Starting Mihile training")
    elif job == MihileJobs[0] and level >= 30:
        print("Doing Mihile Second Job")
        MihileSecondJobAdv()
    elif job == MihileJobs[1] and level >= 60:
        print("Doing Mihile Third Job")
        MihileThirdJobAdv()
    elif job == MihileJobs[2] and level < 100 and field_id == 130000000:
        ToggleRushByLevel(True)
        ToggleKami(True)
        SCLib.UpdateVar("DoingJobAdv",False)
        print("Resuming Mihile third job training")
    elif job == MihileJobs[2] and level >= 100:
        print("Doing Mihile Fourth Job")
        MihileFourthJobAdv()
    #buy potion
    #print( SCLib.GetVar("DoingJobAdv"))
    if not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingJobAdv") and Character.GetMeso() >= 48000 and level > 50 and Inventory.FindItemByID(2002023).count == 0 and not Inventory.FindItemByID(2001582).valid:
        Terminal.SetPushButton("Sell Item",False)
        BuyPotion()
        Terminal.SetPushButton("Leave shop",True)
        time.sleep(1)
        Terminal.SetPushButton("Leave shop",False)
        Terminal.SetPushButton("Sell Item",True)
    ###### lvl 50 hyper rock #######
    if Quest.GetQuestState(61589) !=2 and Character.GetLevel() >= 50 and Inventory.GetEmptySlotCount(2)>=4:
        print("Getting hyper rock")
        Npc.ClearSelection()
        Npc.RegisterSelection("Familiar")
        Npc.RegisterSelection("Teleport Rock")
        Npc.RegisterSelection("You get")
        Quest.StartQuest(61589, 9201253)
        time.sleep(3)
        #Terminal.SetCheckBox("bot/htr",True)
        #time.sleep(5)
        #Terminal.SetCheckBox("bot/htr",False)
    elif Quest.GetQuestState(61589) ==2:
        if Inventory.FindItemByID(2430450).valid:
            print("Using equip box lvl50")
            Inventory.UseItem(2430450)

    ###### lvl 60 tot ########
    if Quest.GetQuestState(61590) !=2 and Character.GetLevel() >= 60:
        print("Getting tot badge")
        Npc.ClearSelection()
        Npc.RegisterSelection("Potential")
        Npc.RegisterSelection("Bonus Potential")
        Npc.RegisterSelection("Cube")
        Npc.RegisterSelection("Soul Weapon")
        Npc.RegisterSelection("gift")
        Quest.StartQuest(61590, 9201253)
        time.sleep(3)
    elif Quest.GetQuestState(61590) ==2 and level < 70:
        if Inventory.FindItemByID(2430451).valid:
            print("Using equip box lvl60")
            Inventory.UseItem(2430451)

def GetBoogie():
    if Character.IsOwnFamiliar(9960098) == False:
        # sleep 1 second every loop
        print("Getting Boogie")
        SCLib.UpdateVar("GettingBoogie",True)
        time.sleep(1)
        ToggleRushByLevel(False)
        item = Inventory.FindItemByID(2870098)
        drop = Field.FindItem(2870098)
        pos = Character.GetPos()
        if drop.valid:
            Terminal.SetCheckBox("Kami Vac",False)
            ToggleAttackQuest(False)
            Terminal.SetCheckBox("Auto Loot",True)
            if pos.x == drop.x and pos.y == drop.y:
                print("Teleported to item location, waiting item to be picked up")
                time.sleep(3)
            else:
                Character.Teleport(drop.x,drop.y)
                print("Teleporting to item location, waiting item to be picked up")
                time.sleep(3)
        if item.valid:
            # use familiar
            Inventory.UseFamiliarCard(2870098)
            Inventory.UseFamiliarCard(2870098)
            Inventory.UseFamiliarCard(2870098)
            ToggleRushByLevel(True)
            print("Restoring rush by level; Boogie")
            time.sleep(1)
            Terminal.SetCheckBox("Kami Vac",True)
            ToggleAttackQuest(True)
            SCLib.UpdateVar("GettingBoogie",False)
            Terminal.SetCheckBox("Kami Loot",False)
            ToggleLoot(False)
            if not Terminal.GetCheckBox("Familiar 0"):
                Terminal.SetComboBox("Familiar0",1)
                Terminal.SetCheckBox("Familiar 0",True)
                ToggleLoot(False)
        else:
            if Field.GetID() == 102010000:
                # Perion Southern Ridge
                # let bot kill mobs and pickup?
                ToggleAttackQuest(True)
                ToggleKami(True)
                time.sleep(2)
            elif Terminal.IsRushing():
                time.sleep(2)
            else:
                # rush to the map
                if field_id == 800000100:
                    Terminal.StopRush()
                Terminal.Rush(102010000)
if Character.GetLevel() >= 13 and GameState.IsInGame() and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingJobAdv"):
    # Jr. Boogie
    if job in IlliumJobs:
        lookback = Quest.GetQuestState(34820)
        if lookback == 2 or level >= 33:
            if field_id == 800000100:
                Terminal.StopRush()
            GetBoogie()
        else:
            print("Illium not done")
    elif job in CadenaJobs:
        if Quest.GetQuestState(34625) == 2:
            GetBoogie()
    elif job in ArkJobs:
        if (job != 15500 and Quest.GetQuestState(34940) == 2 or level >= 36) and Quest.GetQuestState(34902) == 2 and Quest.GetQuestState(34938) == 2:
            GetBoogie()
    elif job in EvanJobs:
        if Quest.GetQuestState(22510) == 2:
            GetBoogie()
    elif job in AranJobs:
        if Quest.GetQuestState(21700) == 2:
            GetBoogie()
    elif job == 11212:
        if level >= 35:
            GetBoogie()
    elif job == 14200:
        if Quest.GetQuestState(22733) == 2:
            GetBoogie()
    elif job != -1 and job != 0 and job not in DemonAvengerJobs and job not in DemonSlayerJobs and job not in KannaJobs and job not in KinesisJobs:
        GetBoogie()
    

if Character.GetLevel() >= 83 and GameState.IsInGame() and getSpider:
    # Big Spider
    if Character.IsOwnFamiliar(9960295) == False:
        print("Getting Big Spider")
        ToggleRushByLevel(False)
        # sleep 1 second every loop
        time.sleep(1)
        item = Inventory.FindItemByID(2870295)
        drop = Field.FindItem(2870295)
        pos = Character.GetPos()
        if drop.valid:
            Terminal.SetCheckBox("Kami Vac",False)
            ToggleAttackQuest(False)
            Terminal.SetCheckBox("Auto Loot",True)
            if pos.x == drop.x and pos.y == drop.y:
                print("Teleported to item location, waiting item to be picked up")
                time.sleep(3)
            else:
                Character.Teleport(drop.x,drop.y)
                print("Teleporting to item location, waiting item to be picked up")
                time.sleep(3)
        if item.valid:
            # use familiar
            print("Found big spider familiar")
            Inventory.UseFamiliarCard(2870295)
            ToggleRushByLevel(True)
            time.sleep(1)
            ToggleKami(True)
            ToggleAttackQuest(True)
            if not Terminal.GetCheckBox("Familiar 0"):
                Terminal.SetComboBox("Familiar0",2)
                Terminal.SetCheckBox("Familiar 0",True)
                #Terminal.SetCheckBox("Auto Loot",False)
        else:
            if Field.GetID() == 310050600:
                # let bot kill mobs and pickup?
                print("Farming for big spider")
                time.sleep(5)
            else:
                # rush to the map
                print("Rushing to Big Spider map")
                if not Terminal.GetCheckBox("map/maprusher/hypertelerock"):
                    Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
                Terminal.Rush(310050600)



if level >= 150 and job not in ThunderBreakerJobs and not accountData['phase_one'] and not SCLib.GetVar("DoingZakum"):
    if field_id != 240000000:
        RushTo(240000000)
    else:
        if len(accountData['done_links']) == 21: #finished training all link to level 140
            print("Phase one end")
            accountData['phase_one'] = True
            accountData['cur_link_pos'] = str(accountData['storage_number']+1)
            accountData['changing_mule'] = True
            WriteJson(accountData,accountId)
            ToggleRushByLevel(True)
            if GameState.IsInGame():
                Terminal.Logout()
                time.sleep(2)
        else:
            print("Current character done, moving to next one")
            accountData['changing_mule'] = True
            WriteJson(accountData,accountId)
            ToggleRushByLevel(True)
            if GameState.IsInGame():
                Terminal.Logout()
                time.sleep(2)
if ((level >= 140 and job not in ThunderBreakerJobs) or (level >= 150 and job in ThunderBreakerJobs)) and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingJobAdv") and not accountData['phase_one'] and level < 160:
    if HasPensalir():
        if job not in ThunderBreakerJobs:
            if field_id != 240000000:
                RushTo(240000000)
                ToggleRushByLevel(False)
            else:
                print("Current character done, moving to next one")
                accountData['changing_mule'] = True
                WriteJson(accountData,accountId)
                if GameState.IsInGame():
                    Terminal.Logout()
                    time.sleep(2)
                    ToggleRushByLevel(True)
        elif job in ThunderBreakerJobs:
            if Quest.GetQuestState(20766) != 2 or Character.GetSkillLevel(10000202) < 6:
                print("Completing Cygnus quests")
                q1 = Quest.GetQuestState(20761)
                q2 = Quest.GetQuestState(20762)
                q3 = Quest.GetQuestState(20763)
                q4 = Quest.GetQuestState(20764)
                q5 = Quest.GetQuestState(20765)
                q6 = Quest.GetQuestState(20766)
                ToggleRushByLevel(False)
                if field_id != 130000000:
                    RushTo(130000000)
                elif q1 != 2:
                    Quest.StartQuest(20761,1101002)
                elif q2 != 2:
                    Quest.StartQuest(20762,1101002)
                elif q3 != 2:
                    Quest.StartQuest(20763,1101002)
                elif q4 != 2:
                    Quest.StartQuest(20764,1101002)
                elif q5 != 2:
                    Quest.StartQuest(20765,1101002)
                elif q6 != 2:
                    Quest.StartQuest(20766,1101002)
            else:
                print("Current character done, moving to next one")
                accountData['changing_mule'] = True
                WriteJson(accountData,accountId)
                if GameState.IsInGame():
                    Terminal.Logout()
                    time.sleep(2)
    else:
        if job in IlliumJobs or level >= 150:
            if field_id != 240000000:
                RushTo(240000000)
                ToggleRushByLevel(False)
            else:
                print("Current character done, moving to next one")
                accountData['changing_mule'] = True
                WriteJson(accountData,accountId)
                if GameState.IsInGame():
                    Terminal.Logout()
                    time.sleep(2)
                    ToggleRushByLevel(True)
        else:
            if field_id != 251010500 and not SCLib.GetVar("BuyExpansion"):
                RushTo(251010500)
            ToggleRushByLevel(False)
            ToggleLoot(True)
            pet = Inventory.FindItemByID(2434265)
            if pet.valid:
                Key.Set(0x41, 2, 2001582)
                time.sleep(2)
                Inventory.UseItem(2434265)
                time.sleep(2)
            Terminal.SetSpinBox("FilterMeso",50000)
            #Terminal.SetCheckBox("settings/expcrash",False)
            Terminal.SetCheckBox("Instant Final Smash",False)
            EquipPensalir()
elif level >= 140 and not HasPensalir(False) and GameState.IsInGame() and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingJobAdv") and accountData['phase_one'] and level < 160:
    if field_id != 251010500 and not SCLib.GetVar("BuyExpansion"):
        RushTo(251010500)
    ToggleRushByLevel(False)
    ToggleLoot(True)
    EquipPensalir()
    Terminal.SetProperty("CheckEquip",True)
elif level >= 140 and accountData['phase_one'] and (HasPensalir(False) and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingJobAdv") and Terminal.GetProperty("CheckEquip",True) or Terminal.GetCheckBox("Kami Loot")):
    ToggleRushByLevel(True)
    Terminal.SetCheckBox("Kami Loot",False)
    Terminal.SetProperty("CheckEquip",False)
    print("Resume rush by level; training to 200")
if level >= 200 and accountData['phase_one'] and not SCLib.GetVar("DoingZakum"):
    if field_id != 240000000:
        RushTo(240000000)
        ToggleRushByLevel(False)
    else:
        print("Current character done, moving to next one")
        accountData['changing_mule'] = True
        WriteJson(accountData,accountId)
        if GameState.IsInGame():
            Terminal.Logout()
            time.sleep(2)
            ToggleRushByLevel(True)
#####Black gate    

#print(SCLib.GetVar("cube_lock"))
if DoBlackGate and Character.GetHP() > 0 and level >= 145 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    ToggleRushByLevel(False)
    map = Field.GetID()
    channel = GameState.GetChannel()
    print("Blackgate farming")
    SCLib.UpdateVar("DoingBG",True)
    if Terminal.GetCheckBox('filter_equip'):
        Terminal.SetCheckBox('filter_equip',False)
    if not Terminal.GetCheckBox('Kami Loot'):
        Terminal.SetCheckBox('Kami Loot',True)
    if not Terminal.GetCheckBox('Auto Loot'):
        Terminal.SetCheckBox('Auto Loot',True)
    Terminal.SetCheckBox("Kami Vac",True)
    ToggleAttackQuest(True)
    Terminal.SetSpinBox("FilterMeso",0)
    if Inventory.GetEmptySlotCount(1) == 0:
        if not Terminal.IsRushing():
            Terminal.Rush(henesys)
    #for item in winter_coupons:
    #    if Character.HasBuff(1, item) == False:
    #        Inventory.UseItem(item)
    #        time.sleep(1)
    if farmed_enough_accessories():
        print("farmed enough accessories")
        SCLib.UpdateVar("DoingBG",False)
    if Terminal.IsRushing():
        print("Rushing... Please wait...")
        #if map == 610050000:
        #    Terminal.StopRush()
        time.sleep(2)
    # IF FOR SOME REASON U END UP IN HENE
    elif map not in blackgate_maps:
        print("Rushing to blackgate")
        Terminal.Rush(610050000)
    # IF AT BDF MAIN MAP
    elif map == 610050000:
        time.sleep(5)
        if channel == 30:
            channel = 1
        else:
            channel += 1
        Terminal.ChangeChannel(channel)
        while Terminal.IsRushing():
            time.sleep(3)
        print("Current channel" + str(GameState.GetChannel()))
        print("Rushing to starting map")
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610050100)
        else:
            print("Still has ring")

    elif map == 610050100:
        print("Arrived in " + str(map) + "...")
        BossCheck()
        # EnterPortal("south00")
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610051500)
        else:
            print("Still has ring")

    elif map == 610051500:
        print("Arrived in " + str(map) + "...")
        BossCheck()
        if not Field.FindItem(1113185).valid:
            Terminal.Rush(610050000)
        else:
            print("Still has ring")
        # BACK TO STARTING POINT
curbrock1 = Quest.GetQuestState(5499)
curbrock2 = Quest.GetQuestState(5500)
curbrock3 = Quest.GetQuestState(5501)
sabitrama = 1061005

curbrockescaperoute1 = 600050030
curbrockescaperoute2 = 600050040
curbrockescaperoute3 = 600050050
escaperoutes = [curbrockescaperoute1,curbrockescaperoute2,curbrockescaperoute3]
'''
if GameState.IsInGame() and not Terminal.IsRushing() and level >= 27 and level <= 29 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingJobAdv"):
    pos = Character.GetPos()
    if job in IlliumJobs and Quest.GetQuestState(34820) !=2:
        print("Illium undone quest")
    elif curbrock1 !=2:
        print("Doing first Curbrock")
        SCLib.UpdateVar("DoingCurbrock",True)
        ToggleRushByLevel(False)
        if curbrock1 ==0:
            Quest.StartQuest(5499, sabitrama)
            #time.sleep(1)
        elif curbrock1 ==1:
            ToggleAttack(False)
            if Quest.CheckCompleteDemand(5499, sabitrama) ==0:
                if field_id in curbrockhideout:
                    DungeonTeleport()
                    time.sleep(8)
                    print("Resume Kami")
                elif field_id == curbrockescaperoute1:
                    DungeonTeleport()
                    time.sleep(8)
                    ToggleRushByLevel(True)
                else:
                    Quest.CompleteQuest(5499,sabitrama)
                    SCLib.UpdateVar("DoingCurbrock",False)
                    ToggleRushByLevel(True)
            else:
                if field_id in curbrockhideout:
                    ToggleKami(False)
                    time.sleep(2)
                    ToggleAttack(False)
                    DungeonTeleport()
                    time.sleep(8)
                    #TeleportEnter(-425,-195)
'''
if GameState.IsInGame() and not Terminal.IsRushing() and level >= 34 and level < 60 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    pos = Character.GetPos()
    if job in IlliumJobs and Quest.GetQuestState(34820) !=2:
        print("Illium undone quest")
    elif job in ArkJobs and (Quest.GetQuestState(34902) !=2 or Quest.GetQuestState(34940) != 2 or Quest.GetQuestState(34938) != 2):
        print("Ark undone quest")
    elif job in CadenaJobs:
        if Quest.GetQuestState(34625) != 2:
            print("Cadena undone quest")
    elif curbrock2 ==0:
        print("Doing second curbrock")
        ToggleRushByLevel(False)
        SCLib.UpdateVar("DoingCurbrock",True)
        Quest.StartQuest(5500, sabitrama)
        time.sleep(3)
    elif SCLib.GetVar("DoingCurbrock"):
        ToggleRushByLevel(False)
        if curbrock2 == 1:
            if field_id not in curbrockhideout and field_id not in escaperoutes:
                SCLib.UpdateVar("DoingCurbrock",False)
        if Quest.CheckCompleteDemand(5500, sabitrama) ==0:
            print("Quest completed")
            if pos.x != -425 and field_id in curbrockhideout and len(Field.GetMobs()) == 0:
                time.sleep(8)
                DungeonTeleport()
                print("Resume Kami")
            elif pos.x != -549 and field_id == curbrockescaperoute2 and len(Field.GetMobs()) == 0:
                time.sleep(8)
                DungeonTeleport()
                ToggleRushByLevel(True)
                print("Resume rush by level; curbrock")
            else:
                Quest.CompleteQuest(5500,sabitrama)
                SCLib.UpdateVar("DoingCurbrock",False)
                time.sleep(4)
                ToggleRushByLevel(True)
                print("Resume rush by level; curbrock")
        else:
            print("Enable kami to kill curbrock")
            SCLib.UpdateVar("DoingCurbrock",True)
            Terminal.StopRush()
            ToggleKami(True)
            ToggleAttackQuest(True)
if GameState.IsInGame() and not Terminal.IsRushing() and curbrock2 == 2 and level >= 61 and level < 100 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum"):
    pos = Character.GetPos()
    if curbrock3 ==0:
        print("Doing Third Curbrock")
        ToggleRushByLevel(False)
        Quest.StartQuest(5501, sabitrama)
        SCLib.UpdateVar("DoingCurbrock",True)
        time.sleep(3)
    elif SCLib.GetVar("DoingCurbrock"):
        if curbrock3 == 1:
            if field_id not in curbrockhideout and field_id not in escaperoutes:
                SCLib.UpdateVar("DoingCurbrock",False)
        if Quest.CheckCompleteDemand(5501, sabitrama) ==0:
            if pos.x != -425 and field_id in curbrockhideout and len(Field.GetMobs()) == 0:
                time.sleep(8)
                DungeonTeleport()
            elif pos.x != -549 and field_id == curbrockescaperoute3 and len(Field.GetMobs()) == 0:
                time.sleep(8)
                DungeonTeleport()
                ToggleRushByLevel(True)
                print("Resume rush by level; curbrock")
            else:
                Quest.CompleteQuest(5501,sabitrama)
                SCLib.UpdateVar("DoingCurbrock",False)
                ToggleRushByLevel(True)
                print("Resume rush by level; curbrock")
        else:
            print("Enable kami to kill curbrock")
            SCLib.UpdateVar("DoingCurbrock",True)
            ToggleKami(True)
            ToggleAttackQuest(True)
            Terminal.StopRush()
if GameState.IsInGame() and field_id in curbrockhideout:
    time.sleep(2)
    if len(Field.GetMobs()) == 0:
        if Quest.CheckCompleteDemand(5500, sabitrama) ==0:
            Quest.CompleteQuest(5500,sabitrama)
        elif Quest.CheckCompleteDemand(5501, sabitrama) ==0:
            Quest.CompleteQuest(5501,sabitrama)
        time.sleep(8)
        DungeonTeleport()
    else:
        print("Mob not dead")
        SCLib.UpdateVar("DoingCurbrock",True)
        ToggleAttackQuest(True)
        ToggleKami(True)
        Terminal.StopRush()
elif GameState.IsInGame() and field_id in escaperoutes:
    if Quest.CheckCompleteDemand(5500, sabitrama) ==0:
        Quest.CompleteQuest(5500,sabitrama)
    elif Quest.CheckCompleteDemand(5501, sabitrama) ==0:
        Quest.CompleteQuest(5501,sabitrama)
    time.sleep(8)
    DungeonTeleport()
    ToggleAttackQuest(True)
    ToggleRushByLevel(True)
    print("Resume rush by level; curbrock")
    SCLib.UpdateVar("DoingCurbrock",False)
elif GameState.IsInGame() and field_id not in curbrockhideout and field_id not in escaperoutes and SCLib.GetVar("DoingCurbrock") and len(Field.GetMobs()) == 0:
    print("Ended up somewhere weird")
    SCLib.UpdateVar("DoingCurbrock",False)
    ToggleAttackQuest(True)
    ToggleKami(True)
    time.sleep(4)
    ToggleRushByLevel(True)
    print("Resume rush by level; curbrock")
    Terminal.StopRush()


quest26 = Quest.GetQuestState(2976)
if GameState.IsInGame() and doBeach and not Terminal.IsRushing() and level >= 36 and level < 55 and quest26 !=2 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock") and job not in XenonJobs:
    time.sleep(1)
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingBeach",True)
    #field_id to Field Name
    BeachGrassDunes1 = (120040100)
    BeachGrassDunes2 = (120040200)
    BeachGrassDunes3 = (120040300)
    GoldBeachResort = (120040000)
    GoldBeachSeaSide1 = (120041000)
    GoldBeachSeaSide2 = (120041100)
    GoldBeachSeaSide3 = (120041200)
    ShallowSea1 = (120041300)
    ShallowSea2 = (120041400)
    ShallowSea3 = (120041500)
    SoftWaveBeach1 = (120041600)
    GentleWaves2 = (120041700)
    HardWaveBeach = (120041800)
    ShadyBeach = (120041900)

    #NPCID to Npc Name
    PilotIrvin = (1082101)
    SwansonBGD2 = (1082201)
    LittleRichieResort = (1082002)
    SwansonResort = (1082000)
    RalphioGBSS2 = (1082202)
    TofuBGSS2 = (1082203)
    SwansonGBSS2 = (1082204)
    RalphioGBSS3 = (1082205)
    SwansonSS1 = (1082206)
    InnerTubeCaddy = (1082005)
    LittleRichieSS2 = (1082207)
    LittleRichieSS3 = (1082208)
    SwansonSS3 = (1082209)
    TofuHWB = (1082210)
    
    #QuestID to Quest Name
    FlyingBlind = (2951)
    AMissionOfGratImportance = (2952)
    FunWithTheSon = (2953)
    GoldenFruit = (2954)
    HouseKeeping = (2955)
    DangerOnTheCoast = (2956)
    LittleTroubleMaker = (2957)
    StatusReport = (2958)
    TheDayTheLightsWentOut = (2959)
    ShineALight = (2960)
    LocalsAndYokels = (2961)
    SubMarineDreams = (2962) 
    PrivateBeach = (2963)
    PutARingOnIt = (2964)
    TheHuntForBlackNovemner = (2965)
    BlackWave = (2966)
    FloatingAway = (2967)
    FreshFlavours = (2968)
    ShrimpySitiuation = (2969)
    TheSadTaleOfLilWilly = (2970)
    FerryFrustrations = (2971)
    TheOriginalSlimeStar = (2972)
    GoingTribal = (2973)
    ChefsSpecial = (2974)
    TerrorFromTheDeep = (2975)
    GoldBeachGoldenOppertunity = (2950)
    
    
    
    #Gets Queststate on Quests
    quest1 = Quest.GetQuestState(FlyingBlind)
    quest2 = Quest.GetQuestState(AMissionOfGratImportance)
    quest3 = Quest.GetQuestState(FunWithTheSon)
    quest4 = Quest.GetQuestState(GoldenFruit)
    quest5 = Quest.GetQuestState(HouseKeeping)
    quest6 = Quest.GetQuestState(DangerOnTheCoast)
    quest7 = Quest.GetQuestState(LittleTroubleMaker)
    quest8 = Quest.GetQuestState(StatusReport)
    quest9 = Quest.GetQuestState(TheDayTheLightsWentOut)
    quest10 = Quest.GetQuestState(ShineALight)
    quest11 = Quest.GetQuestState(LocalsAndYokels)
    quest12 = Quest.GetQuestState(SubMarineDreams)
    quest13 = Quest.GetQuestState(PrivateBeach)
    quest14 = Quest.GetQuestState(PutARingOnIt)
    quest15 = Quest.GetQuestState(TheHuntForBlackNovemner)
    quest16 = Quest.GetQuestState(BlackWave)
    quest17 = Quest.GetQuestState(FloatingAway)
    quest18 = Quest.GetQuestState(FreshFlavours)
    quest19 = Quest.GetQuestState(ShrimpySitiuation)
    quest20 = Quest.GetQuestState(TheSadTaleOfLilWilly)
    quest21 = Quest.GetQuestState(FerryFrustrations)
    quest22 = Quest.GetQuestState(TheOriginalSlimeStar)
    quest23 = Quest.GetQuestState(GoingTribal)
    quest24 = Quest.GetQuestState(ChefsSpecial)
    quest25 = Quest.GetQuestState(TerrorFromTheDeep)
    quest26 = Quest.GetQuestState(2976)
    quest27 = Quest.GetQuestState (GoldBeachGoldenOppertunity)
    
    #Complete quest27 (GoldBeachGoldenOppertunity)
    if quest27 !=2:
        ToggleRushByLevel(False)
        if quest27 ==0:
            ToggleKami(False)
            Quest.StartQuest(GoldBeachGoldenOppertunity, 1082100)
            ToggleKami(True)
    #Complete quest1 (Flying blind)
    elif quest1 !=2:
        if quest1 ==0:
            ToggleKami(False)
            if field_id != BeachGrassDunes3:
                Terminal.Rush(BeachGrassDunes3)
            if pos.x != -822:
                Character.Teleport(-822, -85)
            else:
                Quest.StartQuest(FlyingBlind, PilotIrvin)
        elif quest1 ==1:
            if Quest.CheckCompleteDemand(FlyingBlind, PilotIrvin) ==0:
                ToggleKami(False)
                if field_id != BeachGrassDunes3:
                    Terminal.Rush(BeachGrassDunes3)
                if pos.x != -822:
                    Character.Teleport(-822, -85)
                else:
                    Quest.CompleteQuest(FlyingBlind, PilotIrvin)
            else:
                ToggleKami(True)
                if field_id != BeachGrassDunes3:
                    Terminal.Rush(BeachGrassDunes3)
    #Complete quest2 (A Mission of great importance)
    elif quest2 !=2:
        if quest2 ==0:
            ToggleKami(False)
            if field_id != BeachGrassDunes2:
                Terminal.Rush(BeachGrassDunes2)
            if pos.x != -769:
                Character.Teleport(-769, -85)
            else:
                Quest.StartQuest(AMissionOfGratImportance, SwansonBGD2)
        elif quest2 ==1:
            if Quest.CheckCompleteDemand(AMissionOfGratImportance, LittleRichieResort)==0:
                ToggleKami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -331:
                    Character.Teleport(-331, 116)
                else:
                    Quest.CompleteQuest(AMissionOfGratImportance, LittleRichieResort)
            else:
                ToggleKami(True)
                if field_id != BeachGrassDunes2:
                    Terminal.Rush(BeachGrassDunes2)
    #Complete quest3 (Fun With the son)
    elif quest3 !=2:
        if quest3 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(FunWithTheSon, LittleRichieResort)
        elif quest3 ==1:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(FunWithTheSon, SwansonResort)
    #Complete quest4 (GoldenFruit)
    elif quest4 !=2:
        if quest4 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(GoldenFruit, SwansonResort)
        elif quest4 ==1:
            if Quest.CheckCompleteDemand(GoldenFruit, SwansonResort)==0:
                ToggleKami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -7:
                    Character.Teleport(-7, 116)
                else:
                    Quest.CompleteQuest(GoldenFruit, SwansonResort)
            else:
                ToggleKami(True)
                if field_id != BeachGrassDunes1:
                    Terminal.Rush(BeachGrassDunes1)
    #Complete quest5 (HouseKeeping)
    elif quest5 !=2:
        if quest5 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(HouseKeeping, SwansonResort)
        elif quest5 ==1:
            if Quest.CheckCompleteDemand(HouseKeeping, SwansonResort)==0:
                ToggleKami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -7:
                    Character.Teleport(-7, 116)
                else:
                    Quest.CompleteQuest(HouseKeeping, SwansonResort)
            else:
                ToggleKami(True)
                if field_id != GoldBeachSeaSide1:
                    Terminal.Rush(GoldBeachSeaSide1)
    #Complete quest6 (danger on the coast)
    elif quest6 !=2:
        if quest6 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(DangerOnTheCoast, SwansonResort)
        elif quest6 ==1:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(DangerOnTheCoast, SwansonResort)
    #Complete quest7 (LittleTroubleMaker)
    elif quest7 !=2:
        if quest7 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(LittleTroubleMaker, LittleRichieResort)
        elif quest7 ==1:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(LittleTroubleMaker, SwansonResort)
    #Complete quest8 (StatusReport)
    elif quest8 !=2:
        if quest8 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(StatusReport, SwansonResort)
        elif quest8 ==1:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.CompleteQuest(StatusReport, LittleRichieResort)
    #complete quest9 (TheDayTheLightsWentOut)
    elif quest9 !=2:
        if quest9 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(TheDayTheLightsWentOut, SwansonResort)
        elif quest9 ==1:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -727:
                Character.Teleport(-727, -85)
            else:
                Quest.CompleteQuest(TheDayTheLightsWentOut, RalphioGBSS2)
    #Complete quest10 (ShineALight)
    elif quest10 !=2:
        if quest10 ==0:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -727:
                Character.Teleport(-727, -85)
            else:
                Quest.StartQuest(ShineALight, RalphioGBSS2)
        elif quest10 ==1:
            if Quest.CheckCompleteDemand(ShineALight, RalphioGBSS2)==0:
                ToggleKami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != -727:
                    Character.Teleport(-727, -85)
                else:
                    Quest.CompleteQuest(ShineALight, RalphioGBSS2)
            else:
                ToggleKami(True)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
    #Complete quest11 (LocalsAndYokels)
    elif quest11 !=2:
        if quest11 ==0:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -549:
                Character.Teleport(-549, -85)
            else:
                Quest.StartQuest(LocalsAndYokels, TofuBGSS2)
        elif quest11 ==1:
            if Quest.CheckCompleteDemand(LocalsAndYokels, TofuBGSS2)==0:
                ToggleKami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != -549:
                    Character.Teleport(-549, -85)
                else:
                    Quest.CompleteQuest(LocalsAndYokels, TofuBGSS2)
            else:
                ToggleKami(True)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
    #Complete quest12 (SubMarineDreams)
    elif quest12 !=2:
        if quest12 ==0:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -549:
                Character.Teleport(-549, -85)
            else:
                Quest.StartQuest(SubMarineDreams, TofuBGSS2)
                time.sleep(5)
        elif quest12 ==1:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -549:
                Character.Teleport(-549, -85)
            else:
                Quest.CompleteQuest(SubMarineDreams, TofuBGSS2)
    #Complete quest13 (PrivateBeach)
    elif quest13 !=2:
        if quest13 ==0:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide2:
                Terminal.Rush(GoldBeachSeaSide2)
            if pos.x != -408:
                Character.Teleport(-408, -25)
            else:
                Quest.StartQuest(PrivateBeach, SwansonGBSS2)
        elif quest13 ==1:
            if Quest.CheckCompleteDemand(PrivateBeach, SwansonGBSS2)==0:
                ToggleKami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != -408:
                    Character.Teleport(-408, -25)
                else:
                    Quest.CompleteQuest(PrivateBeach, SwansonGBSS2)
            else:
                ToggleKami(True)
                if field_id != GoldBeachSeaSide3:
                    Terminal.Rush(GoldBeachSeaSide3)
    #Complete quest14 (PutARingOnIt)
    elif quest14 !=2:
        if quest14 ==0:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide3:
                Terminal.Rush(GoldBeachSeaSide3)
            if pos.x != 825:
                Character.Teleport(825, -205)
            else:
                Quest.StartQuest(PutARingOnIt, RalphioGBSS3)
        elif quest14 ==1:
            if Quest.CheckCompleteDemand(PutARingOnIt, RalphioGBSS3)==0:
                ToggleKami(False)
                if field_id != GoldBeachSeaSide2:
                    Terminal.Rush(GoldBeachSeaSide2)
                if pos.x != 825:
                    Character.Teleport(825, -205)
                else:
                    Quest.CompleteQuest(PutARingOnIt, RalphioGBSS3)
            else:
                ToggleKami(True)
                if field_id != GoldBeachSeaSide3:
                    Terminal.Rush(GoldBeachSeaSide3)
    #Complete quest15 (TheHuntForBlackNovemner)
    elif quest15 !=2:
        if quest15 ==0:
            ToggleKami(False)
            if field_id != GoldBeachSeaSide3:
                Terminal.Rush(GoldBeachSeaSide3)
            if pos.x != 825:
                Character.Teleport(825, -205)
            else:
                Quest.StartQuest(TheHuntForBlackNovemner, RalphioGBSS3)
        elif quest15 ==1:
            ToggleKami(False)
            if field_id != ShallowSea1:
                Terminal.Rush(ShallowSea1)
            if pos.x != -168:
                Character.Teleport(-168, -325)
            else:
                Quest.CompleteQuest(TheHuntForBlackNovemner, SwansonSS1)
    #Complete quest16 (BlackWave)
    elif quest16 !=2:
        if quest16 ==0:
            ToggleKami(False)
            if field_id != ShallowSea1:
                Terminal.Rush(ShallowSea1)
            if pos.x != -168:
                Character.Teleport(-168, -325)
            else:
                Quest.StartQuest(BlackWave, SwansonSS1)
        elif quest16 ==1:
            if Quest.CheckCompleteDemand(BlackWave, SwansonResort)==0:
                ToggleKami(False)
                if field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                if pos.x != -7:
                    Character.Teleport(-7, 116)
                else:
                    Quest.CompleteQuest(BlackWave, SwansonResort)
            else:
                ToggleKami(True)
                if field_id != ShallowSea1:
                    Terminal.Rush(ShallowSea1)
    #Complete quest17 (FloatingAway)
    elif quest17 !=2:
        if quest17 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(FloatingAway, SwansonResort)
        elif quest17 ==1:
            if Quest.CheckCompleteDemand(FloatingAway, InnerTubeCaddy)==0:
                ToggleKami(False)
                if field_id != ShallowSea2:
                    Terminal.Rush(ShallowSea2)
                elif pos.x != -627:
                    Character.Teleport(-627, 116)
                else:
                    Quest.CompleteQuest(FloatingAway, InnerTubeCaddy)
            else:
                ToggleKami(True)
                if field_id != ShallowSea2 and Inventory.FindItemByID(4000759).count < 30:
                    Terminal.Rush(ShallowSea2)
                elif Inventory.FindItemByID(4000759).count >= 30:
                    Terminal.Rush(ShallowSea1)
    #Complete quest18 (FreshFlavours)
    elif quest18 !=2:
        if quest18 ==0:
            ToggleKami(False)
            if field_id != ShallowSea2:
                Terminal.Rush(ShallowSea2)
            if pos.x != -352:
                Character.Teleport(-352, -145)
            else:
                Quest.StartQuest(FreshFlavours, LittleRichieSS2)
        elif quest18 ==1:
            if Quest.CheckCompleteDemand(FreshFlavours, LittleRichieSS3)==0:
                ToggleKami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -1131:
                    Character.Teleport(-1131, -325)
                else:
                    Quest.CompleteQuest(FreshFlavours, LittleRichieSS3)
            else:
                ToggleKami(True)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
    #COmplete quest 19 (ShrimpySitiuation)
    elif quest19 !=2:
        if quest19 ==0:
            ToggleKami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -1131:
                Character.Teleport(-1131, -325)
            else:
                Quest.StartQuest(ShrimpySitiuation, LittleRichieSS3)
        elif quest19 ==1:
            if Quest.CheckCompleteDemand(ShrimpySitiuation, LittleRichieSS3)==0:
                ToggleKami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -1131:
                    Character.Teleport(-1131, -325)
                else:
                    Quest.CompleteQuest(ShrimpySitiuation, LittleRichieSS3)
            else:
                ToggleKami(True)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
    #COmplete quest20 (TheSadTaleOfLilWilly)
    elif quest20 !=2:
        if quest20 ==0:
            ToggleKami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -637:
                Character.Teleport(-637, 116)
            else:
                Quest.StartQuest(TheSadTaleOfLilWilly, SwansonSS3)
        elif quest20 ==1:
            if Quest.CheckCompleteDemand(TheSadTaleOfLilWilly, SwansonSS3)==0:
                ToggleKami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -637:
                    Character.Teleport(-637, 116)
                else:
                    Quest.CompleteQuest(TheSadTaleOfLilWilly, SwansonSS3)
            else:
                ToggleKami(True)
                if field_id != SoftWaveBeach1:
                    Terminal.Rush(SoftWaveBeach1)
    #Complete quest21 (FerryFrustrations)
    elif quest21 !=2:
        if quest21 ==0:
            ToggleKami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -637:
                Character.Teleport(-637, 116)
            else:
                Quest.StartQuest(FerryFrustrations, SwansonSS3)
        elif quest21 ==1:
            if Quest.CheckCompleteDemand(FerryFrustrations, SwansonSS3)==0:
                ToggleKami(False)
                if field_id != ShallowSea3:
                    Terminal.Rush(ShallowSea3)
                if pos.x != -637:
                    Character.Teleport(-637, 116)
                else:
                    Quest.CompleteQuest(FerryFrustrations, SwansonSS3)
            else:
                ToggleKami(True)
                Terminal.Rush(GentleWaves2)
                time.sleep(30)
                Terminal.Rush(HardWaveBeach)
                time.sleep(30)
    #Complete quest22 (TheOriginalSlimeStar)
    elif quest22 !=2:
        if quest22 ==0:
            ToggleKami(False)
            if field_id != ShallowSea3:
                Terminal.Rush(ShallowSea3)
            if pos.x != -637:
                Character.Teleport(-637, 116)
            else:
                Quest.StartQuest(TheOriginalSlimeStar, SwansonSS3)
        elif quest22 ==1:
            ToggleKami(False)
            if field_id != HardWaveBeach:
                Terminal.Rush(HardWaveBeach)
            if pos.x != -211:
                Character.Teleport(-211, -145)
            else:
                Quest.CompleteQuest(TheOriginalSlimeStar, TofuHWB)
    #Complete quest23 (GoingTribal)
    elif quest23 !=2:
        if quest23 ==0:
            ToggleKami(False)
            if field_id != HardWaveBeach:
                Terminal.Rush(HardWaveBeach)
            if pos.x != -211:
                Character.Teleport(-211, -145)
            else:
                Quest.StartQuest(GoingTribal, TofuHWB)
        elif quest23 ==1:
            if Quest.CheckCompleteDemand(GoingTribal, TofuHWB)==0:
                ToggleKami(False)
                if field_id != HardWaveBeach:
                    Terminal.Rush(HardWaveBeach)
                if pos.x != -211:
                    Character.Teleport(-211, -145)
                else:
                    Quest.CompleteQuest(GoingTribal, TofuHWB)
            else:
                ToggleKami(True)
                if field_id != HardWaveBeach:
                    Terminal.Rush(HardWaveBeach)
    #Complete quest24 (ChefsSpecial)
    elif quest24 !=2:
        if quest24 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.StartQuest(ChefsSpecial, SwansonResort)
        elif quest24 ==1:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -7:
                Character.Teleport(-7, 116)
            else:
                Quest.CompleteQuest(ChefsSpecial, SwansonResort)
    #Complete quest 25 (TerrorFromTheDeep)
    elif quest25 !=2:
        print("quest 25")
        if Party.IsInParty():
            Party.LeaveParty()
        if quest25 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(TerrorFromTheDeep, LittleRichieResort)
        elif quest25 ==1:
            if Quest.CheckCompleteDemand(TerrorFromTheDeep, LittleRichieResort)==0:
                time.sleep(2)
                ToggleKami(False)
                if field_id in range(ShadyBeach,ShadyBeach+20):
                    TeleportEnter(381,125)
                elif field_id != GoldBeachResort:
                    Terminal.Rush(GoldBeachResort)
                elif pos.x != -331:
                    Character.Teleport(-331, 116)
                else:
                    Quest.CompleteQuest(TerrorFromTheDeep, LittleRichieResort)
            else:
                if field_id not in range(ShadyBeach-1,ShadyBeach+20):
                    Terminal.Rush(HardWaveBeach)
                    print("Not in range")
                    if field_id == HardWaveBeach:
                        TeleportEnter(797,-385)
                else:
                    ToggleKami(True)
                    Terminal.StopRush()
    #Complete quest 26 for beachbum medal
    elif quest26 !=2:
        print("quest 26")
        if quest26 ==0:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.StartQuest(2976, LittleRichieResort)
        elif quest25 ==1:
            ToggleKami(False)
            if field_id != GoldBeachResort:
                Terminal.Rush(GoldBeachResort)
            if pos.x != -331:
                Character.Teleport(-331, 116)
            else:
                Quest.CompleteQuest(2976, LittleRichieResort)
                time.sleep(2)
                Inventory.SendChangeSlotPositionRequest(1,Inventory.FindItemByID(1032254).pos,earring_slot,-1)
                time.sleep(2)
                ToggleRushByLevel(True)
                ToggleKami(True)
                print("Resume rush by level; beach")
    #All quest for Gold Beach Complete!
elif GameState.IsInGame() and quest26 == 2 and Inventory.FindItemByID(1032254).valid and level < 100:
    print("Equiping earring and enabling rush by level")
    time.sleep(2)
    Inventory.SendChangeSlotPositionRequest(1,Inventory.FindItemByID(1032254).pos,earring_slot,-1)
    time.sleep(2)
    ToggleRushByLevel(True)
    ToggleKami(True)
    SCLib.UpdateVar("DoingBeach",False)
elif GameState.IsInGame() and quest26 == 2 and field_id == 120040000:
    ToggleRushByLevel(True)
    ToggleKami(True)
    SCLib.UpdateVar("DoingBeach",False)
    print("Just in case stuck in gold beach, return control to rush by level")
quest17 = Quest.GetQuestState(2054)
if GameState.IsInGame() and doSleepyWood and not Terminal.IsRushing() and level >= 65 and level < 80 and quest17!=2 and not SCLib.GetVar("DoingCurbrock"):
    #print("Doing")
    ToggleRushByLevel(False)
    SCLib.UpdateVar("DoingSleepy",True)
    time.sleep(1)
    pos = Character.GetPos()
    #NPC ID TO NPC NAME

    Ilji = (1061019)
    Gwin = (1061013)
    Ronnie = (1061004)
    TheNote = (1063014)
    MuYoung = (1061014)
    TristansSpirit = (1061015)
    InsignificantBeing = (1061012)
    John = (20000)
    ChunJi = (1061020)
    Chrisharama =(1061000)
    #MAPID TO MAPNAME

    SleepyWood = (105000000)
    SilentSwamp = (105010000)
    HumidSwamp = (105010100)
    SunlessArea = (105020000)
    CaveCliff = (105020100)
    ColdWind = (105020200)
    ChillyCave = (105020300)
    CaveExit = (105020400)
    AnotherDoor = (105030000)
    TempleEntrance = (105030100)
    CollapsedTemple = (105030200)
    EndlessHallway = (105030300)
    GloomyTemple = (105030400)
    ForbiddenAltar = (105030500)
    BottomoftheTemple = (105100100)
    HerosMemory = (910520000)

    #QUESTID TO QUEST NAME
    DrakeAttack1 = (2581)
    DrakeAttack2 = (2582)
    DrakeAttack3 = (2583)
    DrakeAttack4 = (2584)
    DrakeAttack5 = (2585)
    InjuredAdventurer = (2265)
    InjuredAdventurer2 = (2266)
    InjuredAdventurer3 = (2267)
    InjuredAdventurer4 = (2268)
    RonniesMarble = (2586)
    MysteriousNote = (2237)
    MysteriousNote2 = (2238)
    ASpellThatSealsUpACriticalDanger = (2096)
    ASpellThatSealsUpACriticalDanger2 = (2097)
    ForestOfTenacity1 = (2052)
    ForestOfTenacity2 = (2053)
    ForestOfTenacity3 = (2054)
    HerosGladius = (2047)
    HerosGladiusChis = (2048)

    quest1 = Quest.GetQuestState(DrakeAttack1)
    quest2 = Quest.GetQuestState(DrakeAttack2)
    quest3 = Quest.GetQuestState(DrakeAttack3)
    quest4 = Quest.GetQuestState(DrakeAttack4)
    quest5 = Quest.GetQuestState(DrakeAttack5)
    quest6 = Quest.GetQuestState(InjuredAdventurer)
    quest7 = Quest.GetQuestState(InjuredAdventurer2)
    quest8 = Quest.GetQuestState(InjuredAdventurer3)
    quest9 = Quest.GetQuestState(InjuredAdventurer4)
    quest10 = Quest.GetQuestState(RonniesMarble)
    quest11 = Quest.GetQuestState(MysteriousNote)
    quest12 = Quest.GetQuestState(MysteriousNote2)
    quest13 = Quest.GetQuestState(ASpellThatSealsUpACriticalDanger)
    quest14 = Quest.GetQuestState(ASpellThatSealsUpACriticalDanger2)
    quest15 = Quest.GetQuestState(ForestOfTenacity1)
    quest16 = Quest.GetQuestState(ForestOfTenacity2)
    quest17 = Quest.GetQuestState(ForestOfTenacity3)
    #Complete quest1 (DrakeAttack1)
    if quest1 != 2:
        if quest1 ==0:
            acceptQuest(DrakeAttack1, Ilji, SleepyWood, field_id)
        elif quest1 ==1:
            completeQuest(DrakeAttack1, Ilji, SleepyWood, HumidSwamp, field_id)
        elif quest1 ==-1:
            Terminal.Rush(SleepyWood)
    #complete quest2 (DrakeAttack2)
    elif quest2 != 2:
        if quest2 ==0:
            acceptQuest(DrakeAttack2, Ilji, SleepyWood, field_id)
        elif quest2 ==1:
            completeQuest(DrakeAttack2, Ilji, SleepyWood, SunlessArea, field_id)
    #complete quest3 (DrakeAttack3)
    elif quest3 != 2:
        if quest3 ==0:
            acceptQuest(DrakeAttack3, Ilji, SleepyWood, field_id)
        elif quest3 ==1:
            completeQuest(DrakeAttack3, Ilji, SleepyWood, CaveCliff, field_id)
    #complete quest4 (DrakeAttack4)
    elif quest4 != 2:
        if quest4 ==0:
            acceptQuest(DrakeAttack4, Ilji, SleepyWood, field_id)
        elif quest4 ==1:
            completeQuest(DrakeAttack4, Ilji, SleepyWood, ChillyCave, field_id)
    #complete quest5 (DrakeAttack5)
    elif quest5 != 2:
        if quest5 ==0:
            acceptQuest(DrakeAttack5, Ilji, SleepyWood, field_id)
        elif quest5 ==1:
            completeQuest(DrakeAttack5, Ilji, SleepyWood, CaveExit, field_id)
    #complete quest6 (InjuredAdventurer)
    elif quest6 != 2:
        if quest6 ==0:
            acceptQuest(InjuredAdventurer, Ilji, SleepyWood, field_id)
        elif quest6 ==1:
            completeQuest(InjuredAdventurer, Gwin, AnotherDoor, SleepyWood, field_id)
    #complete quest7 (InjuredAdventurer2)
    elif quest7 != 2:
        ToggleHtr(False)
        if quest7 ==0:
            acceptQuest(InjuredAdventurer2, Gwin, AnotherDoor, field_id)
        elif quest7 ==1:
            completeQuest(InjuredAdventurer2, Gwin, AnotherDoor, TempleEntrance, field_id)
    #complete quest8 (InjuredAdventurer3)
    elif quest8 != 2:
        ToggleHtr(False)
        if quest8 ==0:
            acceptQuest(InjuredAdventurer3, Gwin, AnotherDoor, field_id)
        elif quest8 ==1:
            completeQuest(InjuredAdventurer3, Gwin, AnotherDoor, CollapsedTemple, field_id)
    #complete quest9 (InjuredAdventurer4)
    elif quest9 != 2:
        ToggleHtr(True)
        if quest9 ==0:
            acceptQuest(InjuredAdventurer4, Gwin, AnotherDoor, field_id)
        elif quest9 ==1:
            if pos.x != -542:
                Character.Teleport(-525, 1028)
                time.sleep(1)
                Character.EnterPortal()
                time.sleep(1)
                completeQuest(InjuredAdventurer4, Ilji, SleepyWood, SleepyWood, field_id)
    #complete quyest10 (RonniesMarble)
    elif quest10 != 2:
        if quest10 ==0:
            acceptQuest(RonniesMarble, Ronnie, SilentSwamp, field_id)
        elif quest10 ==1:
            completeQuest(RonniesMarble, Ronnie, SilentSwamp, SunlessArea, field_id)
    #complete quest11 (MysteriousNote)
    elif quest11 != 2:
        ToggleHtr(False)
        if quest11 ==0:
            acceptQuest(MysteriousNote, TheNote, SunlessArea, field_id)
        elif quest11 ==1:
            completeQuest(MysteriousNote, MuYoung, BottomoftheTemple, BottomoftheTemple, field_id)
    #complete quest12 (Mysteriousnote2)
    elif quest12 != 2:
        if quest12 ==0:
            ToggleKami(False)
            acceptQuest(MysteriousNote2, MuYoung, BottomoftheTemple, field_id)
        elif quest12 ==1:
            Character.TalkToNpc(TristansSpirit)
            ToggleKami(True)
            completeQuest(MysteriousNote2, TristansSpirit, HerosMemory, HerosMemory, field_id)
    #complete quest13 (ASpellThatSealsUpACriticalDanger)
    elif quest13 !=2:
        ToggleHtr(False)
        if field_id == HerosMemory:
            if pos.x != -343:
                ToggleKami(False)
                Character.Teleport(-343, 190)
            else:
                Character.EnterPortal()
        elif quest13 ==0:
            acceptQuest(ASpellThatSealsUpACriticalDanger, InsignificantBeing, AnotherDoor, field_id)
        elif quest13 ==1:
            completeQuest(ASpellThatSealsUpACriticalDanger, InsignificantBeing, AnotherDoor, ChillyCave, field_id)
    #complete quest14 (ASpellThatSealsUpACriticalDanger2)
    elif quest14 !=2: 
        ToggleHtr(False)
        if quest14 ==0:
            acceptQuest(ASpellThatSealsUpACriticalDanger2, InsignificantBeing, AnotherDoor, field_id)
        elif quest14 ==1:
            if Quest.CheckCompleteDemand(ASpellThatSealsUpACriticalDanger2, InsignificantBeing) ==0:
                completeQuest(ASpellThatSealsUpACriticalDanger2, InsignificantBeing, AnotherDoor, AnotherDoor, field_id)
            else:
                ToggleKami(True)
                if Inventory.GetItemCount(4031213) < 10:
                    if field_id != TempleEntrance:
                        Terminal.Rush(TempleEntrance)
                elif Inventory.GetItemCount(4031214) < 10:
                    if field_id != CollapsedTemple:
                        Terminal.Rush(CollapsedTemple)
                elif Inventory.GetItemCount(4031215) < 10:
                    if field_id != ForbiddenAltar:
                        Terminal.Rush(ForbiddenAltar)
    #complete quest15 (ForestOfTenacity1)
    elif quest15 !=2:
        #print("here")
        if field_id == AnotherDoor:
            if pos.x != -523:
                Character.Teleport(-523, 1028)
                time.sleep(1)
            ToggleAttackQuest(False)
            Character.EnterPortal()
            time.sleep(1)
        if quest15 ==0:
            #print("trying to accept quest")
            if field_id == BottomoftheTemple or field_id == 105100000:
                ToggleHtr(False)
                RushTo(AnotherDoor)
                time.sleep(2)
            ToggleHtr(True)
            acceptQuest(ForestOfTenacity1, John, SleepyWood, field_id)
        elif quest15 ==1:
            if Quest.CheckCompleteDemand(ForestOfTenacity1, John)==0:
                completeQuest(ForestOfTenacity1, John, SleepyWood,SleepyWood, field_id)
            else:
                if field_id != 910530001:
                    if field_id != 910530000:
                        if field_id != SleepyWood:
                            Terminal.Rush(SleepyWood)
                        if pos.x != 1038:
                            Character.Teleport(1038, 255)
                            time.sleep(3)
                            Character.TalkToNpc(1061006)
                            time.sleep(2)
                    elif field_id == 910530000:
                        if pos.x != -75:
                            Character.Teleport(-75, -2685)
                        else:
                            ToggleAttackQuest(False)
                            Character.EnterPortal()
                if field_id == 910530001:
                    if pos.x != 762:
                        Character.Teleport(762, -2325)
                    else:
                        Character.TalkToNpc(1063000)
    #complete quest16 (ForestOfTenacity2)
    elif quest16 != 2:
        if quest16 ==0:
            acceptQuest(ForestOfTenacity2, John, SleepyWood, field_id)
        if quest16 ==1:
            if Quest.CheckCompleteDemand(ForestOfTenacity2, John) ==0:
                completeQuest(ForestOfTenacity2, John, SleepyWood,SleepyWood, field_id)
            else:
                if field_id != 910530101:
                    if field_id != 910530100:
                        if field_id != SleepyWood:
                            Terminal.Rush(SleepyWood)
                        if pos.x != 887:
                            Character.Teleport(887, 255)
                        else:
                            Character.TalkToNpc(1061006)
                    if field_id == 910530100:
                        if pos.x != 1259:
                            Character.Teleport(1259, -2565)
                            time.sleep(1)
                        else:
                            ToggleAttackQuest(False)
                            Character.EnterPortal()
                if field_id == 910530101:
                    if pos.x != -434:
                        Character.Teleport(-434, -1935)
                        time.sleep(1)
                    else:
                        Character.TalkToNpc(1063001)
    #complete quest17 (ForestOfTenacity3)
    elif quest17 != 2:
        if quest17 ==0:
            acceptQuest(ForestOfTenacity3, John, SleepyWood, field_id)
        elif quest17 ==1:
            if Quest.CheckCompleteDemand(ForestOfTenacity3, John)==0:
                completeQuest(ForestOfTenacity3, John, SleepyWood, SleepyWood, field_id)
                ToggleHtr(True)
                ToggleRushByLevel(True)
                ToggleKami(True)
                SCLib.UpdateVar("DoingSleepy",False)
                print("Resume rush by level; sleepywood")
                quest17 = Quest.GetQuestState(ForestOfTenacity3)
                if quest17 == 2:
                    ToggleHtr(True)
                    ToggleRushByLevel(True)
                    ToggleKami(True)
                    print("Resume rush by level; sleepy wood")
            else:
                if field_id != 910530202:
                    if field_id != 910530201:
                        if field_id != 910530200:
                            if field_id != SleepyWood:
                                Terminal.Rush(SleepyWood)
                            if pos.x != 887:
                                Character.Teleport(887, 255)
                                time.sleep(2)
                            else:
                                Character.TalkToNpc(1061006)
                                time.sleep(2)
                        if field_id == 910530200:
                            if pos.x != 1523:
                                Character.Teleport(1523, -1905)
                                time.sleep(1)
                            else:
                                ToggleAttackQuest(False)
                                Character.EnterPortal()
                                time.sleep(1)
                    if field_id == 910530201:
                        if pos.x != 255:
                            Character.Teleport(255, -1545)
                            time.sleep(1)
                        else:
                            ToggleAttackQuest(False)
                            Character.EnterPortal()
                            time.sleep(1)
                if field_id == 910530202:
                    if pos.x != 1009:
                        Character.Teleport(1009, -3345)
                        time.sleep(1)
                    else:
                        Character.TalkToNpc(1063002)
                        time.sleep(1)



#auto star force pensalir gear and accessories
if level >= 61 and star_force and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and Character.GetMeso()>= 5000000:
    #if level >= 140:
    #    for equips in equip_slot_list:
    #        item = Inventory.GetItem(1,equips)
    #        if item.valid and item.currentStar != star_force_level:
    #            #print("Starforcing item {}".format(item.id))
    #            StarItem(equips, item.currentStar, item.maxStar, star_force_level, item.id)
    #    for accessories in accessory_slot_list:
    #        item = Inventory.GetItem(1,accessories)
    #        if item.valid and item.id in accessory_list and item.currentStar != star_force_level:
    #            #print("Starforcing item {}".format(item.id))
    #            StarItem(accessories, item.currentStar, item.maxStar, star_force_level, item.id)
    count = 0
    for x in range(-100, 0):
        item = Inventory.GetItem(1, x)
        if item.valid and item.currentStar != star_force_level and item.currentStar != item.maxStar and (level < 130 or item.maxStar != 20):
            count += 1
            StarItem(x, item.currentStar, item.maxStar, star_force_level, item.id)
            if count >= 2:
                print("Starred 2  times, break for now")
                break
#print(SCLib.GetVar("DoingZakum"))
#ZAKUM DAILY
#print(KillZakumDaily)
if (KillZakumDaily == False or not SCLib.GetVar("DoingZakum")) and (field_id == 211042200 or field_id == TheDoorToZakum or field_id == EntranceToZakumAlter) and not SCLib.GetVar("DoingMP"):
    if field_id == TheDoorToZakum:
        ToggleKami(False)
        TeleportEnter(-3003,-220)
        ToggleRushByLevel(True)
        ToggleLoot(False)
        Terminal.SetCheckBox("Kami Vac",True)
        Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
        SCLib.UpdateVar("DoingZakum",False)
        print("Resume rush by level; Zakum")
    elif (field_id == TheDoorToZakum or field_id == EntranceToZakumAlter or field_id == TheCaveOfTrials3Zakum):
        ToggleKami(False)
        TeleportEnter(-1599,-331)
        ToggleLoot(False)
        SCLib.UpdateVar("DoingZakum",False)
        if field_id == TheCaveOfTrials3Zakum:
            ToggleRushByLevel(True)
            ToggleLoot(False)
            SCLib.UpdateVar("DoingZakum",False)
            print("Resume rush by level; Zakum")

runebuff_id = 80002280
if KillZakumDaily and level >= 105 and (Character.GetEquippedItemIDBySlot(face_slot) != condensed_power_crystal or Character.GetEquippedItemIDBySlot(eye_slot) != aquatic_letter_eye) and Terminal.GetLineEdit("LoginChar") not in accountData['done_zakum'] and (Character.HasBuff(2,runebuff_id) or SCLib.GetVar("DoingZakum")) and not SCLib.GetVar("DoingMP"):
    print("Doing Zakum")
    Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
    if Terminal.GetCheckBox("Kami Vac"):
        Terminal.SetCheckBox("Kami Vac",False)
    if getSpider:
        Terminal.SetComboBox("Familiar0",2)
    else:
        Terminal.SetComboBox("Familiar0",1)
    ToggleRushByLevel(False)
    Terminal.SetCheckBox('filter_equip',False)
    SCLib.UpdateVar("DoingZakum",True)
    pos = Character.GetPos()
    if field_id not in ZakumsAltar:
        if field_id != EntranceToZakumAlter:
            if field_id != TheDoorToZakum:
                GetToTheDoorToZakum()
            else:
                if pos.x not in range(-725,-715):
                    NewY = pos.y -5
                    Character.Teleport(-720, NewY)
                elif Inventory.GetItemCount(4001017) < 1:
                    print("Getting offer")
                    Npc.ClearSelection()
                    Npc.RegisterSelection("Receive an offering for Zakum.")
                    time.sleep(1)
                    Npc.RegisterSelection("Normal/Chaos Zakum")
                    Character.TalkToNpc(2030008)
                    time.sleep(1)
                elif Inventory.GetItemCount(4001017) >= 1:
                    print("Entering Portal to EntranceToZakumAlter")
                    Npc.ClearSelection()
                    Npc.RegisterSelection("Normal Zakum")
                    time.sleep(1)
                    Character.EnterPortal()
                    time.sleep(1)
        else:
            if not NowLockedVar:
                if SCLib.GetVar("zakum_retry_count") >= 7:
                    SCLib.UpdateVar("KillZakumDaily",False)
                    accountData['done_zakum'].append(Terminal.GetLineEdit("LoginChar"))
                    WriteJson(accountData,accountId)
                    ResetNowLockedFunction()
                else:
                    Party.CreateParty()
                    print("Talking to Adobis to enter ZakumsAltar")
                    Character.TalkToNpc(2030013)
                    SCLib.UpdateVar("zakum_retry_count",SCLib.GetVar("zakum_retry_count")+1)
                    time.sleep(1)

            else:
                print("Seems like you diddnt finish your last attempt and are locked. Continueing other bosses")
                SCLib.UpdateVar("KillZakumDaily", False)
                SCLib.UpdateVar("DoingZakum",False)
                accountData['done_zakum'].append(Terminal.GetLineEdit("LoginChar"))
                WriteJson(accountData,accountId)
                ResetNowLockedFunction()
    else:
        print("In zakum altar")
        NowLockedFunction()
        boss2 = Field.FindMob(NormalZakumv2)
        boss1 = Field.FindMob(NormalZakumv1)
        boss = Field.FindMob(NormalZakum)
        if boss.valid or boss1.valid or boss2.valid:
            print("Boss valid")
            DidSpawn()
            if pos.x != -260:
                Character.Teleport(-260, 84)
                ToggleAttackQuest(True)
            else:
                print("Fighting Zakum StandBy")
        else:
            if HasSpawned:
                ToggleLoot(True)
                print("Zakum is dead, waiting 10 sec before continue")
                time.sleep(5)
                face_drop = Field.FindItem(condensed_power_crystal)
                if face_drop.valid:
                    print("Found condensed power crystal")
                    Character.Teleport(face_drop.x,face_drop.y)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(3)
                eye_drop = Field.FindItem(aquatic_letter_eye)
                if eye_drop.valid:
                    print("Found aquatic letter eye")
                    Character.Teleport(eye_drop.x,eye_drop.y)
                    Terminal.SetCheckBox("Auto Loot",True)
                    time.sleep(3)
                face_check = Field.FindItem(condensed_power_crystal)
                eye_check = Field.FindItem(aquatic_letter_eye)
                time.sleep(5)
                if not face_check.valid and not eye_check.valid:
                    print("Did not find accessory, leaving.")
                    Terminal.SetComboBox("Familiar0",1)
                    Character.TalkToNpc(2030010)
                    time.sleep(1)
                    SCLib.UpdateVar("KillZakumDaily", False)
                    #if accountData['cur_link_pos'] == '11':
                    #    accountData['daily_done'] = True
                    #    WriteJson(accountData,accountId)
                    ResetSpawn()
                    ResetNowLockedFunction()
                    if field_id == TheDoorToZakum:
                        if pos.x != -3003:
                            Character.Teleport(-3003, -220)
                            time.sleep(1)
                            Character.EnterPortal()
                            SCLib.UpdateVar("DoingZakum",False)
                            accountData['done_zakum'].append(Terminal.GetLineEdit("LoginChar"))
                            WriteJson(accountData,accountId)

            else:
                print("Finding item in inventory to drop")
                stone = Inventory.FindItemByID(4001017)
                if stone.valid:
                    if pos.x != -25:
                        Character.Teleport(-25, 84)
                    else:
                        print("Dropping stone to spawn Zakum")
                        Inventory.SendChangeSlotPositionRequest(4, stone.pos, 0, 1)
                        ToggleAttackQuest(False)
                        time.sleep(6)
                elif not stone.valid:
                    ToggleLoot(True)
                    print("Zakum is dead, waiting 10 sec before continue")
                    time.sleep(5)
                    face_drop = Field.FindItem(condensed_power_crystal)
                    if face_drop.valid:
                        print("Found condensed power crystal")
                        Character.Teleport(face_drop.x,face_drop.y)
                        Terminal.SetCheckBox("Auto Loot",True)
                        time.sleep(3)
                    eye_drop = Field.FindItem(aquatic_letter_eye)
                    if eye_drop.valid:
                        print("Found aquatic letter eye")
                        Character.Teleport(eye_drop.x,eye_drop.y)
                        Terminal.SetCheckBox("Auto Loot",True)
                        time.sleep(3)
                    face_check = Field.FindItem(condensed_power_crystal)
                    eye_check = Field.FindItem(aquatic_letter_eye)
                    time.sleep(5)
                    if not face_check.valid and not eye_check.valid:
                        print("Did not find accessory, leaving.")
                        Terminal.SetComboBox("Familiar0",1)
                        Character.TalkToNpc(2030010)
                        time.sleep(1)
                        SCLib.UpdateVar("KillZakumDaily", False)
                        #if accountData['cur_link_pos'] == '11':
                        #    accountData['daily_done'] = True
                        #    WriteJson(accountData,accountId)
                        ResetSpawn()
                        ResetNowLockedFunction()
                        if field_id == TheDoorToZakum:
                            if pos.x != -3003:
                                Character.Teleport(-3003, -220)
                                time.sleep(1)
                                Character.EnterPortal()
                                SCLib.UpdateVar("DoingZakum",False)
                                accountData['done_zakum'].append(Terminal.GetLineEdit("LoginChar"))
                                WriteJson(accountData,accountId)
if GameState.IsInGame() and SCLib.GetVar("BuyExpansion") and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingJobAdv"):
    BuyExpansion()

if not SCLib.GetVar("BuyExpansion") and field_id == 240000002 and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock"):
    ToggleRushByLevel(True)
    ToggleKami(True)
    print("Resume rush by level; general store")

if GameState.IsInGame() and level < 140 and Inventory.FindItemByID(5040004).valid and not SCLib.GetVar("GettingBoogie") and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock") and useExploit and not SCLib.GetVar("DoingJobAdv"):
    print("Doing exploit")
    if field_id == TheDoorToZakum:
        if pos.x != -3003:
            ToggleKami(False)
            TeleportEnter(-3003,-220)
            ToggleRushByLevel(True)
            Terminal.SetCheckBox("Kami Vac",True)
            Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
            SCLib.UpdateVar("DoingZakum",False)
            print("Resume rush by level; zakum -> exploit")
    elif (field_id == TheDoorToZakum or field_id == EntranceToZakumAlter or field_id == TheCaveOfTrials3Zakum):
        if pos.x != -1599:
            ToggleKami(False)
            TeleportEnter(-1599,-331)
            SCLib.UpdateVar("DoingZakum",False)
    Exploit1()
    Terminal.SetComboBox("eva_cmb",1)
    Terminal.SetComboBox("HackingOpt",1)
    Terminal.SetCheckBox("Legit Vac",False)
elif GameState.IsInGame() and level < 50 or not Inventory.FindItemByID(5040004).valid or not useExploit:
    Terminal.SetComboBox("eva_cmb",3)
    Terminal.SetComboBox("HackingOpt",2)
    if field_id == 130030106:
        Terminal.SetCheckBox("Legit Vac",False)
    else:
        Terminal.SetCheckBox("Legit Vac",True)

if GameState.IsInGame() and level >= 33 and doEvent and not SCLib.GetVar("GettingBoogie") and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingJobAdv"):
    EventQuests()


if level >= 106 and Terminal.GetCheckBox("Rush By Level") and not SCLib.GetVar("GettingBoogie") and not SCLib.GetVar("DoingMP") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingJobAdv"):
    Terminal.SetCheckBox("timedCCCheck",True)
else:
    Terminal.SetCheckBox("timedCCCheck",False)

if job in KannaJobs and level >= 145 and level < 152:
    ToggleRushByLevel(False)
    if field_id != 240000000:
        RushTo(240000000)
    else:
        time.sleep(5)

def GetNextChar(current_list):
    doAllJobs = True
    autoChar_resistance = 1
    autoChar_explorer = 2
    autoChar_cygnus = 3
    autoChar_aran = 4
    autoChar_evan = 5
    autoChar_mercedes = 6
    autoChar_demon = 7
    autoChar_phantom = 8
    autoChar_dualblade = 9
    autoChar_mihile = 10
    autoChar_luminous = 11
    autoChar_kaiser = 12
    autoChar_angel = 13
    autoChar_cannoneer = 14
    autoChar_xenon = 15
    autoChar_shade = 16
    autoChar_jett = 17
    autoChar_hayato =18
    autoChar_kanna = 19
    autoChar_kinesis = 21
    autoChar_cadena = 22
    autoChar_illium = 23
    autoChar_ark = 24
    
    if "Thunder Breaker" not in current_list:
        return autoChar_cygnus
    elif "Phantom" not in current_list:
        return autoChar_phantom
    elif "Aran" not in current_list:
        return autoChar_aran
    elif "Evan" not in current_list:
        return autoChar_evan
    elif "Mercedes" not in current_list:
        return autoChar_mercedes
    elif "Luminous" not in current_list:
        return autoChar_luminous
    elif "Shade" not in current_list:
        return autoChar_shade
    elif "Demon Avenger" not in current_list or "Demon Slayer" not in current_list:
        return autoChar_demon
    #elif "Mihile" not in current_list:
    #    return autoChar_mihile
    elif "Kaiser" not in current_list:
        return autoChar_kaiser
    elif "Angelic Buster" not in current_list:
        return autoChar_angel
    elif "Xenon" not in current_list:
        return autoChar_xenon
    elif "Cannoneer" not in current_list:
        return autoChar_cannoneer
    elif "Hayato" not in current_list:
        return autoChar_hayato
    elif "Cadena" not in current_list:
        return autoChar_cadena
    elif "Kinesis" not in current_list:
        return autoChar_kinesis
    elif "Illium" not in current_list:
        return autoChar_illium
    elif "Ark" not in current_list:
        return autoChar_ark
    elif "Jett" not in current_list:
        return autoChar_jett
    elif "Kanna" not in current_list:
        return autoChar_kanna
    elif doAllJobs:
        resistance_jobs = ["Blaster","Wild Hunter","Battle Mage","Mechanic"]
        for resistance_job in resistance_jobs:
            if resistance_job not in current_list:
                return autoChar_resistance
        explorer_jobs = ["Shadower","Night Lord","Hero","Paladin","Dark Knight","Ice/Lightning Archmage","Fire/Poison Archmage","Bishop","Bowmaster","Marksman","Corsair","Buccaneer"]
        for explorer_job in explorer_jobs:
            if explorer_job not in current_list:
                return autoChar_explorer
        cygnus_jobs = ["Dawn Warrior","Wind Archer","Night Walker","Thunder Breaker","Blaze Wizard"]
        for cygnus_job in cygnus_jobs:
            if cygnus_job not in current_list:
                return autoChar_cygnus
        if "Dual Blade" not in current_list:
            return autoChar_dualblade
    else:
        return 0

if int(Terminal.GetLineEdit("LoginChar")) >= Login.GetCharCount() and GameState.GetLoginStep() == 2:
    all_jobs = [
        "Evan",
        "Blaze Wizard",
        "Luminous",
        "Kanna",
        "Demon Avenger",
        "Xenon",
        "Blaster",
        "Illium",
        "Cadena",
        "Aran",
        "Mercedes",
        "Phantom",
        "Demon Slayer",
        "Hayato",
        "Kinesis",
        "Shadower",
        "Night Lord",
        "Hero",
        "Paladin",
        "Dark Knight",
        "Ice/Lightning Archmage",
        "Fire/Poison Archmage",
        "Bishop",
        "Bowmaster",
        "Marksman",
        "Corsair",
        "Buccaneer",
        "Jett",
        "Cannoneer",
        "Dual Blade",
        "Dawn Warrior",
        "Wind Archer",
        "Night Walker",
        "Thunder Breaker",
        "Wild Hunter",
        "Battle Mage",
        "Mechanic",
        "Angelic Buster",
        "Kaiser",
        "Beast Tamer",
        "Ark",
        "Shade",
        "Mihile"
    ]
    current = set(all_jobs)
    done_jobs = []
    for x in range(Login.GetCharCount()):
        #print(set(Id2Str(Login.GetChar(x).jobid)))
        if Login.GetChar(x).level >= 140:
            current -= set((Id2Str(Login.GetChar(x).jobid),))
            done_jobs.append(Id2Str(Login.GetChar(x).jobid))
    print("Missing {} jobs {}".format(len(list(current)),str(current)))
    Terminal.SetComboBox("settings/autochar_job",GetNextChar(done_jobs))
    print(GetNextChar(done_jobs))
    if GetNextChar(done_jobs) == 0:
        Terminal.SetCheckBox("Auto Login",False)
        Terminal.SetCheckBox("settings/autochar",False)
    else:
        Terminal.SetCheckBox("Auto Login",True)
        Terminal.SetCheckBox("settings/autochar",True)
    time.sleep(1)
    

##########Map specific settings
if field_id == 105020400:
    Terminal.SetLineEdit("nextmapccportal","west00")
elif field_id == 105020401:
    DungeonTeleport()
elif field_id == 273040300:
    if pos.x != -1271:
        Character.Teleport(-1271,1215)
        time.sleep(30)
elif field_id == 271030540:
    if pos.x != -151:
        Character.Teleport(-151,208)
        time.sleep(30)
elif field_id == 273020300:
    if pos.x != -695:
        Character.Teleport(-695,375)
        time.sleep(30)
else:
    Terminal.SetLineEdit("nextmapccportal","west00")


buffmap_id = 701100015
xpbonus = 2023532
mesobonus = 2023533
attbonus = 2023534
hs = 2311003
htr = 5040004

if level > 63 and Inventory.FindItemByID(htr).valid and not SCLib.GetVar("DoingCurbrock") and not SCLib.GetVar("DoingZakum") and not SCLib.GetVar("DoingJobAdv"):
    # Checks for Fortune Buff
    if not Character.HasBuff(1, xpbonus):
        #ToggleRushByLevel(False)
        if map is not buffmap_id:
            useHTR = Terminal.GetCheckBox("map/maprusher/hypertelerock")
            Terminal.SetCheckBox("map/maprusher/hypertelerock",True)
            Terminal.Rush(buffmap_id)
            Terminal.SetCheckBox("map/maprusher/hypertelerock",useHTR)

def ChooseLightPath():
    choosePacket = Packet.COutPacket(headers.dialogue_header)
    choosePacket.EncodeBuffer("1A 01 00000000")
    Packet.SendPacket(choosePacket)

if field_id == 927020000:
    ToggleRushByLevel(False)
    ChooseLightPath()
    time.sleep(1)