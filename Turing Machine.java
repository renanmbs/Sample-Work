//                      Renan Mougenot Breviglieri Silva

//                      CS 4110 - Online

//                      Assignment #3 - Part A

//                      Dr. Rague

//                      Due: 04/17/2021

//                      Version: 1.0

// -----------------------------------------------------------------------

/* This program is a class to check if the turing machines implemented
 accept the word according to the language */

// -----------------------------------------------------------------------




// -----------------------------------------------------------------------
// This class represents is the declaration of variables for the TM class
// Version 1.0
// -----------------------------------------------------------------------
public class TM {
    String[] code;
    char[] stateType; //Type of State
    String tape; //Declaration of tape
    int tapePos; //Position of the tape
    int cstate; //State of C


    // -----------------------------------------------------------------------
    // This class gives the parameters for the TM class
    // Version 1.0
    // -----------------------------------------------------------------------
    public TM(String[]c, char[] ST){
        this.code = c;
        this.stateType = ST;
        cstate = 0;
        tape = "#";
        tapePos = 0;
    }

    // -----------------------------------------------------------------------
    // This class sets the state of the turing machine
    // Version 1.0
    // -----------------------------------------------------------------------
    public void setState(int cstate){
        this.cstate = cstate;
    }

    // -----------------------------------------------------------------------
    // This class gets the state of the turing machine
    // Version 1.0
    // -----------------------------------------------------------------------
    public int getState(){
        return cstate;
    }

    // -----------------------------------------------------------------------
    // This class sets the tape
    // Version 1.0
    // -----------------------------------------------------------------------
    public void setTape(String tape){
        this.tape = tape;
    }

    // -----------------------------------------------------------------------
    // This class processes the data accordingly to the states
    // Version 1.0
    // -----------------------------------------------------------------------
 public boolean processData(String str) {
        tape = str + "#";
        while (stateType[cstate] == 'R') { //R is for reject state
            stateTransistion(tape.charAt(tapePos));
        }
        if (stateType[cstate] == 'H') //H is for halt state
            return true;
       else
            return false;
    }

    // -----------------------------------------------------------------------
    // This class represents the state transitions
    // Version 1.0
    // -----------------------------------------------------------------------
    public void stateTransistion(char ch) {
        boolean stateTransistionStatus = false;
        boolean Reject = false;
        for (String c : code) {         //ITERATING THROUGH DIFFERENT INSTRUCTIONS
            if (cstate == Integer.parseInt(c.substring(0,1)) && c.charAt(2) == ch) {
                tape = tape.substring(0, tapePos) + c.charAt(5)+ tape.substring(tapePos+1);
                if (c.charAt(7) == 'L') {
                    if (tapePos - 1 == -1)
                        System.out.println("Machine Crashed");
                    else
                        tapePos--;
                } else
                    tapePos++;
                cstate = Integer.parseInt(c.substring(c.length() - 1));
                stateTransistionStatus = true;
                return;
            }
        }
        if (!stateTransistionStatus)
            System.out.println("\n Valid string?   " + Reject);
    }

    // -----------------------------------------------------------------------
    // This class is the main class
    // Version 1.0
    // -----------------------------------------------------------------------
    public static void main(String[]args){

    }
}
