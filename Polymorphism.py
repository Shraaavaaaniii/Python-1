#********************************polymorphism********************************

# 1.function polymorphism
# print(len("Programs"))
# print(len(["Java","C++","Python","C"]))
# print(len({"Name" : "Shravani","Age" : 21}))

# 2.Class polymorphism  : The function with the same name and same number of parameters are defined in the different class(not in derived class)
# class India :
#     def Capital(self):
#         print("New Delhi is the capital of India")

# class USA :
#     def Capital(self):
#         print("Washington D. C. is the capital of USA")

# obj_ind = India()
# obj_usa = USA()

# for i in (obj_ind, obj_usa):
#     i.Capital()

# 3.Method overloading
class Bird:
    def flight(self):   # method which overrided
        print("Most of the birds can fly but some can't")
class Sparrow(Bird):
    def flight(self):
        #parent class method called here
        Bird.flight(self)        
        super().flight() 
        print("Sparrows can fly")

obj = Sparrow()
obj.flight()