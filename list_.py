#list
#Printing list elements
# 1.We can print list elements by directly using varialbe name 
# list1 = [1,2,"Shravani",88.90]
# print(list1)
# print(type(list1))

#2.we can print list elements by using for loop
# list2 = ["John","David","James","Jonathan"]
# for i in list2:
#     print(i)

# 1.append(): It is used to add elements in list at the end
# n = int(input("Enter any number : "))
# l = []
# for i in range(0,n):
#     l.append(input("Enter an element : "))
# print("The elements present in list are ",l)

# 2.insert() : It is used add element to the list at any specified position
# l = ["Rohit","Virat","Hardik"]
# l.insert(1,"Dhoni")
# print("List after inserting new element :",l)

# 3.pop() : Removes the element at a specified position and if position is not mention then it will be remove last element from the list
# l = ["Hockey","Tennis","Weight lifting"]
# l.pop() #It will remove the last element
# print(l)
# l.pop(0) #It will remove the element at index 0 from list
# print(l)

# 4.remove():Removes specified element from the list
# l = ['a','b','c','d']
# l.remove('c')
# print(l)

# 5.index(): Returns the index of first occurence of element from the list
# l = ["Mango","Orange","Pineapple","Guava"]
# print(l.index("Pineapple"))

# 6.count() : Returns the count of the element present in the list
# l = [1,2,3,1,4,2,4,1,3,6,1]
# print("Occurence of 1:",l.count(1))

# 7.reverse(): reverse the elements
# l = [1,2,3,4,5,6,7,8]
# l.reverse()
# print(l)

# 8.sort():Sorts elements either in ascending or descending order
# l1 = [2,5,3,1,4]
# l1.sort() #sort in ascending order
# print(l1)
# l1.sort(reverse = True) # sorts element in descending order by using reverse parameter
# print(l1)

# 9.min(): returns the minimum value from the list
# l = ['z','b','h']
# print(min(l))
# 10.max() : returns the maximum value
# print(max(l))  

# 11. clear():delete all the all the items
# l = [1,2,3,4,5,6,7]
# l.clear()
# print(l)

# 12.extends() : Adds item of list at the end of other list
# car = ["Audi","BMW","Maruti"]
# other_car = ["Jaguar","Thar"]
# car.extend(other_car)
# print(car)
# print(car + other_car)  #concate
# print(car*2) #to repeat the content 2 times

#conversion of list to frozen set
list_ = ["Kavya","Geeta","Kalicharan"]
print(list_)
fs = frozenset(list_)
print(fs)