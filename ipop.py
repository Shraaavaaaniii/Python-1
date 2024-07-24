#Program using print() and input()
#format()
amount = 170.7654
print("Amount = ${:.3f}".format(amount))
#end and sep keyword parameter
print('G','F','G',sep='',end='@')
print("\n24","07","2024",sep='-')
#f-string
print(f"You have to pay Rs.{amount}")
#% operator
age = 20
print("My age is %d years"%age)
#input()
name = input("Enter your name : ")
print(name)
#taking more than one inputs using only one input()
x,y = input("Enter two numbers : ").split()
print("First number :",int(x))
print("Second number :",int(y))
#indentation
i = 1
while(i<=5):
    print(i)
    i+=1