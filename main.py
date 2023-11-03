# 使用seaborn绘制热力图
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 假设你有以下四个点的x、y和z值
x = [-10, -5, 5, 10]
y = [-10, -5, 5, 10]
z = [1, 2, 3, 4]

# 将点转换为一个二维数组，其中每个元素代表对应位置的z值
# 如果某个位置没有点，则用np.nan填充
Z = np.full((21, 21), np.nan) # 创建一个21*21的空数组，因为x和y的范围是-10到10，共21个值
for i in range(len(x)):
    # 将x和y的值映射到数组的索引，注意要加上10，因为数组的索引从0开始
    ix = x[i] + 10
    iy = y[i] + 10
    # 将z的值赋给对应位置的元素
    Z[iy][ix] = z[i]

# 绘制热力图
sns.heatmap(Z, center=0, vmin=0, vmax=4)
# 添加标题
plt.title('Heatmap of z values')
# 显示图像
plt.show()
