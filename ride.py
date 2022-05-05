"""
ID: xie_jj2
LANG: PYTHON3
TASK: ride
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
comet = fin.readline()
group = fin.readline()

s1 = 1
s2 = 1
for i in range (len(comet)):
	s1=s1*(ord(comet[i])-ord('A')+1)
for i in range (len(group)):
	s2=s2*(ord(group[i])-ord('A')+1)
#print("s1=",s1,"s2=",s2)
m1 = s1%47
m2 = s2%47
if(m1==m2):
	fout.write ( 'GO\n')
else:
	fout.write("STAY\n")
fout.close()
