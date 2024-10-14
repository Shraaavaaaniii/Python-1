#*******class******* 
# class demo : 
#     var1 = "Hello"
#     var2 = "Welcome"
#     def display(self) :
#         print('Hi',self.var1)
#         print('Hi',self.var2)
# obj = demo()            #object created
# print(obj.var1)
# print(obj.var2)
# obj.display()

#*****constructor******

#1.Default constructor
# class demo :
#     def __init__(self) :
#         print('I am inside the constructor')
# obj = demo()

#2. Parameterized constructor
# class hello :
#     #constructor defined
#     def __init__(self,name):
#         self.name = name
#     def display(self) :
#         print('My name is',self.name)
# o = hello("Ritesh")  
# o.display()

#*******super() in python********
# class Animal :
#     def __init__(self):
#         print("Animal is running")
# class Dog(Animal) :
#     def __init__(self):
#         print("Dog is barking")
#         super().__init__()
# obj = Dog()


# inheritance 
# # Parent class created
# class Parent :
#     def __init__(self,fname,lname) :
#         self.fname = fname
#         self.lname = lname
#     def display(self) :
#         print(self.fname,self.lname)
# #Child class
# class Child(Parent) :
#     def __init__(self,fname,lname,city):
#         super().__init__(fname,lname)
#         self.city = city
#     def displayDetails(self):
#         print("Name :",self.fname,self.lname,"\nCity :",self.city)

# #object of child class created
# obj = Child("Shravani","Patil","Kolhapur")
# obj.display()
# obj.displayDetails()

# Multilevel inheritance
class Person:
    def __init__(self,name,city):
        self.name = name
        self.city = city
    
class Student(Person):
    def __init__(self,name,city,roll):
        super().__init__(name,city)
        self.roll = roll

class Graduate:
    def __init__(self,name,city,rollno,year):
        super().__init__(name,city,rollno)
        self.year = year
    def show(self) :
        print("Hello my name is",self.name,"and I am from",self.city,"roll number",self.rollno)

obj = Graduate("Shravani Patil","Kolhapur",5,2024)
obj.show()