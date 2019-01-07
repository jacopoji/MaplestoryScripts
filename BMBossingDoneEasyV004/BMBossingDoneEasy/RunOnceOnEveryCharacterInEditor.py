import os, Character, GameState
if GameState.IsInGame():
	charID = Character.GetID()
	charName = Character.GetName()
	with open('BMBossingDoneEasy\\BM BossingDoneEasyV004.py', 'r') as rf:
		lines = rf.readlines(70000)
	with open('BMBossingDoneEasy\\BossingConfigs\\'+str(charName)+' '+str(charID)+'.py', 'w') as wf:
		wf.writelines(lines)
