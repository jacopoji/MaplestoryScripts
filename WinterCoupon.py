import Inventory
import Character
import GameState
import time

items = [2023124, 2023122, 2023118] #1st lucky, 2nd enjoyable, 3rd cold
if GameState.IsInGame():
	for item in items:
		if Character.HasBuff(1, item) == False:
			Inventory.UseItem(item)
			time.sleep(1)
			
