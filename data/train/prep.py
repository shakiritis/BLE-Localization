import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import savgol_filter
import sys

# loc = sys.argv[1]

datapath = "/media/shakir/Common/BLE-Localization/data/train"

# beacon_all = pd.read_csv(os.path.join(datapath, '{}.csv'.format(loc)))
# rss_beacon = []

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff00ff', 'k']
for j in range(64):
    beacon_all = pd.read_csv(os.path.join(datapath, '{}.csv'.format(j+1)))
    rss_beacon = []
    for i in range(12):
        beacon_data = beacon_all[beacon_all['peripheral name'] == 'ble_beacon{}'.format(i+1)]
        rss = beacon_data['RSSI value [dB]'].to_numpy()
        rss_smth = savgol_filter(rss, 555, 3)
        plt.plot(rss_smth, c = colors[i], label=str(i+1) + ": {}".format(str(rss_smth.shape[0])))

    plt.legend()
    plt.savefig('{}/figs/{}.png'.format(datapath, j+1))
    plt.close()