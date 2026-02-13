from farm.crop import Crop

class Rice(Crop):

    def water(self):
        self.grains = self.grains + 5
        return self.grains


    def transplant(self):
        self.grains = self.grains + 10
        return self.grains
