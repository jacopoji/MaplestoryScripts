import time
import Key
import Character
import GameState

# https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
keyBind = 0x44
Key.Set(keyBind, 1, 42111003)
currentMP = Character.GetMP()

if GameState.IsInGame() and currentMP >= 99:
    for i in range(3):
        Key.Press(keyBind)
        time.sleep(1)