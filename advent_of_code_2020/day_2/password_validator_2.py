

password_list = []
with open('pwd_policies.txt') as pwd_policies:
    for line in pwd_policies:
        password_list.append(line)

valid_pwd = 0

for i in range(len(password_list)):
    split_text = password_list[i].split(' ')
    number_lst = split_text[0].split('-')
    first_number = int(number_lst[0])
    second_number = int(number_lst[1])
    letter = split_text[1].replace(':','')
    password = split_text[2]
#    print(password[(first_number - 1)])
    if password[(first_number - 1)] == letter and password[(second_number - 1)] != letter:
        valid_pwd += 1
    elif password[(first_number - 1)] != letter and password[(second_number - 1)] == letter:
        valid_pwd += 1
    
print(valid_pwd)
    

