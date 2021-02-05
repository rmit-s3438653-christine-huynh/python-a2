# PSC derrived from books.py
# Q1.A,B,C,D,E,F employee class

# employee class, empty list
class Employee:
    def __init__(self):
        self.emp = {}

# 1. add employee details
    def addEmpDetails (self, empID, empName, empDept, empSal, yrOfServ):
        self.emp[empID]=(empID, empName, empDept, empSal, yrOfServ)

# 2. delete employee from list
    def delEmpDetails(self, empID):
        del self.emp[empID]

# 3. print employee details 
    def getEmpDetails (self):
        empID = self.emp.keys()
        for item in empID:
            print self.emp[item] [0],
            print self.emp[item] [1],
            print self.emp[item] [2]

# 4. save employee details to txt file
    def saveEmpDetails(self):
        outFile = open ("empDetails.txt", "w")
        empIDList = self.emp.keys()

        for item in empIDList:
            st = self.emp[item] [0] + "," + \
                 self.emp[item] [1] + "," + \
                 str (self.emp [item] [2] )
            outFile.writelines( st + '\n')
        outFile.close()
        
# 5. print ID, names of employee work for more than 10 yr
    def emp_service_years(self):
        for yr in self.emp: #yrOfServ:
            if yr >= 10:
                print self.empID, self.empName, self.yrOfServ
            else:
                print "none work > 10yr"

# 6. change employee department information
    #def change_dept(self, empDept):
        #self.dept = empDept

# tutorialspoint.com
# thegeekstuff.com
# python cookbook
# python : chris fehily
