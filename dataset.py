import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

import numpy as np
import matplotlib.pyplot as plt


def true_function(x):
    '''
    >>> true_function(0)
    0.0
    '''
    return np.sin(np.pi * x * 0.8)


def draw():
    x = np.arange(-1.0,1.1,0.01)
    y = np.sin(np.pi * x * 0.8)

    fig = plt.figure()
    plt.plot(x,y,label="true_function")
    plt.legend()
    fig.savefig("ex1.1.png")
    plt.show()


draw()

if __name__ == '__main__':
    import doctest
    doctest.testmod()