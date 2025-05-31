from smiley import Smiley
import time

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=Smiley.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyebrows(self):
        """
        Draws the eyebrows feature on a smiley
        """
        eyebrows = [17, 19, 20, 22, 21, 18,]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [26, 29]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = Smiley.complexion(self)
            self.pixels[pixel] = eyes

    def blink(self, delay=0.25):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()