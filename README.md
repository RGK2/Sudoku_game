# Sudoku Game

This Python project is about a game called Sudoku, which consists of a 9 by 9 grid with numbers appearing in some of the squares.  
The object of the puzzle is to fill the remaining squares, using all the numbers 1–9 exactly once in each row, column, and the nine 3 × 3 sub grids. 

To run this program you have to run the main.py file in order to play the game. This Python project contains a file, sodu_solver.py, that can solve any Sudoku card with at least 27 numbers or more. It goes through each row and column, trying to find only one 
number that would fit inside one empty square and checking that it does not occur in the same row, column or sub grid twice and restarts the loop if it had found the correct
number from 1 to 9 and checks the same row or column again to see if there is another number that could be filled in before going to the next one. 

A completely random Sudoku grid will be generated using a file called, sodu_setup.py, which randomly chooses an index that is from a nested list variable that contains a list 
with 9 lists each containing 9 elements each with the value 0, representing a 9 by 9 grid. The chosen index is assigned a number from 1 to 9 and the program ensures that this 
number is authentic meaning that it does not occur twice in the same row, column and block. There will always be 28 given numbers on the grid and the rest you have to figure
out on your own. Sometimes the grid generated will have no solution, so therefore it is in a while loop constantly checking if the grid has a valid solution and if it has a
solution the loop breaks and the grid will be displayed on a Python Turtle screen. (I have added an image on the screen with some text saying "Getting Sudoku grid ready..." 
while the program is generating a valid Sudoko grid)

A Python Turtle screen will consist of randomly distributed numbers on the generated Sudoku grid. By clicking on an empty square it will require you to input a number from
1 to 9. If the number is correct the colour of the number will be green if it is not correct it will be red. The program ends when all of the corrrect numbers are filled in 
and an image will pop up saying "You have completed Sudoku grid!".