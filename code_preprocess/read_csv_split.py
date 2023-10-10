import numpy as np
import pandas as pd
import csv


filename = '../../data/train_data.csv'

reactivity_data = []

dms_csv = open('../../data/train_data_dms.csv', 'w', newline='')
dms_writer = csv.writer(dms_csv)
twoa3_csv = open('../../data/train_data_2a3.csv', 'w', newline='')
twoa3_writer = csv.writer(twoa3_csv)

flag = 0
with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # 遍历csvreader对象的每一行内容并输出
    for row in reader:
        if flag == 0:
            # write header
            twoa3_writer.writerow(i for i in row)
            dms_writer.writerow(i for i in row)

        if row['experiment_type'] == '2A3_MaP':
            if row['signal_to_noise'] != '0':
                twoa3_writer.writerow(row[i] for i in row)
        elif row['experiment_type'] == 'DMS_MaP':
            if row['signal_to_noise'] != '0':
                dms_writer.writerow(row[i] for i in row)

        flag += 1

        # if flag == 50000:
        #     break


