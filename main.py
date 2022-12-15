# main class for whatToEat will ask for a users input on what food items are currently available, compare that
# array to the attributes of various meals and return the meals that could be made with the currently available
# food items.

def main():
    # meal_type = input("Breakfast, Lunch, or Dinner? ")
    food_items_input = input("What is currently available to you? ")
    food_items = food_items_input.split(", ")
    return_list = []

    # BREAKFAST FOODS #

    # Bagels
    bec = Food("Breakfast", "Bacon Egg and Cheese", ["bacon", "cheese", "eggs", "bagel"])
    ec_bagel = Food("Breakfast", "Egg and Cheese Bagel", ["cheese", "eggs", "bagel"])
    egg_bagel = Food("Breakfast", "Egg Bagel", ["eggs", "bagel"])
    bagel_creamch = Food("Breakfast", "Bagel with Cream Cheese", ["bagel", "cream cheese"])
    bagel_butter = Food("Breakfast", "Bagel with Butter", ["bagel", "butter"])

    # misc.
    eggs_bacon = Food("Breakfast", "Eggs and Bacon", ["bacon", 'eggs'])
    cheese_quesadilla = Food("Breakfast", "Cheese Quesadilla", ["tortilla", "cheese"])
    butter_toast = Food("Breakfast", "Buttered Toast", ["butter", "bread"])
    toast = Food("Breakfast", "Toast", ["bread"])
    eggs_toast = Food("Breakfast", "Eggs and Toast", ["bread", 'eggs'])
    eggs_b_toast = Food("Breakfast", "Eggs and Buttered Toast", ["bread", "eggs"])
    eggs_bac_toast = Food("Breakfast", "Eggs, Bacon, and Toast", ["bread", "eggs", "bacon"])
    eggs_bac_b_toast = Food("Breakfast", "Eggs, Bacon, and Buttered Toast", ["bread", "butter", "eggs", "bacon"])

    breakfast_meals = [bec, eggs_bacon, cheese_quesadilla, ec_bagel, egg_bagel, bagel_creamch, bagel_butter,
                       butter_toast, toast, eggs_toast, eggs_b_toast, eggs_bac_toast, eggs_bac_b_toast]

    # if meal_type == "Breakfast":
    for meal in breakfast_meals:
        if Food.compare_ingr(meal, food_items, meal.ingredients):
            return_list.append(meal.meal_name)

    print(return_list)


class Food:
    meal_time = ""
    meal_name = ""
    ingredients = [""]

    def __init__(self, meal_time, meal_name, ingredients):
        self.meal_time = meal_time
        self.meal_name = meal_name
        self.ingredients = ingredients

    def compare_ingr(self, food_items, ingredients):
        for ingr in ingredients:  # goes through the ingredients required for the meal one at a time
            counter = 1
            for food in food_items:  # compares req. ingredient to entire input list
                if ingr == food:  # if the req. ingredient matches the current input food item
                    break  # break inner for and move onto next req. ingredient
                elif counter >= len(food_items):  # if the req ingredient does not match the current input food item and there are no more input food items, it is not on the list
                    return False  # return false, as it cannot be made
                else:  # if the req. ingredient does not match the current input food item
                    counter = counter + 1  # pass and move onto next input food item
        return True  # if all req ingredients exist on the input list, the food can be made


if __name__ == "__main__":
    main()
