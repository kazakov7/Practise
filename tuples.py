# '''TUPLES
# (1)What is tuple: tuple vs list
# (2)unpacking arguments
# (3)Zip
# '''
# print("==== What is tuple: tuple vs list ====")
# # Java/php/js => array  -> python list

# nums = [4, 6, 3, 6, 43, 6,]

# letters = list("Hello world!")

# fruits = ["apple", "banana", "cherry", "kiwi"]
# print("fruits", fruits)

# fruits[2] = "melon"
# print(fruits)

# # we can't mutate tuple
# animals = ("dog", "cat", "lion", "fish")
# tuple_obj = ("MIT", 23, True, None)

# print(animals[0])

people = "Andrew", "John"
animal = "dog"

print("====unpacking arguments ====")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print("x", x)
print("y", y)
print("z", z)


def calc(*args):
    print("args>", args)
    total = 1
    for x in args:
        total *= x
    print("the total value: ", total)
    return total


calc(3, 4, 5)
calc(4, 6, 2000)
calc(5, 3, 4, 5, 45, 454, 45, 2)
calc(0)
