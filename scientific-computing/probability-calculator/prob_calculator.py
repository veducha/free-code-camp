import random

# import copy


class Hat:
    def __init__(self, **kwargs):
        self.ballsDict = kwargs

        # Creates a list with one color label for each ball of that color
        self.contents = list()
        for key in kwargs.keys():
            for j in range(0, kwargs[key]):
                self.contents.append(key)

    def draw(self, num):
        if len(self.contents) < num:
            return contents

        rm_contents = self.contents.copy()
        drawn_balls = list()

        for i in range(0, num):
            rnball = random.randrange(0, len(rm_contents))
            drawn_balls.append(rm_contents[rnball])
            rm_contents.pop(rnball)

        return drawn_balls
