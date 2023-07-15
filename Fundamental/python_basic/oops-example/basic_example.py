# TODO : OOPS

class PlayChess:
    # TODO Class Object Attributes
    membership = True

    def __init__(self, name, age):
        # if (self.membership):
        if (PlayChess.membership):
            self.name = name  # TODO: Attributes
            self.age = age  # TODO: Attributes
        else:
            print('The membership was invalidated')

    def run(self):
        print(f'The Access membership {self.membership}')
        return "done"


playChess1 = PlayChess("vamsi", 20)
playChess2 = PlayChess("sukanya", 30)

playChess2.attack = 50

print(playChess1.name)
print(playChess1.age)
print((playChess1.run()))

print(playChess2.attack)
print(playChess1.membership)

value = {'key': 'value'}
if "key" not in value:
    print(value['key'])
else:
    print(value['key'])
# TODO : OOPS

class PlayChess:
    # TODO Class Object Attributes
    membership = True

    def __init__(self, name, age):
        # if (self.membership):
        if (PlayChess.membership):
            self.name = name  # TODO: Attributes
            self.age = age  # TODO: Attributes
        else:
            print('The membership was invalidated')

    def run(self):
        print(f'The Access membership {self.membership}')
        return "done"


playChess1 = PlayChess("vamsi", 20)
playChess2 = PlayChess("sukanya", 30)

playChess2.attack = 50

print(playChess1.name)
print(playChess1.age)
print((playChess1.run()))

print(playChess2.attack)
print(playChess1.membership)

value = {'key': 'value'}
if 'key' not in value.keys():
    print(value['key'])
else:
    print("test")


