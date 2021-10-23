class Student():    

    def __init__(self,first,last):
        self.first=first
        self.last=last

    @property
    def email(self):
        return '{}'.format(self.first) + '.' + '{}@yahoo.com'.format(self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first,self.last)

    @fullName.setter
    def fullName(self,name):
        first , last =name.split(' ')
        self.first=first
        self.last=last

    @fullName.deleter
    def fullName(self):
        print('Delete Name')
        self.first=None
        self.last=None
        
        
st_1=Student("Vaibhav" , "Nath" )
st_2=Student("Thomas" , "Edison" )

print(st_1.email)         #Vaibhav.Nath@yahoo.com
print(st_1.fullName)      #Vaibhav Nath
print(st_1.first)