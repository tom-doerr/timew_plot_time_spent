#!/usr/bin/env python3

import subprocess
from matplotlib import pyplot as plt
import sys

SMOOTHING_FACTOR = 0.9

result = subprocess.run(['timew', 'month', '2021-01-01', '-', 'tomorrow'] + sys.argv[1:], stdout=subprocess.PIPE)

#print(str(result.stdout).split('\\\n'))
hours_spent_list = []
for e in str(result.stdout).split('\\n')[2:-8]:
    extracted_content = e.split(" ")[-1]
    if extracted_content == '':
        hours_spent = 0
    else:
        time_split = [int(e) for e in extracted_content.split(':')]
        hours_spent = time_split[0] + time_split[1] / 60

    print("hours_spent:", hours_spent)
    hours_spent_list.append(hours_spent)
    #print(e)

hours_spent_list_smoothed = []
smoothed_val = hours_spent_list[0] 
for e in hours_spent_list:
    smoothed_val = SMOOTHING_FACTOR * smoothed_val + (1 - SMOOTHING_FACTOR) * e
    hours_spent_list_smoothed.append(smoothed_val)


#plt.plot(hours_spent_list)
plt.plot(hours_spent_list_smoothed)
plt.show()
