class Pet:
    def __init__(self, name, age, health):
        self.name = name
        self.__age = age
        self.__health = health

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def display(self):
        print(self.name, "-", self.get_health())

    def sound(self):
        print("Pet sound")


class Dog(Pet):
    def sound(self):
        print("Woof!")


class Cat(Pet):
    def sound(self):
        print("Meow!")


dog = Dog("Buddy", 3, 80)
cat = Cat("Kitty", 2, 90)

pets = [dog, cat]

for pet in pets:
    pet.display()
    pet.sound()
    pet.set_health(pet.get_health() + 10)
    print("Updated Health:", pet.get_health())
    print()