#!/usr/bin/env python3

import subprocess
from matplotlib import pyplot as plt

result = subprocess.run(['timew', 'month'], stdout=subprocess.PIPE)

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

plt.plot(hours_spent_list)
