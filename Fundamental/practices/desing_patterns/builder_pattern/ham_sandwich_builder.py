from practices.desing_patterns.builder_pattern.sandwich_builder import SandwichBuilder


class HamSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredient("White bread...", )

    def add_filling(self):
        self.sandwich.add_ingredient("Cheese")
        self.sandwich.add_ingredient("Mayonnaise")
