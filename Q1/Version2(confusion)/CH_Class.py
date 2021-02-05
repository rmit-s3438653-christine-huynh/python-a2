# PSC try making own classes

from Employee import *
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
    def addEmpDetails (self, empID, empName, empDept, empSal, yrOfServ):
        Employee.empList.append()
        
# 2. delete employee from list
    def delEmpDetails(self, empID):
        del empID

# 3. print employee details 
    def getEmpDetails (self): 
        print "%-8s %-18s %-15s %-10s %-10s" %(self.id, self.name, self.dept,
                                                self.sal, self.yos)

# 4. save employee details to txt file
    def saveEmpDetails(self):
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

def main():
# 1. add employee data
    e1 = Employee ("sga59", "Susan Gilmore", "Accounts", 80000, 6)
    e2 = Employee ("gai09", "Greg Anderson", "IT", 120000, 12)
    e2 = Employee ("dje23", "Dave Jones", "Engineering", 100000, 10)
    e3 = Employee ("lwf05", "Luke Williamson", "Finance", 125000, 15)
    e4 = Employee ("wnf11", "William Norman", "Finance", 101000, 11)
    e5 = Employee ("hse55", "Harvey Smith", "Engineering", 80000, 5)
    e6 = Employee ("dmm33", "Debbie Myer", "Marketing", 120000, 15)
    
# 3. print employee details
    print "%-8s %-18s %-15s %-10s %-10s" %("ID", "NAME", "DEPARTMENT",
                                                "SALARY", "YRS OF SERVICE")
    Employee.getEmpDetails(e1)
    Employee.getEmpDetails(e2)
    Employee.getEmpDetails(e3)
    Employee.getEmpDetails(e4)
    Employee.getEmpDetails(e5)
    Employee.getEmpDetails(e6)
    print "\n"

# 2. delete employee data
    #Employee.delEmpDetails( "sga59" )
    #print "EMPLOYEE 'sga59' HAS BEEN REMOVED FROM THE EMPLOYEE RECORD"

# 5. print employee who worked > 10 yr
    #for yr in yrOfServ: #yrOfServ:
    #if Employee.emp_service_years >= 10:
        #print empID, empName, yrOfServ
    #else:
        #print "NO EMPLOYEE WORKED > 10yr"

# 6. change department of employee1 (e1)
    e1.change_dept("Arts")
    print "EMPLOYEE 'Susan Gilmore' DEPARTMENT HAS BEEN CHANGED TO 'Arts' "
    print "%-8s %-18s %-15s %-10s %-10s" %("ID", "NAME", "DEPARTMENT",
                                                "SALARY", "YRS OF SERVICE")
    e1.getEmpDetails()

# 4. saving employee details to txt file
    #Employee.saveEmpDetails()
    #print "NEW EMPLOYEE RECORD IS SAVED TO 'saveEmpR2.txt'"

main ()
#ID: %s, NAME: %s, DEPARTMENT: %s, SALARY: %s, YRS OF SERVICE: %s" % (
            #self.id, self.name, self.dept, self.sal, self.yos)
