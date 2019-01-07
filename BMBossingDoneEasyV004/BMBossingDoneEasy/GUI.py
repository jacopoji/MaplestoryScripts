from tkinter import *
import os
class Checkbar(Frame):
	def __init__(self,parent=None, bosses=[]):
		Frame.__init__(self, parent)
		self.bossvars = []
		self.diffvars = []
		self.standAlonevars = []
		self.kamivars = []
		self.hypertelevars = []
		
		headerframe = Frame(self, bd=6)
		headerframe.pack(side=TOP, fill=BOTH)
		headerlabel = Label(headerframe, text="BM BossingDoneEasy GUI", bg="Pink")
		headerlabel.pack(side=TOP, fill=BOTH)
		
		#Settings Frame
		kamivar = IntVar()
		hypertelevar = IntVar()
		settingsFrame = Frame(self, bd=6)
		settingsFrame.pack(side=TOP, fill=BOTH)
		Settings = Label(settingsFrame, text="Character Settings", bg="Pink")
		Settings.pack(side=TOP, fill=BOTH)
		kamiVac = Checkbutton(settingsFrame, text="Kami Vac", bg="Pink", compound='top', variable=kamivar)
		kamiVac.pack(side=LEFT)
		hyperTeleportRock = Checkbutton(settingsFrame, text="Hyper Teleport Rock", bg="Pink", variable=hypertelevar)
		hyperTeleportRock.pack(side=RIGHT)
		self.kamivars.append(kamivar)
		self.hypertelevars.append(hypertelevar)
		
		x = 0
		bossframe = Frame(self, bd=6)
		bossframe.pack(side=LEFT, anchor=W)
		diffFrame = Frame(self, bd=6)
		diffFrame.pack(side=TOP)
		EasyBosses = ["Zakum", "Horntail", "Magnus", "Gollux"]
		NormalBosses = ["Zakum", "Horntail","Hilla", "Magnus", "Crimson Queen", "Pierre", "Von Bon", "Vellum", "Gollux"]
		HardBosses = ["Hilla", "Magnus", "Gollux"]
		ChaosBosses = ["Horntail", "Crimson Queen", "Pierre", "Von Bon", "Vellum", "Gollux"]
		StandAloneChaos = ["Zakum"]
		for boss in bosses:
			bossvar = BooleanVar()
			
			bossbutton = Checkbutton(bossframe, text=boss, variable=bossvar, activebackground="Grey", bd=6)
			bossbutton.grid(row=x, column=0, sticky=W)
			
			diffvar = IntVar()
			if boss in EasyBosses:
				diffRadio = Radiobutton(diffFrame, text='Easy', variable=diffvar, value=1, bg="Green",bd=6)
				diffRadio.grid(row=x, column=0)
			if boss in NormalBosses:
				diffRadio1 = Radiobutton(diffFrame, text='Normal', variable=diffvar, value=2, bg="Yellow",bd=6)
				diffRadio1.grid(row=x, column=1)
			if boss in HardBosses:
				diffRadio2 = Radiobutton(diffFrame, text='Hard', variable=diffvar, value=3, bg="Orange",bd=6)
				diffRadio2.grid(row=x, column=2)
			if boss in ChaosBosses:
				diffRadio3 = Radiobutton(diffFrame, text='Chaos', variable=diffvar, value=4, bg="Red",bd=6)
				diffRadio3.grid(row=x, column=3)
			if boss in StandAloneChaos:
				standAlonevar = IntVar()
				ChaosStandalone = Checkbutton(diffFrame, text='Chaos', variable=standAlonevar,bg="Red", activebackground="Grey", bd=6)
				ChaosStandalone.grid(row=x, column=3)
				self.standAlonevars.append(standAlonevar)
			self.bossvars.append(bossvar)
			self.diffvars.append(diffvar)
			x+=1
	def statebossvar(self):
		return map((lambda bossvar: bossvar.get()), self.bossvars)
	def statediffvar(self):
		return map((lambda diffvar: diffvar.get()), self.diffvars)
	def statestandAlonevar(self):
		return map((lambda standAlonevar: standAlonevar.get()), self.standAlonevars)
	def stateKamivar(self):
		return map((lambda kamivar: kamivar.get()), self.kamivars)
	def stateHypertelevar(self):
		return map((lambda hypertelevar: hypertelevar.get()), self.hypertelevars)
root = Tk()
root.title("BoldMold's Bossing Done Easy")
bossbtn = Checkbar(root, bosses=['Zakum','Hilla','Horntail','Magnus', 'Crimson Queen', 'Pierre','Von Bon', 'Vellum', 'Gollux'])
bossbtn.pack()


#DropDown To change Script
profilevar = StringVar()
profile = profilevar.get()
def change_dropdown(*args):
	profile = profilevar.get()
	print(profile)
listofprofiles = os.listdir("BossingConfigs")
print(listofprofiles)
profilevar = StringVar()
OptionMenu(root, profilevar, *listofprofiles).pack(side=RIGHT)
profilevar.trace('w', change_dropdown)
profilevar.set("Click To Choose Profile")

def allstates():
	print(list(bossbtn.statebossvar()))
	print(list(bossbtn.statediffvar()))
	print(list(bossbtn.statestandAlonevar()))
	print(list(bossbtn.stateKamivar()))
	print(list(bossbtn.stateHypertelevar()))
	kamiVac = list(bossbtn.stateKamivar())
	hypertelerock = list(bossbtn.stateHypertelevar())
	Weeklybosses = list(bossbtn.statestandAlonevar())
	difficulty = list(bossbtn.statediffvar())
	dobosses = list(bossbtn.statebossvar())
	ZakumDiff = difficulty[0]
	HillaDiff = difficulty[1]
	HorntailDiff = difficulty[2]
	MagnusDiff = difficulty[3]
	CrimsonQueenDiff = difficulty[4]
	PierreDiff = difficulty[5]
	VonBonDiff = difficulty[6]
	VellumDiff = difficulty[7]
	GolluxDiff = difficulty[8]
	profile = profilevar.get()
	if kamiVac[0]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[31] = "usingkami		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Using KamiVac")
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[31] = "usingkami		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
	if hypertelerock[0]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[25] = "usingHyperTeleportRock = True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Using Hyper Teleport Rock")
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[25] = "usingHyperTeleportRock = False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
			
	if dobosses[0]: 
		print("Kill Zakum, True",)
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[34] = "DoZakumDaily	=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		if ZakumDiff ==0:
			print("You have not checked what diff you want for Zakum")
		if ZakumDiff ==1:
			print("Zakum Diff, Easy")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[46] = "ZakumEasy		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[46] = "ZakumEasy		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if ZakumDiff ==2:
			print("Zakum Diff, Normal")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[47] = "ZakumNormal		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[47] = "ZakumNormal		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[34] = "DoZakumDaily	=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
	if Weeklybosses[0]:
		print("Kill Zakum Chaos (Weekly)")
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[48] = "ZakumChaos		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[48] = "ZakumChaos		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
			
			
	if dobosses[1]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[35] = "DoHilla			=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Hilla, True")
		if HillaDiff ==0:
			print("You have not checked what diff you want for Hilla")
		if HillaDiff ==2:
			print("Hilla Diff, Normal")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[50] = "HillaNormal		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[50] = "HillaNormal		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if HillaDiff ==3:
			print("Hilla Diff, Hard")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[51] = "HillaHard		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[51] = "HillaHard		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[35] = "DoHilla			=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
			
			
	if dobosses[2]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[36] = "DoHorntail		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Horntail, True")
		if HorntailDiff ==0:
			print("You have not checked what diff you want for Horntail")
		if HorntailDiff ==1:
			print("Horntail Diff, Easy")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[53] = "HorntailEasy	=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[53] = "HorntailEasy	=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if HorntailDiff ==2:
			print("Horntail Diff, Normal")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[54] = "HorntailNormal	=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[54] = "HorntailNormal	=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if HorntailDiff ==4:
			print("Horntail Diff, Chaos")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[55] = "HorntailChaos	=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[55] = "HorntailChaos	=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[36] = "DoHorntail		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
			
			
	if dobosses[3]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[37] = "DoMagnus		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Magnus, True")
		if MagnusDiff ==0:
			print("You have not checked what diff you want for Magnus")
		if MagnusDiff ==1:
			print("Magnus Diff, Easy")
		if MagnusDiff ==2:
			print("Magnus Diff, Normal")
		if MagnusDiff ==3:
			print("Magnus Diff, Hard")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[59] = "MagnusHard		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[59] = "MagnusHard		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[37] = "DoMagnus		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)

	if dobosses[4]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[39] = "DoCrimsonQueen	=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Crimson Queen, True")
		if CrimsonQueenDiff ==0:
			print("You have not checked what diff you want for Crimson Queen")
		if CrimsonQueenDiff ==2:
			print("Crimson Queen Diff, Normal")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[64] = "CrimsonQueenNormal	=	True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[64] = "CrimsonQueenNormal	=	False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if CrimsonQueenDiff ==4:
			print("Crimson Queen Diff, Chaos")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[65] = "CrimsonQueenChaos	=	True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[65] = "CrimsonQueenChaos	=	False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[39] = "DoCrimsonQueen	=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
			
	if dobosses[5]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[40] = "DoPierre		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Pierre, True")
		if PierreDiff ==0:
			print("You have not checked what diff you want for Pierre")
		if PierreDiff ==2:
			print("Pierre Diff, Normal")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[67] = "PierreNormal	=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[67] = "PierreNormal	=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if PierreDiff ==4:
			print("Pierre Diff, Chaos")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[68] = "PierreChaos		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[68] = "PierreChaos		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[40] = "DoPierre		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)

	if dobosses[6]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[41] = "DoVonBon		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Von Bon, True")
		if VonBonDiff ==0:
			print("You have not checked what diff you want for Von Bon")
		if VonBonDiff ==2:
			print("Von Bon Diff, Normal")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[70] = "VonBonNormal	=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[70] = "VonBonNormal	=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if VonBonDiff ==4:
			print("Von Bon Diff, Chaos")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[71] = "VonBonChaos		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[71] = "VonBonChaos		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[41] = "DoVonBon		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
			
	if dobosses[7]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[42] = "DoVellum		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Vellum, True")
		if VellumDiff ==0:
			print("You have not checked what diff you want for Vellum")
		if VellumDiff ==2:
			print("Vellum Diff, Normal")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[73] = "VellumNormal	=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[73] = "VellumNormal	=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if VellumDiff ==4:
			print("Vellum Diff, Chaos")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[74] = "VellumChaos		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[74] = "VellumChaos		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[42] = "DoVellum		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
			
	if dobosses[8]:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[43] = "DoGollux		=		True\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)
		print("Kill Gollux, True")
		if GolluxDiff ==0:
			print("You have not checked what diff you want for Gollux")
		if GolluxDiff ==1:
			print("Gollux Kill 2 Shoulders")
		if GolluxDiff ==2:
			print("Gollux Kill 1 Shoulder")
		if GolluxDiff ==3:
			print("Gollux Kill to head")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[78] = "GolluxHard		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[78] = "GolluxHard		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		if GolluxDiff ==4:
			print("Gollux Diff, Chaos. Straight to Head / Need Head Teleport")
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[79] = "GolluxChaos		=		True\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
		else:
			with open('BM BossingDoneEasyV004.py', 'r') as rf:
				lines = rf.readlines(100000)
			lines[79] = "GolluxChaos		=		False\n"
			with open('BM BossingDoneEasyV004.py', 'w') as wf:
				wf.writelines(lines)
			with open('BossingConfigs\\'+profile, 'w') as wf:
				wf.writelines(lines)
	else:
		with open('BM BossingDoneEasyV004.py', 'r') as rf:
			lines = rf.readlines(100000)
		lines[43] = "DoGollux		=		False\n"
		with open('BM BossingDoneEasyV004.py', 'w') as wf:
			wf.writelines(lines)
		with open('BossingConfigs\\'+profile, 'w') as wf:
			wf.writelines(lines)

Button(root, text='Update Script', command=allstates, bg="White").pack(side=RIGHT)

statuslabel = Label(root, text="Status bar",bd=1, relief=SUNKEN, anchor=W)
statuslabel.pack(side=BOTTOM, fill=X)
root.mainloop()
