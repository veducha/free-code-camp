import random
import copy


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

        # Create copy of contents to not alter the main object
        rm_contents = self.contents.copy()
        drawn_balls = list()

        for i in range(0, num):
            rnball = random.randrange(0, len(rm_contents))
            drawn_balls.append(rm_contents[rnball])
            rm_contents.pop(rnball)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(0, num_experiments):
        new_hat = copy.copy(hat)
        sample = new_hat.draw(num_balls_drawn)

        boo = True
        for key, value in expected_balls.items():
            boo = True and (value <= sample.count(key))

        if boo:
            count += 1

    return count / num_experiments


# h = Hat(red = 1, blue = 2, green =3)
