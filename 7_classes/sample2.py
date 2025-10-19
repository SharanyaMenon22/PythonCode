class Person:
    ## name, age, place_of_residence.
    def __init__(self, name, age, gender, place_of_residence):
        self.name = name
        self._age = age
        self.gender = gender
        self.place_of_residence = place_of_residence

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old and I stay in {self.place_of_residence}." # ?
    
    # def set_age(self, age):
    #     if age <= 0:
    #         print(f"{age} for age is an invalid valid")
    #         return
    #     self.age = age
    

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            print(f"{value} for age is an invalid value")
            return
        self._age = value

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Residence: {self.place_of_residence}'

person = Person("Sai", 45, 'M', "Singapore")
print(person.greet())

# person.set_age(46)
person.age = 47

person.age = -1

print(person.age)