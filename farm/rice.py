"""
Module: rice
Defines the Rice class, a specific type of Crop with additional actions like transplanting.
"""
from farm.crop import Crop

class Rice(Crop):
    """
    Represents a Rice crop, child class of Crop.

    Overrides the water method and adds a transplant method for rice-specific behavior.
    """
    def water(self):
        """
        Waters the rice, increasing the grain count by 5 (same as base Crop).

        Returns:
            int: Updated grain count after watering.
        """
        self.grains = self.grains + 5
        return self.grains


    def transplant(self):
        """
        Transplants the rice, increasing the grain count by 10.

        Returns:
            int: Updated grain count after transplanting.
        """
        self.grains = self.grains + 10
        return self.grains
