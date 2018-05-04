def sin_plot(xmin, xmax, step):

    import numpy as np
    x = np.arange(xmin, xmax, step)
    y = np.sin(x)
    return x, y