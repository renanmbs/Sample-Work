
//Import Modules
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Main function
int main(int argc ,char *argv[]){
    
    //Checking if the user knows how to use the program
    if (argc != 4) {
        printf("Usage: \n");
        printf("    ./matrixmultiplication <m_dimension> <n_dimension> <p_dimension>");
        return 0;
    }

    //Variables input by the user
    int m_dimension = atoi(argv[1]);
    int n_dimension = atoi(argv[2]);
    int p_dimension = atoi(argv[3]);

    //Creating Matrices from the user given size
    double matrix_a[m_dimension][n_dimension];
    double matrix_b[n_dimension][p_dimension];
    double matrix_result[m_dimension][p_dimension];
    
    /*MATRIX A*/
    //Asking for the person to enter values of matrix A
    printf("Enter Values for Matrix A: \n");
    //Rows of matrix A
    for (int i = 0; i < m_dimension; i++){
        //Columns of matrix A
        for (int j = 0; j < n_dimension; j++){
            //Entering the values
            printf("Enter Element A [%d][%d] : ",i,j);
            //User input
            scanf("%lf", &matrix_a[i][j]);
        }

    }
    
    /*MATRIX B*/
    //Asking for the person to enter values of matrix B
    printf("Enter Values for Matrix B: \n");
    //Rows of matrix B
    for (int i = 0; i < n_dimension; i++){
        //Columns of matrix B
        for (int j = 0; j < p_dimension; j++){
            //Entering the values
            printf("Enter Element B [%d][%d] : ",i,j);
            //User input
            scanf("%lf",&matrix_b[i][j]);
            }
    }
    
    /*RESULTING MATRIX*/
    for (int i = 0; i < m_dimension; i++){
        for (int j = 0; j < p_dimension; j++){
            //Setting the result matrix to be filled with the results
            matrix_result[i][j] = 0;
            for (int k = 0; k < n_dimension; k++){
                //Calculation
                matrix_result[i][j] =  matrix_result[i][j] + matrix_a[i][k] * matrix_b[k][j];
            }
        }
    }
    
    //Printing Result
    for (int i = 0; i < m_dimension; i++){
        printf("| ");
        for (int j = 0; j < p_dimension; j++){
            printf(" %.2f ",matrix_result[i][j]);
        }
        printf(" |\n");
    }
    

return 0;

}

