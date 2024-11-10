#types of functions

#1.default arguments :
def average(a=5,b=10):
    print((a+b)/2)
average(b=5) 

#2.required arguments :
def name(fname,mname,lname):
    print("hello",fname,mname,lname)
name("Shravani","Uday","Patil")

#3.variable length arguments:
def sum(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
    print(sum)
sum(4,5)
sum(10,59,1)  