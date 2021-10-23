#CLASS PRACTICES

class Student():

    year=2021

    def __init__(self,first,last,student_id):
        self.first=first
        self.last=last
        self.student_id=student_id

    def FullName(self):
        return '{} {}'.format(self.first , self.last)

    def Email(self):
        return '{}'.format(self.first) +"."+ '{}@gmail.com'.format(self.last)

    def __repr__(self):           #used for debugging
        return "Student('{}','{}',{})".format(self.first ,self.last ,self.student_id)

    def __str__(self):
        return '{} - {} - {}'.format(self.FullName(),self.student_id,self.Email())

    def __add__(self,other):
        return self.student_id + other.student_id


    @classmethod
    def ChangeYear(cls,yearr):
        cls.year=yearr

    @staticmethod
    def greet():
        print("Good morning")

class Branch(Student):                   ##inheritance

    def __init__(self, first, last, student_id,branch):
        super().__init__(first, last, student_id)
        self.branch=branch



st_1=Student("Vaibhav" , "Nath" , 1010199)
st_2=Student("Thomas" , "Edison" , 1010109)


print(repr(st_1))                 #Student('Vaibhav','Nath',1010199)
print(str(st_1))                  # Vaibhav Nath - 1010199 - Vaibhav.Nath@gmail.com

print(st_1+st_2)                  #2020308

##print(Student.year)             #2021
##print(st_1.FullName())          #Vaibhav Nath
##print(Student.FullName(st_1))   #Vaibhav Nath
##print(st_1.year)                #2021
##print(st_1.first)               #Vaibhav
##print(st_1.Email())             #Vaibhav.Nath@gmail.com


##st_1.year=2020
##print(st_1.year)     #2020


##Student.ChangeYear(2010)
##print(st_1.year)        #2020 because we have declared st_1.year=2020 in the code
##print(Student.year)     #2010
##print(st_2.year)        #2010
# st_1.greet()              #Good Morning
# print(st_1.greet())       #Good morning  None


# st_3=Branch("Virat","Nath",101205,"CSE")
# print(st_3.Email())                             #Virat.Nath@gmail.com
# print(st_3.FullName())                          #Virat Nath
# st_3.greet()                                    #Good morning



