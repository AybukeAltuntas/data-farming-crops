from farm.crop import Crop

class Corn(Crop):

    def water(self):
        self.grains = self.grains + 10
        return self.grains
