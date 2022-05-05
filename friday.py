"""
ID: xie_jj2
LANG: PYTHON3
TASK: friday
"""

def daysBetween(year, month, day):
    yearIndex = 1900
    numLeapYears = 0;
    numDays =0
    while (yearIndex < year):
        if(yearIndex%100 ==0 and yearIndex% 400 ==0):
            #leap year
            numLeapYears += 1
        elif(yearIndex%100 !=0 and yearIndex%4 ==0):
            numLeapYears += 1
        yearIndex += 1
    numDays += (year - 1900)*365+ numLeapYears
    leapYear = False

    if(year%100 ==0 and year% 400 ==0):
        #leap year
        leapYear = True
    elif(year%100 !=0 and year%4 ==0):
        leapYear = True

    for i in range(1,month+1):
        if(i-1 in (1, 3, 5, 7, 8, 10, 12)):
            numDays += 31
        elif(i-1 in (4, 6, 9, 11)):
            numDays += 30
        elif(leapYear and i-1 ==2):
            numDays += 29
        elif(i-1==2):
            numDays += 28
    numDays += day

    return numDays


fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')
n = int(fin.readline())

monday = 1
year1 = 1900
yearN = year1+n
numLeapYears = 0
# how many leap years
weekDayOn13 = {1:0, 2:0, 3:0, 4:0,5:0,6:0,0:0}
for i in range(year1,yearN):
    for j in range(1, 13):
        j13 = daysBetween(i,j,13)%7
        #print(i, j,j13)
        weekDayOn13[j13] += 1

#print(n, weekDayOn13)
fout.write(str(weekDayOn13[6])+" "+str(weekDayOn13[0])+" "+
           str(weekDayOn13[1])+" "+str(weekDayOn13[2])+" "+
           str(weekDayOn13[3])+" "+str(weekDayOn13[4])+" "+
           str(weekDayOn13[5])+"\n")
fout.close()
