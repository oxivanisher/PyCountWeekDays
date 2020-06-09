#!/usr/bin/env python

import yaml
import numpy as np

with open(r'config.yml') as file:
    cfg = yaml.load(file, Loader=yaml.FullLoader)

day_count = np.busday_count(np.datetime64('today', 'D'), cfg['target_date'], weekmask=cfg['days_to_count'])
print("Counting days %s until %s: %s" % (cfg['days_to_count'], cfg['target_date'], day_count))
