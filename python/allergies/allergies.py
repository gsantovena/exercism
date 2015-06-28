class Allergies:

    items = (
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats",
    )

    def __init__(self, score):
        self.score = score
        self.list = [x for x in self.items if self.is_allergic_to(x)]

    def is_allergic_to(self, item):
        return not 1 << self.items.index(item) & self.score == 0

