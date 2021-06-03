#!/usr/bin/python3
"""Module for function definition"""
from os import stat
from sys import stdin
import json


count = 0
size = 0
n_stat = 0
stats = dict()
summary_last_10 = dict()

try:
    for line in stdin:
        count += 1
        line_ls = line.split(' ')
        status_code = line_ls[7]
        size += int(line_ls[-1])

        if status_code not in summary_last_10:
            summary_last_10[status_code] = 0
        summary_last_10[status_code] += 1

        if count % 10 == 0:
            store = {
                "size": size,
                "stats": json.dumps(summary_last_10, sort_keys=True)}
            stats[n_stat] = store
            summary_last_10 = dict()
            n_stat += 1
except KeyboardInterrupt:
    for key in stats:
        print('File size:', stats[key]['size'])
        sts = json.loads(stats[key]['stats'])
        for sts_code in sts:
            print("{}: {}".format(sts_code, sts[sts_code]))