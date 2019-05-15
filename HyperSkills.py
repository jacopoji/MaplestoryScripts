# Hyper Skill Assigner by dolbaeb!!! edited by lalaefi.
# Download - https://mega.nz/#!134mFYyY!r4M0Vfp94wKe6M0scI6wVbkz6aoCeP0RJMDu95-_Yh8
# v1 - 27/09/2018
# v2 - 05/10/2018 <- v199 - updated opcodes.
# v3 - 07/10/2018 <- v199 - added Power Unity.
# v4 - 08/10/2018 <- v199 - added more skills.
# v5 - 17/11/2018 <- v200 - updated opcodes.
# v6 - 21/12/2018 <- v201 - Dragon blaze added.
# v7 - 29/04/2019 <- v204 - Sweeping staff added.
#
#
# Notes:
#   This script is NOT meant to be auto-ran! Run it once by loading it in Scripter -> Editor and then hitting the Run button.
#   Have a clean keyboard in-game. The script will overwrite some of your keys.
#   After level 200, *RELOG*, reset your hyper skills and run this script.
#   Make sure you have at least 1 SP available in the ExtendedSPSet for active hyper skills.

import time
import GameState
import Key
import Packet

class Hayato():
   God_Of_Blades = [41121054, 0x70] # F1

class Demon_Slayer():
   Blue_Blood = [31121054, 0x71] # F2

class Demon_Avenger():
   Forbidden_Contract = [31221054, 0x72] # F3

class Battle_Mage():
   Master_of_Death = [32121056, 0x73] # F4
   Sweeping_Staff = [32121052, 0x58, 160] # X

class Kaiser():
   Kaisers_Majesty = [61121054, 0x74] # F5

class Cadena():
   Shadowdealers_Elixir = [64121054, 0x77] # F8

class Shade():
   Spirit_Bond_Max = [25121131, 0x78] # F9
   Spirit_Bond_Max2 = [25121133, 0x79] # F10

class Mercedes():
   Elvish_Blessing = [23121054, 0x7A] # F11

class Illium():
   Divine_Wrath = [152121042, 0x7B] # F12

class Ark():
   Divine_Wrath = [155121042, 0x31] # 1

class Paladin():
   Epic_Adventure = [1221053, 0x33] # 3
   Sacrosanctity = [1221054, 0x32] # 2

class Hero():
   Cry_Valhalla = [1121054, 0x34] # 4
   Epic_Adventure = [1121053, 0x35] # 5

class Dark_Knight():
   Dark_Thirst = [1321054, 0x36] # 6
   Epic_Adventure = [1321053, 0x37] # 7

class Shadower():
   Epic_Adventure = [4221053, 0x38] # 8

class Night_Lord():
   Bleed_Dart = [4121054, 0x73] # F4
   Epic_Adventure = [4121053, 0x30] # 0

class Blade_Master():
   Epic_Adventure = [4341053, 0x51] # Q

class Jett():
   Epic_Adventure = [5721053, 0x58] # X

class Cannon_Master():
   Buckshot = [5321054, 0x43] # C
   Epic_Adventure = [5321053, 0x56] # V

class Corsair():
   Epic_Adventure = [5221053, 0x4E] # N
   Whalers_Potion = [5221054, 0x42] # B

class Buccaneer():
   Epic_Adventure = [5121053, 0x41] # A
   Power_Unity = [5121052, 0x5A] # Z
   Stimulating_Conversation = [5121054, 0x4D] # M

class Ice_Lightning():
   Absolute_Zero_Aura = [2221054, 0x44] # D
   Epic_Adventure = [2221053, 0x46] # F

class Fire_Poison():
   Epic_Adventure = [2121053, 0x47] # G
   Inferno_Aura = [2121054, 0x55] # U

class Bishop():
   Epic_Adventure = [2321053, 0xBA] # ;
   Heavens_Door = [2321052, 0x4A] # J
   Righteously_Indignant = [2321054, 0x4C] # L

class Blaze_Wizard():
   Dragons_blaze = [12121054, 0xDD] # ]

class Marksman():
   Bullseye_Shot = [3221054, 0xC0] # ~`
   Epic_Adventure = [3221053, 0x52] # R

class Bowmaster():
   Concentration = [3121054, 0x54] # T
   Epic_Adventure = [3121053, 0x59] # Y

class Mihile():
   Charging_Light = [51121052, 0xDB] # [
   Sacred_Cube = [51121054, 0x4F] # O

class Dawn_Warrior():
   Soul_Forge = [11121054, 0x50] # P

class Wild_Hunter():
   Silent_Rampage = [33121054, 0x76] # F7

class Night_Walker():
   Dominion = [14121052, 0x75] # F6

class KeyType:
   Skill = 1
   Item = 2

CP_UserHyperSkillUpRequest = 513 # 0x0201
LP_ChangeSkillRecordResult = 97 # 0x0061

def bind_skill(skill):
    oPacket = Packet.COutPacket(CP_UserHyperSkillUpRequest)
    oPacket.Encode4(int(time.monotonic() * 1000))
    oPacket.Encode4(skill[0])
    Packet.SendPacket(oPacket)

    Packet.WaitForRecv(LP_ChangeSkillRecordResult, 10000)
    print("Received {}.".format(skill[0]))

    Key.Set(skill[1], KeyType.Skill, skill[0])

if GameState.IsInGame():
    bind_skill(Ark.Divine_Wrath)
    bind_skill(Bishop.Heavens_Door)
    bind_skill(Bishop.Righteously_Indignant)
    bind_skill(Blaze_Wizard.Dragons_blaze)
    bind_skill(Bowmaster.Concentration)
    bind_skill(Buccaneer.Power_Unity)
    bind_skill(Buccaneer.Stimulating_Conversation)
    bind_skill(Cadena.Shadowdealers_Elixir)
    bind_skill(Cannon_Master.Buckshot)
    bind_skill(Corsair.Whalers_Potion)
    bind_skill(Dark_Knight.Dark_Thirst)
    bind_skill(Demon_Avenger.Forbidden_Contract)
    bind_skill(Demon_Slayer.Blue_Blood)

    bind_skill(Fire_Poison.Inferno_Aura)
    bind_skill(Hayato.God_Of_Blades)
    bind_skill(Hero.Cry_Valhalla)
    bind_skill(Illium.Divine_Wrath)
    bind_skill(Marksman.Bullseye_Shot)
    bind_skill(Mercedes.Elvish_Blessing)
    bind_skill(Mihile.Charging_Light)
    bind_skill(Mihile.Sacred_Cube)
    bind_skill(Night_Lord.Bleed_Dart)
    bind_skill(Night_Walker.Dominion)
    bind_skill(Paladin.Sacrosanctity)
    bind_skill(Wild_Hunter.Silent_Rampage)
    bind_skill(Ice_Lightning.Absolute_Zero_Aura)
    bind_skill(Battle_Mage.Sweeping_Staff)

    
    # bind_skill(Bishop.Epic_Adventure)
    # bind_skill(Blade_Master.Epic_Adventure)
    # bind_skill(Cannon_Master.Epic_Adventure)
    # bind_skill(Corsair.Epic_Adventure)
    # bind_skill(Dark_Knight.Epic_Adventure)
    # bind_skill(Fire_Poison.Epic_Adventure)
    # bind_skill(Bowmaster.Epic_Adventure)
    # bind_skill(Buccaneer.Epic_Adventure)
    # bind_skill(Hero.Epic_Adventure)
    # bind_skill(Ice_Lightning.Epic_Adventure)
    # bind_skill(Jett.Epic_Adventure)
    # bind_skill(Marksman.Epic_Adventure)
    # bind_skill(Night_Lord.Epic_Adventure)
    # bind_skill(Paladin.Epic_Adventure)
    # bind_skill(Shadower.Epic_Adventure)
    
    #These do nothing or just don't work with every weapon.
    #bind_skill(Battle_Mage.Master_of_Death)
    #bind_skill(Dawn_Warrior.Soul_Forge)
    #bind_skill(Kaiser.Kaisers_Majesty)
    #bind_skill(Shade.Spirit_Bond_Max)
    #bind_skill(Shade.Spirit_Bond_Max2)