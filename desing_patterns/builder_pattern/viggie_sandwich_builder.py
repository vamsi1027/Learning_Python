from practices.desing_patterns.builder_pattern.sandwich_builder import SandwichBuilder


class VeggieSandwichBuilder(SandwichBuilder):

    def add_bread(self):
        self.sandwich.add_ingredient("Sweet brand..")

    def add_filling(self):
        self.sandwich.add_ingredient("Tomato")
        self.sandwich.add_ingredient("Cucumber")
