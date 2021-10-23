#classmethod , staticmethod
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

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()== 5 or day.weekday()==6:   #python knows day as monday==0 and sunday==6 
            return False
        return True

emp_1=Employee('Vaibhav','Nath',50000)       
emp_2=Employee('Test','User',60000)


print(Employee.raise_amount)     #1.04
print(emp_1.raise_amount)        #1.04
print(emp_2.raise_amount)        #1.04


Employee.set_raise_amount(1.07)   #changes value of class variable to 1.07
print(emp_1.raise_amount)        #1.07
print(emp_2.raise_amount)        #1.07
print(Employee.raise_amount)     #1.07


emp_1.set_raise_amount(1.06)          #changes value of class variable to 1.06
print(emp_1.raise_amount)         #1.06
print(emp_2.raise_amount)         #1.06
print(Employee.raise_amount)      #1.06


emp_str_1='John-Doe-70000'
emp_str_2='Steve-Smith-30000'

new_emp_1=Employee.from_string(emp_str_1)
new_emp_2=Employee.from_string(emp_str_2)

print(new_emp_2.email)     ##Steve.Smith@gmail.com
print(new_emp_2.pay)       ##30000


##first,last,pay=emp_str_1.split('-')
##new_emp_1=Employee(first,last,pay)


print(new_emp_1.email)     ##John.Doe@gmail.com
print(new_emp_1.pay)       ##70000


print(new_emp_1.__dict__)
##{'first': 'John', 'last': 'Doe', 'pay': '70000', 'email': 'John.Doe@gmail.com'}



import datetime
my_date=datetime.date(2021,9,20)
print(Employee.is_workday(my_date))

##True   since the day 20-09-2021 is monday












