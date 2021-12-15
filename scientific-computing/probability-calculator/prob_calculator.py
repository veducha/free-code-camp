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

    def __str__(self):
        return str(self.contents)

    def draw(self, num):
        if len(self.contents) < num:
            return self.contents

        drawn_balls = list()

        for i in range(0, num):
            rnball = random.randrange(0, len(self.contents))
            drawn_balls.append(self.contents[rnball])
            self.contents.pop(rnball)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(0, num_experiments):
        new_hat = copy.deepcopy(hat)
        sample = new_hat.draw(num_balls_drawn)

        boo = True

        for key in expected_balls.keys():
            event = expected_balls[key] <= sample.count(key)
            boo = boo and event

        if boo:
            count += 1

    return count / num_experiments
