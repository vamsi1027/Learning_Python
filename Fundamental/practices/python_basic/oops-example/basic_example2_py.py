# TODO : __init__

class Player:
    # TODO : Default parameters we are using
    def __init__(self, name='vamsi', age=0):
        print("Creating self  ...")
        self.vamsi = None
        if age > 10:
            self.name = name
            self.age = age

    def create_data(self):
        self.vamsi = "vamsi"
        print("Creating data...")

    def run(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_value(cls, num1, num2):
        print("Adding value class method")
        return cls('harish', num1 + num2)

    @staticmethod
    def sun_value(num1, num2):
        print("Adding value static class method")
        return num1 - num2

# player = Player()
#player = Player("vamsi", 10)

#print(player.run())

player = Player.adding_value(2,3)

#print(player.name)

#print(Player.adding_value(2,3))
#print(Player.sun_value(2,4))
