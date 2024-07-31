#looping statements,break,continue
t = ("Mogra","Chapha","Jaee")
#for loop to print items in iterable
#iterable can be range(),list,tuple
for i in t:
    print(i)
else:
    print("I am coming out of for loop")
# in while loop we have to initialise variable and also need to increment or decrment accordingly
i = 1
while i<=20:
    print(i,end=" ")
    i+=1
else:
    print("\nI am coming out of while loop")
#break to terminate loop 
print("Odd numbers from 1 to 10 ")
for i in range(1,20,2):
    if(i==11):  #when the value of i becomes 11 it will terminates loop
        break
    print(i,end=" ")
#continue to skip the iteration 
name = "harry" 
for i in name:
    if(i == "r"):  # whenever value of i is r it will skip statement coming after continue
        continue
    print(i,end="")