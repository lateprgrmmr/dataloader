import sys
import os
import csv
import petl as etl 

#print("dumb fuck")
text = 'a,1\nb,2\nc,3\n'
with open('example.txt', 'w') as f:
    f.write(text)
T1 = etl.fromtext('example.txt')
T2 = T1.capture('lines','(.*),(.*)$',['Fucks','Given'])
print(T2)