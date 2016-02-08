def north(position):
    position[1] += 1
    return position


def south(position):
    position[1] -= 1
    return position


def east(position):
    position[0] += 1
    return position


def west(position):
    position[0] -= 1
    return position


class Sled:
    def __init__(self):
        self.position = [0,0]
        self.richting = {"^": north,
                         "v": south,
                         "<": west,
                         ">": east,}

    def move(self, teken):
        self.position = self.richting[teken](self.position)

    def check(self):
        global counter
        if self.position not in houses:
            houses.append(list(self.position))
            counter += 1


houses = [[0,0]]
counter = 1
FILE = "input.txt"
isrobot = False
santa = Sled()
robot = Sled()
person = {False: santa, True: robot}


with open(FILE) as f:
    for teken in f.read():
        person[isrobot].move(teken)
        person[isrobot].check()
        isrobot = not isrobot
    print(counter)







