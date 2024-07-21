class SmartDiet:
    def __init__(self):
        self.food = {}
        self.total_calories = 0

    def register_food(self, title, calories):
        self.food[title] = calories

    def add_food(self, title, count):
        self.total_calories += self.food[title] * count

    def calculate(self):
        return self.total_calories


from main import SmartDiet

def test_if_empty():
    diet = SmartDiet()
    assert 0 == diet.calculate()

def test_if_one():
    diet = SmartDiet()
    diet.register_food("Хлеб", 300)
    diet.add_food("Хлеб", 2)
    assert 600 == diet.calculate()

def test_if_many():
    diet = SmartDiet()
    diet.register_food("Хлеб", 300)
    diet.register_food("Круассан", 450)
    diet.register_food("Курица", 250)
    diet.add_food("Круассан", 2)
    diet.add_food("Хлеб", 1)
    assert 1200 == diet.calculate()