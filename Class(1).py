#class

class Employee:        #class definition

    def __init__(self,first,last,pay):     #method of class
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+ '.' + last+ '@gmail.com'

    def fullName(self):                    #method of class
        return '{} {}'.format(self.first, self.last)
        

emp_1=Employee('Vaibhav','Nath',50000)       #instance of class
emp_2=Employee('Test','User',60000)          #instance of class

print(emp_1.fullName())   #calling by instance we dont need to pass argument
print(Employee.fullName(emp_1))   #calling by class we need to paass argument


##Vaibhav Nath
##Vaibhav Nath



##print(emp_1)      ##<__main__.Employee object at 0x000001189D5F6550>
##print(emp_2)      ##<__main__.Employee object at 0x000001189D5F6CD0>


##print(emp_1.email)                ##Vaibhav.Nath@gmail.com
##print(emp_2.email)                ##Test.User@gmail.com


##print('{} {}'.format(emp_1.first, emp_1.last))      ##Vaibhav Nath


##print(emp_1.fullName())           ##Vaibhav Nath



## emp_1.first='Vaibhav'
## emp_1.last='Nath'
## emp_1.email='vaibhav.nath78@gmail.com'
## emp_1.pay=50000
##
## emp_2.first='Test'
## emp_2.last='User'
## emp_2.email='test.user78@gmail.com'
## emp_2.pay=60000