import pandas as pd
import numpy as np
from tool import append_imgQuality

training=pd.DataFrame({'A':np.arange(4),'image':['1','2','3','4']}, index=['a','b','c','d'])
training = append_imgQuality('test.txt',training,' ')
training.to_csv('test.csv',index_label='item_id')


