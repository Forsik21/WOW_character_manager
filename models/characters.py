class Character():
    def __init__(self, name):
        self.name = name
        self.lvl = 1
        self.hp = 0

    def show_info(self):
        print(self.name)
        print(self.lvl)
        print(self.hp)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.stats()

    def stats(self):
        self.based_hp = 151
        self.based_atk = 30
        self.based_armor = 8
        self.hp = self.based_hp

    def attack(self, target):
        target.hp -=  self.based_atk - target.based_armor
