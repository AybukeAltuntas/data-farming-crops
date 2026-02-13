"""
Module: crop
Defines the base Crop class for all types of crops in the farm simulation.
This class handles basic crop operations like watering and checking ripeness.
"""


class Crop:
    """
    Base class representing a generic crop.

    Attributes:
        grains (int): Amount of grains the crop currently has. Initialized to 0.
    """
    def __init__(self):
        """
        Initializes a Crop instance with 0 grains.
        """
        self.grains = 0

    def water(self):
        """
        Waters the crop, increasing the grain count by 5.

        Returns:
            int: Updated grain count after watering.
        """
        self.grains = self.grains + 5
        return self.grains

    def ripe(self):
        """
        Checks if the crop is ripe. A crop is considered ripe if grains >= 15.

        Returns:
            bool: True if crop is ripe, False otherwise.
        """
        return self.grains >= 15
