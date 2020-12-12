
passport_lst = []
passport_lst2 = []
with open('passports.txt') as passports:
    for line in passports:
        value = line.split()
        passport_lst.append(value)
for i in range(len(passport_lst)):
    if len(passport_lst[i]) == 0:
            passport_lst2.append('xxx:yyy')
    else:
        for k in range(len(passport_lst[i])):
            passport_lst2.append(passport_lst[i][k])

user = 0
passport_dict = {}
passport_dict[0] = {}

for t in range(len(passport_lst2)):
    if passport_lst2[t] == 'xxx:yyy':
        user += 1
        passport_dict[user] = {}
        continue
    else:
        split = passport_lst2[t].split(':')
        pass_dict = { split[0] : split[1] }
        passport_dict[user].update(pass_dict)

count = 0
for i in passport_dict.keys():
    if (len(passport_dict[i]) == 8) or (len(passport_dict[i]) == 7 and 'cid' not in passport_dict[i]):
        if int(passport_dict[i].get('byr')) >= 1920 and int(passport_dict[i].get('byr')) <= 2002:
            if int(passport_dict[i].get('iyr')) >= 2010 and int(passport_dict[i].get('iyr')) <= 2020: 
                if int(passport_dict[i].get('eyr')) >= 2020 and int(passport_dict[i].get('eyr')) <= 2030:
                    if '#' in passport_dict[i].get('hcl') and len(str(passport_dict[i].get('hcl'))) == 7:
                        if passport_dict[i].get('ecl') == 'amb' or passport_dict[i].get('ecl') == 'blu' or passport_dict[i].get('ecl') == 'brn' or passport_dict[i].get('ecl') == 'gry' or passport_dict[i].get('ecl') == 'grn' or passport_dict[i].get('ecl') == 'hzl' or passport_dict[i].get('ecl') == 'oth':
                            if len(str(passport_dict[i].get('pid'))) == 9:
                                if 'cm' in passport_dict[i].get('hgt'):
                                    replace_cm = passport_dict[i]['hgt'].replace('cm','')
                                    if int(replace_cm) >= 150 and int(replace_cm) <= 193:
                                        count += 1
                                        print(passport_dict[i])
                                elif 'in' in passport_dict[i].get('hgt'):
                                    replace_in = passport_dict[i]['hgt'].replace('in','')
                                    if int(replace_in) >= 59 and int(replace_in) <= 76:
                                        count += 1
                                        print(passport_dict[i])
print(count)
                                    







                        


        

        
        

        


