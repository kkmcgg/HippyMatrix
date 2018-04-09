import numpy as np
from matplotlib import pyplot as plt

colorCount = 9
aspect = 2
flag = np.zeros((colorCount,colorCount*aspect))
# x = np.ceil(np.linspace(4,0,num=5)+.5)
x = colorCount-np.arange(0,colorCount)
print x
for i in range(0,flag.shape[1]):
    flag[:,i]=x

# plt.imshow(flag, vmin = 0, vmax= colorCount, interpolation='nearest', cmap='viridis')
# plt.imshow(flag, vmin = 0, vmax= colorCount, interpolation='nearest', cmap='magma')
plt.imshow(flag, vmin = 0, vmax= colorCount, interpolation='nearest', cmap='cubehelix')
plt.show()
