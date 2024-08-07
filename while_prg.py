# while loop program

#1.python program to print natural numbers from 1 to n
# n = int(input("Enter any natural number : "))
# i = 1
# while i<=n:
#     print(i,end=" ")
#     i+=1

# 2.python program to print all the even numbers from 1 to n
# n = int(input("Enter any natural number : "))
# i = 1
# print("Even numbers from 1 to",n)
# while i<=n:
#     if i%2==0:
#         print(i,end=" ")
#     i+=1

# 3.Odd numbers from 1 to n
# n = int(input("Enter any number upto which you want to print odd numbers : "))
# i = 1
# while i<=n:
#     if i%2!=0:
#         print(i,end=" ")
#     i+=1

# 4.Some of n natural numbers
# n = int(input("Enter any number : "))
# sum = 0
# i = 1
# while i<=n:
#     sum = sum+i
#     i+=1
# print("Sum of natural numbers from 1 to",n,"=",sum)

#5.some of odd numbers from 1 to n
# n = int(input("Enter any natural number : "))
# sum = 0
# i = 1
# while i<=n:
#     if i%2 != 0:
#         sum = sum + i
#     i+=1
# print("sum of odd numbers from 1 to",n,"=",sum)

# 6.Some of even numbers from 1 to n
# n = int(input("Enter any natural number : "))
# sum = 0
# i = 1
# while i<=n:
#     if i%2 == 0:
#         sum = sum + i
#     i+=1
# print("sum of odd numbers from 1 to",n,"=",sum)

# 7.python program to print numbers from 1 to n in reverse
# n = int(input("Enter any natural number : "))
# i = n
# print("Numbers from 1 to",n,"in reverse order")
# while i>=1:
#     print(i,end=" ")
#     i-=1

# 8.Python program to print fibonacci series up to n
# a = 0
# b = 1
# n = int(input("Enter any number upto which you want to print fibonacci series : "))
# print("Fibonacci series up to",n,": ",a,b,end=" ")
# while True:
#     fibo = a+b
#     if fibo <= n:
#         print(fibo,end=" ")
#         a = b
#         b = fibo

# 9.Python program to find factorial of given number
# fact = 1
# n = int(input("Enter any number : "))
# i = n
# if n == 0:
#     print("Factorial of zero is one")
# else:
#     while i>0:
#         fact = fact * i
#         i -= 1
#     print("Factorial of",n,"is",fact)

# 10.Python program to find given number is prime or not
# n = int(input("Enter any number to find whether it s prime or not : "))
# c = 0
# i = 2
# while i < n:
#     if n%i == 0:
#         c+=1
#         break
#     i+=1
# if c == 0:
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")

# 11.Python program to find sum of digits of given number
# n = int(input("Enter any number :"))
# sum = 0
# while n > 0:
#     sum += n%10 
#     n = n//10
# print("Sum of all digits in the number is",sum)

# 12.Write a python program to find the given number is palindrom or not
# n = int(input("Enter any number : "))
# t = n
# rev = 0
# while n > 0:
#     rev = (rev * 10) + (n%10)
#     n = n//10
# if t == rev:
#     print(t,"is palindrom number")
# else:
#     print(t,"is not a palindrom number")

# 13.Write a python program to reverse a given number
# n = int(input("Enter any number : "))
# t = n
# rev = 0
# while n > 0:
#     rev = (rev * 10) + (n%10)
#     n = n//10
# print("Reverse number is",rev)

# 14.Python program to print multiplication table
# n = int(input("Enter any number of which you want an mutiplication table : "))
# i = 1
# print("--- Table of %d ---"%n)
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# 15.Python program to find largest of n numbers
# n = [34,78,10,5,90,46]
# i = 0
# max = n[i]
# while i<len(n):
#     if n[i]>max:
#         max = n[i]
#     i+=1 
# print("Largest umber ffrom given list is",max)

# 16.Python program to find smallest number from n number
# a = [10,40,33,2,55,59]
# i = 0
# min = a[1]
# while i < len(a):
#     if min > a[i]:
#         min = a[i]
#     i+=1
# print("Smallest number from list is",min)