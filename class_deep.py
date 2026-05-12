'''CLASS DEEP DIVING
    (1)Encapsulation
    (2)Enheritence
    (2)Polymorphism
'''


print("========= Encapsulation =========")
# Encapsulation> public,privite,protected


class Account():
    description = "The class makes bank accounts"

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    def get_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} usd!")

    def deposit(self, amount):
        print("Deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()
print("================")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("================")


try:
    result = my_account.owner
    print("Result:", result)
except Exception as err:
    print("NO target state found", err)
my_account.holder = "Martin"
print(my_account.holder)
