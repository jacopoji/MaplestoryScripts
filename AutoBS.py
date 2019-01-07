import DataType
import Character
import Field
import Inventory
import Terminal
import time

Terminal.SetRushByLevel(False)
while True:
    if Character.GetLevel() >= 83:
        # Eye of Time
        if Character.IsOwnFamiliar(9960295) == False:
            Terminal.SetCheckBox("timedCCCheck",False)
            # sleep 1 second every loop
            time.sleep(1)

            item = Inventory.FindItemByID(2870295)
            if item.valid:
                # use familiar
                Inventory.UseFamiliarCard(2870295)
                time.sleep(3)
                Terminal.SetCheckBox("timedCCCheck",True)
            else:
                if Field.GetID() == 310050600:
                    # Time Lane: Memory Lane 1
                    # let bot kill mobs and pickup?
                    time.sleep(30)
                else:
                    # rush to the map
                    Terminal.Rush(310050600)

        else:
            break
    else:
        break
