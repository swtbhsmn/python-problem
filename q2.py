# Q2.  Define a class Person and its two child classes: Male and Female. All classes have a
#      method "get_gender" which can print "Male" for Male class and "Female" for Female Class.
#      Bonus: Make class Person an abstract class and make get_gender an abstract method in the same class.
#      The two child classes must inherit and implement get_gender. i.,e, When trying to initialize an 
#      object of class Person, the program must throw an error.
#      Hint: 
#      Use abc library (comes natively with Python3) https://www.python-course.eu/python3_abstract_classes.php

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self):
	    self.gender = "unknown"

    @abstractmethod
    def get_gender(self):
	    pass

class Male(Person):
    def __init__(self):
	    self.gender = "Male"
    
    def get_gender(self):
        return self.gender

class Female(Person):
    def __init__(self):
	    self.gender = "Female"
    def get_gender(self):
        return self.gender

class OtherGender(Person):
  
    def get_gender(self):
        return self.gender

#person  = Person() // class Person, the program must throw an error beacuse it is an abstract class.

fe_male  = Female()
male     = Male()
other    = OtherGender()

print(fe_male.get_gender())  # Female
print(male.get_gender())     # Male
print(other.get_gender())    # unknown
