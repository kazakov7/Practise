'''CLASS DEEP DIVING
    (1)Encapsulation
    (2)Enheritence <
    (2)Polimorphism <
'''


print("========= Inheritence =========")
# Enheritence=> PARENT > CHILD
# Parent only provides only Public & proteced properties( state + methods ) to children!


class Animal:
    description = "The class creates animals"

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"The animal can make voice: {self.voice}")


class Dog(Animal):  # child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"The {self.name} says: {self.sound}")


class Cat(Animal):  # child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        pass


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "Zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----------")
dog.make_voice()
fish.make_voice()

print(dog.voice)

print(dog.status)
print(cat.status)

print("========= Polimorphism =========")
dog.make_voice()
fish.make_voice()
print("-------")
# fish>Fish>Animal>object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print("result:", result)
# fish>Animal>object
data = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("result: ", data, data2)
