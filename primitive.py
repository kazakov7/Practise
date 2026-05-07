# print("≈≈≈≈≈≈ Number≈≈≈≈≈≈≈")
# in Java: variable is a name storage location!
# in Python: variable is named reference!

# count = 100
# count_type = type(count)
# print(f'the count : {count} and type: {count_type}')

# result1 = count.bit_count()
# result2 = count.numerator
# print(result1, result2)

# print("≈≈≈≈≈≈ String ≈≈≈≈≈≈≈")
# # Methods: title() upper() lower() find() replace()

# cource = "AI Python fullstack"
# result = type(cource)
# print(f"the ressult (1): {result} ")

# result = cource.title()
# print(f"the ressult (1): {result} ")

# result = cource.upper()
# print(f"the ressult (1): {result} ")

# result = cource.replace("fullstack", "MasterClass")
# print(f"the ressult (1): {result} ")

print("≈≈≈≈≈≈ Boolean ≈≈≈≈≈≈≈")
# # functions> type() input() bool() int() str()
# y = input("GIve your value for y: ")
# print("y:", y)

# result = y.isnumeric()
# print(f"The input value is numeric: {result}")

# Truthy vs Falsy value
# Truthy: True 100 -100 "Martin"
# Falsy: False 0 " None"

test_falsy = "" or False or None or 0
print("test_falsy:", bool(test_falsy))
test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))
