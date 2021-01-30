# Switch Interface validator

import re

switch_interfaces = [ '1/1/1',
                      '1/1/2',
                      '1/1/3',
                      '1/1/4',
                      '1/1/5',
                      '1/1/6',
                      '1/1/7',
                      '1/1/8',
                      '1/1/9',
                      '1/z/10',
                      '1/1/11',
                      '1/1/12',
                      '1/1/13',
                      '1/1/14',
                      '1/1/151',
                      '1/1/16',
                      '1/1/17',
                      '1/1/18',
                      '1/1/19',
                      '19/1/20',
                      '1/1/x1',
                      '1/1/x2',
                      '1/1/x3',
                      '1/1/x4' ]


for i in range(len(switch_interfaces)):
    if not re.fullmatch("([0-9]\/){2}([0-9]{2}|[0-9])", switch_interfaces[i]):
        print("Interface " + switch_interfaces[i] + " is not valid")
    else:
        print("Interface " + switch_interfaces[i] + " is valid")
