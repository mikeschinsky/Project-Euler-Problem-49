#  Euler Project problem 49
#  14 September 2014
#  
#  1) create set of 4 digit primes
#  2) cycle through primes, 
#         create hash of digits to use in identifying palindromes
#         if hash is new, add to dictionary as [hash : number]
#         if hash already exists, add into dictionary [hash : number * 10,000 + new number]
#  3) find max entry in dictionary -->  the answer
#
#  FIND PRIMES
#
from sets import Set
from math import sqrt
import collections  #http://stackoverflow.com/questions/327534/storing-and-updating-lists-in-python-dictionaries-why-does-this-happen
PrimeSet = set()
NotPrime = set()
for x in range(1000,10000):
    PrimeSet.add(x)
for s in PrimeSet:
    for t in range(2,int(sqrt(s))+1):
        if s % t == 0:
            NotPrime.add(s)
            break;
PrimeSet = PrimeSet - NotPrime
print len(PrimeSet)
print len(NotPrime)
#
# Now we have a set of primes, next step is to create a hash for each one, to codify which digits make up each prime number
HashList = collections.defaultdict(list)
DeltaSet = collections.defaultdict(list)
for a in PrimeSet:
	s = 0
	s += 10**(a % 10)
	s += 10**((a % 100) / 10)
	s += 10**((a % 1000) / 100)
	s += 10**(a / 1000)
	HashList[s].append(a)

for t in HashList.keys():
    HashList[t].sort()
    for v in range(len(HashList[t]) - 2):
        x = HashList[t][v+1] - HashList[t][v]
        if x not in DeltaSet[t]:
            DeltaSet[t].append(x)
        else:
            code = t
            progression = x
            DeltaSet[t].append(x)
            print "Found it!!!" , DeltaSet[t]
print code
print HashList[code]
p =  HashList.keys()
print p


