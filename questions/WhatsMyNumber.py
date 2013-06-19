from questions.base import Question
from models.base import Model, Integer


class Number(Model):
        def __init__(self):
            low = 0
            high = 10
            self.extend([
            Integer('digit 1', range(low, high)),
            Integer('digit 2', range(low, high)),
            Integer('digit 3', range(low, high)),
            Integer('digit 4', range(low, high)),
            Integer('digit 5', range(low, high)),
            Integer('digit 6', range(low, high)),
            Integer('digit 7', range(low, high)),
            Integer('digit 8', range(low, high)),
            Integer('digit 9', range(low, high)),
            Integer('digit 10', range(low, high))
            ])

class WhatsMyNumber(Question):
    """
    A toy problem to see if the system can guess a number.  
    """

    def __init__(self):
        self.target = [2,1,7,4,0,8,2,8,9,6]
        self.model = Number()

    def __str__(self):
        return "What's my phone number?"

    def check( self , coordinates ):
        """
        Check to see if the queens can attack each other.

        :param coordinates: an array of digits that address a state in the space.
        
        :returns: a coordinates object, with a grade if possible.
        """
        if coordinates == self.target:
            coordinates.warmth = 1
            

        return coordinates