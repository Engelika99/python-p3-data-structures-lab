spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food ["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
   for food in spicy_foods:
        if food["cuisine"] == "American":
            return food
       
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get("heat_level", 0) for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods > 0:
        average_heat_level = total_heat_level / num_foods
        return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food = []

    for food in spicy_foods:
        new_spicy_food.append(food)

    new_spicy_food.append(spicy_food)

    return new_spicy_food