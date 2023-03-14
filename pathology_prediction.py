
import pandas as pd
import numpy as np

import os
print(os.listdir("../"))


data = pd.read_csv('train_genetic_disorders.csv')

print("Dataset size: ", data.shape)
print('\n', '**'* 50, '\n')
data.info()
print('\n', '**'* 50, '\n')
data.describe(include = 'all')



