import numpy as np
import pandas as pd
import csv


filename = '../../data/train_data.csv'

reactivity_data = []

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # 遍历csvreader对象的每一行内容并输出
    flag = 0
    for row in reader:
        flag += 1
        if flag % 1000 == 0:
            print(flag, end='   ')
            print(len(row['sequence']), end='  ')
            print(row['experiment_type'])

    print(flag)
