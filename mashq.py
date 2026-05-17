# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)

# langs = ["JavaScript", "Java"]
# langs.insert(1, "python")
# print(langs)

# fruits = ["banana", "apple", "kiwi"]
# fruits.remove("apple")
# print(fruits)
# fruits.clear()
# print(fruits)

# colors = ["red", "blue", "green", "black"]
# print(colors.index("green"))

# nums = [1, 2, 3, 2, 4, 2, 5]
# print(nums.count(2))

# nums = [5, 1, 8, 2, 9]
# sorted = sorted(nums)
# print(sorted)

# nums = [1, 2, 3, 4, 5]
# nums.reverse()
# print(nums)

# a = [1, 2, 3]
# b = a
# c = a.copy()
# a.append(1)
# print(a)
# print(b)
# print(c)

# TASK
# nums = [4, 1, 7, 1, 9, 1, 3]


# def mix(list):
#     list.remove(max(list))
#     list.sort()
#     list.append(100)
#     return list
# print(mix(nums))

# users = []


# def addUser(user):
#     if len(user) >= 5:
#         users.append(user)
#         print("user qoshildi")
#     else:
#         print("Username kamida 5 ta harf bo'lishi kerak")


# addUser("Kevin")
# addUser("Sevila")
# addUser("Ronaldo")


# def delUser(user):
#     res = users.index(user)
#     if users[res]:
#         users.remove(user)
#         print("User o'chirildi")
# delUser("Kevin")


# nums = [1, 2, 3]

# for i in nums:
#     if len(nums) == 10:
#         print(nums)
#         break
#     else:
#         nums.append(i)

# def test(word):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     result = ""
#     for x in abc:
#         for y in word:
#             if (y == x):
#                 res = (abc.index(y)+7) % 26
#                 result += abc[res]

#     print(result)


# test("mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf")


# def majority(arr):
#     obj = {}
#     for x in arr:
#         if obj.get(x):
#             obj[x] += 1
#         else:
#             obj[x] = 1
#     max = 0
#     result = 0
#     for x, y in obj.items():
#         if y > max:
#             max = y
#             result = x

#     return f"{result} soni {max} marta ishlatildi!"


# print(majority([2, 2]))

# print("====== To-Do list =======")
def addTask():
    while True:
        print("Bosh menuga qaytish uchun 0 ni kiriting!\n")
        str = input("Rejani kiriting>>>")
        if len(str) > 1:
            rejalar.append(str)
            print("Reja muvaffaqiyatli qo'shildi\n")
        elif str == "0":
            break
        else:
            print("Reja kamida 2 ta harf bo'lishi kerak")


def readTask():
    if not rejalar:
        print("\nHali reja mavjud emas!\n")
    else:
        print("Mavjud rejalar:")
        for index, task in enumerate(rejalar, start=1):
            print(f"{index}-{task}")


def delTask():
    try:
        if not rejalar:
            print("\nHali reja mavjud emas!\n")
        else:
            while True:
                print("\nBosh menuga qaytish uchun 0 ni kiriting!\n")
                task = int(input("O'chirmoq bo'lgan taskni tanlang>>>"))
                if task == 0:
                    break
                elif task > len(rejalar) or task < 0:
                    print("\nReja raqami noto'g'ri tanlandi!\n")
                else:
                    del rejalar[task-1]
                    print(f"{task}-reja muvaffaqiyatli o'chirildi!\n")
    except ValueError:
        print("Iltimos,faqat raqam kiriting!")


def updateTask():
    try:
        while True:
            print("\nBosh menuga qaytish uchun 0 ni kiriting!\n")
            req = int(input("Tahrirlamoqchi bo'lgan rejani tanlang!>>>"))
            if req < 0 or req > len(rejalar):
                print("\nReja raqami noto'g'ri tanlandi!\n")
            elif req == 0:
                break
            else:
                res = input("\nYangi rejan nomini kiriting>>>")
                rejalar[req-1] = res
                print("\nReja tahrirlandi!")
    except ValueError:
        print("Iltimos,faqat raqam kiriting!")


rejalar = []
while True:
    print("""
    (1) Reja qo'shish
    (2)Rejani ko'rish
    (3)Rejani o'chirish
    (4)Rejani yangilash
    (5)Chiqish
    """)

    try:
        req = int(input("Menuni tanlang>>>"))
        if req == 1:
            addTask()
        elif req == 2:
            readTask()
        elif req == 3:
            readTask()
            delTask()
        elif req == 4:
            readTask()
            updateTask()
        elif req == 5:
            print("Dastur yakunlandi!")
            break
        else:
            print("Menu raqami noto'g'ri kiritildi!")
    except ValueError:
        print("Iltimos,faqat raqam kiriting!")
