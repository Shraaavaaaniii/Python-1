# Directory handling in python

# 1.mkdir() : to create a directory
import os as o 
# o.mkdir("programs") 

# 2.getcwd() : to get current working directory
# print("String format : ",o.getcwd())
# print("Binary format : ",o.getcwdb())

# 3.rename() : to rename directory
o.rename("Python programs","mypackage")

# 4.chdir() : to change directory
# print("Current directory : ",o.getcwd())
# o.chdir("C:/Users/Rushikesh Patil/Desktop/Python")
# print("Changed directory : ",o.getcwd())

# 5.listdir() : to list out subdirectories
# print("Files and programs present in current working directories are : ",o.listdir())

# 6.rmdir() : to remove directory
# o.rmdir("C:/Users/Rushikesh Patil/Desktop/Python-1/Python programs/hello")

# 7.o.path.isdir()...
# other = "C:/Users/Rushikesh Patil/Desktop/Python-1/Python programs"
# print("Is 'C:\Users\Rushikesh Patil\Desktop\Python-1\Python programs' directory ? ",o.path.isdir(other))