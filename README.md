# SPDA Coursework Part I - Dots and Boxes

Repository link: https://github.com/carloseplural/DotsAndBoxes

## Overview

This project was made on Python using Object Oriented Programming and only using modules present in the Python Standard Library.
There are two files, **main.py** where the game is run and which contains the cell inputs, menus and selections, and **classes.py** which defines the board, rules, player interactions etc.

## Code Description

There are two files in this project:

```
main.py
classes.py
```

and two modules from the Python Standard Library were used:

```
ast
random
```

### main.py

This file contains the main structure of the game. Loops for each game mode and turns, most of error handling and inputs.


The program starts with a menu and a prompt to select the game mode, in this menu the user can select *Player vs Player* (two human players), *Player vs PC (easy)* ("random" computer), *Player vs PC (less easy)* ("smart" computer) and *Player vs PC (synchronous)*. It will then ask to enter a board size x by y in tuple form (min x, y = 3), e.g 4,5. After the parameters for the game are chosen the first player, 'A' or 'B', will be chosen at random (except for synchronous mode) (In player vs computer modes the human player is always 'A' and computer 'B').

Once these options are chosen the first thing to appear is an example that shows how to draw a line. It can be confusing to remember rows and columns so that reference will always be there at the top of the terminal :smiley:. Directly below the example, the gameboard and scoreboard will be displayed when the game starts.  

Depending on the mode selected, one of four loops will then start. They are very similar in structure and run in the following order:

  1. Outer loop for the reset option.
      - Restarts/breaks depending on the user input "Y"/"N".
      - After each reset the first player will be chosen at random.
  2. First inner loop for maximum number of lines drawn.
      - Itself contains two loops, one for each player.
      - Broken when the board is full
  3. Second inner loop for each turn.
      - First it handles errors for each cell (value, syntax, type, index).
      - And then looks at both cells in conjunction to check them against the rules.
  4. Once Rules are checked, saves each inputed cell and goes back to the first inner loop.
  5. Draws a line and checks if the cell fills a box (in case the current player is human).
      - If the player is the computer, the move is already validated in the function.
      - If a box is filled, sets the turn counter to repeat the current turn (giving the player a free turn)
  6. Displays a new updated board and increases play count by one.
      - Given a board syze (x,y) the maximum number of plays for each game is max = [2 * (x * y) - x - y].
  7. Checks if the board is full and in case it isn't it goes to the next turn.
  8. This will repeat until the board is full
  9. The winner (or tie) will be displayed.
  10. The reset prompt will appear, in which the player can choose "Y" or "N".

### classes.py

This file contains the classes used to run the game and they include the functions that govern all the player-board interactions.

There are two main classes, 'Board' and 'Player'. From the 'Player class' there are three inhereted classes, 'Human' 'Synchronous' and 'Computer'. And finally two more inherited classes from Computer, 'Random_Computer' and 'Smart_Computer'.

In the **'Board'** class we find the following functions:

*General*
- **create_Board** - Generates the board
- **display_Board** - Displays the board on the terminal
- **example** - Displays a line drawn on a 4x4 box as reference
- **get_score** - Prints the score for both players

*Rules*
- **cells_are_empty** - Checks if the line has already been drawn
- **cells_are_adjacenet** - Checks if both the cells selected are vertically or horizontally adjacent. 
- **cells_are_different** - Checks if the player has selected two different cells.
- **check_rules** - A function to check whether all the play follows are the rules.
    - It is cleaner to write a function that checks all the rules, instead of writting 3 functions each time.

*Game/board management*
- **check_box** - After each play, this function checks if the line draw has completed a box on each potential side - up, down, left and right.
    - I assumed this would be more efficient to check the closest boxes rather than interating through the whole board after each play.
- **fill_box** - If the 'check_box' function returns True, this function will be called. This fills the box with the player letter A, B or S (synchronous mode). If a player draws a box, the function will also increase their score by 1 or by 0.5 (if in synchronous mode the player and computer draw the same side).
- **count_play** - This function adds 1 to the variable 'self.play_count' each time a successful play is logged. This is set to 0 at the start of each game.
- **board_is_full** - Checks if the board is full. For any board size x,y the maximum number of lines z drawn is z = [2 * (x * y) - x - y]. When the variable self.play_count is equal to z the game ends.
    - This is a more efficient way to check rather than iterate through the intire board each time a line is drawn. 
- **get_winner** - Displays the result when the game reaches the end, winner or tie.
- **reset_game** - Once called returns true to continue the loop or false to break it, depending on the user input. This resets the game with the same parameters (board size and mode), and the first player will be selected at random.

All **Player** classes are used to input each move into the board. There is only one function per class. The functions are:

*Human*
- **move_player** - Takes the input from the user, transforms it and draws a line on the board.

*Synchronous*
- **move_synchronous** - Takes the input from the user and draws the line on the board. On the same function, the 'computer' selects an optimal (highest possible points) and valid play, and draws a line on the board.
    - As player and pc play at the same time, it makes sense to put them in the same function. As the whole function has to stop in case there is an error, e.g when for example the player and computer choose the same side of the box and that line does not fill a box.

*Random_Computer*
- **move_computer** - Creates a list of possible plays and selects a valid combination of cells at random using the random module.

*Smart_Computer*
- **move_computer** - Creates a list of possible and valid plays, from this list it creates another list with the highest point yielding plays indexed at the start. Picks the first combination of cells from the latter list.
  
## Dots and Boxes

> Dots and Boxes is a pencil-and-paper game for two players (sometimes more). It was first published in the 19th century by French mathematician Édouard Lucas, who called it la pipopipette. It has gone by many other names, including the dots and dashes, game of dots, dot to dot grid, boxes, and pigs in a pen

> The game starts with an empty grid of dots. Usually two players take turns adding a single horizontal or vertical line between two unjoined adjacent dots. A player who completes the fourth side of a 1×1 box earns one point and takes another turn. A point is typically recorded by placing a mark that identifies the player in the box, such as an initial. The game ends when no more lines can be placed. The winner is the player with the most points. The board may be of any size grid.
> -- <cite>[wikipedia][1]</cite>

[1]: https://en.wikipedia.org/wiki/Dots_and_Boxes

## Rules

There are 3 simple rules to this game:

1. Two different cells must be chosen to draw a line.
2. A line can only be drawn between two vertically or two horizontally adjacent cells.
3. A line cannot be drawn if it has already been drawn before.

The game will end when there are no more lines left to draw.

The player with most points wins. 

In case the points are the same, the game results in a tie.

## Run the game
1. **Run the main.py file**

2. **Select mode**

  + 'Player vs Player' - human vs human

  + 'Player vs PC (easy)' - human vs random computer

  + 'Player vs PC (less easy)' - human vs smart computer

  + 'Player vs PC (synchronous)' - human vs smart computer synchronous
   
![image](https://user-images.githubusercontent.com/48217684/208267248-faad96d7-51ab-4c9d-beea-a20a205bf733.png)

**3. Select the board size x by y**

  + Must be written as "x,y", **with** the comma.
  + x: Number of rows
  + y: Number of columns
  + The minimum number of rows and columns is 3.
  
![image](https://user-images.githubusercontent.com/48217684/208267620-a938884b-86ec-41b9-87be-3a8479beb188.png)

**4. See example**

  - This example shows how to draw a line on the board

![image](https://user-images.githubusercontent.com/48217684/208267904-f0adcf43-e68c-4fd4-a475-e0f138d0b19e.png)

**5. Play the game!** 
 
 *Player vs Player, Player vs PC (easy), Player vs PC (less easy)*
 
  - Each player enters two cells until they fill a box.
  - Whoever completes a box gets a free turn and receives 1 point.
  - After each turn the score will be updated and the board will be displayed

  ![image](https://user-images.githubusercontent.com/48217684/208268298-54fd25b8-fbfc-46db-bb99-74674af129ec.png)
  
   *Player vs Player (synchronous)*
   
   - The human player is asked to enter two cells.
   - The computer will select it's move, based on points potential .
   - If both pick the same cells and it **DOES** fill a box, the point will be split between players (0.5 each) and an "S" will be shown in the centre of the box.
   
  ![image](https://user-images.githubusercontent.com/48217684/208269083-c4758536-c8c8-47ff-a1a2-eefe5c995d29.png)
  
   - If both pick the same cells and it **DOES NOT** fill a box, the play restarts and both have to choose again.

  *All modes*

  - The game will continue until there are no moves left.
  - The final score and winner will be displayed at the end.

  ![image](https://user-images.githubusercontent.com/48217684/208268611-3fe1c993-84a8-4f30-bb2d-3743c931999f.png)
  
  - After the game ends you can reset the game by selecting the option "Y"
      - Selecting "Y" will restart the game with the same board size and in the same mode.
  - To stop running the game select "N".



