import numpy as np

# Two operands and their result
sample_and = ["000", "010", "100", "111"]
sample_or = ["000", "011", "101", "111"]
sample_xor = ["000", "011", "101", "110"]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Derivative of sigmoid function
def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))


class NN:
    w1 = np.random.randn()
    w2 = np.random.randn()
    bias = np.random.randn()

    def act_func(self, a, b):
        z = self.w1 * a + self.w2 * b + self.bias
        return sigmoid(z)

    def learn(self, n, learning_rate, sample):
        rate = learning_rate
        for i in range(n):
            example = sample[np.random.randint(len(sample))]
            a = int(example[0])
            b = int(example[1])
            target = int(example[2])

            z = self.w1 * a + self.w2 * b + self.bias
            predict = sigmoid(z)

            # Derivative of error
            de_dz = 2 * (predict - target) * sigmoid_p(z)

            # Partial derivatives of error
            de_dw1 = de_dz * a
            de_dw2 = de_dz * b
            de_db = de_dz

            self.w1 -= rate * de_dw1
            self.w2 -= rate * de_dw2
            self.bias -= rate * de_db

    def test(self, a, b):
        if self.act_func(a, b) >= .5:
            return 1
        else:
            return 0

    def logical_test(self, operator):
        print("0 " + operator + " 0 = " + str(self.test(0, 0)))
        print("0 " + operator + " 1 = " + str(self.test(0, 1)))
        print("1 " + operator + " 0 = " + str(self.test(1, 0)))
        print("1 " + operator + " 1 = " + str(self.test(1, 1)))

    def print_param(self):
        print("w1 = " + str(round(self.w1, 3)))
        print("w2 = " + str(round(self.w2, 3)))
        print("bias = " + str(round(self.bias, 3)))


net = NN()
print("Randomly generated parameters:")
net.print_param()
print()

net.learn(10000, .1, sample_and)

print("Testing with AND:")
net.logical_test("AND")
net.print_param()

print()

net.learn(10000, .1, sample_or)

print("Testing with OR:")
net.logical_test("OR")
net.print_param()

print()

net.learn(100000, .01, sample_xor)

print("Testing with XOR:")
net.logical_test("XOR")
net.print_param()
