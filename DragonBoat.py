import Character
import Context
import DataType
import Field
import Inventory
import Key
import Npc
import Packet
import Quest
import Terminal
import time

'''
item = Inventory.GetItem(1,3)
print("id",item.sn)
print("id in hex filled",hex(item.sn)[2:].zfill(16))
print('{:16x}'.format(item.sn))
'''
print(Terminal.GetProperty("Use item",2))
Terminal.SetPushButton("Use item",True)