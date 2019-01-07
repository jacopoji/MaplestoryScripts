import time
import Key
import Character
import GameState
import Terminal
# https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
#keyBind = 0x44
#Key.Set(keyBind, 1, 42111003)
currentMP = Character.GetMP()

if GameState.IsInGame() and currentMP >= 99:
    Terminal.SetCheckBox('Auto Attack', 1)
elif GameState.IsInGame() and currentMP <= 40:
    Terminal.SetCheckBox('Auto Attack', 0)