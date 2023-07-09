from practices.OopsDeeper.abstract.abstract_animal import Animal


class Cat(Animal):

    def make_sound(self):
        print("Making noise cat")
        print(__name__)
