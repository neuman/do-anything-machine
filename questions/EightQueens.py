from questions.base import Question
from models.base import Model, Integer


class ChessPiece(Model):
        def __init__(self):
            low = 0
            high = 10
            name = "Queen"
            self.extend([
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high)),
            Integer('digit', range(low, high))
            ])

class EightQueens(Question):
    """
    Implementation of the eight queens problem.  
    """

    def __init__(self):
        self.target = [2,1,7,4,0,8,2,8,9,6]
        self.model = Number()

    def __str__(self):
        return "How can eight queen pieces be placed on a chessboard so that none can attack any other in their next move?"

    def check( self , coordinates ):
        """
        Check to see if the coordinates are valid first then grade if possible.

        :param coordinates: an array of digits that address a state in the space.
        
        :returns: a coordinates object, with a grade if possible.
        """
        if coordinates == self.target:
            coordinates.warmth = 1
            

        return coordinates