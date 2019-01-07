import Character
import DataType
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time
import GameState
# Need To Have Lep Familliar Not Filtered and Farming Settings Enabled

jobid = Character.GetJob()
level = Character.GetLevel()
if Character.GetLevel() >= 103:
    while Character.IsOwnFamiliar(9961073) == False:
        time.sleep(1)
        Terminal.SetRushByLevel(False)
        field_id = Field.GetID()
        time.sleep(1)
        item = Inventory.FindItemByID(2871073) # Lep ID
        if item.valid:
            Inventory.UseFamiliarCard(2871073) # Once Char Gets Lep Uses Card
            Terminal.Rush(600000000) # Rush To Nlc Avoid Rush Bug In Lep Map
            while True:
                if Terminal.IsRushing() == True:
                    time.sleep(1)
                elif Field.GetID() == 600000000:
                    Terminal.SetCheckBox("map/maprusher/hypertelerock", True)
                    Terminal.SetRadioButton("bot/mobvac/old", True)
                    Terminal.SetCheckBox("MonkeySpiritsNDcheck", False)
                    Terminal.SetCheckBox("Grenade Kami", False)
                    Terminal.SetRushByLevel(True) # Set Rush True To Go Back Farming etc
                    time.sleep(3)
                    break
                elif Terminal.IsRushing == False and Field.GetID() == 610010001:
                    Terminal.Rush(600000000)
        else:
            if Field.GetID() != 610010001:
                if Terminal.IsRushing():
                    time.sleep(1)
                else:
                    Terminal.SetCheckBox("map/maprusher/hypertelerock", False)
                    Terminal.SetRadioButton("bot/mobvac/old", False)
                    Terminal.SetCheckBox("MonkeySpiritsNDcheck", True)
                    Terminal.SetCheckBox("Grenade Kami", True)
                    Terminal.Rush(610010001)
                time.sleep(1)