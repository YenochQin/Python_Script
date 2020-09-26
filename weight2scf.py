import os
import sys
path = sys.path[0]
print(path)
# Get file name 
name = input("The file name:")

# Open files
csffile = open(f"{path}/{name}.c",'r')
weightfile = open(f"{path}/{name}.l",'r')

weights = weightfile.readlines()
# print(weights)

# The information of the atom
title = weights[0]
ncfg = int(title[-8:-1])
ncfg
eterm = weights[5]
finalterm = eterm[-3:-1]

rawweights = weights[6:]
# len(rawweights)
# rawweights[0]


# Get weight
wt = []
# for cfg in range(ncfg):
cfg = 0
WT = 0
for row in range(0,len(rawweights)):
        # print(i)
        rwt = rawweights[row]
        for i in range(0,len(rwt),11):
            if i <= len(rwt) - 11:
                # print(i)
                # print(rwt[i:i+11])
                wt.append(rwt[i:i+11])
                cfg+=1
            
                # print(cfg)

for ww in range(len(wt)):
    WT += float(wt[ww]) ** 2

print(WT)
# Get configurations
csf = csffile.readlines()
# csf[0] = '\n'
# csf.insert(1,'\n')

# Put the filal data in data.c
datafile = open(f'{name}.c','w')

num = 0
for line in range(len(csf)):
    if finalterm in csf[line]:
        blank = int(65 - len(csf[line])) * " "
        # print(len(csf[line]))
        term = csf[line]
        csf[line] = term[:-1] + blank + wt[num] + "\n"
        num += 1
    # print(a[line])
    datafile.write(str(csf[line]))

datafile.close()
