import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

fp = "/media/shakir/01D8D4802772B180/projects/BLELocalization/"

pos = sys.argv[1]
plot  = int(sys.argv[2])

data = pd.read_csv(fp + pos + ".csv")

for i in range(12):
    beacon = data[data['peripheral name']=="ble_beacon{}".format(i+1)]
    print("Position {}: ".format(i+1), len(beacon))

    if plot == 1:
        rssi = beacon['RSSI value [dB]']
        plt.plot(rssi, label = 'ble_beacon{}'.format(i+1))
        plt.legend()
plt.show()

