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
    food_names = []
    for food in spicy_foods:
        if isinstance(food, str):  
            food_names.append(food) 
        elif isinstance(food, dict) and 'name' in food:  
            food_names.append(food['name'])  
    return food_names


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if isinstance(food, dict) and 'heat_level' in food and food['heat_level'] > 5:
            spiciest_foods.append(food)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level_emoji = "🌶" * spicy_food["heat_level"]
        print(f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {heat_level_emoji}')


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
    return None


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(spicy_food["heat_level"] for spicy_food in spicy_foods)
    spicy_foods_num = len(spicy_foods)

    if spicy_foods_num == 0:
        return 0
    return total_heat // spicy_foods_num

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
   



