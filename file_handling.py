#File handling
#to create a new file
# f.write
# f = open("demo",'w')
# f.write("Twinkle Twinkle little star, how I wonder what you are")
f = open("demo",'r')
print(f.read())
print(f.tell())
f.seek(20)
print(f.tell())
f.close()