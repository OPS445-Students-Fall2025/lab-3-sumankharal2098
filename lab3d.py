#!/usr/bin/env python3
'''Lab 3 - run df to find free space on /'''
# Author ID: 137379236

import subprocess

def free_space():
    # runs: df -h | grep '/$' | awk '{print $4}'
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'",
                         stdout=subprocess.PIPE, shell=True)
    output = p.communicate()[0]
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
