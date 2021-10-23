class Employee:
    
    raise_amount=1.04   #class variable

    def __init__(self,first,last):     
        self.first=first
        self.last=last     

    @property
    def email(self):                    
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullName(self):                    
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self,name):
        first , last = name.split(' ')
        self.first=first
        self.last=last

    @fullName.deleter
    def fullName(self):
        print('delete name')
        self.first=None
        self.last=None

emp_1=Employee('Vaibhav','Nath')

emp_1.fullName='JIMMY SHERGIL'  #it produces an error , for this we use setter



##emp_1.first='jim'           #changes only the local declaration of first

print(emp_1.first)          #jim

print(emp_1.email)          #Vaibhav.Nath@gmail.com    #name in email does not changes

print(emp_1.fullName)

##print(emp_1.fullName())     #jim Nath

del emp_1.fullName

print(emp_1.first)          #jim

print(emp_1.email())          #jim.Nath@gmail.com    #name in email does not changes

print(emp_1.fullName())     #jim Nath



