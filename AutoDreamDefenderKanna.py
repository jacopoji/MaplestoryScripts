import Character
import Character
import DataType
import Field
import Terminal
import time
import GameState

ptgo_up = Field.FindPortal('ptgo_up')
ptgo_down = Field.FindPortal('ptgo_down')
ptgo_left = Field.FindPortal('ptgo_left')
ptgo_right = Field.FindPortal('ptgo_right')
ptback_up = Field.FindPortal('ptback_up')
ptback_down = Field.FindPortal('ptback_down')
ptback_left = Field.FindPortal('ptback_left')
ptback_right = Field.FindPortal('ptback_right')

NIGHTMARE_BOX = [9833080, 9833081, 9833082, 9833083, 9833084, 9833085]
DD_MAP = [921171000, 921171001, 921171002, 921171003, 921171004, 921171005]

SLEEP_TIME = 0.5


def toggle_attack(flag):
    # If you really would like to use SI with this script, change code here to
    # Terminal.SetCheckBox("Skill Injection", flag)
    # Disclaimer: I never tested SI in DD. Use on your own risk.
    Terminal.SetCheckBox("MonkeySpiritsNDcheck", flag)


def is_in_center(x, y):
    return x >= ptgo_left.x - 50 and x <= ptgo_right.x + 50 and y >= ptgo_up.y - 50 and y <= ptgo_down.y + 50


def is_in_left(x, y):
    return x >= ptback_left.x - 450 and x <= ptback_left.x + 450 and y >= ptback_left.y - 250 and y <= ptback_left.y + 250


def is_in_right(x, y):
    return x >= ptback_right.x - 450 and x <= ptback_right.x + 450 and y >= ptback_right.y - 250 and y <= ptback_right.y + 250


def is_in_up(x, y):
    return x >= ptback_up.x - 450 and x <= ptback_up.x + 450 and y >= ptback_up.y - 250 and y <= ptback_up.y + 250


def is_in_down(x, y):
    return x >= ptback_down.x - 450 and x <= ptback_down.x + 450 and y >= ptback_down.y - 250 and y <= ptback_down.y + 250


def room_of(x, y):
    if is_in_center(x, y):
        return 'center'
    elif is_in_up(x, y):
        return 'up'
    elif is_in_down(x, y):
        return 'down'
    elif is_in_left(x, y):
        return 'left'
    elif is_in_right(x, y):
        return 'right'
    else:
        return None


def find_one_box():
    for box_id in NIGHTMARE_BOX:
        mob = Field.FindMob(box_id)
        if mob.valid:
            return mob
    return None


def close_enough(x1, y1, x2, y2, distance):
    if (x1 - x2)**2 + (y1 - y2)**2 < distance**2:
        return True
    else:
        return False


def safe_teleport(x, y):
    toggle_attack(False)
    pos = Character.GetPos()
    if not close_enough(pos.x, pos.y, x, y, 1000):
        print('TOO FAR. NOT SAFE TO TELEPORT!!!')
        return
    Character.Teleport(x, y - 5)
    time.sleep(SLEEP_TIME)


def safe_enter_portal():
    start = Character.GetPos()
    Character.EnterPortal()
    time.sleep(SLEEP_TIME)
    end = Character.GetPos()
    if close_enough(start.x, start.y, end.x, end.y, 10):
        Character.EnterPortal()


def moving_to_room(from_room, to_room):
    if from_room is None or to_room is None or from_room == to_room:
        return

    print('Moving from %s to %s.' % (from_room, to_room))
    if from_room == 'center':
        if to_room == 'up' and ptgo_up.valid:
            safe_teleport(ptgo_up.x, ptgo_up.y)
        elif to_room == 'down' and ptgo_down.valid:
            safe_teleport(ptgo_down.x, ptgo_down.y)
        elif to_room == 'left' and ptgo_left.valid:
            safe_teleport(ptgo_left.x, ptgo_left.y)
        elif to_room == 'right' and ptgo_right.valid:
            safe_teleport(ptgo_right.x, ptgo_right.y)
        safe_enter_portal()
    elif to_room == 'center':
        if from_room == 'up' and ptback_up.valid:
            safe_teleport(ptback_up.x, ptback_up.y)
        elif from_room == 'down' and ptback_down.valid:
            safe_teleport(ptback_down.x, ptback_down.y)
        elif from_room == 'left' and ptback_left.valid:
            safe_teleport(ptback_left.x, ptback_left.y)
        elif from_room == 'right' and ptback_right.valid:
            safe_teleport(ptback_right.x, ptback_right.y)
        safe_enter_portal()
    else:
        moving_to_room(from_room, 'center')


if GameState.IsInGame() and Field.GetID() in DD_MAP:
    box = find_one_box()
    if box is None:
        print('Can not find any nightmare box. Wait.')
        toggle_attack(False)
        time.sleep(SLEEP_TIME)
    else:
        room_of_box = room_of(box.x, box.y)
        print('Found box in room: %s' % room_of_box)

        pos = Character.GetPos()
        room_of_char = room_of(pos.x, pos.y)
        print('The character is in room: %s' % room_of_char)

        if room_of_box == room_of_char:
            if close_enough(pos.x, pos.y, box.x, box.y, 50):
                print('Close enough. Toggle AA. Wait.')
                toggle_attack(True)
                time.sleep(SLEEP_TIME)
            else:
                print('Not close enough. Teleport to box.')
                safe_teleport(box.x, box.y)
        else:
            moving_to_room(room_of_char, room_of_box)
else:
    print('Not in game or not in DD map.')
    time.sleep(SLEEP_TIME)