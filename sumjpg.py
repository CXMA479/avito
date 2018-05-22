import os

root_dir='train_split'

dir_list = os.listdir(root_dir)
jpg_cnt=0
for direc in dir_list:
    jpg_cnt += len(  os.listdir( os.path.join(root_dir, direc) ) )

print(jpg_cnt)



