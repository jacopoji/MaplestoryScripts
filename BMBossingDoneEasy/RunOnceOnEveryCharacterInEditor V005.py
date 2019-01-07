import os, Character, GameState
if GameState.IsInGame():
	charID = Character.GetID()
	charName = Character.GetName()
	with open('BMBossingDoneEasy\\BM BossingDoneEasyV005.py', 'r') as rf:
		lines = rf.readlines()
	with open('BMBossingDoneEasy\\BossingConfigs\\'+str(charName)+' '+str(charID)+'.py', 'w') as wf:
		wf.writelines(lines)
