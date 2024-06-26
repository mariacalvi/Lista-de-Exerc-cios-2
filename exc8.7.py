class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show_data(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}")


person1 = Person("Maria", 19)
person2 = Person("Harry", 30)
employee1 = Employee("Dev", 34, 5000000)
employee2 = Employee("SZA", 35, 60000)

people_and_employees = [person1, person2, employee1, employee2]

for obj in people_and_employees:
    obj.show_data()
