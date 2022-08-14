/**************************************************
*Renan Mougenot Breviglieri Silva
*RockPaperScissor.java
*This program serves for object programming rock, paper, scissors
***************************************************/
import java.util.Random;
import javax.swing.JOptionPane;


public class RockPaperScissor {

   //Tells person to enter its guess
	public String getUserChoice() {
		String choice;
		choice=JOptionPane.showInputDialog("Enter rock, scissors or paper");
		
      //Invalid input 
		while (!(choice.equalsIgnoreCase("Rock") || choice.equalsIgnoreCase("Paper")
				|| choice.equalsIgnoreCase("Scissors"))) {
			JOptionPane.showMessageDialog(null, "Sorry, wrong input");
			choice=JOptionPane.showInputDialog("Enter rock, scissors or paper");
		}
		return choice;
	}

	public String getCPUChoice() {
		//get random number
		Random rand = new Random();
		int x = rand.nextInt(3);

      //Get result from number and choose rock, paper or scissors for computer
		if (x == 0)
			return "Rock";
		else if (x == 1)
			return "Paper";
		else
			return "Scissors";
	}
   //Result of the game 1
	public String pickWinner(String userChoice, String cpuChoice) {
		if(userChoice.equalsIgnoreCase("Rock")){
			if(cpuChoice.equalsIgnoreCase("Paper"))
				return "Computer";
			else if(cpuChoice.equalsIgnoreCase("Scissors"))
				return "User";
			else
				return "Tie";
		}
      //Result of the game 2
		else if(userChoice.equalsIgnoreCase("Paper")){
			if(cpuChoice.equalsIgnoreCase("Rock"))
				return "User";
			else if(cpuChoice.equalsIgnoreCase("Scissors"))
				return "Computer";
			else
				return "Tie";
		}
      //Result of the game 3
		else{
			if(cpuChoice.equalsIgnoreCase("Rock"))
				return "Computer";
			else if(cpuChoice.equalsIgnoreCase("Paper"))
				return "User";
			else
				return "Tie";
		}
	}

}
