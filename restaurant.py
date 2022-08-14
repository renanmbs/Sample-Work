import numpy as np
import random

def choice_function():

    choices = input()

    if(choices == "1"):

        return 1

    elif(choices == "2"):

        return 2

    elif(choices == "3"):

        return 3

    elif(choices == "4"):

        return 4

    else:
        print("Please choose again! ")

        return 5


breakfast = ["Eva's Bakery","Alpha Café"]

lunch = ["Spitz","Lemon Shark Poké","Poké & Sushi Hut","Toasters", "Apollo Burger"]

dinner = ["Bambara", "The Capital Grille", "Monarca", "DP Cheesesteaks", "The Melting Pot", "Pago"]

coffee = ["The Daily Coffee", "Three Pines Coffee", "Moose City", "Ascoli Espresso"]

print("Welcome to the random restaurant picker! \n")
print("Choose your option: \n")
print(" 1 - Breakfast; \n 2 - Lunch; \n 3 - Dinner; \n 4 - Only Coffee;")

user_input = choice_function()

while(user_input == 5):
    user_input = choice_function()

if(user_input == 1):
    breakfast_choice = random.choice(breakfast)
    print("\nThe restaurant picker chooses: \n")
    print("                  ","BREAKFAST")
    print("--------------------------------------------------")
    print("                 ",breakfast_choice)
    print("--------------------------------------------------\n")

elif(user_input == 2):
    lunch_choice = random.choice(lunch)
    print("\nThe restaurant picker chooses: \n")
    print("                  ","LUNCH")
    print("--------------------------------------------------")
    print("                 ",lunch_choice)
    print("--------------------------------------------------\n")

elif(user_input == 3):
    dinner_choice = random.choice(dinner)
    print("\nThe restaurant picker chooses: \n")
    print("                  ","DINNER")
    print("--------------------------------------------------")
    print("                 ",dinner_choice)
    print("--------------------------------------------------\n") 

elif(user_input == 4):
    coffee_choice = random.choice(coffee)
    print("\nThe restaurant picker chooses: \n")
    print("                  ","COFFEE")
    print("--------------------------------------------------")
    print("                 ",coffee_choice)
    print("--------------------------------------------------\n") 





