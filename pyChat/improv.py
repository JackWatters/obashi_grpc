"""
@author twsswt
"""

class Improv(object):
    """
    An aggregation of the artifacts necessary (clock, cast and directions) to perform a simulation.
    """

    def __init__(self, clock, cast):
        self.clock = clock
        self.cast = cast
        self.blocked = True

    def perform(self):
        self.clock.start()
        self.cast.start()
        