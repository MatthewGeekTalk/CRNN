import numpy as np
import os

path = os.path.abspath('./part1') + os.path.sep + 'gt.txt'
with open(path, 'r',encoder='UTF-8') as anno_file:
    # info = np.array([tmp.strip().split(',') for tmp in anno_file.readlines()])
    for tmp in anno_file.readlines():
        info = np.array(tmp.strip().split(','))
        if info[1] != 'English':
            os.remove(path + '/' + info[0])
anno_file.close()