import DataType, time, Packet, GameState, Character

# v197.1
purchase = 0x04ED
recv = 0x066E

# Change to amount of red cubes the script should buy
AmountRedCubes = 0
# Change to amount of black cubes the script should buy
AmountBlackCubes = 0

# Don't touch below
AmountRedBought = 0
AmountBlackBought = 0

redcube = Packet.COutPacket(purchase)
redcube.Encode1(0x54)
redcube.Encode4(0x052F841E)
redcube.Encode4(0x044AA200)

blackcube = Packet.COutPacket(purchase)
blackcube.Encode1(0x54)
blackcube.Encode4(0x052F841F)
blackcube.Encode4(0x07DE2900)


if AmountRedCubes != 0:
    print("Beginning to purchase {0} red cubes...".format(AmountRedCubes))
if AmountBlackCubes != 0:
    print("Beginning to purchase {0} black cubes...".format(AmountBlackCubes))


while AmountRedBought < AmountRedCubes:
    if GameState.IsInCashShop():
        if Character.GetMeso() >= 72000000:
            Packet.SendPacket(redcube)
            Packet.WaitForRecv(recv, 1000)
            time.sleep(0.9)
            AmountRedBought += 6
            print("{0} red cubes purchased".format(AmountRedBought))
            if AmountRedBought >= AmountRedCubes:
                print("Cube purchase completed!")
        else:
            print("Not enough meso, exiting script...")
            break
    else:
        print("Not in Cash Shop, exiting script...")
        break


while AmountBlackBought < AmountBlackCubes:
    if GameState.IsInCashShop():
        if Character.GetMeso() >= 132000000:
            Packet.SendPacket(blackcube)
            Packet.WaitForRecv(recv, 1000)
            time.sleep(0.9)
            AmountBlackBought += 6
            print("{0} black cubes purchased".format(AmountBlackBought))
            if AmountBlackBought >= AmountBlackCubes:
                print("Cube purchase completed!")
        else:
            print("Not enough meso, exiting script...")
            break
    else:
        print("Not in Cash Shop, exiting script...")
        break