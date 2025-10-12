'''
types: int
       string
       float
       boolean

collections = list
              tuples
              dictionaries
              set

persons = []              
person = ["Sai", 45, "Singapore"]       
persons.append(person)

.....

...



Now need to update the age.
persons[0][1] = 46  👈  at this point, it does not make sense what 1 index is.

To overcome this issue, we can create user defined types called classes.
'''



class Square:

    def __init__(self, side):
        self._side = side
    

    @property
    def area(self):
        return f'Area = {self.side * self.side}'
    
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    

square = Square(4)
print(square.area)

square.side = 10

print(square.area)


class Person:
    ## name, age, place_of_residence.
    def __init__(self, name, age, place_of_residence):
        self.name = name
        self._age = age
        self.place_of_residence = place_of_residence

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old and I stay in {self.place_of_residence}." # ?
    
    def set_age(self, age):
        self._age = age

    @property
    def age(self):
        return f'age is {self._age}'    

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Residence: {self.place_of_residence}'

person = Person("Sai", 45, "Singapore")
print(person.greet())

person.set_age(46)

print(person.age)



class Employee(Person):
    # name, age, place_of_residence, qualification
    # since some of the attributes are common to Person, we can inherit Employee from Person.

    def __init__(self, name, age, place_of_residence, qualification):
        super().__init__(name, age, place_of_residence)
        self.profession = qualification

    def greet(self):
        return super().greet() + f"I am working as {self.profession}"        
    
    def __str__(self):
        return super().__str__() + f', Profession: {self.profession}'

employee = Employee("Sai", 46, "Singapore", "Software Engineer")

print(employee.greet())
print(employee)

list_of_employees = []

list_of_employees.append(employee)
list_of_employees.append(Employee("Jagan", 46, "India", "Mechanical Engineer"))
list_of_employees.append(Employee("Sharanya", 20, "Singapore", "Software Engineer"))

for employee in list_of_employees:
    print(employee.greet())


# need to group the employees by profession.

group_by_profession = {}

for employee in list_of_employees:
    
    employees = group_by_profession.get(employee.profession, [])
    employees.append(employee)
    group_by_profession[employee.profession] = employees # update the dictionary back with the list of employees.


for key, employees in group_by_profession.items():
    print(f"\n{key}:")
    for emp in employees:
        print(f"{emp.name}")


# get the list of employees who are not sofware engineers.

not_sw = []
for key, employees in group_by_profession.items():
    if key != 'Software Engineer':
        not_sw.append(employees)

for employee in employees:
    print(employee)
