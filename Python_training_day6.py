# 1) Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
import math
class Circle():
    """This class can be used to find the area of the circle"""

    def __init__(self,circle_radius):
        self.radius = circle_radius
    def area_of_circle(self):
        print (math.pi*(self.radius * 2))
# print(Circle.__name__)
# cir = Circle(2)
# cir.area_of_circle()


# 2) Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle():
    """This class can be used to find out the area of the rectangle"""
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area_of_rectange(self):
        print(self.width*self.length)

# rect = Rectangle(4,5)
# rect.area_of_rectange()

# 3) Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():
    """Test"""
    def __init__(self,a=0):
        self.area = a

    def Area(self):
        print (self.area)

class Square(Shape):
    def __init__(self,length=0):
        self.len = length

    def Area(self):
       print(self.len*self.len)


# test = Square(4)
# test.Area()

# test1 = Shape()
# test1.Area()


# 4) Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case

class Test:
    # def set_String(self,word):
    #     self.word=word

    def set_String(self):
        self.word = input("Enter the name:")

    def get_String(self):
        print(self.word.upper())

# test1 = Test()
# test1.set_String()
# test1.get_String()

# 5) Differentiate between Multiple &Multilevel Inheritance

# Multiple Class definition

class Vehicle():
    no_of_tyres = 4
    fuel_type = "Petrol"
    def Honk(self):
        print("Piee Piee Piee.........")

class Car(Vehicle):
    car_color ='red'
    car_make = '2018'

class Train(Car):
    no_of_tyres = 108


# car_test = Car
# car_test.Honk('self')
# print (car_test.no_of_tyres)
# print(car_test.car_color)
# print(car_test.car_make)


# Multi level Inheritance

class Vehicle():
    no_of_tyres = 4
    fuel_type = "Petrol"
    def Honk(self):
        print("Piee Piee Piee.........")

class Car(Vehicle):
    car_color ='red'
    car_make = '2018'

class Train(Car):
    no_of_tyres = 108

class Bullet_train(Train,Car):
    fuel_type = 'current'

# a = Vehicle()
# a.Honk()

# bullet_test = Bullet_train
# print (bullet_test.no_of_tyres)
# print (bullet_test.fuel_type)
# print (bullet_test.car_make)
# print (bullet_test.car_color)
# bullet_test.Honk('self')

class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

# print(M.mro())

class First():
    def __init__(self):
        print ("first")
    def Test(self,var):
        self.var = var
        # a = type(self.var)
        print ("The length of the",len(self.var))
class Second():
    def __init__(self):
        print ("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print ("that's it")

# A = Third()
# A.Test("praneeth")

# 6) Differentiate static and class methods

from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1989)

# print(person1.age)
# print(person2.age)
# print(Person.isAdult(22))


# vowels = ['a', 'e', 'i', 'o', 'u']
# vowelsIter = iter(vowels)
# print(next(vowelsIter))
# print(next(vowelsIter))
# print(next(vowelsIter))
# print(next(vowelsIter))
# print(next(vowelsIter))

