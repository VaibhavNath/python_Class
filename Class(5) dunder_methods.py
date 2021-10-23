#special methods ( dunder or magic methods )
#Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
# __init__, __add__, __len__, __repr__ etc.

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
        self.pay=int(self.pay * self.raise_amount)

    def __repr__(self):           #used for debugging
        return "Employee('{}','{}',{})".format(self.first ,self.last ,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullName(),self.email)

    def __add__(self , other):      #add salary of employees
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())


emp_1=Employee('Vaibhav','Nath',50000)       
emp_2=Employee('Test','User',60000)

print(emp_1+emp_2)           #110000  #adds the salary of both emp

##print(emp_1)

print(repr(emp_1))             #Employee('Vaibhav','Nath',50000)      
print(str(emp_1))              #Vaibhav Nath - Vaibhav.Nath@gmail.com


print(emp_1.__repr__())        #Employee('Vaibhav','Nath',50000) 
print(emp_1.__str__())         #Vaibhav Nath - Vaibhav.Nath@gmail.com



print(int.__add__(1,2))           #3
print(str.__add__('a','b'))       #ab



print(len('vaibhav'))                 #7
print('vaibhav'.__len__())            #7


print(len(emp_1))                     #12
