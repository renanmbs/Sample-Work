
#Import needed module
import sys

#Check if the user knows how to use the program
if len(sys.argv) != 4:
    print ("Usage:")
    print ("    ", end = "")
    print("python matrixmultiplication.py <m_dimension> <n_dimension> <p_dimension>")
    quit()

#If everything is plugged in right
else:

    #Variables
    m_dimension = int(sys.argv[1])
    n_dimension = int(sys.argv[2])
    p_dimension = int(sys.argv[3])
    m_dimension2 = m_dimension
    #Initialize matrices
    matrix_a = [] # m = rows // n =  columns
    matrix_b = [] # n = rows // p = columns
    matrix_result = [] # m = rows // p = columns

    #Print stament for the user to plug the values for their matrices
    print("Enter Values for Matrix A: ")


    #Loop for rows in Matrix A
    for Loop_1 in range(m_dimension):
        #Empty list Elements of A inside list Matrix A
        elements_of_A = []
        #Loop for columns
        for Loop_2 in range(n_dimension):
            #Print format to print each element to be input
            print("Enter element A [%s]" % Loop_1, "[%s]" % Loop_2,":")
            #Add in matrix elements of A the values input
            elements_of_A.append(int(input()))
        #Add in matrix Matrix A for values of Matrix Elements of A
        matrix_a.append(elements_of_A)

    #Loop for rows in Matrix B
    for Loop_3 in range(n_dimension):
        #Empty list Elements of B inside list Matrix B
        elements_of_B = []
        #Loop for columns
        for Loop_4 in range(p_dimension):
            #Print format to print each element to be input
            print("Enter element B[%s]" % Loop_3, "[%s]" % Loop_4,":")
            #Add in matrix elements of A the values input
            elements_of_B.append(int(input()))
        #Add in matrix Matrix A for values of Matrix Elements of A
        matrix_b.append(elements_of_B)

    #Set the length to iterate for results (removing extra 0)
    length_of_matrix_b = len(matrix_b)-1

    #Calculate Results

    #list Elements of Result that iterates through the matrices to calculate
    elements_of_result = [[0 for Inner_Loop_1 in range(length_of_matrix_b)] for Inner_Loop_2 in range(len(matrix_a))]

    #Loop through values of Matrix A
    for Loop_4 in range(len(matrix_a)):
        #Loop starting at the first value of Matrix B
        for Loop_5 in range(len(matrix_b[0])):
            #Loop through values of Matrix B
            for Loop_6 in range(len(matrix_b)):

                #Calculation of matrix multiplication and saved on Matrix Elements of Results
                elements_of_result[Loop_4][Loop_5] += matrix_a[Loop_4][Loop_6] * matrix_b[Loop_6][Loop_5]
    #Add the elements to the main Matrix Result
    matrix_result.append(elements_of_result)


    #Pring format
    for Loop_Print in range(m_dimension):
        print("|", end = " ")
        for Loop_Print_2 in range(p_dimension):
            print(" %f " % matrix_result[0][Loop_Print][Loop_Print_2], end = "")
        print(" |")
