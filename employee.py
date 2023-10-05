class Employee:
    def __init__(self,name,age,gender,salary):

        if salary <= 0:
            print('Invalid salary')
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
    def __str__(self) :
        return f'name = {self.name} {self.age} {self.gender} {self.salary}' 

Employee1 = Employee(
        str(input('Enter employee name:')),
        int(input('Enter employee age:')),
        str(input('Enter employee gender:')),
        int(input('Enter employee salary:'))
    )
print(Employee1)