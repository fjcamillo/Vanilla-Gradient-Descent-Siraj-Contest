import numpy as np
from functools import reduce

def model(type, x, theta):
    if type == 'linear':
        print('Model Type: Linear')
        line = np.multiply(x, theta)
        hypothesis = reduce(lambda x, y: np.add(x, y), line)
        return hypothesis

if __name__ == '__main__':
    main()
