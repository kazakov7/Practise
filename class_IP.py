'''CLASS DEEP DIVING
    (1)Encapsulation
    (2)Enheritence <
    (2)Polymorphism <
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
