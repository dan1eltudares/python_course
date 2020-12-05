seats_lts = []
with open('boarding_pass.txt') as boarding_pass:
    for board in boarding_pass:
        seats_lts.append(board)

binary = ''
highest_id = 0
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
#    print(seat_id)
    if seat_id >= highest_id:
        highest_id = seat_id
print(highest_id)



