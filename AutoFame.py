import Character
import Packet
import Field
import GameState
import time
import Login
import Terminal
import Quest

fameCharacter = 'NikuBenKi'
fameMap = 807000000
accountPIC = '000111'
channel = 14

if GameState.IsInGame():
    if Quest.GetQuestState(57402) != 2:
        if Field.GetID() == 807040000 or Field.GetID() == 807040100:
            quest1 = Quest.GetQuestState(57400)
            quest2 = Quest.GetQuestState(57401)
            quest3 = Quest.GetQuestState(57402)
            if quest1 != 2:
                Quest.StartQuest(57400, 0)
            elif quest2 != 2:
                if quest2 == 0:
                    Quest.StartQuest(57401, 9130082)
                else:
                    Quest.CompleteQuest(57401, 9130082)
            elif quest3 != 2:
                if quest3 == 0:
                    Quest.StartQuest(57402, 0)
                elif quest3 == 1:
                    if Field.GetID() != 807040100:
                        Terminal.Rush(807040100)
                    else:
                        Quest.CompleteQuest(57402, 9130083)
                       
    if Character.GetLevel() < 15:
        Terminal.SetCheckBox('Kami Vac', True)
    else:
        Terminal.SetCheckBox('Kami Vac', False)
        Terminal.Rush(fameMap)
   
    if Field.GetID() == fameMap:
        if channel != GameState.GetChannel():
            Terminal.ChangeChannel(channel)
            while Terminal.IsRushing():
                time.sleep(1)
        famePerson = Field.FindCharacter(fameCharacter)
        if famePerson.valid:
            print("Faming Character {}".format(fameCharacter))
            Character.Teleport(famePerson.x, famePerson.y)
            time.sleep(3)
            charPacket = Packet.COutPacket(0x0159)
            charPacket.Encode4(int(time.monotonic()*1000))
            charPacket.Encode4(famePerson.id)
            charPacket.EncodeBuffer('FF 00 01 00 00')
            Packet.SendPacket(charPacket)
            time.sleep(2)
            famePacket = Packet.COutPacket(0x0157)
            famePacket.Encode4(famePerson.id)
            famePacket.EncodeBuffer('01')
            Packet.SendPacket(famePacket)
            time.sleep(1)
            Packet.SendPacket(famePacket)
            Terminal.SetProperty('lastFameChar', Character.GetName())
            Terminal.Logout()
   
if GameState.GetLoginStep() == 2 and Login.GetCharCount() > 0:
    if Login.GetChar(0).name == Terminal.GetProperty('lastFameChar', 'lol'):
        print("Deleting {}".format(Terminal.GetProperty('lastFameChar','lol')))
        deleteChar = Packet.COutPacket(0x0082)
        deleteChar.EncodeString(accountPIC)
        deleteChar.Encode4(Login.GetChar(0).id)
        Packet.SendPacket(deleteChar)
        time.sleep(1)