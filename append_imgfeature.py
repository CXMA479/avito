import pandas as pd
import numpy as np
from tool import append_imgQuality


training = pd.read_csv('../data/train.csv', index_col = "item_id", parse_dates = ["activation_date"])
training = append_imgQuality('../output/train_quality.txt',training,'\t')
training.to_csv('../output/train_imgQuality.csv', index_label='item_id')
print('Proc tset...')
testing = pd.read_csv('../data/test.csv', index_col = "item_id", parse_dates = ["activation_date"])
testing = append_imgQuality('../output/test_quality.txt',testing,'\t')
testing.to_csv('../output/test_imgQuality.csv', index_label='item_id')



