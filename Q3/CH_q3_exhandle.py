# PSC Q3 exception handling

def main():

# empty list
    numList = []

#record how many numbers to put in list
    while True:
        try:
            num = int(raw_input("how many numbers you want to record? ") )
            break
        except ValueError, TypeError:
            print "It must be a number"
            continue

#input number to calc
    for y in range(num):

        while True:
            try:
                n = int(raw_input("enter a number: ") )
                numList.append(n)
                x = sum(numList)
                break
            except ValueError, TypeError:
                print"It must be a number"
                continue

    #myList = num.append(num)

    print "your entered numbers are: ", numList
    print "the sum of the numbers is: ", x


main()
# dreamincode.net
# trycatch.py
# docs.python.org
