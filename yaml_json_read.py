#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

with open('output.yml') as f:
	new_file = yaml.load(f)

with open('output.json') as f:
	new_list = json.load(f)

pp(new_file)
print '         '
pp(new_list)
