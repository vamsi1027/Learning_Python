class SandwichOrder:
    def __init__(self):
        self.ingredient = []

    def add_ingredient(self, ingredient):
        self.ingredient.append(ingredient)

    def display(self):
        print("Sandwich with the following ingredients")
        for ingredient in self.ingredients:
            print(f" %s" % ingredient)
