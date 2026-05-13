'''TUPLES
(1)What is tuple: tuple vs list
(2)unpacking arguments
(3)Zip
'''
print("==== What is tuple: tuple vs list ====")
# Java/php/js => array  -> python list

nums = [4, 6, 3, 6, 43, 6,]

letters = list("Hello world!")

fruits = ["apple", "banana", "cherry", "kiwi"]
print("fruits", fruits)

fruits[2] = "melon"
print(fruits)

# we can't mutate tuple
animals = ("dog", "cat", "lion", "fish")
tuple_obj = ("MIT", 23, True, None)

print(animals[0])
