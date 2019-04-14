import json
from pprint import pprint
import random

def get_options():
    with open('data/options.json') as input_file:
        options = json.load(input_file)
    # pprint(options)
    
    return options

def get_ingredients():
    ingredients = []
    with open('data/ingredients.txt') as input_file:
        for line in input_file:
            ingredients.append(line.strip("\n"))
    return ingredients

def have_ingredients(option, ingredients):
    result =  all(elem in option['ingredients']  for elem in ingredients)
    if result:
        return True
    else:
        return False

def suggest_meal(options, ingredients):
    possible_meals = []
    for option in options:
        if have_ingredients(option, ingredients):
            possible_meals.append(option["name"])

    print(possible_meals)
    return random.choice(possible_meals)


def main():
    options = get_options()
    ingredients = get_ingredients()
    suggestion = suggest_meal(options, ingredients)
    print(suggestion)

if __name__ == "__main__":
    main()