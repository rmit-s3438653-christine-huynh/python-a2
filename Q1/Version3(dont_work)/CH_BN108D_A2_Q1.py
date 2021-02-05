# Q1.A,B,C,D,E,F
# Assisted by Min Gurung

from EmployeeClass import *

def main():
    
# 1. add employee details
    #e = Employee()
    #e.addEmpDetails ("sga59", "Susan Gilmore", "Accounts", 80000, 6)
    #e.addEmpDetails ("gai09", "Greg Anderson", "IT", 120000, 12)
    #e.addEmpDetails ("dje23", "Dave Jones", "Engineering", 100000, 10)
    #e.addEmpDetails ("lwf05", "Luke Williamson", "Finance", 125000, 15)
    #e.addEmpDetails ("wnf11", "William Norman", "Finance", 101000, 11)
    #e.addEmpDetails ("hse55", "Harvey Smith", "Engineering", 80000, 5)
    #e.addEmpDetails ("dmm33", "Debbie Myer", "Marketing", 120000, 15)
  
    e1 = Employee ("sga59", "Susan Gilmore", "Accounts", 80000, 6)
    e2 = Employee ("gai09", "Greg Anderson", "IT", 120000, 12)
    e2 = Employee ("dje23", "Dave Jones", "Engineering", 100000, 10)
    e3 = Employee ("lwf05", "Luke Williamson", "Finance", 125000, 15)
    e4 = Employee ("wnf11", "William Norman", "Finance", 101000, 11)
    e5 = Employee ("hse55", "Harvey Smith", "Engineering", 80000, 5)
    e6 = Employee ("dmm33", "Debbie Myer", "Marketing", 120000, 15)
    
    #e.addEmpDetails(e1)


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
    #del Employee.empList[e1]

# 5. print employee who worked > 10 yr
    #Employee.emp_service_years()

# 6. change department of employee1 (e1)
    e1.change_dept("Arts")
    print "EMPLOYEE 'Susan Gilmore's DEPARTMENT HAS BEEN CHANGED TO 'Arts' "
    print "%-8s %-18s %-15s %-10s %-10s" %("ID", "NAME", "DEPARTMENT",
                                                "SALARY", "YRS OF SERVICE")
    e1.getEmpDetails()

# 4. saving employee details to txt file
    #Employee.saveEmpDetails()
    #print "NEW EMPLOYEE RECORD IS SAVED TO 'saveEmpR2.txt'"
main ()

