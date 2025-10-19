import os

stars = '*' * 40

class Person:
    def __init__(self, name, age, gender, place_of_residence):
        self.name = name
        self.age = age
        self._gender = gender
        self.place_of_residence = place_of_residence

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value in ['M', 'F']:
            self._gender = value
        else:
            raise ValueError("Gender must be 'M', 'F'")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Place of Residence: {self.place_of_residence}"

class Employee(Person):
    def __init__(self, name, age, gender, profession, place_of_residence):
        super().__init__(name, age, gender, place_of_residence)
        self.profession = profession

    def __str__(self):
        person_str = super().__str__()
        return f"{person_str}, Profession: {self.profession}"


def brittle_way():
    print(f'\n{stars}\n')
    list_of_emps = []
    emp_csv_path = os.path.join( os.path.abspath(__file__), '..', 'employee.csv')

    with open(emp_csv_path, 'r') as file:
        for index, line in enumerate(file):
            if index == 0:
                continue
            columns = line.split(',')
            employee = Employee(
                columns[0], # name
                columns[1], # age
                columns[2], # gender
                columns[3], # profession
                columns[4], # placeofresidence
            )
            list_of_emps.append(employee)
    
    for emp in list_of_emps:
        print(emp)


def header_index_mapping(header):
    headers = {}
    for i, h in enumerate(header.strip().split(',')):
        headers[h] = i
    return headers

def robust_way():

    print(f'\n{stars}\n')

    list_of_employees = []

    emp_csv_path = os.path.join(os.path.abspath(__file__), '..', 'employee.csv')

    with open(emp_csv_path, 'r') as file:
        for index, line in enumerate(file):
            if index == 0:
                headers = header_index_mapping(line)
                continue
            row = line.strip().split(',')
            employee = Employee(
                name=row[headers['Name']],
                age=row[headers['Age']],
                gender=row[headers['Gender']],
                profession=row[headers['Profession']],
                place_of_residence=row[headers['PlaceOfResidence']]
            )
            list_of_employees.append(employee)

    for emp in list_of_employees:
        print(emp)


def main():
    brittle_way()
    robust_way()


if __name__ == '__main__':
    main()