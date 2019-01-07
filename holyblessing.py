import GameState
import Terminal
import time

if GameState.IsInGame():
	print("In Game, waiting 5seconds...")
	time.sleep(3)
	Terminal.EnterCashShop()
if GameState.IsInCashShop():
	print("Entered CashShop, waiting 100seconds...")
	time.sleep(200)
	Terminal.LeaveCashShop()
else:
	print("Not in Game, waiting 5sec...")
	time.sleep(3)
