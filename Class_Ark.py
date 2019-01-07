import os, sys, Character, GameState, Field, DataType, time, Npc, Packet, Terminal, Context, Inventory, Key, Quest
#ark prequests

#PLEASE HAVE FOLLOWING OPTIONS ENABLED
# AUTO NPC
# GFMA
# SI 155001100 (NO DELAY + DELAY 250)
# PET ITEM Teleport




def ToPortal(portal, enter=True):
    portal = Field.FindPortal(portal)
    if portal.valid:
        if not (Character.GetPos().x < portal.x+5 and Character.GetPos().x > portal.x-5):
            Character.Teleport(portal.x, portal.y-5)
            time.sleep(1)
            if enter:
                Character.EnterPortal()
                time.sleep(1)
        elif enter:
            time.sleep(1)
            Character.EnterPortal()
            
def Teleport(x, y):
    if not (Character.GetPos().x < x+5 and Character.GetPos().x > x-5):
        Character.Teleport(x, y-5)
        
def ToNPC(npc):
    npc = Field.FindNpc(npc)
    if npc.valid:
        if not (Character.GetPos().x < npc.x+5 and Character.GetPos().x > npc.x-5):
            Character.Teleport(npc.x, npc.y-10)
    time.sleep(1)

def ToDirection(direction, distance=100):
    pos = Character.GetPos()
    if direction=="right":
        Character.Teleport(pos.x+distance, pos.y)
    elif direction=="left":
        Character.Teleport(pos.x-distance, pos.y)
    elif direction=="up":
        Character.Teleport(pos.x, pos.y+distance)
    elif direction=="down":
        Character.Teleport(pos.x, pos.y-distance)

def Rush(mapid):
    if Terminal.IsRushing():
        time.sleep(1)
    elif Field.GetID() != mapid:
        time.sleep(1)
        Terminal.Rush(mapid)
        
def DoQuest(id):
	if Quest.GetQuestState(id) != 2:
		print("havn't finished quest "+str(id)+" yet")
		return True
	else:
		return False
	
def NeedQuest(id):
	if Quest.GetQuestState(id) == 0:
		return True
	else:
		return False

def HasQuest(id):
	if Quest.GetQuestState(id) == 1:
		return True
	else:
		return False

def InProgress(id, npc):
	if Quest.CheckCompleteDemand(id, npc) == 1:
		print("Currently doing quest "+str(id))
		return True
	else:
		return False

def StartQuest(id, npc):
	print("Getting quest "+str(id))
	Quest.StartQuest(id, npc)
	time.sleep(2)
	
def CompleteQuest(id, npc):
	print("Completing quest "+str(id))
	Quest.CompleteQuest(id, npc)
	time.sleep(2)

def Getmap():
    return Field.GetID()


if GameState.IsInGame():
    #advance quest
    if DoQuest(34901):
        if NeedQuest(34901):
            StartQuest(34901, 0)
    elif Character.GetLevel() >= 30 and DoQuest(34902):
        StartQuest(34902, 0)
    elif Character.GetLevel() >= 60 and DoQuest(34903):
        if NeedQuest(34903):
            StartQuest(34903, 0)
        elif HasQuest(34903):
            CompleteQuest(34903, 0)
    elif Character.GetLevel() >= 100 and DoQuest(34904):
        if NeedQuest(34904):
            StartQuest(34904, 0)
        elif HasQuest(34904):
            CompleteQuest(34904, 0)
        
            
    #Tutorial questline
    if DoQuest(34940):
        Terminal.SetCheckBox("filter_equip", True)
        Terminal.SetCheckBox("filter_etc", False)
        Terminal.SetCheckBox("Rush By Level", False)
        if DoQuest(34915):
            if NeedQuest(34915):
                StartQuest(34915, 3001406)
        
        elif DoQuest(34916):
            if NeedQuest(34916):
                StartQuest(34916, 3001400)
            elif HasQuest(34916):
                CompleteQuest(34916, 3001400)
                
        elif DoQuest(34917):
            if NeedQuest(34917):
                ToNPC(3001400)
                StartQuest(34917, 3001400)
            elif HasQuest(34917):
                if InProgress(34917, 3001400):
                    Rush(402000610)
                else:
                    Rush(402000600)
                    ToNPC(3001400)
                    CompleteQuest(34917, 3001400)
        
        elif DoQuest(34918):
            if NeedQuest(34918):
                ToNPC(3001400)
                StartQuest(34918, 3001400)
            elif HasQuest(34918):
                ToNPC(3001401)
                CompleteQuest(34918, 3001401)
        
        
        elif DoQuest(34919):
            if NeedQuest(34919):
                ToNPC(3001401)
                StartQuest(34919,3001401)
            elif HasQuest(34919):
                if InProgress(34919, 3001401):
                    Rush(402000611)
                else:
                    Rush(402000600)
                    ToNPC(3001401)
                    CompleteQuest(34919, 3001401)
        
        
        elif DoQuest(34920):
            if NeedQuest(34920):
                ToNPC(3001401)
                StartQuest(34920, 3001401)
            elif HasQuest(34920):
                ToNPC(3001400)
                CompleteQuest(34920, 3001402)
                
        elif DoQuest(34921):
            if NeedQuest(34921):
                ToNPC(3001400)
                StartQuest(34921, 3001402)
            elif HasQuest(34921):
                if InProgress(34921, 3001402):
                    Rush(402000612)
                else:
                    Rush(402000600)
                    ToNPC(3001400)
                    CompleteQuest(34921, 3001402)
        
        elif DoQuest(34922):
            if NeedQuest(34922):
                ToNPC(3001400)
                StartQuest(34922, 3001402)
            elif HasQuest(34922):
                ToNPC(3001403)
                CompleteQuest(34922, 3001403)
                
        elif DoQuest(34923):
            if NeedQuest(34923):
                Rush(402000613)
                StartQuest(34923, 3001404)
            elif HasQuest(34923):
                if InProgress(34923, 3001404):
                    time.sleep(2)
                else:
                    ToNPC(3001404)
                    CompleteQuest(34923, 3001404)
        
        elif DoQuest(34924):
            if NeedQuest(34924):
                Rush(402000600)
                StartQuest(34924, 3001400)
            elif HasQuest(34924):
                Rush(402000614)
                CompleteQuest(34924, 3001405)
                
        elif DoQuest(34925):
            if NeedQuest(34925):
                StartQuest(34925, 3001405)
            elif HasQuest(34925):
                CompleteQuest(34925, 3001400)
                
        elif DoQuest(34926):
            if NeedQuest(34926):
                ToNPC(3001400)
                StartQuest(34926, 3001402)
            elif HasQuest(34926):
                if InProgress(34926, 3001402):
                    Rush(402000616)
                else:
                    Rush(402000600)
                    ToNPC(3001400)
                    CompleteQuest(34926, 3001402)
                
                
        elif DoQuest(34927):
            if NeedQuest(34927):
                ToNPC(3001401)
                StartQuest(34927, 3001401)
            elif HasQuest(34927):
                if InProgress(34927, 3001401):
                    Rush(402000618)
                else:
                    Rush(402000600)
                    ToNPC(3001401)
                    CompleteQuest(34927, 3001401)
                    
        elif DoQuest(34928):
            if NeedQuest(34928):
                ToNPC(3001400)
                StartQuest(34928, 3001400)
            elif HasQuest(34928):
                Rush(402000615)
                CompleteQuest(34928, 3001407)
        
        elif DoQuest(34929):
            if NeedQuest(34929):
                Rush(402000600)
                ToNPC(3001400)
                StartQuest(34929, 3001400)
            elif HasQuest(34929):
                Rush(402000620)
                CompleteQuest(34929, 3001408)
                
        elif DoQuest(34930):
            if NeedQuest(34930):
                Rush(402000621)
                ToNPC(3001409)
                StartQuest(34930, 3001409)
            elif HasQuest(34930):
                if InProgress(34930, 3001409):
                    time.sleep(2)
                else:
                    ToNPC(3001409)
                    CompleteQuest(34930, 3001409)
                
        elif DoQuest(34931):
            if NeedQuest(34931):
                #Rush(402000621)
                ToNPC(3001410)
                StartQuest(34931, 3001410)
            elif HasQuest(34931):
                if InProgress(34931, 3001410):
                    Rush(402000622)
                    time.sleep(2)
                else:
                    ToNPC(3001410)
                    CompleteQuest(34931, 3001410)
        
        elif DoQuest(34932):
            if NeedQuest(34932):
                Rush(402000630)
                StartQuest(34932, 3001411)
            elif HasQuest(34932):
                Rush(402000631)
                CompleteQuest(34932, 3001412)
        
        elif DoQuest(34933):
            if NeedQuest(34933):
                Rush(402000631)
                ToNPC(3001412)
                StartQuest(34933, 3001412)
            elif HasQuest(34933):
                if InProgress(34933, 3001412):
                    time.sleep(2)
                else:
                    ToNPC(3001412)
                    CompleteQuest(34933, 3001412)
        
        elif DoQuest(34934):
            if NeedQuest(34934):
                Rush(402000633)
                StartQuest(34934, 3001413)
            elif HasQuest(34934):
                if InProgress(34934, 3001413):
                    time.sleep(2)
                else:
                    ToNPC(3001413)
                    CompleteQuest(34934, 3001413)
                    #Dialog
        
        elif DoQuest(34935):
            if NeedQuest(34935):
                Rush(402000635)
                StartQuest(34935, 3001414)
            elif HasQuest(34935):
                if Getmap()==402000648:
                    CompleteQuest(34935, 3001416)
                    #spam space
        elif DoQuest(34936):
            if NeedQuest(34936):
                if Getmap()==402000648:
                    StartQuest(34936, 3001415)
            if Getmap()==402090006:
                for i in range(22):
                    Key.Down(0x20)
                    time.sleep(0.1)
                    Key.Up(0x20)
        
        elif DoQuest(34937):
            if NeedQuest(34937):
                if Getmap()==402000644:
                    StartQuest(34937, 3001417)
            elif HasQuest(34937):
                CompleteQuest(34937, 3001417)
        
        elif DoQuest(34938):
            if Getmap()==402000644:
                StartQuest(34938, 3001423)
            elif Getmap()==940205100 and Field.GetMobCount()==1:
                ToPortal("next00")
            elif Getmap()==940205200 and Field.GetMobCount()==1:
                ToPortal("next00")
            elif Getmap()==940205300 and Field.GetMobCount()==1:
                ToPortal("next00")
                
        elif DoQuest(34939):
            StartQuest(34939, 0)
        
        elif DoQuest(34940):
            if Getmap()==402000640:
                StartQuest(34940, 0)
            elif Getmap()==940205400 and Field.GetMobCount()==1:
                ToPortal("next00")
            elif Getmap()==940205500 and Field.GetMobCount()==1:
                ToPortal("next00")
            elif Getmap()==940205600 and Field.GetMobCount()==1:
                ToPortal("next00")
    
    #Get jr boogie familiar
    elif not Character.IsOwnFamiliar(9960098):
        Terminal.SetCheckBox("Rush By Level", False)
        Rush(102010000)
        Terminal.SetCheckBox("filter_familiar", False)
        if Inventory.FindItemByID(2870098).valid:
            Inventory.UseFamiliarCard(2870098)
            time.sleep(5)
            Terminal.Rush(100000000)
            timer=0
            while Terminal.IsRushing() and timer < 60:
                time.sleep(1)
                timer += 1
            Terminal.SetCheckBox("Rush By Level", True)
            Terminal.SetCheckBox("filter_familiar", True)
            Terminal.SetCheckBox("filter_etc", True)
            