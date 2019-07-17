import random

# Numbers for learning
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')

# List of numbers
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

# Distorted number 5 for testing
num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

test_nums = [num51, num52, num53, num54, num55, num56]

# Initialisation of weight with zeros
weights = [0 for i in range(15)]

# Limit of activation function
bias = 7


# Checking if the number is 5
def proceed(number):
    net = 0
    for i in range(15):
        net += int(number[i])*weights[i]
    return net >= bias


# If there is a mistake and the result is 1
def decrease(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] -= 1


# If there is a mistake and the result is 0
def increase(number):
    for i in range(15):
        if int(number[i]) == 1:
            weights[i] += 1


# Learning
for i in range(10000):
    option = random.randint(0, 9)

    if option != 5:
        if proceed(nums[option]):
            decrease(nums[option])
    else:
        if not proceed(num5):
            increase(num5)

# Printing the result weights
for i in range(15):
    print("w" + str(i) + " = " + str(weights[i]))

print()

# Testing the network with the numbers
for i in range(10):
    if proceed(nums[i]) != 1:
        print(str(i) + " is not 5")
    else:
        print(str(i) + " is 5")

print()

# Testing the network with distorted numbers
for i in range(6):
    if proceed(test_nums[i]) != 1:
        print(str(i) + " is not 5")
    else:
        print(str(i) + " is 5")