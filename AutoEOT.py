import DataType
import Character
import Field
import Inventory
import Terminal
import time

Terminal.SetRushByLevel(False)
while True:
    if Character.GetLevel() >= 146:
        # Eye of Time
        if Character.IsOwnFamiliar(9960350) == False:
            # sleep 1 second every loop
            time.sleep(1)

            item = Inventory.FindItemByID(2870350)
            if item.valid:
                # use familiar
                Inventory.UseFamiliarCard(2870350)
                time.sleep(3)
            else:
                if Field.GetID() == 270010100:
                    # Time Lane: Memory Lane 1
                    # let bot kill mobs and pickup?
                    time.sleep(30)
                else:
                    # rush to the map
                    Terminal.Rush(270010100)

        else:
            break
    else:
        break
