import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_excel("C:/Users/01din/Desktop/rand.xlsx")

arr = np.zeros((1,1000))
for i in range(0,1000):
    arr[i] = df.iloc[i]

plt.hist(arr)
plt.show()