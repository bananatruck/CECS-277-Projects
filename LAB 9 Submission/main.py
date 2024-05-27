#Lab 9
#Keshav Jindal
#4/10/24
#This program is a maze game
import hero 
import maze
import minotaur 



'''A Maze Game where the player explores to find the exit and avoid the Minotaur'''

def main():
  '''Function that runs the game'''
  
  maze_instance = maze.Maze() #Introduces an intance of the maze class
  hero_instance = hero.Hero() #Starts an instance of the hero class
  minotaur_instance = minotaur.Minotaur() #Creates an instance of the Minotaur class
  play = True
    
  while play:
    #Prints the maze and the hero's location
    for row in maze_instance:
      print(''.join(row))
    direction = input('Choose a direction(WASD): ')
    direction = direction.upper()
    while(direction !='W' and direction !='A' and direction != 'S' and direction != 'D'):
      direction = input('Choose a direction(WASD): ')
      direction = direction.upper()
      #Checks if the direction is valid


    if direction == 'W':
      hero_instance.go_up() 
    elif direction == 'A':
      hero_instance.go_left()

    elif direction == 'S':
      hero_instance.go_down()

    elif direction == 'D':
      hero_instance.go_right()
    

    minotaur_instance.move_minotaur()

    
    if hero_instance.location == minotaur_instance.location:
      #Checks if the hero and the minotaur are in the same location
      for row in maze_instance:
        print(''.join(row))
      print('You Lose, The Minotaur got you!')
      
      play = False
      
    if not maze_instance.search_maze('f'):
      #checks if the hero is in the finish location
      for row in maze_instance:
        print(''.join(row))
      print ('Congratulations! You reached the exit and successfully escaped the minotaur')
      
      play = False
    
main()