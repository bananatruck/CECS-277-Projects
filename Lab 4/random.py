import random


class Die:
    """Represents a single die with a number of sides and a value."""
    def init (self, sides=6):
        """Initialize the die with a number of sides and a default value of 0. """
        self. sides = sides
        self. value = self.roll()

    def roll(self):
        """Roll the die and return the value it lands on."""
        self. value = random.randint(1, self. sides)
        return self._value
    def get_value(self):
        """Return the value of the die."""
        return self._value

    def str (self):
        """Return the string representation of the die's value."""
        return str(self._value)

    def lt_(self, other):
        """Return True if this die's value is less than the other die's value."""
        return self. value < other._value

    def eq_(self, other):
        """Return True if this die's value is equal to the other die's value."""
        return self._value == other._value

        def sub (self, other):
            """Return the difference between this die's value and the other die's value."""
        return abs(self._value - other._value)