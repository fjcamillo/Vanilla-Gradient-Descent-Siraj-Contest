import numpy as np
from functools import reduce

def model(type, x, theta):
    if type == 'linear':
        print('Model Type: Linear')
        line = np.multiply(x, theta)
        hypothesis = reduce(lambda x, y: np.add(x, y), line)
        return hypothesis

def gradient_descent(type, learning_rate, hypothesis, x, y, theta):
    if type == 'linear':
        cost = np.multiply(np.subtract(hypothesis, y), x)
        train = np.subtract(theta, np.multiply(cost, learning_rate))
        return train
        

if __name__ == '__main__':
    main()
