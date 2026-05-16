'''COMPREHENSION
    (1)What is comprehension
    (2)set and dict comp.
'''
print("===== What is comprehension & list comprehension =====")
# Comprehension acts like spread operator!
'''Comprehension general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [11, 2, 4, 2, 1, 201]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("ーーーーー")
people = [("Robert", 20),
          ("Steve", 19),
          ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)

print("========")
cars = [("Ferrari", 78),
        ("Tayota", 87),
        ("Audi", 116),
        ("BMW", 109),
        ("'Pagani", 33)]
list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)

print("===== set and dictionary comprehension =====")
numbs = [11, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)
dict_people = {person[0]: person[1] for person in people}  # b version
print("dict_people:", dict_people)
