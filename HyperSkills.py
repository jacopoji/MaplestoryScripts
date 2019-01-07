# Hyper Skill Assigner by dolbaeb
# v1 - 27/09/2018
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
    God_Of_Blades = [41121054, 0x70] # VK_F1

class Demon_Slayer():
    Blue_Blood = [31121054, 0x71] # VK_F2

class Demon_Avenger():
    Forbidden_Contract = [31221054, 0x72] # VK_F3

class Battle_Mage():
    Master_of_Death = [32121056, 0x73] # VK_F4

class Kaiser():
    Kaisers_Majesty = [61121054, 0x74] # VK_F5

class Angelic_Buster():
    Pretty_Exaltation = [65121054, 0x75] # VK_F6
    Final_Contract = [65121053, 0x76] # VK_F7

class Cadena():
    Shadowdealers_Elixir = [64121054, 0x77] # VK_F8

class Shade():
    Spirit_Bond_Max = [25121131, 0x78] # VK_F9
    Spirit_Bond_Max2 = [25121133, 0x79] # VK_F10

class Mercedes():
    Elvish_Blessing = [23121054, 0x7A] # VK_F11

class Illium():
    Divine_Wrath = [152121042, 0x7B] # VK_F12

class Ark():
    Divine_Wrath = [155121042, 0x31] # 1

class Paladin():
    Sacrosanctity = [1221054, 0x32] # 2
    Epic_Adventure = [1221053, 0x33] # 3

class Hero():
    Cry_Valhalla = [1121054, 0x34] # 4
    Epic_Adventure = [1121053, 0x35] # 5

class Dark_Knight():
    Dark_Thirst = [1321054, 0x36] # 6
    Epic_Adventure = [1321053, 0x37] # 7

class Shadower():
    Epic_Adventure = [4221053, 0x38] # 8

class Night_Lord():
    Bleed_Dart = [4121054, 0x73] # VK_F4
    Epic_Adventure = [4121053, 0x30] # 0

class Blade_Master():
    Epic_Adventure = [4341053, 0x51] # Q

class Jett():
    Bionic_Maximizer = [5721054, 0x5A] # Z
    Epic_Adventure = [5721053, 0x58] # X

class Cannon_Master():
    Buckshot = [5321054, 0x43] # C
    Epic_Adventure = [5321053, 0x56] # V

class Corsair():
    Whalers_Potion = [5221054, 0x42] # B
    Epic_Adventure = [5221053, 0x4E] # N

class Buccaneer():
    Stimulating_Conversation = [5121054, 0x4D] # M
    Epic_Adventure = [5121053, 0x41] # A

class Ice_Lightning():
    Absolute_Zero_Aura = [2221054, 0x44] # D
    Epic_Adventure = [2221053, 0x46] # F

class Fire_Poison():
    Epic_Adventure = [2121053, 0x47] # G

class Bishop():
    Heavens_Door = [2321052, 0x00] # J
    Righteously_Indignant = [2321054, 0x00] # L
    Epic_Adventure = [2321053, 0xBA] # ;:

class Marksman():
    Bullseye_Shot = [3221054, 0xC0] # ~`
    Epic_Adventure = [3221053, 0x52] # R

class Bowmaster():
    Concentration = [3121054, 0x54] # T
    Epic_Adventure = [3121053, 0x59] # Y

class Wind_Archer():
    Storm_Bringer = [13121054, 0x55] # U

class Mihile():
    Sacred_Cube = [51121054, 0x4F] # O

class Dawn_Warrior():
    Soul_Forge = [11121054, 0x50] # P

class Beast_Tamer():
    Team_Roar = [112121056, 0xDB] # [{

class KeyType:
    Skill = 1
    Item = 2

USER_HYPER_SKILL_UP_REQUEST = 496
CHANGE_SKILL_RECORD_RESULT = 95

def bind_skill(skill):
    oPacket = Packet.COutPacket(USER_HYPER_SKILL_UP_REQUEST)
    oPacket.Encode4(int(time.monotonic() * 1000))
    oPacket.Encode4(skill[0])
    Packet.SendPacket(oPacket)

    Packet.WaitForRecv(CHANGE_SKILL_RECORD_RESULT, 10000)
    print("Received {}.".format(skill[0]))

    Key.Set(skill[1], KeyType.Skill, skill[0])

if GameState.IsInGame():
    bind_skill(Angelic_Buster.Final_Contract)
    bind_skill(Ark.Divine_Wrath)
    bind_skill(Bishop.Epic_Adventure)
    bind_skill(Bishop.Heavens_Door)
    bind_skill(Bishop.Righteously_Indignant)
    bind_skill(Blade_Master.Epic_Adventure)
    bind_skill(Bowmaster.Concentration)
    bind_skill(Bowmaster.Epic_Adventure)
    bind_skill(Buccaneer.Epic_Adventure)
    bind_skill(Buccaneer.Stimulating_Conversation)
    bind_skill(Cadena.Shadowdealers_Elixir)
    bind_skill(Cannon_Master.Buckshot)
    bind_skill(Cannon_Master.Epic_Adventure)
    bind_skill(Corsair.Epic_Adventure)
    bind_skill(Corsair.Whalers_Potion)
    bind_skill(Dark_Knight.Dark_Thirst)
    bind_skill(Dark_Knight.Epic_Adventure)
    bind_skill(Demon_Avenger.Forbidden_Contract)
    bind_skill(Demon_Slayer.Blue_Blood)
    bind_skill(Fire_Poison.Epic_Adventure)
    bind_skill(Hayato.God_Of_Blades)
    bind_skill(Hero.Cry_Valhalla)
    bind_skill(Hero.Epic_Adventure)
    bind_skill(Ice_Lightning.Epic_Adventure)
    bind_skill(Illium.Divine_Wrath)
    bind_skill(Jett.Epic_Adventure)
    bind_skill(Marksman.Bullseye_Shot)
    bind_skill(Marksman.Epic_Adventure)
    bind_skill(Mercedes.Elvish_Blessing)
    bind_skill(Mihile.Sacred_Cube)
    bind_skill(Night_Lord.Bleed_Dart)
    bind_skill(Night_Lord.Epic_Adventure)
    bind_skill(Paladin.Epic_Adventure)
    bind_skill(Paladin.Sacrosanctity)
    bind_skill(Shadower.Epic_Adventure)

    # No CD

    bind_skill(Ice_Lightning.Absolute_Zero_Aura)
    bind_skill(Jett.Bionic_Maximizer)

    # These do nothing or just don't work with every weapon.

    # bind_skill(Angelic_Buster.Pretty_Exaltation)
    # bind_skill(Battle_Mage.Master_of_Death)
    # bind_skill(Beast_Tamer.Team_Roar)
    # bind_skill(Dawn_Warrior.Soul_Forge)
    # bind_skill(Kaiser.Kaisers_Majesty)
    # bind_skill(Shade.Spirit_Bond_Max)
    # bind_skill(Shade.Spirit_Bond_Max2)
    # bind_skill(Wind_Archer.Storm_Bringer)