import re

with open ('flags.txt') as f:
     eachline = f.read()
     # print(eachline) # for debug, check if the output is the desired format

realflag = re.search("[A-Z]{5}[0-9]{5}[A-Z]{6}", eachline)
print(realflag)