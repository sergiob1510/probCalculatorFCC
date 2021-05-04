import copy
import random


class Hat:
    def __init__(self, **kwarg):
        contents = []
        for arg in kwarg:
            for n in range(kwarg[arg]):
                contents.append(arg)
        self.contents = contents

    def draw(self, number):
        contents = self.contents
        drawn_balls = []
        if number >= len(contents):
            return contents
        else:
            for n in range(number):
                len_contents = len(contents)
                i = random.randrange(len_contents)
                x = contents[i]
                drawn_balls.append(x)
                contents = contents[0:i] + contents[i + 1:]
        self.contents = contents
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    bad = 0
		
    for n in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        prob = experiment_hat.draw(num_balls_drawn)
        for value in expected_balls.keys():
            count = 0
            for x in range(len(prob)):
                if prob[x] == value:
                    count += 1
            if count < expected_balls[value]:
                bad += 1
                break


    return 1 - bad / num_experiments
