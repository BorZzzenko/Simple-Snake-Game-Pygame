from GameFieldObject import GameFieldObject


class Food(GameFieldObject):
    def __init__(self, x, y, score):
        GameFieldObject.__init__(self, x, y)
        self.__score = score

    @property
    def score(self):
        return self.__score
