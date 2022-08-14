//                      Renan Mougenot Breviglieri Silva

//                      CS 4110 - Online

//                      Assignment #3 - Part B

//                      Question 2

//                      Dr. Rague

//                      Due: 04/17/2021

//                      Version: 1.0

// -----------------------------------------------------------------------

/* This program is a class to check if the language,
 that contains N b's (N > 0, N is an integer) followed by N+1 a's,
 accepts the input strings */
 
// -----------------------------------------------------------------------



// Test Turing Machine
public class PBTwo{
    public static void main(String[] args)  {
        // Language: All words that contain N b's (N > 0, N is an integer) followed by N+1 a's.
        String[] C  =       //RULES
        {   "0,b=>B,R,1",
            "1,b=>b,R,1",
            "1,A=>A,R,1",
            "1,a=>A,L,2",
            "2,A=>A,L,2",
            "2,b=>b,L,3",
            "2,B=>B,R,4",
            "3,b=>b,L,3",
            "3,B=>B,R,0",
            "4,A=>A,R,4",
            "4,a=>A,R,5",
            "5,#=>#,R,6",
          };
        char[] ST = {'R','R','R','R','R','R','H'};      //STATES
        String inString;
        boolean accept1;
        TM TM1 = new TM(C, ST);
        if(args.length >= 1){
            // Input string is command line parameter
            inString = args[0];      // Process input string
            accept1 = TM1.processData(inString);
            System.out.println("\n Valid string?   " + accept1);

        }

    }// end main

} // end class
