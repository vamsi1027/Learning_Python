class User(object):
    def __init__(self, email):
        self.email = email

    def sing_in(self):
        print('Logging in')


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power
    def attack(self):
     print(f'Attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'Attack with arrow of {self.arrow}')

        # isinstance(object, className)


wizard = Wizard('vamsi', 23, "vamsi@motivity")
archer = Archer('hm', "arrow")

wizard.attack()
archer.attack()

print(isinstance(wizard, Wizard))
print(wizard.email)

for char in [wizard, archer]:
    char.attack()


def player_attache(char):
    char.attack()


player_attache(wizard)
player_attache(archer)
