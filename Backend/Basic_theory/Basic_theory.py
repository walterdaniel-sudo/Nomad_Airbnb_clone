# class Human:
#     def __init__(self, name):
#         print("human initialized")
#         self.name = name
        
#     def say_hello(self):
#         print(f"hello my name is {self.name}")

# class Player(Human):
#     def __init__(self, name, xp):
#         super().__init__(name)
#         self.xp = xp

# class Fan(Human):
#     def __init__(self, name, fav_team):
#         super().__init__(name)
#         self.fav_team = fav_team

#     def my_fav_team(self):
#         print(f"Name={self.name}/Fav_team={self.fav_team}")

# nico = Player("nico", "blue")
# nico.say_hello()
# daniel = Fan("daniel", "토트넘")
# daniel.my_fav_team()

# class Dog:
#     def woof(self):
#         print("woof woof")

# class Beagle(Dog):
#     def woof(self):
#         super().woof()
#         print("super woof")

# beagle = Beagle()
# beagle.woof()

# Underscore Underscore method
# dir = dir은 클래스의 속성과 메소드를 보여준다.
# Python standard library 참고
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print(super().__str__())
        return f"Dog: {self.name}"
    def __getattribute__(self, name):
        print(f"they want to get {name}")
        return "😂"

jia = Dog("jia")
print(jia.name)