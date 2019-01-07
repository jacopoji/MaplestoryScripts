import DataType
import Character
import Field
import Inventory
import Terminal
import time

Terminal.SetRushByLevel(False)

def loot_settings(bool_settings):
    Terminal.SetCheckBox("Auto Loot",bool_settings)
    Terminal.SetCheckBox("Kami Loot",bool_settings)

if Character.GetLevel() >= 13:
    # Jr. Boogie
    while Character.IsOwnFamiliar(9960098) == False:
        # sleep 1 second every loop
        time.sleep(1)

        item = Inventory.FindItemByID(2870098)
        if item.valid:
            # use familiar
            Inventory.UseFamiliarCard(2870098)
            loot_settings(False)
            time.sleep(3)
        else:
            if Field.GetID() == 102010000:
                # Perion Southern Ridge
                # let bot kill mobs and pickup?
                loot_settings(True)
                time.sleep(1)
            else:
                # rush to the map
                Terminal.Rush(102010000)
