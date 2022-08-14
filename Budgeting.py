#Importing Modules
import matplotlib.pyplot as plt
import  numpy as np

#Parameters
income = 500
gas_money = 300
groceries_money = 200

#Function to calculate gas expense
def calculation_gas(expense):

    #Parameter
    sum = 0

    #Loop through expenses
    for loop_1 in expense:
        #Sum expenses
        sum = int(sum + loop_1)
    #Check how much money is left
    money_left_gas = int(gas_money - sum)

    return money_left_gas

#Function to calculate groceries expense
def calculation_groceries(expense):

    #Parameter
    sum = 0

    #Loop through expenses
    for loop_1 in expense:
        #Sum expenses
        sum = int(sum + loop_1)
    #Check how much money is left
    money_left_groceries = int(groceries_money - sum)

    return money_left_groceries

#Function to calculate full expense
def calculation(expense_1, expense_2):

    #Parameter
    sum_1 = 0
    sum_2 = 0

    #Loop through expenses 1
    for loop_1 in expense_1:
        #Sum expenses
        sum_1 = int(sum_1 + loop_1)

    #Loop through expenses 2
    for loop_2 in expense_2:
        #Sum expenses
        sum_2 = int(sum_2 + loop_2)

    #Check how much money is left
    money_left_total = int(income - (sum_1 + sum_2))

    return money_left_total

#Getting input
print("Choices: 1 - Gas")
print("Choices: 2 - Groceries")
print("Choices: 3 - All expenses")
type = int(input(("\nEnter type of expense: ")))

#Gas
if (type == 1):
    #Number of expenses to be input
    number_of_expenses = int(input("Enter number of expenses : "))

    #Array of expenses
    print("To use: Plug in the numbers separated by a space")
    expenses = list(map(int,input("\nEnter the expenses : ").strip().split()))[:number_of_expenses]

    #Make sure the expenses are correct
    print("You said: ")
    print(expenses)

    #Check if the input is correct
    print("Choices: 1 - Yes")
    print("Choices: 2 - No")
    check = int(input(("Choice: ")))

    #Correct
    if (check == 1):
        #Calculate expenses
        result = calculation_gas(expenses)

        #Calculate the Average
        average_gas = np.average(expenses)

        #Print
        print("Money left to spend in gas: $%d" % result)
        print("Average spent in gas: $%f" % average_gas)

    #Incorrect
    else:
        print("Restart the program with the correct numbers")


#Groceries
elif (type == 2):
    #Number of expenses to be input
    number_of_expenses = int(input("Enter number of expenses : "))

    #Array of expenses
    print("To use: Plug in the numbers separated by a space")
    expenses = list(map(int,input("\nEnter the expenses : ").strip().split()))[:number_of_expenses]

    #Make sure the expenses are correct
    print("You said: ")
    print(expenses)

    #Check if the input is correct
    print("Choices: 1 - Yes")
    print("Choices: 2 - No")
    check = int(input(("Choice: ")))

    #Correct
    if (check == 1):

        #Calculate expenses
        result = calculation_groceries(expenses)

        #Calculate the Average
        average_groceries = np.average(expenses)

        #Print
        print("Money left to spend for groceries: $%d" % result)
        print("Average spent in groceries: $%f" % average_groceries)

    #Incorrect
    else:
        print("Restart the program with the correct numbers")

#Total
elif (type == 3):
    #Number of expenses to be input
    gas = int(input("Enter number of the gas expenses : "))
    #Array of expenses
    print("To use: Plug in the numbers separated by a space")
    gas_expenses = list(map(int,input("\nEnter the expenses : ").strip().split()))[:gas]

    #Number of expenses to be input
    grocery = int(input("\nEnter number of the grocery expenses : "))
    #Array of expenses
    grocery_expenses = list(map(int,input("\nEnter the expenses : ").strip().split()))[:grocery]

    #Make sure the expenses are correct
    print("You said: ")
    print(gas_expenses)
    print(grocery_expenses)

    #Check if the input is correct
    print("Choices: 1 - Yes")
    print("Choices: 2 - No")
    check = int(input(("Choice: ")))

    #Correct
    if (check == 1):
        #Calculate expenses
        result = calculation(gas_expenses,grocery_expenses)

        #Calculate the Average
        average_gas = np.average(gas_expenses)
        average_groceries = np.average(grocery_expenses)

        #Print
        print("Money left to spend: $%f" % result)
        print("Average spent in gas: $%f" % average_gas)
        print("Average spent in groceries: $%f" % average_groceries)

    #Incorrect
    else:
        print("Restart the program with the correct numbers")

else:
    print("Not a valid option")
