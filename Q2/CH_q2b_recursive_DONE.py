# PSC Q2 create a list from user input
# Q2b recursive (if, else)
# sum of entered numbers

# empty list
nList = []

# record how many numbers to put in list
num = int(raw_input("how many numbers you want to record? ") )

# input number to calc
for y in range(num):
    n = int(raw_input("enter a number: ") )
    nList.append(n)

print "your entered numbers are: ", nList

def main():
# recursive sum function
    def listSum(numList):
        if len(numList) == 1:
            return numList[0]
        else:
            return numList[0] + listSum(numList[1:])
# print
    print "the recursive sum of the numbers is: ",(listSum( nList ) )

main()
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
