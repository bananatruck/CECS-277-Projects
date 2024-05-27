# player.py
from die import Die

class Player:
  """
  A class representing a player in the game of Yahtzee.

  Attributes:
  _dice (list): A list of Die objects representing the player's dice.
  _points (int): The player's current score.
  """
  definit__(self):
  """Initializes the player with three dice and zero points."""
  self._dice = [Die() for in range(3)]
  self._points = 0
  self._sort_dice()

def_sort_dice(self):
  """Sorts the dice based on their values."""
self._dice.sort()

def get_points(self):
  """Returns the player's current points."""
  return self._points

def roll_dice(self):
  """Rolls all dice and sorts them."""
  for die in self._dice:
    die.roll()
  self._sort_dice()

def has_pair(self):
  """Checks for a pair among the dice and increments points if found."""
  for i in range(len(self._dice) 1):
    if self. dice[i] == self._dice[i + 1]:
      self._points += 1
      return True
  return False

def has_three_of_a_kind(self):
  """Checks for three of a kind among the dice and increments points if found."""
  if self._dice[0] == self._dice[1] == self._dice[2]:
    self._points += 3
    return True
  return False

def has_series(self):
# We should compare the values of the dice, not the dice objects themselves.
  if (self._dice[0]._value + 1 = self._dice[1]._value):
  (self._dice[1].value + 1 == self._dice[2]._value):
  self._points += 2
  return True
return False

def str_(self):

  """returns a sting representation of the player's dice and points."""
  return f"D1={self._dice[0].value}, D2={self._dice[1]} D3={self._dice[2].value}"