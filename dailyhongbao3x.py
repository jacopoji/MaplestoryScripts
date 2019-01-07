import Inventory
import Character
import GameState
import time

items = [2023721] #1st 3exp, 2nd 3drop, 2450158
if GameState.IsInGame():
	for item in items:
		if Character.HasBuff(1, item) == False:
			Inventory.UseItem(item)
			time.sleep(1)
			
