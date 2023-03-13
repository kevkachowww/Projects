"""
School Catalogue
Let’s put your knowledge of classes to the test by creating a digital school catalog for the New York City Department of Education. The Department of Education wants the catalog to hold quick reference material for each school in the city.

We need to create classes for primary and high schools. Because these classes share properties and methods, each will inherit from a parent School class. Our parent and three child classes have the following properties, getters, setters, and methods:

School
Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
Getters: all properties have getters
Setters: the numberOfStudents property has a setter
Methods: A __repr__ method that displays information about the school.

Primary
Includes everything in the School class, plus one additional property
Properties: pickupPolicy (string, like "Pickup after 3pm")

Middle
Does not include any additional properties or methods

High
Includes everything in the School class, plus one additional property
Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])
"""
from abc import ABC, abstractmethod

class School(ABC):
    name = None
    level = None
    numberOfStudents = 0

    def __init__(self, name, level, num):
        self.name = name
        self.level = level
        self.numberOfStudents = num

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getNumberOfStudents(self):
        return self.numberOfStudents

    def setNumberOfStudents(self, newNumberOfStudents):
        if isinstance(newNumberOfStudents, int):
            self.numberOfStudents = newNumberOfStudents
        else:
            raise TypeError

    def __repr__(self):
        return f"{self.name} is a {self.level} school with {self.numberOfStudents} students"


class PrimarySchool(School):
    pickupPolicy = None

    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        return f"{super().__repr__()}, the pickup policy is {self.pickupPolicy}"


class Middle(School):

    def __init__(self):
        pass


class HighSchool(School):
    sportsTeams = []

    def __init__(self, name, numberOfStudents, sportsTeam):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeam = sportsTeam

    def getSportsTeams(self):
        return self.sportsTeam

    def __repr__(self):
        return "{super}, and here is the list of sports teams: {sportsTeam}".format(super=super().__repr__(),
                                                                                    sportsTeam=self.sportsTeam)

# For Testing
a = School('Mineola', 'high', 100)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(200)
print(a.getNumberOfStudents())
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.getPickupPolicy())
print(b)
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)