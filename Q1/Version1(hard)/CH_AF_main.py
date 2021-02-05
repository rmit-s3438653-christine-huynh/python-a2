from CH_emp_AF2 import *

def main():
# 1. adding employee details to dictionary list
    e = Employee()
    e.addEmpDetails ("sga59", "Susan Gilmore", "Accounts", 80000, 6)
    e.addEmpDetails ("gai09", "Greg Anderson", "IT", 120000, 12)
    e.addEmpDetails ("dje23", "Dave Jones", "Engineering", 100000, 10)
    e.addEmpDetails ("lwf05", "Luke Williamson", "Finance", 125000, 15)
    e.addEmpDetails ("wnf11", "William Norman", "Finance", 101000, 11)
    e.addEmpDetails ("hse55", "Harvey Smith", "Engineering", 80000, 5)
    e.addEmpDetails ("dmm33", "Debbie Myer", "Marketing", 120000, 15)

# displays employee details
    print "EMPLOYEE RECORDS ADDED: "
    e.getEmpDetails()

# 2. deleting employee details that match the word 'sga59'
    e.delEmpDetails( "sga59" )
    print "\n"
    print "EMPLOYEE 'sga59' HAS BEEN REMOVED FROM THE EMPLOYEE RECORD"
    
# 3. prints new employee list with removed detail
    print "\n"
    print "THE NEW EMPLOYEE RECORD: "
    e.getEmpDetails()

# 5. prints employees who worked > 10 yrs
   # e.emp_service_years()

# 6. change dept info
    #e.get(empDept[,default_value] )

# 4. saving employee details to txt file
    print "\n"
    e.saveEmpDetails()
    print "NEW EMPLOYEE RECORD IS SAVED TO 'empDetails.txt'"

main()
