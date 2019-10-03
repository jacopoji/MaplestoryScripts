import Character,GameState,Terminal,Inventory
import sys,os,datetime,json
from enum import Enum
sys.path.append('C:/Users/Jacopo/Desktop/Scripts/dependencies')
import JOB_CONSTANTS,PACKET_HEADERS,EQUIP_SLOTS,HELPER


'''configurables'''
do_zakum_daily=True #kill zakum boss
do_horntail_daily = True
star_force = True #Starforce items or not
star_force_level = 10
#do Monster park how many times?
do_monster_park = True
do_MP_count = 2
buy_tickets = 1
#Do IA rerolling
DoIA = True
#Do Cubing
DoCube = True
buy_cube_number = 10 # 720M
#Key to restart pers. variables
HotKey = 0x7A
storage_map_id = 550000000
storage_npc_id = 9270054
buy_character_expansion = True
json_file_route = 'C:/Users/Jacopo/Desktop/TerminalManager/info/'

class StatusEnum(Enum):
    DISCONNECTED = "Disconnected"
    JOBADV = "JobAdv"
    SPIDER = "Spider"
    ZAKUM = "Zakum"
    HORNTAIL = "Horntail"
    MONSTERPARK = "MonsterPark"
    STOREMESO = "StoreMeso"
    CUBING = "Cubing"
    BUYEXPANSION = "BuyExpansion"
    FARMING = "Farming"


class Trainer:
    def __init__(self):
        self.accountId = Terminal.GetLineEdit("LoginID")
        self.accountData = self.startupCheck()
        self.handleReady()
        self.writeJson()
        self.current_date = str(datetime.datetime.utcnow().date())
        self.characterId = Character.GetName()

    def ControlCentre(self):
        status = self.StatusChecker()
        if status == StatusEnum.STOREMESO:
            self.StoreMeso()
        elif status == StatusEnum.DISCONNECTED:
            time.sleep(5)
    def StatusChecker(self):
        '''Returns the current state of the character'''
        '''
        Disconnected `
        Do Job adv `
        Do zakum `
        Do horntail `
        Get Spider Familiar `
        Do Monster Park `
        Store meso `
        Black gate `
        Cubing `
        Buy Expansion `
        '''

        
        logged_in = GameState.IsInGame()

        total_star = HELPER.GetTotalStar()
        
        if doStoreMeso():
            return StatusEnum.STOREMESO
        elif not logged_in:
            return StatusEnum.DISCONNECTED
        elif doJobAdv():
            return StatusEnum.JOBADV
        elif doSpider():
            return StatusEnum.SPIDER
        elif doZakum():
            return StatusEnum.ZAKUM
        elif doHorntail():
            return StatusEnum.HORNTAIL
        elif doMonsterPark():
            return StatusEnum.MONSTERPARK
        elif doCubing():
            return StatusEnum.CUBING
        elif doBuyExpansion():
            return StatusEnum.BUYEXPANSION
        else:
            return StatusEnum.FARMING

    def startupCheck(self):
        split_id = self.accountId.split("@")[0]
        if os.path.exists(json_file_route+'{}.json'.format(split_id)):
            print("Loading")
            with open(json_file_route+'{}.json'.format(split_id)) as f:
                return json.load(f,cls = SetDecoder)
        else:
            print("Creating")
            with open(json_file_route+'{}.json'.format(split_id), "w+") as db_file:
                db_file.write(json.dumps({}))
                return {}

    def handleReady(self):
        false_list = ['ready_for_cube','face_done','eye_done','earring_done','ring_done','necklace_done','cubing_done','storing_meso','pet_expire','training_done','monster_park_done']
        zero_list = ['storage_number','used_slots','total_slots','necklace','eye','face','earring','ring']
        for entry in false_list:
            if entry not in self.accountData:
                self.accountData[entry] = False
        for entry in zero_list:
            if entry not in self.accountData:
                self.accountData[entry] = 0
        if 'kanna_pos' not in self.accountData:
            if Character.GetJob() == 4212:
                self.accountData['kanna_pos'] = Terminal.GetLineEdit("LoginChar")
        if 'IGN' not in self.accountData or self.accountData['IGN'] == '':
            self.accountData['IGN'] = Character.GetName()
        if 'total_meso' not in self.accountData:
            if Character.GetJob() == 4212:
                self.accountData['total_meso'] = int(self.accountData['storage_number']) * 30 + Character.GetMeso() / 1000000000
        if 'date' not in self.accountData:
            self.accountData['date'] = str(datetime.datetime.utcnow().date())
        if 'equips' not in self.accountData:
            self.accountData['equips'] = []
        if 'zakum_daily_done' not in self.accountData:
            self.accountData['zakum_daily_done'] = set()
        if 'horntail_daily_done' not in self.accountData:
            self.accountData['horntail_daily_done'] = set()
    
    def writeJson(self):
        split_id = self.accountId.split("@")[0]
        with open(json_file_route+'{}.json'.format(split_id), 'w') as outfile:
            parsed = json.dumps(self.accountData, indent=4, sort_keys=True,cls = SetEncoder)
            outfile.write(parsed)
            outfile.close()

    def dateCheck(self):
        if self.current_date != self.accountData['date']:
            self.accountData['date'] = self.current_date
            self.accountData['kanna_daily_done'] = False
            self.writeJson()

    def doJobAdv(self):
        level = Character.GetLevel()
        job = Character.GetJob()

        first_job = (job == JOB_CONSTANTS.KannaJobs[0] and level < 13)
        second_job = (job == JOB_CONSTANTS.KannaJobs[0] and level >= 30)
        third_job = False #Automatic
        fourth_job = False #Automatic
        return first_job or second_job or third_job or fourth_job
    
    def doSpider(self):
        has_spider = Character.IsOwnFamiliar(9960295)
        return not has_spider and Character.GetLevel() >= 83

    def doZakum(self):
        return Character.GetLevel() > 120 and not self.characterId in self.accountData['zakum_daily_done'] and do_zakum_daily and not HELPER.FarmedEnoughAccessories()

    def doMonsterPark(self):
        return (level >= 116 and level <= 149) and do_monster_park and not self.accountData['monster_park_done']

    def doStoreMeso(self):
        return self.accountData['storing_meso'] or (Character.GetMeso() == 29999999999 and Character.GetJob() == JOB_CONSTANTS.KannaJobs[3])

    def doBlackGate(self):
        return not HELPER.FarmedEnoughAccessories()

    def doCubing(self):
        necklace = "necklace"
        eye = 'eye'
        face = 'face'
        earring = 'earring'
        ring = 'ring'
        can_cube = not self.accountData['cubing_done'] and Character.GetLevel() >=145
        can_cube = can_cube and HELPER.FarmedEnoughAccessories()
        have_cubes = Inventory.FindItemByID(MISC.red_cube_id).valid or Character.GetMeso() > 800000000
        return can_cube and have_cubes

    def doBuyExpansion(self):
        return self.accountData['pet_expire'] and self.accountData['cubing_done'] and Character.GetJob() in JOB_CONSTANTS.KannaJobs

    def doHorntail(self):
        return Character.GetLevel() > 140 and not self.characterId in self.accountData['horntail_daily_done'] and do_horntail_daily and not HELPER.FarmedEnoughAccessories()

    def StoreMeso(self):
        storage_map_id = 550000000
        storage_npc_id = 9270054
        ###########store mesos
        def store_mesos():
            while True:
                if Field.GetID() == storage_map_id:
                    print("Current Mesos before store = {}".format(Character.GetMeso()))
                    Packet.BlockRecvHeader(PACKET_HEADERS.block_header)
                    Character.Teleport(2268,17)
                    time.sleep(1)
                    Character.TalkToNpc(storage_npc_id)
                    time.sleep(1)
                    oPacket = Packet.COutPacket(PACKET_HEADERS.store_header)
                    oPacket.EncodeBuffer("07 FFFFFFF903DC5401")
                    Packet.SendPacket(oPacket)
                    oPacket1 = Packet.COutPacket(PACKET_HEADERS.store_header)
                    oPacket1.Encode2(8)
                    Packet.SendPacket(oPacket1)
                    print("Completed meso storing")
                    time.sleep(1)
                    print("Current Mesos after store = {}".format(Character.GetMeso()))
                    Packet.UnBlockRecvHeader(PACKET_HEADERS.block_header)
                    break
                else:
                    Terminal.Rush(storage_map_id)
                    print("Still rushing to storage")
                    time.sleep(2)

        def withdraw_mesos():
            if Field.GetID() ==101000000: #wait till character gets to ellinia
                #1032006
                time.sleep(2)
                Packet.BlockRecvHeader(PACKET_HEADERS.block_header)
                print("Current Mesos before withdraw = {}".format(Character.GetMeso()))
                Character.TalkToNpc(1032006)
                time.sleep(3)
                oPacket = Packet.COutPacket(PACKET_HEADERS.store_header)
                oPacket.EncodeBuffer("07 00000006FC23ABFF")
                Packet.SendPacket(oPacket)
                oPacket1 = Packet.COutPacket(PACKET_HEADERS.store_header)
                oPacket1.Encode2(8)
                #oPacket2.EncodeBuffer("08")
                Packet.SendPacket(oPacket1)
                time.sleep(1)
                print("Current Mesos after withdraw = {}".format(Character.GetMeso()))
                time.sleep(1)
                Packet.UnBlockRecvHeader(PACKET_HEADERS.block_header)

            else:
                Terminal.Rush(101000000)
                time.sleep(3)

        if Character.GetMeso() == 29999999999 and Character.GetJob() == 4212:
            #if mesos =29999999999, which is max, store them in the storage
            HELPER.ToggleRushByLevel(False)
            #Terminal.LoadProfile(r"C:\Users\Jacopo\Desktop\TerminalManager\terminalProfiles\StoreMesos.xml")
            if self.accountData['storing_meso'] == False:
                store_mesos()
            #Next step is to change the AutoChar Number and then logon into the new created luminous and release control
            #Read AutoChar Number, +1 write to file.
            time.sleep(3)
            if Character.GetMeso() == 0:
                self.accountData['storing_meso'] = True
                self.writeJson()
                print("logging out")
                if GameState.IsInGame():
                    Terminal.Logout()
                time.sleep(3)
        #print(GameState.GetLoginStep())
        if self.accountData['storing_meso'] and GameState.GetLoginStep() == 2:
            autochar_kanna = 19
            autochar_lumi = 11
            Terminal.SetCheckBox("Auto Login",False)
            Terminal.SetLineEdit("LoginChar", str(accountData['storage_number'] + 1))
            Terminal.SetComboBox("settings/autochar_job",autochar_lumi)
            Terminal.SetCheckBox("Auto Login",True)
            Terminal.SetCheckBox("settings/autochar",True)
        

        if self.accountData['storing_meso'] and Character.GetJob() == 2700 and Character.GetMeso() == 0:
            print("withdrawing mesos")
            HELPER.ToggleRushByLevel(False)
            withdraw_mesos()
            time.sleep(2)
            SCLib.UpdateVar("withdraw_flag",True)
        elif self.accountData['storing_meso'] and Character.GetJob() == 2700 and Character.GetMeso() == 29999999999 and SCLib.GetVar("withdraw_flag"):
            #safe to say that storage is empty and can switch back to kanna
            self.accountData['storage_number'] = self.accountData['storage_number'] + 1
            self.accountData['storing_meso'] = False
            self.writeJson()
            if GameState.IsInGame():
                Terminal.Logout()
            Terminal.SetLineEdit("LoginChar", self.accountData['kanna_pos'])
            SCLib.UpdateVar("withdraw_flag",False)
            print("Logging out and changing to Kanna farmer")
            time.sleep(2)
        elif self.accountData['storing_meso'] and Character.GetJob() == 2700 and Character.GetMeso() != 0 and not SCLib.GetVar("withdraw_flag"):
            #need to update bank number but did not withdraw mesos
            self.accountData['storage_number'] = self.accountData['storage_number'] + 1
            self.writeJson()
            if GameState.IsInGame():
                Terminal.Logout()
            print("Logging out and changing to next bank")
            time.sleep(2)

        def ChooseLightPath():
            choosePacket = Packet.COutPacket(PACKET_HEADERS.dialogue_header)
            choosePacket.EncodeBuffer("1A 01 00000000")
            Packet.SendPacket(choosePacket)

        if Field.GetID() == 927020000:
            ChooseLightPath()
            time.sleep(1)



class SetEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,set):
            return list(obj)
        return json.JSONEncoder.default(self,obj)

class SetDecoder(json.JSONDecoder):
    def default(self,obj):
        if isinstance(obj,list):
            return set(obj)
        return json.JSONDecoder.default(self,obj)

def main():
    if GameState.IsInGame():
        if Terminal.GetProperty("Trainer",-1) == -1:
            Terminal.SetProperty("Trainer",Trainer())
    trainer = Terminal.GetProperty("Trainer",-1)
    if trainer != -1:
        trainer.ControlCentre()
main()

def LoggingIn():
    if GameState.GetLoginStep() == 2:
        self.accountData['total_slots'] = Login.GetCharSlot()
        self.accountData['used_slots'] = Login.GetCharCount()
        self.writeJson()

