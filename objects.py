'''OBJECTS
(1)What is object
(2)Iterable objects & Range
(3)Dictionary
(4)error handling system
'''

import array
import math
from math import ceil
print("======= What is Object ======")
# An object has state and method properties
# Everything is object in Python!

print(type("Hello world"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# Paradigm> Functional Programming & OOP
# OOP 4 concepts> Abstraction, Encapsulation, Inheritence, Polimorphism
result1 = math.ceil(97.7)
print("result1:", result1)

result2 = math.ceil(98.7)
print("result2:", result2)


result3 = math.ceil(0.7)
print("result3:", result3)
