import maze 
import hero
import random

class Minotaur:
  '''
  Represents the Minotaur in the maze game.

  Contains the following methods:

  __init__(): Initializes the minotaur's starting position in the maze.
  move_minotaur(): Moves the minotaur randomly until it reaches the hero's location.
  '''
  
  def __init__(self):
    
    '''
    Initializes the minotaur's starting position in the maze.
    '''
    self.maze = maze.Maze() #Creates an instance of the Maze class
    self.location = random.choice([(i, j) for i in range(len(self.maze)) for j in range(len(self.maze[i])) if self.maze[i][j] == ' ']) #Selects a random location in the maze that is empty
    self.maze[self.location[0]][self.location[1]] = 'M' #Updates the maze with the minotaur's position

    

  def move_minotaur(self): 
    '''
    Moves the minotaur randomly until it reaches the hero's location.
    '''
    
    hero_location = hero.Hero().location #Gets the location of the hero
    row, col = self.location #Gets the row and column of the minotaur
    new_row, new_col = row, col #Initializes the new row and column to the current row and column

    if hero_location[0] < row and self.maze[new_row - 1][new_col] != '*' and self.maze[new_row - 1][new_col] != 'f':
      new_row -= 1
    elif hero_location[0] > row and self.maze[new_row + 1][new_col] != '*' and self.maze[new_row + 1][new_col] != 'f':
      new_row += 1
    elif hero_location[1] < col and self.maze[new_row][new_col - 1] != '*' and self.maze[new_row][new_col - 1] != 'f':
      new_col -= 1
    elif hero_location[1] > col and self.maze[new_row][new_col + 1] != '*' and self.maze[new_row][new_col + 1] != 'f':
      new_col += 1
        
    self.maze[row][col] = ' '
    captured_char = self.maze[new_row][new_col]
    self.maze[new_row][new_col] = 'M'
    self.location = new_row, new_col
    return captured_char
    