import numpy as np
from scipy import interpolate

# 定义原始数据点的坐标和z值
x = [0,50,100]
y = [0,50,100]
z = [[0.28,1.91,0.48],[1.14,5.49,1.44],[0.16,1.64,0.23]]

# 创建二维插值函数
interp_func = interpolate.interp2d(x, y, z, kind='cubic')

# 定义新的插值点坐标
new_x = np.linspace(0, 100, 1000)
new_y = np.linspace(0, 100, 1000)

# 使用插值函数计算新的插值点的z值
new_z = interp_func(new_x, new_y)

# 绘制结果
import matplotlib.pyplot as plt
plt.imshow(new_z, cmap='jet', extent=[0, 100, 0, 100], origin='lower')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()