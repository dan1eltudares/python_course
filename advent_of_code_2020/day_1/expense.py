# Python code to read expense_report.txt file
expense_list = []
with open('expense_report.txt') as expense_report:
    for number in expense_report:
        expense_list.append(number)

for x in expense_list:
    for y in expense_list:
        for z in expense_list:
            if int(x) + int(y) + int(z) == 2020:
                print(x,y,z)
                print(int(x) * int(y) * int(z))


