import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d


if __name__ == '__main__':
    # x = np.array(([[0, 10, 20, 30, 40, 50, 60, 70, 80]]))
    # x_r = np.repeat(x, [8], axis=0)
    # print(x_r.shape)
    # print(x_r)
    #
    # y = np.array(([[80, 70, 60, 50, 40, 30, 20, 10]])).T
    # y_r = np.repeat(y, [9], axis=1)
    # print(y_r.shape)
    # print(y_r)

    x=np.arange(0, 1000,1)

    y=np.arange(0, 1000,1)
    z=np.zeros((1000,1000))
    z[500,500]=1

    c = plt.pcolormesh(x, y, z, cmap='viridis', shading='gouraud')# 彩虹热力图

    plt.colorbar(c, label='AUPR')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()