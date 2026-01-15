#---- Class----

# class Person:
#     name = "Soniya"
#     occupation = "Data Scientist"
#     networth = 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

#--- Object----

# a= Person()
# b = Person()
# a.name="Shuvam"
# a.occupation = "Accountant"
# print(a.name, a.occupation)



# b.name = "Nitika"
# b.occupation ="HR"
# print(b.name, b.occupation)
# a.info()
# b.info()


#----Constructor----
#---Parameterized constructor----
# class Person:
#     def __init__(self, n, o):
#         print("Hey I am a peerson")
#         self.name = n
#         self.occ = o

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# d = Person("Harry", "Developer")
# e = Person("Divya", "HR") # e is passing as self automatically
# d.info()
# e.info()
# d.name = "Divya"
# d.occupation ="HR"

#----Default Constructor----

# class Details:
#     def __init__ (self):
#         print("animal Crab belongs to Crustaceans group")
# obj1 = Details()

#----Decorators-----


# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("Hello World")


# def add(a,b):
#     print(a+b)

# hello()
# greet(add)(1,2)

#====Practical use case====

# import logging 

# def log_function_call(func):
#     def decorated(*args,**kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a,b):
#     return a+ b

#----Getters AND Setters-----

# class MyClass:
#     def __init__(self, value):
#         self._value = value
    
#     def show(self):
#         print(f"Value is {self._value}")
    
#     @property
#     def ten_value(self):
#         return 10 * self._value
    
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10
        
    

# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()


#----Inheritance----

# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"The name of Employee: {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLangugae(self):
#         print("The default language is Python")


# e = Employee("Rohan Das", 420)
# e.showDetails()
# e1 = Employee(" Das", 820)
# e1.showDetails()
# e2 = Programmer("Soniya", 850)
# e2.showLangugae()

#---Access Modifier----
# class Employee:
#     def __init__(self):
#         self.name = "Acc"

# a = Employee()
# print(a.name)

#----Public Access ----

# class Student:
#     def __init__(self):
#         self.name = "Picatchu"
#         self.age = 12

# obj = Student()
# print(obj.age )
# print(obj.name)

#-- Private Acess---

# class Employee:
#     def __init__(self):
#         self.__name = "Emp"

# a = Employee()
# #print(a.__name) # cannot be accessed directly

# print(a._Employee__name) # can be accessed indirectly with maligning

# print(a.__dir__())

#----Protected Modifier----

# class Student:
#     def __init__ (self):
#         self._name ="Harry"
    
#     def _funName(self): # Protected Method
#         return "Code With Harry"
    
# class Subject(Student):  # inherited
#     pass

# obj = Student()
# obj1 = Subject()
# print(dir(obj))

# # calling by object of Student class
# print(obj._name)
# print(obj._funName())

# # calling by object of Subject Class
# print(obj1._name)
# print(obj1._funName())
    

#----Static Method---
# class Math:
#     def __init__(self, num):
#         self.num =num

#     def addtonum(self, n):
#         self.num =self.num + n

#     @staticmethod
#     def add(a,b):
#         a + b

# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

#---Instance Vs Class Variables----


#----Instance Variables----
# class Employee:
#     def __init__(self, name):
#         self.name = name
#         self.raise_amount = 0.2 # instance variables
#     def showDetails(self):
#         print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount}")

# Employee.showDetails(emp1)
# emp1 = Employee("Raj")
# emp1.showDetails()
# emp2 = Employee("Rohan")
# emp2.raise_amount = 0.5
# emp2.showDetails()


#--- class variable 
# class Employee:
#     companyName = "Apple" #---class variable--
#     noOfEmployees = 0
#     def __init__(self, name):
#         self.name = name
#         self.raise_amount = 0.02
#         Employee.noOfEmployees += 1
#     def showDetails(self):
#         print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# # Employee.showDetails(emp1)
# emp1 = Employee("Raj")
# emp1.companyName = "Apple India"
# emp1.showDetails()
# Employee.companyName = "Google"
# print(Employee.companyName)

# emp2 = Employee("Rohan")
# emp2.raise_amount = 0.5
# emp2.companyName = "Nestle"
# emp2.showDetails()  



#----Class Methods----

# class Employee:
#     company ="Tesla"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")

#     @classmethod
#     def changeCompany (cls, newCompany):
#         cls.company = newCompany

# e1 = Employee()
# e1.name =" Rahul"
# e1.show()
# e1.changeCompany("Fire Wicket")
# e1.show()
# print(Employee.company)

#---Class methods as Alternative Constructors---

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary 

#     @classmethod
#     def fromStr(cls, string):
#         return cls(string.split("-")[0], string.split("-")[1])

# e1 = Employee("Raj", 12000)
# print(e1.name)
# print(e1.salary)



# string = "John-12000"
# e2 = Employee.fromStr(string)
# print(e2.name)
# print(e2.salary)
 
#----dir() method----

# x= [1,2,3]
# print(dir(x))
# print(x.__add__)

#__dict__ attribute

# class person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         self.version = 1

# p = person("John", 30)
# print(p. __dict__)

# print(help(person))

# print(help(str))

#----super() keyword---
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Soniya")
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()
# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

# class Programmer(Employee):
#     def __init__(self, name, id, lang):
#          super(). __init__(name, id)
#          self.lang = lang

# rohan = Employee("Rohan Das", "420")
# Soniya = Programmer("Soniya", "2345", "Python")
# print(rohan.name)
# print(Soniya.name)
# print(Soniya.id)
# print(Soniya.lang)


#----Magic/ Dunder method----
# class Employee:
#     name ="Soniya"

#     def __len__(self):
#         i = 0
#         for c in  self.name:
#             i = i + 1
#         return i
#     def __str__(self):
#         return(f"The name of employee is {self.name}")
    
#     def __repr__(self):
#         return f"The name of employee is {self.name} repr"
#     def __call__(self):
#         return f"Hey i am good "

# e = Employee()
# print(e.name)
# print(len(e))
# print(str(e))
# print(repr(e))
# print(e())


#---Method overriding----

# class shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
# class circle(shape):
#     def __init__(self, radius):
#         self.radius =radius

#     def area(self):
#         return 3.14 * self.radius *self.radius

# rec = shape(3,5)
# print(rec.area())

# c= circle(5)
# print(c.area())

#. or can be done as 
# class shape:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def area(self):
#         return self.x * self.y
# class circle(shape):
#     def __init__(self, radius):
#         self.radius =radius
#         super().__init__(radius, radius)

#     def area(self):
#         return 3.14 * super().area() #---super class area method is called 

# rec = shape(3,5)
# print(rec.area())

# c= circle(5)
# print(c.area())


