#!/usr/bin/env python

import yaml 
import json

my_list = range(5)
my_list.append({})
my_list[-1]['vendor'] = 'juniper'
my_list[-1]['ip_addr'] = '10.65.56.100'

with open('output.yml', 'w') as f:
	f.write (yaml.dump(my_list, default_flow_style=False))

with open('output.json', 'a') as f:
	json.dump(my_list, f)

#print yaml.dump(my_list, default_flow_style=False)

