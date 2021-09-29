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

####################################################
# function [data_room, flag_finish, potential_list] = uniquely_fill(data_room)
# uniquely fill the table
# if flag_finish==0, we need potential_list to find 
def uniquely_fill(data_room):
    flag_changed = 1
    flag_finish = 1
    while(flag_changed==1):
        flag_changed = 0 # if still unfinish in this loop, this flag will be reset
        flag_finish = 1
        # bulid the potential list
        potential_list = list()
        for i in range(0,9):
            potential_list_onerow = list()
            for j in range(0,9):
                if (data_room[i][j] != 0): # there is a number in this space
                    potential_list_onedata= list() # append an empty list
                else:
                    flag_finish = 0 # haven't finish yet
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

    # output, if flag_finish==0, we need potential_list to find 
    return data_room, flag_finish, potential_list

####################################################
# function [least_potential, x_of_least_potential, y_of_least_potential] = multi_solution_indicate(data_room,potential_list)
# indicate how many solutions there are, and the space that routes to multiple solutions 
def multi_solution_indicate(data_room,potential_list):
    least_potential = 10
    x_of_least_potential = list()
    y_of_least_potential = list()
    for i in range(0,9):
        for j in range(0,9):
            if (data_room[i][j] == 0):
                len_potent = len(potential_list[i][j])
                if (len_potent < least_potential):
                    least_potential = len_potent
    for i in range(0,9):
        for j in range(0,9):
            if (data_room[i][j] == 0):
                len_potent = len(potential_list[i][j])
                if (len_potent == least_potential):
                    least_potential = len_potent
                    x_of_least_potential.append(i)
                    y_of_least_potential.append(j)
    return least_potential,x_of_least_potential,y_of_least_potential
    
####################################################
# function bool = is_potential_list_empty(potential_list)
# check if a potential_list is empty
def is_potential_list_empty(potential_list):
    max_len_potent = 0
    for i in range(0,9):
        for j in range(0,9):
            len_potent = len(potential_list[i][j])
            if (len_potent>max_len_potent):
                max_len_potent = len_potent
    if (max_len_potent == 0):
        return True
    else:
        return False

####################################################
# function bool = check_sudoku(data_room)
# perform after unique_fill() with is_finish==True
# to check the result is valid
def check_sudoku(data_room):
    flag_valid = True
    for i in range(0,9):
        sum_data = 0
        for j in range(0,9):
            sum_data = sum_data + data_room[i][j]
        if (sum_data!=45):
            flag_valid = False
    for j in range(0,9):
        sum_data = 0
        for i in range(0,9):
            sum_data = sum_data + data_room[i][j]
        if (sum_data!=45):
            flag_valid = False
    return flag_valid

# read data and create main room for data
input_data = list()
for i in range(0,9):
    str_read = input()
    input_data.append(str_read)

Data_room = list() 
for i in range(0,9):
    one_row = list()
    for j in range(0,9):
        one_row.append(int(input_data[i][j]))
    Data_room.append(one_row)

[Data_room, is_finish, potential_table] = uniquely_fill(Data_room)
if ((is_finish == 1) and (check_sudoku(Data_room))):
    for i in range(0,9):
        print(Data_room[i])
    print()
else:    # may be multiple solution
    [least_potential, x_list, y_list] = multi_solution_indicate(Data_room,potential_table)
    for test in range(0,len(x_list)):
        for n in potential_table[x_list[test]][y_list[test]]:
            Data_room_try = list()
            for i in range(0,9):
                Data_room_try_oneRow = list()
                for j in range(0,9):
                    Data_room_try_oneRow.append(Data_room[i][j])
                Data_room_try.append(Data_room_try_oneRow)
            Data_room_try[x_list[test]][y_list[test]] = n
            [Data_room_result, is_finish, potential_table_2nd] = uniquely_fill(Data_room_try)
            if ((is_finish == 1) and (check_sudoku(Data_room_result))):
                for print_index in range(0,9):
                    print(Data_room_result[print_index])
                print()
                for i in range(0,9):
                    for j in range(0,9):
                        try:
                            potential_table[i][j].remove(Data_room_result[i][j])
                        except ValueError:
                            pass
