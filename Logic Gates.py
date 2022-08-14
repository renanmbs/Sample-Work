
#Lists of Variables
A = [1,0]
B = [1,0]
C = [1,0]
D = [1,0]
E = [1,0]


#Simulation of gate NOT
def NOT(x):
    if (x == 0):
        return 1
    elif (x == 1):
        return 0

#Print format
print("  A  |  B  |  C  |  D  |  E  ||  Q  ")
print("--------------------------------------")

#Nested loops to iterate through all options of the variables
for Loop_1 in A:
    for Loop_2 in B:
        for Loop_3 in C:
            for Loop_4 in D:
                for Loop_5 in E:
                    #Calculate boolean expression
                    Q = ((Loop_1 and Loop_2) or NOT(Loop_3)) and (Loop_4 and Loop_5)
                    #print result in format
                    print(" ", Loop_1, " | ", Loop_2, " | ", Loop_3, " | ", Loop_4, " | ", Loop_5, " || ",  Q)
