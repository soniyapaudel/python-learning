# print("Hello world", 7 )
# print(5)
# print("Bye")
# print(17*13)
# ---- do not remove this line ---
# print("hi soni \n  python is python and it is python and everywhere it only pythy pyes ")
# ''' This is the way to write the multi line comments in python
# have you known this
# or not
# '''

# """ this is also another way of
# representing multi line comments
# """

# #-------Escape sequwnce character-------
# print('Hey i am\'a\"good girl\"\n and this viewer is also good /girl')
# print('me\t mine')
# print("Hey", 6, 7, sep="~", end="009\n")
# print("Soniyo")


# ------Variables------
# a = 12345234567894589
# b = "python"
# c = True
# d = "None"


# ------ Data types------
# ------numeric: complex----
# e = complex(3, 3)
# print(e)

# ---- numeric => integer-----
# print(type(a))

# ------ numeric: string--------
# print(type(b))

# -------numeric => Boolean------
# print(type(c))

# ------numeric => string------
# print(type(d))

# -------list --------
# list1 =[8, 2.3, [-4,5], ["apple", "banana"] ]
# print(list1)
# print(type(list1))

# -----Tuple--------
# tuple1 = (("parrot", "sparrow"),("lion","Tiger"))
# print(tuple1)
# print(type(tuple1))

# ------Dictionary--------
# dict1 ={"name":"Soniya", "age": "23", "Can Vote":"True"}
# print(dict1)
# print(type(dict1))

# # operator

# print(5+6)
# print(15-6)
# print(15*6)
# print(15/6)
# print(15//6)
# print(5%3)
# print(2**4)


# -----Type Casting / Type Conversion-----

# ------Explicit TYpe Casting-----
# string ="15"
# number =7
# string_number = int(string)
# sum = number + string_number
# print("The sum of both the numbers is:", sum)


# -------Implicit Type Casting-------

# python automatically converts a to int

# a=7
# print(type(a))

# # python automatically converts b to float
# b = 3.0
# print(type(b))

# #python automatically converts c to float as it is float addition

# c= a+b
# print(c)
# print(type(c))

# input from user
# a = input("Enter your name:")
# print("My name is", a)

# x = input("Enter first number:")
# y= input("Enter second number:")
# print(x + y) # here the output is 243 because python is doing string concatenation, not addition

# print(int(x) + int(y))

# -----Strings----
# name ="Soniya"
# friend =" Bimala "
# anotherFriend = 'Prasamsha'


# print("Hello, " + name)
# print("Hello, " + friend)
# print("Hello," + anotherFriend)

# # Multiline Strings
# a ="""Lorem ipsum
# Great! You’re doing everything RIGHT — learning Python basics and wanting to start real projects + push them to GitHub.
# I’ll give you the best FREE learning + project roadmap that matches your level (Day 11 beginner) and will prepare you for jobs.
#  """
# print(a)

# apple="green"
# print(apple)
# print(apple[0])
# print(apple[1])
# print(apple[2])
# print(apple[3])
# print(apple[4])
# print(apple[5]) This throws a error because there is no value in the array 5 of the variable apple
# print(apple[6])  This throws a error because there is no value in the array 6 of the variable apple

# ------String Slicing-------
# names =" Marrie, Carrie"
# print(names[0:5])
# print(len(names))

# fruit = "Mango"
# len1 =len(fruit)
# print("Mango is a", len1, "Letter word")
# mangoLen = len(fruit)
# print(fruit[0:4])
# print(fruit[1:4])
# print(fruit[:5])
# print(fruit[:-3]) # why the output Ma comes when we didi negative slicing so len of fruit is 5 and 5-3 means 2 so the
# print(fruit[:len(fruit)-3])
# print(fruit[-1:len(fruit)-3]) # it doesnot give output

# --- Loop through a String ----

# alphabets = "ABCDE"
# for i in alphabets:
#     print(i)

# ----Quick Quiz----

# nm = "Soniya"
# print(nm[-4:-2])


# ---String Method---

# a="Soniya"
# print(len(a))
# print(a.upper())
# print(a.lower())

# ----Strip Method----
# str1 = " Silver Spoon "
# print(str1.strip())


# -----rstrip() method

# str2 = "Hello!!!##"
# print(str2.rstrip("!")) #  here rstrip doesnot remove "!" since "#" is present at the end which stops the stripping
# print(str2.rstrip("!#"))

# ---replace()----

# str2="Silver Spoon"
# print(str2.replace("Sp", "M"))

# -----Split()----

# str2="Silver Spoon"
# print(str2.split(" "))

# -----Capitalize()-----
# str1 ="hello"
# capStr1 = str1.capitalize()
# print(capStr1)

# blogHeading ="introduction to python programming"
# print(blogHeading.capitalize())

# str2 ="hello WorlD"
# print(str2.capitalize())

# ----Center()------
# str1 = "Welcome to the Console"
# print(str1.center(50))

# ----count()-----
# str2 = "Abracadabra"
# print(str2.count("a"))
# print(str2.count("A"))
# print(str2.count("r"))


# ---endswith()----

# str1 = "Welcome to soniya world, a cutie pie  @#@#@@"
# print(str1.endswith("@"))
# print(str1.endswith("!"))

# ----find()-----

# str1="The name is John Doe. He is an honest man "
# print(str1.find("is"))

# ---isalnum()----
# str1 =" welcome To the console"
# print(str1.isalnum())

# str2 ="WelcomeToTheConsole"
# print(str2.isalnum())

# ----isalpha()----
# str1 ="welcome"
# print(str1.isalpha())

# str2 ="welcomw00"
# print(str2.isalpha())

# ---islower()----
# str = "welcome to the kingdom of soniya"
# print(str.islower())

# str4 = "WelCoMe"
# print(str4.islower())


# -----isprintable()---
# text ="We wish you a Merry Christmas"
# print(text.isprintable())

# text2 ="Welcome to hello \nworld"
# print(text2.isprintable())


# ---isspace()-----
# text1 ="      " # using space bar
# print(text1.isspace())
# text2 ="    "   # using tab
# print(text2.isspace())

# text3 ="..          " # using tab and some .
# print(text3.isspace())


# ---istitle()----

# text =" World Health Organization"
# print(text.istitle())

# text1 ="Soniya is cutie"
# print(text1.istitle())

# ----isupper()----
# text="WORLD HEALTH ORGANIZATION"
# print(text.isupper())

# ---replace()
# text ="Python is the Compiled Language"
# print(text.replace("Compiled", "Interpreted"))


# --- startswith()----
# str ="Python is a programming language"
# print(str.startswith("Python"))

# ---swapcase()-----

# text ="Python Is a Interpreted Language"
# print(text.swapcase())

# ---title()----
# str = "His name is john doe. john is cutie pie"
# print(str.title())

# --if-else statement----
# a = int(input("Enter your age:"))
# print("Your age is:",a)

# if(a>18):
#     print("You can drive")

# else:
#     print("You cannot drive")

# applePrice = 210
# budget = 200
# if(applePrice <= budget):
#     print("Siri!, put 1 kg Apples into cart")
# else:
#     print("Siri!, do not add Apples in cart")


# -----Elif----

# num = int(input("Enter the value of num:"))
# if(num < 0):
#     print("Number is negative")
# elif(num == 0):
#     print("Number is 0")
# elif(num == 999):
#     print("Number is special")
# else:
#     print("Number is positive ")


# ---- Nested If Statement -----
# num = int(input("Enter the number you want to check:"))
# if(num < 0):
#     print("Number is negative.")
# elif(num > 0):
#     if(num <=10):
#         print("Number is between 1-10")
#     elif(num >10 and num <=20):
#         print("Number is between 11-20")
#     else:
#         print("Number is gretaer than 20")
# else:
#     print("Number is zero")


# ---Match Statement----
# x = int(input("Enter the value of x:"))

# match x:
#     case 0:
#         print("X is Zero")
#     case 4:
#         print("case is 4")
#     case _:
#         print(x)


# x = 4 #5 #11
# match x:
#     case 0:
#         print("X is Zero")
#     case 4 if x% 2 == 0:
#         print("X%2 == 0. and case is 4")
#     case _ if x<10:
#         print("x is < 10")
#     case _:
#         print(x)


# -----For loop----------
# ---Iterating over string---
# name ="Poonam"
# for i in name:
#     print(i, end =",")
#     if(i=="o"):
#         print("This is something special")

# --- Iterating over list----

# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# ----range() function-----

# for k in range(5):
#     print(k)

# for k in range(5):
#     print(k+1)


# for k in range(1,9):
#     print(k )

# name ="Soniya"
# for i in range(100):
#     print(name)

# --- 3rd parametr in range---

# for i in range(1, 11,2 ):
#     print(i)

# ---While Loop ------

# count = 5
# while(count > 0):
#     print(count)
#     count = count-1

# i = int(input("Enter the number:"))
# while(i<=38):
#     i = int(input("Enter the number:"))
#     print(i)
# print("Done with the loop")


# ----Else with while loop-----

# x = 5
# while(x > 0):
#     print(x)
#     x =x-1
# else:
#     print('counter is 0')


# --- Do while loop emulate in python -----

# while True:
#     number = int(input("Enter a positive number:"))
#     print(number)
#     if not number > 0:
#         break

# ------break-----

# break statement totally breaks the loop
# for i in range(12):
#     if(i==10):
#         break
#     print("5 X", i+1, "=", 5 * (i+1))
# print("break the loop")


# ---- Continue Statement

# ---continue statement break the iteration-----

# for i in range(12):
#     if(i== 10):
#         print("Skip the iteration")
#         continue
#     print("5 X", i, "=", 5*i)


# ----Break statement with while loop
# i = 0
# while True:
#     print(i)
#     i = i+1
#     if(i%100 == 0):
#         break


# ----Functions in Python -----


# def calculateGmean(a,b):
#     mean = (a*b)/ (a+b)
#     print(mean)

# a= 9
# b = 10
# c=15
# d=19
# calculateGmean(a,b)
# calculateGmean(c,d)


# def isGreater(a,b):
#     if(a>b):
#         print("First number is greater")
#     else:
#         print("Second number is greater or equal")


# a=9
# b=125

# isGreater(a,b)


# --------Function Argument-------


# ------ Default Argument-----
# def average(a=9, b=1):
#     print("The average is:", (a+b)/2)

# average()

# def name(fname, mname="John",lname="Doe"):
#     print("Hello", fname, mname, lname)


# name("Amy")


# ---------Keyword Argument-----
# def name(fname,mname,lname):
#     print("Hello", fname,mname,lname)

# name(mname="Peter", lname="Wesker", fname="Jade")


# ------Required Argument-----

# def name(fname, mname,lname):
#     print("hello", fname,mname,lname)

# name("peter","john", "Quilt")


# ----Variable length Arguments------
# ---Arbitary Arguments -----

# def name (*name):
#     print("Hello", name[0], name[1], name[2])


# name("john","Baroque","Byzantine")


# def average(*numbers):
#     #print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is:", sum / len(numbers))

# average(5,6,7,8,9)


# keyword Arbitary argument----

# def name(**name):
#     print("hello", name["fname"],name["mname"],name["lname"])

# name(mname="Ram", lname="Sita", fname="Hanuman")


# ----return Statement-----

# def name(fname,mname,lname):
#     return "Hello," + fname + " " + mname + " " +lname

# print(name("James", "Burrito", "Avocado"))

# -----List---------------

# lst1 = [3,5,7,2]
# lst2 =["Blue", "Green", "Red", "Yello"]


# print(lst1)
# print(lst2)
# print(type(lst1))
# print(lst1[0])
# print(lst1[1])
# print(lst1[2])
# print(lst1[3])

# --- A List cana contain different data types-------

# details =["Abhijeet", "BSC.CSIT", 2075, 25 ]
# print(details)

# --- checking item is present in list or not----

# colors = ["Red", "Green", "Yellow", "Blue"]
# if "Yellow" in colors:
#     print("yellow is present.")
# else:
#     print("Yellow is not present")

# colors = ["Red", "Green", "Yellow", "Blue"]
# if "6" in colors:
#     print("6 is present in colors.")
# else:
#     print("6 is not present.")


# ---- Range of index-----

# animals=["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])
# print(animals[-7:-2])


# #---Printing element from a given index till end-----
# animals=["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[4:])
# print(animals[-4:])

# #---printing all element from start to a given index-----

# animals=["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[:6])
# print(animals[:-3])

# ----Printing alternate values----
# animals=["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[::2]) # using positive indexes
# print(animals[-8:-1:2]) #using negative indexes

# ---printing every 3rd consecutive value within a given range----

# animals=["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[1:8:3])

# -----List comprehension----

# ----Accepts items with the small letter "o" in the new list----
#
# names=["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_o = [item for item in names if "o" in item]
# print(namesWith_o)

# ---Accepts item which have more than 4 letters----
# names=["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_o = [item for item in names if (len(item) >4) ]
# print(namesWith_o)

# -----List Method in Python------

# ---list.sort() => sort list in ascending order
# colors = ["voilet", "indigo", "blue", "green" ]
# colors.sort()
# print(colors)

# num = [4,2,1,2,6,10,19,6,3,4,1,2]
# num.sort()
# print(num)

# What if i wnat to sort list in descending order ?
# ---- Then just pass reverse =True as parameter
# colors = ["voilet", "indigo", "blue", "green" ]
# colors.sort(reverse = True)
# print(colors)


# -----Reverse Method----

# colors = ["voilet", "indigo", "blue", "green" ]
# colors.reverse()
# print(colors)

# ---Index method----
# colors = ["voilet", "indigo", "blue", "green" ]
# print(colors.index("green"))

# ----Count method----
# colors = ["voilet","green", "indigo", "blue", "green" ]
# print(colors.count("green"))

# ----Copy method----
# colors = ["voilet","Purple", "indigo", "blue", "green" ]
# newlist = colors.copy()
# print(colors)
# print(newlist)

# ----append method---
# colors = ["voilet", "indigo", "blue", "green" ]
# colors.append("Purple")
# print(colors)

# ---insert method
# colors = ["voilet", "indigo", "blue", "green" ]
# colors.insert(1,"pink")
# print(colors)

# ----Extend method----
# colors = ["voilet", "indigo", "blue", "green" ]
# rainbow=["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)

# ----concatenating two lists----
# colors = ["voilet", "indigo", "blue", "green" ]
# colors2 =["green", "yellow", "orange", "red"]
# print(colors +colors2)

# ----Tuples in python ----
# ---Tuples are immutable

# tuple1 = (1,2,2,3,5,4,6)
# tuple2 =("Red", "Green","blue")
# print(tuple1)
# print(type(tuple2))
# print(tuple1)
# print(type(tuple2))

# tuple3 = ("soniya",)
# print( tuple3)
# print(type(tuple3))

# details = ("Abhijeet", 18,"bsc.it", 9.8)
# print(details)

# print(tuple2[2])
# print(len(tuple2))

# if "Green" in tuple2:
#     print("Green is present")
# else:
#     print("Green is not present")


# ----Printing elements within aparticular range ----

# animals=("cat", "dog","bat","mouse","pig","horse","donkey","goat","cow")
# print(animals[3:7])
# print(animals[-7:-2])


# ----printing all elements from a given index till end
# animals=("cat", "dog","bat","mouse","pig","horse","donkey","goat","cow")

# print(animals[4:])
# print(animals[4:])

# ---Printing all elements from start to a given index
# animals=("cat", "dog","bat","mouse","pig","horse","donkey","goat","cow")
# print(animals[:6])
# print(animals[:-3])


# ---- print alternate values---
# animals=("cat", "dog","bat","mouse","pig","horse","donkey","goat","cow")

# print(animals[::2])
# print(animals[-8:-1:2])

# ---printing every 3rd consecutive within given range----

# animals=("cat", "dog","bat","mouse","pig","horse","donkey","goat","cow")
# print(animals[1:8:3])


# ----- Manipulating Tuples----

# countries =("Spain", "Italy", "India", "England", "Germany")

# temp = list(countries)
# temp.append("Russia") # add item
# temp.pop(3) # remove item
# temp[2]="Finland" # change item
# countries = tuple(temp)
# print(countries)

# countries =("Pakistan", "Afghanistan", "Bangladesh", "Srilanka")
# countries2 = ("Vietnam", "India","China")
# southEastAsia = countries + countries2
# print(southEastAsia)

# ----count() method----

# tuple1 = (0,1,2,3,3,4,2,3,3,9,6,5)
# res = tuple1.count(3)
# print("count of 3  in tuple1 is:", res)

# tuple1 = (0,1,2,3,31,4,2,3,3,9,6,5)
# res = tuple1.index(3,4,8)
# print("index of 3  in tuple1 is:", res)
# print(len(tuple1))

# -----String formatting in python ---

# letter = "Hey my name is {} and I am from {}"
# country = "Nepal"
# name="Soniya"

# print(letter.format(name, country))

# print(f"Hey my name is {name} and I am from {country}")

# val = 'Geeks'
# print(f"{val} for {val} is a portal for {val}.")
# name= 'Tushar'
# age= '23'
# print(f"Hey my name is {name} and I'm {age} years old.")

# txt = "For only {price:.2f} dollars"
# print(txt.format(price =49))

# --- f string can be used in a single statement----

# print(type(f"{2 *30}"))

# ----DocString in Python----

# def square(n):
#     ''' Takes in a number n, return the square of n'''
#     print(n ** 2)
# square(5)
# print(square.__doc__)

# ----Recursion in python---

# def factorial(num):
#     if(num ==1 or num == 0):
#         return 1
#     else:
#         return(num * factorial(num-1))


# num = int(input("Ente the number you want to calculate factorial:"))
# print("Number is:", num)
# print("Factorial:", factorial(num))

# ---sets in Python---

# info ={"Carla", 19, False, 5.9, 19}
# print(type(info))

# #----Empty set----
# set = {","} # or can be create as
# #set()
# print(type(set))

# ---Accessing set using for loop---
# info ={"Carla", 19, False, 5.9, 19}
# for item in info :
#     print(item)


# ---Set Methods()-----
# ----union and update()-----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# cities.update(cities2)
# print(cities)

# ---Intersection and intersection_update()----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3=cities.intersection(cities2)
# print(cities3)
# cities.intersection_update(cities2)
# print(cities)

# ----symmetric difference  and symmetric difference update---

# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)
# cities.symmetric_difference_update(cities2)
# print(cities)


# ----difference and difference_update----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.difference(cities2)
# print(cities3)

# print(cities.difference(cities2))

# ---isdisjoint()
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# print(cities.isdisjoint(cities2))

# ---issuperset()----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# print(cities.issuperset(cities2))

# cities3 = {"Seoul", "Madrid", "kabul"}
# print(cities.issuperset(cities3))

# ----issubset()----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo","Seoul","Kabul","Madrid"}

# print(cities2.issubset(cities))

# -----add()-----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities.add("helsinki")
# print(cities)

# ---remove()/discard----

# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# ---pop()----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# items = cities.pop()
# print(cities)
# print(items)

# ---del----
# ---del is not a method it is keyword which deletes the set entirely---

# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)
# --- got Name Error as output becaus etrhe set is deleted entirely

# ---clear()----
# cities = {"Tokyo","Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

# ---check if item exists----

# info ={"carla", 19,False, 5.9}
# if "carla" in info :
#     print("carla is exist")
# else:
#     print("carla is not exist")

# ----Dictionaries in Python ---

# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# print(info)

# ---Accessing Single Value----
# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# print(info['name'])
# print(info.get('eligible'))

# ---Accessing MUltiple Values----

# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# print(info.values())
# print(info.keys())
# for key in info.keys():
#     print(f"The value coreesponding to the key {key} is {info[key]}")

# ---Acessing key-value pairs----
# print(info.items())


# ----udate()-----
# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# print(info)
# info.update({'age': 20})
# info.update({'DOB' :2002})
# print(info)

# ----clear method----

# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# info.clear()
# print(info) #--- empty dictionary {} output aauxa

# print(info.clear()) # None output aauxa


# ----pop() method---

# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# info.pop('eligible')
# print(info)


# ---popitem()----
# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# info.popitem()
# print(info)

# info ={ 'name' : 'Zakir', 'age' : 19, 'eligible': True}
# del info['age']
# print(info)

# ---for loop with else----

# for i in range(5):
#     print(i)

# else:
#     print("Sorry no i")

# for i in range(6):
#     print(i)
#     if i == 4:
#         break
# else:
#     print("Sorry no i")

# for x in range(5):
#     print("iteration no {} in for loop".format(x+1))
# else:
#     print("else block in loop")
# print("Out of loop")

# ----Exception  Handling/Error handling----

# a = input("Enter The number:")
# print(f"Multiplication table of {a} is:")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid Input!")
# print("Some imp lines of code")
# print("End of program")

# try:
#     num =int(input("Enter an integer:"))
# except ValueError:
#     print("Number entered is not an integer")

# try:
#     num =int(input("Enter an integer:"))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer")
# except IndexError:
#     print("Index Error")


# -----Finally Keyword in python----
# --- important example----
# def func1():
#     try:
#         l =[5,6,7,1]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occurred")
#         return 0
#     finally:
#         print("I am always executed")

# x = func1()
# print(x)


# -----Raising custom errors in python----

# a = int(input("Enter any value between 5 and 9 :"))
# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

# a = int(input("Enter any value between 5 and 9 :"))
# if(a<5 or a>9):
#     quit()

# -----Enumerate function-----
# marks = [12, 56, 32, 98, 1, 4, 45]
# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Sunna, awesome!")
#     index +=1

# marks = [12, 56, 32, 98, 1, 4, 45]

# for index, mark in enumerate (marks):
#     print(mark)
#     if(index == 3):
#         print("Sunna, awesome!")


# fruits = ['apple', 'banana', 'mango']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)


# -----Changing the start index---

# fruits =['apple', 'banana', 'mango', 'orange']

# for index, fruit in enumerate(fruits, start =1):
#     print(index, fruit)

# ---How import works in python---

# import math
# result = math.sqrt(9)
# print(result)

# ---From keyword---
# ---multiple function---

# from math import sqrt, pi
# result = sqrt(9)*pi
# print(result)
# print(pi)


# ---from math import *

# from math import *
# result = sqrt(16)
# print(result)
# print(pi)

# ---as keyword---
# import math as m
# result = m.sqrt(9)
# print(result)

# ----The dir Function----
# import math
# print(dir(math))
# print(math.nan, type(math.nan))

# --- importing fro another file----
# from soniya import welcome, soniya

# welcome()
# print(soniya)

# from soniya import *
# welcome()

# import python

# python.welcome()

# -----Local and Global Variable----

# x = 4
# print(x)

# def hello():
#     x=7
#     print(f"The local x is {x}")
#     print("hello soni")

# print(f"The global x is {x}")
# hello()
# print(f"The global x is {x}")


# -----global keyword----
# x = 10
# def my_func():
#     global x
#     x=5

#     y=9

# my_func()
# print(x)

# ---- File Handling/ i/o handling----

# ---Read from the files
# f = open('files.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# --- Write method in files----

# f = open('files.txt', 'w')
# f.write('Hello! world')
# f.close()

# ----Append in file---

# f = open('files.txt', 'a')
# f.write('Hey you know your text were overwritten by wtite method which you write previous things the message to soniya for her python learning journey now i am appending this in that journey  ')
# f.close()

# ----- Closing a file------

# f = open('files.txt', 'a')
# f.close()

# --- With statemnet for closing file without using f.close()---

# with open('files.txt', 'a') as f:
#     f.write("\n hey I am inside with")


# -----readline() method-----

# f = open('myfile.txt','r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of student {i} in maths is: {m1}")
#     print(f"marks of student {i} in English is: {m2}")
#     print(f"marks of student {i} in Nepali is: {m3}")

#     print(line)

# ---Writelines() method------

# f= open('myfile2.txt','w')
# lines =['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# ----seek() functions----

# with open('file.txt','r') as f:
#     #-- move to the 10th byte to the file
#     f.seek(10)
#     #--- read the next 5 bytes
#     data = f.read(5)
#     print(data)


# --- tell() function---
# with open('file.txt', 'r') as f:

#     # Read the first 10 bytes
#     data = f.read(10)

#     # Save the current Position
#     current_position = f.tell()

#     # Seek to the Saved position
#     f.seek(current_position)

#     print(data)

# --- Truncate() function ----

# with open('sample.txt', 'w') as f:
#     f.write("Soniya!")
#     f.truncate() # pass argument here
#     f.truncate(3)
# with open('sample.txt', 'r') as f:
#     print(f.read())


# --- lambda function ----
# def double(x):
#     return x*2

# print(double(5))

# double = lambda x: x*2
# cube = lambda y : y*y*y
# avg = lambda x, y, z: (x+y+z)/ 3

# print(cube(4))
# print(double(5))
# print(avg(3,5,10))

# #--- we can pass functiom to function like below
# def appl(fx, value):
#     return 6 + fx(value)

# print(appl(cube, 2))
# print(appl(lambda x: x*x*x, 2))


# ---- Map() function -----

# def cube(x):
#     return  x*x*x

# print(cube(2))

# l = [1,2,4,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

# def cube(y):
#     return y*y*y

# print(cube(2))

# l= [1, 2, 4, 6, 8, 9]

# newl = list(map(cube, l))
# print(newl)


# numbers = [1,2,3,4,5]
# doubled = map(lambda x: x*2, numbers)
# print(list(doubled))

# --- Filter---
# def cube(y):
#     return y*y*y

# print(cube(2))
# l = [1, 2, 4, 6, 8, 9]
# newl = list(map(cube, l))
# print(newl)

# def filter_function(a):
#         return a>2

# newnewl = list(filter(filter_function, l))
# print(newnewl)

# ----Reduce Function-----

# from functools import reduce

# numbers = [1,2,3,4,5]
# sum = reduce(lambda x,y: x+y, numbers)

# print(sum)

# --- is vs == -----

# a =[1,2,43]
# b = [1,2,43]

# print( a is b)# exact location of object in memory
# print(a == b) #value

# c = 4
# d ="4"
# print( c is d)
# print( c == d)


