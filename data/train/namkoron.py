import shutil
import os
from glob import glob
import pandas as pd

# datapath = "/media/shakir/01D8D4802772B180/projects/BLELocalization/data/train/"
# rname_path = "/media/shakir/01D8D4802772B180/projects/BLELocalization/data/train/renamed"

# files = glob(rname_path + "*.csv")

# for f in files:
#     num = int(os.path.basename(f)[:-4])
#     if num < 57:
#         print("{} copied to ------> {}".format(os.path.basename(f), "{}.csv".format(num+8)))
#         shutil.copy(f, os.path.join(rname_path, "{}.csv".format(num+8)))
#     else:
#         print("{} copied to ------> {}".format(os.path.basename(f), "{}.csv".format(num-56)))
#         shutil.copy(f, os.path.join(rname_path, "{}.csv".format(num-56)))

d = 0.6175

df = pd.DataFrame(['position', 'x', 'y', 'z'])
cnt = 0

for i in range(8):
    for j in range(8):
        cnt += 1
        info = {'position': [cnt], 'x': [j*d], 'y': [i*d], 'z': [0.6025]}
        print(pd.DataFrame(info))
        df = pd.concat([df, pd.DataFrame(info)], ignore_index = True)

df.to_csv('labels.csv', index=False)