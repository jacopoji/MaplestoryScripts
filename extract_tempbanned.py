#Made by Retard (https://www.gamekiller.net/members/retard.942916/)

from re import search
from datetime import datetime, date

now = datetime.now()

#Group 1 : ban year
#Group 2 : ban month
#Group 3 : ban day
#Group 4 : release year
#Group 5 : release month
#Group 6 : release day
regex = r"(\d+)\/(\d+)\/(\d+) \d+:\d+-(2018|2019)\/(\d+)\/(\d+)"
username_password = r";(.+@\w+.\w+;\w+)"

def days_between(date1, date2):
    return (date1 - date2).days

with open("banned.txt", "r") as banned:
    with open("tmpbanned.txt", "a+") as tmpbanned:
        content = banned.readlines()
        for line in content:
            matches = search(regex, line)
            if matches:
                ban_day = date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
                release_day = date(int(matches.group(4)), int(matches.group(5)), int(matches.group(6)))
                today = date(now.year, now.month, now.day)
                                    #2019/04/02   2019/04/16
                difference = days_between(today, release_day)
        
                if difference >= 0:
                    tmpbanned.write(str(search(username_password, line).group(1)) + "\r\n")