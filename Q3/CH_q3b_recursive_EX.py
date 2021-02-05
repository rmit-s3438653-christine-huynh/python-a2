# PSC Q2 create a list from user input
# Q2b recursive (if, else)
# sum of entered numbers

# empty list
numList = []

# record how many numbers to put in list
#exception handling 1
while True:
    try:
        num = int(raw_input("how many numbers you want to record? ") )
        break
    except ValueError, TypeError:
        print "It must be a number"
        continue

# input number to calc
for y in range(num):

# exception handle 2
    while True:
        try:
            n = int(raw_input("enter a number: ") )
            numList.append(n)
            
            break
        except ValueError, TypeError:
            print "It must be a number"
            continue
print "your entered numbers are: ", numList
    
# recursive sum function
def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])
    
# print
print"the sum of the numbers is: ",(listSum(numList))

# dreamincode.net
# stackoverflow.com
# interactivepython.org
# http://interactivepython.org/courselib/static/pythonds/Recursion/recursionsimple.html
'''
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))
'''
