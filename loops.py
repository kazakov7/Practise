'''
(1)for
(2)break/else
(3)while
'''
print("======= for operator ======")
# Iterable object=>str dict list tuple map filter
text = "MIT"
nums = [2, 3, 5, 3, 3]
obj = dict(brand="Ferrari", year=2025)
range_obj = range(0, 3)

for letter in text:
    print(letter)
print("===========")
for num in nums:
    print(num)
print("===========")
for key in obj:
    print(key, obj.get(key))

for x in range(0, 20, 5):
    print(x)

print("======== break/else ========")
for x in range(0, 20, 5):
    print(x)
    if x > 100:
        print("Reached break")
        break
else:
    print("executed successfully")

print("=====While operator=====")
# num = 40
# while num > 0:
#     num -= 10
#     print(f"the num equals: {num}")

print("==========")
count = 0
while True:
    count += 1
    num = int(input("Find number"))

    if num == 41:
        print(f"You found number in {count} steps!")
        break
    else:
        print("Wrong, please find again")
