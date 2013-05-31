class Question( object ):
    """
    Human language description of the question goes here in as much detail as seems relevant. 
    """

    model = None

    def __str__(self):
        return "Question With No Name"

    def check(self, coordinates):
        """
        Check to see if the coordinates are valid first then grade if possible.

        :param coordinates: an array of digits that address a state in the space.
        
        :returns: a grade if possible.
        """
        raise NotImplementedError( "Should have implemented this" )

    def ask(self):
        pass