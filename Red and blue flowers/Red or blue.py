import numpy as np
from matplotlib import pyplot as plt

bias = np.random.randn()


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))


class Flower:
    def __init__(self, length, width, color=None):
        self.length = length
        self.width = width
        self.color = color

    def act_func(self):
        arg = self.length * weight[0] + self.width * weight[1] + bias
        return sigmoid(arg)

    def print_flower(self):
        print("{length:<10}"
              "{width:<10}"
              "{color:<10}\n".format(length=self.length, width=self.width, color=self.color))

    def set_color(self):
        if self.act_func() >= .5:
            self.color = colors[1]
        else:
            self.color = colors[0]


colors = ["blue", "red"]

weight = [np.random.rand() for i in range(2)]


source = open("data.txt", "r")

data = []

for line in source.readlines():
    data.append(line.split())

data.pop(0)

flowers = []

for flower in data:
    flowers.append(Flower(float(flower[0]), float(flower[1]), flower[2]))

for point in flowers:
    plt.scatter(point.length, point.width, c=point.color)

# Learning
for i in range(1000):
    costs = []
    learning_rate = 0.1
    for flower in flowers:
        if flower.color == "red":
            target = 1
        else:
            target = 0
        z = flower.length * weight[0] + flower.width * weight[1] + bias
        model = flower.act_func()
        cost = np.square(model - target)

        dcost_dz = 2 * (model - target) * sigmoid_p(z)  # Derivative of cost function

        dz_dw1 = flower.length
        dz_dw2 = flower.width
        dz_db = 1

        dcost_dw1 = dcost_dz * dz_dw1
        dcost_dw2 = dcost_dz * dz_dw2
        dcost_db = dcost_dz * dz_db

        weight[0] -= learning_rate * dcost_dw1
        weight[1] -= learning_rate * dcost_dw2
        bias -= learning_rate * dcost_db

for w in weight:
    print(w)

print(str(bias) + "\n")

for f in flowers:
    f.set_color()
    f.print_flower()

print()

test = []

for i in range(25):
    length = np.random.uniform(0.5, 3)
    width = np.random.uniform(0.5, 1.75)
    f = Flower(round(length, 2), round(width, 2))
    f.set_color()
    plt.scatter(f.length, f.width, c=f.color, linewidths=2, edgecolors="black")
    test.append(f)
    test[i].print_flower()

plt.axis([0, 4, 0, 2])
plt.grid()
plt.show()
