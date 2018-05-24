import pandas as pd
import numpy as np
from tool import append_imgQuality


training = pd.read_csv('../input/train.csv', index_col = "item_id", parse_dates = ["activation_date"])
#training=pd.DataFrame({'A':np.arange(4),'image':['1','2','3','4']}, index=['a','b','c','d'])
training = append_imgQuality('imgQuality_train.txt',training,'\t')
training.to_csv('../output/train+img.cvs')

testing = pd.read_csv('../input/test.csv', index_col = "item_id", parse_dates = ["activation_date"])
#training=pd.DataFrame({'A':np.arange(4),'image':['1','2','3','4']}, index=['a','b','c','d'])
testing = append_imgQuality('imgQuality_test.txt',testing,'\t')
testing.to_csv('../output/test+img.cvs')



