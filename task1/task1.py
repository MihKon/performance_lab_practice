import sys


start_arg_num = 1
total_arg_len = len(sys.argv)

arr_num = int(sys.argv[start_arg_num])
interval_num = int(sys.argv[total_arg_len-1])

len_flag = arr_num > interval_num
end_of_cycle_arr = arr_num-interval_num if len_flag else 0

round_arr = [i for i in range(1, arr_num+1)]

result_path = ''
start_element = round_arr[0]
break_flag = False

while True:
    temp_arr = []
    current_index = round_arr.index(start_element)

    for i in range(interval_num):
        if current_index >= arr_num:
            current_index = 0
        temp_arr.append(round_arr[current_index])
        current_index += 1
    
    if temp_arr[interval_num-1] == round_arr[0]:
        break_flag = True
    else:
        start_element = temp_arr[interval_num-1]
        
    result_path += str(temp_arr[0])
    
    if break_flag:
        break

print(result_path)
