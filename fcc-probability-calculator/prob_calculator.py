import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **keywords):
        contenido = []
        for x in keywords:
            for y in range(keywords[x]):
                contenido.append(str(x))

        self.contents = contenido

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        newContents = []
        count = len(self.contents)
        for x in range(num_balls_drawn):
            ram = random.randint(0, count - 1)
            newContents.append(self.contents.pop(ram))
            count = count - 1
        return newContents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_array = []
    count = 0
    for x in expected_balls:
        expected_array.append([x, expected_balls[x]])
    for x in range(num_experiments):
        check = 0
        hat2 = copy.deepcopy(hat)
        draw_balls = hat2.draw(num_balls_drawn)
        for y in expected_array:
            if draw_balls.count(y[0]) < y[1]:
                check = 1
        if check > 0:
            count += 1
    return 1 - (count / num_experiments)
