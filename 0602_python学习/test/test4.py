#求众数
import numpy as np

nums = [1,2,3,4,4,6,9,7,6,6]
counts = np.bincount(nums)
mode = np.argmax(counts) #返回众数
print(mode)