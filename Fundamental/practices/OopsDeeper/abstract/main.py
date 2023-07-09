from practices.OopsDeeper.abstract.impl_animal_with_dog import Dog
from practices.OopsDeeper.abstract.impl_animal_with_cat import Cat

if __name__ == '__main__':
    my_dog_sound = Dog()
    my_dog_sound.make_sound()

    my_cat_sound = Cat()
    my_cat_sound.make_sound()
    print(__name__)
