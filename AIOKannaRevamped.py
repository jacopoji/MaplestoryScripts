import Character
import sys
sys.path.append('C:/Users/Jacopo/Desktop/Scripts/dependencies')
import JOB_CONSTANTS,PACKET_HEADERS,EQUIP_SLOTS

def StatusChecker():
    '''Returns the current state of the character'''
    level = Character.GetLevel()
    job = Character.GetJob()

    first_job = (job == JOB_CONSTANTS.KannaJobs[0] and level < 13)
    second_job = (job == JOB_CONSTANTS.KannaJobs[0] and level >= 30)
    third_job = False #Automatic
    fourth_job = False #Automatic



    if first_job or second_job or third_job or fourth_job:
        return "JobAdv"
    else if