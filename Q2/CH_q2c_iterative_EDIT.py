# PSC Q2 create a list from user input
# Q2c iterative (for, while)
# sum of entered numbers

# empty list
nList = []

#record how many numbers to put in list
num = int(raw_input("how many numbers you want to record? ") )
    
#input number to calc
for y in range(num):
        n = int(raw_input("enter a number: ") )
        nList.append(n)

print "your entered numbers are: ", nList


#iterative sum function
def listsum(nList):
    theSum = 0
    for i in nList:
        theSum = theSum + i
    return theSum

print "the iterative sum of the numbers is: "(listsum(nList))


# dreamincode.net
# stackoverflow.com
# interactivepython.org
'''
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))
'''
