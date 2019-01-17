import math,sys

#number = int(sys.argv[1])
number = 13195
biggestprimefactor = 2
while (number > biggestprimefactor):
    if (number%biggestprimefactor) == 0:
        number = number/biggestprimefactor
        biggestprimefactor = 2
    else:
        biggestprimefactor+=1
#print("The largest prime factor of ",sys.argv[1] ," is ", biggestprimefactor)
print(biggestprimefactor)
