class Employee:
    
    raise_amount=1.04   #class variable

    def __init__(self,first,last,pay):     
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+ '.' + last+ '@gmail.com'         

    def fullName(self):                    
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)   #cannot simply write raise_amount because when we access class variable inside a method we need to use class name as Employee.raise_amount or self.raise_amount


class Developer(Employee):
    
    raise_amount=1.10     #class variable , it does not make any changes to parent class variable's and when called by developer object it will be called rather than class variable

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)    #allows the Employee class to handle the three attributes first , last , pay
        self.prog_lang=prog_lang


class Manager(Employee):
    
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)    #allows the Employee class to handle the three attributes first , last , pay
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self , emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self , emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())
    
    
##emp_1=Employee('Vaibhav','Nath',50000)       
##emp_2=Employee('Test','User',60000)


dev_1=Developer('Vaibhav','Nath',50000,'python')     #access attribute of parent class from child class  
dev_2=Developer('Test','User',60000,'java')        #access attribute of parent class from child class


print(dev_1.fullName())                #Vaibhav Nath                
print(dev_2.first +' '+ dev_2.last)    #Test User
print(dev_1.prog_lang)                 #python


mgr_1=Manager('Sam','Curran',90000,[dev_1])
print(mgr_1.email)                     #Sam.Curran@gmail.com
mgr_1.add_emp(dev_2)
mgr_1.print_emps()


##--> Vaibhav Nath
##--> Test User


mgr_1.remove_emp(dev_1)
mgr_1.print_emps()


##--> Test User


'''print(dev_1.email)
print(dev_2.first +' '+ dev_2.last)'''

##Vaibhav.Nath@gmail.com
##Test User


'''print(emp_1.email)
print(emp_2.first +' '+ emp_2.last)'''

##Vaibhav.Nath@gmail.com
##Test User


'''print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)'''


##50000
##55000



print(isinstance(mgr_1, Manager))             #True

print(isinstance(mgr_1, Employee))            #True

print(isinstance(mgr_1, Developer))           #False

print(issubclass(Developer, Employee))        #True

print(issubclass(Manager , Employee))         #True

print(issubclass(Developer , Manager))        #False

















