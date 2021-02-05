# PSC Q2 create a list from user input
# Q2c iterative (for, while)
# sum of entered numbers

# empty list
nList = []

#record how many numbers to put in list
#exception handling 1
while True:
    try:
        num = int(raw_input("how many numbers you want to record? ") )
        break
    except ValueError, TypeError:
        print "It must be a number"
        continue
    
#input number to calc
for y in range(num):
    
#exception handle 2
    while True:
        try:
            n = int(raw_input("enter a number: ") )
            numList.append(n)
            break
        except ValueError, TypeError:
            print "It must be a number"
            continue
print "your entered numbers are: ", numList

#iterative sum function
def listSum(nList):
    theSum = 0
    for i in nList:
        theSum = theSum + i
    return theSum

    print("the sum of the numbers is: ", listsum([nList]))

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
