from maze import Maze

class Hero:
  '''
  Represents the player's character in the maze game.

  Contains the following methods

  __init__(): Initializes the hero's starting position in the maze.
  go_up(): Moves the hero up one space in the maze.
  go_down(): Moves the hero down one space in the maze.
  go_left(): Moves the hero left one space in the maze.
  go_right(): Moves the hero right one space in the maze.
  
  '''
  def __init__(self):
    '''
    Initializes the hero's starting position in the maze.
    '''
    self.maze = Maze() #Creates an instance of the Maze class
    self.location = self.maze.search_maze('s') #Finds the starting position of the hero
    if self.location is not None: #Checks if the starting position is valid
      self.maze[self.location[0]][self.location[1]] = 'H'  #Updates the maze with the hero's position
    self.location = self.maze.search_maze('H') #Finds the updated hero's position

  def go_up(self):
    '''
    Moves the hero up one space in the maze using rows and columns and checks to see if the direction is towards a wall.
    '''
    row, col = self.location
    new_row, new_col = row - 1, col
    if 0 <= new_row < len(self.maze) and self.maze[new_row][new_col] != '*':
      self.maze[row][col] = ' '
      self.location = new_row, new_col
      self.maze[new_row][new_col] = 'H'
      return self.maze[new_row][new_col]
    return '*'

  def go_down(self):
    '''
    Moves the hero down one space in the maze using rows and columns.and checks to see if the direction is towards a wall.
    '''
    row, col = self.location 
    new_row, new_col = row + 1, col
    if 0 <= new_row < len(self.maze) and self.maze[new_row][new_col] != '*':
      self.maze[row][col] = ' '
      self.location = new_row, new_col
      self.maze[new_row][new_col] = 'H'
      return self.maze[new_row][new_col]
    return '*'

  def go_left(self):
    '''
    Moves the hero left one space in the maze using rows and columns.and checks to see if the direction is towards a wall.
    '''
    row, col = self.location 
    new_row, new_col = row, col - 1
    if 0 <= new_col < len(self.maze[0]) and self.maze[new_row][new_col] != '*':
      self.maze[row][col] = ' '
      self.location = new_row, new_col
      self.maze[new_row][new_col] = 'H'
      return self.maze[new_row][new_col]
    return '*'

  def go_right(self):
    '''
    Moves the hero right one space in the maze using rows and columns.and checks to see if the direction is towards a wall.
    '''
    row, col = self.location 
    new_row, new_col = row, col + 1
    if 0 <= new_col < len(self.maze[0]) and self.maze[new_row][new_col] != '*':
      self.maze[row][col] = ' '
      self.location = new_row, new_col
      self.maze[new_row][new_col] = 'H'
      return self.maze[new_row][new_col]
    return '*'
