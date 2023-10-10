import numpy as np
import pandas as pd
import csv


filename = '../../data/train_data.csv'

reactivity_data = []

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # 遍历csvreader对象的每一行内容并输出
    for row in reader:
        for data in row:
            if data[0:11] == 'reactivity_' and data[0:12] != 'reactivity_e':
                if row[data] == '':
                    reactivity_data.append(-1000)
                else:
                    reactivity_data.append(float(row[data]))
        print(np.array(reactivity_data))
        x = len(reactivity_data) - sum(np.array(reactivity_data) == -1000)
        print(len(reactivity_data))
        print(np.array(reactivity_data) == -1000)
        reactivity_data = []
            # if data == 'sequence':
                # str0 = row[data]
                # print(len(str0))

