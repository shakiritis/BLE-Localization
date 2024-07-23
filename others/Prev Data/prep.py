import numpy as np
import pandas as pd
import sys

point = sys.argv[1]

fp = "/home/shakir/Desktop/BLEData/"

data = pd.read_csv(fp + point + '.csv')

devices = ["BLEBeacon9_esp", "BLEBeacon10_esp", "BLEBeacon11_cc2562", "BLEBeacon12_cc2562", "BLEBeacon13", "BLEBeacon7_esp", "BLEBeacon8_esp", "BLEBeacon10_esp", "BLEBeacon14_esp", "BLErasp2", "BLErasp1", "BLErasp6"]

for dev in devices:
    count = data[data['peripheral name']==dev]
    print(dev, len(count))
    
