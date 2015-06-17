class Allergies:

    items = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, score):
        self.score = score
        self.list = [x for x in self.items if self.is_allergic_to(x)]

    def is_allergic_to(self, item):
        return not self.items[item] & self.score == 0

