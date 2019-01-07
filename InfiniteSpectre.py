# Infinite Specter State by dolbaeb
# v1 - 30/09/2018
# v2 - 05/10/2018 <- updated opcodes
#
# Notes:
#   If your Abyssal Recall is not level 30, change it in Ark.Abyssal_Recall from 30 to your skill level!
#   You are required to have the Abyssal Recall skill node equipped to use this script.

import time

import Character
import Field
import GameState
import Packet
import Quest
import Terminal

# This is how I use my fancy enum classes Dan. Deal with it!
class Ark():
    Job_ID = 15512
    Specter_State = 155000007
    Abyssal_Recall = [400051334, 400051035, 6] # <- SKILL LEVEL
    Knuckle_Booster = 155101005

class QuestStatus():
    NotStarted = 0
    Started = 1
    Completed = 2

class BuffType():
    Item = 1
    Skill = 2

class CommonSkills():
    # indieBooster -1
    Beginner_DSI = [
        8006, 10008006, 20008006, 20018006, 20028006, 20038006,
        20048006, 20058006, 30008006, 30018006, 30028006,
        50008006, 60008006, 60018006, 60028006, 100008006,
        130008006, 140008006, 150008006, 110008006, 40018006,
        40028006, 150018006
    ]

    VMatrix_DSI = 400001006

    # indieBooster -2
    Real_SI = [
        5121009, 15111005, 15121005, 5821009
    ]

    # indieBooster -3
    Lure_of_Swiftness = 80002215
    Liberate_the_Swift_Rune = 80001427

    # indieBooster -1
    Liberate_the_Destructive_Rune = 80001432

class BaseAttackSpeed():
    Fastest2 = 0
    Fastest = 1
    Faster2 = 2
    Faster = 3
    Fast2 = 4
    Fast = 5
    Normal = 6
    Slow2 = 7
    Slow = 8
    Slower = 9

# Green MP pots. Both give indieBooster -1
EXTREME_GREEN_POTION1 = 2023126
EXTREME_GREEN_POTION2 = 2023554

# 5th job quest
FIFTH_JOB_RECORD_OF_POWER = 1465

# Headers
USER_SKILL_CANCEL_REQUEST = 329
USER_SKILL_PREPARE_REQUEST = 330

def get_update_time():
    return int(time.monotonic() * 1000)

def get_attack_speed_degree():
    attSpeed = BaseAttackSpeed.Fast # Knuckle is usually Fast

    if Character.HasBuff(BuffType.Skill, Ark.Knuckle_Booster):
        attSpeed -= 2
  
    if Character.HasBuff(BuffType.Skill, CommonSkills.VMatrix_DSI):
        attSpeed -= 1
  
    else:
        for nSkillID in CommonSkills.Beginner_DSI:
            if Character.HasBuff(BuffType.Skill, nSkillID):
                attSpeed -= 1
                break
      
        for nSkillID in CommonSkills.Real_SI:
            if Character.HasBuff(BuffType.Skill, nSkillID):
                attSpeed -= 2
                break

    canBypassCap = False

    if Character.HasBuff(BuffType.Item, EXTREME_GREEN_POTION1) or Character.HasBuff(BuffType.Item, EXTREME_GREEN_POTION2):
        canBypassCap = True
        attSpeed -= 1
  
    if Character.HasBuff(BuffType.Skill, CommonSkills.Lure_of_Swiftness) or Character.HasBuff(BuffType.Skill, CommonSkills.Liberate_the_Swift_Rune):
        canBypassCap = True
        attSpeed -= 2

    elif Character.HasBuff(BuffType.Skill, CommonSkills.Liberate_the_Destructive_Rune):
        canBypassCap = True
        attSpeed -= 1

    elif not canBypassCap and attSpeed < 2:
        attSpeed = 2
  
    if attSpeed < 0:
        attSpeed = 0

    return attSpeed

def user_skill_prepare_request(nRequestTime, nSkillID, nSLV, nActionSpeed):
    oPacket = Packet.COutPacket(USER_SKILL_PREPARE_REQUEST)
    oPacket.Encode4(nSkillID)
    oPacket.Encode1(nSLV)
    oPacket.Encode1(nActionSpeed)
    oPacket.Encode4(0xFFFFFFFF)
    oPacket.Encode4(nRequestTime)
    oPacket.Encode4(0)
    Packet.SendPacket(oPacket)

def user_skill_cancel_request(nSkillID):
    oPacket = Packet.COutPacket(USER_SKILL_CANCEL_REQUEST)
    oPacket.Encode4(nSkillID)
    oPacket.Encode1(1)
    Packet.SendPacket(oPacket)

if GameState.IsInGame() and \
    not Terminal.IsRushing() and \
    Field.GetMobCount() > 0 and \
    Character.GetJob() == Ark.Job_ID and \
    Quest.GetQuestState(FIFTH_JOB_RECORD_OF_POWER) == QuestStatus.Completed and \
    (Character.GetBuff(BuffType.Skill, Ark.Abyssal_Recall[1]).timeLeft < 5000 or not Character.HasBuff(BuffType.Skill, Ark.Specter_State)):
    user_skill_prepare_request(get_update_time(), Ark.Abyssal_Recall[0], Ark.Abyssal_Recall[2], get_attack_speed_degree())
    user_skill_cancel_request(Ark.Abyssal_Recall[0])
print(Character.GetBuffs()[3].id)
if not Character.HasBuff(2,Ark.Abyssal_Recall[1]):
    Terminal.SetCheckBox("Skill Injection",False)
elif Character.HasBuff(2,Ark.Abyssal_Recall[1]):
    Terminal.SetCheckBox("Skill Injection",True)