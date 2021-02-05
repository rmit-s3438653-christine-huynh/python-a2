# PSC try making own classes

class Employee:
# employee class attributes
    empList = [] # class list to add employee object
    
# initialise instance variables
    def __init__( self, empID, empName, empDept, empSal, yrOfServ ):
        self.id = empID
        self.name = empName
        self.dept = empDept
        self.sal = empSal
        self.yos = yrOfServ

# 1. add employee details
    #def addEmpDetails (self, empID, empName, empDept, empSal, yrOfServ):
        #Employee.empList.append()
    def addEmpDetails (emp):
        Employee.empList.append(emp)
        
# 2. delete employee from list
    def delEmpDetails(self, empID):
        del empID

# 3. print employee details 
    def getEmpDetails (self): 
        print "%-8s %-18s %-15s %-10s %-10s" %(self.id, self.name, self.dept,
                                                self.sal, self.yos)

# 4. save employee details to txt file
    def saveEmpDetails():
        outFile = open ("empDetails.txt", "w")
        #outFile.write ("%-8s %-18s %-15s %-10s %-10s" %("ID", "NAME",
                                                #               "DEPARTMENT",
                                               # "SALARY", "YRS OF SERVICE")
        outFile.write(getEmpDetails)

        #empIDList = self.emp.keys()
        #for item in empIDList:
            #st = self.emp[item] [0] + "," + \
                 #self.emp[item] [1] + "," + \
                 #str (self.emp [item] [2] )
            #outFile.writelines( st + '\n')
        outFile.close()
        
# 5. print ID, names of employee work for more than 10 yr
    def emp_service_years(self,yrOfServ):
        self.yos = yrOfServ

# 6. change employee department information
    def change_dept(self, empDept):
        self.dept = empDept


