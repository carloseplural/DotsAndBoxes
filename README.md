# SPDA Coursework Part I - Dots and Boxes

## Summary
This game was made on Python using Object Oriented Programming and using only modules present in the Python Standard Library.
There are two files, main.py where the game is run and which contains the inputs, menus and selections, and classes.py which defines the board, rules, player interactions etc.

## Dots and Boxes

> Dots and Boxes is a pencil-and-paper game for two players (sometimes more). It was first published in the 19th century by French mathematician Édouard Lucas, who called it la pipopipette. It has gone by many other names, including the dots and dashes, game of dots, dot to dot grid, boxes, and pigs in a pen

> The game starts with an empty grid of dots. Usually two players take turns adding a single horizontal or vertical line between two unjoined adjacent dots. A player who completes the fourth side of a 1×1 box earns one point and takes another turn. A point is typically recorded by placing a mark that identifies the player in the box, such as an initial. The game ends when no more lines can be placed. The winner is the player with the most points. The board may be of any size grid.
> -- <cite>[wikipedia][1]</cite>

[1]: https://en.wikipedia.org/wiki/Dots_and_Boxes

## Rules

There are 3 simple rules to this game:

1. Two different points must be chosen to draw a line.
2. A line can only be drawn between two vertically or horizontally adjacent points.
3. A line cannot be drawn if it was already drawn before.

## Files
There are two files necessary to run the game:
```bash
main.py
classes.py
```

## Modules
```bash
random
ast
```

## Run the game
1. **Run the main.py file**

2. **Select mode**

  + Player vs Player
    - Human vs Human. Each player makes a move manually.
    - There are two players, "A" and "B". Both players choose which one they are beforehand.
    - First to play is picked at random
  
  + Player vs PC (easy)
    - Human player is player "A", and computer is "B". The first to start is chosen randomly. 
    - Computer picks a random but valid play each turn.

  + Player vs PC (less easy)
    - Human player is player "A", and computer is "B". The first to start is chosen randomly. 
    - Computer picks the highest point yielding play, if there isn't one then picks a random but valid play.
  
  + Player vs PC (synchronous)
    - Human player and computer play *symultaneously*.
    - Human player is player "A", and computer is "B".
    - The computer move is generated first and tries to get the most points per move.
   
![image](https://user-images.githubusercontent.com/48217684/208267248-faad96d7-51ab-4c9d-beea-a20a205bf733.png)

**3. Select the board size x by y**

  + Must be written as "x,y", **with** the comma.
  + x: Number of rows
  + y: Number of columns
  + The minimum number of rows and columns is 3.
  
![image](https://user-images.githubusercontent.com/48217684/208267620-a938884b-86ec-41b9-87be-3a8479beb188.png)

**4. See example**

  - Player will be prompt to select the first cell as "x,y". Example: 0,1
  - Then the second cell as "x,y". Example: 0,2
  - If both cells respect the rules, a line will be drawn linking the two points:

![image](https://user-images.githubusercontent.com/48217684/208267904-f0adcf43-e68c-4fd4-a475-e0f138d0b19e.png)

**5. Play the game!** 
 
 *Player vs Player, Player vs PC (easy), Player vs PC (less easy)*
 
  - Each player enters two cells until they fill a box.
  - Whoever completes a box gets a free turn and receives 1 point.
  - After each turn the score will be updated and the board will be displayed

  ![image](https://user-images.githubusercontent.com/48217684/208268298-54fd25b8-fbfc-46db-bb99-74674af129ec.png)
  
   *Player vs Player (synchronous)*
   
   - The human player is asked to enter two cells.
   - The computer will select it's move, based on potential points.
   - If both pick the same cells and it **DOES** fill a box, the point will be split and an "S" will be shown.
   
  ![image](https://user-images.githubusercontent.com/48217684/208269083-c4758536-c8c8-47ff-a1a2-eefe5c995d29.png)
  
   - If both pick the same cells and it **DOES NOT** fill a box, the play restarts and both have to choose again.

  *All modes*

  - The game will continue until there are no moves left.
  - The final score and winner will be displayed.

  ![image](https://user-images.githubusercontent.com/48217684/208268611-3fe1c993-84a8-4f30-bb2d-3743c931999f.png)
  
  - After the game ends you can reset the game by selecting the option "Y"
      - Selecting "Y" will restart the game with the same board size and in the same mode.
  - To stop running the game select "N".





