# Abstraction in python
from abc import ABC, abstractmethod

class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30 km/hr")

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25 km/hr")

t = Tesla()
t.mileage()
s = Suzuki()
s.mileage()