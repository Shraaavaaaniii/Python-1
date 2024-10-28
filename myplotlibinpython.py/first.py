# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6],color='red')
# plt.xlim(1,5)
# plt.ylim(1,6)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Demo graph')
# plt.legend(['Values'])
# plt.show()

# line plot
# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
# plt.plot(x,y)
# plt.show()

# Scatter plot
# import matplotlib.pyplot as plt
# x = [3,1,3,12,2,4,4]
# y = [3,2,1,4,5,6,7]
# plt.scatter(x,y)
# plt.title("Scatter chart")
# plt.show()

# Bar plot
# import matplotlib.pyplot as plt
# x = [3,1,3,12,2,4,4]
# y = [3,2,1,4,5,6,7]
# plt.bar(x,y)
# plt.title("Bar chart")
# plt.legend(["bar"])
# plt.show()

# horizontal bar plot 
import matplotlib.pyplot as plt
x = [3,1,3,12,2,4,4]
y = [3,2,1,4,5,6,7]
plt.barh(x,y)
plt.title("Bar chart")
plt.legend(["bar"])
plt.show()