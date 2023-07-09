from practices.OopsDeeper.abstract.abstract_animal import Animal


class Dog(Animal):
    def make_sound(self):
        print("created sound")
        print(__name__)
