import Packet, Character, time

Header = 0x0205
Skills = [80000400, #STR
          80000401, #DEX
          80000402, #INT
          80000403, #LUK
          80000404, #HP
          80000405, #MP
          80000406, #Demon Fury/Mana
          80000407, #Speed
          80000408, #Jump
          80000409, #Critical Trigger
          80000410, #Critical Damage
          80000411, #Critical Damage
          80000412, #IED
          80000413, #Damage
          80000414, #BD
          80000415, #Elem Resistance
          80000416, #Abnormal Status Resistance
          80000417] #Power Stance

def getUpdateTime():
    return int(time.monotonic() * 1000)

def constructPacket(skillId, skillLevel):
    #014F 2ECCB980 04C4B591 00000001
    oPacket = Packet.COutPacket(Header)
    oPacket.Encode4(getUpdateTime())
    oPacket.Encode4(skillId)
    oPacket.Encode4(skillLevel)
    Packet.SendPacket(oPacket)
    time.sleep(1)

for skill in Skills:
    skill_level = Character.GetSkillLevel(skill)
    if Character.GetSkillLevel(skill) < 5:      #Gets the skill to 5 points.
        constructPacket(skill, 5 - skill_level)

    time.sleep(1)

    skill_level = Character.GetSkillLevel(skill)
    if skill != 80000406 and skill != 80000407 and skill != 80000408:      #If the skill doesn't max out at 5 points, gets it to 10 points.
        constructPacket(skill, 5 - skill_level)