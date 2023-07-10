class MyGem():
    current = 0

    def __init__(self, first, last):
        print("I'm init..........")
        self.first = first
        self.last = last

    def __iter__(self):
        print("I'm iter...........")
        return self

    def __next__(self):
        print("I'm next.............")
        if MyGem.current < self.last:
            num = MyGem.current
            MyGem.current += 1
            return num
        raise StopIteration

    def generator(self, value):
        print(value)

    def another_generator(self, value):
        self.generator()




new_Gne = MyGem(0, 10)
for i in new_Gne:
    print(i)
new_Gne.another_generator(3)
