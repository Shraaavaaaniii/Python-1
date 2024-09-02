# from mypackage import arithmeticop,logicalop
# print(mypackage.logicalop.sub(100,200))

# 2.#from mypackage import arithmeticop,logicalop
# print(arithmeticop.add(50,10))
# print(logicalop.OR(2,3))

# 3.
from mypackage.arithmeticop import add  # type: ignore
print(add(80,30))