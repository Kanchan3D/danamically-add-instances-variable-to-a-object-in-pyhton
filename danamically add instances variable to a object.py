class Student:
    name=''
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
stud=Student("Jessa",20)
print('Before')
print('Name:',stud.name,'Age:',stud.age)
stud.marks=75
print('After')
print('Name:',stud.name,'Age:',stud.age,'Marks:',stud.marks)
stud.std=12
print(stud.std)