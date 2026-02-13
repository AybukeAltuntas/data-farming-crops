# pylint: disable=too-few-public-methods


class Crop:

    def __init__(self):
        self.grains = 0

    def water(self):
        self.grains = self.grains + 5
        return self.grains

    def ripe(self):
        return self.grains >= 15
