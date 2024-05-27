import random

class Maze:
  '''
  Represents the Maze in the game 

  Contains the following methods:
  
  __init__(): Initializes the maze with walls and empty spaces.
  __str__(): Returns a string representation of the maze.
  search_maze(ch): Returns the location of a character in the maze.
  __getitem__(): Returns the character at a specific location in the maze.
  __len__(): Returns the number of rows in the maze.
  __new__(): Creates a new instance of the Maze class.
  
  '''
  
  _instance = None #Stores the instance of the Maze class
  _initialized = False #Stores a boolean value indicating whether the maze has been initialized
  def __new__(cls):
    '''
    Creates a new instance of the Maze class.
    '''
    if cls._instance is None: #Checks if the instance is None
      cls._instance = super().__new__(cls) #Creates a new instance of the Maze class
    return cls._instance

  def __init__(self):
    if not Maze._initialized: #Checks if the maze has been initialized
      with open('minomaze.txt', 'r') as file:#Opens the file that contains the maze
        self.maze = [list(line.strip()) for line in file] #Reads the file and creates a list of lists
        Maze._initialized = True 


  def __getitem__(self,row):
    '''
    Returns the character at a specific location in the maze.
    '''
    return self.maze[row] 

  def __len__(self):
    '''
    Returns the number of rows in the maze.
    '''
    return len(self.maze) 

  def __str__(self):
    '''
    Returns a string representation of the maze.
    '''
    return str(self.maze) 

  def search_maze(self, ch):
    '''
    Returns the location of a character in the maze by searching through the maze.
    '''
    for i in range(len(self.maze)):
      for j in range(len(self.maze[i])):
        if self.maze[i][j] == ch:
          self.row = i
          self.col = j
          return i, j
    
    

