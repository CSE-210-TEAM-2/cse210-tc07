from typing import Text


class Word:
    def __init__(self):
        """
        Class constructor
        Attributes: move_word, points

        """

    def move_word(self):
        """
        Displays word and moves it across the screen. Boolean which evaluates to
        True when on the screen and False when off
        """
        self.move_word = self.text
        return self.velocity


    def points(self):
        """
        Calculates points. If user typed word, points are the sum of the 
        total letters in the word. If typed incorrectly, player receives 0 points.
        """
        if self.word == input:
            self.points = sum(len(self.word))
        else:
            self.points = 0 
    

