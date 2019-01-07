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

while True:
	time.sleep(2)
	fieldid = Field.GetID()
	MPString = "Ruined City (Lv.160-169)"
	if fieldid != 100000000:
		if fieldid != 951000000:
			if fieldid != 954000001:
				if fieldid != 954000101:
					if fieldid != 954000201:
						if fieldid != 954000301:
							if fieldid != 954000401:
								if fieldid != 954000501:
									Terminal.Rush(100000000)
	if fieldid == 100000000:
		Character.Teleport(3133,334)
		Character.TalkToNpc(9071003)
	elif fieldid == 951000000:
                time.sleep(2)
		Character.Teleport(665,92)
		time.sleep(1)
		Character.EnterPortal()
		Npc.RegisterSelection(MPString)
	elif fieldid == 954000001:
                time.sleep(2)
		Character.Teleport(-2495,135)
		time.sleep(1)
		Character.EnterPortal()	
	elif fieldid == 954000101:
                time.sleep(2)
		Character.Teleport(-2031,136)
		time.sleep(1)
		Character.EnterPortal()
	elif fieldid == 954000201:
                time.sleep(2)
		Character.Teleport(1187,-597)
		time.sleep(1)
		Character.EnterPortal()
	elif fieldid == 954000301:
                time.sleep(2)
		Character.Teleport(-342,-597)
		time.sleep(1)
		Character.EnterPortal()
	elif fieldid == 954000401:
                time.sleep(2)
		Character.Teleport(913,-751)
		time.sleep(1)
		Character.EnterPortal()
	elif fieldid == 954000501:
		Character.Teleport(795,-751)
		time.sleep(4)
		Character.Teleport(-232,-940)
		time.sleep(2)
		Character.EnterPortal()
		time.sleep(5)
		
		
