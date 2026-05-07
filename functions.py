'''Functions
(1)Define vs Call
(2)Parametr vs Argument
(3) Keyword & default argument
(4)Scope
'''
print("≈≈≈ Deifne (parametr) vs Call (arguemnt) ≈≈≈≈")
# build in function > print() type()
# Function: reusable block of code
# Instead of block {} in java, Python uses intentation

# Define (parametr)


# def greet(a):
#     print("How are you,", a)


# def greeting(b):
#     print("How are you,", b)
#     return f"Hi {b}"


# # CALL - argument
# result1 = greet('Martin')
# print("result1:", result1)

# result2 = greeting("Justin")
# print("result2:", result2)

print("≈≈≈ Keyword & default arguments ≈≈≈≈≈≈")
# Define


def give_greet(name, age=22):
    print("Executed give_greet function")
    return f"Hi {name}, you are {age} years old"


# call
result3 = give_greet(name='Justin', age=23)
print("result1:", result3)

# call
result3 = give_greet(name='John')
print("result1:", result3)
