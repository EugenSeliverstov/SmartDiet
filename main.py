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


if __name__ == '__main__':
    food = {
        "Хлеб": 300,
        "Круассан": 450,
        "Курица": 300
    }
    diet = SmartDiet()
    for title, calories in food.items():
        diet.register_food(title, calories)
    while True:
        print("Выберите еду:")
        for title in food:
            print("\t" + title)
        title = input("Название: ")
        count = int(input("Количество: "))
        diet.add_food(title, count)
        print("Суммарная калорийность: " + str(diet.calculate()))