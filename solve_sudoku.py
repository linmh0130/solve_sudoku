# solve Sudoku by LMH
# this program can solve Sudoku problem with only one solution
# input should be 9 rows without any space in each row
# the number need to be filled should be 0 when inputing
# e.g.:
# 072100500
# 030020409
# 580047100
# 026700950
# 043065010
# 057000643
# 004971020
# 210386090
# 000000360

# the output will be
# [4, 7, 2, 1, 9, 3, 5, 8, 6]
# [6, 3, 1, 5, 2, 8, 4, 7, 9]
# [5, 8, 9, 6, 4, 7, 1, 3, 2]
# [1, 2, 6, 7, 3, 4, 9, 5, 8]
# [9, 4, 3, 8, 6, 5, 2, 1, 7]
# [8, 5, 7, 2, 1, 9, 6, 4, 3]
# [3, 6, 4, 9, 7, 1, 8, 2, 5]
# [2, 1, 5, 3, 8, 6, 7, 9, 4]
# [7, 9, 8, 4, 5, 2, 3, 6, 1]

# read data and create main room for data
input_data = list()
for i in range(0,9):
    str_read = input()
    input_data.append(str_read)

data_room = list() 
for i in range(0,9):
    one_row = list()
    for j in range(0,9):
        one_row.append(int(input_data[i][j]))
    data_room.append(one_row)

flag_changed = 1
n_iterations = 0
while(flag_changed==1):
    flag_changed = 0 # if still unfinish in this loop, this flag will be reset
    # bulid the potential list
    potential_list = list()
    for i in range(0,9):
        potential_list_onerow = list()
        for j in range(0,9):
            if (data_room[i][j] != 0): # there is a number in this space
                potential_list_onedata= list() # append an empty list
            else:
                # delete the impotential number
                potential_list_onedata = list([1,2,3,4,5,6,7,8,9])
                for num in range(1,10):
                    for k in range(0,9):
                        if (data_room[k][j] == num):
                            try:
                                potential_list_onedata.remove(num)
                            except ValueError:
                                pass
                        if (data_room[i][k] == num):
                            try:
                                potential_list_onedata.remove(num)
                            except ValueError:
                                pass
                        start_square_row = int(i/3)*3
                        start_square_column = int(j/3)*3
                    for k_row in range(start_square_row,start_square_row+3):
                        for k_column in range(start_square_column,start_square_column+3):
                            if (data_room[k_row][k_column] == num):
                                try:
                                    potential_list_onedata.remove(num)
                                except ValueError:
                                    pass
            potential_list_onerow.append(potential_list_onedata)
        potential_list.append(potential_list_onerow)

    # only one number is potential in a space
    for i in range(0,9):
        for j in range(0,9):
            if(len(potential_list[i][j])==1): 
                data_room[i][j] = potential_list[i][j][0]
                flag_changed = 1

    for num in range(1,10):
        # in a row, one number can only appear in one space
        for i in range(0,9):
            counts_appear_in_potential = 0
            fill_index_j = -1
            for j in range(0,9):
                if (potential_list[i][j].count(num) == 1):
                    counts_appear_in_potential = counts_appear_in_potential + 1
                    fill_index_j = j
            if (counts_appear_in_potential == 1):
                data_room[i][fill_index_j] = num
                flag_changed = 1

        # in a column, one number can only appear in one space
        for j in range(0,9):
            counts_appear_in_potential = 0
            fill_index_i = -1
            for i in range(0,9):
                if (potential_list[i][j].count(num) == 1):
                    counts_appear_in_potential = counts_appear_in_potential + 1
                    fill_index_i = i
            if (counts_appear_in_potential == 1):
                data_room[fill_index_i][j] = num
                flag_changed = 1
    
        # in a square, one number can only appear in one space, to do

# output results
for i in range(0,9):
    print(data_room[i])
