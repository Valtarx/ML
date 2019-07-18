import numpy as np
from matplotlib import pyplot as plt

# Creating a txt-file with data
data = open("data.txt", "w")

data.write("{:<10}".format("Length:") +
           "{:<10}".format("Width:") +
           "{:<10}".format("Color:") + "\n")

# A set of flowers's colors
colors = ["blue", "red"]


# Function for writing data
def write_data(length, width, color):
    data.write("{length:<10}"
               "{width:<10}"
               "{color:<10}\n".format(length=length, width=width, color=color))


# Blue flowers parameters
min_blue_length = .5
max_blue_length = 1.5
min_blue_width = .5
max_blue_width = 1.25

# Red flowers parameters
min_red_length = 1
max_red_length = 3
min_red_width = 1
max_red_width = 1.75

# Expected value
mbl = (min_blue_length + max_blue_length) / 2
mbw = (min_blue_width + max_blue_width) / 2

mrl = (min_red_length + max_red_length) / 2
mrw = (min_red_width + max_red_width) / 2

# Creating data randomly
for i in range(1000):
    option = np.random.randint(0, 2)

    if option == 0:
        length = .35 * np.random.randn() + mbl
        width = .235 * np.random.randn() + mbw
        if length > 0 and width > 0:
            write_data(round(length, 2), round(width, 2), colors[option])
            plt.scatter(length, width, c=colors[option])
    else:
        length = 0.6 * np.random.randn() + mrl
        width = .14 * np.random.randn() + mrw
        if length > 0 and width > 0:
            write_data(round(length, 2), round(width, 2), colors[option])
            plt.scatter(length, width, c=colors[option])

plt.axis([0, 4, 0, 2])
plt.grid()
plt.show()
