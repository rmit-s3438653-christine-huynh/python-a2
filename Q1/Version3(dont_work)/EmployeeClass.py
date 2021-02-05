# PSC try making own classes
# Q1,A,B,C,D,E,F
# advised by Min Gurung

class Employee:
# empty list
    #empList = []
    def __init__( self, empID, empName, empDept, empSal, yrOfServ ):
        self.id = empID
        self.name = empName
        self.dept = empDept
        self.sal = empSal
        self.yos = yrOfServ

# mutated (change state) methods
    def setId(self, empID):
        self.id = empID

    def setName(self, empName):
        self.name = empName

    def setDept(self, empDept):
        self.dept = empDept

    def setSal(self, empSal):
        self.sal = empSal

    def setYos(self, yrOfServ):
        self.yos = yrOfServ

# accessor methods (get methods)
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def getDept(self):
        return self.dept
    def getSal(self):
        return self.sal

    def getYos(self):
        return self.yos

# 1. add employee details
    def addEmpDetails (self, empID, empName, empDept, empSal, yrOfServ):
        empList.append (empID, empName, empDept, empSal, yrOfServ)

        #Employee.empList.append(Employee)
        
    #def addEmpDetails (emp):
        #Employee.empList.append(emp)
        
# 2. delete employee from list
    def delEmpDetails(empID):
        del empID

# 3. print employee details 
    def getEmpDetails (self): 
        print "%-8s %-18s %-15s %-10s %-10s" %(self.id, self.name, self.dept,
                                                self.sal, self.yos)

# 4. save employee details to txt file
    def saveEmpDetails():
        outFile = open ("empDetails.txt", "w")
        outFile.write ("%-8s %-18s %-15s %-10s %-10s" %("ID", "NAME",
                                                #               "DEPARTMENT",
                                               # "SALARY", "YRS OF SERVICE")
        outFile.write(getEmpDetails(e1,e2,e3,e4,e5,e6)

        #empIDList = self.emp.keys()
        #for item in empIDList:
            #st = self.emp[item] [0] + "," + \
                 #self.emp[item] [1] + "," + \
                 #str (self.emp [item] [2] )
            #outFile.writelines( st + '\n')
        outFile.close()
        
# 5. print ID, names of employee work for more than 10 yr
    def emp_service_years(self,yrOfServ):
        if Employee.yrOfServ >= 10:
            print empID, empName
        else:
            print "NO EMPLOYEE WORKED > 10yr"
            
        #self.yos = yrOfServ

# 6. change employee department information
    def change_dept(self, empDept):
        self.dept = empDept
