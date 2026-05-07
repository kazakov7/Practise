# # Dunder __Builtins__, __init__
# message = "Python: everthying is Object "
# print(message)

# result = type(message)
# print("result:", result)

# '''In Python, there a builtin tools:
# (1)Types: int float string list dict
# (2)Functions: print() len() input() type() str() int()
# (3)Contstants: True False None
# '''

# print(dir(__builtins__))


print("≈≈≈≈≈≈ Number≈≈≈≈≈≈≈")
# in Java: variable is a name storage location!
# in Python: variable is named reference!

count = 100
count_type = type(count)
print(f'the count : {count} and type: {count_type}')

result1 = count.bit_count()
result2 = count.numerator
print(result1, result2)
