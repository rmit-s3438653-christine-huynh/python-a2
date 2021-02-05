# PSC try making own classes
# Q1,A,B,C,D,E,F
# advised by Min Gurung

class Employee:
#class list to add employee object
    empList = []
    
    def __init__( self, empID, empName, empDept, empSal, yrOfServ ):
# initialise instance variables
        self.id = empID
        self.name = empName
        self.dept = empDept
        self.sal = empSal
        self.yos = yrOfServ

# define set methoda for each variable
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

# define get methods for each variable
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


