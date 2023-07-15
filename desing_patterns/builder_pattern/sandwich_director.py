from practices.desing_patterns.builder_pattern.sandwich_builder import SandwichBuilder


class SandwichDirectory:
    builder: SandwichBuilder

    def __init__(self, builder):
        self.builder = builder

    def build_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_result()

