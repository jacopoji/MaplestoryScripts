import Inventory
import sys,os
sys.path.append('C:/Users/Jacopo/Desktop/Scripts/dependencies')
import EQUIP_SLOTS,EQUIP_ID
def GetTotalStar():
    total_star = 0
    for x in range(-100, 0):
        item = Inventory.GetItem(1,x)
        total_star += item.currentStar
    return total_star


def FarmedEnoughAccessories():
    eye = 0
    face = 0
    earring = 0
    necklace = 0
    ring = 0
    items = Inventory.GetItems(1)
    for item in items:
        if item.id in EQUIP_ID.necklace_list and item.grade > 0:
            necklace = 1
        elif item.id in EQUIP_ID.ring_list and item.grade > 0:
            ring += 1
        elif item.id in EQUIP_ID.eye_list and item.grade > 0:
            eye = 1
        elif item.id in EQUIP_ID.face_list and item.grade > 0:
            face = 1
        elif item.id in EQUIP_ID.earring_list and item.grade > 0:
            earring = 1

    if Inventory.GetItem(1,EQUIP_SLOTS.necklace_slot).id in EQUIP_ID.necklace_list and item.grade > 0:
        necklace = 1
    elif Inventory.GetItem(1,EQUIP_SLOTS.eye_slot).id in EQUIP_ID.eye_list and item.grade > 0:
        eye = 1
    elif Inventory.GetItem(1,EQUIP_SLOTS.face_slot).id in EQUIP_ID.face_list and item.grade > 0:
        face = 1
    elif Inventory.GetItem(1,EQUIP_SLOTS.earring_slot).id in EQUIP_ID.earring_list and item.grade > 0:
        earring = 1
    
    for ring_slot in EQUIP_SLOTS.ring_slots:
        if Inventory.GetItem(1,ring_slot).id in EQUIP_ID.ring_list and item.grade > 0:
            ring += 1
    return (eye + face + earring + necklace + ring) >= 5

def ToggleRushByLevel(indicator):
	Terminal.SetCheckBox("Rush By Level",indicator)
	Terminal.SetRushByLevel(indicator)