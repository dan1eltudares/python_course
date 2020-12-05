seats_lts = []
with open('boarding_pass.txt') as boarding_pass:
    for board in boarding_pass:
        seats_lts.append(board)


binary = ''
id_lst = []
for i in range(len(seats_lts)):
    row_bin = ''
    seat_bin = ''
    for y in seats_lts[i]:
        if y == 'F':
            row_bin += '0' 
        elif y == 'B':
            row_bin += '1'
        elif y == 'R':
            seat_bin += '1'
        elif y == 'L':
            seat_bin += '0'
    row = int(row_bin,2)
    seat = int(seat_bin,2)
    seat_id = row * 8 + seat
    id_lst.append(seat_id)
id_lst.sort()
new_lst = [x for x in range(85,884)]
first_set = set(id_lst)
sec_set = set(new_lst)
diff = (first_set - sec_set).union(sec_set - first_set)
print(diff)



        





