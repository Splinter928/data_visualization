from random import choice


class RandomWalk:
    """class for random walk generation"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # every walk starts in (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Computing all points of walk"""
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # NULL steps aborting
            if x_step == 0 and y_step == 0:
                continue

            # calculation of the next coordinates values
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        # step length and direction definition
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
