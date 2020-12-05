

password_list = []
with open('pwd_policies.txt') as pwd_policies:
    for line in pwd_policies:
        password_list.append(line)

valid_pwd = 0

for i in range(len(password_list)):
    split_text = password_list[i].split(' ')
    number_lst = split_text[0].split('-')
    first_number = number_lst[0]
    second_number = number_lst[1]
    letter = split_text[1].replace(':','')
    password = split_text[2]
    letter_count = password.count(letter)
    if int(letter_count) >= int(first_number) and int(letter_count) <= int(second_number):
        valid_pwd += 1
    
print(valid_pwd)
    

