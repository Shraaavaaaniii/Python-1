# horizontal bar plot 
import matplotlib.pyplot as plt
x = [3,1,3,12,2,4,4]
y = [3,2,1,4,5,6,7]
plt.barh(x,y)
plt.title("Bar chart")
plt.legend(["bar"])
plt.show()