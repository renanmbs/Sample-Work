import numpy as np
import math

def gas_expense_calculation():

    print("How many miles away is the destination?")
    destination = int(input())

    print("How many gallons are on your tank?")
    tank_size = int(input())

    print("What is your MPG?")
    mpg = int(input())

    print("What is the price of Gas?")
    gas_price = int(input())

    calculation_tank = (tank_size * mpg)
    price_per_fill = (tank_size * gas_price)

    if(calculation_tank >= destination):
        final_gas =  math.ceil(int(price_per_fill * 2))
        print("Final Gas Expense (Both Ways): %d " % final_gas)


    else:
        tanks = (destination/calculation_tank)
        formated_tank = round(tanks, 2)
        final_gas = math.ceil(int(price_per_fill * int(formated_tank) * 2))
        print("Final Gas Expense (Both Ways): %d " % final_gas)

    return final_gas


def hotel_calculation():

    print("How much is the hotel?")
    hotel = int(input())

    return hotel

def food_calculation(day):

    print("How much will you spend a day in food?")
    food = int(input())

    food_price = ((day - 1) * food)

    return food_price

def price_per_traveler(price):
    print("How many travelers?")
    traveler = int(input())

    price_per_person = (price / traveler)
    formated_price = round(price_per_person, 2)

    print("Price per traveler: $%d" % formated_price)


print("Welcome to the trip calculator!")

print("Press 1 for Flying, Press 2 for Driving: ")
type = int(input())

if (type == 1):
    print("How much is the plane ticket?")
    plane = int(input())

elif (type == 2):
    print("Press 1 to Estimate Gas Expenses or 2 to Input Value")
    choice = int(input())

    if(choice == 1):
        gas_expense = gas_expense_calculation()

    if(choice == 2):
        print("How much will you spend on gas?")
        gas_expense = int(input())

else:
    print("Please choose the appropriate value")

print("\nHow many days in the trip?")
days = int(input())

hotel_expense = hotel_calculation()

food_expense = food_calculation(days)

print("Any extra expenses? If so, input how much will be spent")
extra_expense = int(input())


print("Calculating...")

if (type == 1):
    final_calculation = math.ceil(plane + hotel_expense + food_expense + extra_expense)
    final_per_day = math.ceil(final_calculation / days)


    print("Approximate Total Cost: $%d" % final_calculation)
    print("Approximate Cost for Each Day: $%d" % final_per_day)

    print("Press 1 if you want the price per traveler, or 2 to end")
    decision = int(input())

    if(decision == 1):
        price_per_traveler(final_calculation)
        print("Thank you for using the trip calculator!")

    if(decision == 2):
        print("Thank you for using the trip calculator!")

elif (type == 2):
    final_calculation = math.ceil(gas_expense + hotel_expense + food_expense + extra_expense)
    final_per_day = math.ceil(final_calculation / days)


    print("Approximate Total Cost: $%d" % final_calculation)
    print("Approximate Cost for Each Day: $%d" % final_per_day)

    print("Press 1 if you want the price per traveler, or 2 to end")
    decision = int(input())

    if(decision == 1):
        price_per_traveler(final_calculation)
        print("Thank you for using the trip calculator!")

    if(decision == 2):
        print("Thank you for using the trip calculator!")
