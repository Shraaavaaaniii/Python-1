class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("The person name is",self.name,"and person age is",self.age)

class Student(Person):
    def __init__(self,name,age,dob):
        self.sName = name
        self.sAge = age
        self.dob = dob
        super().__init__("Shravani",21)
    def displayInfo(self):
        print(f"*****Student information *****\nName : {self.sName}\nAge : {self.sAge}\nDOB : {self.dob}",)

obj = Student("Shree",50,"30/09/2004")
obj.info()
obj.displayInfo()