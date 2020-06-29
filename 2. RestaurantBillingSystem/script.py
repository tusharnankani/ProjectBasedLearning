from food import Food
from drink import Drink
# For error handling;
import sys

food1 = Food('Sandwich', 50, 330)
food2 = Food('Chocolate Cake', 40, 450)
food3 = Food('Cream Puff', 20, 180)

foods = [food1, food2, food3]

drink1 = Drink('Coffee', 30, 180)
drink2 = Drink('Orange Juice', 20, 350)
drink3 = Drink('Espresso', 30, 30)

drinks = [drink1, drink2, drink3]
print('--------------------')
print('Food')

for index, food in enumerate(foods):
    print(str(index) + '. ' + food.info())

print('--------------------')
print('Drinks')

for index, drink in enumerate(drinks):
    print(str(index) + '. ' + drink.info())
    index += 1
 
print('--------------------')

while(True):
    food_order = int(input('Enter food item number: '))
    
    try:
        selected_food = foods[food_order]
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Please try again!")
        continue


    drink_order = int(input('Enter drink item number: '))

    try:
        selected_drink = drinks[drink_order]
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Please try again!")
        continue

    break

# Take input from the console and assign it to the count variable
count = int(input('How many meals would you like to purchase? (10% off for 3 or more): '))

# Call the get_total_price method from selected_food and from selected_drink
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)


print('Your total is Rs. ' + str(result))

