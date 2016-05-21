## Animal is-a object
class Animal(object):
    pass

##Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
     ##Dog has-a name
        self.name = name

##Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ##cat has-a name
        self.name = name

##Person is a object
class Person(object):
    def __init__(self, name):
        ##Person has-a name
        self.name = name

        ##person has-a pet
        self.pet = name

##Employee is a Person
class Employee(Person):
    def __init__(self, name, salary):
        ##Employee has-a name
        super(Employee, self).__init__(name)
        ##Employee has-a salary
        self.salary = salary

##Fish is-a object
class Fish(object):
    pass

##salmon is-a fish
class Salmon(Fish):
    pass

##Halibut is-a fish
class Halibut(Fish):
    pass

##rover is-a Dog
rover = Dog("Rover")

##satan is-a Cat
satan = Cat("Satan")

##Mary is-a Person
mary = Person("Mary")

##mary has-a pet
mary.pet = satan

##frank is-a employee
##frank has-a name and salary
frank = Employee("Frank", 120000)

#frank has-a pet
frank.pet = rover

##flipper is-a fish
flipper = Fish()

##crouse is-a fish
crouse = Salmon()

##harry is-a halibut
harry = Halibut()