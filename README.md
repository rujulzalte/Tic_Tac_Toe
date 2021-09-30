
# Tic_Tac_Toe
This repository consists of the source code file the well know game Tic Tac Toe.

## Getting started

This is the README file for the repository of a game known as Tic Tac Toe. If you are interested in creating simple programs using basic conditional statements and loops you can refer to this.


## Requirements

To run the game you would be needing [**Python3**](https://www.python.org/downloads/) 

	* Version 3.6.x and greater

## Instructions 

1: The game requires a user who can play it with the computer.

2: You can make your move by entering a number in between **0-8**. 

3: The number will correspond to the board position as illustrated.
    
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
	

**4: Condition of winning the game:**
	  The winner will be decided on the basis of whoever so first fill their respective sign on the board's position.
	  Three consecutive in *ROW OR COLUMN OR EITHER IN DIAGONAL*

5: PLAY WITH YOUR BEST MOVES.

## Details of the source code

This code is made on the basic logic of [python programming](https://www.python.org/) . It consists of [functions](https://www.w3schools.com/python/python_functions.asp), [if else statments](https://www.w3schools.com/python/python_conditions.asp) and [while loop](https://www.w3schools.com/python/python_while_loops.asp). Using all the concepts I have implemented the code. 

## Functions that drives the source code

1: *main_tic_tac_toe() - This is the main driver function that will drive the entire code and the flow will start from here.*

2: *restart() - This function is made so that the user can have a choice to restart the game after 1 game gets over.*

3: *win_direction() - The win_direction function is used to identify the winning condition and check from which direction the sequence occurred i.e. vertical, diagonal or horizontal. The function returns the value in form of a True or False value (i.e. boolean value). Returning true value is the sign that we have found a winner which satisfies the winning condition.*

4: *win_diagonal() - This function helps us to recognize that any diagonal is present which satisfies the winning condition. Function returns True or False value (i.e. boolean value). It shows that the winning condition is found at the diagonals of the board.* 

5: *win_horizontal() - win_horizontal is a function that can detect whether the winning condition is achieved in any of the horizontal lines of the board. Function returns True or False value (i.e. boolean value). It shows that the winning condition is found across the horizontal column of the board.*

6: *win_vertical() - This function will check the vertical rows of the board and would see if the winning condition is achieved or not. Function returns True or False value (i.e. boolean value). It shows that the winning condition is found in the rows of the board.*

7: *choose_player() - This function is created so that the user can input his/her choice and make a move on the board. It is also checking if the input is within the given range or not, if not then it shows a warning message and again asks for the valid input.*

8: *choose_computer() - This function is made so that as soon as the player makes the move then the computer will make its move and the details will be displayed on the screen.*

9: *display_board() - It is nothing but a printing function that helps the user to understand the moves which have been played by showing the matrix repression of the board. The board will look similar to the board which is mention above in the [instructions](Instructions).* 

10: *instructions() - The function shows all the basics information such as rules for the user to play the game.*

## More Resources

* [Learing python](https://www.w3schools.com/python/)
* [Installtion of python](https://www.python.org/downloads/)
* [Python coding questions](https://www.programiz.com/python-programming/examples)




###### [Created By : Rujul Zalte](https://www.linkedin.com/in/rujulzalte/)

																	
																	
