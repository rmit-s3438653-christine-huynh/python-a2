# PSC Q2 create a list from user input

def main():

# empty list
    numList = []

#record how many numbers to put in list
    num = int(raw_input("how many numbers you want to record? ") )

#input number
    for y in range(num):

        n = int(raw_input("enter a number: ") )
        numList.append(n)

# print results
    print "your entered numbers are: ", numList
    
main()
# dreamincode.net
