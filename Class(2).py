class Employee:
    
    num_of_emp = 0
    raise_amount=1.04   #class variable

    def __init__(self,first,last,pay):     
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+ '.' + last+ '@gmail.com'

        Employee.num_of_emp += 1     

    def fullName(self):                    
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay * Employee.raise_amount)   #cannot simply write raise_amount because when we access class variable inside a method we need to use class name as Employee.raise_amount or self.raise_amount

        
print(Employee.num_of_emp)

#0

emp_1=Employee('Vaibhav','Nath',50000)       
emp_2=Employee('Test','User',60000)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

##50000
##52000


print(Employee.num_of_emp)

#2


print(Employee.raise_amount)    #access class variable from class
print(emp_1.raise_amount)       #accessing class variable from instance
print(emp_2.raise_amount)

##1.04
##1.04
##1.04


Employee.raise_amount=1.06      #changes the class variable value
print(Employee.raise_amount)    #access class variable from class
print(emp_1.raise_amount)       #accessing class variable from instance
print(emp_2.raise_amount)

##1.06
##1.06
##1.06


emp_1.raise_amount=1.05        #changes value of class variable only for this instance.
print(emp_1.raise_amount)
print(emp_2.raise_amount)

##1.05
##1.06


print(emp_1.__dict__)

##{'first': 'Vaibhav', 'last': 'Nath', 'pay': 50000, 'email': 'Vaibhav.Nath@gmail.com'}
