class Human:
    def __init__(self, name):
        print("human initialized")
        self.name = name
        
    def say_hello(self):
        print(f"hello my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp

class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team

nico = Player("name", "blue")
nico.say_hello()

class Dog:
    def woof(self):
        print("woof woof")

class Beagle(Dog):
    def woof(self):
        super().woof()
        print("super woof")