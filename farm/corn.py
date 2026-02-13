"""
Module: corn
Defines the Corn class, a specific type of Crop with custom watering behavior.
"""
from farm.crop import Crop

class Corn(Crop):

    """
    Represents a Corn crop, child class of Crop.

    Overrides the water method to increase grains faster than the base Crop.
    """
    def water(self):
        """
        Waters the corn, increasing the grain count by 10 (more than base Crop).

        Returns:
            int: Updated grain count after watering.
        """
        self.grains = self.grains + 10
        return self.grains
